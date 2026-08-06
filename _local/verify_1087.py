from __future__ import annotations

import importlib.util
import itertools
import json
import math
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "dsa" / "leetcode" / "1087_brace-expansion"
sys.path.insert(0, str(ROOT))

from server.app.engine_runner import run_player_code
from server.app.validated_cases import select_cases_for_run


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def oracle(s: str) -> list[str]:
    segments = [segment for segment in re.split(r"(\{[^{}]*\})", s) if segment]
    positions: list[tuple[str, ...]] = []
    for segment in segments:
        if segment.startswith("{"):
            positions.append(tuple(segment[1:-1].split(",")))
        else:
            positions.extend((character,) for character in segment)
    return sorted("".join(selection) for selection in itertools.product(*positions))


def insertion_sort_control(s: str) -> list[str]:
    groups: list[list[str]] = []
    cursor = 0
    while cursor < len(s):
        if s[cursor] == "{":
            closing_brace = s.find("}", cursor)
            groups.append(s[cursor + 1 : closing_brace].split(","))
            cursor = closing_brace + 1
        else:
            groups.append([s[cursor]])
            cursor += 1

    words = [""]
    for choices in groups:
        words = [prefix + choice for prefix in words for choice in choices]

    for i in range(1, len(words)):
        current = words[i]
        j = i - 1
        while j >= 0 and words[j] > current:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = current
    return words


def assert_equal(label: str, actual: list[str], expected: list[str]) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


current = load_module(
    "lc1087_current",
    PACKAGE / "variants" / "optimal" / "solutions" / "solve.py",
)
candidate = load_module(
    "lc1087_candidate",
    PACKAGE / "variants" / "optimal" / "solutions" / "candidate.py",
)
native = load_module(
    "lc1087_native",
    PACKAGE / "variants" / "optimal" / "solutions" / "leetcode.py",
)

cases_payload = json.loads((PACKAGE / "cases.json").read_text(encoding="utf-8"))
benchmark_payload = json.loads((PACKAGE / "benchmark.json").read_text(encoding="utf-8"))
authored_cases = cases_payload["cases"] + benchmark_payload["cases"]

for case in authored_cases:
    s = case["input"]["s"]
    expected = oracle(s)
    assert_equal(f"{case['id']} authored expected", case["expected"], expected)
    assert_equal(f"{case['id']} protected", current.solve(s), expected)
    assert_equal(f"{case['id']} candidate", candidate.solve(s), expected)
    assert_equal(f"{case['id']} native", native.Solution().expand(s), expected)
    assert_equal(f"{case['id']} slower control", insertion_sort_control(s), expected)

boundaries = [
    "a",
    "z" * 50,
    "{b,a}",
    "{b,a}{d,c}",
    "a{d,b,c}z",
    "{d,c,b,a}x{f,e}",
    "z{x,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a}",
]
for test_number, s in enumerate(boundaries, 1):
    expected = oracle(s)
    assert_equal(f"boundary {test_number} protected", current.solve(s), expected)
    assert_equal(f"boundary {test_number} candidate", candidate.solve(s), expected)
    assert_equal(f"boundary {test_number} native", native.Solution().expand(s), expected)
    assert_equal(f"boundary {test_number} control", insertion_sort_control(s), expected)

rng = random.Random(1087)
alphabet = "abcdefghijklmnopqrstuvwxyz"
for test_number in range(5000):
    tokens: list[str] = []
    brace_groups = 0
    expansion_count = 1
    target_positions = rng.randint(1, 14)
    for _ in range(target_positions):
        use_group = brace_groups < 6 and rng.random() < 0.45
        if use_group:
            choice_count = rng.randint(2, 4)
            if expansion_count * choice_count > 256:
                use_group = False
        if use_group:
            choices = rng.sample(alphabet, choice_count)
            rng.shuffle(choices)
            token = "{" + ",".join(choices) + "}"
            if sum(map(len, tokens)) + len(token) <= 50:
                tokens.append(token)
                brace_groups += 1
                expansion_count *= choice_count
                continue
        if sum(map(len, tokens)) < 50:
            tokens.append(rng.choice(alphabet))
    s = "".join(tokens)
    expected = oracle(s)
    assert_equal(f"random {test_number} protected", current.solve(s), expected)
    assert_equal(f"random {test_number} candidate", candidate.solve(s), expected)
    assert_equal(f"random {test_number} native", native.Solution().expand(s), expected)
    assert_equal(f"random {test_number} control", insertion_sort_control(s), expected)

candidate_source = (PACKAGE / "variants" / "optimal" / "solutions" / "candidate.py").read_text(encoding="utf-8")
protected_source = (PACKAGE / "variants" / "optimal" / "solutions" / "solve.py").read_text(encoding="utf-8")
control_source = '''
def solve(s: str) -> list[str]:
    groups: list[list[str]] = []
    cursor = 0
    while cursor < len(s):
        if s[cursor] == "{":
            closing_brace = s.find("}", cursor)
            groups.append(s[cursor + 1 : closing_brace].split(","))
            cursor = closing_brace + 1
        else:
            groups.append([s[cursor]])
            cursor += 1

    words = [""]
    for choices in groups:
        words = [prefix + choice for prefix in words for choice in choices]

    for i in range(1, len(words)):
        current = words[i]
        j = i - 1
        while j >= 0 and words[j] > current:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = current
    return words
'''


def verdict(source: str) -> dict[str, object]:
    run_cases, benchmark_cases = select_cases_for_run("lc_1087", mode="real_test")
    result = run_player_code(
        challenge_id="lc_1087",
        source=source,
        n=16,
        seed=1087,
        mode="real_test",
        run_cases=run_cases,
        benchmark_cases=benchmark_cases,
    )
    scaling = result.runtime_scaling_data
    relative_growth_exponent = None
    if len(scaling) >= 2 and scaling[0].ratio > 0 and scaling[-1].ratio > 0:
        relative_growth_exponent = math.log(scaling[-1].ratio / scaling[0].ratio) / math.log(
            scaling[-1].size / scaling[0].size
        )
    return {
        "passed": result.passed,
        "correct": result.correct,
        "within_threshold": result.within_threshold,
        "complexity_passed": result.complexity_passed,
        "correctness_cases": [case.passed for case in result.case_results if case.kind != "benchmark"],
        "benchmark_cases": [case.passed for case in result.case_results if case.kind == "benchmark"],
        "relative_growth_exponent": relative_growth_exponent,
        "largest_runtime_ratio": scaling[-1].ratio if scaling else None,
        "runtime_scaling_data": [point.model_dump() for point in scaling],
        "message": result.message,
    }


summary = {
    "authored_cases": len(authored_cases),
    "ordinary_cases": len(cases_payload["cases"]),
    "benchmark_tiers": len(benchmark_payload["cases"]),
    "random_cases": 5000,
    "boundary_cases": len(boundaries),
    "protected": verdict(protected_source),
    "candidate": verdict(candidate_source),
    "slower_control": verdict(control_source),
}
print(json.dumps(summary, indent=2))
