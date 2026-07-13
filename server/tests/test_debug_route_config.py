"""Tests for packaged debugger runtime selection."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from . import conftest  # noqa: F401
from server.app import external_programs
from server.app.routes import debug


class DebugRouteConfigTest(unittest.TestCase):
    def test_debug_rejects_real_and_multi_case_modes(self) -> None:
        with self.assertRaisesRegex(debug.DebugPreparationError, "one visible or custom case"):
            debug._debug_validated_setup(
                {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                "lc_1",
                mode="real_test",
            )
        with self.assertRaisesRegex(debug.DebugPreparationError, "exactly one selected case"):
            debug._debug_validated_setup(
                {"challengeId": "lc_1", "caseIds": ["sample-1", "sample-2"]},
                "lc_1",
                mode="practice",
            )

    def test_packaged_debug_uses_configured_runtime(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "1",
                "CODEN_DEBUG_PYTHON": sys.executable,
            },
        ):
            self.assertEqual(debug._debug_python_exe(), sys.executable)

    def test_packaged_debug_does_not_fall_back_to_system_python(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "1",
                "CODEN_DEBUG_PYTHON": r"C:\missing\python.exe",
            },
        ):
            with self.assertRaises(debug.DebugPythonUnavailable) as ctx:
                debug._debug_python_exe()
        self.assertIn("bundled debug Python runtime", str(ctx.exception))

    def test_dev_debug_uses_current_interpreter(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "",
                "CODEN_DEBUG_PYTHON": "",
                "CODEN_PYTHON_EXE": "",
            },
        ):
            self.assertEqual(debug._debug_python_exe(), sys.executable)

    def test_solution_path_is_language_scoped(self) -> None:
        expected = {
            "python": "python_v1.py",
            "cpp": "cpp_v1.cpp",
            "java": "java_v1.java",
            "csharp": "csharp_v1.cs",
            "javascript": "javascript_v1.js",
            "go": "go_v1.go",
            "kotlin": "kotlin_v1.kt",
        }
        for language, filename in expected.items():
            path = str(debug._solution_path("lc_1", language)).replace("\\", "/")
            self.assertTrue(path.endswith(f"dsa/leetcode/1_two-sum/user_solutions/{filename}"), path)

    def test_python_debug_capability_uses_runtime_probe(self) -> None:
        with (
            patch.object(debug, "_debug_python_exe", return_value=sys.executable),
            patch.object(debug, "_python_has_debugpy", return_value=True),
        ):
            capability = debug._debug_capability("python")

        self.assertTrue(capability["available"])
        self.assertEqual(capability["adapter_id"], "debugpy")
        self.assertEqual(capability["missing"], [])

    def test_debug_tool_lookup_prefers_env_over_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cpp_adapter = root / "lldb-custom.exe"
            cpp_compiler = root / "clang-custom.exe"
            javac = root / "javac-custom.exe"
            java = root / "java-custom.exe"
            dotnet = root / "dotnet-custom.exe"
            netcoredbg = root / "netcoredbg-custom.exe"
            node = root / "node-custom.exe"
            js_adapter = root / "js-debug-adapter.js"
            go = root / "go-custom.exe"
            kotlinc = root / "kotlinc-custom.exe"
            dlv = root / "dlv-custom.exe"
            for tool in (cpp_adapter, cpp_compiler, javac, java, dotnet, netcoredbg, node, js_adapter, go, kotlinc, dlv):
                tool.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_CPP_DEBUG_ADAPTER": str(cpp_adapter),
                        "CODEN_CPP_COMPILER": str(cpp_compiler),
                        "CODEN_JAVAC": str(javac),
                        "CODEN_JAVA": str(java),
                        "CODEN_DOTNET": str(dotnet),
                        "CODEN_NETCOREDBG": str(netcoredbg),
                        "CODEN_NODE": str(node),
                        "CODEN_JS_DEBUG_ADAPTER": str(js_adapter),
                        "CODEN_GO": str(go),
                        "CODEN_KOTLINC": str(kotlinc),
                        "CODEN_GO_DEBUG_ADAPTER": str(dlv),
                    },
                    clear=False,
                ),
            ):
                self.assertEqual(debug._first_tool("lldb-dap", "lldb-vscode"), str(cpp_adapter))
                self.assertEqual(debug._first_tool("g++", "clang++"), str(cpp_compiler))
                self.assertEqual(debug._first_tool("javac"), str(javac))
                self.assertEqual(debug._first_tool("java"), str(java))
                self.assertEqual(debug._first_tool("dotnet"), str(dotnet))
                self.assertEqual(debug._first_tool("netcoredbg"), str(netcoredbg))
                self.assertEqual(debug._first_tool("node"), str(node))
                self.assertEqual(debug._js_debug_adapter_path(), str(js_adapter))
                self.assertEqual(debug._first_tool("go"), str(go))
                self.assertEqual(debug._first_tool("kotlinc"), str(kotlinc))
                self.assertEqual(debug._first_tool("dlv"), str(dlv))

    def test_debug_tools_dir_supplies_native_debug_tools(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = {
                "cpp_adapter": root / "cpp" / "bin" / "lldb-dap.exe",
                "cpp_compiler": root / "cpp" / "bin" / "g++.exe",
                "javac": root / "jdk" / "bin" / "javac.exe",
                "java": root / "jdk" / "bin" / "java.exe",
                "dotnet": root / "dotnet" / "bin" / "dotnet.exe",
                "netcoredbg": root / "csharp" / "bin" / "netcoredbg.exe",
                "node": root / "node" / "bin" / "node.exe",
                "js_adapter": root / "javascript" / "js-debug-adapter.js",
                "go": root / "go" / "bin" / "go.exe",
                "kotlinc": root / "kotlin" / "bin" / "kotlinc.bat",
                "dlv": root / "go" / "bin" / "dlv.exe",
            }
            for tool in paths.values():
                tool.parent.mkdir(parents=True, exist_ok=True)
                tool.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_DEBUG_TOOLS_DIR": str(root),
                        "CODEN_CPP_DEBUG_ADAPTER": "",
                        "CODEN_CPP_COMPILER": "",
                        "CODEN_JAVAC": "",
                        "CODEN_JAVA": "",
                        "CODEN_DOTNET": "",
                        "CODEN_NETCOREDBG": "",
                        "CODEN_NODE": "",
                        "CODEN_JS_DEBUG_ADAPTER": "",
                        "CODEN_GO": "",
                        "CODEN_KOTLINC": "",
                        "CODEN_GO_DEBUG_ADAPTER": "",
                    },
                    clear=False,
                ),
            ):
                self.assertEqual(debug._first_tool("lldb-dap", "lldb-vscode"), str(paths["cpp_adapter"]))
                self.assertEqual(debug._first_tool("g++", "clang++"), str(paths["cpp_compiler"]))
                self.assertEqual(debug._first_tool("javac"), str(paths["javac"]))
                self.assertEqual(debug._first_tool("java"), str(paths["java"]))
                self.assertEqual(debug._first_tool("dotnet"), str(paths["dotnet"]))
                self.assertEqual(debug._first_tool("netcoredbg"), str(paths["netcoredbg"]))
                self.assertEqual(debug._first_tool("node"), str(paths["node"]))
                self.assertEqual(debug._js_debug_adapter_path(), str(paths["js_adapter"]))
                self.assertEqual(debug._first_tool("go"), str(paths["go"]))
                self.assertEqual(debug._first_tool("kotlinc"), str(paths["kotlinc"]))
                self.assertEqual(debug._first_tool("dlv"), str(paths["dlv"]))

    def test_cpp_debug_capability_reports_missing_adapter_and_compiler(self) -> None:
        with (
            patch.object(debug.shutil, "which", return_value=None),
            patch.dict(
                os.environ,
                {
                    "CODEN_DEBUG_TOOLS_DIR": "",
                    "CODEN_CPP_DEBUG_ADAPTER": "",
                    "CODEN_CPP_COMPILER": "",
                },
                clear=False,
            ),
        ):
            capability = debug._debug_capability("cpp")

        self.assertFalse(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "lldb-dap")
        self.assertIn("lldb-dap or lldb-vscode", capability["missing"])
        self.assertIn("g++ or clang++", capability["missing"])
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_cpp_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return f"C:\\tools\\{name}.exe" if name in {"lldb-dap", "g++"} else None

        with patch.object(debug.shutil, "which", side_effect=fake_tool):
            capability = debug._debug_capability("cpp")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "lldb-dap")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_cpp_debug_capability_can_use_env_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            adapter = root / "lldb-dap.exe"
            compiler = root / "g++.exe"
            adapter.write_text("", encoding="utf-8")
            compiler.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_CPP_DEBUG_ADAPTER": str(adapter),
                        "CODEN_CPP_COMPILER": str(compiler),
                    },
                    clear=False,
                ),
            ):
                capability = debug._debug_capability("cpp")

        self.assertTrue(capability["available"])
        self.assertEqual(capability["adapter_command"], str(adapter))
        self.assertEqual(capability["missing"], [])

    def test_java_debug_capability_reports_missing_adapter_and_jdk(self) -> None:
        with (
            patch.object(debug.shutil, "which", return_value=None),
            patch.dict(
                os.environ,
                {
                    "CODEN_DEBUG_TOOLS_DIR": "",
                    "CODEN_JAVA_DEBUG_ADAPTER": "",
                    "CODEN_JAVAC": "",
                    "CODEN_JAVA": "",
                },
                clear=False,
            ),
        ):
            capability = debug._debug_capability("java")

        self.assertFalse(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "java-debug")
        self.assertIn("Java debug adapter", capability["missing"])
        self.assertIn("javac and java", capability["missing"])
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_java_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return f"C:\\tools\\{name}.exe" if name in {"javac", "java"} else None

        with tempfile.NamedTemporaryFile(suffix=".jar") as adapter:
            with (
                patch.object(debug.shutil, "which", side_effect=fake_tool),
                patch.dict(os.environ, {"CODEN_JAVA_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                capability = debug._debug_capability("java")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "java-debug")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_java_debug_capability_can_use_env_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            adapter = root / "java-debug.jar"
            javac = root / "javac.exe"
            java = root / "java.exe"
            adapter.write_text("", encoding="utf-8")
            javac.write_text("", encoding="utf-8")
            java.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_JAVA_DEBUG_ADAPTER": str(adapter),
                        "CODEN_JAVAC": str(javac),
                        "CODEN_JAVA": str(java),
                    },
                    clear=False,
                ),
            ):
                capability = debug._debug_capability("java")

        self.assertTrue(capability["available"])
        self.assertEqual(capability["adapter_command"], str(adapter))
        self.assertEqual(capability["missing"], [])

    def test_java_debug_capability_can_use_debug_tools_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            adapter = root / "java" / "java-debug-adapter.jar"
            javac = root / "jdk" / "bin" / "javac.exe"
            java = root / "jdk" / "bin" / "java.exe"
            for tool in (adapter, javac, java):
                tool.parent.mkdir(parents=True, exist_ok=True)
                tool.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_DEBUG_TOOLS_DIR": str(root),
                        "CODEN_JAVA_DEBUG_ADAPTER": "",
                        "CODEN_JAVAC": "",
                        "CODEN_JAVA": "",
                    },
                    clear=False,
                ),
            ):
                capability = debug._debug_capability("java")

        self.assertTrue(capability["available"])
        self.assertEqual(capability["adapter_command"], str(adapter))
        self.assertEqual(capability["missing"], [])

    def test_csharp_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return f"C:\\tools\\{name}.exe" if name in {"netcoredbg", "dotnet"} else None

        with patch.object(debug.shutil, "which", side_effect=fake_tool):
            capability = debug._debug_capability("csharp")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "netcoredbg")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_csharp_debug_capability_can_use_env_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dotnet = root / "dotnet.exe"
            netcoredbg = root / "netcoredbg.exe"
            dotnet.write_text("", encoding="utf-8")
            netcoredbg.write_text("", encoding="utf-8")

            with (
                patch.object(debug.shutil, "which", return_value=None),
                patch.dict(
                    os.environ,
                    {
                        "CODEN_DOTNET": str(dotnet),
                        "CODEN_NETCOREDBG": str(netcoredbg),
                    },
                    clear=False,
                ),
            ):
                capability = debug._debug_capability("csharp")

        self.assertTrue(capability["available"])
        self.assertEqual(capability["adapter_command"], str(netcoredbg))
        self.assertEqual(capability["missing"], [])

    def test_capabilities_endpoint_lists_all_languages(self) -> None:
        def fake_capability(language: str) -> dict[str, str]:
            return {"language": language}

        with patch.object(debug, "_debug_capability", side_effect=fake_capability):
            body = debug.debug_capabilities()

        self.assertEqual(
            set(body["languages"]),
            {"python", "cpp", "java", "csharp", "javascript", "go", "kotlin", "sql", "bash"},
        )

    def test_javascript_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return r"C:\tools\node.exe" if name == "node" else None

        with tempfile.NamedTemporaryFile(suffix=".js") as adapter:
            with (
                patch.object(debug.shutil, "which", side_effect=fake_tool),
                patch.dict(os.environ, {"CODEN_JS_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                capability = debug._debug_capability("javascript")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "js-debug")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_javascript_debug_capability_reports_missing_tools(self) -> None:
        with (
            patch.object(debug.shutil, "which", return_value=None),
            patch.dict(
                os.environ,
                {
                    "CODEN_DEBUG_TOOLS_DIR": "",
                    "CODEN_NODE": "",
                    "CODEN_JS_DEBUG_ADAPTER": "",
                },
                clear=False,
            ),
        ):
            capability = debug._debug_capability("javascript")

        self.assertFalse(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertIn("JavaScript debug adapter", capability["missing"])
        self.assertIn("Node.js", capability["missing"])
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_go_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return f"C:\\tools\\{name}.exe" if name in {"dlv", "go"} else None

        with patch.object(debug.shutil, "which", side_effect=fake_tool):
            capability = debug._debug_capability("go")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "delve-dap")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_go_debug_capability_reports_missing_tools(self) -> None:
        with (
            patch.object(debug.shutil, "which", return_value=None),
            patch.dict(
                os.environ,
                {
                    "CODEN_DEBUG_TOOLS_DIR": "",
                    "CODEN_GO": "",
                    "CODEN_GO_DEBUG_ADAPTER": "",
                },
                clear=False,
            ),
        ):
            capability = debug._debug_capability("go")

        self.assertFalse(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertIn("delve/dlv", capability["missing"])
        self.assertIn("Go toolchain", capability["missing"])
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_kotlin_debug_capability_has_launch_wiring(self) -> None:
        def fake_tool(name: str) -> str | None:
            return f"C:\\tools\\{name}.exe" if name in {"kotlinc", "java"} else None

        with tempfile.NamedTemporaryFile(suffix=".jar") as adapter:
            with (
                patch.object(debug.shutil, "which", side_effect=fake_tool),
                patch.dict(os.environ, {"CODEN_JAVA_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                capability = debug._debug_capability("kotlin")

        self.assertTrue(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertEqual(capability["adapter_id"], "java-debug")
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_kotlin_debug_capability_reports_missing_tools(self) -> None:
        with (
            patch.object(debug.shutil, "which", return_value=None),
            patch.dict(
                os.environ,
                {
                    "CODEN_DEBUG_TOOLS_DIR": "",
                    "CODEN_JAVA_DEBUG_ADAPTER": "",
                    "CODEN_KOTLINC": "",
                    "CODEN_JAVA": "",
                },
                clear=False,
            ),
        ):
            capability = debug._debug_capability("kotlin")

        self.assertFalse(capability["available"])
        self.assertTrue(capability["launch_supported"])
        self.assertIn("Java/Kotlin debug adapter", capability["missing"])
        self.assertIn("kotlinc and java", capability["missing"])
        self.assertNotIn("language launch wiring", capability["missing"])

    def test_cpp_function_harness_can_embed_debug_input(self) -> None:
        harness = external_programs._cpp_function_harness(
            ["arr", "target", "n"],
            {"arr": "list[int]", "target": "int", "n": "int"},
            "list[int]",
            input_json='{"arr":[1],"target":1,"n":1}',
        )

        self.assertIn('string __json = "{\\"arr\\":[1],\\"target\\":1,\\"n\\":1}";', harness)
        self.assertNotIn("string __json = __CodenJson::readAll();", harness)

    def test_cpp_debug_sources_preserve_solution_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            solution_path = Path(tmp) / "lc_1.cpp"
            solution_path.write_text("class Solution { public: int solve(int n) { return n; } };\n", encoding="utf-8")
            source_label = str(solution_path).replace("\\", "/")

            function_source = debug._cpp_function_debug_source(
                solution_path,
                "class Solution { public: int solve(int n) { return n; } };",
                ["n"],
                {"n": "int"},
                "int",
                '{"n":3}',
            )

        self.assertIn(f'#line 1 "{source_label}"', function_source)
        self.assertIn('string __json = "{\\"n\\":3}";', function_source)

    def test_prepare_cpp_debug_session_builds_launch_config(self) -> None:
        def fake_first_tool(*names: str) -> str | None:
            if "lldb-dap" in names:
                return r"C:\tools\lldb-dap.exe"
            if "g++" in names:
                return r"C:\tools\g++.exe"
            return None

        def fake_build(
            *,
            compiler: str,
            workdir: Path,
            solution_path: Path,
            payload: dict[str, object],
        ) -> Path:
            exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
            exe_path.write_text("", encoding="utf-8")
            self.assertEqual(compiler, r"C:\tools\g++.exe")
            self.assertEqual(payload["challengeId"], "lc_1")
            self.assertTrue(solution_path.is_file())
            return exe_path

        with tempfile.TemporaryDirectory() as source_tmp:
            solution_path = Path(source_tmp) / "lc_1.cpp"
            solution_path.write_text("class Solution { public: int solve(int n) { return n; } };", encoding="utf-8")
            with (
                patch.object(debug, "_first_tool", side_effect=fake_first_tool),
                patch.object(debug, "_build_cpp_debug_target", side_effect=fake_build),
            ):
                session = debug._prepare_cpp_debug_session(
                    {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    solution_path,
                )

        tempdir_name = session.tempdir.name if session.tempdir is not None else ""
        try:
            self.assertEqual(session.adapter_executable, r"C:\tools\lldb-dap.exe")
            self.assertEqual(session.adapter_id, "lldb-dap")
            self.assertEqual(session.launch_config["type"], "lldb-dap")
            self.assertTrue(str(session.launch_config["program"]).endswith("main.exe" if os.name == "nt" else "main"))
            self.assertEqual(session.breakpoint_path, solution_path)
            self.assertTrue(Path(tempdir_name).exists())
        finally:
            session.cleanup()
        self.assertFalse(Path(tempdir_name).exists())

    def test_build_cpp_debug_target_writes_combined_source(self) -> None:
        def fake_run_process(
            args: list[str],
            *,
            cwd: Path,
            timeout_seconds: float,
            input_text: str | None = None,
            env: dict[str, str] | None = None,
        ) -> subprocess.CompletedProcess[str]:
            Path(args[-1]).write_text("", encoding="utf-8")
            return subprocess.CompletedProcess(args, 0, "", "")

        source = """
