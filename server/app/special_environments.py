"""Isolated runners for LeetCode SQL, pandas, and Bash playgrounds."""

from __future__ import annotations

import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from server.app.config import CODEN_HOME, PROJECT_ROOT


@dataclass(frozen=True)
class EnvironmentResult:
    value: Any = None
    stdout: str = ""
    stderr: str = ""
    runtime_ms: float | None = None
    error_message: str = ""

    @property
    def ok(self) -> bool:
        return not self.error_message


def run_special_environment(
    *,
    category: str,
    source: str,
    input_data: dict[str, Any],
    timeout_seconds: float = 8.0,
) -> EnvironmentResult:
    normalized = category.strip().lower()
    if normalized == "database":
        return _run_sql(source, input_data)
    if normalized == "pandas":
        return _run_pandas(source, input_data, timeout_seconds)
    if normalized == "shell":
        return _run_bash(source, input_data, timeout_seconds)
    return EnvironmentResult(error_message=f"Unknown special environment: {category}.")


def _run_sql(source: str, input_data: dict[str, Any]) -> EnvironmentResult:
    tables = input_data.get("tables", input_data)
    if not isinstance(tables, dict) or not tables:
        return EnvironmentResult(
            error_message='SQL input must contain a non-empty "tables" object.'
        )
    started = time.perf_counter()
    try:
        with sqlite3.connect(":memory:") as connection:
            connection.row_factory = sqlite3.Row
            for raw_name, raw_rows in tables.items():
                _create_sqlite_table(connection, str(raw_name), raw_rows)
            statements = _sqlite_statements(source)
            if not statements:
                raise sqlite3.OperationalError("SQL source contains no statements.")
            cursor = connection.execute(statements[0])
            for statement in statements[1:]:
                cursor = connection.execute(statement)
            columns = [column[0] for column in cursor.description or []]
            rows = [[_json_safe(cell) for cell in row] for row in cursor.fetchall()]
        runtime_ms = (time.perf_counter() - started) * 1000.0
        return EnvironmentResult(
            value={"columns": columns, "rows": rows},
            stdout=json.dumps({"columns": columns, "rows": rows}, ensure_ascii=False),
            runtime_ms=runtime_ms,
        )
    except sqlite3.Error as exc:
        return EnvironmentResult(
            runtime_ms=(time.perf_counter() - started) * 1000.0,
            error_message=f"SQL error: {exc}",
        )


def _sqlite_statements(source: str) -> list[str]:
    """Split complete SQLite statements without breaking semicolons in literals."""
    statements: list[str] = []
    buffer = ""
    for character in source:
        buffer += character
        if character == ";" and sqlite3.complete_statement(buffer):
            if buffer.strip():
                statements.append(buffer.strip())
            buffer = ""
    if buffer.strip():
        statements.append(buffer.strip())
    return statements


def _create_sqlite_table(connection: sqlite3.Connection, name: str, raw_rows: Any) -> None:
    if isinstance(raw_rows, dict) and isinstance(raw_rows.get("rows"), list):
        columns = [str(column) for column in raw_rows.get("columns") or []]
        rows = raw_rows["rows"]
        records = [dict(zip(columns, row)) for row in rows if isinstance(row, list)]
    elif isinstance(raw_rows, list):
        records = [row for row in raw_rows if isinstance(row, dict)]
        columns = []
        for record in records:
            for column in record:
                if str(column) not in columns:
                    columns.append(str(column))
    else:
        raise sqlite3.OperationalError(f'Table "{name}" must be an array of row objects.')
    if not columns:
        raise sqlite3.OperationalError(f'Table "{name}" has no columns.')
    column_types = {
        column: _sqlite_type(next((row.get(column) for row in records if row.get(column) is not None), None))
        for column in columns
    }
    quoted_columns = ", ".join(
        f'{_quote_identifier(column)} {column_types[column]}' for column in columns
    )
    connection.execute(f"CREATE TABLE {_quote_identifier(name)} ({quoted_columns})")
    placeholders = ", ".join("?" for _ in columns)
    insert = (
        f"INSERT INTO {_quote_identifier(name)} "
        f"({', '.join(_quote_identifier(column) for column in columns)}) VALUES ({placeholders})"
    )
    connection.executemany(insert, [[row.get(column) for column in columns] for row in records])


def _quote_identifier(value: str) -> str:
    if not value or "\x00" in value:
        raise sqlite3.OperationalError("SQL table and column names must be non-empty.")
    return '"' + value.replace('"', '""') + '"'


def _sqlite_type(value: Any) -> str:
    if isinstance(value, bool) or isinstance(value, int):
        return "INTEGER"
    if isinstance(value, float):
        return "REAL"
    if isinstance(value, (bytes, bytearray)):
        return "BLOB"
    return "TEXT"


