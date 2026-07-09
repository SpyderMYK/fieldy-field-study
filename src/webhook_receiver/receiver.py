#!/usr/bin/env python3
"""Fieldy webhook capture receiver (RQ1/RQ3/RQ6 instrument).

Captures every incoming request verbatim — method, path, headers, body —
as one JSONL line per event, so the undocumented payload schema and
delivery/retry semantics can be characterized from raw evidence.

Stdlib only. Auth is a shared token in the URL query string, because
Fieldy webhooks have no HMAC signing (verified against their docs,
2026-07). Set FIELDY_WEBHOOK_TOKEN in the environment; requests without
a matching ?token= are rejected with 403 and logged (headers only, no
body) so unauthorized probes are still visible in the record.
"""

import base64
import json
import os
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

BIND = os.environ.get("FIELDY_BIND", "127.0.0.1")
PORT = int(os.environ.get("FIELDY_PORT", "8771"))
TOKEN = os.environ.get("FIELDY_WEBHOOK_TOKEN")
ARCHIVE_DIR = os.environ.get("FIELDY_ARCHIVE_DIR", "/tank/fieldy/raw")

MAX_BODY = 10 * 1024 * 1024  # 10 MB cap; anything bigger is suspect


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def archive_path() -> str:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return os.path.join(ARCHIVE_DIR, f"webhooks-{day}.jsonl")


def write_event(event: dict) -> None:
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(archive_path(), "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "FieldyCapture/1.0"

    def _token_ok(self) -> bool:
        qs = parse_qs(urlparse(self.path).query)
        return bool(TOKEN) and qs.get("token", [None])[0] == TOKEN

    def _respond(self, code: int, text: str) -> None:
        body = text.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _capture(self) -> None:
        authorized = self._token_ok()
        length = min(int(self.headers.get("Content-Length") or 0), MAX_BODY)
        raw = self.rfile.read(length) if (length and authorized) else b""
        try:
            body: object = raw.decode("utf-8")
            encoding = "utf-8"
        except UnicodeDecodeError:
            body = base64.b64encode(raw).decode("ascii")
            encoding = "base64"
        write_event(
            {
                "received_at": utcnow(),
                "authorized": authorized,
                "remote_addr": self.client_address[0],
                "method": self.command,
                "path": urlparse(self.path).path,
                "headers": dict(self.headers.items()),
                "body_encoding": encoding,
                "body": body,
            }
        )
        if authorized:
            self._respond(200, "ok")
        else:
            self._respond(403, "forbidden")

    def do_POST(self) -> None:  # noqa: N802 (http.server naming)
        self._capture()

    def do_GET(self) -> None:  # noqa: N802
        if self._token_ok():
            self._respond(200, "fieldy capture receiver: alive")
        else:
            self._respond(403, "forbidden")

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write(
            "%s %s %s\n" % (utcnow(), self.client_address[0], fmt % args)
        )


def main() -> None:
    if not TOKEN:
        sys.exit("FIELDY_WEBHOOK_TOKEN is not set; refusing to start open")
    server = ThreadingHTTPServer((BIND, PORT), Handler)
    print(f"{utcnow()} listening on {BIND}:{PORT}, archiving to {ARCHIVE_DIR}")
    server.serve_forever()


if __name__ == "__main__":
    main()
