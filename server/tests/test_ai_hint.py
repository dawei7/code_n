"""Tests for ``POST /api/ai/hint``.

The hint endpoint talks to a local Ollama instance. In the
test environment Ollama is not running, so the tests focus on:

  * The fallback path (Ollama unreachable → server-generated
    hint from the algorithm_hint field)
  * The prompt construction (asserts the optimal source is
    sent to Ollama, but stripped from the response)
  * The response shape (hint, model, latency_ms, fallback,
    fallback_reason)
  * The post-processor (``_strip_code_blocks``) catches
    code leaks

For tests that need a "working Ollama" stub, we monkey-patch
``_call_ollama`` directly.
"""
from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from challenges.algorithms.sorting import SORT_01_SOURCE

from server.app.routes import ai as ai_route

from . import conftest  # noqa: F401


def _make_report(challenge_id: str = "sort_01", passed: bool = True, **overrides):
    """Build a minimal AI report for tests."""
    base = {
        "challenge_id": challenge_id,
        "challenge_name": "Sort 01",
        "category": "sorting",
        "description": "Sort a list",
        "required_complexity": "O(n²)",
        "test": {"n": 8, "seed": 1},
        "user_source": SORT_01_SOURCE,
        "result": {
            "passed": passed,
            "correct": passed,
            "within_threshold": True,
            "actual_complexity": "O(n²)",
            "message": "Passed! 100 ops",
            "ops_total": 100,
            "ops_breakdown": {
                "comparisons": 50, "swaps": 30, "reads": 10,
                "writes": 10, "calls": 0,
            },
            "too_efficient": False,
            "too_efficient_reason": "",
        },
        "locals_at_failure": {
            "line_no": 5,
            "event": "line",
            "locals": {"i": 3, "j": 7},
            "return_value": "",
        },
        "algorithm_hint": "",
    }
    base.update(overrides)
    return base


class FallbackTest(conftest._Base):
    """When Ollama is down, the endpoint returns the fallback hint."""

    def test_ollama_unreachable_falls_back(self) -> None:
        # Patch _call_ollama to raise URLError.
        import urllib.error
        with patch.object(ai_route, "_call_ollama", side_effect=urllib.error.URLError("refused")):
            r = self.client.post(
                "/api/ai/hint",
                json={"report": _make_report()},
            )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertTrue(body["fallback"])
        self.assertEqual(body["model"], "fallback")
        self.assertIn("ollama_unreachable", body["fallback_reason"])
        # The hint should still be present (non-empty)
        self.assertTrue(body["hint"])

    def test_ollama_returns_junk_falls_back(self) -> None:
        # The LLM returns only code (which gets stripped to empty).
        with patch.object(ai_route, "_call_ollama", return_value="```python\nreturn [0, 1, 2]\n```"):
            r = self.client.post(
                "/api/ai/hint",
                json={"report": _make_report()},
            )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        # Either fallback (stripped to empty) or the model
        # response is just code → fallback. We assert fallback.
        self.assertTrue(body["fallback"], f"expected fallback, got: {body}")

    def test_fallback_for_failed_run(self) -> None:
        # A failed run still gets a useful fallback hint.
        report = _make_report(
            passed=False,
            **{"result": {
                "passed": False,
                "correct": False,
                "within_threshold": True,
                "actual_complexity": "O(n²)",
                "message": "Incorrect solution!",
                "ops_total": 100,
                "ops_breakdown": {"comparisons": 50, "swaps": 30, "reads": 10, "writes": 10, "calls": 0},
                "too_efficient": False,
                "too_efficient_reason": "",
            }},
        )
        import urllib.error
        with patch.object(ai_route, "_call_ollama", side_effect=urllib.error.URLError("refused")):
            r = self.client.post("/api/ai/hint", json={"report": report})
        body = r.json()
        self.assertTrue(body["fallback"])
        # The fallback should mention "Incorrect" or "match" or
        # "expected" (so the user knows what to look at).
        self.assertTrue(body["hint"])

    def test_fallback_for_too_efficient_run(self) -> None:
        report = _make_report(
            passed=False,
            **{"result": {
                "passed": False,
                "correct": True,
                "within_threshold": True,
                "actual_complexity": "O(1)",
                "message": "Solution rejected: too efficient",
                "ops_total": 1,
                "ops_breakdown": {"comparisons": 0, "swaps": 0, "reads": 0, "writes": 0, "calls": 1},
                "too_efficient": True,
                "too_efficient_reason": "suspicious",
            }},
        )
        import urllib.error
        with patch.object(ai_route, "_call_ollama", side_effect=urllib.error.URLError("refused")):
            r = self.client.post("/api/ai/hint", json={"report": report})
        body = r.json()
        self.assertTrue(body["fallback"])
        # The hint should mention efficiency or hardcoded.
        hint = body["hint"].lower()
        self.assertTrue(
            "efficient" in hint or "hardcoded" in hint or "suspicious" in hint,
            f"expected too-efficient hint, got: {body['hint']!r}",
        )

    def test_unknown_challenge_returns_404(self) -> None:
        # Even on the fallback path, the challenge must exist
        # so the server can look up its optimal source.
        report = _make_report(challenge_id="does_not_exist")
        r = self.client.post("/api/ai/hint", json={"report": report})
        self.assertEqual(r.status_code, 404)

    def test_missing_challenge_id_returns_400(self) -> None:
        report = _make_report()
        del report["challenge_id"]
        r = self.client.post("/api/ai/hint", json={"report": report})
        self.assertEqual(r.status_code, 400)


