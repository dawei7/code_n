"""Versioned user-solution overlay API tests."""
from __future__ import annotations

import json

from server.app.user_solutions import user_solution_dir
from server.tests.conftest import _Base, _TEST_LEGACY_SOLUTIONS


class SolutionRoutesTests(_Base):
    def test_first_open_creates_only_three_versioned_files(self) -> None:
        response = self.client.get("/api/solutions/lc_1?language=python")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["versions"], [1, 2, 3])
        self.assertEqual(payload["active_version"], 1)
        self.assertEqual(
            payload["filename"],
            "dsa/leetcode/1_two-sum/user_solutions/python_v1.py",
        )

        directory = user_solution_dir("lc_1")
        code_files = sorted(path.name for path in directory.glob("*.py"))
        self.assertEqual(code_files, ["python_v1.py", "python_v2.py", "python_v3.py"])
        self.assertFalse((directory / "python.py").exists())

    def test_switch_reads_real_version_without_copy_alias(self) -> None:
        first_source = "def solve(nums, target):\n    return [0, 1]\n"
        second_source = "def solve(nums, target):\n    return [1, 2]\n"
        self.client.get("/api/solutions/lc_1?language=python")
        self.client.put(
            "/api/solutions/lc_1?language=python",
            json={"source": first_source},
        )
        switched = self.client.post(
            "/api/solutions/lc_1/versions/switch?language=python",
            json={"version": 2},
        )
        self.assertEqual(switched.status_code, 200)
        self.assertTrue(switched.json()["filename"].endswith("python_v2.py"))
        self.client.put(
            "/api/solutions/lc_1?language=python",
            json={"source": second_source},
        )

        from server.app.routes import debug

        self.assertEqual(debug._solution_path("lc_1", "python").name, "python_v2.py")

        back = self.client.post(
            "/api/solutions/lc_1/versions/switch?language=python",
            json={"version": 1},
        )
        self.assertEqual(back.json()["source"], first_source)
        self.assertEqual(
            (user_solution_dir("lc_1") / "python_v2.py").read_text(encoding="utf-8"),
            second_source,
        )

        self.assertEqual(debug._solution_path("lc_1", "python").name, "python_v1.py")

    def test_sql_and_bash_also_use_three_explicit_versions(self) -> None:
        checks = (
            ("lc_175", "sql", ["sql_v1.sql", "sql_v2.sql", "sql_v3.sql"]),
            ("lc_192", "bash", ["bash_v1.sh", "bash_v2.sh", "bash_v3.sh"]),
        )
        for challenge_id, language, expected_files in checks:
            response = self.client.get(
                f"/api/solutions/{challenge_id}?language={language}"
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["versions"], [1, 2, 3])
            directory = user_solution_dir(challenge_id)
            self.assertEqual(
                sorted(path.name for path in directory.glob(f"{language}_v*")),
                expected_files,
            )

    def test_legacy_alias_is_migrated_to_active_version(self) -> None:
        from server.app.user_solutions import migrate_legacy_solutions

        legacy_python = _TEST_LEGACY_SOLUTIONS / "python"
        legacy_python.mkdir(parents=True, exist_ok=True)
        current = "def solve(nums, target):\n    return [0, 1]\n"
        old_backup = "def solve(nums, target):\n    return [1, 0]\n"
        (legacy_python / "lc_1.py").write_text(current, encoding="utf-8")
        (legacy_python / "lc_1_v1.py").write_text(old_backup, encoding="utf-8")
        (_TEST_LEGACY_SOLUTIONS / ".versions.json").write_text(
            json.dumps({"python:lc_1": {"active": 1, "names": {"1": "First"}}}),
            encoding="utf-8",
        )

        self.assertEqual(migrate_legacy_solutions([_TEST_LEGACY_SOLUTIONS]), 2)
        directory = user_solution_dir("lc_1")
        self.assertEqual((directory / "python_v1.py").read_text(encoding="utf-8"), current)
        self.assertEqual((directory / "python_v3.py").read_text(encoding="utf-8"), old_backup)

        payload = self.client.get("/api/solutions/lc_1?language=python").json()
        self.assertEqual(payload["version_names"], {"1": "First"})
        self.assertEqual(
            sorted(path.name for path in directory.glob("*.py")),
            ["python_v1.py", "python_v2.py", "python_v3.py"],
        )

    def test_invalid_version_is_rejected(self) -> None:
        response = self.client.post(
            "/api/solutions/lc_1/versions/switch?language=python",
            json={"version": 4},
        )
        self.assertEqual(response.status_code, 400)
