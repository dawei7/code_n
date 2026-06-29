"""Tests for internal CodeChef community/generated baselines."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from . import conftest  # noqa: F401
from server.app import codechef_community
from server.app.engine_runner import run_player_code
from tools import export_codechef_optimal_solutions


class _Response:
    def __init__(self, payload: dict, status_code: int = 200, text: str = ""):
        self._payload = payload
        self.status_code = status_code
        self.text = text

    def json(self) -> dict:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class _Session:
    def __init__(self):
        self.submitted_source = ""

    def get(self, url: str, **kwargs):
        if "/api/ide/" in url and "/languages/" in url:
            return _Response({
                "languages": [
                    {"id": "42", "short_name": "C++", "full_name": "C++"},
                    {"id": "116", "short_name": "PYTH 3", "full_name": "Python3"},
                ]
            })
        if "/api/ide/submit" in url:
            return _Response({"result_code": "accepted", "points": 100})
        if "/submit/BWFPF01" in url:
            return _Response({}, text='window.csrfToken = "fake-csrf";')
        raise AssertionError(f"unexpected GET {url}")

    def post(self, url: str, data=None, **kwargs):
        if "/api/ide/submit" in url:
            self.submitted_source = data["sourceCode"]
            self.submitted_headers = kwargs.get("headers") or {}
            return _Response({"upid": "123456789", "result_code": "wait"})
        raise AssertionError(f"unexpected POST {url}")


class _ExplainedSession:
    def get(self, url: str, params=None, **kwargs):
        if "/api/annotations/top" in url:
            return _Response({
                "status": "success",
                "annotations": [
                    {
                        "submission_id": "low",
                        "result_code": 15,
                        "language": "PYTH 3",
                        "username": "someone",
                        "score": 4,
                    },
                    {
                        "submission_id": "high",
                        "result_code": 15,
                        "language": "PYTH 3",
                        "username": "popular",
                        "score": 26,
                    },
                ],
            })
        if "/api/submission-code/high" in url:
            return _Response({
                "data": {
                    "code": "import sys\nprint('popular')\n",
                    "language": {"short_name": "PYTH 3"},
                }
            })
        raise AssertionError(f"unexpected GET {url}")


class CodeChefCommunityTest(conftest._Base):
    def test_submit_accepted_python3_solution_is_cached_internally(self) -> None:
        source = "import sys\nprint('ok')\n"
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "community.json"
            session = _Session()
            with patch.object(codechef_community, "CACHE_PATH", cache_path), patch.object(
                codechef_community,
                "_session",
                return_value=session,
            ):
                result = codechef_community.submit_python3_solution(
                    "cc_BWFPF01",
                    source,
                    poll_interval=0,
                )

                self.assertTrue(result["accepted"])
                self.assertEqual(result["submission_id"], "123456789")
                self.assertEqual(session.submitted_headers["X-CSRF-Token"], "fake-csrf")
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                self.assertEqual(cached["solutions"]["BWFPF01"]["source"], source)
                self.assertEqual(
                    cached["solutions"]["BWFPF01"]["selection"],
                    "generated Python3 solution accepted by CodeChef",
                )

    def test_refresh_prefers_most_popular_explained_python_solution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "community.json"
            with patch.object(codechef_community, "CACHE_PATH", cache_path), patch.object(
                codechef_community,
                "_session",
                return_value=_ExplainedSession(),
            ):
                solution = codechef_community.refresh_best_python3_solution("cc_BWFPF01")

                self.assertIsNotNone(solution)
                self.assertEqual(solution["submission_id"], "high")
                self.assertEqual(solution["popularity"], 26)
                self.assertEqual(
                    solution["selection"],
                    "most popular explained CodeChef Python3 solution",
                )
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                self.assertEqual(cached["solutions"]["BWFPF01"]["submission_id"], "high")

    def test_load_cached_source_prefers_exported_def_solve_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "optimal"
            exported = root / "path" / "BWFPF01.py"
            exported.parent.mkdir(parents=True)
            exported.write_text("def solve():\n    print('exported')\n", encoding="utf-8")
            cache_path = Path(tmp) / "community.json"
            cache_path.write_text(
                json.dumps({
                    "solutions": {
                        "BWFPF01": {
                            "source": "print('raw cache')\n",
                        }
                    }
                }),
                encoding="utf-8",
            )

            with patch.object(codechef_community, "CACHE_PATH", cache_path), patch.object(
                codechef_community,
                "OPTIMAL_CODECHEF_ROOT",
                root,
            ):
                codechef_community._load_exported_source.cache_clear()
                self.assertIn("def solve()", codechef_community.load_cached_source("cc_BWFPF01"))
                codechef_community._load_exported_source.cache_clear()

    def test_exporter_uses_official_python_solution_as_fallback(self) -> None:
        sources = export_codechef_optimal_solutions._baseline_sources()
        self.assertEqual(sources["CWC23QUALIF"]["kind"], "official_python")
        self.assertIn("n=int(input())", sources["CWC23QUALIF"]["source"])

    def test_codechef_runner_supports_real_input_print_solution_shape(self) -> None:
        source = (
            "def solve():\n"
            "    score = int(input())\n"
            "    print('Yes' if score >= 12 else 'No')\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )

        result = run_player_code("cc_CWC23QUALIF", source, n=2, seed=1)

        self.assertTrue(result.correct)
        self.assertTrue(result.passed)
        self.assertEqual(result.return_value_repr, '"No"')

    def test_codechef_runner_supports_top_level_input_print_script(self) -> None:
        source = "score = int(input())\nprint('Yes' if score >= 12 else 'No')\n"

        result = run_player_code("cc_CWC23QUALIF", source, n=2, seed=1)

        self.assertTrue(result.correct)
        self.assertTrue(result.passed)
        self.assertEqual(result.return_value_repr, '"No"')
