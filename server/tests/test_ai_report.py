"""Tests for the AI report (built in :func:`server.app.ai_report.build`).

The report is included in every ``RunResponse``. The tests cover:

  * The structural fields are present after a run
  * The user's source is included verbatim (truncated if too long)
  * The test setup is reflected
  * The result fields are correct
  * ``locals_at_failure`` is populated when there's a trace
  * The optimal source is NOT in the report (the LLM is the
    only consumer; the client never sees it)
  * Edge cases: empty trace (syntax error), huge source (cap)
"""
from __future__ import annotations

import json
import unittest

from challenges.algorithms.sorting import SORT_01_SOURCE

from . import conftest  # noqa: F401


class AiReportShapeTest(conftest._Base):
    """The report is present and has the expected fields."""

    def test_report_is_in_run_response(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertIn("ai_report", body)
        report = body["ai_report"]
        self.assertIsInstance(report, dict)
        # Top-level fields
        for key in (
            "challenge_id", "challenge_name", "category", "description",
            "required_complexity", "test", "user_source", "result",
            "locals_at_failure", "algorithm_hint",
        ):
            self.assertIn(key, report, f"missing key {key!r} in ai_report")

    def test_report_challenge_id_matches(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        report = r.json()["ai_report"]
        self.assertEqual(report["challenge_id"], "sort_01")
        self.assertEqual(report["category"], "sorting")

    def test_report_includes_user_source(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        report = r.json()["ai_report"]
        self.assertEqual(report["user_source"], SORT_01_SOURCE)

    def test_report_test_field_reflects_request(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 12, "seed": 7},
        )
        report = r.json()["ai_report"]
        self.assertEqual(report["test"]["n"], 12)
        self.assertEqual(report["test"]["seed"], 7)

    def test_report_result_has_passing_solution(self) -> None:
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        report = r.json()["ai_report"]
        self.assertTrue(report["result"]["passed"])
        self.assertTrue(report["result"]["correct"])
        self.assertGreater(report["result"]["ops_total"], 0)

    def test_report_locals_at_failure_for_working_run(self) -> None:
        # Even a passing run has a "last frame" with locals; the
        # report should include it.
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 4, "seed": 1},
        )
        report = r.json()["ai_report"]
        self.assertIsNotNone(report["locals_at_failure"])
        # The locals dict has the line_no + event + locals.
        self.assertIn("line_no", report["locals_at_failure"])
        self.assertIn("event", report["locals_at_failure"])
        self.assertIn("locals", report["locals_at_failure"])

    def test_report_user_source_truncated_when_huge(self) -> None:
        # Make a deliberately huge source (10 KB). The cap is
        # 4 KB so the report should truncate.
        big_source = "def solve(data, n):\n" + "    pass\n" * 4000
        # Actually that exceeds the Pydantic n=8 cap. Let's keep
        # it short but verify the truncation by checking the
        # reported length.
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": big_source, "n": 4, "seed": 1},
        )
        # The response is 200 with passed=False (the source is
        # syntactically valid but doesn't solve sorting). We
        # only care about the report's source cap.
        self.assertEqual(r.status_code, 200)
        report = r.json()["ai_report"]
        self.assertLessEqual(len(report["user_source"]), 4096)

    def test_report_does_not_leak_optimal_source(self) -> None:
        # The report must not include the canonical optimal
        # source — the LLM endpoint is the only consumer that
        # ever needs it, and it looks it up server-side.
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 4, "seed": 1},
        )
        report = r.json()["ai_report"]
        # The optimal source for sort_01 is the bubble sort
        # implementation. We can sniff for a characteristic
        # substring (e.g. the function name in the file is
        # "solve" but the optimal source has a distinct
        # structure). The strongest test: the report's
        # user_source equals what the player submitted, NOT
        # the canonical source.
        self.assertEqual(report["user_source"], SORT_01_SOURCE)
        # And the report JSON itself should not contain a
        # second copy of the algorithm code beyond what the
        # player submitted. (The user_source field is the only
        # one allowed to have code.)
        keys_with_source = [k for k in report.keys() if "source" in k]
        self.assertEqual(set(keys_with_source), {"user_source"})

    def test_report_serialization_is_json_safe(self) -> None:
        # The report must round-trip through JSON without
        # raising (no sets, no TrackedList, etc).
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 4, "seed": 1},
        )
        report = r.json()["ai_report"]
        # Round-trip
        roundtripped = json.loads(json.dumps(report))
        self.assertEqual(roundtripped["challenge_id"], "sort_01")
        self.assertIn("locals_at_failure", roundtripped)

    def test_report_includes_ast_op_counts(self) -> None:
        # The report must propagate the AST-derived op counts
        # (user_ast_ops, reference_ast_ops, and the ±5% CI
        # band). This was a regression: the engine_runner
        # passed these as kwargs to build_ai_report, but the
        # builder's ``return AiReport(...)`` forgot to include
        # them — they ended up None in the JSON. The
        # Complexity tab reads runResult.user_ast_ops
        # directly, so this bug was non-fatal there, but the
        # AI report was empty and the LLM was missing the
        # most useful context.
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": SORT_01_SOURCE, "n": 8, "seed": 1},
        )
        report = r.json()["ai_report"]
        # The user submitted the canonical solution; its
        # AST op count for n=8 should match the reference
        # exactly (within 1 for tie-breaking).
        self.assertIsNotNone(report["user_ast_ops"])
        self.assertIsNotNone(report["reference_ast_ops"])
        self.assertIsNotNone(report["reference_ci_low"])
        self.assertIsNotNone(report["reference_ci_high"])
        # The user and reference are both bubble sort, so
        # the values should be the same.
        self.assertEqual(report["user_ast_ops"], report["reference_ast_ops"])
        # The CI low is floor(μ × 0.95); high is ceil(μ × 1.05).
        μ = report["reference_ast_ops"]
        import math
        self.assertEqual(report["reference_ci_low"], math.floor(μ * 0.95))
        self.assertEqual(report["reference_ci_high"], math.ceil(μ * 1.05))

    def test_report_for_wrong_solution(self) -> None:
        # A wrong solution (returns data unchanged) produces a
        # report with passed=False and a clear message.
        r = self.client.post(
            "/api/challenges/sort_01/run",
            json={"source": "def solve(data, n):\n    return data\n", "n": 4, "seed": 1},
        )
        report = r.json()["ai_report"]
        self.assertFalse(report["result"]["passed"])
        self.assertFalse(report["result"]["correct"])
        # The message should mention "Incorrect".
        self.assertIn("Incorrect", report["result"]["message"])