def _run_pandas(source: str, input_data: dict[str, Any], timeout_seconds: float) -> EnvironmentResult:
    python = _python_runtime()
    if python is None:
        return EnvironmentResult(
            error_message="Pandas runtime is unavailable. Rebuild the app with the bundled Python environment."
        )
    with tempfile.TemporaryDirectory(prefix="coden-pandas-") as tmp:
        workdir = Path(tmp)
        solution_path = workdir / "solution.py"
        runner_path = workdir / "runner.py"
        solution_path.write_text(source, encoding="utf-8")
        runner_path.write_text(_PANDAS_RUNNER, encoding="utf-8")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [python, str(runner_path), str(solution_path)],
                cwd=str(workdir),
                input=json.dumps(input_data),
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(error_message=f"Pandas program timed out after {timeout_seconds:g} seconds.")
        runtime_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            if "No module named 'pandas'" in detail:
                detail = "pandas is not installed in the selected Python runtime."
            return EnvironmentResult(
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message=f"Pandas error: {detail[:1600]}",
            )
        try:
            value = json.loads(completed.stdout)
        except json.JSONDecodeError:
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message="Pandas runner did not return valid JSON.",
            )
        return EnvironmentResult(value=value, stdout=completed.stdout, stderr=completed.stderr, runtime_ms=runtime_ms)


def _run_bash(source: str, input_data: dict[str, Any], timeout_seconds: float) -> EnvironmentResult:
    bash = _bash_runtime()
    if bash is None:
        return EnvironmentResult(
            error_message=(
                "Bash runtime not found. Bundle bash.exe under debug-tools/bash/bin, "
                "install Git for Windows, or set CODEN_BASH."
            )
        )
    stdin = input_data.get("stdin", "")
    files = input_data.get("files", {})
    if not isinstance(stdin, str) or not isinstance(files, dict):
        return EnvironmentResult(error_message='Bash input requires string "stdin" and object "files" values.')
    with tempfile.TemporaryDirectory(prefix="coden-bash-") as tmp:
        workdir = Path(tmp)
        script = workdir / "solution.sh"
        script.write_text(source, encoding="utf-8", newline="\n")
        for raw_name, contents in files.items():
            relative = Path(str(raw_name))
            if relative.is_absolute() or ".." in relative.parts:
                return EnvironmentResult(error_message=f"Unsafe Bash fixture path: {raw_name}.")
            target = workdir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(str(contents), encoding="utf-8", newline="\n")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [bash, str(script)],
                cwd=str(workdir),
                input=stdin,
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(error_message=f"Bash program timed out after {timeout_seconds:g} seconds.")
        runtime_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message=f"Bash exited with code {completed.returncode}: {(completed.stderr or completed.stdout).strip()[:1600]}",
            )
        return EnvironmentResult(
            value=completed.stdout.rstrip("\n"),
            stdout=completed.stdout,
            stderr=completed.stderr,
            runtime_ms=runtime_ms,
        )


def _python_runtime() -> str | None:
    configured = os.environ.get("CODEN_DEBUG_PYTHON") or os.environ.get("CODEN_PYTHON_EXE")
    if configured and Path(configured).is_file():
        return configured
    executable = Path(sys.executable)
    if executable.is_file() and executable.name.lower() not in {"coden-server.exe", "coden-server"}:
        return str(executable)
    return None


def _bash_runtime() -> str | None:
    configured = os.environ.get("CODEN_BASH")
    if configured and Path(configured).is_file():
        return configured
    roots = [
        CODEN_HOME / "debug-tools",
        PROJECT_ROOT / "debug-tools",
        PROJECT_ROOT / "server" / "dist" / "debug-tools",
    ]
    for root in roots:
        for relative in ("bash/bin/bash.exe", "bash/bash.exe", "bin/bash.exe", "bash.exe"):
            candidate = root / relative
            if candidate.is_file():
                return str(candidate)
    if os.name == "nt":
        for candidate in (
            Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "bin" / "bash.exe",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Git" / "bin" / "bash.exe",
        ):
            if candidate.is_file():
                return str(candidate)
    found = shutil.which("bash")
    return found


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


_PANDAS_RUNNER = r'''
import importlib.util
import inspect
import json
import sys

import pandas as pd

payload = json.load(sys.stdin)
spec = importlib.util.spec_from_file_location("coden_user_solution", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = getattr(module, "solve", None)
if not callable(solve):
    candidates = [
        value for name, value in vars(module).items()
        if callable(value) and not name.startswith("_") and getattr(value, "__module__", "") == module.__name__
    ]
    if len(candidates) != 1:
        raise RuntimeError("Define solve(...) or exactly one public solution function.")
    solve = candidates[0]

tables = payload.get("tables", {})
args = dict(payload.get("args", {}))
if not isinstance(tables, dict) or not isinstance(args, dict):
    raise RuntimeError('Pandas input requires object "tables" and optional object "args" values.')
for name, rows in tables.items():
    args[name] = pd.DataFrame(rows)

signature = inspect.signature(solve)
if not args and len(signature.parameters) == 1 and "data" in payload:
    args[next(iter(signature.parameters))] = pd.DataFrame(payload["data"])
result = solve(**args)
if isinstance(result, pd.DataFrame):
    output = {"columns": [str(column) for column in result.columns], "rows": result.where(pd.notna(result), None).values.tolist()}
elif isinstance(result, pd.Series):
    output = {"name": None if result.name is None else str(result.name), "values": result.where(pd.notna(result), None).tolist()}
elif hasattr(result, "item"):
    output = result.item()
else:
    output = result
print(json.dumps(output, ensure_ascii=False, default=str))
'''
