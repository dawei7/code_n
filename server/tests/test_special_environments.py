"""Source-native LeetCode SQL, pandas, and Bash runtime tests."""

from __future__ import annotations

import shutil

import pytest

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
