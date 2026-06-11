"""Spec generator for cOde(n) algorithm challenges.

Avoids the manual-indentation problem of multi-line source
strings by taking a structured input (a list of dicts) and
emitting the Python spec code with correct indentation.

Usage:
    python -m challenges.algorithms._generator \\
        --module graphs \\
        --input specs_to_add.py

Where `specs_to_add.py` defines SPECS_TO_ADD = [
    {
        "id": "graph_20",
        "name": "Topological Sort (Kahn)",
        "difficulty": 5,
        "complexity": "O_N2",
        "description": "...",
        "source_url": "...",
        "params": ["num_nodes", "edges"],
        "inputs": {...},
        "returns": "...",
        "solve": '''
            def solve(num_nodes, edges):
                ...
        ''',
        "verify": '''
            # Re-run and compare.
            ...
        ''',
        "samples": [Sample("...", "...")],
        "hint": "...",
        "parents": [],
        "children": [],
    },
    ...
]

The generator appends each new spec to the target module's
SPECS list, using a closing `SPECS.extend([...])` pattern.
It also writes the matching `optimal_solutions/<id>.py` files
so the Solve button keeps working.

Why a generator at all?
----------------
Each new spec needs a `*_SOURCE` string literal whose function
body must be indented (4 spaces) inside the string, plus
matching `setup_fn` / `verify_fn` and an `AlgorithmSpec(...)`
block at the right indent level inside `SPECS.extend([...])`.
Getting all four levels right by hand is error-prone — and the
mistakes are silent until the spec gauntlet or the registry
import fails. This generator centralises the formatting so
the author can focus on the algorithm, not the whitespace.
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import sys
from pathlib import Path
from typing import Any


# Where the modules live, relative to the project root.
CHALLENGES_DIR = Path(__file__).resolve().parent.parent.parent
ALGORITHMS_DIR = CHALLENGES_DIR / "challenges" / "algorithms"
OPTIMAL_DIR = CHALLENGES_DIR / "optimal_solutions"


def _indent_block(text: str, spaces: int) -> str:
    """Indent every non-blank line of `text` by `spaces` spaces.

    Blank lines are left blank (no whitespace) so the source
    stays readable. Leading/trailing newlines are stripped so
    the caller can wrap the result cleanly.
    """
    pad = " " * spaces
    out_lines = []
    for line in text.strip("\n").splitlines():
        if line.strip() == "":
            out_lines.append("")
        else:
            out_lines.append(pad + line)
    return "\n".join(out_lines)


def _format_source(name: str, body: str) -> str:
    """Wrap a `def solve(...)` body as a top-level spec source string.

    The string is a triple-quoted Python literal whose content
    is a complete `def solve(...)` definition. The function body
    must be indented by 4 spaces INSIDE the string — the
    generator does this for the caller.

    Strategy: the caller is writing the function in the
    middle of a Python dict literal, so every line is over-
    indented. We compute the smallest leading-whitespace
    prefix among all non-blank lines, then strip that many
    spaces from every line. The first `def solve` ends up
    at column 0; the rest of the function body keeps its
    RELATIVE indent (which is what the author intended).
    """
    raw_lines = body.strip("\n").splitlines()
    # Compute the minimum indent across non-blank lines.
    min_indent = None
    for line in raw_lines:
        if line.strip() == "":
            continue
        lead = len(line) - len(line.lstrip())
        if min_indent is None or lead < min_indent:
            min_indent = lead
    if min_indent is None:
        min_indent = 0
    # Strip that prefix from every line.
    dedented = []
    for line in raw_lines:
        if line.strip() == "":
            dedented.append("")
        else:
            dedented.append(line[min_indent:])
    # Now apply a small re-indent: ensure the FIRST non-blank
    # line is at column 0. If the author wrote `def solve` at
    # the minimum-indent level, it's already there; if they
    # wrote it one level deeper, we still leave it (rare).
    body_text = "\n".join(dedented)
    return f"{name} = '''\n{body_text}\n'''\n\n"


def _format_helper(name: str, body: str) -> str:
    """Wrap a helper function definition at module level.

    `body` is a function body (no `def` line). The generator
    adds the `def name(...):` and indents the body.
    """
    pad = "    "
    formatted = []
    for line in body.strip("\n").splitlines():
        if line.strip() == "":
            formatted.append("")
        else:
            formatted.append(pad + line)
    body_indented = "\n".join(formatted)
    return f"def {name}(...):\n{body_indented}\n\n"


def render_spec_block(record: dict[str, Any], complexity_map: dict[str, str]) -> str:
    """Render a single AlgorithmSpec(...) block for the SPECS list.

    Indentation: 4 spaces (inside SPECS.extend([...])).
    """
    complexity = complexity_map.get(record["complexity"], "O_N")
    params_str = "[" + ", ".join(f'"{p}"' for p in record["params"]) + "]"
    inputs_str = "{\n" + _indent_block(
        "".join(f'    "{k}": "{v}",\n' for k, v in record["inputs"].items()),
        8,
    ).rstrip(",\n") + "\n    }" if record.get("inputs") else "{}"
    # Build samples.
    samples_lines = []
    for s in record["samples"]:
        # Each sample is a Sample(input_repr, output_repr) call.
        samples_lines.append(f'            Sample("{s[0]}", "{s[1]}"),')
    samples_str = "\n".join(samples_lines) if samples_lines else ""
    parents_str = "[" + ", ".join(f'"{p}"' for p in record.get("parents", [])) + "]"
    children_str = "[" + ", ".join(f'"{c}"' for c in record.get("children", [])) + "]"
    source_const = record["id"].upper().replace("-", "_") + "_SOURCE"
    setup_fn = "_setup_" + record["id"].replace("-", "_")
    verify_fn = "_verify_" + record["id"].replace("-", "_")
    description = record["description"].rstrip()
    hint = record.get("hint", "")

    parts = [
        f'    AlgorithmSpec(',
        f'        id="{record["id"]}",',
        f'        name="{record["name"]}",',
        f'        category="{record["category"]}",',
        f'        difficulty={record["difficulty"]},',
        f'        required_complexity=ComplexityClass.{complexity},',
        f'        description=(',
    ]
    # Description is a parenthesized string concatenation; preserve
    # the user's newlines by wrapping in a single triple-quoted
    # literal at indent 12.
    desc_block = _indent_block(f'"""\n{description}\n"""', 12)
    parts.append(desc_block + ",")
    parts.append(f'        source_url="{record["source_url"]}",')
    parts.append(f'        params={params_str},')
    parts.append(f'        inputs={inputs_str},')
    parts.append(f'        returns="{record["returns"]}",')
    parts.append(f'        source={source_const},')
    parts.append(f'        setup_fn={setup_fn},')
    parts.append(f'        verify_fn={verify_fn},')
    if samples_str:
        parts.append(f'        samples=[')
        parts.append(samples_str)
        parts.append(f'        ],')
    parts.append(f'        hint="{hint}",')
    parts.append(f'        parents={parents_str},')
    parts.append(f'        children={children_str},')
    parts.append(f'    ),')
    return "\n".join(parts) + "\n"


def render_helpers(record: dict[str, Any]) -> str:
    """Render the source string + setup_fn + verify_fn for a record.

    These are emitted at module level (0-indent).
    """
    out = []
    # 1. The source string (def solve wrapped in triple-quotes).
    source_name = record["id"].upper().replace("-", "_") + "_SOURCE"
    out.append(_format_source(source_name, record["solve"]))
    # 2. setup_fn.
    setup_name = "_setup_" + record["id"].replace("-", "_")
    out.append(f"def {setup_name}(challenge, n, seed):\n")
    body = _indent_block(record["setup"], 4)
    out.append(body)
    out.append("\n\n")
    # 3. verify_fn.
    verify_name = "_verify_" + record["id"].replace("-", "_")
    out.append(f"def {verify_name}(challenge, result):\n")
    body = _indent_block(record["verify"], 4)
    out.append(body)
    out.append("\n\n")
    return "".join(out)


def render_module_extension(records: list[dict[str, Any]], complexity_map: dict[str, str]) -> str:
    """Render the full text to append to the target module.

    Layout:
        # === <id>: <name> ===
        <source + helpers>

        # === <id>: <name> ===
        <source + helpers>

        ...

        # Append the new <category> specs to SPECS.
        SPECS.extend([
            <spec block 1>

            <spec block 2>
            ...
        ])
    """
    out = []
    for rec in records:
        out.append(f"\n\n# === {rec['id']}: {rec['name']} ===\n\n")
        out.append(render_helpers(rec))
    out.append("\n# Append the new specs to SPECS.\n")
    out.append("SPECS.extend([\n")
    for rec in records:
        out.append(render_spec_block(rec, complexity_map))
    out.append("])\n")
    return "".join(out)


def render_optimal_solution(record: dict[str, Any]) -> str:
    """Render the standalone optimal_solutions/<id>.py file."""
    name = record["name"]
    description = record["description"].splitlines()[0] if record.get("description") else name
    # The solve() body in the record is already a complete def
    # solve(...) — wrap it as a module-level function.
    body = record["solve"].strip("\n")
    return (
        f'"""Optimal solution for {record["id"]}: {name}.\n\n'
        f"{description}\n\"\"\"\n\n\n"
        f"{body}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--module",
        required=True,
        help="Target module name (e.g. 'graphs', 'dynamic', 'strings', 'trees')",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Python file with a SPECS_TO_ADD list of dicts",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the rendered output instead of writing files",
    )
    args = parser.parse_args()

    # Load the input file as a Python module so the author can
    # import helpers (Sample, etc.) and reuse functions.
    input_path = Path(args.input).resolve()
    spec_module_spec = importlib.util.spec_from_file_location("input_specs", input_path)
    input_module = importlib.util.module_from_spec(spec_module_spec)
    spec_module_spec.loader.exec_module(input_module)
    records = input_module.SPECS_TO_ADD
    if not isinstance(records, list):
        print("ERROR: SPECS_TO_ADD must be a list", file=sys.stderr)
        return 1

    complexity_map = {
        "O_1": "O_1",
        "O_LOG_N": "O_LOG_N",
        "O_N": "O_N",
        "O_N_LOG_N": "O_N_LOG_N",
        "O_N2": "O_N2",
        "O_N3": "O_N3",
        "O_2N": "O_2N",
        "UNKNOWN": "UNKNOWN",
    }

    # Render the module extension.
    module_path = ALGORITHMS_DIR / f"{args.module}.py"
    extension_text = render_module_extension(records, complexity_map)
    if args.dry_run:
        print(extension_text)
    else:
        with open(module_path, "a", encoding="utf-8") as f:
            f.write(extension_text)
        print(f"Appended to {module_path}")

    # Render each optimal_solutions/<id>.py.
    for rec in records:
        opt_text = render_optimal_solution(rec)
        opt_path = OPTIMAL_DIR / f"{rec['id']}.py"
        if args.dry_run:
            print(f"\n--- {opt_path} ---\n{opt_text}")
        else:
            with open(opt_path, "w", encoding="utf-8") as f:
                f.write(opt_text)
            print(f"Wrote {opt_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
