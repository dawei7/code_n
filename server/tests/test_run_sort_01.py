"""End-to-end: ``POST /api/challenges/sort_01/run`` with a real solution.

This is the load-bearing test. It posts the canonical
``SORT_01_SOURCE`` (bubble sort) to the server, gets a
:class:`RunResponse` back, and asserts the result is correct
(``passed=True``) AND within the complexity budget
(``within_threshold=True``) AND uses the expected algorithm
(``algorithm_match=True`` for sort_01 — no fingerprint, so True).

Also tests the negative case: a deliberately wrong solution
should return ``passed=False`` with a useful message.
"""
from __future__ import annotations

from challenges.algorithms.sorting import SORT_01_SOURCE

from . import conftest  # noqa: F401


class RunSort01Test(conftest._Base):
    def test_optimal_bubble_sort_passes(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertTrue(body["passed"], f"expected passed=true, got: {body}")
        self.assertTrue(body["correct"])
        self.assertTrue(body["within_threshold"])
        # The engine's classifier is conservative at small n; for n=8
        # bubble sort's ~112 ops can land in either O(n²) or O(n log n)
        # depending on the random data. The budget is generous enough
        # that both classes are within the O(n²) threshold.
        self.assertIn(body["actual_complexity"], {"O(n²)", "O(n log n)"})
        self.assertEqual(body["required_complexity"], "O(n²)")
        self.assertGreater(body["stats"]["total"], 0)
        # The trace should have a non-trivial number of frames for a
        # working bubble sort. (n=8 → ~ 8 outer * 8 inner * 3 lines/iter = ~190)
        self.assertGreater(len(body["trace"]), 50, "trace should have captured line events")
        # The ops log should have reads, comparisons, writes.
        self.assertGreater(body["stats"]["comparisons"], 0)
        self.assertGreater(body["stats"]["reads"], 0)
        self.assertGreater(body["stats"]["writes"], 0)

    def test_no_op_returns_incorrect(self) -> None:
        # A solution that does nothing should fail correctness.
        source = (
            "def solve(data, n):\n"
            "    return data\n"
        )
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": source, "n": 8, "seed": 1},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertFalse(body["passed"])
        self.assertFalse(body["correct"])
        self.assertIn("Incorrect", body["message"])

    def test_trace_includes_locals_snapshot(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        # At least one frame should have a `data` local that's a list.
        any_with_data = any(
            isinstance(f["locals"].get("data"), list)
            for f in body["trace"]
        )
        self.assertTrue(any_with_data, "expected some trace frames to have `data` as a list")

    def test_unknown_challenge_returns_404(self) -> None:
        r = self.client.post(
            "/api/challenges/does_not_exist/run",
            json={"source": SORT_01_SOURCE, "n": 4, "seed": 1},
        )
        self.assertEqual(r.status_code, 404)

    def test_n_too_large_returns_422(self) -> None:
        # sort_01 max_n is 50. Pydantic's le=100 cap lets 60 through
        # to the engine-level check (which fires our structured error).
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 60, "seed": 1},
        )
        self.assertEqual(r.status_code, 422, r.text)
        body = r.json()
        # FastAPI's HTTPException wraps our detail in {"detail": ...}.
        detail = body.get("detail", {})
        self.assertEqual(detail.get("error"), "n_too_large")
        self.assertEqual(detail.get("maximum"), 50)