class PostProcessorTest(unittest.TestCase):
    """``_strip_code_blocks`` removes any code from the LLM response."""

    def setUp(self) -> None:
        self.optimal = "def solve(data):\n    return sorted(data)\n"

    def test_strips_python_fenced_block(self) -> None:
        text = "Try this:\n```python\ndef solve(x):\n    return x\n```\nGood luck!"
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertNotIn("def solve", out)
        self.assertIn("Try this", out)
        self.assertIn("Good luck", out)

    def test_strips_optimal_source_lines(self) -> None:
        # The LLM echoes the optimal source line.
        text = "Look at:\ndef solve(data):\n    return sorted(data)\nThat should work."
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertNotIn("def solve(data)", out)
        self.assertNotIn("return sorted(data)", out)

    def test_strips_return_keyword_line(self) -> None:
        text = "A common bug is\nreturn [0, 1, 2]\nin your code. Try fixing it."
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertNotIn("return [0, 1, 2]", out)

    def test_strips_for_keyword_line(self) -> None:
        text = "Hint:\nfor i in range(n):\n    total += 1\nHope that helps."
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertNotIn("for i in range(n):", out)

    def test_keeps_prose_hints(self) -> None:
        text = "You might want to use a loop instead of recursion here."
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertEqual(out, text)

    def test_keeps_prose_with_keyword_words(self) -> None:
        # Sentences like "If you want to iterate..." are not
        # code. The post-processor should keep them.
        text = "If you want to iterate over the list, use a for loop."
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertIn("If you want", out)
        self.assertIn("for loop", out)

    def test_empty_input_returns_empty(self) -> None:
        self.assertEqual(ai_route._strip_code_blocks("", self.optimal), "")

    def test_only_code_returns_empty(self) -> None:
        # If the LLM returned only a code block, the post-
        # processed output is empty. The endpoint uses this as
        # the signal to fall back.
        text = "```python\nreturn 42\n```"
        out = ai_route._strip_code_blocks(text, self.optimal)
        self.assertEqual(out, "")


class WorkingOllamaTest(conftest._Base):
    """A stubbed Ollama returns a clean hint; verify the shape."""

    def test_ollama_returns_prose(self) -> None:
        with patch.object(
            ai_route, "_call_ollama",
            return_value="Your loop is doing one extra pass; try a different bound.",
        ):
            r = self.client.post(
                "/api/ai/hint",
                json={"report": _make_report()},
            )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertFalse(body["fallback"])
        self.assertEqual(body["model"], ai_route._MODEL)
        self.assertIn("loop", body["hint"].lower())
        self.assertGreaterEqual(body["latency_ms"], 0)

    def test_ollama_optimal_source_stripped_from_response(self) -> None:
        # The LLM echoes the optimal source. The post-processor
        # should strip those lines.
        with patch.object(
            ai_route, "_call_ollama",
            return_value=(
                "Here's a hint.\n"
                "def solve(data):\n"
                "    return sorted(data)\n"
                "Good luck!"
            ),
        ):
            r = self.client.post(
                "/api/ai/hint",
                json={"report": _make_report()},
            )
        body = r.json()
        # The hint should NOT contain the optimal source.
        self.assertNotIn("def solve(data):", body["hint"])
        self.assertNotIn("return sorted(data)", body["hint"])
        # But the prose should remain.
        self.assertIn("Here's a hint", body["hint"])
        self.assertIn("Good luck", body["hint"])

    def test_prompt_includes_optimal_source(self) -> None:
        # The prompt sent to Ollama should include the optimal
        # source — that's how the LLM knows what "the answer"
        # is. We assert by checking the captured prompt that
        # the LLM-stub function receives.
        captured = {}

        def fake_call(prompt: str) -> str:
            captured["prompt"] = prompt
            return "Prose hint."

        with patch.object(ai_route, "_call_ollama", side_effect=fake_call):
            self.client.post("/api/ai/hint", json={"report": _make_report()})
        self.assertIn("optimal", captured["prompt"].lower())
        self.assertIn("def solve", captured["prompt"])
