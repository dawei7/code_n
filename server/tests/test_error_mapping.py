"""Error-path tests: player code that crashes, infinite loops, syntax errors."""
from __future__ import annotations

from . import conftest  # noqa: F401


class ErrorMappingTest(conftest._Base):
    def test_infinite_loop_is_killed(self) -> None:
        # ``step_limit`` in the engine runner is operation_limit * 25
        # (min 10_000). An infinite loop with no ops should hit the
        # ``ExecutionStepLimitExceeded`` safety net.
        source = (
            "def solve(data, n):\n"
            "    while True:\n"
            "        pass\n"
        )
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": source, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertFalse(body["passed"])
        # The engine_runner catches it as a step-limit or as a crash
        # depending on which fires first; either way the player sees
        # a useful message.
        self.assertTrue(
            "Python steps" in body["message"] or "infinite" in body["message"].lower(),
            f"unexpected message: {body['message']!r}",
        )

    def test_syntax_error_returns_422(self) -> None:
        source = (
            "def solve(data, n):\n"
            "    return data[  # SyntaxError: unclosed bracket\n"
        )
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": source, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 422, r.text)
        body = r.json()
        self.assertEqual(body["detail"]["error"], "syntax")

    def test_missing_solve_returns_400(self) -> None:
        source = "def foo(x):\n    return x\n"
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": source, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 400, r.text)
        body = r.json()
        self.assertEqual(body["detail"]["error"], "no_solve")

    def test_player_runtime_error_surfaces(self) -> None:
        # NameError in player code should produce a passed=false
        # response (200) with the error name in the message.
        source = (
            "def solve(data, n):\n"
            "    return undefined_variable + 1\n"
        )
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": source, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertFalse(body["passed"])
        self.assertIn("NameError", body["message"])
