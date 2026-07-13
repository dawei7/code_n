from __future__ import annotations

import asyncio
import json
import os
import sys
import unittest
from pathlib import Path

from server.app.dap_client import DAPClient


class DAPClientTcpTest(unittest.IsolatedAsyncioTestCase):
    async def test_tcp_adapter_request_response(self) -> None:
        async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
            headers: dict[str, str] = {}
            while True:
                line = await reader.readline()
                if not line:
                    return
                text = line.decode("ascii").strip()
                if not text:
                    break
                key, _, value = text.partition(":")
                headers[key.lower()] = value.strip()
            raw = await reader.readexactly(int(headers["content-length"]))
            request = json.loads(raw.decode("utf-8"))
            response = {
                "seq": 1,
                "type": "response",
                "request_seq": request["seq"],
                "command": request["command"],
                "success": True,
                "body": {"ok": True},
            }
            payload = json.dumps(response, separators=(",", ":")).encode("utf-8")
            writer.write(f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii") + payload)
            await writer.drain()

        server = await asyncio.start_server(handle_client, "127.0.0.1", 0)
        port = int(server.sockets[0].getsockname()[1])
        client = DAPClient()
        try:
            await client.start(
                sys.executable,
                ["-c", "import time; time.sleep(30)"],
                cwd=str(Path.cwd()),
                env=os.environ.copy(),
                connect_host="127.0.0.1",
                connect_port=port,
            )
            body = await client.request("initialize", {})
            self.assertEqual(body, {"ok": True})
        finally:
            await client.stop()
            server.close()
            await server.wait_closed()