class Solution {
public:
    vector<int> solve(vector<int> nums, int target) {
        return vector<int>{0, 1};
    }
};
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.cpp"
            solution_path.write_text(source, encoding="utf-8")
            with patch.object(debug, "_run_process", side_effect=fake_run_process):
                exe_path = debug._build_cpp_debug_target(
                    compiler="g++",
                    workdir=Path(build_tmp),
                    solution_path=solution_path,
                    payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
                )

            self.assertTrue(exe_path.is_file())
            main_text = (Path(build_tmp) / "main.cpp").read_text(encoding="utf-8")
            self.assertIn(str(solution_path).replace("\\", "/"), main_text)
            self.assertIn('string __json = "{', main_text)
            self.assertIn("Solution solution;", main_text)

    def test_java_function_harness_can_embed_debug_input(self) -> None:
        harness = external_programs._java_function_harness(
            ["arr", "target", "n"],
            {"arr": "list[int]", "target": "int", "n": "int"},
            "list[int]",
            input_json='{"arr":[1],"target":1,"n":1}',
        )

        self.assertIn('String json = "{\\"arr\\":[1],\\"target\\":1,\\"n\\":1}";', harness)
        self.assertNotIn("String json = Json.readAll();", harness)

    def test_java_debug_adapter_invocation_supports_jar_and_executable(self) -> None:
        self.assertEqual(
            debug._java_debug_adapter_invocation(r"C:\tools\java-debug.jar", r"C:\tools\java.exe"),
            (r"C:\tools\java.exe", ["-jar", r"C:\tools\java-debug.jar"]),
        )
        self.assertEqual(
            debug._java_debug_adapter_invocation(r"C:\tools\java-debug-adapter.exe", r"C:\tools\java.exe"),
            (r"C:\tools\java-debug-adapter.exe", []),
        )

    def test_js_debug_adapter_invocation_supports_script_and_executable(self) -> None:
        self.assertEqual(
            debug._js_debug_adapter_invocation(r"C:\tools\js-debug-adapter.js", r"C:\tools\node.exe"),
            (r"C:\tools\node.exe", [r"C:\tools\js-debug-adapter.js"]),
        )
        self.assertEqual(
            debug._js_debug_adapter_invocation(r"C:\tools\js-debug-adapter.exe", r"C:\tools\node.exe"),
            (r"C:\tools\js-debug-adapter.exe", []),
        )

    def test_prepare_java_debug_session_builds_launch_config(self) -> None:
        def fake_first_tool(*names: str) -> str | None:
            if "javac" in names:
                return r"C:\tools\javac.exe"
            if "java" in names:
                return r"C:\tools\java.exe"
            return None

        def fake_build(
            *,
            javac: str,
            workdir: Path,
            solution_path: Path,
            payload: dict[str, object],
        ) -> debug.JavaDebugTarget:
            class_path = workdir / "Main.class"
            class_path.write_text("", encoding="utf-8")
            self.assertEqual(javac, r"C:\tools\javac.exe")
            self.assertEqual(payload["challengeId"], "lc_1")
            self.assertTrue(solution_path.is_file())
            source_path = workdir / "Solution.java"
            source_path.write_text(solution_path.read_text(encoding="utf-8"), encoding="utf-8")
            return debug.JavaDebugTarget(main_class="Main", classpath=workdir, source_path=source_path)

        with tempfile.TemporaryDirectory() as source_tmp, tempfile.NamedTemporaryFile(suffix=".jar") as adapter:
            solution_path = Path(source_tmp) / "lc_1.java"
            solution_path.write_text("class Solution { public int solve(int n) { return n; } }", encoding="utf-8")
            with (
                patch.object(debug, "_first_tool", side_effect=fake_first_tool),
                patch.object(debug, "_build_java_debug_target", side_effect=fake_build),
                patch.dict(os.environ, {"CODEN_JAVA_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                session = debug._prepare_java_debug_session(
                    {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    solution_path,
                )

        tempdir_name = session.tempdir.name if session.tempdir is not None else ""
        try:
            self.assertEqual(session.adapter_executable, r"C:\tools\java.exe")
            self.assertEqual(session.adapter_args, ["-jar", adapter.name])
            self.assertEqual(session.adapter_id, "java-debug")
            self.assertEqual(session.launch_config["type"], "java")
            self.assertEqual(session.launch_config["mainClass"], "Main")
            self.assertEqual(session.launch_config["classPaths"], [tempdir_name])
            self.assertEqual(session.breakpoint_path, Path(tempdir_name) / "Solution.java")
            self.assertTrue(Path(tempdir_name).exists())
        finally:
            session.cleanup()
        self.assertFalse(Path(tempdir_name).exists())

    def test_build_java_debug_target_writes_function_harness(self) -> None:
        def fake_run_process(
            args: list[str],
            *,
            cwd: Path,
            timeout_seconds: float,
            input_text: str | None = None,
            env: dict[str, str] | None = None,
        ) -> subprocess.CompletedProcess[str]:
            (cwd / "Main.class").write_text("", encoding="utf-8")
            self.assertIn("-g", args)
            self.assertIn("-d", args)
            return subprocess.CompletedProcess(args, 0, "", "")

        source = """
import java.util.*;

public class Solution {
    public List<Integer> solve(List<Integer> nums, int target) {
        return Arrays.asList(0, 1);
    }
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.java"
            solution_path.write_text(source, encoding="utf-8")
            with patch.object(debug, "_run_process", side_effect=fake_run_process):
                target = debug._build_java_debug_target(
                    javac="javac",
                    workdir=Path(build_tmp),
                    solution_path=solution_path,
                    payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
                )

            self.assertEqual(target.main_class, "Main")
            self.assertEqual(target.classpath, Path(build_tmp))
            self.assertEqual(target.source_path, Path(build_tmp) / "Solution.java")
            copied_source = target.source_path.read_text(encoding="utf-8")
            self.assertIn("public class Solution", copied_source)
            main_text = (Path(build_tmp) / "Main.java").read_text(encoding="utf-8")
            self.assertIn('String json = "{', main_text)
            self.assertIn("Solution solution = new Solution();", main_text)

    def test_prepare_javascript_debug_session_builds_launch_config(self) -> None:
        def fake_first_tool(*names: str) -> str | None:
            return r"C:\tools\node.exe" if "node" in names else None

        def fake_build(
            *,
            workdir: Path,
            solution_path: Path,
            payload: dict[str, object],
        ) -> Path:
            launcher = workdir / "coden_js_debug_launcher.js"
            launcher.write_text("", encoding="utf-8")
            self.assertEqual(payload["challengeId"], "lc_1")
            self.assertTrue(solution_path.is_file())
            return launcher

        with tempfile.TemporaryDirectory() as source_tmp, tempfile.NamedTemporaryFile(suffix=".js") as adapter:
            solution_path = Path(source_tmp) / "lc_1.js"
            solution_path.write_text("class Solution { solve() { return data.indexOf(target); } }\n", encoding="utf-8")
            with (
                patch.object(debug, "_first_tool", side_effect=fake_first_tool),
                patch.object(debug, "_build_javascript_debug_target", side_effect=fake_build),
                patch.dict(os.environ, {"CODEN_JS_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                session = debug._prepare_javascript_debug_session(
                    {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    solution_path,
                )

        tempdir_name = session.tempdir.name if session.tempdir is not None else ""
        try:
            self.assertEqual(session.adapter_executable, r"C:\tools\node.exe")
            self.assertEqual(session.adapter_args, [adapter.name])
            self.assertEqual(session.adapter_id, "js-debug")
            self.assertEqual(session.launch_config["type"], "pwa-node")
            self.assertEqual(session.launch_config["runtimeExecutable"], r"C:\tools\node.exe")
            self.assertTrue(str(session.launch_config["program"]).endswith("coden_js_debug_launcher.js"))
            self.assertEqual(session.breakpoint_path, solution_path)
            self.assertTrue(Path(tempdir_name).exists())
        finally:
            session.cleanup()
        self.assertFalse(Path(tempdir_name).exists())

    def test_build_javascript_debug_target_writes_function_launcher(self) -> None:
        source = """
class Solution {
    solve(nums, target) {
        return [0, 1];
    }
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.js"
            solution_path.write_text(source, encoding="utf-8")
            launcher = debug._build_javascript_debug_target(
                workdir=Path(build_tmp),
                solution_path=solution_path,
                payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
            )

            self.assertEqual(launcher, Path(build_tmp) / "coden_js_debug_launcher.js")
            launcher_text = launcher.read_text(encoding="utf-8")
            self.assertIn("runInThisContext", launcher_text)
            self.assertIn(json.dumps(str(solution_path)), launcher_text)
            self.assertIn("class Solution", launcher_text)
            self.assertIn("solution.solve(input_nums, input_target)", launcher_text)
            self.assertIn("__codenPrintJson(result)", launcher_text)

    @unittest.skipUnless(shutil.which("node"), "Node.js is not installed")
    def test_javascript_debug_function_launcher_runs_under_node(self) -> None:
        node = shutil.which("node")
        assert node is not None
        source = """
class Solution {
    solve(nums, target) {
        return [0, 1];
    }
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.js"
            solution_path.write_text(source, encoding="utf-8")
            launcher = debug._build_javascript_debug_target(
                workdir=Path(build_tmp),
                solution_path=solution_path,
                payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
            )
            result = subprocess.run(
                [node, str(launcher)],
                cwd=build_tmp,
                text=True,
                capture_output=True,
                timeout=10,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip().splitlines()[-1], "[0,1]")

    def test_prepare_go_debug_session_builds_tcp_delve_launch_config(self) -> None:
        def fake_first_tool(*names: str) -> str | None:
            if "dlv" in names:
                return r"C:\tools\dlv.exe"
            if "go" in names:
                return r"C:\tools\go.exe"
            return None

        def fake_build(
            *,
            go: str,
            workdir: Path,
            solution_path: Path,
            payload: dict[str, object],
            env: dict[str, str],
        ) -> Path:
            exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
            exe_path.write_text("", encoding="utf-8")
            self.assertEqual(go, r"C:\tools\go.exe")
            self.assertEqual(payload["challengeId"], "lc_1")
            self.assertTrue(solution_path.is_file())
            self.assertIn("GOCACHE", env)
            return exe_path

        with tempfile.TemporaryDirectory() as source_tmp:
            solution_path = Path(source_tmp) / "lc_1.go"
            solution_path.write_text(
                "package main\n\nfunc solve(data []int, target int) int { return 0 }\n",
                encoding="utf-8",
            )
            with (
                patch.object(debug, "_first_tool", side_effect=fake_first_tool),
                patch.object(debug, "_build_go_debug_target", side_effect=fake_build),
                patch.object(debug, "_free_tcp_port", return_value=43123),
            ):
                session = debug._prepare_go_debug_session(
                    {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    solution_path,
                )

        tempdir_name = session.tempdir.name if session.tempdir is not None else ""
        try:
            self.assertEqual(session.adapter_executable, r"C:\tools\dlv.exe")
            self.assertEqual(session.adapter_args, ["dap", "--listen", "127.0.0.1:43123"])
            self.assertEqual(session.adapter_id, "delve-dap")
            self.assertEqual(session.adapter_connect_host, "127.0.0.1")
            self.assertEqual(session.adapter_connect_port, 43123)
            self.assertEqual(session.launch_config["mode"], "exec")
            self.assertTrue(str(session.launch_config["program"]).endswith("main.exe" if os.name == "nt" else "main"))
            self.assertEqual(session.breakpoint_path, solution_path)
            self.assertTrue(Path(tempdir_name).exists())
        finally:
            session.cleanup()
        self.assertFalse(Path(tempdir_name).exists())

    def test_build_go_debug_target_writes_function_harness(self) -> None:
        def fake_run_process(
            args: list[str],
            *,
            cwd: Path,
            timeout_seconds: float,
            input_text: str | None = None,
            env: dict[str, str] | None = None,
        ) -> subprocess.CompletedProcess[str]:
            Path(args[args.index("-o") + 1]).write_text("", encoding="utf-8")
            self.assertIn("-gcflags=all=-N -l", args)
            self.assertIsNotNone(env)
            return subprocess.CompletedProcess(args, 0, "", "")

        source = """
package main

func solve(nums []int, target int) []int {
    return []int{0, 1}
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.go"
            solution_path.write_text(source, encoding="utf-8")
            with patch.object(debug, "_run_process", side_effect=fake_run_process):
                exe_path = debug._build_go_debug_target(
                    go="go",
                    workdir=Path(build_tmp),
                    solution_path=solution_path,
                    payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    env={"GOCACHE": str(Path(build_tmp) / "gocache")},
                )

            self.assertTrue(exe_path.is_file())
            solution_text = (Path(build_tmp) / "solution.go").read_text(encoding="utf-8")
            self.assertIn(f"//line {str(solution_path).replace(chr(92), '/')}:1", solution_text)
            harness_text = (Path(build_tmp) / "coden_harness.go").read_text(encoding="utf-8")
            self.assertIn("func main()", harness_text)
            self.assertIn("var input_nums []int", harness_text)
            self.assertIn('__CodenMustDecode(__CodenField(__input, "nums"), &input_nums)', harness_text)
            self.assertIn("result := solve(input_nums, input_target)", harness_text)

    def test_prepare_kotlin_debug_session_builds_java_adapter_launch_config(self) -> None:
        def fake_first_tool(*names: str) -> str | None:
            if "kotlinc" in names:
                return r"C:\tools\kotlinc.bat"
            if "java" in names:
                return r"C:\tools\java.exe"
            return None

        def fake_build(
            *,
            kotlinc: str,
            workdir: Path,
            solution_path: Path,
            payload: dict[str, object],
        ) -> debug.JavaDebugTarget:
            jar_path = workdir / "coden-kotlin-debug.jar"
            jar_path.write_text("", encoding="utf-8")
            self.assertEqual(kotlinc, r"C:\tools\kotlinc.bat")
            self.assertEqual(payload["challengeId"], "lc_1")
            self.assertTrue(solution_path.is_file())
            return debug.JavaDebugTarget(main_class="CodenHarnessKt", classpath=jar_path, source_path=solution_path)

        with tempfile.TemporaryDirectory() as source_tmp, tempfile.NamedTemporaryFile(suffix=".jar") as adapter:
            solution_path = Path(source_tmp) / "lc_1.kt"
            solution_path.write_text(
                "class Solution { fun solve(data: List<Int>, target: Int) = 0 }\n",
                encoding="utf-8",
            )
            with (
                patch.object(debug, "_first_tool", side_effect=fake_first_tool),
                patch.object(debug, "_build_kotlin_debug_target", side_effect=fake_build),
                patch.dict(os.environ, {"CODEN_JAVA_DEBUG_ADAPTER": adapter.name}, clear=False),
            ):
                session = debug._prepare_kotlin_debug_session(
                    {"challengeId": "lc_1", "caseIds": ["sample-1"]},
                    solution_path,
                )

        tempdir_name = session.tempdir.name if session.tempdir is not None else ""
        try:
            self.assertEqual(session.adapter_executable, r"C:\tools\java.exe")
            self.assertEqual(session.adapter_args, ["-jar", adapter.name])
            self.assertEqual(session.adapter_id, "java-debug")
            self.assertEqual(session.launch_config["type"], "java")
            self.assertEqual(session.launch_config["mainClass"], "CodenHarnessKt")
            self.assertTrue(session.launch_config["classPaths"][0].endswith("coden-kotlin-debug.jar"))
            self.assertEqual(session.breakpoint_path, solution_path)
            self.assertTrue(Path(tempdir_name).exists())
        finally:
            session.cleanup()
        self.assertFalse(Path(tempdir_name).exists())

    def test_build_kotlin_debug_target_writes_function_harness(self) -> None:
        def fake_run_process(
            args: list[str],
            *,
            cwd: Path,
            timeout_seconds: float,
            input_text: str | None = None,
            env: dict[str, str] | None = None,
        ) -> subprocess.CompletedProcess[str]:
            Path(args[args.index("-d") + 1]).write_text("", encoding="utf-8")
            self.assertIn("-include-runtime", args)
            return subprocess.CompletedProcess(args, 0, "", "")

        source = """
class Solution {
    fun solve(nums: MutableList<Int>, target: Int): MutableList<Int> {
        return mutableListOf(0, 1)
    }
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.kt"
            solution_path.write_text(source, encoding="utf-8")
            with patch.object(debug, "_run_process", side_effect=fake_run_process):
                target = debug._build_kotlin_debug_target(
                    kotlinc="kotlinc",
                    workdir=Path(build_tmp),
                    solution_path=solution_path,
                    payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
                )

            self.assertEqual(target.main_class, "CodenHarnessKt")
            self.assertEqual(target.classpath, Path(build_tmp) / "coden-kotlin-debug.jar")
            self.assertEqual(target.source_path, solution_path)
            harness_text = (Path(build_tmp) / "CodenHarness.kt").read_text(encoding="utf-8")
            self.assertIn("fun main()", harness_text)
            self.assertIn("val solution = Solution()", harness_text)
            self.assertIn("solution.solve(input_nums, input_target)", harness_text)

    @unittest.skipUnless(shutil.which("dotnet"), "dotnet SDK is not installed")
    def test_csharp_function_debug_target_builds_with_user_solution_path(self) -> None:
        dotnet = shutil.which("dotnet")
        assert dotnet is not None
        source = """
using System.Collections.Generic;

public class Solution
{
    public List<int> Solve(List<int> nums, int target)
    {
        return new List<int> { 0, 1 };
    }
}
"""
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as build_tmp:
            solution_path = Path(source_tmp) / "lc_1.cs"
            solution_path.write_text(source, encoding="utf-8")
            env = os.environ.copy()
            env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
            env["DOTNET_NOLOGO"] = "1"

            dll_path = debug._build_csharp_debug_target(
                dotnet=dotnet,
                workdir=Path(build_tmp),
                solution_path=solution_path,
                payload={"challengeId": "lc_1", "caseIds": ["sample-1"]},
                env=env,
            )

            self.assertTrue(dll_path.is_file())
            project_text = (Path(build_tmp) / "CodenDebug.csproj").read_text(encoding="utf-8")
            self.assertIn(str(solution_path), project_text)
            self.assertIn("<StartupObject>Program</StartupObject>", project_text)
