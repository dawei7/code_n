from __future__ import annotations

import json
import shutil

import pytest

from server.app.external_programs import run_function_program


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is not installed")
def test_javascript_json_normalizer_preserves_proto_data_property() -> None:
    source = """
class Solution {
    solve() {
        const result = {};
        Object.defineProperty(result, "__proto__", {
            value: { safe: true },
            enumerable: true,
            configurable: true,
            writable: true,
        });
        return result;
    }
}
"""
    result = run_function_program(
        language="javascript",
        source=source,
        input_json="{}",
        param_names=[],
        param_hints={},
        returns_hint="Object",
        timeout_seconds=5.0,
    )

    assert result.error_message == ""
    assert json.loads(result.stdout.strip()) == {"__proto__": {"safe": True}}

