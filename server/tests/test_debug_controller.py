"""Unit tests for the DAP client (``DapClient``) and the
``DebugController`` state machine.

The real ``debugpy`` subprocess is hard to drive in a unit
test (timing, port allocation, DAP wire format details). For
the controller, we test the pure logic: how does the
``DebugState`` evolve when we feed it events? We do this by
constructing a ``DapClient`` with a fake transport that
speaks DAP on both ends.

For the integration test (start a real worker, hit a
breakpoint, step, exit), see ``test_debug_e2e.py`` (in the
``tests/`` directory, alongside the engine tests).
"""
from __future__ import annotations

import asyncio
import json
import unittest

from server.app.debug_controller import (
    DapClient,
    DebugController,
    DebugState,
    _encode_message,
    _read_message,
)


# ---------------------------------------------------------------------------
# Low-level framing
# ---------------------------------------------------------------------------


class FramingTest(unittest.TestCase):
    """The DAP wire format: Content-Length headers + JSON body."""

    def test_encode_round_trip(self) -> None:
        msg = {"seq": 1, "type": "request", "command": "initialize", "arguments": {}}
        encoded = _encode_message(msg)
        # The encoded bytes should be parseable back.
        # The framing is: "Content-Length: N\r\n\r\n{json body}"
        header_end = encoded.index(b"\r\n\r\n")
        header = encoded[:header_end].decode("ascii")
        body = encoded[header_end + 4 :]
        self.assertTrue(header.startswith("Content-Length:"))
        length = int(header.split(":", 1)[1].strip())
        self.assertEqual(length, len(body))
        self.assertEqual(json.loads(body), msg)


# ---------------------------------------------------------------------------
# DapClient: feed events through a fake stream and verify state transitions
# ---------------------------------------------------------------------------


class _FakeStream:
    """Minimal :class:`asyncio.StreamReader` / ``StreamWriter``
    substitute. We can't use a real socket in a unit test;
    instead we build a tiny shim that has the same async
    ``readline`` / ``readexactly`` / sync ``write`` / async
    ``drain`` / sync ``close`` / async ``wait_closed`` API
    the DAP client uses. Tests feed canned DAP messages
    into the inbound buffer (with ``feed``); the read
    methods yield to the event loop until data is
    available.
    """

    def __init__(self) -> None:
        self._inbound: bytes = b""
        self._outbound: list[bytes] = []
        self.closed = False

    def feed(self, message: dict) -> None:
        self._inbound += _encode_message(message)

    def write(self, data: bytes) -> None:
        self._outbound.append(data)

    async def drain(self) -> None:
        return None

    def close(self) -> None:
        self.closed = True

    async def wait_closed(self) -> None:
        return None

    def take_outbound(self) -> list[dict]:
        """Decode all messages the client has written so far."""
        out: list[dict] = []
        buf = b"".join(self._outbound)
        self._outbound.clear()
        while buf:
            header_end = buf.index(b"\r\n\r\n")
            header = buf[:header_end].decode("ascii")
            length = int(header.split(":", 1)[1].strip())
            body = buf[header_end + 4 : header_end + 4 + length]
            buf = buf[header_end + 4 + length :]
            out.append(json.loads(body))
        return out

    async def readline(self) -> bytes:
        # Yield until a newline is available. We poll the
        # inbound buffer rather than blocking on an
        # ``asyncio.Event`` so the test doesn't have to wire
        # up a waiter.
        for _ in range(200):  # ~2s at 10ms per loop
            if b"\n" in self._inbound:
                break
            await asyncio.sleep(0.01)
        if b"\n" not in self._inbound:
            return b""  # EOF
        idx = self._inbound.index(b"\n")
        line = self._inbound[: idx + 1]
        self._inbound = self._inbound[idx + 1 :]
        return line

    async def readexactly(self, n: int) -> bytes:
        for _ in range(200):  # ~2s
            if len(self._inbound) >= n:
                break
            await asyncio.sleep(0.01)
        if len(self._inbound) < n:
            raise EOFError()
        out = self._inbound[:n]
        self._inbound = self._inbound[n:]
        return out


class DapClientTest(unittest.IsolatedAsyncioTestCase):
    """The DAP client state machine, driven by fake messages."""

    async def _make_client(self) -> tuple[DapClient, _FakeStream, _FakeStream]:
        # We don't actually open a socket; we patch connect()
        # to a no-op after construction and route the
        # reader/writer through fake streams.
        client = DapClient("127.0.0.1", 0)
        fake_reader = _FakeStream()
        fake_writer = _FakeStream()
        client._reader = fake_reader  # type: ignore[assignment]
        client._writer = fake_writer  # type: ignore[assignment]
        # Start the read loop.
        asyncio.create_task(client._read_loop())
        # Yield once so the read loop can register itself.
        await asyncio.sleep(0)
        return client, fake_reader, fake_writer

    async def test_initialize_sends_request_and_receives_response(self) -> None:
        client, fake_reader, fake_writer = await self._make_client()
        # Start a request and feed the response.
        task = asyncio.create_task(client.initialize())
        await asyncio.sleep(0)  # let the read loop consume
        # The request should already be in outbound.
        sent = fake_writer.take_outbound()
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0]["command"], "initialize")
        request_seq = sent[0]["seq"]
        # Feed the response.
        fake_reader.feed({
            "seq": 2,
            "type": "response",
            "request_seq": request_seq,
            "success": True,
            "command": "initialize",
            "body": {},
        })
        # initialize() returns None on success; what we care
        # about is that the request was sent AND the response
        # was consumed without raising.
        result = await task
        self.assertIsNone(result)

    async def test_event_queue_drains_unwanted_events(self) -> None:
        client, fake_reader, _ = await self._make_client()
        # Feed some non-stopped events.
        fake_reader.feed({"seq": 10, "type": "event", "event": "output", "body": {"text": "hi"}})
        fake_reader.feed({"seq": 11, "type": "event", "event": "thread", "body": {}})
        # Now feed a stopped event; wait_for_event should
        # return it (after draining the others).
        fake_reader.feed({
            "seq": 12, "type": "event", "event": "stopped",
            "body": {"threadId": 1, "reason": "breakpoint"},
        })
        event = await client.wait_for_event("stopped", timeout=1.0)
        self.assertIsNotNone(event)
        self.assertEqual(event["body"]["reason"], "breakpoint")

    async def test_failed_response_raises(self) -> None:
        client, fake_reader, fake_writer = await self._make_client()
        task = asyncio.create_task(client.initialize())
        await asyncio.sleep(0)
        sent = fake_writer.take_outbound()
        request_seq = sent[0]["seq"]
        fake_reader.feed({
            "seq": 2, "type": "response",
            "request_seq": request_seq, "success": False,
            "command": "initialize", "message": "boom",
        })
        with self.assertRaises(Exception) as cm:
            await task
        self.assertIn("boom", str(cm.exception))


# ---------------------------------------------------------------------------
# DebugState: the small state struct used by the route layer
# ---------------------------------------------------------------------------


class DebugStateTest(unittest.TestCase):
    def test_defaults(self) -> None:
        s = DebugState()
        self.assertFalse(s.paused)
        self.assertIsNone(s.current_line)
        self.assertIsNone(s.current_frame_id)
        self.assertEqual(s.locals, [])
        self.assertEqual(s.stopped_reason, "")