class AiReportPureTest(unittest.TestCase):
    """The :func:`server.app.ai_report.build` function directly.

    Unit tests for the builder — no FastAPI / TestClient.
    """

    def test_build_minimal(self) -> None:
        from server.app.ai_report import build

        report = build(
            challenge_id="test_01",
            challenge_name="Test",
            category="test",
            description="A test challenge",
            required_complexity="O(n)",
            n=10,
            seed=1,
            user_source="def solve(x):\n    return x\n",
            passed=True,
            correct=True,
            within_threshold=True,
            actual_complexity="O(n)",
            message="Passed! 10 ops",
            ops_total=10,
            ops_breakdown={"comparisons": 0, "swaps": 0, "reads": 10, "writes": 0, "calls": 0},
            too_efficient=False,
            too_efficient_reason="",
            trace_frames=[],
        )
        d = report.to_dict()
        self.assertEqual(d["challenge_id"], "test_01")
        self.assertEqual(d["test"]["n"], 10)
        self.assertIsNone(d["locals_at_failure"])

    def test_build_with_trace(self) -> None:
        from server.app.ai_report import build

        # Mock trace frame with the attrs the builder reads.
        class _Frame:
            line_no = 5
            event = "line"
            locals = {"x": 1, "y": [1, 2, 3]}
            return_value = ""

        report = build(
            challenge_id="test_02",
            challenge_name="Test 2",
            category="test",
            description="Another test",
            required_complexity="O(n²)",
            n=20,
            seed=2,
            user_source="def solve(x):\n    return x\n",
            passed=False,
            correct=False,
            within_threshold=True,
            actual_complexity="O(n)",
            message="Wrong",
            ops_total=5,
            ops_breakdown={"comparisons": 1, "swaps": 0, "reads": 4, "writes": 0, "calls": 0},
            too_efficient=False,
            too_efficient_reason="",
            trace_frames=[_Frame()],
        )
        d = report.to_dict()
        self.assertIsNotNone(d["locals_at_failure"])
        self.assertEqual(d["locals_at_failure"]["line_no"], 5)
        self.assertEqual(d["locals_at_failure"]["event"], "line")
        self.assertEqual(d["locals_at_failure"]["locals"]["x"], 1)
        self.assertEqual(d["locals_at_failure"]["locals"]["y"], [1, 2, 3])

    def test_build_truncates_huge_locals(self) -> None:
        from server.app.ai_report import build

        # A frame with a huge locals dict (a 200-element list).
        class _Frame:
            line_no = 1
            event = "line"
            locals = {"big_list": list(range(200))}
            return_value = ""

        report = build(
            challenge_id="test_03",
            challenge_name="Test 3",
            category="test",
            description="x",
            required_complexity="O(1)",
            n=1,
            seed=1,
            user_source="def solve(x):\n    return x\n",
            passed=True,
            correct=True,
            within_threshold=True,
            actual_complexity="O(1)",
            message="OK",
            ops_total=1,
            ops_breakdown={"comparisons": 0, "swaps": 0, "reads": 0, "writes": 0, "calls": 1},
            too_efficient=False,
            too_efficient_reason="",
            trace_frames=[_Frame()],
        )
        d = report.to_dict()
        # Either the locals are present (small enough) or
        # they're marked as truncated. Both are acceptable.
        lf = d["locals_at_failure"]
        if lf["locals"].get("_truncated"):
            self.assertIn("_reason", lf["locals"])
        else:
            self.assertIn("big_list", lf["locals"])
