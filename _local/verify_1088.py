from __future__ import annotations

import bisect
import importlib.util
import itertools
import json
import math
import random
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "dsa" / "leetcode" / "1088_confusing-number-ii"
sys.path.insert(0, str(ROOT))

from server.app.engine_runner import run_player_code
from server.app.validated_cases import select_cases_for_run


ROTATED_CHARACTER = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_confusing_numbers() -> list[int]:
    confusing: list[int] = []
    for length in range(1, 10):
        for first_digit in "1689":
            for suffix in itertools.product("01689", repeat=length - 1):
                text = first_digit + "".join(suffix)
                value = int(text)
                rotated = int("".join(ROTATED_CHARACTER[digit] for digit in reversed(text)))
                if rotated != value:
                    confusing.append(value)

    maximum = 1_000_000_000
    rotated_maximum = int("".join(ROTATED_CHARACTER[digit] for digit in reversed(str(maximum))))
    if rotated_maximum != maximum:
        confusing.append(maximum)
    return confusing


CONFUSING_NUMBERS = build_confusing_numbers()


def oracle(n: int) -> int:
    return bisect.bisect_right(CONFUSING_NUMBERS, n)


def rescan_rotation_control(n: int) -> int:
    mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    answer = 0
    candidates = [1, 6, 8, 9]
    while candidates:
        value = candidates.pop()
        if value > n:
            continue

        text = str(value)
        rotated = int("".join(mapping[digit] for digit in reversed(text)))
        if rotated != value:
            answer += 1

        for digit in (0, 1, 6, 8, 9):
            candidate = value * 10 + digit
            if candidate <= n:
                candidates.append(candidate)
    return answer


def assert_equal(label: str, actual: int, expected: int) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected}, got {actual}")


current = load_module(
    "lc1088_current",
    PACKAGE / "variants" / "optimal" / "solutions" / "solve.py",
)
candidate = load_module(
    "lc1088_candidate",
    PACKAGE / "variants" / "optimal" / "solutions" / "candidate.py",
)
native = load_module(
    "lc1088_native",
    PACKAGE / "variants" / "optimal" / "solutions" / "leetcode.py",
)

cases_payload = json.loads((PACKAGE / "cases.json").read_text(encoding="utf-8"))
benchmark_payload = json.loads((PACKAGE / "benchmark.json").read_text(encoding="utf-8"))
authored_cases = cases_payload["cases"] + benchmark_payload["cases"]

for case in authored_cases:
    n = case["input"]["n"]
    expected = oracle(n)
    assert_equal(f"{case['id']} authored expected", case["expected"], expected)
    assert_equal(f"{case['id']} protected", current.solve(n), expected)
    assert_equal(f"{case['id']} candidate", candidate.solve(n), expected)
    assert_equal(f"{case['id']} native", native.Solution().confusingNumberII(n), expected)
    assert_equal(f"{case['id']} slower control", rescan_rotation_control(n), expected)

boundaries = [
    1,
    5,
    6,
    9,
    10,
    11,
    25,
    69,
    88,
    89,
    8000,
    999_999_999,
    1_000_000_000,
]
for test_number, n in enumerate(boundaries, 1):
    expected = oracle(n)
    assert_equal(f"boundary {test_number} protected", current.solve(n), expected)
    assert_equal(f"boundary {test_number} candidate", candidate.solve(n), expected)
    assert_equal(f"boundary {test_number} native", native.Solution().confusingNumberII(n), expected)
    assert_equal(f"boundary {test_number} control", rescan_rotation_control(n), expected)

rng = random.Random(1088)
for test_number in range(5000):
    n = rng.randint(1, 5000)
    expected = oracle(n)
    assert_equal(f"random {test_number} protected", current.solve(n), expected)
    assert_equal(f"random {test_number} candidate", candidate.solve(n), expected)
    assert_equal(f"random {test_number} native", native.Solution().confusingNumberII(n), expected)
    assert_equal(f"random {test_number} control", rescan_rotation_control(n), expected)

protected_source = (PACKAGE / "variants" / "optimal" / "solutions" / "solve.py").read_text(encoding="utf-8")
candidate_source = (PACKAGE / "variants" / "optimal" / "solutions" / "candidate.py").read_text(encoding="utf-8")
exhaustive_control_source = '''
def solve(n: int) -> int:
    mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    answer = 0
    for value in range(1, n + 1):
        remaining = value
        rotated = 0
        while remaining:
            digit = remaining % 10
            if digit not in mapping:
                break
            rotated = rotated * 10 + mapping[digit]
            remaining //= 10
        else:
            if rotated != value:
                answer += 1
    return answer
'''


def verdict(source: str, *, include_correctness: bool = True) -> dict[str, object]:
    run_cases, benchmark_cases = select_cases_for_run("lc_1088", mode="real_test")
    result = run_player_code(
        challenge_id="lc_1088",
        source=source,
        n=16,
        seed=1088,
        mode="real_test",
        run_cases=run_cases if include_correctness else run_cases[:1],
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
        "correctness_cases": [case.passed for case in result.case_results if case.kind != "benchmark"],
        "benchmark_cases": [case.passed for case in result.case_results if case.kind == "benchmark"],
        "relative_growth_exponent": relative_growth_exponent,
        "largest_runtime_ratio": scaling[-1].ratio if scaling else None,
        "runtime_scaling_data": [point.model_dump() for point in scaling],
        "message": result.message,
    }


summary = {
    "oracle_confusing_count_at_maximum": len(CONFUSING_NUMBERS),
    "authored_cases": len(authored_cases),
    "ordinary_cases": len(cases_payload["cases"]),
    "benchmark_tiers": len(benchmark_payload["cases"]),
    "random_cases": 5000,
    "boundary_cases": len(boundaries),
    "rescan_control_direct_authored_outputs": len(authored_cases),
    "protected": verdict(protected_source),
    "candidate": verdict(candidate_source),
    "exhaustive_control_benchmark": verdict(exhaustive_control_source, include_correctness=False),
}
print(json.dumps(summary, indent=2))
