"""LeetCode challenge specifications generated from local docs.

The LeetCode dataset is large and docs-first. This module exposes the
documented problems to the normal challenge registry so the app can browse and
open them by dataset while the richer runnable specs are filled in over time.
"""

from __future__ import annotations

import ast
import json
import keyword
import random
import re
from pathlib import Path
from typing import Any

from code_n.counter import ComplexityClass
from challenges.spec import AlgorithmSpec, Sample


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "algorithms" / "leetcode"


INDEX_PATH = DOCS_ROOT / "index.json"


def _load_difficulty_metadata() -> dict[str, tuple[int, str, float, list[str]]]:
    """Build the 10-level rating from official tier + acceptance percentile.

    Easy and Medium are divided into three equally populated acceptance bands;
    Hard is divided into four. Within a tier, a higher acceptance rate means an
    easier sublevel. This always maps Easy -> 1..3, Medium -> 4..6, and Hard ->
    7..10 while adapting to the actual LeetCode corpus distribution.
    """
    if not INDEX_PATH.is_file():
        return {}
    try:
        questions = json.loads(INDEX_PATH.read_text(encoding="utf-8")).get("questions", [])
    except (OSError, json.JSONDecodeError):
        return {}

    configuration = {"Easy": (1, 3), "Medium": (4, 3), "Hard": (7, 4)}
    grouped: dict[str, list[dict[str, Any]]] = {label: [] for label in configuration}
    for question in questions:
        label = str(question.get("difficulty", ""))
        if label in grouped and question.get("acceptance_rate") is not None:
            grouped[label].append(question)

    result: dict[str, tuple[int, str, float, list[str]]] = {}
    for label, entries in grouped.items():
        base, band_count = configuration[label]
        entries.sort(key=lambda item: float(item["acceptance_rate"]), reverse=True)
        total = len(entries)
        for rank, question in enumerate(entries):
            band = min(band_count - 1, rank * band_count // max(total, 1))
            frontend_id = str(question.get("frontend_id", ""))
            acceptance = float(question["acceptance_rate"])
            categories = [
                f"leetcode_{str(topic.get('slug', '')).replace('-', '_')}"
                for topic in question.get("topics", [])
                if topic.get("slug")
            ]
            result[frontend_id] = (base + band, label, acceptance, categories)
    return result


_DIFFICULTY_METADATA = _load_difficulty_metadata()
_DIFFICULTY_FALLBACK = {"Easy": 2, "Medium": 5, "Hard": 8}


def _noop_source(params: list[str]) -> str:
    signature = ", ".join(params)
    return f"def solve({signature}):\n    return None\n"


def _noop_verify(challenge, result) -> bool:
    return False


def _source_matches_contract(source: str, params: list[str]) -> bool:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False

    if any(isinstance(node, ast.ClassDef) for node in tree.body):
        return False

    solve = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "solve"),
        None,
    )
    if solve is None:
        return False
    source_params = [arg.arg for arg in solve.args.args]
    if source_params != params:
        return False
    if "return None" in source:
        return False
    if any(token in source for token in (".val", ".next", "TreeNode", "ListNode")):
        return False
    return True


def _load_solution_source(doc_path: Path, params: list[str]) -> str:
    relative_doc = doc_path.relative_to(DOCS_ROOT)
    solution_path = (PROJECT_ROOT / "optimal_solutions" / "leetcode" / relative_doc).with_suffix(".py")
    if solution_path.is_file():
        source = solution_path.read_text(encoding="utf-8")
        if _source_matches_contract(source, params):
            return source
    return _noop_source(params)


def _normalise_literal(raw: str) -> str:
    return re.sub(r"\btrue\b", "True", re.sub(r"\bfalse\b", "False", re.sub(r"\bnull\b", "None", raw)))


def _literal_value(raw: str) -> Any:
    return ast.literal_eval(_normalise_literal(raw.strip()))


def _sample_values(sample: Sample, params: list[str]) -> dict[str, Any]:
    values: dict[str, Any] = {}
    text = sample.input_repr.strip()
    for index, name in enumerate(params):
        next_names = [re.escape(other) for other in params[index + 1:]]
        lookahead = rf",\s*(?:{'|'.join(next_names)})\s*=" if next_names else r"$"
        match = re.search(rf"(?:^|,\s*){re.escape(name)}\s*=\s*(.*?)(?={lookahead})", text)
        if not match:
            continue
        try:
            values[name] = _literal_value(match.group(1))
        except (SyntaxError, ValueError):
            continue
    return values


