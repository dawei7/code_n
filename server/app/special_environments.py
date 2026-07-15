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
    challenge_id: str = "",
    timeout_seconds: float = 8.0,
) -> EnvironmentResult:
    normalized = category.strip().lower()
    if normalized == "database":
        return _run_sql(source, input_data)
    if normalized == "pandas":
        return _run_pandas(source, input_data, timeout_seconds)
    if normalized == "shell":
        return _run_bash(source, input_data, timeout_seconds)
    if normalized == "concurrency":
        return _run_concurrency(source, input_data, challenge_id, timeout_seconds)
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


def _run_concurrency(
    source: str,
    input_data: dict[str, Any],
    challenge_id: str,
    timeout_seconds: float,
) -> EnvironmentResult:
    python = _python_runtime()
    if python is None:
        return EnvironmentResult(
            error_message="Concurrency runtime is unavailable. Rebuild the app with the bundled Python environment."
        )
    if challenge_id not in {"lc_1114", "lc_1115", "lc_1116", "lc_1117", "lc_1188", "lc_1195", "lc_1226", "lc_1242", "lc_1279"}:
        return EnvironmentResult(error_message=f"Unsupported concurrency challenge: {challenge_id}.")
    with tempfile.TemporaryDirectory(prefix="coden-concurrency-") as tmp:
        workdir = Path(tmp)
        solution_path = workdir / "solution.py"
        runner_path = workdir / "runner.py"
        solution_path.write_text(source, encoding="utf-8")
        runner_path.write_text(_CONCURRENCY_RUNNER, encoding="utf-8")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [python, str(runner_path), str(solution_path), challenge_id],
                cwd=str(workdir),
                input=json.dumps(input_data),
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(
                runtime_ms=(time.perf_counter() - started) * 1000.0,
                error_message=f"Concurrency program deadlocked or timed out after {timeout_seconds:g} seconds.",
            )
        process_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=process_ms,
                error_message=f"Concurrency error: {detail[:1600]}",
            )
        try:
            payload = json.loads(completed.stdout)
            value = payload["value"]
            runtime_ms = float(payload.get("runtime_ms", process_ms))
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=process_ms,
                error_message="Concurrency runner did not return valid JSON.",
            )
        return EnvironmentResult(
            value=value,
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


_CONCURRENCY_RUNNER = r'''
import importlib.util
import json
import sys
import threading
import time
import traceback
from collections import Counter
from urllib.parse import urlsplit


def load_module(path):
    spec = importlib.util.spec_from_file_location("coden_user_solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_threads(calls, *, stagger=False):
    errors = []

    def guarded(call):
        try:
            call()
        except BaseException:
            errors.append(traceback.format_exc())

    threads = []
    for call in calls:
        thread = threading.Thread(target=guarded, args=(call,), daemon=True)
        threads.append(thread)
        thread.start()
        if stagger:
            time.sleep(0.0005)
    for thread in threads:
        thread.join(2.0)
    if any(thread.is_alive() for thread in threads):
        raise RuntimeError("worker threads did not finish; probable deadlock")
    if errors:
        raise RuntimeError(errors[0])


def run_1114(module, data):
    target = module.Foo()
    output = []
    methods = {
        1: lambda: target.first(lambda: output.append("first")),
        2: lambda: target.second(lambda: output.append("second")),
        3: lambda: target.third(lambda: output.append("third")),
    }
    run_threads([methods[value] for value in data["nums"]], stagger=True)
    return "".join(output)


def run_1115(module, data):
    target = module.FooBar(int(data["n"]))
    output = []
    calls = {
        "foo": lambda: target.foo(lambda: output.append("foo")),
        "bar": lambda: target.bar(lambda: output.append("bar")),
    }
    order = data.get("threads", ["bar", "foo"])
    run_threads([calls[name] for name in order])
    return "".join(output)


def run_1116(module, data):
    target = module.ZeroEvenOdd(int(data["n"]))
    output = []
    calls = {
        "zero": lambda: target.zero(output.append),
        "even": lambda: target.even(output.append),
        "odd": lambda: target.odd(output.append),
    }
    order = data.get("threads", ["even", "odd", "zero"])
    run_threads([calls[name] for name in order])
    return "".join(str(value) for value in output)


def run_1117(module, data):
    target = module.H2O()
    output = []
    calls = []
    for atom in data["water"]:
        if atom == "H":
            calls.append(lambda target=target: target.hydrogen(lambda: output.append("H")))
        elif atom == "O":
            calls.append(lambda target=target: target.oxygen(lambda: output.append("O")))
        else:
            raise ValueError(f"invalid atom: {atom!r}")
    run_threads(calls, stagger=bool(data.get("stagger", True)))
    return "".join(output)


def run_1188(module, data):
    target = module.BoundedBlockingQueue(int(data["capacity"]))
    dequeued = []
    calls = []
    wants_size = False
    for operation in data["operations"]:
        if operation[0] == "enqueue":
            value = int(operation[1])
            calls.append(lambda value=value: target.enqueue(value))
        elif operation[0] == "dequeue":
            calls.append(lambda: dequeued.append(target.dequeue()))
        elif operation[0] == "size":
            wants_size = True
        else:
            raise ValueError(f"unknown operation: {operation!r}")
    run_threads(calls, stagger=bool(data.get("stagger", True)))
    return {"dequeued": dequeued, "final_size": target.size() if wants_size else target.size()}


def run_1195(module, data):
    target = module.FizzBuzz(int(data["n"]))
    output = []
    calls = {
        "fizz": lambda: target.fizz(lambda: output.append("fizz")),
        "buzz": lambda: target.buzz(lambda: output.append("buzz")),
        "fizzbuzz": lambda: target.fizzbuzz(lambda: output.append("fizzbuzz")),
        "number": lambda: target.number(output.append),
    }
    run_threads([calls[name] for name in data.get("threads", calls)])
    return output


def run_1226(module, data):
    target = module.DiningPhilosophers()
    rounds = int(data["n"])
    order = [int(value) for value in data.get("start_order", range(5))]
    philosophers = []
    while len(philosophers) < rounds * 5:
        philosophers.extend(order)
    philosophers = philosophers[: rounds * 5]
    lock = threading.Lock()
    fork_owner = [None] * 5
    violations = []
    completed = []

    def request(call_id, philosopher):
        left = philosopher
        right = (philosopher + 1) % 5
        events = []

        def pick(fork, label):
            with lock:
                if fork_owner[fork] is not None:
                    violations.append("shared-fork-overlap")
                fork_owner[fork] = call_id
                events.append(label)

        def put(fork, label):
            with lock:
                if fork_owner[fork] != call_id:
                    violations.append("put-unowned-fork")
                fork_owner[fork] = None
                events.append(label)

        target.wantsToEat(
            philosopher,
            lambda: pick(left, "pick-left"),
            lambda: pick(right, "pick-right"),
            lambda: events.append("eat"),
            lambda: put(left, "put-left"),
            lambda: put(right, "put-right"),
        )
        with lock:
            completed.append({"philosopher": philosopher, "events": events})

    run_threads([
        lambda call_id=index, philosopher=value: request(call_id, philosopher)
        for index, value in enumerate(philosophers)
    ], stagger=True)
    return {"calls": completed, "violations": violations}


class HtmlParser:
    def __init__(self, graph, delays):
        self.graph = graph
        self.delays = delays
        self.lock = threading.Lock()
        self.fetches = []
        self.active = 0
        self.max_active = 0

    def getUrls(self, url):
        with self.lock:
            self.fetches.append(url)
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        time.sleep(self.delays.get(url, 0.0005))
        result = list(self.graph.get(url, []))
        with self.lock:
            self.active -= 1
        return result


def crawler_fixture(data):
    if "urls" in data:
        urls = list(data["urls"])
        graph = {url: [] for url in urls}
        for left, right in data.get("edges", []):
            graph[urls[left]].append(urls[right])
        return graph, data["start_url"]
    shape = data.get("shape")
    if shape == "star":
        width = int(data["width"])
        host = data.get("hostname", "a.com")
        root = f"http://{host}"
        children = [f"{root}/{index}" for index in range(width)]
        return {root: children, **{url: [] for url in children}}, root
    if shape == "duplicate-edges":
        root = "http://a.com"
        child = root + "/x"
        return {root: [child, child, child], child: [root]}, root
    if shape == "off-host-bridge":
        root = "http://a.com"
        foreign = "http://b.com/x"
        hidden = "http://a.com/hidden"
        return {root: [foreign], foreign: [hidden], hidden: []}, root
    nodes = int(data.get("nodes", 1))
    urls = [f"http://a.com/{index}" for index in range(nodes)]
    if shape == "dense":
        return {url: urls[index + 1:] for index, url in enumerate(urls)}, urls[0]
    graph = {url: urls[index + 1:index + 4] for index, url in enumerate(urls)}
    return graph, urls[0]


def run_1242(module, data):
    graph, start = crawler_fixture(data)
    delay_scale = float(data.get("parser_delay", 0.0002))
    delays = {url: delay_scale * (1 + index % 5) for index, url in enumerate(graph)}
    parser = HtmlParser(graph, delays)
    target = module.Solution()
    urls = target.crawl(start, parser)
    return {"urls": list(urls), "fetches": parser.fetches, "max_active": parser.max_active, "graph": graph, "start_url": start}


def run_1279(module, data):
    target = module.TrafficLight()
    cars = [int(value) for value in data["cars"]]
    directions = [int(value) for value in data["directions"]]
    arrival_times = [int(value) for value in data.get("arrival_times", data.get("arrivalTimes", []))]
    if not (len(cars) == len(directions) == len(arrival_times)):
        raise ValueError("cars, directions, and arrival_times must have equal lengths")

    state_lock = threading.Lock()
    green_road = 1
    active = Counter()
    events = []
    violations = []
    first_arrival = min(arrival_times, default=0)

    def request(car_id, direction, arrival_time):
        nonlocal green_road
        road_id = 1 if direction <= 2 else 2
        time.sleep(max(0, arrival_time - first_arrival) * 0.0001)

        def turn_green():
            nonlocal green_road
            with state_lock:
                if green_road == road_id:
                    violations.append("redundant-green-change")
                if any(count and road != road_id for road, count in active.items()):
                    violations.append("green-change-during-crossing")
                green_road = road_id
                events.append({"kind": "green", "road": road_id, "car": car_id})

        def cross_car():
            with state_lock:
                if green_road != road_id:
                    violations.append("red-road-crossing")
                if any(count and road != road_id for road, count in active.items()):
                    violations.append("cross-road-overlap")
                active[road_id] += 1
            time.sleep(0.0005)
            with state_lock:
                events.append({"kind": "cross", "road": road_id, "direction": direction, "car": car_id})
                active[road_id] -= 1

        target.carArrived(car_id, road_id, direction, turn_green, cross_car)

    run_threads([
        lambda car_id=car_id, direction=direction, arrival_time=arrival_time: request(
            car_id, direction, arrival_time
        )
        for car_id, direction, arrival_time in zip(cars, directions, arrival_times)
    ])
    return {"cars": cars, "events": events, "violations": violations}


RUNNERS = {
    "lc_1114": run_1114,
    "lc_1115": run_1115,
    "lc_1116": run_1116,
    "lc_1117": run_1117,
    "lc_1188": run_1188,
    "lc_1195": run_1195,
    "lc_1226": run_1226,
    "lc_1242": run_1242,
    "lc_1279": run_1279,
}

data = json.load(sys.stdin)
module = load_module(sys.argv[1])
started = time.perf_counter()
value = RUNNERS[sys.argv[2]](module, data)
runtime_ms = (time.perf_counter() - started) * 1000.0
print(json.dumps({"value": value, "runtime_ms": runtime_ms}, ensure_ascii=False, default=str))
'''
