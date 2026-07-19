"""Source-native LeetCode special-environment runtime tests."""

from __future__ import annotations

import shutil

import pytest

from server.app.challenge_packages import leetcode_solution_path
from server.app.special_environments import run_special_environment

from . import conftest


class SpecialEnvironmentRouteTest(conftest._Base):
    def test_database_challenge_exposes_sql_editor_and_runs_custom_fixture(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        detail = self.client.get("/api/challenges/lc_175")
        self.assertEqual(detail.status_code, 200, detail.text)
        body = detail.json()
        self.assertTrue(body["runnable_in_coden"])
        self.assertEqual(body["supported_languages"], ["sql"])
        self.assertEqual(body["primary_language"], "sql")
        self.assertTrue(body["optimal_sources"]["sql"])
        self.assertIn("SELECT", body["starter_sources"]["sql"])

        response = self.client.post(
            "/api/challenges/lc_175/run",
            json={
                "language": "sql",
                "source": "SELECT personId, firstName FROM Person ORDER BY personId",
                "custom_input": {
                    "tables": {
                        "Person": [
                            {"personId": 2, "firstName": "Grace"},
                            {"personId": 1, "firstName": "Ada"},
                        ]
                    }
                },
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        result = response.json()
        self.assertTrue(result["passed"], result)
        self.assertIn('"columns": ["personId", "firstName"]', result["return_value_repr"])
        self.assertEqual(result["selected_case_ids"], ["custom"])

    def test_scalable_concurrency_challenges_run_native_classes_and_scaling_tiers(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        challenges = {
            "1115": ("1115_print-foobar-alternately", "class FooBar"),
            "1116": ("1116_print-zero-even-odd", "class ZeroEvenOdd"),
            "1117": ("1117_building-h2o", "class H2O"),
            "1195": ("1195_fizz-buzz-multithreaded", "class FizzBuzz"),
            "1242": ("1242_web-crawler-multithreaded", "class Solution"),
        }
        for frontend_id, (package_name, class_declaration) in challenges.items():
            with self.subTest(frontend_id=frontend_id):
                detail = self.client.get(f"/api/challenges/lc_{frontend_id}")
                self.assertEqual(detail.status_code, 200, detail.text)
                body = detail.json()
                self.assertTrue(body["runnable_in_coden"])
                self.assertEqual(body["supported_languages"], ["python"])
                self.assertIn(class_declaration, body["starter_sources"]["python"])

                solution_path = leetcode_solution_path(f"lc_{frontend_id}", "python")
                self.assertIsNotNone(solution_path)
                source = solution_path.read_text(encoding="utf-8")
                response = self.client.post(
                    f"/api/challenges/lc_{frontend_id}/run",
                    json={"language": "python", "source": source, "mode": "real_test"},
                )
                self.assertEqual(response.status_code, 200, response.text)
                result = response.json()
                self.assertTrue(result["correct"], result)
                self.assertTrue(result["runtime_check"], result)
                self.assertTrue(result["runtime_passed"], result)
                self.assertTrue(result["passed"], result)

    def test_bounded_concurrency_challenges_run_practice_without_benchmarks(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        challenges = {
            "1114": ("1114_print-in-order", "class Foo"),
            "1188": ("1188_design-bounded-blocking-queue", "class BoundedBlockingQueue"),
            "1226": ("1226_the-dining-philosophers", "class DiningPhilosophers"),
            "1279": ("1279_traffic-light-controlled-intersection", "class TrafficLight"),
        }
        for frontend_id, (package_name, class_declaration) in challenges.items():
            with self.subTest(frontend_id=frontend_id):
                detail = self.client.get(f"/api/challenges/lc_{frontend_id}")
                self.assertEqual(detail.status_code, 200, detail.text)
                body = detail.json()
                self.assertTrue(body["runnable_in_coden"])
                self.assertIn(class_declaration, body["starter_sources"]["python"])
                solution_path = leetcode_solution_path(f"lc_{frontend_id}", "python")
                self.assertIsNotNone(solution_path)
                source = solution_path.read_text(encoding="utf-8")
                response = self.client.post(
                    f"/api/challenges/lc_{frontend_id}/run",
                    json={"language": "python", "source": source},
                )
                self.assertEqual(response.status_code, 200, response.text)
                result = response.json()
                self.assertTrue(result["correct"], result)
                self.assertTrue(result["passed"], result)
                self.assertFalse(result["runtime_check"], result)


def test_sql_environment_returns_a_result_grid() -> None:
    result = run_special_environment(
        category="database",
        source="SELECT id, name FROM People WHERE id > 1 ORDER BY id",
        input_data={"tables": {"People": [{"id": 2, "name": "Grace"}, {"id": 1, "name": "Ada"}]}},
    )
    assert result.ok, result.error_message
    assert result.value == {"columns": ["id", "name"], "rows": [[2, "Grace"]]}


def test_sql_environment_returns_post_mutation_grid_from_final_statement() -> None:
    result = run_special_environment(
        category="database",
        source="DELETE FROM People WHERE id = 1; SELECT id, name FROM People ORDER BY id;",
        input_data={"tables": {"People": [{"id": 2, "name": "Grace"}, {"id": 1, "name": "Ada"}]}},
    )
    assert result.ok, result.error_message
    assert result.value == {"columns": ["id", "name"], "rows": [[2, "Grace"]]}


@pytest.mark.skipif(
    shutil.which("bash") is None and shutil.which("git") is None,
    reason="Bash runtime is not installed on this test machine.",
)
def test_bash_environment_receives_stdin_and_files() -> None:
    result = run_special_environment(
        category="shell",
        source="head -n 1 file.txt && cat",
        input_data={"stdin": "from stdin\n", "files": {"file.txt": "from file\nsecond\n"}},
    )
    assert result.ok, result.error_message
    assert result.value == "from file\nfrom stdin"


def test_pandas_environment_reports_dependency_or_returns_dataframe() -> None:
    result = run_special_environment(
        category="pandas",
        source=(
            "import pandas as pd\n\n"
            "def solve(data: pd.DataFrame) -> pd.DataFrame:\n"
            "    return data[data['score'] >= 90][['id']]\n"
        ),
        input_data={"tables": {"data": [{"id": 1, "score": 95}, {"id": 2, "score": 80}]}},
    )
    if not result.ok:
        assert "pandas is not installed" in result.error_message
    else:
        assert result.value == {"columns": ["id"], "rows": [[1]]}


def test_concurrency_environment_reports_probable_deadlock() -> None:
    source = """
from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.never = Event()

    def foo(self, printFoo):
        self.never.wait()

    def bar(self, printBar):
        self.never.wait()
"""
    result = run_special_environment(
        category="concurrency",
        source=source,
        input_data={"n": 1},
        challenge_id="lc_1115",
        timeout_seconds=0.2,
    )
    assert not result.ok
    assert "deadlocked or timed out" in result.error_message


def test_traffic_light_environment_rejects_crossing_against_the_green_light() -> None:
    source = """
class TrafficLight:
    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        crossCar()
"""
    result = run_special_environment(
        category="concurrency",
        source=source,
        input_data={"cars": [1], "directions": [3], "arrival_times": [0]},
        challenge_id="lc_1279",
    )
    assert result.ok, result.error_message
    assert "red-road-crossing" in result.value["violations"]
