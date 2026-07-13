"""Compile and run non-Python programs."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from engine.languages import normalize_language
from server.app.config import CODEN_HOME, PROJECT_ROOT


@dataclass(frozen=True)
class ExternalProgramResult:
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0
    error_message: str = ""
    runtime_ms: float | None = None

    @property
    def ok(self) -> bool:
        return not self.error_message and self.returncode == 0


_TOOL_ENV_OVERRIDES = {
    "g++": "CODEN_CPP_COMPILER",
    "clang++": "CODEN_CPP_COMPILER",
    "javac": "CODEN_JAVAC",
    "java": "CODEN_JAVA",
    "dotnet": "CODEN_DOTNET",
    "node": "CODEN_NODE",
    "go": "CODEN_GO",
    "kotlinc": "CODEN_KOTLINC",
}

_RUNTIME_MARKER = "__CODEN_RUNTIME_MS__="


_TOOL_FILENAMES = {
    "g++": ("g++.exe", "g++"),
    "clang++": ("clang++.exe", "clang++"),
    "javac": ("javac.exe", "javac"),
    "java": ("java.exe", "java"),
    "dotnet": ("dotnet.exe", "dotnet"),
    "node": ("node.exe", "node"),
    "go": ("go.exe", "go"),
    "kotlinc": ("kotlinc.bat", "kotlinc.exe", "kotlinc"),
}

_TOOL_SUBDIRS = (
    "",
    "bin",
    "cpp",
    "cpp/bin",
    "java",
    "java/bin",
    "jdk/bin",
    "csharp",
    "csharp/bin",
    "dotnet",
    "dotnet/bin",
    "javascript",
    "javascript/bin",
    "node",
    "node/bin",
    "go",
    "go/bin",
    "kotlin",
    "kotlin/bin",
)


def run_function_program(
    *,
    language: str,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float = 5.0,
    measure_runtime: bool = False,
    runtime_iterations: int = 1,
) -> ExternalProgramResult:
    """Run a function-style challenge implementation.

    The Python challenge setup is serialized to JSON and fed to a small
    generated harness. The harness deserializes known challenge input shapes,
    calls ``Solution.solve(...)`` / ``Solution.Solve(...)``, and prints JSON for
    the existing Python verifier.
    """
    language_id = normalize_language(language)
    with tempfile.TemporaryDirectory(prefix=f"coden-{language_id}-") as tmp:
        workdir = Path(tmp)
        if language_id == "cpp":
            return _run_cpp_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
            )
        if language_id == "java":
            return _run_java_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
            )
        if language_id == "csharp":
            return _run_csharp_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
            )
        if language_id == "javascript":
            return _run_javascript_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
                runtime_iterations,
            )
        if language_id == "go":
            return _run_go_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
            )
        if language_id == "kotlin":
            return _run_kotlin_function(
                workdir,
                source,
                input_json,
                param_names,
                param_hints,
                returns_hint,
                timeout_seconds,
                measure_runtime,
            )
    return ExternalProgramResult(
        error_message=f"Unsupported external function-call language: {language_id}."
    )


def _run_cpp_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
) -> ExternalProgramResult:
    compiler = _first_tool("g++", "clang++")
    if compiler is None:
        return ExternalProgramResult(
            error_message="C++ compiler not found. Install g++ or clang++ on PATH, or set CODEN_CPP_COMPILER."
        )
    source_path = workdir / "main.cpp"
    exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
    source_path.write_text(
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n\n"
        + source.rstrip()
        + "\n\n"
        + _cpp_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
        ),
        encoding="utf-8",
    )
    compile_result = _run_process(
        [compiler, "-std=c++17", "-O0", "-g", str(source_path), "-o", str(exe_path)],
        cwd=workdir,
        timeout_seconds=30.0,
    )
    if compile_result.returncode != 0:
        return ExternalProgramResult(
            stderr=compile_result.stderr,
            returncode=compile_result.returncode,
            error_message=_message("C++ compile failed", compile_result.stderr or compile_result.stdout),
        )
    return _run_executable([str(exe_path)], workdir, input_json, timeout_seconds, "C++ program")


def _run_java_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
) -> ExternalProgramResult:
    javac = _first_tool("javac")
    java = _first_tool("java")
    if javac is None or java is None:
        return ExternalProgramResult(
            error_message="Java runtime not found. Install a JDK with javac and java on PATH, or set CODEN_JAVAC and CODEN_JAVA."
        )
    solution_path = workdir / "Solution.java"
    harness_path = workdir / "Main.java"
    solution_path.write_text(source, encoding="utf-8")
    harness_path.write_text(
        _java_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
        ),
        encoding="utf-8",
    )
    compile_result = _run_process(
        [javac, "-g", str(solution_path), str(harness_path)],
        cwd=workdir,
        timeout_seconds=30.0,
    )
    if compile_result.returncode != 0:
        return ExternalProgramResult(
            stderr=compile_result.stderr,
            returncode=compile_result.returncode,
            error_message=_message("Java compile failed", compile_result.stderr or compile_result.stdout),
        )
    return _run_executable([java, "-cp", str(workdir), "Main"], workdir, input_json, timeout_seconds, "Java program")


def _run_javascript_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
    runtime_iterations: int = 1,
) -> ExternalProgramResult:
    node = _first_tool("node")
    if node is None:
        return ExternalProgramResult(
            error_message="JavaScript runtime not found. Install Node.js on PATH, or set CODEN_NODE."
        )
    source_path = workdir / "main.js"
    source_path.write_text(
        source.rstrip()
        + "\n\n"
        + _javascript_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
            runtime_iterations=runtime_iterations,
        ),
        encoding="utf-8",
    )
    return _run_executable([node, str(source_path)], workdir, input_json, timeout_seconds, "JavaScript program")


def _run_go_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
) -> ExternalProgramResult:
    go = _first_tool("go")
    if go is None:
        return ExternalProgramResult(
            error_message="Go runtime not found. Install Go on PATH, or set CODEN_GO."
        )
    solution_path = workdir / "solution.go"
    harness_path = workdir / "coden_harness.go"
    exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
    solution_path.write_text(source, encoding="utf-8")
    harness_path.write_text(
        _go_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
        ),
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["GOCACHE"] = str(workdir / "gocache")
    compile_result = _run_process(
        [go, "build", "-o", str(exe_path), str(solution_path), str(harness_path)],
        cwd=workdir,
        timeout_seconds=60.0,
        env=env,
    )
    if compile_result.returncode != 0:
        return ExternalProgramResult(
            stderr=compile_result.stderr,
            returncode=compile_result.returncode,
            error_message=_message("Go compile failed", compile_result.stderr or compile_result.stdout),
        )
    return _run_executable([str(exe_path)], workdir, input_json, timeout_seconds, "Go program", env=env)


def _run_kotlin_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
) -> ExternalProgramResult:
    kotlinc = _first_tool("kotlinc")
    java = _first_tool("java")
    if kotlinc is None or java is None:
        return ExternalProgramResult(
            error_message="Kotlin runtime not found. Install Kotlin compiler plus Java on PATH, or set CODEN_KOTLINC and CODEN_JAVA."
        )
    solution_path = workdir / "Solution.kt"
    harness_path = workdir / "CodenHarness.kt"
    jar_path = workdir / "main.jar"
    solution_path.write_text(source, encoding="utf-8")
    harness_path.write_text(
        _kotlin_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
        ),
        encoding="utf-8",
    )
    compile_result = _run_process(
        [kotlinc, str(solution_path), str(harness_path), "-include-runtime", "-d", str(jar_path)],
        cwd=workdir,
        timeout_seconds=60.0,
    )
    if compile_result.returncode != 0:
        return ExternalProgramResult(
            stderr=compile_result.stderr,
            returncode=compile_result.returncode,
            error_message=_message("Kotlin compile failed", compile_result.stderr or compile_result.stdout),
        )
    return _run_executable([java, "-jar", str(jar_path)], workdir, input_json, timeout_seconds, "Kotlin program")


def _run_csharp_function(
    workdir: Path,
    source: str,
    input_json: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    timeout_seconds: float,
    measure_runtime: bool = False,
) -> ExternalProgramResult:
    dotnet = _first_tool("dotnet")
    if dotnet is None:
        return ExternalProgramResult(
            error_message="C# runtime not found. Install the .NET SDK on PATH, or set CODEN_DOTNET."
        )
    project_path = workdir / "CodenRun.csproj"
    solution_path = workdir / "Solution.cs"
    harness_path = workdir / "Program.cs"
    project_path.write_text(_csharp_project(_dotnet_target_framework(dotnet)), encoding="utf-8")
    solution_path.write_text(source, encoding="utf-8")
    harness_path.write_text(
        _csharp_function_harness(
            param_names,
            param_hints,
            returns_hint,
            param_values=_param_values_from_json(input_json),
            measure_runtime=measure_runtime,
        ),
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    env["DOTNET_NOLOGO"] = "1"
    build_result = _run_process(
        [dotnet, "build", str(project_path), "-nologo", "-v:q"],
        cwd=workdir,
        timeout_seconds=60.0,
        env=env,
    )
    if build_result.returncode != 0:
        return ExternalProgramResult(
            stderr=build_result.stderr,
            returncode=build_result.returncode,
            error_message=_message("C# compile failed", build_result.stderr or build_result.stdout),
        )
    return _run_executable(
        [dotnet, "run", "--project", str(project_path), "--no-build", "--no-launch-profile"],
        workdir,
        input_json,
        timeout_seconds,
        "C# program",
        env=env,
    )


def _first_tool(*names: str) -> str | None:
    for name in names:
        env_name = _TOOL_ENV_OVERRIDES.get(name)
        if env_name:
            configured = _configured_tool(env_name, _TOOL_FILENAMES.get(name))
            if configured:
                return configured
    for root in _native_tool_dirs():
        for name in names:
            bundled = _find_named_file(root, _TOOL_FILENAMES.get(name, (name,)))
            if bundled:
                return bundled
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def _configured_tool(env_name: str, filenames: Iterable[str] | None = None) -> str | None:
    value = os.environ.get(env_name)
    if not value:
        return None
    path = Path(value)
    if path.is_file():
        return str(path)
    if path.is_dir() and filenames is not None:
        return _find_named_file(path, filenames)
    return None


def _native_tool_dirs() -> list[Path]:
    dirs: list[Path] = []
    configured = os.environ.get("CODEN_DEBUG_TOOLS_DIR", "")
    for raw in configured.split(os.pathsep):
        raw = raw.strip()
        if raw:
            dirs.append(Path(raw))
    dirs.extend(
        [
            CODEN_HOME / "debug-tools",
            PROJECT_ROOT / "debug-tools",
            PROJECT_ROOT / "server" / "dist" / "debug-tools",
        ]
    )

    seen: set[str] = set()
    existing: list[Path] = []
    for directory in dirs:
        try:
            resolved = str(directory.resolve())
        except OSError:
            resolved = str(directory)
        if resolved in seen or not directory.is_dir():
            continue
        seen.add(resolved)
        existing.append(directory)
    return existing


def _find_named_file(root: Path, filenames: Iterable[str]) -> str | None:
    names = tuple(filenames)
    for subdir in _TOOL_SUBDIRS:
        base = root / Path(subdir) if subdir else root
        for name in names:
            candidate = base / name
            if candidate.is_file():
                return str(candidate)
    return None


def _run_process(
    args: list[str],
    *,
    cwd: Path,
    timeout_seconds: float,
    input_text: str | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            args,
            cwd=str(cwd),
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        return subprocess.CompletedProcess(args, 124, stdout=stdout, stderr=stderr or "Timed out.")


def _run_executable(
    args: list[str],
    workdir: Path,
    process_input: str,
    timeout_seconds: float,
    label: str,
    env: dict[str, str] | None = None,
) -> ExternalProgramResult:
    result = _run_process(
        args,
        cwd=workdir,
        input_text=process_input,
        timeout_seconds=timeout_seconds,
        env=env,
    )
    if result.returncode == 124:
        return ExternalProgramResult(
            stdout=result.stdout,
            stderr=result.stderr,
            returncode=result.returncode,
            error_message=f"{label} timed out after {timeout_seconds:g}s.",
            runtime_ms=_extract_runtime_ms(result.stderr),
        )
    if result.returncode != 0:
        return ExternalProgramResult(
            stdout=result.stdout,
            stderr=result.stderr,
            returncode=result.returncode,
            error_message=_message(f"{label} exited with code {result.returncode}", result.stderr or result.stdout),
            runtime_ms=_extract_runtime_ms(result.stderr),
        )
    return ExternalProgramResult(
        stdout=result.stdout,
        stderr=result.stderr,
        returncode=0,
        runtime_ms=_extract_runtime_ms(result.stderr),
    )


def _extract_runtime_ms(stderr: str) -> float | None:
    match = re.search(rf"{re.escape(_RUNTIME_MARKER)}([0-9]+(?:\.[0-9]+)?)", stderr or "")
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def _dotnet_target_framework(dotnet: str) -> str:
    result = _run_process([dotnet, "--version"], cwd=Path.cwd(), timeout_seconds=10.0)
    match = re.match(r"(\d+)\.", (result.stdout or "").strip())
    if match:
        return f"net{match.group(1)}.0"
    return "net8.0"


def _csharp_project(target_framework: str, startup_object: str | None = None) -> str:
    startup_line = f"    <StartupObject>{startup_object}</StartupObject>\n" if startup_object else ""
    return (
        '<Project Sdk="Microsoft.NET.Sdk">\n'
        "  <PropertyGroup>\n"
        "    <OutputType>Exe</OutputType>\n"
        f"    <TargetFramework>{target_framework}</TargetFramework>\n"
        "    <ImplicitUsings>enable</ImplicitUsings>\n"
        "    <Nullable>disable</Nullable>\n"
        f"{startup_line}"
        "  </PropertyGroup>\n"
        "</Project>\n"
    )


_CPP_JSON_HELPERS = r"""class __CodenJson {
public:
    static string readAll() {
        ostringstream buffer;
        buffer << cin.rdbuf();
        return buffer.str();
    }

    static string field(const string& json, const string& name) {
        string needle = "\"" + name + "\"";
        size_t pos = json.find(needle);
        if (pos == string::npos) return "null";
        pos = json.find(':', pos + needle.size());
        if (pos == string::npos) return "null";
        size_t start = pos + 1;
        while (start < json.size() && isspace(static_cast<unsigned char>(json[start]))) start++;
        size_t end = valueEnd(json, start);
        return json.substr(start, end - start);
    }

    static int toInt(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return 0;
        if (raw.front() == '"') raw = toString(raw);
        return stoi(raw);
    }

    static long long toLong(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return 0LL;
        if (raw.front() == '"') raw = toString(raw);
        return stoll(raw);
    }

    static double toDouble(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return 0.0;
        if (raw.front() == '"') raw = toString(raw);
        return stod(raw);
    }

    static bool toBool(string raw) {
        raw = trim(raw);
        return raw == "true" || raw == "1";
    }

    static string toString(string raw) {
        raw = trim(raw);
        if (raw == "null") return "";
        if (raw.size() < 2 || raw.front() != '"' || raw.back() != '"') return raw;
        string out;
        for (size_t i = 1; i + 1 < raw.size(); i++) {
            char ch = raw[i];
            if (ch == '\\' && i + 1 < raw.size()) {
                char escaped = raw[++i];
                if (escaped == 'n') out.push_back('\n');
                else if (escaped == 'r') out.push_back('\r');
                else if (escaped == 't') out.push_back('\t');
                else if (escaped == 'u') {
                    if (i + 4 < raw.size()) i += 4;
                    out.push_back('?');
                } else {
                    out.push_back(escaped);
                }
            } else {
                out.push_back(ch);
            }
        }
        return out;
    }

    static char toChar(const string& raw) {
        string value = toString(raw);
        return value.empty() ? '\0' : value[0];
    }

    static vector<int> toVectorInt(const string& raw) {
        vector<int> out;
        for (const string& item : splitArray(raw)) out.push_back(toInt(item));
        return out;
    }

    static optional<int> toOptionalInt(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return nullopt;
        return toInt(raw);
    }

    static optional<long long> toOptionalLong(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return nullopt;
        return toLong(raw);
    }

    static optional<double> toOptionalDouble(string raw) {
        raw = trim(raw);
        if (raw.empty() || raw == "null") return nullopt;
        return toDouble(raw);
    }

    static vector<optional<int>> toVectorOptionalInt(const string& raw) {
        vector<optional<int>> out;
        for (const string& item : splitArray(raw)) out.push_back(toOptionalInt(item));
        return out;
    }

    static vector<optional<long long>> toVectorOptionalLong(const string& raw) {
        vector<optional<long long>> out;
        for (const string& item : splitArray(raw)) out.push_back(toOptionalLong(item));
        return out;
    }

    static vector<optional<double>> toVectorOptionalDouble(const string& raw) {
        vector<optional<double>> out;
        for (const string& item : splitArray(raw)) out.push_back(toOptionalDouble(item));
        return out;
    }

    static vector<long long> toVectorLong(const string& raw) {
        vector<long long> out;
        for (const string& item : splitArray(raw)) out.push_back(toLong(item));
        return out;
    }

    static vector<double> toVectorDouble(const string& raw) {
        vector<double> out;
        for (const string& item : splitArray(raw)) out.push_back(toDouble(item));
        return out;
    }

    static vector<bool> toVectorBool(const string& raw) {
        vector<bool> out;
        for (const string& item : splitArray(raw)) out.push_back(toBool(item));
        return out;
    }

    static vector<string> toVectorString(const string& raw) {
        vector<string> out;
        for (const string& item : splitArray(raw)) out.push_back(toString(item));
        return out;
    }

    static vector<char> toVectorChar(const string& raw) {
        vector<char> out;
        for (const string& item : splitArray(raw)) out.push_back(toChar(item));
        return out;
    }

    static vector<vector<int>> toVectorVectorInt(const string& raw) {
        vector<vector<int>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorInt(item));
        return out;
    }

    static vector<vector<long long>> toVectorVectorLong(const string& raw) {
        vector<vector<long long>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorLong(item));
        return out;
    }

    static vector<vector<double>> toVectorVectorDouble(const string& raw) {
        vector<vector<double>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorDouble(item));
        return out;
    }

    static vector<vector<bool>> toVectorVectorBool(const string& raw) {
        vector<vector<bool>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorBool(item));
        return out;
    }

    static vector<vector<string>> toVectorVectorString(const string& raw) {
        vector<vector<string>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorString(item));
        return out;
    }

    static vector<vector<char>> toVectorVectorChar(const string& raw) {
        vector<vector<char>> out;
        for (const string& item : splitArray(raw)) out.push_back(toVectorChar(item));
        return out;
    }

    static unordered_map<int, int> toMapIntInt(const string& raw) {
        unordered_map<int, int> out;
        for (const auto& entry : objectEntries(raw)) out[toInt(entry.first)] = toInt(entry.second);
        return out;
    }

    static unordered_map<int, vector<int>> toMapIntVectorInt(const string& raw) {
        unordered_map<int, vector<int>> out;
        for (const auto& entry : objectEntries(raw)) out[toInt(entry.first)] = toVectorInt(entry.second);
        return out;
    }

    static string toJson(int value) { return to_string(value); }
    static string toJson(long long value) { return to_string(value); }
    static string toJson(double value) {
        ostringstream out;
        out << setprecision(17) << value;
        return out.str();
    }
    static string toJson(bool value) { return value ? "true" : "false"; }
    static string toJson(char value) { return quote(string(1, value)); }
    static string toJson(const string& value) { return quote(value); }
    static string toJson(const char* value) { return quote(string(value)); }

    template <typename T>
    static string toJson(const optional<T>& value) {
        return value.has_value() ? toJson(*value) : "null";
    }

    static string toJson(const vector<bool>& values) {
        string out = "[";
        for (size_t i = 0; i < values.size(); i++) {
            if (i) out += ",";
            out += values[i] ? "true" : "false";
        }
        out += "]";
        return out;
    }

    template <typename T>
    static string toJson(const vector<T>& values) {
        string out = "[";
        for (size_t i = 0; i < values.size(); i++) {
            if (i) out += ",";
            out += toJson(values[i]);
        }
        out += "]";
        return out;
    }

    template <typename T>
    static string toJson(const unordered_map<int, T>& values) {
        vector<int> keys;
        for (const auto& item : values) keys.push_back(item.first);
        sort(keys.begin(), keys.end());
        string out = "{";
        for (size_t i = 0; i < keys.size(); i++) {
            if (i) out += ",";
            out += quote(to_string(keys[i])) + ":" + toJson(values.at(keys[i]));
        }
        out += "}";
        return out;
    }