def _sized_like_sample(value: Any, n: int, rng: random.Random) -> Any:
    if isinstance(value, list):
        if not value:
            return []
        size = max(1, n)
        if all(isinstance(item, str) for item in value):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            shared = rng.choice(alphabet)
            words = []
            for _ in range(size):
                length = rng.randint(3, 8)
                chars = [shared] + [rng.choice(alphabet) for _ in range(length - 1)]
                rng.shuffle(chars)
                words.append("".join(chars))
            return words
        if all(isinstance(item, int) and not isinstance(item, bool) for item in value):
            low = min(value + [0])
            high = max(value + [10])
            return [rng.randint(low, high) for _ in range(size)]
        if all(isinstance(item, list) for item in value):
            rows = max(1, min(n, 20))
            template = value[0] if value else [0]
            cols = max(1, len(template))
            return [_sized_like_sample(template, cols, rng) for _ in range(rows)]
        return [value[i % len(value)] for i in range(size)]
    if isinstance(value, int) and not isinstance(value, bool):
        return n if value >= 0 else -n
    return value


def _generated_value(name: str, doc: str, n: int, rng: random.Random) -> Any:
    lowered = f"{name} {doc}".lower()
    if name == "n" or lowered.startswith("n "):
        return n
    if "list[str]" in lowered or name in {"words", "wordlist", "dictionary"}:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shared = rng.choice(alphabet) if "common" in lowered or name == "words" else ""
        words = []
        for _ in range(max(1, n)):
            length = rng.randint(3, 8)
            chars = [rng.choice(alphabet) for _ in range(length)]
            if shared:
                chars[0] = shared
            words.append("".join(chars))
        return words
    if "string" in lowered or name in {"s", "t", "word"}:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return "".join(rng.choice(alphabet) for _ in range(max(1, n)))
    if "matrix" in lowered or "grid" in lowered or name in {"grid", "matrix"}:
        rows = max(1, min(n, 20))
        cols = max(1, min(n, 20))
        return [[rng.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    if "list" in lowered or "array" in lowered or name in {"nums", "arr", "data"}:
        return [rng.randint(-20, 20) for _ in range(max(1, n))]
    if "bool" in lowered:
        return bool(rng.getrandbits(1))
    return rng.randint(0, max(1, n))


def _leetcode_setup(params: list[str], input_docs: dict[str, str], samples: list[Sample], source: str):
    def setup(challenge, n, seed):
        rng = random.Random(seed)
        sample_values = _sample_values(samples[0], params) if samples else {}
        values: dict[str, Any] = {}
        for name in params:
            if name in sample_values:
                values[name] = _sized_like_sample(sample_values[name], n, rng)
            else:
                values[name] = _generated_value(name, input_docs.get(name, ""), n, rng)
        challenge._setup_data = values
        if source and "return None" not in source:
            try:
                import copy
                challenge._expected_result = challenge._reference_solve(**copy.deepcopy(values))
            except Exception:
                challenge._expected_result = None
        return values

    return setup


def _leetcode_verify(challenge, result) -> bool:
    if not hasattr(challenge, "_expected_result"):
        return False
    return result == challenge._expected_result


def _read_field(text: str, field: str) -> str:
    pattern = rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def _read_link_slug_and_url(text: str) -> tuple[str, str]:
    raw = _read_field(text, "Official Link")
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", raw)
    if not match:
        return "", ""
    return match.group(1).strip(), match.group(2).strip()


def _section(text: str, start: str, end_markers: tuple[str, ...]) -> str:
    start_index = text.find(start)
    if start_index == -1:
        return ""
    body_start = start_index + len(start)
    end_indexes = [
        index
        for marker in end_markers
        if (index := text.find(marker, body_start)) != -1
    ]
    body_end = min(end_indexes) if end_indexes else len(text)
    return text[body_start:body_end].strip()


def _goal(text: str) -> str:
    return _section(
        text,
        "### Goal",
        ("### Function Contract", "### Input", "### Output", "### Examples", "## Underlying"),
    )


def _inputs(text: str) -> list[tuple[str, str]]:
    body = _section(
        text,
        "**Inputs**",
        ("**Return value**", "### Output", "### Examples", "## Underlying"),
    )
    if not body:
        body = _section(text, "### Input", ("### Output", "### Examples", "## Underlying"))

    inputs: list[tuple[str, str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        match = re.match(r"-\s*`?([A-Za-z_][A-Za-z0-9_]*)`?\s*:?\s*(.*)", stripped)
        if match:
            name, doc = match.groups()
            inputs.append((name, doc.strip() or "Input value."))
    return inputs


def _safe_param_name(name: str) -> str:
    cleaned = re.sub(r"\W+", "_", name).strip("_") or "value"
    if cleaned[0].isdigit():
        cleaned = f"arg_{cleaned}"
    if keyword.iskeyword(cleaned):
        cleaned = f"{cleaned}_"
    return cleaned


def _return_value(text: str) -> str:
    body = _section(text, "**Return value**", ("### Examples", "## Underlying"))
    if body:
        return body.strip()
    return _section(text, "### Output", ("### Examples", "## Underlying")).strip() or "Return the result."


def _examples(text: str) -> list[Sample]:
    examples: list[Sample] = []
    pending_input: str | None = None
    in_examples = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line == "### Examples":
            in_examples = True
            continue
        if in_examples and (line == "---" or line.startswith("## ")):
            break
        if not in_examples:
            continue
        if line.startswith("- Input: `") and line.endswith("`"):
            pending_input = line.removeprefix("- Input: `")[:-1]
        elif line.startswith("- Output: `") and line.endswith("`") and pending_input is not None:
            examples.append(Sample(pending_input, line.removeprefix("- Output: `")[:-1]))
            pending_input = None
        elif re.match(r"^\d+\.\s*`", line) and "` -> `" in line and line.endswith("`"):
            left, right = line.split("` -> `", 1)
            pending = left.split("`", 1)[1]
            examples.append(Sample(pending, right[:-1]))
    return examples[:3]


def _parse_complexity(text: str) -> ComplexityClass:
    tc_match = re.search(r"-\s*\*\*Time Complexity\*\*:\s*`?([^\n`]+)`?", text, re.IGNORECASE)
    if not tc_match:
        return ComplexityClass.UNKNOWN
    raw = tc_match.group(1).strip().lower()
    
    # Check exponential first
    if "o(2" in raw or "2^" in raw or "2\u207f" in raw or "exponential" in raw:
        return ComplexityClass.O_2N
        
    # Check cubic
    if "o(n3)" in raw or "o(n^3)" in raw or "o(n\u00b3)" in raw or "n^3" in raw or "n³" in raw or "3" in raw:
        return ComplexityClass.O_N3
        
    # Check quadratic
    if "o(n2)" in raw or "o(n^2)" in raw or "o(n\u00b2)" in raw or "n^2" in raw or "n²" in raw or "n2" in raw or "quadratic" in raw or "*" in raw or "^2" in raw or "²" in raw or "2" in raw:
        return ComplexityClass.O_N2
        
    # Check n log n
    if "n log" in raw or "nlog" in raw:
        return ComplexityClass.O_N_LOG_N
        
    # Check log n
    if "log" in raw:
        return ComplexityClass.O_LOG_N
        
    # Check constant
    if "o(1)" in raw or "constant" in raw or raw == "1":
        return ComplexityClass.O_1
        
    # Check linear (default fallback for most single/addition/total loops or variables)
    if any(c.isalpha() for c in raw):
        return ComplexityClass.O_N
        
    return ComplexityClass.UNKNOWN


def _build_spec(path: Path) -> AlgorithmSpec | None:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    frontend_id = _read_field(text, "Frontend ID")
    if not title_match or not frontend_id:
        return None
 
    slug, url = _read_link_slug_and_url(text)
    inputs = _inputs(text)
    params = []
    input_docs = {}
    seen_params: set[str] = set()
    for raw_name, doc in inputs:
        name = _safe_param_name(raw_name)
        if name in seen_params:
            continue
        seen_params.add(name)
        params.append(name)
        input_docs[name] = doc
    if not params:
        params = ["value"]
        input_docs = {"value": "Input value."}
 
    category = path.parent.name.replace("-", "_")
    difficulty_label = _read_field(text, "Difficulty")
    metadata = _DIFFICULTY_METADATA.get(frontend_id)
    difficulty = metadata[0] if metadata else _DIFFICULTY_FALLBACK.get(difficulty_label, 5)
    acceptance_rate = metadata[2] if metadata else None
    description = _goal(text) or f"Solve the LeetCode problem {title_match.group(1).strip()}."
    if url:
        source_url = url
    elif slug:
        source_url = f"https://leetcode.com/problems/{slug}/"
    else:
        source_url = ""
 
    samples = _examples(text)
    source = _load_solution_source(path, params)
    required_complexity = _parse_complexity(text)
 
    return AlgorithmSpec(
        id=f"lc_{frontend_id}",
        name=title_match.group(1).strip(),
        category=f"leetcode_{category}",
        difficulty=difficulty,
        required_complexity=required_complexity,
        description=description,
        source_url=source_url,
        params=params,
        inputs=input_docs,
        returns=_return_value(text),
        source=source,
        setup_fn=_leetcode_setup(params, input_docs, samples, source),
        verify_fn=_leetcode_verify if "return None" not in source else _noop_verify,
        samples=samples,
        hint="Use the Reference tab for the problem statement and algorithm outline.",
        max_n=50,
        difficulty_label=metadata[1] if metadata else difficulty_label,
        acceptance_rate=acceptance_rate,
        categories=metadata[3] if metadata else [f"leetcode_{category}"],
    )


def _collect_specs() -> list[AlgorithmSpec]:
    if not DOCS_ROOT.exists():
        return []
    specs = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if path.name.startswith("_") or path.stem.endswith("_de"):
            continue
        spec = _build_spec(path)
        if spec is not None:
            specs.append(spec)
    return specs


SPECS = _collect_specs()