private:
    static string trim(string value) {
        size_t first = value.find_first_not_of(" \t\r\n");
        if (first == string::npos) return "";
        size_t last = value.find_last_not_of(" \t\r\n");
        return value.substr(first, last - first + 1);
    }

    static size_t valueEnd(const string& text, size_t start) {
        if (start >= text.size()) return start;
        if (text[start] == '"') {
            bool escaped = false;
            for (size_t i = start + 1; i < text.size(); i++) {
                if (escaped) {
                    escaped = false;
                } else if (text[i] == '\\') {
                    escaped = true;
                } else if (text[i] == '"') {
                    return i + 1;
                }
            }
            return text.size();
        }
        if (text[start] == '[' || text[start] == '{') {
            char open = text[start];
            char close = open == '[' ? ']' : '}';
            int depth = 0;
            bool inString = false;
            bool escaped = false;
            for (size_t i = start; i < text.size(); i++) {
                char ch = text[i];
                if (inString) {
                    if (escaped) escaped = false;
                    else if (ch == '\\') escaped = true;
                    else if (ch == '"') inString = false;
                    continue;
                }
                if (ch == '"') inString = true;
                else if (ch == open) depth++;
                else if (ch == close) {
                    depth--;
                    if (depth == 0) return i + 1;
                }
            }
            return text.size();
        }
        size_t end = start;
        while (end < text.size() && text[end] != ',' && text[end] != '}' && text[end] != ']') end++;
        while (end > start && isspace(static_cast<unsigned char>(text[end - 1]))) end--;
        return end;
    }

    static vector<string> splitArray(string raw) {
        raw = trim(raw);
        vector<string> items;
        if (raw.size() < 2 || raw.front() != '[' || raw.back() != ']') return items;
        size_t i = 1;
        while (i + 1 < raw.size()) {
            while (i + 1 < raw.size() && (isspace(static_cast<unsigned char>(raw[i])) || raw[i] == ',')) i++;
            if (i + 1 >= raw.size() || raw[i] == ']') break;
            size_t end = valueEnd(raw, i);
            items.push_back(raw.substr(i, end - i));
            i = end;
        }
        return items;
    }

    static vector<pair<string, string>> objectEntries(string raw) {
        raw = trim(raw);
        vector<pair<string, string>> entries;
        if (raw.size() < 2 || raw.front() != '{' || raw.back() != '}') return entries;
        size_t i = 1;
        while (i + 1 < raw.size()) {
            while (i + 1 < raw.size() && (isspace(static_cast<unsigned char>(raw[i])) || raw[i] == ',')) i++;
            if (i + 1 >= raw.size() || raw[i] == '}') break;
            size_t key_end = valueEnd(raw, i);
            string key = raw.substr(i, key_end - i);
            i = key_end;
            while (i < raw.size() && isspace(static_cast<unsigned char>(raw[i]))) i++;
            if (i >= raw.size() || raw[i] != ':') break;
            i++;
            while (i < raw.size() && isspace(static_cast<unsigned char>(raw[i]))) i++;
            size_t value_end = valueEnd(raw, i);
            entries.push_back({key, raw.substr(i, value_end - i)});
            i = value_end;
        }
        return entries;
    }

    static string quote(const string& value) {
        string out = "\"";
        for (char ch : value) {
            if (ch == '"' || ch == '\\') {
                out.push_back('\\');
                out.push_back(ch);
            } else if (ch == '\n') {
                out += "\\n";
            } else if (ch == '\r') {
                out += "\\r";
            } else if (ch == '\t') {
                out += "\\t";
            } else {
                out.push_back(ch);
            }
        }
        out += "\"";
        return out;
    }
};"""


_JAVA_JSON_HELPERS = r"""import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class Json {
    static String readAll() throws IOException {
        StringBuilder out = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int ch;
        while ((ch = reader.read()) != -1) {
            out.append((char) ch);
        }
        return out.toString();
    }

    static String field(String json, String name) {
        String needle = "\"" + name + "\"";
        int pos = json.indexOf(needle);
        if (pos < 0) return "null";
        pos = json.indexOf(':', pos + needle.length());
        if (pos < 0) return "null";
        int start = pos + 1;
        while (start < json.length() && Character.isWhitespace(json.charAt(start))) start++;
        int end = valueEnd(json, start);
        return json.substring(start, end);
    }

    static int asInt(String raw) {
        raw = trim(raw);
        if (raw.startsWith("\"")) raw = asString(raw);
        return raw.isEmpty() || raw.equals("null") ? 0 : Integer.parseInt(raw);
    }

    static long asLong(String raw) {
        raw = trim(raw);
        if (raw.startsWith("\"")) raw = asString(raw);
        return raw.isEmpty() || raw.equals("null") ? 0L : Long.parseLong(raw);
    }

    static double asDouble(String raw) {
        raw = trim(raw);
        if (raw.startsWith("\"")) raw = asString(raw);
        return raw.isEmpty() || raw.equals("null") ? 0.0 : Double.parseDouble(raw);
    }

    static boolean asBoolean(String raw) {
        raw = trim(raw);
        return raw.equals("true") || raw.equals("1");
    }

    static String asString(String raw) {
        raw = trim(raw);
        if (raw.equals("null")) return "";
        if (raw.length() < 2 || raw.charAt(0) != '"' || raw.charAt(raw.length() - 1) != '"') return raw;
        StringBuilder out = new StringBuilder();
        for (int i = 1; i + 1 < raw.length(); i++) {
            char ch = raw.charAt(i);
            if (ch == '\\' && i + 1 < raw.length()) {
                char escaped = raw.charAt(++i);
                if (escaped == 'n') out.append('\n');
                else if (escaped == 'r') out.append('\r');
                else if (escaped == 't') out.append('\t');
                else if (escaped == 'u') {
                    if (i + 4 < raw.length()) i += 4;
                    out.append('?');
                } else {
                    out.append(escaped);
                }
            } else {
                out.append(ch);
            }
        }
        return out.toString();
    }

    static Character asChar(String raw) {
        String value = asString(raw);
        return value.isEmpty() ? '\0' : value.charAt(0);
    }

    static boolean isNullLiteral(String raw) {
        raw = trim(raw);
        return raw.isEmpty() || raw.equals("null");
    }

    static List<Integer> listInt(String raw) {
        List<Integer> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(isNullLiteral(item) ? null : asInt(item));
        return out;
    }

    static List<Long> listLong(String raw) {
        List<Long> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(isNullLiteral(item) ? null : asLong(item));
        return out;
    }

    static List<Double> listDouble(String raw) {
        List<Double> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(isNullLiteral(item) ? null : asDouble(item));
        return out;
    }

    static List<Boolean> listBool(String raw) {
        List<Boolean> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(isNullLiteral(item) ? null : asBoolean(item));
        return out;
    }

    static List<String> listString(String raw) {
        List<String> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(asString(item));
        return out;
    }

    static List<Character> listChar(String raw) {
        List<Character> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(isNullLiteral(item) ? null : asChar(item));
        return out;
    }

    static List<List<Integer>> listListInt(String raw) {
        List<List<Integer>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listInt(item));
        return out;
    }

    static List<List<Long>> listListLong(String raw) {
        List<List<Long>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listLong(item));
        return out;
    }

    static List<List<Double>> listListDouble(String raw) {
        List<List<Double>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listDouble(item));
        return out;
    }

    static List<List<Boolean>> listListBool(String raw) {
        List<List<Boolean>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listBool(item));
        return out;
    }

    static List<List<String>> listListString(String raw) {
        List<List<String>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listString(item));
        return out;
    }

    static List<List<Character>> listListChar(String raw) {
        List<List<Character>> out = new ArrayList<>();
        for (String item : splitArray(raw)) out.add(listChar(item));
        return out;
    }

    static Map<Integer, Integer> mapIntInt(String raw) {
        Map<Integer, Integer> out = new LinkedHashMap<>();
        for (Map.Entry<String, String> entry : objectEntries(raw).entrySet()) {
            out.put(asInt(entry.getKey()), asInt(entry.getValue()));
        }
        return out;
    }

    static Map<Integer, List<Integer>> mapIntListInt(String raw) {
        Map<Integer, List<Integer>> out = new LinkedHashMap<>();
        for (Map.Entry<String, String> entry : objectEntries(raw).entrySet()) {
            out.put(asInt(entry.getKey()), listInt(entry.getValue()));
        }
        return out;
    }

    static String toJson(Object value) {
        if (value == null) return "null";
        if (value instanceof String) return quote((String) value);
        if (value instanceof Character) return quote(String.valueOf(value));
        if (value instanceof Boolean || value instanceof Number) return String.valueOf(value);
        if (value instanceof List<?>) {
            List<?> values = (List<?>) value;
            StringBuilder out = new StringBuilder("[");
            for (int i = 0; i < values.size(); i++) {
                if (i > 0) out.append(",");
                out.append(toJson(values.get(i)));
            }
            out.append("]");
            return out.toString();
        }
        if (value instanceof Map<?, ?>) {
            Map<?, ?> values = (Map<?, ?>) value;
            List<Object> keys = new ArrayList<>(values.keySet());
            keys.sort((a, b) -> String.valueOf(a).compareTo(String.valueOf(b)));
            StringBuilder out = new StringBuilder("{");
            for (int i = 0; i < keys.size(); i++) {
                if (i > 0) out.append(",");
                Object key = keys.get(i);
                out.append(quote(String.valueOf(key))).append(":").append(toJson(values.get(key)));
            }
            out.append("}");
            return out.toString();
        }
        if (value.getClass().isArray()) {
            StringBuilder out = new StringBuilder("[");
            int length = Array.getLength(value);
            for (int i = 0; i < length; i++) {
                if (i > 0) out.append(",");
                out.append(toJson(Array.get(value, i)));
            }
            out.append("]");
            return out.toString();
        }
        return quote(String.valueOf(value));
    }

    private static String trim(String value) {
        return value == null ? "" : value.trim();
    }

    private static int valueEnd(String text, int start) {
        if (start >= text.length()) return start;
        if (text.charAt(start) == '"') {
            boolean escaped = false;
            for (int i = start + 1; i < text.length(); i++) {
                char ch = text.charAt(i);
                if (escaped) escaped = false;
                else if (ch == '\\') escaped = true;
                else if (ch == '"') return i + 1;
            }
            return text.length();
        }
        if (text.charAt(start) == '[' || text.charAt(start) == '{') {
            char open = text.charAt(start);
            char close = open == '[' ? ']' : '}';
            int depth = 0;
            boolean inString = false;
            boolean escaped = false;
            for (int i = start; i < text.length(); i++) {
                char ch = text.charAt(i);
                if (inString) {
                    if (escaped) escaped = false;
                    else if (ch == '\\') escaped = true;
                    else if (ch == '"') inString = false;
                    continue;
                }
                if (ch == '"') inString = true;
                else if (ch == open) depth++;
                else if (ch == close) {
                    depth--;
                    if (depth == 0) return i + 1;
                }
            }
            return text.length();
        }
        int end = start;
        while (end < text.length() && text.charAt(end) != ',' && text.charAt(end) != '}' && text.charAt(end) != ']') end++;
        while (end > start && Character.isWhitespace(text.charAt(end - 1))) end--;
        return end;
    }

    private static List<String> splitArray(String raw) {
        raw = trim(raw);
        List<String> items = new ArrayList<>();
        if (raw.length() < 2 || raw.charAt(0) != '[' || raw.charAt(raw.length() - 1) != ']') return items;
        int i = 1;
        while (i + 1 < raw.length()) {
            while (i + 1 < raw.length() && (Character.isWhitespace(raw.charAt(i)) || raw.charAt(i) == ',')) i++;
            if (i + 1 >= raw.length() || raw.charAt(i) == ']') break;
            int end = valueEnd(raw, i);
            items.add(raw.substring(i, end));
            i = end;
        }
        return items;
    }

    private static Map<String, String> objectEntries(String raw) {
        raw = trim(raw);
        Map<String, String> entries = new LinkedHashMap<>();
        if (raw.length() < 2 || raw.charAt(0) != '{' || raw.charAt(raw.length() - 1) != '}') return entries;
        int i = 1;
        while (i + 1 < raw.length()) {
            while (i + 1 < raw.length() && (Character.isWhitespace(raw.charAt(i)) || raw.charAt(i) == ',')) i++;
            if (i + 1 >= raw.length() || raw.charAt(i) == '}') break;
            int keyEnd = valueEnd(raw, i);
            String key = raw.substring(i, keyEnd);
            i = keyEnd;
            while (i < raw.length() && Character.isWhitespace(raw.charAt(i))) i++;
            if (i >= raw.length() || raw.charAt(i) != ':') break;
            i++;
            while (i < raw.length() && Character.isWhitespace(raw.charAt(i))) i++;
            int valueEnd = valueEnd(raw, i);
            entries.put(key, raw.substring(i, valueEnd));
            i = valueEnd;
        }
        return entries;
    }

    private static String quote(String value) {
        StringBuilder out = new StringBuilder("\"");
        for (int i = 0; i < value.length(); i++) {
            char ch = value.charAt(i);
            if (ch == '"' || ch == '\\') {
                out.append('\\').append(ch);
            } else if (ch == '\n') {
                out.append("\\n");
            } else if (ch == '\r') {
                out.append("\\r");
            } else if (ch == '\t') {
                out.append("\\t");
            } else if (ch < 32) {
                out.append(String.format("\\u%04x", (int) ch));
            } else {
                out.append(ch);
            }
        }
        out.append("\"");
        return out.toString();
    }
}
"""


_KOTLIN_JSON_HELPERS = r"""object CodenJson {
    fun readAll(): String {
        val reader = System.`in`.bufferedReader()
        val out = StringBuilder()
        while (true) {
            val ch = reader.read()
            if (ch == -1) break
            out.append(ch.toChar())
        }
        return out.toString()
    }

    fun field(json: String, name: String): String {
        val needle = "\"" + name + "\""
        var pos = json.indexOf(needle)
        if (pos < 0) return "null"
        pos = json.indexOf(':', pos + needle.length)
        if (pos < 0) return "null"
        var start = pos + 1
        while (start < json.length && json[start].isWhitespace()) start++
        val end = valueEnd(json, start)
        return json.substring(start, end)
    }

    fun asInt(rawInput: String): Int {
        var raw = trim(rawInput)
        if (raw.startsWith("\"")) raw = asString(raw)
        return if (raw.isEmpty() || raw == "null") 0 else raw.toInt()
    }

    fun asLong(rawInput: String): Long {
        var raw = trim(rawInput)
        if (raw.startsWith("\"")) raw = asString(raw)
        return if (raw.isEmpty() || raw == "null") 0L else raw.toLong()
    }

    fun asDouble(rawInput: String): Double {
        var raw = trim(rawInput)
        if (raw.startsWith("\"")) raw = asString(raw)
        return if (raw.isEmpty() || raw == "null") 0.0 else raw.toDouble()
    }

    fun asBoolean(rawInput: String): Boolean {
        val raw = trim(rawInput)
        return raw == "true" || raw == "1"
    }

    fun asString(rawInput: String): String {
        val raw = trim(rawInput)
        if (raw == "null") return ""
        if (raw.length < 2 || raw[0] != '"' || raw[raw.length - 1] != '"') return raw
        val out = StringBuilder()
        var i = 1
        while (i + 1 < raw.length) {
            val ch = raw[i]
            if (ch == '\\' && i + 1 < raw.length) {
                val escaped = raw[++i]
                when (escaped) {
                    'n' -> out.append('\n')
                    'r' -> out.append('\r')
                    't' -> out.append('\t')
                    'u' -> {
                        if (i + 4 < raw.length) i += 4
                        out.append('?')
                    }
                    else -> out.append(escaped)
                }
            } else {
                out.append(ch)
            }
            i++
        }
        return out.toString()
    }

    fun asChar(raw: String): Char {
        val value = asString(raw)
        return if (value.isEmpty()) '\u0000' else value[0]
    }

    fun isNullLiteral(rawInput: String): Boolean {
        val raw = trim(rawInput)
        return raw.isEmpty() || raw == "null"
    }

    fun listInt(raw: String): MutableList<Int> {
        val out = mutableListOf<Int>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) 0 else asInt(item))
        return out
    }

    fun listNullableInt(raw: String): MutableList<Int?> {
        val out = mutableListOf<Int?>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) null else asInt(item))
        return out
    }

    fun listLong(raw: String): MutableList<Long> {
        val out = mutableListOf<Long>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) 0L else asLong(item))
        return out
    }

    fun listNullableLong(raw: String): MutableList<Long?> {
        val out = mutableListOf<Long?>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) null else asLong(item))
        return out
    }

    fun listDouble(raw: String): MutableList<Double> {
        val out = mutableListOf<Double>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) 0.0 else asDouble(item))
        return out
    }

    fun listNullableDouble(raw: String): MutableList<Double?> {
        val out = mutableListOf<Double?>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) null else asDouble(item))
        return out
    }

    fun listBool(raw: String): MutableList<Boolean> {
        val out = mutableListOf<Boolean>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) false else asBoolean(item))
        return out
    }

    fun listString(raw: String): MutableList<String> {
        val out = mutableListOf<String>()
        for (item in splitArray(raw)) out.add(asString(item))
        return out
    }

    fun listChar(raw: String): MutableList<Char> {
        val out = mutableListOf<Char>()
        for (item in splitArray(raw)) out.add(if (isNullLiteral(item)) '\u0000' else asChar(item))
        return out
    }

    fun listListInt(raw: String): MutableList<MutableList<Int>> {
        val out = mutableListOf<MutableList<Int>>()
        for (item in splitArray(raw)) out.add(listInt(item))
        return out
    }

    fun listListLong(raw: String): MutableList<MutableList<Long>> {
        val out = mutableListOf<MutableList<Long>>()
        for (item in splitArray(raw)) out.add(listLong(item))
        return out
    }

    fun listListDouble(raw: String): MutableList<MutableList<Double>> {
        val out = mutableListOf<MutableList<Double>>()
        for (item in splitArray(raw)) out.add(listDouble(item))
        return out
    }

    fun listListBool(raw: String): MutableList<MutableList<Boolean>> {
        val out = mutableListOf<MutableList<Boolean>>()
        for (item in splitArray(raw)) out.add(listBool(item))
        return out
    }

    fun listListString(raw: String): MutableList<MutableList<String>> {
        val out = mutableListOf<MutableList<String>>()
        for (item in splitArray(raw)) out.add(listString(item))
        return out
    }

    fun listListChar(raw: String): MutableList<MutableList<Char>> {
        val out = mutableListOf<MutableList<Char>>()
        for (item in splitArray(raw)) out.add(listChar(item))
        return out
    }

    fun mapIntInt(raw: String): MutableMap<Int, Int> {
        val out = linkedMapOf<Int, Int>()
        for ((key, value) in objectEntries(raw)) out[asInt(key)] = asInt(value)
        return out
    }

    fun mapIntListInt(raw: String): MutableMap<Int, MutableList<Int>> {
        val out = linkedMapOf<Int, MutableList<Int>>()
        for ((key, value) in objectEntries(raw)) out[asInt(key)] = listInt(value)
        return out
    }

    fun toJson(value: Any?): String {
        return when (value) {
            null -> "null"
            is String -> quote(value)
            is Char -> quote(value.toString())
            is Boolean -> value.toString()
            is Number -> value.toString()
            is IntArray -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is LongArray -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is DoubleArray -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is BooleanArray -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is CharArray -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is Array<*> -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is Iterable<*> -> value.joinToString(prefix = "[", postfix = "]") { toJson(it) }
            is Map<*, *> -> {
                val keys = value.keys.sortedBy { it.toString() }
                keys.joinToString(prefix = "{", postfix = "}") { key ->
                    quote(key.toString()) + ":" + toJson(value[key])
                }
            }
            else -> quote(value.toString())
        }
    }

    private fun trim(value: String?): String = value?.trim() ?: ""

    private fun valueEnd(text: String, start: Int): Int {
        if (start >= text.length) return start
        if (text[start] == '"') {
            var escaped = false
            var i = start + 1
            while (i < text.length) {
                val ch = text[i]
                if (escaped) escaped = false
                else if (ch == '\\') escaped = true
                else if (ch == '"') return i + 1
                i++
            }
            return text.length
        }
        if (text[start] == '[' || text[start] == '{') {
            val open = text[start]
            val close = if (open == '[') ']' else '}'
            var depth = 0
            var inString = false
            var escaped = false
            var i = start
            while (i < text.length) {
                val ch = text[i]
                if (inString) {
                    if (escaped) escaped = false
                    else if (ch == '\\') escaped = true
                    else if (ch == '"') inString = false
                    i++
                    continue
                }
                if (ch == '"') inString = true
                else if (ch == open) depth++
                else if (ch == close) {
                    depth--
                    if (depth == 0) return i + 1
                }
                i++
            }
            return text.length
        }
        var end = start
        while (end < text.length && text[end] != ',' && text[end] != '}' && text[end] != ']') end++
        while (end > start && text[end - 1].isWhitespace()) end--
        return end
    }

    private fun splitArray(rawInput: String): MutableList<String> {
        val raw = trim(rawInput)
        val items = mutableListOf<String>()
        if (raw.length < 2 || raw[0] != '[' || raw[raw.length - 1] != ']') return items
        var i = 1
        while (i + 1 < raw.length) {
            while (i + 1 < raw.length && (raw[i].isWhitespace() || raw[i] == ',')) i++
            if (i + 1 >= raw.length || raw[i] == ']') break
            val end = valueEnd(raw, i)
            items.add(raw.substring(i, end))
            i = end
        }
        return items
    }

    private fun objectEntries(rawInput: String): MutableMap<String, String> {
        val raw = trim(rawInput)
        val entries = linkedMapOf<String, String>()
        if (raw.length < 2 || raw[0] != '{' || raw[raw.length - 1] != '}') return entries
        var i = 1
        while (i + 1 < raw.length) {
            while (i + 1 < raw.length && (raw[i].isWhitespace() || raw[i] == ',')) i++
            if (i + 1 >= raw.length || raw[i] == '}') break
            val keyEnd = valueEnd(raw, i)
            val key = raw.substring(i, keyEnd)
            i = keyEnd
            while (i < raw.length && raw[i].isWhitespace()) i++
            if (i >= raw.length || raw[i] != ':') break
            i++
            while (i < raw.length && raw[i].isWhitespace()) i++
            val itemEnd = valueEnd(raw, i)
            entries[key] = raw.substring(i, itemEnd)
            i = itemEnd
        }
        return entries
    }

    private fun quote(value: String): String {
        val out = StringBuilder("\"")
        for (ch in value) {
            when (ch) {
                '"' -> out.append("\\\"")
                '\\' -> out.append("\\\\")
                '\n' -> out.append("\\n")
                '\r' -> out.append("\\r")
                '\t' -> out.append("\\t")
                else -> {
                    if (ch.code < 32) out.append(String.format("\\u%04x", ch.code))
                    else out.append(ch)
                }
            }
        }
        out.append('"')
        return out.toString()
    }
}
"""


def _cpp_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
) -> str:
    declarations: list[str] = []
    call_args: list[str] = []
    values = param_values or {}
    for name in param_names:
        var_name = _harness_identifier(name)
        hint_type = _cpp_type_for_hint(_name_hint(name, param_hints.get(name, name)))
        cpp_type = _prefer_hint_for_ambiguous_value(_cpp_type_for_value(values.get(name)), hint_type)
        reader = _cpp_reader_for_type(cpp_type)
        declarations.append(
            f'    {cpp_type} {var_name} = __CodenJson::{reader}(__CodenJson::field(__json, "{name}"));'
        )
        call_args.append(var_name)

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    timing_start = "    auto __coden_start = chrono::steady_clock::now();\n" if measure_runtime else ""
    timing_end = (
        "    auto __coden_end = chrono::steady_clock::now();\n"
        f'    cerr << "{_RUNTIME_MARKER}" << fixed << setprecision(6) << chrono::duration<double, milli>(__coden_end - __coden_start).count() << endl;\n'
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"    solution.solve({call});\n"
            + timing_end
            + f"    cout << __CodenJson::toJson({call_args[0]}) << endl;"
        )
    else:
        body = (
            timing_start
            + f"    auto result = solution.solve({call});\n"
            + timing_end
            + "    cout << __CodenJson::toJson(result) << endl;"
        )

    json_source = (
        "__CodenJson::readAll()"
        if input_json is None
        else json.dumps(input_json)
    )

    return (
        _CPP_JSON_HELPERS
        + "\n\n"
        "int main() {\n"
        f"    string __json = {json_source};\n"
        + "\n".join(declarations)
        + "\n"
        "    Solution solution;\n"
        f"{body}\n"
        "    return 0;\n"
        "}\n"
    )


def _java_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
) -> str:
    declarations: list[str] = []
    call_args: list[str] = []
    values = param_values or {}
    for name in param_names:
        var_name = _harness_identifier(name)
        hint_type = _java_type_for_hint(_name_hint(name, param_hints.get(name, name)))
        java_type = _prefer_hint_for_ambiguous_value(_java_type_for_value(values.get(name)), hint_type)
        reader = _java_reader_for_type(java_type)
        declarations.append(
            f'        {java_type} {var_name} = Json.{reader}(Json.field(json, "{name}"));'
        )
        call_args.append(var_name)

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    timing_start = "        long __codenStart = System.nanoTime();\n" if measure_runtime else ""
    timing_end = (
        f'        System.err.printf(Locale.US, "{_RUNTIME_MARKER}%.6f%n", (System.nanoTime() - __codenStart) / 1000000.0);\n'
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"        solution.solve({call});\n"
            + timing_end
            + f"        System.out.println(Json.toJson({call_args[0]}));"
        )
    else:
        body = (
            timing_start
            + f"        Object result = solution.solve({call});\n"
            + timing_end
            + "        System.out.println(Json.toJson(result));"
        )

    json_source = "Json.readAll()" if input_json is None else json.dumps(input_json)

    return (
        _JAVA_JSON_HELPERS
        + "\n"
        "class Main {\n"
        "    public static void main(String[] args) throws Exception {\n"
        f"        String json = {json_source};\n"
        + "\n".join(declarations)
        + "\n"
        "        Solution solution = new Solution();\n"
        f"{body}\n"
        "    }\n"
        "}\n"
    )


def _csharp_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
) -> str:
    properties: list[str] = []
    call_args: list[str] = []
    values = param_values or {}
    for name in param_names:
        prop = _csharp_identifier(name)
        hint_type = _csharp_type_for_hint(_name_hint(name, param_hints.get(name, name)))
        csharp_type = _prefer_hint_for_ambiguous_value(_csharp_type_for_value(values.get(name)), hint_type)
        properties.extend(
            [
                f'        [JsonPropertyName("{name}")]',
                f"        public {csharp_type} {prop} {{ get; set; }} = {_csharp_default(csharp_type)};",
            ]
        )
        call_args.append(f"input.{prop}")

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    timing_start = "        long __codenStart = Stopwatch.GetTimestamp();\n" if measure_runtime else ""
    timing_end = (
        f'        Console.Error.WriteLine("{_RUNTIME_MARKER}" + (((Stopwatch.GetTimestamp() - __codenStart) * 1000.0) / Stopwatch.Frequency).ToString("F6", CultureInfo.InvariantCulture));\n'
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"        solution.Solve({call});\n"
            + timing_end
            + f"        Console.WriteLine(JsonSerializer.Serialize({call_args[0]}, JsonOptions));"
        )
    else:
        body = (
            timing_start
            + f"        var result = solution.Solve({call});\n"
            + timing_end
            + "        Console.WriteLine(JsonSerializer.Serialize(result, JsonOptions));"
        )
    json_source = (
        "Console.In.ReadToEnd()"
        if input_json is None
        else json.dumps(input_json)
    )

    return (
        "using System;\n"
        "using System.Collections.Generic;\n"
        "using System.Diagnostics;\n"
        "using System.Globalization;\n"
        "using System.Text.Json;\n"
        "using System.Text.Json.Serialization;\n\n"
        "public class Program\n"
        "{\n"
        "    private static readonly JsonSerializerOptions JsonOptions = new JsonSerializerOptions\n"
        "    {\n"
        "        PropertyNameCaseInsensitive = true,\n"
        "        Converters = { new StringifiedStringConverter() }\n"
        "    };\n\n"
        "    public static int Main(string[] args)\n"
        "    {\n"
        f"        string json = {json_source};\n"
        "        InputModel input = JsonSerializer.Deserialize<InputModel>(json, JsonOptions) ?? new InputModel();\n"
        "        Solution solution = new Solution();\n"
        f"{body}\n"
        "        return 0;\n"
        "    }\n\n"
        "    public class InputModel\n"
        "    {\n"
        + "\n".join(properties)
        + "\n"
        "    }\n"
        "\n"
        "    public class StringifiedStringConverter : JsonConverter<string>\n"
        "    {\n"
        "        public override string Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)\n"
        "        {\n"
        "            if (reader.TokenType == JsonTokenType.String) return reader.GetString() ?? \"\";\n"
        "            if (reader.TokenType == JsonTokenType.Number)\n"
        "            {\n"
        "                if (reader.TryGetInt64(out long longValue)) return longValue.ToString(CultureInfo.InvariantCulture);\n"
        "                return reader.GetDouble().ToString(\"R\", CultureInfo.InvariantCulture);\n"
        "            }\n"
        "            if (reader.TokenType == JsonTokenType.True) return \"true\";\n"
        "            if (reader.TokenType == JsonTokenType.False) return \"false\";\n"
        "            if (reader.TokenType == JsonTokenType.Null) return \"\";\n"
        "            using JsonDocument document = JsonDocument.ParseValue(ref reader);\n"
        "            return document.RootElement.ToString();\n"
        "        }\n\n"
        "        public override void Write(Utf8JsonWriter writer, string value, JsonSerializerOptions options)\n"
        "        {\n"
        "            writer.WriteStringValue(value);\n"
        "        }\n"
        "    }\n"
        "}\n"
    )


def _javascript_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
    runtime_iterations: int = 1,
) -> str:
    del param_hints, param_values
    declarations: list[str] = []
    call_args: list[str] = []
    for name in param_names:
        var_name = _harness_identifier(name)
        declarations.append(f'const {var_name} = __input[{json.dumps(name)}];')
        call_args.append(var_name)

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    iterations = max(1, int(runtime_iterations)) if measure_runtime and not in_place else 1
    timing_start = "const __codenStart = process.hrtime.bigint();\n" if measure_runtime else ""
    timing_end = (
        f"process.stderr.write(`{_RUNTIME_MARKER}${{(Number(process.hrtime.bigint() - __codenStart) / 1e6).toFixed(6)}}\\n`);\n"
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"solution.solve({call});\n"
            + timing_end
            + f"__codenPrintJson({call_args[0]});"
        )
    elif measure_runtime:
        body = (
            timing_start
            + "let result;\n"
            + f"for (let __codenI = 0; __codenI < {iterations}; __codenI++) {{\n"
            + f"    result = solution.solve({call});\n"
            + "}\n"
            + timing_end
            + "__codenPrintJson(result);"
        )
    else:
        body = (
            f"const result = solution.solve({call});\n"
            + "__codenPrintJson(result);"
        )

    json_source = "__codenReadAll()" if input_json is None else json.dumps(input_json)
    return (
        "const __codenFs = require(\"fs\");\n\n"
        "function __codenReadAll() {\n"
        "    return __codenFs.readFileSync(0, \"utf8\");\n"
        "}\n\n"
        "function __codenNormalize(value) {\n"
        "    if (value === undefined) return null;\n"
        "    if (typeof value === \"bigint\") return Number(value);\n"
        "    if (value instanceof Map) {\n"
        "        const obj = {};\n"
        "        for (const [key, item] of value.entries()) {\n"
        "            obj[String(key)] = __codenNormalize(item);\n"
        "        }\n"
        "        return obj;\n"
        "    }\n"
        "    if (value instanceof Set) {\n"
        "        return Array.from(value, __codenNormalize);\n"
        "    }\n"
        "    if (Array.isArray(value)) {\n"
        "        return value.map(__codenNormalize);\n"
        "    }\n"
        "    if (value && typeof value === \"object\") {\n"
        "        const obj = {};\n"
        "        for (const [key, item] of Object.entries(value)) {\n"
        "            obj[String(key)] = __codenNormalize(item);\n"
        "        }\n"
        "        return obj;\n"
        "    }\n"
        "    return value;\n"
        "}\n\n"
        "function __codenPrintJson(value) {\n"
        "    const encoded = JSON.stringify(__codenNormalize(value));\n"
        "    console.log(encoded === undefined ? \"null\" : encoded);\n"
        "}\n\n"
        f"const __json = {json_source};\n"
        "const __input = JSON.parse(__json || \"{}\");\n"
        + "\n".join(declarations)
        + "\n"
        "const solution = new Solution();\n"
        f"{body}\n"
    )


def _go_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
) -> str:
    declarations: list[str] = []
    call_args: list[str] = []
    values = param_values or {}
    for name in param_names:
        var_name = _harness_identifier(name)
        hint_type = _go_type_for_hint(_name_hint(name, param_hints.get(name, name)))
        go_type = _prefer_go_hint_for_ambiguous_value(_go_type_for_value(values.get(name)), hint_type)
        raw_field = f'__CodenField(__input, "{name}")'
        if go_type == "string":
            declarations.append(f"{var_name} := __CodenString({raw_field})")
        elif go_type == "[]string":
            declarations.append(f"{var_name} := __CodenStringSlice({raw_field})")
        elif go_type == "[][]string":
            declarations.append(f"{var_name} := __CodenStringMatrix({raw_field})")
        elif go_type == "[]rune":
            declarations.append(f"{var_name} := __CodenRuneSlice({raw_field})")
        elif go_type == "[][]rune":
            declarations.append(f"{var_name} := __CodenRuneMatrix({raw_field})")
        else:
            declarations.extend(
                [
                    f"var {var_name} {go_type}",
                    f"__CodenMustDecode({raw_field}, &{var_name})",
                ]
            )
        call_args.append(var_name)

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    timing_start = "__codenStart := time.Now()\n" if measure_runtime else ""
    timing_end = (
        f"fmt.Fprintf(os.Stderr, \"{_RUNTIME_MARKER}%.6f\\n\", float64(time.Since(__codenStart).Nanoseconds())/1e6)\n"
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"solve({call})\n"
            + timing_end
            + f"__CodenPrintJSON({call_args[0]})"
        )
    else:
        body = (
            timing_start
            + f"result := solve({call})\n"
            + timing_end
            + "__CodenPrintJSON(result)"
        )

    json_source = "__CodenReadAll()" if input_json is None else json.dumps(input_json)
    indented_declarations = "\n".join(f"\t{line}" for line in declarations)
    indented_body = "\n".join(f"\t{line}" for line in body.splitlines())
    time_import = '\t"time"\n' if measure_runtime else ""
    return (
        "package main\n\n"
        "import (\n"
        "\t\"bytes\"\n"
        "\t\"encoding/json\"\n"
        "\t\"fmt\"\n"
        "\t\"io\"\n"
        "\t\"os\"\n"
        f"{time_import}"
        ")\n\n"
        "func __CodenReadAll() string {\n"
        "\tdata, err := io.ReadAll(os.Stdin)\n"
        "\tif err != nil {\n"
        "\t\tpanic(err)\n"
        "\t}\n"
        "\treturn string(data)\n"
        "}\n\n"
        "func __CodenObject(text string) map[string]json.RawMessage {\n"
        "\tvar obj map[string]json.RawMessage\n"
        "\tif text == \"\" {\n"
        "\t\ttext = \"{}\"\n"
        "\t}\n"
        "\tif err := json.Unmarshal([]byte(text), &obj); err != nil {\n"
        "\t\tpanic(err)\n"
        "\t}\n"
        "\tif obj == nil {\n"
        "\t\treturn map[string]json.RawMessage{}\n"
        "\t}\n"
        "\treturn obj\n"
        "}\n\n"
        "func __CodenField(obj map[string]json.RawMessage, name string) json.RawMessage {\n"
        "\tif raw, ok := obj[name]; ok && len(raw) > 0 {\n"
        "\t\treturn raw\n"
        "\t}\n"
        "\treturn json.RawMessage(\"null\")\n"
        "}\n\n"
        "func __CodenMustDecode(raw json.RawMessage, target any) {\n"
        "\tif len(raw) == 0 {\n"
        "\t\traw = json.RawMessage(\"null\")\n"
        "\t}\n"
        "\tif err := json.Unmarshal(raw, target); err != nil {\n"
        "\t\tpanic(err)\n"
        "\t}\n"
        "}\n\n"
        "func __CodenAny(raw json.RawMessage) any {\n"
        "\tdecoder := json.NewDecoder(bytes.NewReader(raw))\n"
        "\tdecoder.UseNumber()\n"
        "\tvar value any\n"
        "\tif err := decoder.Decode(&value); err != nil {\n"
        "\t\tpanic(err)\n"
        "\t}\n"
        "\treturn value\n"
        "}\n\n"
        "func __CodenString(raw json.RawMessage) string {\n"
        "\tswitch value := __CodenAny(raw).(type) {\n"
        "\tcase nil:\n"
        "\t\treturn \"\"\n"
        "\tcase string:\n"
        "\t\treturn value\n"
        "\tcase json.Number:\n"
        "\t\treturn value.String()\n"
        "\tcase bool:\n"
        "\t\tif value {\n"
        "\t\t\treturn \"true\"\n"
        "\t\t}\n"
        "\t\treturn \"false\"\n"
        "\tdefault:\n"
        "\t\tencoded, err := json.Marshal(value)\n"
        "\t\tif err != nil {\n"
        "\t\t\tpanic(err)\n"
        "\t\t}\n"
        "\t\treturn string(encoded)\n"
        "\t}\n"
        "}\n\n"
        "func __CodenStringSlice(raw json.RawMessage) []string {\n"
        "\tif string(raw) == \"null\" {\n"
        "\t\treturn nil\n"
        "\t}\n"
        "\tvar values []json.RawMessage\n"
        "\t__CodenMustDecode(raw, &values)\n"
        "\tout := make([]string, len(values))\n"
        "\tfor i, item := range values {\n"
        "\t\tout[i] = __CodenString(item)\n"
        "\t}\n"
        "\treturn out\n"
        "}\n\n"
        "func __CodenStringMatrix(raw json.RawMessage) [][]string {\n"
        "\tif string(raw) == \"null\" {\n"
        "\t\treturn nil\n"
        "\t}\n"
        "\tvar rows []json.RawMessage\n"
        "\t__CodenMustDecode(raw, &rows)\n"
        "\tout := make([][]string, len(rows))\n"
        "\tfor i, row := range rows {\n"
        "\t\tout[i] = __CodenStringSlice(row)\n"
        "\t}\n"
        "\treturn out\n"
        "}\n\n"
        "func __CodenRuneSlice(raw json.RawMessage) []rune {\n"
        "\titems := __CodenStringSlice(raw)\n"
        "\tout := make([]rune, len(items))\n"
        "\tfor i, item := range items {\n"
        "\t\trunes := []rune(item)\n"
        "\t\tif len(runes) > 0 {\n"
        "\t\t\tout[i] = runes[0]\n"
        "\t\t}\n"
        "\t}\n"
        "\treturn out\n"
        "}\n\n"
        "func __CodenRuneMatrix(raw json.RawMessage) [][]rune {\n"
        "\tif string(raw) == \"null\" {\n"
        "\t\treturn nil\n"
        "\t}\n"
        "\tvar rows []json.RawMessage\n"
        "\t__CodenMustDecode(raw, &rows)\n"
        "\tout := make([][]rune, len(rows))\n"
        "\tfor i, row := range rows {\n"
        "\t\tout[i] = __CodenRuneSlice(row)\n"
        "\t}\n"
        "\treturn out\n"
        "}\n\n"
        "func __CodenPrintJSON(value any) {\n"
        "\tencoded, err := json.Marshal(value)\n"
        "\tif err != nil {\n"
        "\t\tpanic(err)\n"
        "\t}\n"
        "\tfmt.Println(string(encoded))\n"
        "}\n\n"
        "func main() {\n"
        f"\t__json := {json_source}\n"
        "\t__input := __CodenObject(__json)\n"
        f"{indented_declarations}\n"
        f"{indented_body}\n"
        "}\n"
    )


def _kotlin_function_harness(
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str | None = None,
    param_values: dict[str, object] | None = None,
    measure_runtime: bool = False,
) -> str:
    declarations: list[str] = []
    call_args: list[str] = []
    values = param_values or {}
    for name in param_names:
        var_name = _harness_identifier(name)
        hint_type = _kotlin_type_for_hint(_name_hint(name, param_hints.get(name, name)))
        kotlin_type = _prefer_kotlin_hint_for_ambiguous_value(
            _kotlin_type_for_value(values.get(name)),
            hint_type,
        )
        reader = _kotlin_reader_for_type(kotlin_type)
        declarations.append(
            f'    val {var_name}: {kotlin_type} = CodenJson.{reader}(CodenJson.field(json, "{name}"))'
        )
        call_args.append(var_name)

    call = ", ".join(call_args)
    in_place = _is_in_place_return(returns_hint)
    timing_start = "    val __codenStart = System.nanoTime()\n" if measure_runtime else ""
    timing_end = (
        f'    System.err.println(String.format(java.util.Locale.US, "{_RUNTIME_MARKER}%.6f", (System.nanoTime() - __codenStart) / 1000000.0))\n'
        if measure_runtime else ""
    )
    if in_place and call_args:
        body = (
            timing_start
            + f"    solution.solve({call})\n"
            + timing_end
            + f"    println(CodenJson.toJson({call_args[0]}))"
        )
    else:
        body = (
            timing_start
            + f"    val result = solution.solve({call})\n"
            + timing_end
            + "    println(CodenJson.toJson(result))"
        )

    json_source = "CodenJson.readAll()" if input_json is None else _kotlin_string_literal(input_json)
    return (
        _KOTLIN_JSON_HELPERS
        + "\n\n"
        "fun main() {\n"
        f"    val json = {json_source}\n"
        + "\n".join(declarations)
        + "\n"
        "    val solution = Solution()\n"
        f"{body}\n"
        "}\n"
    )


def _hint_text(type_hint: str) -> str:
    return type_hint.replace("`", "").replace("â€”", " ").replace("-", " ").lower()


def _name_hint(name: str, type_hint: str) -> str:
    hint = str(type_hint or name)
    return f"{name} {hint}" if name and name != hint else hint


def _has_word(text: str, *words: str) -> bool:
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in words)


def _starts_with_word(text: str, *words: str) -> bool:
    return any(re.match(rf"\s*{re.escape(word)}\b", text) for word in words)


_SCALAR_INT_START_WORDS = (
    "n",
    "m",
    "k",
    "q",
    "target",
    "capacity",
    "amount",
    "size",
    "length",
    "row",
    "col",
    "key",
    "val",
    "value",
    "index",
    "count",
    "src",
    "dest",
    "left",
    "right",
    "divisor",
    "dividend",
)


def _is_bool_hint(text: str) -> bool:
    return _starts_with_word(text, "bool", "boolean") or "true if" in text or "false if" in text


def _is_scalar_int_hint(text: str) -> bool:
    return (
        _starts_with_word(text, *_SCALAR_INT_START_WORDS)
        or bool(re.search(r"\b(?:int|integer|count|index|length)\b", text))
        or any(phrase in text for phrase in ("number of", "total number", "minimum number", "maximum number"))
    )


def _is_char_list_hint(text: str) -> bool:
    return (
        "list[char" in text
        or "list of char" in text
        or _starts_with_word(text, "chars", "characters")
        or ("list" in text and _has_word(text, "characters"))
    )


def _is_char_grid_hint(text: str) -> bool:
    return (
        "list[list[char" in text
        or (
            "board" in text
            and (
                "list[list[str" in text
                or "char" in text
                or "digit" in text
                or "sudoku" in text
                or "'.'" in text
            )
        )
    )


def _is_map_hint(text: str) -> bool:
    return bool(re.search(r"\b(?:dict|map|mapping)\b", text))


def _is_digit_mapping_list_hint(text: str) -> bool:
    return "mapping" in text and (
        "permutation" in text
        or "digit" in text
        or "length 10" in text
        or "length10" in text
    )


def _is_pair_list_hint(text: str) -> bool:
    return (
        "directed pairs" in text
        or "[old, new]" in text
        or "[old,new]" in text
        or "[u, v]" in text
        or "[u,v]" in text
    )


def _is_scalar_string_hint(text: str) -> bool:
    if "list[str" in text or "list of string" in text or "list of word" in text:
        return False
    return (
        "digit string" in text
        or ("integer digits" in text and "list" not in text)
        or "string of" in text
        or "peg name" in text
        or "first string" in text
        or "second string" in text
        or "word to " in text
        or "prefix to " in text
        or (_has_word(text, "str") and "list" not in text)
        or _starts_with_word(text, "str")
        or _starts_with_word(text, "string")
        or ("pattern" in text and "list" not in text and "length" not in text)
    )


def _is_scalar_double_hint(text: str) -> bool:
    return _starts_with_word(text, "eps") or "real number" in text or "float" in text or "double" in text


def _is_double_list_hint(text: str) -> bool:
    return ("list" in text or "array" in text) and (
        "probability" in text
        or "probabilities" in text
        or "item sizes" in text
        or "in (0, 1]" in text
        or _has_word(text, "probs")
        or "list[float" in text
        or "list[double" in text
        or "float" in text
        or "double" in text
    )


def _is_string_list_hint(text: str) -> bool:
    return (
        ("list[str" in text and "list[list[str" not in text)
        or "list of string" in text
        or "string tokens" in text
        or (_has_word(text, "tokens") and ("string" in text or "operands" in text or "operators" in text))
    )


def _is_string_matrix_hint(text: str) -> bool:
    return (
        "list[list[str" in text
        or "list of list of str" in text
        or _has_word(text, "accounts", "equations")
    )


def _is_mixed_string_table_hint(text: str) -> bool:
    return (
        "list of operation tuples" in text
        or "list of (cmd" in text
        or "op_name" in text
        or (
            "operations" in text
            and (
                "list[list" in text
                or "tuple" in text
                or "tuples" in text
                or "*args" in text
            )
        )
    )


def _is_double_matrix_hint(text: str) -> bool:
    return (
        "double matrix" in text
        or "float matrix" in text
        or "real-valued matrix" in text
        or (("list" in text or "matrix" in text) and "polygon vertices" in text)
        or ("list of m (x, y)" in text and ("polygon" in text or "vertices" in text))
    )


def _is_nested_coordinate_matrix_hint(text: str) -> bool:
    return bool(re.search(r"\(\(x\d*, y\d*\), \(x\d*, y\d*\)\)", text))


def _is_level_order_tree_list_hint(text: str) -> bool:
    return (
        bool(re.search(r"\broot\s+list\b", text))
        or "level order binary tree" in text
        or "level-order binary tree" in text
        or "level order tree" in text
        or "level-order tree" in text
        or "bst level-order" in text
        or "bst level order" in text
        or ("list" in text and "tree" in text and ("level" in text or "main tree" in text or "pattern tree" in text))
        or "linked list" in text
    )


def _is_int_table_hint(text: str) -> bool:
    return "list[list]" in text and "[[val" in text


def _is_explicit_int_list_hint(text: str) -> bool:
    return "list[int" in text and "list[list[int" not in text


def _is_long_scalar_hint(text: str) -> bool:
    return bool(re.search(r"\b(?:long\s+long|long\s+integer|long\s+int|int64|64\s+bit\s+(?:signed\s+)?(?:integer|int))\b", text))


def _is_long_list_hint(text: str) -> bool:
    return (
        "list[long" in text
        or "list of long" in text
        or "long array" in text
        or "array of long" in text
        or bool(re.search(r"\b(?:list|array)\s+of\s+64\s+bit\s+(?:signed\s+)?(?:integers|ints)\b", text))
    )


def _is_nullable_long_list_hint(text: str) -> bool:
    return (
        ("long?" in text or "nullable long" in text or "optional long" in text or "optional[long" in text)
        and ("list" in text or "array" in text)
    )


def _is_long_matrix_hint(text: str) -> bool:
    return (
        "list[list[long" in text
        or "list of lists of long" in text
        or "matrix of long" in text
        or "long matrix" in text
    )


def _is_dimension_array_hint(text: str) -> bool:
    return "list of length n+1" in text and "matrix i has shape" in text


def _is_counted_matrix_hint(text: str) -> bool:
    is_numeric_tuple_list = (
        "operation" not in text
        and "op_name" not in text
        and "cmd" not in text
        and (
            "list of (" in text
            or "list of n (" in text
            or "list of m (" in text
            or "list of k (" in text
        )
    )
    return (
        bool(re.search(r"\bn\s*x\s*n\b", text))
        or is_numeric_tuple_list
        or "list of n lists" in text
        or "list of length n; children[" in text
        or ("children[" in text and ("[left, right]" in text or "list of" in text))
    )


def _is_generic_int_list_hint(text: str) -> bool:
    if not ("list" in text or "array" in text):
        return False
    if any(word in text for word in ("char", "string", "word", "probability", "float", "double", "bool")):
        return False
    if any(word in text for word in ("tuple", "operation", "matrix", "grid", "maze", "board", "dict", "map")):
        return False
    return (
        "list of n" in text
        or "list of k" in text
        or "list of available" in text
        or "list of length n" in text
        or "array of length" in text
        or "sorted array" in text
    )


def _param_values_from_json(input_json: str) -> dict[str, object]:
    try:
        data = json.loads(input_json)
    except (TypeError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _cpp_type_for_value(value: object) -> str | None:
    kind = _value_kind(value)
    return {
        "bool": "bool",
        "int": "int",
        "long": "long long",
        "float": "double",
        "string": "string",
        "list_bool": "vector<bool>",
        "list_int": "vector<int>",
        "list_long": "vector<long long>",
        "list_nullable_long": "vector<optional<long long>>",
        "list_nullable_int": "vector<optional<int>>",
        "list_float": "vector<double>",
        "list_nullable_float": "vector<optional<double>>",
        "list_string": "vector<string>",
        "list_char": "vector<char>",
        "list_list_bool": "vector<vector<bool>>",
        "list_list_int": "vector<vector<int>>",
        "list_list_long": "vector<vector<long long>>",
        "list_list_float": "vector<vector<double>>",
        "list_list_string": "vector<vector<string>>",
        "list_list_char": "vector<vector<char>>",
        "map_int_int": "unordered_map<int, int>",
        "map_int_list_int": "unordered_map<int, vector<int>>",
    }.get(kind)


def _java_type_for_value(value: object) -> str | None:
    kind = _value_kind(value)
    return {
        "bool": "boolean",
        "int": "int",
        "long": "long",
        "float": "double",
        "string": "String",
        "list_bool": "List<Boolean>",
        "list_int": "List<Integer>",
        "list_long": "List<Long>",
        "list_nullable_long": "List<Long>",
        "list_nullable_int": "List<Integer>",
        "list_float": "List<Double>",
        "list_nullable_float": "List<Double>",
        "list_string": "List<String>",
        "list_char": "List<Character>",
        "list_list_bool": "List<List<Boolean>>",
        "list_list_int": "List<List<Integer>>",
        "list_list_long": "List<List<Long>>",
        "list_list_float": "List<List<Double>>",
        "list_list_string": "List<List<String>>",
        "list_list_char": "List<List<Character>>",
        "map_int_int": "Map<Integer, Integer>",
        "map_int_list_int": "Map<Integer, List<Integer>>",
    }.get(kind)


def _csharp_type_for_value(value: object) -> str | None:
    kind = _value_kind(value)
    return {
        "bool": "bool",
        "int": "int",
        "long": "long",
        "float": "double",
        "string": "string",
        "list_bool": "List<bool>",
        "list_int": "List<int>",
        "list_long": "List<long>",
        "list_nullable_long": "List<long?>",
        "list_nullable_int": "List<int?>",
        "list_float": "List<double>",
        "list_nullable_float": "List<double?>",
        "list_string": "List<string>",
        "list_char": "List<char>",
        "list_list_bool": "List<List<bool>>",
        "list_list_int": "List<List<int>>",
        "list_list_long": "List<List<long>>",
        "list_list_float": "List<List<double>>",
        "list_list_string": "List<List<string>>",
        "list_list_char": "List<List<char>>",
        "map_int_int": "Dictionary<int, int>",
        "map_int_list_int": "Dictionary<int, List<int>>",
    }.get(kind)


def _go_type_for_value(value: object) -> str | None:
    csharp_type = _csharp_type_for_value(value)
    return _go_type_from_csharp(csharp_type) if csharp_type is not None else None


def _kotlin_type_for_value(value: object) -> str | None:
    csharp_type = _csharp_type_for_value(value)
    return _kotlin_type_from_csharp(csharp_type) if csharp_type is not None else None


def _go_type_for_hint(type_hint: str) -> str:
    return _go_type_from_csharp(_csharp_type_for_hint(type_hint))


def _kotlin_type_for_hint(type_hint: str) -> str:
    return _kotlin_type_from_csharp(_csharp_type_for_hint(type_hint))


def _go_type_from_csharp(csharp_type: str) -> str:
    return {
        "bool": "bool",
        "int": "int",
        "long": "int64",
        "double": "float64",
        "string": "string",
        "List<bool>": "[]bool",
        "List<int>": "[]int",
        "List<long>": "[]int64",
        "List<long?>": "[]*int64",
        "List<int?>": "[]*int",
        "List<double>": "[]float64",
        "List<double?>": "[]*float64",
        "List<string>": "[]string",
        "List<char>": "[]rune",
        "List<List<bool>>": "[][]bool",
        "List<List<int>>": "[][]int",
        "List<List<long>>": "[][]int64",
        "List<List<double>>": "[][]float64",
        "List<List<string>>": "[][]string",
        "List<List<char>>": "[][]rune",
        "Dictionary<int, int>": "map[int]int",
        "Dictionary<int, List<int>>": "map[int][]int",
    }.get(csharp_type, "int")


def _kotlin_type_from_csharp(csharp_type: str) -> str:
    return {
        "bool": "Boolean",
        "int": "Int",
        "long": "Long",
        "double": "Double",
        "string": "String",
        "List<bool>": "MutableList<Boolean>",
        "List<int>": "MutableList<Int>",
        "List<long>": "MutableList<Long>",
        "List<long?>": "MutableList<Long?>",
        "List<int?>": "MutableList<Int?>",
        "List<double>": "MutableList<Double>",
        "List<double?>": "MutableList<Double?>",
        "List<string>": "MutableList<String>",
        "List<char>": "MutableList<Char>",
        "List<List<bool>>": "MutableList<MutableList<Boolean>>",
        "List<List<int>>": "MutableList<MutableList<Int>>",
        "List<List<long>>": "MutableList<MutableList<Long>>",
        "List<List<double>>": "MutableList<MutableList<Double>>",
        "List<List<string>>": "MutableList<MutableList<String>>",
        "List<List<char>>": "MutableList<MutableList<Char>>",
        "Dictionary<int, int>": "MutableMap<Int, Int>",
        "Dictionary<int, List<int>>": "MutableMap<Int, MutableList<Int>>",
    }.get(csharp_type, "Int")


def _prefer_hint_for_ambiguous_value(value_type: str | None, hint_type: str) -> str:
    if value_type is None:
        return hint_type
    if (value_type, hint_type) in {
        ("vector<optional<int>>", "vector<optional<long long>>"): "vector<optional<long long>>",
        ("vector<optional<int>>", "vector<long long>"): "vector<optional<long long>>",
        ("List<int?>", "List<long?>"): "List<long?>",
        ("List<int?>", "List<long>"): "List<long?>",
    }:
        return {
            ("vector<optional<int>>", "vector<optional<long long>>"): "vector<optional<long long>>",
            ("vector<optional<int>>", "vector<long long>"): "vector<optional<long long>>",
            ("List<int?>", "List<long?>"): "List<long?>",
            ("List<int?>", "List<long>"): "List<long?>",
        }[(value_type, hint_type)]
    if (value_type, hint_type) in {
        ("vector<char>", "vector<string>"),
        ("List<Character>", "List<String>"),
        ("List<char>", "List<string>"),
        ("vector<vector<char>>", "vector<vector<string>>"),
        ("List<List<Character>>", "List<List<String>>"),
        ("List<List<char>>", "List<List<string>>"),
        ("vector<int>", "vector<optional<int>>"),
        ("List<int>", "List<int?>"),
        ("int", "long long"),
        ("int", "long"),
        ("vector<int>", "vector<long long>"),
        ("vector<vector<int>>", "vector<vector<long long>>"),
        ("List<Integer>", "List<Long>"),
        ("List<List<Integer>>", "List<List<Long>>"),
        ("List<int>", "List<long>"),
        ("List<List<int>>", "List<List<long>>"),
    }:
        return hint_type
    return value_type


def _prefer_go_hint_for_ambiguous_value(value_type: str | None, hint_type: str) -> str:
    if value_type is None:
        return hint_type
    if (value_type, hint_type) in {
        ("[]*int", "[]*int64"),
        ("[]*int", "[]int64"),
        ("[]int", "[]*int"),
        ("[]int", "[]int64"),
        ("[][]int", "[][]int64"),
        ("int", "int64"),
        ("[]rune", "[]string"),
        ("[][]rune", "[][]string"),
    }:
        return hint_type
    return value_type


def _prefer_kotlin_hint_for_ambiguous_value(value_type: str | None, hint_type: str) -> str:
    if value_type is None:
        return hint_type
    if (value_type, hint_type) in {
        ("MutableList<Int?>", "MutableList<Long?>"),
        ("MutableList<Int?>", "MutableList<Long>"),
        ("MutableList<Int>", "MutableList<Int?>"),
        ("MutableList<Int>", "MutableList<Long>"),
        ("MutableList<MutableList<Int>>", "MutableList<MutableList<Long>>"),
        ("Int", "Long"),
        ("MutableList<Char>", "MutableList<String>"),
        ("MutableList<MutableList<Char>>", "MutableList<MutableList<String>>"),
    }:
        return hint_type
    return value_type


def _value_kind(value: object) -> str | None:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "long" if value < -(2 ** 31) or value > 2 ** 31 - 1 else "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "string"
    if isinstance(value, (list, tuple)):
        return _list_value_kind(list(value))
    if isinstance(value, dict):
        return _dict_value_kind(value)
    return None


def _list_value_kind(values: list[object]) -> str | None:
    if not values:
        return "list_empty"
    if all(isinstance(value, str) and len(value) == 1 for value in values):
        return "list_char"
    item_kinds = {_value_kind(value) for value in values}
    if None in item_kinds:
        return None
    had_null = "null" in item_kinds
    item_kinds.discard("null")
    if not item_kinds:
        return None
    item_kinds.discard("list_empty")
    if not item_kinds:
        return None
    if item_kinds == {"bool"}:
        return "list_bool"
    if item_kinds <= {"int", "bool", "long"}:
        if "long" in item_kinds:
            return "list_nullable_long" if had_null else "list_long"
        return "list_nullable_int" if had_null else "list_int"
    if item_kinds <= {"int", "bool", "long", "float"}:
        return "list_nullable_float" if had_null else "list_float"
    if item_kinds == {"string"}:
        return "list_string"
    if "string" in item_kinds and item_kinds <= {"string", "int", "bool", "float"}:
        return "list_string"
    if item_kinds <= {"list_int", "list_long"}:
        return "list_list_long" if "list_long" in item_kinds else "list_list_int"
    if item_kinds <= {"list_int", "list_long", "list_float"}:
        return "list_list_float"
    if item_kinds == {"list_bool"}:
        return "list_list_bool"
    if item_kinds <= {"list_bool", "list_int"}:
        return "list_list_int"
    if item_kinds == {"list_string"}:
        return "list_list_string"
    if "list_string" in item_kinds and item_kinds <= {"list_string", "list_int", "list_float", "list_bool"}:
        return "list_list_string"
    if item_kinds == {"list_char"}:
        return "list_list_char"
    return None


def _dict_value_kind(values: dict[object, object]) -> str | None:
    if not values:
        return None
    if not all(_is_int_key(key) for key in values):
        return None
    value_kinds = {_value_kind(value) for value in values.values()}
    if value_kinds <= {"int", "bool"}:
        return "map_int_int"
    if value_kinds <= {"list_int"}:
        return "map_int_list_int"
    return None


def _is_int_key(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, str):
        return bool(re.fullmatch(r"-?\d+", value))
    return False


def _cpp_type_for_hint(type_hint: str) -> str:
    text = _hint_text(type_hint)
    if _is_bool_hint(text):
        return "bool"
    if _is_digit_mapping_list_hint(text):
        return "vector<int>"
    if _is_pair_list_hint(text):
        return "vector<vector<int>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "unordered_map<int, vector<int>>"
        return "unordered_map<int, int>"
    if _is_scalar_string_hint(text):
        return "string"
    if _is_char_grid_hint(text):
        return "vector<vector<char>>"
    if _is_char_list_hint(text):
        return "vector<char>"
    if _is_mixed_string_table_hint(text):
        return "vector<vector<string>>"
    if _is_string_matrix_hint(text):
        return "vector<vector<string>>"
    if _is_string_list_hint(text):
        return "vector<string>"
    if _is_double_matrix_hint(text):
        return "vector<vector<double>>"
    if _is_double_list_hint(text):
        return "vector<double>"
    if _is_long_matrix_hint(text):
        return "vector<vector<long long>>"
    if _is_nullable_long_list_hint(text):
        return "vector<optional<long long>>"
    if _is_long_list_hint(text):
        return "vector<long long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "vector<vector<int>>"
    if _is_int_table_hint(text):
        return "vector<vector<int>>"
    if _is_level_order_tree_list_hint(text):
        return "vector<optional<int>>"
    if _is_counted_matrix_hint(text):
        return "vector<vector<int>>"
    if _is_explicit_int_list_hint(text):
        return "vector<int>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "vector<int>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "vector<vector<string>>"
    if "list[list[bool" in text:
        return "vector<vector<bool>>"
    if "list[list[float" in text or "list[list[double" in text:
        return "vector<vector<double>>"
    if "list[list[long" in text:
        return "vector<vector<long long>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "vector<vector<int>>"
    if _has_word(text, "accounts", "equations"):
        return "vector<vector<string>>"
    if "list[str" in text or "list of string" in text:
        return "vector<string>"
    if "list[bool" in text:
        return "vector<bool>"
    if "list[float" in text or "list[double" in text:
        return "vector<double>"
    if "list[long" in text:
        return "vector<long long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "vector<int>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "vector<int>"
    if _is_level_order_tree_list_hint(text):
        return "vector<optional<int>>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "vector<string>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "string"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "vector<int>"
    if "bool" in text:
        return "bool"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "string"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _java_type_for_hint(type_hint: str) -> str:
    text = _hint_text(type_hint)
    if _is_bool_hint(text):
        return "boolean"
    if _is_digit_mapping_list_hint(text):
        return "List<Integer>"
    if _is_pair_list_hint(text):
        return "List<List<Integer>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "Map<Integer, List<Integer>>"
        return "Map<Integer, Integer>"
    if _is_scalar_string_hint(text):
        return "String"
    if _is_char_grid_hint(text):
        return "List<List<Character>>"
    if _is_char_list_hint(text):
        return "List<Character>"
    if _is_mixed_string_table_hint(text):
        return "List<List<String>>"
    if _is_string_matrix_hint(text):
        return "List<List<String>>"
    if _is_string_list_hint(text):
        return "List<String>"
    if _is_double_matrix_hint(text):
        return "List<List<Double>>"
    if _is_double_list_hint(text):
        return "List<Double>"
    if _is_long_matrix_hint(text):
        return "List<List<Long>>"
    if _is_nullable_long_list_hint(text):
        return "List<Long>"
    if _is_long_list_hint(text):
        return "List<Long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "List<List<Integer>>"
    if _is_int_table_hint(text):
        return "List<List<Integer>>"
    if _is_level_order_tree_list_hint(text):
        return "List<Integer>"
    if _is_counted_matrix_hint(text):
        return "List<List<Integer>>"
    if _is_explicit_int_list_hint(text):
        return "List<Integer>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "List<Integer>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "List<List<String>>"
    if "list[list[bool" in text:
        return "List<List<Boolean>>"
    if "list[list[float" in text or "list[list[double" in text:
        return "List<List<Double>>"
    if "list[list[long" in text:
        return "List<List<Long>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "List<List<Integer>>"
    if _has_word(text, "accounts", "equations"):
        return "List<List<String>>"
    if "list[str" in text or "list of string" in text:
        return "List<String>"
    if "list[bool" in text:
        return "List<Boolean>"
    if "list[float" in text or "list[double" in text:
        return "List<Double>"
    if "list[long" in text:
        return "List<Long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "List<Integer>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "List<Integer>"
    if _is_level_order_tree_list_hint(text):
        return "List<Integer>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "List<String>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "String"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "List<Integer>"
    if "bool" in text:
        return "boolean"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "String"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _cpp_reader_for_type(cpp_type: str) -> str:
    readers = {
        "int": "toInt",
        "long long": "toLong",
        "double": "toDouble",
        "bool": "toBool",
        "string": "toString",
        "char": "toChar",
        "vector<int>": "toVectorInt",
        "vector<optional<int>>": "toVectorOptionalInt",
        "vector<optional<long long>>": "toVectorOptionalLong",
        "vector<long long>": "toVectorLong",
        "vector<double>": "toVectorDouble",
        "vector<optional<double>>": "toVectorOptionalDouble",
        "vector<bool>": "toVectorBool",
        "vector<string>": "toVectorString",
        "vector<char>": "toVectorChar",
        "vector<vector<int>>": "toVectorVectorInt",
        "vector<vector<long long>>": "toVectorVectorLong",
        "vector<vector<double>>": "toVectorVectorDouble",
        "vector<vector<bool>>": "toVectorVectorBool",
        "vector<vector<string>>": "toVectorVectorString",
        "vector<vector<char>>": "toVectorVectorChar",
        "unordered_map<int, int>": "toMapIntInt",
        "unordered_map<int, vector<int>>": "toMapIntVectorInt",
    }
    return readers.get(cpp_type, "toInt")


def _java_reader_for_type(java_type: str) -> str:
    readers = {
        "int": "asInt",
        "long": "asLong",
        "double": "asDouble",
        "boolean": "asBoolean",
        "String": "asString",
        "char": "asChar",
        "Character": "asChar",
        "List<Integer>": "listInt",
        "List<Long>": "listLong",
        "List<Double>": "listDouble",
        "List<Boolean>": "listBool",
        "List<String>": "listString",
        "List<Character>": "listChar",
        "List<List<Integer>>": "listListInt",
        "List<List<Long>>": "listListLong",
        "List<List<Double>>": "listListDouble",
        "List<List<Boolean>>": "listListBool",
        "List<List<String>>": "listListString",
        "List<List<Character>>": "listListChar",
        "Map<Integer, Integer>": "mapIntInt",
        "Map<Integer, List<Integer>>": "mapIntListInt",
    }
    return readers.get(java_type, "asInt")


def _kotlin_reader_for_type(kotlin_type: str) -> str:
    readers = {
        "Int": "asInt",
        "Long": "asLong",
        "Double": "asDouble",
        "Boolean": "asBoolean",
        "String": "asString",
        "Char": "asChar",
        "MutableList<Int>": "listInt",
        "MutableList<Int?>": "listNullableInt",
        "MutableList<Long>": "listLong",
        "MutableList<Long?>": "listNullableLong",
        "MutableList<Double>": "listDouble",
        "MutableList<Double?>": "listNullableDouble",
        "MutableList<Boolean>": "listBool",
        "MutableList<String>": "listString",
        "MutableList<Char>": "listChar",
        "MutableList<MutableList<Int>>": "listListInt",
        "MutableList<MutableList<Long>>": "listListLong",
        "MutableList<MutableList<Double>>": "listListDouble",
        "MutableList<MutableList<Boolean>>": "listListBool",
        "MutableList<MutableList<String>>": "listListString",
        "MutableList<MutableList<Char>>": "listListChar",
        "MutableMap<Int, Int>": "mapIntInt",
        "MutableMap<Int, MutableList<Int>>": "mapIntListInt",
    }
    return readers.get(kotlin_type, "asInt")


def _kotlin_string_literal(value: str) -> str:
    return json.dumps(value).replace("$", r"\$")


def _harness_identifier(name: str) -> str:
    cleaned = re.sub(r"\W", "_", name)
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"value_{cleaned}"
    return f"input_{cleaned}"


def _csharp_type_for_hint(type_hint: str) -> str:
    text = type_hint.replace("`", "").replace("—", " ").replace("-", " ").lower()
    if _is_bool_hint(text):
        return "bool"
    if _is_digit_mapping_list_hint(text):
        return "List<int>"
    if _is_pair_list_hint(text):
        return "List<List<int>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "Dictionary<int, List<int>>"
        return "Dictionary<int, int>"
    if _is_scalar_string_hint(text):
        return "string"
    if _is_char_grid_hint(text):
        return "List<List<char>>"
    if _is_char_list_hint(text):
        return "List<char>"
    if _is_mixed_string_table_hint(text):
        return "List<List<string>>"
    if _is_string_matrix_hint(text):
        return "List<List<string>>"
    if _is_string_list_hint(text):
        return "List<string>"
    if _is_double_matrix_hint(text):
        return "List<List<double>>"
    if _is_double_list_hint(text):
        return "List<double>"
    if _is_long_matrix_hint(text):
        return "List<List<long>>"
    if _is_nullable_long_list_hint(text):
        return "List<long?>"
    if _is_long_list_hint(text):
        return "List<long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "List<List<int>>"
    if _is_int_table_hint(text):
        return "List<List<int>>"
    if _is_level_order_tree_list_hint(text):
        return "List<int?>"
    if _is_counted_matrix_hint(text):
        return "List<List<int>>"
    if _is_explicit_int_list_hint(text):
        return "List<int>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "List<int>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "List<List<string>>"
    if "list[list[bool" in text:
        return "List<List<bool>>"
    if "list[list[float" in text or "list[list[double" in text:
        return "List<List<double>>"
    if "list[list[long" in text:
        return "List<List<long>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "List<List<int>>"
    if _has_word(text, "accounts", "equations"):
        return "List<List<string>>"
    if "list[str" in text or "list of string" in text:
        return "List<string>"
    if "list[bool" in text:
        return "List<bool>"
    if "list[float" in text or "list[double" in text:
        return "List<double>"
    if "list[long" in text:
        return "List<long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "List<int>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "List<int>"
    if _is_level_order_tree_list_hint(text):
        return "List<int?>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "List<string>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "string"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "List<int>"
    if "bool" in text:
        return "bool"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "string"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _csharp_default(csharp_type: str) -> str:
    if csharp_type.startswith("List<") or csharp_type.startswith("Dictionary<"):
        return "new()"
    if csharp_type == "string":
        return '""'
    if csharp_type == "bool":
        return "false"
    if csharp_type == "double":
        return "0.0"
    return "0"


_CSHARP_KEYWORDS = {
    "abstract",
    "as",
    "base",
    "bool",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "checked",
    "class",
    "const",
    "continue",
    "decimal",
    "default",
    "delegate",
    "do",
    "double",
    "else",
    "enum",
    "event",
    "explicit",
    "extern",
    "false",
    "finally",
    "fixed",
    "float",
    "for",
    "foreach",
    "goto",
    "if",
    "implicit",
    "in",
    "int",
    "interface",
    "internal",
    "is",
    "lock",
    "long",
    "namespace",
    "new",
    "null",
    "object",
    "operator",
    "out",
    "override",
    "params",
    "private",
    "protected",
    "public",
    "readonly",
    "ref",
    "return",
    "sbyte",
    "sealed",
    "short",
    "sizeof",
    "stackalloc",
    "static",
    "string",
    "struct",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "uint",
    "ulong",
    "unchecked",
    "unsafe",
    "ushort",
    "using",
    "virtual",
    "void",
    "volatile",
    "while",
}


def _csharp_identifier(name: str) -> str:
    cleaned = re.sub(r"\W", "_", name)
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"value_{cleaned}"
    if cleaned in _CSHARP_KEYWORDS:
        cleaned = f"@{cleaned}"
    return cleaned


def _is_in_place_return(returns_hint: str) -> bool:
    text = returns_hint.lower()
    return "none" in text or "void" in text or "in-place" in text or "in place" in text


def _message(prefix: str, detail: str) -> str:
    detail = detail.strip()
    if not detail:
        return prefix
    if len(detail) > 1200:
        detail = detail[:1200] + "..."
    return f"{prefix}: {detail}"
