"""Non-scaling complexity-certificate validation and run integration."""

from __future__ import annotations

import calendar
import json
import math
import random
import runpy
import shutil
import sqlite3
import subprocess
from bisect import bisect_left, bisect_right
from datetime import date, timedelta
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, groupby, permutations, product
from pathlib import Path

import pytest

from engine.complexity_certificates import validate_complexity_certificate
from engine.special_environments import category_is_runnable
from server.app.engine_runner import (
    _JudgeArrayReader,
    _JudgeListNode,
    _JudgeMajorityReader,
    _JudgeNode,
    _JudgePoint,
    _JudgeSea,
    _JudgeTreeNode,
    _color_red_triangle_match,
    _list_node_from_values,
    _list_node_to_values,
    _traffic_light_match,
)
from server.app.challenge_packages import (
    leetcode_complexity_certificate_path,
    leetcode_complexity_certificate_status,
    leetcode_package_dir,
    leetcode_solution_path,
)
from server.app.primary_languages import primary_language_for_challenge
from server.app.special_environments import run_special_environment
from tools.audit_leetcode_migration import build_report

from . import conftest


import bisect
import collections
import functools
import heapq
import itertools
import math
import string
import typing

LEETCODE_GLOBALS = {
    # typing
    "Optional": typing.Optional,
    "List": typing.List,
    "Dict": typing.Dict,
    "Set": typing.Set,
    "Tuple": typing.Tuple,
    "Deque": typing.Deque,
    "Any": typing.Any,
    "Union": typing.Union,
    "Callable": typing.Callable,
    "Iterator": typing.Iterator,
    "Iterable": typing.Iterable,
    "Mapping": typing.Mapping,
    "Sequence": typing.Sequence,
    # custom LeetCode data structures
    "ListNode": _JudgeListNode,
    "TreeNode": _JudgeTreeNode,
    "Node": _JudgeNode,
    "Point": _JudgePoint,
    "math": math,
    "heapq": heapq,
    "bisect": bisect,
    "itertools": itertools,
    "functools": functools,
    "collections": collections,
    "string": string,
}
# Export all standard functions into namespace
for mod in (math, collections, itertools, heapq, bisect, functools):
    LEETCODE_GLOBALS.update({k: getattr(mod, k) for k in dir(mod) if not k.startswith('_')})

def _optimal_solution_path(package: Path, ext: str = "py") -> str:
    candidates = [
        package / "variants" / "optimal" / f"solution.{ext}",
        package / "variants" / "optimal" / "solutions" / f"solution.{ext}",
        package / "variants" / "optimal" / "solutions" / f"leetcode.{ext}",
        package / "variants" / "optimal" / "solutions" / f"solve.{ext}",
    ]
    for c in candidates:
        if c.is_file():
            return str(c)
    return str(package / "variants" / "optimal" / f"solution.{ext}")

def _run_native_module(path: str, init_globals: dict | None = None) -> dict:
    g = dict(LEETCODE_GLOBALS)
    if init_globals:
        g.update(init_globals)
    return runpy.run_path(path, init_globals=g)

CERTIFIED_METHODS = {
    "2": "asymptotic_optimality",
    "6": "bounded_domain",
    "7": "bounded_domain",
    "9": "bounded_domain",
    "12": "bounded_domain",
    "13": "bounded_domain",
    "17": "asymptotic_optimality",
    "19": "asymptotic_optimality",
    "21": "asymptotic_optimality",
    "24": "asymptotic_optimality",
    "27": "asymptotic_optimality",
    "29": "bounded_domain",
    "31": "asymptotic_optimality",
    "36": "bounded_domain",
    "37": "bounded_domain",
    "38": "bounded_domain",
    "362": "bounded_domain",
    "384": "bounded_domain",
    "401": "bounded_domain",
    "405": "bounded_domain",
    "479": "bounded_domain",
    "800": "bounded_domain",
    "999": "bounded_domain",
    "1056": "bounded_domain",
    "1108": "bounded_domain",
    "1114": "bounded_concurrency",
    "1118": "bounded_domain",
    "1134": "bounded_domain",
    "1137": "bounded_domain",
    "1154": "bounded_domain",
    "1165": "asymptotic_optimality",
    "1188": "bounded_concurrency",
    "1226": "bounded_concurrency",
    "1271": "bounded_domain",
    "1274": "bounded_domain",
    "1275": "bounded_domain",
    "1279": "bounded_concurrency",
    "1281": "bounded_domain",
    "1284": "bounded_domain",
    "1290": "bounded_domain",
    "1291": "bounded_domain",
    "1307": "bounded_domain",
    "1323": "bounded_domain",
    "1344": "bounded_domain",
    "1401": "asymptotic_optimality",
    "1432": "bounded_domain",
    "1491": "bounded_domain",
    "1507": "bounded_domain",
    "1518": "bounded_domain",
    "1533": "asymptotic_optimality",
    "1556": "bounded_domain",
    "1620": "bounded_domain",
    "1623": "asymptotic_optimality",
    "1633": "asymptotic_optimality",
    "1635": "asymptotic_optimality",
    "1641": "bounded_domain",
    "1643": "bounded_domain",
    "1645": "asymptotic_optimality",
    "1646": "bounded_domain",
    "1651": "asymptotic_optimality",
    "1704": "asymptotic_optimality",
    "1706": "asymptotic_optimality",
    "1718": "bounded_domain",
    "1723": "bounded_domain",
    "1729": "asymptotic_optimality",
    "1731": "asymptotic_optimality",
    "1732": "bounded_domain",
    "1736": "bounded_domain",
    "1741": "asymptotic_optimality",
    "1812": "bounded_domain",
    "1813": "bounded_domain",
    "1815": "bounded_domain",
    "1884": "bounded_domain",
    "1886": "asymptotic_optimality",
    "1900": "bounded_domain",
    "1904": "bounded_domain",
    "1958": "bounded_domain",
    "1980": "asymptotic_optimality",
    "2081": "bounded_domain",
    "2119": "asymptotic_optimality",
    "2160": "bounded_domain",
    "2162": "bounded_domain",
    "2165": "bounded_domain",
    "2174": "bounded_domain",
    "2177": "asymptotic_optimality",
    "2178": "asymptotic_optimality",
    "2231": "bounded_domain",
    "2232": "bounded_domain",
    "2235": "bounded_domain",
    "2236": "bounded_domain",
    "2283": "asymptotic_optimality",
    "2305": "bounded_domain",
    "2310": "bounded_domain",
    "2317": "asymptotic_optimality",
    "2319": "asymptotic_optimality",
    "2335": "bounded_domain",
    "2347": "bounded_domain",
    "2396": "asymptotic_optimality",
    "2405": "asymptotic_optimality",
    "2409": "asymptotic_optimality",
    "2413": "asymptotic_optimality",
    "2428": "asymptotic_optimality",
    "2429": "bounded_domain",
    "2437": "bounded_domain",
    "2446": "bounded_domain",
    "2469": "asymptotic_optimality",
    "2520": "bounded_domain",
    "2544": "bounded_domain",
    "2549": "bounded_domain",
    "2566": "bounded_domain",
    "2647": "asymptotic_optimality",
    "2648": "asymptotic_optimality",
    "2649": "asymptotic_optimality",
    "2650": "asymptotic_optimality",
    "2651": "bounded_domain",
    "2664": "bounded_domain",
    "2665": "asymptotic_optimality",
    "2666": "asymptotic_optimality",
    "2667": "asymptotic_optimality",
    "2670": "bounded_domain",
    "2676": "bounded_domain",
    "2682": "bounded_domain",
    "2683": "asymptotic_optimality",
    "2690": "asymptotic_optimality",
    "2798": "bounded_domain",
    "2800": "bounded_domain",
    "2801": "bounded_domain",
    "2802": "asymptotic_optimality",
    "2803": "asymptotic_optimality",
    "2804": "asymptotic_optimality",
    "2805": "bounded_concurrency",
    "2806": "bounded_domain",
    "2821": "bounded_concurrency",
    "2824": "bounded_domain",
    "2928": "bounded_domain",
    "2932": "bounded_domain",
    "3001": "bounded_domain",
    "3014": "bounded_domain",
    "3024": "bounded_domain",
    "3099": "bounded_domain",
    "3100": "bounded_domain",
    "3114": "bounded_domain",
    "3127": "bounded_domain",
    "3136": "bounded_domain",
    "3146": "asymptotic_optimality",
    "3194": "bounded_domain",
    "3200": "bounded_domain",
    "3222": "bounded_domain",
    "3226": "bounded_domain",
    "3232": "bounded_domain",
    "3238": "bounded_domain",
    "3242": "bounded_domain",
    "3248": "bounded_domain",
    "3260": "asymptotic_optimality",
    "3270": "bounded_domain",
    "3274": "bounded_domain",
    "3280": "bounded_domain",
    "3285": "asymptotic_optimality",
    "3340": "asymptotic_optimality",
    "3437": "asymptotic_optimality",
    "3481": "asymptotic_optimality",
    "3483": "asymptotic_optimality",
    "3678": "bounded_domain",
    "3683": "bounded_domain",
    "3684": "bounded_domain",
    "3690": "bounded_domain",
    "3697": "bounded_domain",
    "3704": "bounded_domain",
    "3726": "bounded_domain",
    "3731": "bounded_domain",
    "3733": "asymptotic_optimality",
    "3747": "bounded_domain",
    "3750": "bounded_domain",
    "3753": "bounded_domain",
    "3754": "bounded_domain",
    "3813": "bounded_domain",
    "3821": "bounded_domain",
    "3842": "bounded_domain",
    "3894": "bounded_domain",
    "3895": "asymptotic_optimality",
    "3898": "asymptotic_optimality",
    "3899": "bounded_domain",
    "3908": "bounded_domain",
    "3931": "asymptotic_optimality",
    "3945": "bounded_domain",
    "3950": "bounded_domain",
    "3954": "bounded_domain",
    "3955": "bounded_domain",
    "3959": "bounded_domain",
    "3963": "asymptotic_optimality",
    "3966": "bounded_domain",
    "3986": "bounded_domain",
    "3988": "bounded_domain",
    "3990": "bounded_domain",
    "3996": "bounded_domain",
    "4000": "bounded_domain",
}


def test_add_two_numbers_optimality_certificate_covers_output_boundaries() -> None:
    add_two_numbers = _reference_solve("2")
    package = leetcode_package_dir("lc_2")
    assert package is not None
    node_type = type(_list_node_from_values([0]))
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py"),
        init_globals={"ListNode": node_type},
    )
    native_add_two_numbers = native_namespace["Solution"]().addTwoNumbers

    def oracle(left: list[int], right: list[int]) -> list[int]:
        left_value = sum(digit * 10**i for i, digit in enumerate(left))
        right_value = sum(digit * 10**i for i, digit in enumerate(right))
        total = left_value + right_value
        digits: list[int] = []
        while total:
            total, digit = divmod(total, 10)
            digits.append(digit)
        return digits or [0]

    def assert_matches(left: list[int], right: list[int], expected: list[int]) -> None:
        app_result = add_two_numbers(_list_node_from_values(left), _list_node_from_values(right))
        native_result = native_add_two_numbers(_list_node_from_values(left), _list_node_from_values(right))
        assert _list_node_to_values(app_result) == expected
        assert _list_node_to_values(native_result) == expected
        assert len(expected) in {max(len(left), len(right)), max(len(left), len(right)) + 1}

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        left = case["input"]["l1"]
        right = case["input"]["l2"]
        expected = oracle(left, right)
        assert case["expected"] == expected
        assert_matches(left, right, expected)

    for n in (1, 2, 99, 100):
        for m in (1, 2, 99, 100):
            left = [9] * n
            right = [1] * m
            assert_matches(left, right, oracle(left, right))


def test_zigzag_bounded_domain_matches_cycle_arithmetic_oracle() -> None:
    convert = _reference_solve("6")
    package = leetcode_package_dir("lc_6")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_convert = native_namespace["Solution"]().convert

    def oracle(s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        cycle = 2 * (num_rows - 1)
        result: list[str] = []
        for r in range(num_rows):
            for i in range(r, len(s), cycle):
                result.append(s[i])
                j = i + cycle - 2 * r
                if 0 < r < num_rows - 1 and j < len(s):
                    result.append(s[j])
        return "".join(result)

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        s = case["input"]["s"]
        num_rows = case["input"]["numRows"]
        expected = oracle(s, num_rows)
        assert case["expected"] == expected
        assert convert(s, num_rows) == expected
        assert native_convert(s, num_rows) == expected

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,."
    boundary = "".join(alphabet[i % len(alphabet)] for i in range(1000))
    for num_rows in range(1, 1001):
        expected = oracle(boundary, num_rows)
        assert convert(boundary, num_rows) == expected
        assert native_convert(boundary, num_rows) == expected


def test_reverse_integer_bounded_domain_matches_string_oracle() -> None:
    reverse = _reference_solve("7")
    package = leetcode_package_dir("lc_7")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_reverse = native_namespace["Solution"]().reverse

    def oracle(x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_value = sign * int(str(abs(x))[::-1])
        return reversed_value if -(2**31) <= reversed_value <= 2**31 - 1 else 0

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        x = case["input"]["x"]
        expected = oracle(x)
        assert case["expected"] == expected
        assert reverse(x) == expected
        assert native_reverse(x) == expected

    boundary_values = range(-10_000, 10_001)
    lower_edge = range(-(2**31), -(2**31) + 10_001)
    upper_edge = range(2**31 - 10_001, 2**31)
    for x in (*boundary_values, *lower_edge, *upper_edge):
        expected = oracle(x)
        assert reverse(x) == expected
        assert native_reverse(x) == expected


def test_palindrome_number_bounded_domain_matches_string_oracle() -> None:
    is_palindrome = _reference_solve("9")
    package = leetcode_package_dir("lc_9")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_is_palindrome = native_namespace["Solution"]().isPalindrome

    def oracle(x: int) -> bool:
        digits = str(x)
        return digits == digits[::-1]

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        x = case["input"]["x"]
        expected = oracle(x)
        assert case["expected"] == expected
        assert is_palindrome(x) == expected
        assert native_is_palindrome(x) == expected

    boundary_values = range(-10_000, 10_001)
    lower_edge = range(-(2**31), -(2**31) + 10_001)
    upper_edge = range(2**31 - 10_001, 2**31)
    for x in (*boundary_values, *lower_edge, *upper_edge):
        expected = oracle(x)
        assert is_palindrome(x) == expected
        assert native_is_palindrome(x) == expected


def test_integer_to_roman_bounded_domain_matches_digit_place_oracle() -> None:
    int_to_roman = _reference_solve("12")
    package = leetcode_package_dir("lc_12")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_int_to_roman = native_namespace["Solution"]().intToRoman

    thousands = ("", "M", "MM", "MMM")
    hundreds = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    tens = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    ones = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

    def oracle(num: int) -> str:
        return (
            thousands[num // 1000]
            + hundreds[num // 100 % 10]
            + tens[num // 10 % 10]
            + ones[num % 10]
        )

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        num = case["input"]["num"]
        expected = oracle(num)
        assert case["expected"] == expected

    for num in range(1, 4000):
        expected = oracle(num)
        assert int_to_roman(num) == expected
        assert native_int_to_roman(num) == expected


def test_roman_to_integer_bounded_domain_matches_digit_place_encoder() -> None:
    roman_to_int = _reference_solve("13")
    package = leetcode_package_dir("lc_13")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_roman_to_int = native_namespace["Solution"]().romanToInt

    thousands = ("", "M", "MM", "MMM")
    hundreds = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    tens = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    ones = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

    def encode(num: int) -> str:
        return (
            thousands[num // 1000]
            + hundreds[num // 100 % 10]
            + tens[num // 10 % 10]
            + ones[num % 10]
        )

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        numeral = case["input"]["s"]
        expected = case["expected"]
        assert numeral == encode(expected)

    for num in range(1, 4000):
        numeral = encode(num)
        assert roman_to_int(numeral) == num
        assert native_roman_to_int(numeral) == num


def test_phone_combinations_optimality_matches_complete_cartesian_domain() -> None:
    letter_combinations = _reference_solve("17")
    package = leetcode_package_dir("lc_17")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_letter_combinations = native_namespace["Solution"]().letterCombinations
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def oracle(digits: str) -> list[str]:
        return ["".join(values) for values in product(*(letters[digit] for digit in digits))]

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        digits = case["input"]["digits"]
        expected = oracle(digits)
        assert sorted(case["expected"]) == sorted(expected)

    checked = 0
    for length in range(1, 5):
        for digit_tuple in product(letters, repeat=length):
            digits = "".join(digit_tuple)
            expected = oracle(digits)
            assert letter_combinations(digits) == expected
            assert native_letter_combinations(digits) == expected
            checked += 1
    assert checked == 4_680


def test_remove_nth_node_optimality_matches_every_legal_position() -> None:
    remove_nth = _reference_solve("19")
    package = leetcode_package_dir("lc_19")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_remove_nth = native_namespace["Solution"]().removeNthFromEnd

    checked = 0
    for length in range(1, 31):
        values = list(range(length))
        for n in range(1, length + 1):
            expected = values[: length - n] + values[length - n + 1 :]
            head = _list_node_from_values(values)
            native_head = _list_node_from_values(values)
            assert _list_node_to_values(remove_nth(head, n)) == expected
            assert _list_node_to_values(native_remove_nth(native_head, n)) == expected
            checked += 1
    assert checked == 465


def test_merge_two_sorted_lists_optimality_matches_sorted_concatenation() -> None:
    merge_lists = _reference_solve("21")
    package = leetcode_package_dir("lc_21")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_merge_lists = native_namespace["Solution"]().mergeTwoLists

    def assert_merge(left: list[int], right: list[int]) -> None:
        expected = sorted(left + right)
        app_result = merge_lists(_list_node_from_values(left), _list_node_from_values(right))
        native_result = native_merge_lists(
            _list_node_from_values(left),
            _list_node_from_values(right),
        )
        assert _list_node_to_values(app_result) == expected
        assert _list_node_to_values(native_result) == expected

    small_lists = [
        list(values)
        for length in range(5)
        for values in combinations_with_replacement(range(-2, 3), length)
    ]
    checked = 0
    for left in small_lists:
        for right in small_lists:
            assert_merge(left, right)
            checked += 1
    assert checked == 15_876

    boundary_values = list(range(-100, -50))
    for left_length in range(51):
        if left_length:
            left_positions = {
                position * len(boundary_values) // left_length
                for position in range(left_length)
            }
        else:
            left_positions = set()
        left = [value for i, value in enumerate(boundary_values) if i in left_positions]
        right = [value for i, value in enumerate(boundary_values) if i not in left_positions]
        assert len(left) == left_length
        assert_merge(left, right)


def test_swap_pairs_optimality_preserves_node_identity_at_every_legal_length() -> None:
    swap_pairs = _reference_solve("24")
    package = leetcode_package_dir("lc_24")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_swap_pairs = native_namespace["Solution"]().swapPairs

    def nodes_from(head: object) -> list[object]:
        nodes: list[object] = []
        while head is not None:
            nodes.append(head)
            head = head.next
        return nodes

    for length in range(101):
        values = list(range(length))
        for swap in (swap_pairs, native_swap_pairs):
            head = _list_node_from_values(values)
            original_nodes = nodes_from(head)
            expected_nodes: list[object] = []
            for i in range(0, length - 1, 2):
                expected_nodes.extend((original_nodes[i + 1], original_nodes[i]))
            if length % 2:
                expected_nodes.append(original_nodes[-1])

            result_nodes = nodes_from(swap(head))
            assert result_nodes == expected_nodes
            assert [node.val for node in original_nodes] == values


def test_remove_element_optimality_matches_filter_oracle_across_legal_shapes() -> None:
    remove_element = _reference_solve("27")
    package = leetcode_package_dir("lc_27")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_remove_element = native_namespace["Solution"]().removeElement

    def assert_filter(values: list[int], target: int) -> None:
        expected = [value for value in values if value != target]
        for remove in (remove_element, native_remove_element):
            nums = values.copy()
            retained = remove(nums, target)
            assert retained == len(expected)
            assert nums[:retained] == expected

    for length in range(7):
        for values in product(range(3), repeat=length):
            for target in range(4):
                assert_filter(list(values), target)

    for length in range(101):
        values = [(i * 17 + length) % 51 for i in range(length)]
        for target in (0, 25, 50, 51, 100):
            assert_filter(values, target)


def test_divide_two_integers_bounded_domain_matches_arithmetic_oracle() -> None:
    divide = _reference_solve("29")
    package = leetcode_package_dir("lc_29")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_divide = native_namespace["Solution"]().divide

    minimum = -(2**31)
    maximum = 2**31 - 1

    def oracle(dividend: int, divisor: int) -> int:
        quotient = abs(dividend) // abs(divisor)
        if (dividend < 0) != (divisor < 0):
            quotient = -quotient
        return min(maximum, max(minimum, quotient))

    def assert_quotient(dividend: int, divisor: int) -> None:
        expected = oracle(dividend, divisor)
        assert divide(dividend, divisor) == expected
        assert native_divide(dividend, divisor) == expected

    for dividend in range(-256, 257):
        for divisor in range(-64, 65):
            if divisor:
                assert_quotient(dividend, divisor)

    boundary_dividends = (
        minimum,
        minimum + 1,
        -(2**30),
        -1,
        0,
        1,
        2**30,
        maximum - 1,
        maximum,
        2,
        -2,
    )
    boundary_divisors = (
        minimum,
        minimum + 1,
        -(2**30),
        -3,
        -2,
        -1,
        1,
        2,
        3,
        2**30,
        maximum - 1,
        maximum,
    )
    for dividend in boundary_dividends:
        for divisor in boundary_divisors:
            assert_quotient(dividend, divisor)

    rng = random.Random(29)
    for _ in range(20_000):
        dividend = rng.randint(minimum, maximum)
        divisor = 0
        while divisor == 0:
            divisor = rng.randint(minimum, maximum)
        assert_quotient(dividend, divisor)


def test_next_permutation_optimality_traverses_complete_small_cycles() -> None:
    next_permutation = _reference_solve("31")
    package = leetcode_package_dir("lc_31")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_next_permutation = native_namespace["Solution"]().nextPermutation

    checked = 0
    for length in range(1, 9):
        for multiset in combinations_with_replacement(range(4), length):
            ordered = sorted(set(permutations(multiset)))
            for i, values in enumerate(ordered):
                expected = list(ordered[(i + 1) % len(ordered)])
                for advance in (next_permutation, native_next_permutation):
                    nums = list(values)
                    assert advance(nums) is None
                    assert nums == expected
                checked += 1

    assert checked == 87_380

    for length in range(1, 101):
        ascending = list(range(1, length + 1))
        expected_ascending = ascending[:-2] + ascending[-2:][::-1]
        descending = ascending[::-1]
        for advance in (next_permutation, native_next_permutation):
            nums = ascending.copy()
            assert advance(nums) is None
            assert nums == expected_ascending

            nums = descending.copy()
            assert advance(nums) is None
            assert nums == ascending


def test_valid_sudoku_bounded_domain_classifies_every_equal_digit_pair() -> None:
    is_valid = _reference_solve("36")
    package = leetcode_package_dir("lc_36")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_is_valid = native_namespace["Solution"]().isValidSudoku

    def empty_board() -> list[list[str]]:
        return [["."] * 9 for _ in range(9)]

    checked = 0
    for first, second in combinations(range(81), 2):
        first_row, first_column = divmod(first, 9)
        second_row, second_column = divmod(second, 9)
        board = empty_board()
        board[first_row][first_column] = "1"
        board[second_row][second_column] = "1"
        expected = not (
            first_row == second_row
            or first_column == second_column
            or (first_row // 3, first_column // 3)
            == (second_row // 3, second_column // 3)
        )
        assert is_valid(board) is expected
        assert native_is_valid(board) is expected
        checked += 1

    assert checked == 3_240

    complete = [
        list("534678912"),
        list("672195348"),
        list("198342567"),
        list("859761423"),
        list("426853791"),
        list("713924856"),
        list("961537284"),
        list("287419635"),
        list("345286179"),
    ]
    assert is_valid(empty_board())
    assert native_is_valid(empty_board())
    assert is_valid(complete)
    assert native_is_valid(complete)


def test_sudoku_solver_bounded_domain_solves_near_complete_and_authored_boards() -> None:
    solve_sudoku = _reference_solve("37")
    package = leetcode_package_dir("lc_37")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_solve_sudoku = native_namespace["Solution"]().solveSudoku

    complete = [
        list("534678912"),
        list("672195348"),
        list("198342567"),
        list("859761423"),
        list("426853791"),
        list("713924856"),
        list("961537284"),
        list("287419635"),
        list("345286179"),
    ]

    def assert_solution(board: list[list[str]], expected: list[list[str]]) -> None:
        clues = [row.copy() for row in board]
        for solve in (solve_sudoku, native_solve_sudoku):
            working = [row.copy() for row in board]
            assert solve(working) is None
            assert working == expected
            assert all(
                clue == "." or working[row][column] == clue
                for row in range(9)
                for column, clue in enumerate(clues[row])
            )

    removed_groups = {(position,) for position in range(81)}
    for position in range(81):
        row, column = divmod(position, 9)
        same_row = row * 9 + (column + 1) % 9
        same_column = ((row + 1) % 9) * 9 + column
        box_row = (row // 3) * 3 + (row + 1) % 3
        box_column = (column // 3) * 3 + (column + 1) % 3
        same_box = box_row * 9 + box_column
        removed_groups.add(tuple(sorted((position, same_row))))
        removed_groups.add(tuple(sorted((position, same_column))))
        removed_groups.add(tuple(sorted((position, same_box))))

    for removed in sorted(removed_groups):
        board = [row.copy() for row in complete]
        for position in removed:
            row, column = divmod(position, 9)
            board[row][column] = "."
        assert_solution(board, complete)
    assert len(removed_groups) == 324

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        assert_solution(case["input"]["board"], case["expected"])


def test_count_and_say_bounded_domain_matches_grouping_oracle() -> None:
    count_and_say = _reference_solve("38")
    package = leetcode_package_dir("lc_38")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_count_and_say = native_namespace["Solution"]().countAndSay

    def describe(term: str) -> str:
        return "".join(
            f"{sum(1 for _ in run)}{digit}" for digit, run in groupby(term)
        )

    expected = "1"
    previous_length = 0
    for n in range(1, 31):
        assert len(expected) >= previous_length
        assert count_and_say(n) == expected
        assert native_count_and_say(n) == expected
        previous_length = len(expected)
        expected = describe(expected)


def test_internal_angles_bounded_domain_matches_heron_oracle() -> None:
    internal_angles = _reference_solve("3899")
    package = leetcode_package_dir("lc_3899")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_internal_angles = native_namespace["Solution"]().internalAngles

    def oracle(sides: list[int] | tuple[int, int, int]) -> list[float]:
        a, b, c = sorted(sides)
        if a + b <= c:
            return []
        four_area = math.sqrt(
            (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)
        )
        return sorted(
            math.degrees(math.atan2(four_area, y * y + z * z - x * x))
            for x, y, z in ((a, b, c), (b, a, c), (c, a, b))
        )

    def assert_matches(actual: list[float], expected: list[float]) -> None:
        assert len(actual) == len(expected)
        assert actual == sorted(actual)
        for actual_angle, expected_angle in zip(actual, expected, strict=True):
            assert math.isclose(actual_angle, expected_angle, abs_tol=1e-9)

    checked = 0
    for sides in combinations_with_replacement(range(1, 41), 3):
        expected = oracle(sides)
        for arrangement in set(permutations(sides)):
            values = list(arrangement)
            assert_matches(internal_angles(values), expected)
            assert_matches(native_internal_angles(values), expected)
            checked += 1
    assert checked == 64_000

    rng = random.Random(3899)
    for _ in range(10_000):
        sides = [rng.randint(1, 1000) for _ in range(3)]
        expected = oracle(sides)
        assert_matches(internal_angles(sides), expected)
        assert_matches(native_internal_angles(sides), expected)

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        sides = case["input"]["sides"]
        expected = oracle(sides)
        assert_matches(case["expected"], expected)
        assert_matches(internal_angles(sides), expected)
        assert_matches(native_internal_angles(sides), expected)

    boundary_families = [
        [1, 1, 1],
        [1, 1, 2],
        [1, 999, 1000],
        [1, 1000, 1000],
        [999, 999, 1000],
        [1000, 1000, 1000],
    ]
    for sides in boundary_families:
        expected = oracle(sides)
        for arrangement in set(permutations(sides)):
            values = list(arrangement)
            assert_matches(internal_angles(values), expected)
            assert_matches(native_internal_angles(values), expected)


def test_valid_digit_bounded_domain_matches_complete_string_oracle() -> None:
    valid_digit = _reference_solve("3908")
    package = leetcode_package_dir("lc_3908")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_valid_digit = native_namespace["Solution"]().validDigit

    def oracle(n: int, x: int) -> bool:
        digits = str(n)
        target = str(x)
        return target in digits and digits[0] != target

    checked = 0
    for n in range(100_001):
        for x in range(10):
            expected = oracle(n, x)
            assert valid_digit(n, x) == expected
            assert native_valid_digit(n, x) == expected
            checked += 1
    assert checked == 1_000_010

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        n = case["input"]["n"]
        x = case["input"]["x"]
        expected = oracle(n, x)
        assert case["expected"] == expected
        assert valid_digit(n, x) == expected
        assert native_valid_digit(n, x) == expected


def test_find_degrees_optimality_matches_upper_triangle_oracle() -> None:
    find_degrees = _reference_solve("3898")
    package = leetcode_package_dir("lc_3898")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_find_degrees = native_namespace["Solution"]().findDegrees

    def oracle(matrix: list[list[int]]) -> list[int]:
        degree = [0] * len(matrix)
        for left in range(len(matrix)):
            for right in range(left + 1, len(matrix)):
                if matrix[left][right]:
                    degree[left] += 1
                    degree[right] += 1
        return degree

    checked = 0
    for size in range(1, 7):
        edges = list(combinations(range(size), 2))
        for mask in range(1 << len(edges)):
            matrix = [[0] * size for _ in range(size)]
            for bit, (left, right) in enumerate(edges):
                if mask >> bit & 1:
                    matrix[left][right] = 1
                    matrix[right][left] = 1
            expected = oracle(matrix)
            assert find_degrees(matrix) == expected
            assert native_find_degrees(matrix) == expected
            checked += 1
    assert checked == 33_867

    rng = random.Random(3898)
    for _ in range(10_000):
        size = rng.randint(1, 100)
        matrix = [[0] * size for _ in range(size)]
        for left in range(size):
            for right in range(left + 1, size):
                matrix[left][right] = matrix[right][left] = rng.randrange(2)
        expected = oracle(matrix)
        assert find_degrees(matrix) == expected
        assert native_find_degrees(matrix) == expected

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        matrix = case["input"]["matrix"]
        expected = oracle(matrix)
        assert expected == case["expected"]
        assert find_degrees(matrix) == expected
        assert native_find_degrees(matrix) == expected

    maximum_families = [
        [[0] * 100 for _ in range(100)],
        [[int(row != column) for column in range(100)] for row in range(100)],
        [[int(abs(row - column) == 1) for column in range(100)] for row in range(100)],
        [
            [int(row != column and (row == 0 or column == 0)) for column in range(100)]
            for row in range(100)
        ],
    ]
    for matrix in maximum_families:
        expected = oracle(matrix)
        assert find_degrees(matrix) == expected
        assert native_find_degrees(matrix) == expected


def test_count_digit_appearances_optimality_matches_decimal_oracle() -> None:
    count_digit_appearances = _reference_solve("3895")
    package = leetcode_package_dir("lc_3895")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_count = native_namespace["Solution"]().countDigitOccurrences

    def oracle(nums: list[int], digit: int) -> int:
        target = str(digit)
        return sum(str(value).count(target) for value in nums)

    checked = 0
    for value in range(1, 100_001):
        representation = str(value)
        for digit in range(10):
            expected = representation.count(str(digit))
            assert count_digit_appearances([value], digit) == expected
            assert native_count([value], digit) == expected
            checked += 1
    assert checked == 1_000_000

    rng = random.Random(3895)
    for _ in range(20_000):
        nums = [rng.randint(1, 10**6) for _ in range(rng.randint(1, 50))]
        digit = rng.randint(0, 9)
        expected = oracle(nums, digit)
        assert count_digit_appearances(nums, digit) == expected
        assert native_count(nums, digit) == expected

    maximum_values = [10**6] * 1000
    for digit in range(10):
        expected = oracle(maximum_values, digit)
        assert count_digit_appearances(maximum_values, digit) == expected
        assert native_count(maximum_values, digit) == expected


def test_traffic_signal_color_bounded_domain_covers_every_legal_timer() -> None:
    traffic_signal = _reference_solve("3894")
    package = leetcode_package_dir("lc_3894")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_traffic_signal = native_namespace["Solution"]().trafficSignal

    def oracle(timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 31 <= timer <= 90:
            return "Red"
        return "Invalid"

    result_counts = {"Green": 0, "Orange": 0, "Red": 0, "Invalid": 0}
    for timer in range(1001):
        expected = oracle(timer)
        assert traffic_signal(timer) == expected
        assert native_traffic_signal(timer) == expected
        result_counts[expected] += 1

    assert result_counts == {
        "Green": 1,
        "Orange": 1,
        "Red": 60,
        "Invalid": 939,
    }


def test_toggle_light_bulbs_bounded_domain_matches_parity_oracle() -> None:
    toggle_light_bulbs = _reference_solve("3842")

    def oracle(bulbs: list[int]) -> list[int]:
        counts = [0] * 101
        for bulb in bulbs:
            counts[bulb] += 1
        return [bulb for bulb in range(1, 101) if counts[bulb] % 2]

    checked = 0
    for length in range(1, 9):
        for values in product(range(1, 6), repeat=length):
            bulbs = list(values)
            assert toggle_light_bulbs(bulbs) == oracle(bulbs)
            checked += 1
    assert checked == 488_280

    rng = random.Random(3842)
    for length in range(1, 101):
        for _ in range(20):
            bulbs = [rng.randint(1, 100) for _ in range(length)]
            assert toggle_light_bulbs(bulbs) == oracle(bulbs)

    for bulbs in (
        [1],
        [100],
        [1, 100, 1, 99, 100, 50],
        list(range(1, 101)),
        [bulb for bulb in range(1, 51) for _ in range(2)],
    ):
        assert toggle_light_bulbs(bulbs) == oracle(bulbs)


def test_vowel_consonant_score_bounded_domain_matches_ascii_oracle() -> None:
    vowel_consonant_score = _reference_solve("3813")
    vowels = frozenset("aeiou")

    def oracle(text: str) -> int:
        vowel_count = sum(char in vowels for char in text)
        consonant_count = sum(
            "a" <= char <= "z" and char not in vowels for char in text
        )
        return vowel_count // consonant_count if consonant_count else 0

    checked = 0
    for length in range(1, 7):
        for characters in product("ab u1", repeat=length):
            text = "".join(characters)
            assert vowel_consonant_score(text) == oracle(text)
            checked += 1
    assert checked == 19_530

    rng = random.Random(3813)
    alphabet = "abcdefghijklmnopqrstuvwxyz 0123456789"
    for length in range(1, 101):
        for _ in range(50):
            text = "".join(rng.choice(alphabet) for _ in range(length))
            assert vowel_consonant_score(text) == oracle(text)

    for text in (
        "a" * 100,
        "b" * 100,
        " " * 100,
        "0" * 100,
        "aeiou" * 20,
        "abcdefghijklmnopqrstuvwxyz" * 3 + "abcdefghijklmnopqrstuv",
    ):
        assert len(text) == 100
        assert vowel_consonant_score(text) == oracle(text)


def test_nth_smallest_one_bits_certificate_matches_rank_oracle() -> None:
    nth_smallest = _reference_solve("3821")

    values_by_ones = {
        one_count: [
            value
            for value in range(1, 1 << 12)
            if value.bit_count() == one_count
        ]
        for one_count in range(1, 13)
    }
    checked = 0
    for one_count, values in values_by_ones.items():
        for rank, expected in enumerate(values, 1):
            assert nth_smallest(rank, one_count) == expected
            checked += 1
    assert checked == (1 << 12) - 1

    def rank_of(value: int, one_count: int) -> int:
        rank = 1
        remaining = one_count
        for position in range(49, -1, -1):
            if value & (1 << position):
                if remaining <= position:
                    rank += math.comb(position, remaining)
                remaining -= 1
        return rank

    checked_boundaries = 0
    for one_count in range(1, 51):
        total = math.comb(50, one_count)
        ranks = {
            1,
            total,
            (total + 1) // 2,
            max(1, total // 3),
            max(1, (2 * total) // 3),
        }
        for rank in ranks:
            value = nth_smallest(rank, one_count)
            assert 0 < value < 1 << 50
            assert value.bit_count() == one_count
            assert rank_of(value, one_count) == rank
            checked_boundaries += 1
    assert checked_boundaries == 246


def test_smallest_absent_bounded_domain_matches_exact_average_oracle() -> None:
    smallest_absent = _reference_solve("3678")

    def oracle(nums: list[int]) -> int:
        average = Fraction(sum(nums), len(nums))
        present = set(nums)
        candidate = 1
        while candidate <= average or candidate in present:
            candidate += 1
        return candidate

    checked = 0
    for length in range(1, 6):
        for values in product(range(-3, 5), repeat=length):
            nums = list(values)
            assert smallest_absent(nums) == oracle(nums)
            checked += 1
    assert checked == 37_448

    rng = random.Random(3678)
    for length in range(1, 101):
        for _ in range(50):
            nums = [rng.randint(-100, 100) for _ in range(length)]
            assert smallest_absent(nums) == oracle(nums)

    for nums in (
        [-100] * 100,
        [100] * 100,
        list(range(1, 101)),
        [-100, 100],
    ):
        assert smallest_absent(nums) == oracle(nums)


def test_earliest_task_bounded_domain_matches_completion_oracle() -> None:
    earliest_time = _reference_solve("3683")

    for start in range(1, 101):
        for duration in range(1, 101):
            assert earliest_time([[start, duration]]) == start + duration

    rng = random.Random(3683)
    for length in range(1, 101):
        for _ in range(50):
            tasks = [
                [rng.randint(1, 100), rng.randint(1, 100)]
                for _ in range(length)
            ]
            assert earliest_time(tasks) == min(start + duration for start, duration in tasks)

    for tasks in (
        [[1, 1]] * 100,
        [[100, 100]] * 100,
        [[100, 100]] * 99 + [[1, 1]],
    ):
        assert earliest_time(tasks) == min(start + duration for start, duration in tasks)


def test_max_k_distinct_bounded_domain_matches_repeated_maximum_oracle() -> None:
    max_k_distinct = _reference_solve("3684")

    def oracle(nums: list[int], k: int) -> list[int]:
        remaining = set(nums)
        chosen = []
        for _ in range(min(k, len(remaining))):
            value = max(remaining)
            remaining.remove(value)
            chosen.append(value)
        return chosen

    checked = 0
    for length in range(1, 7):
        for values in product(range(1, 6), repeat=length):
            nums = list(values)
            for k in range(1, length + 1):
                assert max_k_distinct(nums, k) == oracle(nums, k)
                checked += 1
    assert checked == 112_305

    rng = random.Random(3684)
    for length in range(1, 101):
        for _ in range(50):
            nums = [rng.randint(1, 1_000_000_000) for _ in range(length)]
            k = rng.randint(1, length)
            assert max_k_distinct(nums, k) == oracle(nums, k)

    for nums, k in (
        ([1] * 100, 100),
        (list(range(1, 101)), 100),
        ([1_000_000_000, 1, 1_000_000_000], 2),
    ):
        assert max_k_distinct(nums, k) == oracle(nums, k)


def test_split_merge_bounded_domain_matches_shortest_path_oracle() -> None:
    from collections import deque

    min_split_merge = _reference_solve("3690")

    def oracle_distances(start: tuple[int, ...]) -> dict[tuple[int, ...], int]:
        distances = {start: 0}
        queue = deque([start])
        while queue:
            state = queue.popleft()
            distance = distances[state]
            length = len(state)
            for first in range(length):
                for last in range(first, length):
                    block = list(state[first : last + 1])
                    remainder = list(state[:first] + state[last + 1 :])
                    for gap in range(len(remainder) + 1):
                        candidate = tuple(remainder[:gap] + block + remainder[gap:])
                        if candidate not in distances:
                            distances[candidate] = distance + 1
                            queue.append(candidate)
        return distances

    distinct_checked = 0
    for length in range(2, 7):
        start = tuple(range(length))
        expected = oracle_distances(start)
        assert len(expected) == math.factorial(length)
        for target in permutations(range(length)):
            assert min_split_merge(list(start), list(target)) == expected[target]
            distinct_checked += 1
    assert distinct_checked == 872

    duplicate_checked = 0
    for length in range(2, 7):
        for ones in range(length + 1):
            states = []
            for one_positions in combinations(range(length), ones):
                positions = set(one_positions)
                states.append(tuple(1 if index in positions else 0 for index in range(length)))
            for start in states:
                expected = oracle_distances(start)
                assert len(expected) == len(states)
                for target in states:
                    assert min_split_merge(list(start), list(target)) == expected[target]
                    duplicate_checked += 1
    assert duplicate_checked == 1_272


def test_decimal_representation_bounded_domain_matches_place_value_oracle() -> None:
    decimal_representation = _reference_solve("3697")

    def oracle(value: int) -> list[int]:
        digits = str(value)
        return [
            int(digit) * 10 ** (len(digits) - index - 1)
            for index, digit in enumerate(digits)
            if digit != "0"
        ]

    for value in range(1, 100_001):
        assert decimal_representation(value) == oracle(value)

    rng = random.Random(3697)
    for _ in range(10_000):
        value = rng.randint(1, 1_000_000_000)
        assert decimal_representation(value) == oracle(value)

    for value in (101_010_101, 900_000_009, 999_999_999, 1_000_000_000):
        assert decimal_representation(value) == oracle(value)


def test_remove_zeros_bounded_domain_matches_arithmetic_oracle() -> None:
    remove_zeros = _reference_solve("3726")

    def arithmetic_oracle(value: int) -> int:
        reversed_kept_digits = []
        while value:
            digit = value % 10
            if digit != 0:
                reversed_kept_digits.append(digit)
            value //= 10

        result = 0
        for digit in reversed(reversed_kept_digits):
            result = result * 10 + digit
        return result

    for value in range(1, 1_000_001):
        assert remove_zeros(value) == arithmetic_oracle(value)

    values = {10**15, 101_010_101_010_101, 999_999_999_999_999}
    for power in range(1, 16):
        boundary = 10**power
        values.update({boundary - 1, boundary, boundary + 1})

    state = 3_726
    for _ in range(50_000):
        state = (6_364_136_223_846_793_005 * state + 1) % 10**15
        values.add(state or 1)

    for value in sorted(values):
        assert remove_zeros(value) == arithmetic_oracle(value)


def test_count_distinct_after_removing_zeros_matches_zero_free_oracle() -> None:
    count_distinct = _reference_solve("3747")

    zero_free_count = 0
    for value in range(1, 1_000_001):
        if "0" not in str(value):
            zero_free_count += 1
        assert count_distinct(value) == zero_free_count

    values = {1, 9, 10, 11, 99, 100, 101, 999_999_999_999_999, 10**15}
    for power in range(1, 16):
        boundary = 10**power
        values.update({boundary - 1, boundary, boundary + 1})

    state = 3_747
    for _ in range(10_000):
        state = (6_364_136_223_846_793_005 * state + 1) % 10**15
        values.add(state or 1)

    def prefix_oracle(bound: int) -> int:
        digits = tuple(map(int, str(bound)))

        @lru_cache(None)
        def count(position: int, tight: bool, started: bool) -> int:
            if position == len(digits):
                return int(started)
            limit = digits[position] if tight else 9
            total = 0
            for digit in range(limit + 1):
                next_tight = tight and digit == limit
                if not started and digit == 0:
                    total += count(position + 1, next_tight, False)
                elif digit != 0:
                    total += count(position + 1, next_tight, True)
            return total

        return count(0, True, False)

    for value in sorted(values):
        assert count_distinct(value) == prefix_oracle(value)


def test_reverse_binary_flips_matches_mirrored_bit_oracle() -> None:
    minimum_flips = _reference_solve("3750")

    def oracle(value: int) -> int:
        width = value.bit_length()
        return sum(
            2
            for offset in range(width // 2)
            if ((value >> offset) & 1) != ((value >> (width - 1 - offset)) & 1)
        )

    for value in range(1, 1_000_001):
        assert minimum_flips(value) == oracle(value)

    values = {1, 7, 10, 10**9}
    for width in range(1, 31):
        boundary = 1 << (width - 1)
        values.update({max(1, boundary - 1), boundary, min(10**9, boundary + 1)})

    state = 3_750
    for _ in range(10_000):
        state = (1_103_515_245 * state + 12_345) % 10**9
        values.add(state or 1)

    for value in sorted(values):
        assert minimum_flips(value) == oracle(value)


def test_total_waviness_digit_dp_matches_direct_prefix_oracle() -> None:
    total_waviness = _reference_solve("3753")

    def one(value: int) -> int:
        digits = list(map(int, str(value)))
        return sum(
            (digits[index] - digits[index - 1])
            * (digits[index] - digits[index + 1])
            > 0
            for index in range(1, len(digits) - 1)
        )

    prefix = [0]
    for value in range(1, 1_000_001):
        prefix.append(prefix[-1] + one(value))

    for upper in range(1, 1_000_001, 997):
        assert total_waviness(1, upper) == prefix[upper]

    rng = random.Random(3753)
    for _ in range(1_000):
        left = rng.randint(1, 1_000_000)
        right = rng.randint(left, 1_000_000)
        assert total_waviness(left, right) == prefix[right] - prefix[left - 1]

    for value in (10**12, 101_010_101_010_101, 999_999_999_999_999, 10**15):
        assert total_waviness(value, value) == one(value)


def test_sum_and_multiply_matches_arithmetic_digit_oracle() -> None:
    sum_and_multiply = _reference_solve("3754")

    def oracle(value: int) -> int:
        reversed_kept = []
        digit_sum = 0
        while value:
            digit = value % 10
            if digit:
                reversed_kept.append(digit)
                digit_sum += digit
            value //= 10

        concatenated = 0
        for digit in reversed(reversed_kept):
            concatenated = concatenated * 10 + digit
        return concatenated * digit_sum

    for value in range(0, 1_000_001):
        assert sum_and_multiply(value) == oracle(value)

    values = {0, 1, 10**9, 900_000_009, 999_999_999}
    state = 3_754
    for _ in range(10_000):
        state = (1_103_515_245 * state + 12_345) % (10**9 + 1)
        values.add(state)
    for value in sorted(values):
        assert sum_and_multiply(value) == oracle(value)


def test_find_missing_elements_bounded_domain_matches_range_oracle() -> None:
    find_missing = _reference_solve("3731")

    for mask in range(1 << 10):
        nums = [value + 1 for value in range(10) if mask & (1 << value)]
        if len(nums) < 2:
            continue
        expected = [
            value
            for value in range(min(nums), max(nums) + 1)
            if value not in nums
        ]
        assert find_missing(nums) == expected
        assert find_missing(list(reversed(nums))) == expected

    rng = random.Random(3731)
    for _ in range(10_000):
        length = rng.randint(2, 100)
        nums = rng.sample(range(1, 101), length)
        expected = [
            value
            for value in range(min(nums), max(nums) + 1)
            if value not in nums
        ]
        assert find_missing(nums) == expected


def test_delivery_closed_form_matches_scheduling_and_binary_oracles() -> None:
    minimum_time = _reference_solve("3733")

    def schedule_oracle(d: list[int], r: list[int]) -> int:
        states = {(0, 0)}
        for hour in range(1, 100):
            next_states = set(states)
            for first, second in states:
                if hour % r[0] and first < d[0]:
                    next_states.add((first + 1, second))
                if hour % r[1] and second < d[1]:
                    next_states.add((first, second + 1))
            states = next_states
            if tuple(d) in states:
                return hour
        raise AssertionError("small scheduling oracle exceeded its horizon")

    for first in range(1, 9):
        for second in range(1, 9):
            for first_interval in range(2, 9):
                for second_interval in range(2, 9):
                    d = [first, second]
                    r = [first_interval, second_interval]
                    assert minimum_time(d, r) == schedule_oracle(d, r)

    def binary_oracle(d: list[int], r: list[int]) -> int:
        period = r[0] // math.gcd(r[0], r[1]) * r[1]
        def feasible(hours: int) -> bool:
            return (
                hours - hours // r[0] >= d[0]
                and hours - hours // r[1] >= d[1]
                and hours - hours // period >= sum(d)
            )
        low, high = 0, 2 * sum(d) + 2
        while low + 1 < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle
        return high

    state = 3733
    for _ in range(100_000):
        state = (6_364_136_223_846_793_005 * state + 1) % 10**18
        first = state % 10**9 + 1
        state = (6_364_136_223_846_793_005 * state + 1) % 10**18
        second = state % 10**9 + 1
        state = (6_364_136_223_846_793_005 * state + 1) % 10**18
        first_interval = state % 29_999 + 2
        state = (6_364_136_223_846_793_005 * state + 1) % 10**18
        second_interval = state % 29_999 + 2
        d = [first, second]
        r = [first_interval, second_interval]
        assert minimum_time(d, r) == binary_oracle(d, r)


def test_no_zero_pairs_bounded_domain_matches_digit_and_enumeration_oracles() -> None:
    count_pairs = _reference_solve("3704")

    def direct(target: int) -> int:
        return sum(
            "0" not in str(left) and "0" not in str(target - left)
            for left in range(1, target)
        )

    for target in range(2, 5_001):
        assert count_pairs(target) == direct(target)

    def digit_oracle(target: int) -> int:
        digits = tuple(int(digit) for digit in reversed(str(target))) + (0,)

        @lru_cache(maxsize=None)
        def count(
            position: int,
            carry: int,
            left_active: bool,
            right_active: bool,
        ) -> int:
            if position == len(digits):
                return int(carry == 0 and not left_active and not right_active)

            if position == 0:
                left_choices = range(1, 10)
                right_choices = range(1, 10)
            else:
                left_choices = range(10) if left_active else (0,)
                right_choices = range(10) if right_active else (0,)

            ways = 0
            for left_digit in left_choices:
                for right_digit in right_choices:
                    column_sum = left_digit + right_digit + carry
                    if column_sum % 10 != digits[position]:
                        continue
                    ways += count(
                        position + 1,
                        column_sum // 10,
                        left_active and left_digit != 0,
                        right_active and right_digit != 0,
                    )
            return ways

        return count(0, 0, True, True)

    rng = random.Random(3704)
    targets = [rng.randint(2, 10**15) for _ in range(50)]
    targets.extend((101_010_101_010_101, 999_999_999_999_999, 10**15))
    for target in targets:
        assert count_pairs(target) == digit_oracle(target)


def test_permutations_iii_output_bound_through_maximum_n() -> None:
    permute = _reference_solve("3437")

    for n in range(1, 11):
        actual = permute(n)
        odd_count = (n + 1) // 2
        even_count = n // 2
        expected_count = math.factorial(odd_count) * math.factorial(even_count)
        if odd_count == even_count:
            expected_count *= 2

        assert len(actual) == expected_count
        assert actual == sorted(actual)
        assert len({tuple(values) for values in actual}) == expected_count
        for values in actual:
            assert sorted(values) == list(range(1, n + 1))
            assert all((left ^ right) & 1 for left, right in zip(values, values[1:]))


def test_apply_substitutions_matches_topological_oracle_on_legal_dags() -> None:
    apply_substitutions = _reference_solve("3481")

    def oracle(replacements: list[list[str]], text: str) -> str:
        raw = dict(replacements)
        expanded: dict[str, str] = {}

        def substitute_known(value: str) -> str:
            parts: list[str] = []
            position = 0
            while position < len(value):
                if value[position] != "%":
                    parts.append(value[position])
                    position += 1
                    continue
                closing = value.index("%", position + 1)
                parts.append(expanded[value[position + 1 : closing]])
                position = closing + 1
            return "".join(parts)

        while len(expanded) < len(raw):
            progress = False
            for key, value in raw.items():
                dependencies = value.split("%")[1::2]
                if key not in expanded and all(dep in expanded for dep in dependencies):
                    expanded[key] = substitute_known(value)
                    progress = True
            assert progress

        return substitute_known(text)

    alphabet = "ABCDEFGHIJ"
    checked = 0
    for key_count in range(1, 8):
        keys = list(alphabet[:key_count])
        parent_choices = [range(index + 1) for index in range(key_count)]
        for parents in product(*parent_choices):
            replacements = []
            for index, key in enumerate(keys):
                parent = parents[index]
                value = key.lower() if parent == 0 else f"%{keys[parent - 1]}%"
                replacements.append([key, value])
            replacements.reverse()
            ordered_keys = keys if checked % 2 == 0 else keys[::-1]
            text = "_".join(f"%{key}%" for key in ordered_keys)
            assert apply_substitutions(replacements, text) == oracle(replacements, text)
            checked += 1

    rng = random.Random(3481)
    for _ in range(5_000):
        key_count = rng.randint(1, 10)
        keys = list(alphabet[:key_count])
        replacements = []
        for index, key in enumerate(keys):
            dependencies = keys[:index]
            if not dependencies or rng.random() < 0.35:
                value = chr(ord("a") + rng.randrange(4))
            elif rng.random() < 0.5:
                dependency = rng.choice(dependencies)
                value = f"x%{dependency}%y"
            else:
                first = rng.choice(dependencies)
                second = rng.choice(dependencies)
                value = f"%{first}%%{second}%"
            replacements.append([key, value])
        rng.shuffle(replacements)
        rng.shuffle(keys)
        text = "_".join(f"%{key}%" for key in keys)
        assert apply_substitutions(replacements, text) == oracle(replacements, text)
        checked += 1

    doubling = [["A", "r"]]
    for index in range(1, 10):
        doubling.append([alphabet[index], f"%{alphabet[index - 1]}%%{alphabet[index - 1]}%"])
    maximum_text = "_".join(f"%{key}%" for key in reversed(alphabet))
    actual = apply_substitutions(doubling, maximum_text)
    assert actual == oracle(doubling, maximum_text)
    assert len(actual) == sum(1 << exponent for exponent in range(10)) + 9
    assert checked == 10913


def test_unique_three_digit_even_numbers_covers_every_legal_multiset() -> None:
    total_numbers = _reference_solve("3483")
    checked = 0

    for length in range(3, 11):
        for digits in combinations_with_replacement(range(10), length):
            frequency = [digits.count(value) for value in range(10)]
            expected = 0

            for units in range(0, 10, 2):
                if frequency[units] == 0:
                    continue
                frequency[units] -= 1

                for hundreds in range(1, 10):
                    if frequency[hundreds] == 0:
                        continue
                    frequency[hundreds] -= 1
                    expected += sum(count > 0 for count in frequency)
                    frequency[hundreds] += 1

                frequency[units] += 1

            assert total_numbers(list(digits)) == expected
            checked += 1

    assert checked == 184690


def test_latest_time_bounded_domain_matches_every_obtainable_pattern() -> None:
    find_latest_time = _reference_solve("3114")
    valid_times = [f"{hour:02d}:{minute:02d}" for hour in range(12) for minute in range(60)]
    patterns = set()

    for time in valid_times:
        for mask in range(1 << 4):
            chars = list(time)
            for bit, index in enumerate((0, 1, 3, 4)):
                if mask & (1 << bit):
                    chars[index] = "?"
            patterns.add("".join(chars))

    assert len(patterns) == 1925
    for pattern in patterns:
        expected = max(
            time
            for time in valid_times
            if all(source == "?" or source == digit for source, digit in zip(pattern, time))
        )
        assert find_latest_time(pattern) == expected


def test_make_square_bounded_domain_matches_all_legal_grids() -> None:
    can_make_square = _reference_solve("3127")

    checked = 0
    for cells in product("BW", repeat=9):
        grid = [list(cells[row * 3 : (row + 1) * 3]) for row in range(3)]
        expected = any(
            sum(
                grid[row + row_offset][column + column_offset] == "B"
                for row_offset in range(2)
                for column_offset in range(2)
            )
            != 2
            for row in range(2)
            for column in range(2)
        )
        assert can_make_square(grid) is expected
        checked += 1

    assert checked == 512


def test_valid_word_bounded_domain_matches_category_state_space() -> None:
    is_valid = _reference_solve("3136")
    vowels = set("aeiouAEIOU")
    letters = {
        chr(code)
        for start, end in ((ord("a"), ord("z")), (ord("A"), ord("Z")))
        for code in range(start, end + 1)
    }
    digits = {str(value) for value in range(10)}

    def oracle(word: str) -> bool:
        return (
            len(word) >= 3
            and all(character in letters or character in digits for character in word)
            and any(character in vowels for character in word)
            and any(character in letters - vowels for character in word)
        )

    checked = 0
    for length in range(1, 8):
        for characters in product("aB0@", repeat=length):
            word = "".join(characters)
            assert is_valid(word) is oracle(word)
            checked += 1

    assert checked == 21844

    source_alphabet = sorted(letters | digits | {"@", "#", "$"})
    for character in source_alphabet:
        for word in (
            character + "aB",
            "a" + character + "B",
            "aB" + character,
            character * 20,
        ):
            assert is_valid(word) is oracle(word)

    for word in (
        "aB" + "0" * 18,
        "aB" + "0" * 17 + "$",
        "A" * 19 + "z",
        "1" * 20,
    ):
        assert len(word) == 20
        assert is_valid(word) is oracle(word)


def test_minimum_average_bounded_domain_matches_direct_removal_oracle() -> None:
    minimum_average = _reference_solve("3194")

    def oracle(nums: list[int]) -> float:
        remaining = list(nums)
        answer = float("inf")
        while remaining:
            smallest = min(remaining)
            remaining.remove(smallest)
            largest = max(remaining)
            remaining.remove(largest)
            answer = min(answer, (smallest + largest) / 2)
        return answer

    checked = 0
    for length in (2, 4, 6):
        for values in product(range(1, 6), repeat=length):
            assert minimum_average(list(values)) == oracle(list(values))
            checked += 1

    assert checked == 16275

    rng = random.Random(3194)
    for length in range(2, 51, 2):
        for _ in range(40):
            nums = [rng.randint(1, 50) for _ in range(length)]
            assert minimum_average(nums) == oracle(nums)


def test_maximum_triangle_height_matches_every_legal_color_pair() -> None:
    maximum_height = _reference_solve("3200")

    def simulate(first: int, second: int) -> int:
        row = 1
        while True:
            if row % 2 == 1:
                if first < row:
                    return row - 1
                first -= row
            else:
                if second < row:
                    return row - 1
                second -= row
            row += 1

    checked = 0
    for red in range(1, 101):
        for blue in range(1, 101):
            expected = max(simulate(red, blue), simulate(blue, red))
            assert maximum_height(red, blue) == expected
            checked += 1

    assert checked == 10000


def test_coin_game_winner_matches_every_legal_coin_pair() -> None:
    winning_player = _reference_solve("3222")

    def simulate(x: int, y: int) -> str:
        turns = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            turns += 1
        return "Alice" if turns % 2 == 1 else "Bob"

    checked = 0
    for x in range(1, 101):
        for y in range(1, 101):
            assert winning_player(x, y) == simulate(x, y)
            checked += 1

    assert checked == 10000


def test_bit_changes_matches_reduced_domain_and_maximum_width_cases() -> None:
    min_changes = _reference_solve("3226")

    def oracle(n: int, k: int) -> int:
        changes = 0
        while n or k:
            n_bit = n & 1
            k_bit = k & 1
            if k_bit and not n_bit:
                return -1
            if n_bit and not k_bit:
                changes += 1
            n >>= 1
            k >>= 1
        return changes

    checked = 0
    for n in range(1, 1 << 10):
        for k in range(1, 1 << 10):
            assert min_changes(n, k) == oracle(n, k)
            checked += 1
    assert checked == 1023 * 1023

    boundary_cases = [
        (1, 1),
        (1_000_000, 1_000_000),
        (1_000_000, 524_288),
        (524_288, 1_000_000),
        (999_999, 1),
    ]
    rng = random.Random(3226)
    boundary_cases.extend(
        (rng.randint(1, 1_000_000), rng.randint(1, 1_000_000))
        for _ in range(2000)
    )
    for n, k in boundary_cases:
        assert min_changes(n, k) == oracle(n, k)


def test_digit_game_matches_partition_sums_across_legal_boundaries() -> None:
    can_alice_win = _reference_solve("3232")

    def oracle(nums: list[int]) -> bool:
        single_digit_sum = sum(value for value in nums if value < 10)
        double_digit_sum = sum(value for value in nums if value >= 10)
        return single_digit_sum != double_digit_sum

    checked = 0
    for value in range(1, 100):
        assert can_alice_win([value]) == oracle([value])
        checked += 1
    for first in range(1, 100):
        for second in range(1, 100):
            nums = [first, second]
            assert can_alice_win(nums) == oracle(nums)
            checked += 1

    representatives = (1, 9, 10, 99)
    for length in range(3, 5):
        for values in product(representatives, repeat=length):
            nums = list(values)
            assert can_alice_win(nums) == oracle(nums)
            checked += 1

    for length in range(1, 101):
        structured = [representatives[index % len(representatives)] for index in range(length)]
        assert can_alice_win(structured) == oracle(structured)
        checked += 1

    rng = random.Random(3232)
    for _ in range(2000):
        nums = [rng.randint(1, 99) for _ in range(rng.randint(1, 100))]
        assert can_alice_win(nums) == oracle(nums)
        checked += 1

    assert checked == 12320


def test_winning_players_match_grouped_counts_across_bounded_games() -> None:
    winning_player_count = _reference_solve("3238")

    def oracle(n: int, picks: list[list[int]]) -> int:
        frequencies: dict[tuple[int, int], int] = {}
        for player, color in picks:
            key = (player, color)
            frequencies[key] = frequencies.get(key, 0) + 1
        return sum(
            any(frequencies.get((player, color), 0) > player for color in range(11))
            for player in range(n)
        )

    checked = 0
    reduced_events = tuple(product(range(3), range(3)))
    for length in range(1, 5):
        for sequence in product(reduced_events, repeat=length):
            picks = [list(event) for event in sequence]
            assert winning_player_count(3, picks) == oracle(3, picks)
            checked += 1

    for player in range(10):
        for color in range(11):
            picks = [[player, color]]
            assert winning_player_count(10, picks) == oracle(10, picks)
            checked += 1

    for length in range(1, 101):
        picks = [[index % 10, (index // 10) % 11] for index in range(length)]
        assert winning_player_count(10, picks) == oracle(10, picks)
        checked += 1

    rng = random.Random(3238)
    for _ in range(2000):
        n = rng.randint(2, 10)
        picks = [
            [rng.randrange(n), rng.randint(0, 10)]
            for _ in range(rng.randint(1, 100))
        ]
        assert winning_player_count(n, picks) == oracle(n, picks)
        checked += 1

    assert checked == 9590


def test_neighbor_sum_matches_coordinate_oracle_across_bounded_grids() -> None:
    source_path = leetcode_solution_path("lc_3242", "python")
    assert source_path is not None
    neighbor_sum_class = _run_native_module(str(source_path))["NeighborSum"]

    adjacent_directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
    diagonal_directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))

    def oracle(grid: list[list[int]], value: int, directions: tuple[tuple[int, int], ...]) -> int:
        side = len(grid)
        row, column = next(
            (row, column)
            for row in range(side)
            for column in range(side)
            if grid[row][column] == value
        )
        return sum(
            grid[row + row_change][column + column_change]
            for row_change, column_change in directions
            if 0 <= row + row_change < side and 0 <= column + column_change < side
        )

    checked = 0
    for side in range(3, 11):
        value_count = side * side
        multipliers = [
            multiplier
            for multiplier in range(1, value_count)
            if math.gcd(multiplier, value_count) == 1
        ]
        offsets = (0, 1, value_count // 2, value_count - 1)
        for multiplier in multipliers:
            for offset in offsets:
                values = [
                    (multiplier * index + offset) % value_count
                    for index in range(value_count)
                ]
                grid = [
                    values[row * side : (row + 1) * side]
                    for row in range(side)
                ]
                service = neighbor_sum_class(grid)
                for value in range(value_count):
                    assert service.adjacentSum(value) == oracle(
                        grid, value, adjacent_directions
                    )
                    assert service.diagonalSum(value) == oracle(
                        grid, value, diagonal_directions
                    )
                    checked += 1

    rng = random.Random(3242)
    for _ in range(2000):
        side = rng.randint(3, 10)
        values = list(range(side * side))
        rng.shuffle(values)
        grid = [values[row * side : (row + 1) * side] for row in range(side)]
        service = neighbor_sum_class(grid)
        for value in range(side * side):
            assert service.adjacentSum(value) == oracle(grid, value, adjacent_directions)
            assert service.diagonalSum(value) == oracle(grid, value, diagonal_directions)
            checked += 1

    assert checked > 100_000


def test_snake_position_matches_coordinates_across_bounded_valid_paths() -> None:
    final_position = _reference_solve("3248")
    moves = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }

    checked = 0
    for side in range(2, 5):
        frontier = [(0, 0, [])]
        for _ in range(8):
            next_frontier = []
            for row, column, commands in frontier:
                for command, (row_change, column_change) in moves.items():
                    next_row = row + row_change
                    next_column = column + column_change
                    if not (0 <= next_row < side and 0 <= next_column < side):
                        continue
                    next_commands = commands + [command]
                    assert final_position(side, next_commands) == next_row * side + next_column
                    next_frontier.append((next_row, next_column, next_commands))
                    checked += 1
            frontier = next_frontier

    rng = random.Random(3248)
    for side in range(2, 11):
        for length in range(1, 101):
            row = column = 0
            commands = []
            for _ in range(length):
                legal = [
                    (command, row + row_change, column + column_change)
                    for command, (row_change, column_change) in moves.items()
                    if 0 <= row + row_change < side
                    and 0 <= column + column_change < side
                ]
                command, row, column = rng.choice(legal)
                commands.append(command)
            assert final_position(side, commands) == row * side + column
            checked += 1

    assert checked > 10_000


def test_largest_palindrome_matches_small_oracle_and_large_boundaries() -> None:
    largest_palindrome = _reference_solve("3260")

    for length in range(1, 6):
        half_length = (length + 1) // 2
        lower = 10 ** (half_length - 1)
        upper = 10**half_length
        for divisor in range(1, 10):
            expected = None
            for half_value in range(upper - 1, lower - 1, -1):
                left = str(half_value)
                candidate = left + left[: length // 2][::-1]
                if int(candidate) % divisor == 0:
                    expected = candidate
                    break
            assert expected is not None
            assert largest_palindrome(length, divisor) == expected

    def remainder(value: str, divisor: int) -> int:
        current = 0
        for digit in value:
            current = (current * 10 + int(digit)) % divisor
        return current

    for length in (6, 7, 20, 101, 1000):
        for divisor in range(1, 10):
            result = largest_palindrome(length, divisor)
            assert len(result) == length
            assert result[0] != "0"
            assert result == result[::-1]
            assert remainder(result, divisor) == 0

    maximum = largest_palindrome(100_000, 7)
    assert len(maximum) == 100_000
    assert maximum[0] != "0"
    assert maximum == maximum[::-1]
    assert remainder(maximum, 7) == 0


def test_number_key_matches_every_digit_triple_and_full_boundaries() -> None:
    generate_key = _reference_solve("3270")

    def oracle(num1: int, num2: int, num3: int) -> int:
        padded = (f"{num1:04d}", f"{num2:04d}", f"{num3:04d}")
        return int("".join(min(digits) for digits in zip(*padded)))

    checked = 0
    for place in (1, 10, 100, 1000):
        for digit1 in range(10):
            for digit2 in range(10):
                for digit3 in range(10):
                    base = 1111 - place
                    num1 = base + digit1 * place
                    num2 = base + digit2 * place
                    num3 = base + digit3 * place
                    assert generate_key(num1, num2, num3) == oracle(num1, num2, num3)
                    checked += 1

    boundaries = (1, 9, 10, 99, 100, 999, 1000, 9999)
    for num1, num2, num3 in product(boundaries, repeat=3):
        assert generate_key(num1, num2, num3) == oracle(num1, num2, num3)
        checked += 1

    rng = random.Random(3270)
    for _ in range(10_000):
        numbers = [rng.randint(1, 9999) for _ in range(3)]
        assert generate_key(*numbers) == oracle(*numbers)
        checked += 1

    assert checked == 14_512


def test_chessboard_colors_match_every_ordered_square_pair() -> None:
    same_color = _reference_solve("3274")
    files = "abcdefgh"
    ranks = "12345678"
    squares = [file + rank for file in files for rank in ranks]

    checked = 0
    for first in squares:
        for second in squares:
            first_is_even = (files.index(first[0]) + ranks.index(first[1])) % 2 == 0
            second_is_even = (
                files.index(second[0]) + ranks.index(second[1])
            ) % 2 == 0
            assert same_color(first, second) == (first_is_even == second_is_even)
            checked += 1

    assert checked == 4096


def test_binary_date_matches_every_valid_date_in_source_domain() -> None:
    convert_date = _reference_solve("3280")

    def binary(value: int) -> str:
        digits: list[str] = []
        while value:
            digits.append(str(value % 2))
            value //= 2
        return "".join(reversed(digits))

    current = date(1900, 1, 1)
    final = date(2100, 12, 31)
    checked = 0

    while current <= final:
        source = current.isoformat()
        expected = "-".join(
            (binary(current.year), binary(current.month), binary(current.day))
        )
        assert convert_date(source) == expected
        checked += 1
        current += timedelta(days=1)

    assert checked == 73_414


def test_stable_mountains_match_exhaustive_small_arrays_and_boundaries() -> None:
    stable_mountains = _reference_solve("3285")

    checked = 0
    for length in range(2, 7):
        for heights in product(range(1, 4), repeat=length):
            for threshold in range(1, 4):
                expected = [
                    index
                    for index in range(1, length)
                    if heights[index - 1] > threshold
                ]
                assert stable_mountains(list(heights), threshold) == expected
                checked += 1

    assert checked == 3267

    maximum = [100 if index % 2 == 0 else 1 for index in range(100)]
    assert stable_mountains(maximum, 50) == list(range(1, 100, 2))
    assert stable_mountains([100] * 100, 99) == list(range(1, 100))
    assert stable_mountains([100] * 100, 100) == []
    assert stable_mountains([1, 100], 1) == []


def test_balanced_string_matches_exhaustive_small_strings_and_boundaries() -> None:
    is_balanced = _reference_solve("3340")

    checked = 0
    for length in range(2, 7):
        for digits in product("0123", repeat=length):
            num = "".join(digits)
            expected = sum(map(int, num[::2])) == sum(map(int, num[1::2]))
            assert is_balanced(num) is expected
            checked += 1

    assert checked == 5456
    assert is_balanced("0" * 100) is True
    assert is_balanced("9" * 100) is True
    assert is_balanced("90" * 50) is False
    assert is_balanced("9" * 99) is False
    assert is_balanced("01" * 50) is False


def test_water_bottles_ii_bounded_domain_matches_every_legal_pair() -> None:
    max_bottles_drunk = _reference_solve("3100")

    for num_bottles in range(1, 101):
        for initial_exchange in range(1, 101):
            exchanges = 0
            while True:
                next_count = exchanges + 1
                cumulative_cost = (
                    next_count * (2 * initial_exchange + next_count - 3) // 2
                )
                if cumulative_cost > num_bottles - 1:
                    break
                exchanges = next_count

            assert max_bottles_drunk(num_bottles, initial_exchange) == (
                num_bottles + exchanges
            )


def test_harshad_number_bounded_domain_matches_every_legal_integer() -> None:
    digit_sum_if_harshad = _reference_solve("3099")

    for value in range(1, 101):
        digit_sum = sum(int(digit) for digit in str(value))
        expected = digit_sum if value % digit_sum == 0 else -1
        assert digit_sum_if_harshad(value) == expected


def test_triangle_type_certificate_matches_every_legal_array() -> None:
    triangle_type = _reference_solve("3024")

    for nums_tuple in product(range(1, 101), repeat=3):
        nums = list(nums_tuple)
        first, second, third = sorted(nums)
        if first + second <= third:
            expected = "none"
        elif first == third:
            expected = "equilateral"
        elif first == second or second == third:
            expected = "isosceles"
        else:
            expected = "scalene"
        assert triangle_type(nums) == expected


def test_count_pairs_bounded_domain_matches_pair_enumeration_oracle() -> None:
    count_pairs = _reference_solve("2824")

    def brute_force(nums: list[int], target: int) -> int:
        return sum(
            nums[left] + nums[right] < target
            for left in range(len(nums))
            for right in range(left + 1, len(nums))
        )

    for length in range(1, 7):
        for values in product(range(-2, 3), repeat=length):
            nums = list(values)
            for target in range(-3, 4):
                candidate = nums.copy()
                assert count_pairs(candidate, target) == brute_force(nums, target)

    boundaries = [
        [-50] * 50,
        [50] * 50,
        [-50, 50] * 25,
        list(range(-25, 25)),
    ]
    for nums in boundaries:
        for target in (-50, 0, 50):
            candidate = nums.copy()
            assert count_pairs(candidate, target) == brute_force(nums, target)


def test_distribute_candies_i_bounded_domain_matches_every_legal_pair() -> None:
    distribute_candies = _reference_solve("2928")

    def bounded_enumeration(n: int, limit: int) -> int:
        total = 0
        for first in range(limit + 1):
            for second in range(limit + 1):
                third = n - first - second
                total += 0 <= third <= limit
        return total

    for n in range(1, 51):
        for limit in range(1, 51):
            assert distribute_candies(n, limit) == bounded_enumeration(n, limit)


def test_maximum_strong_pair_xor_i_bounded_domain_matches_algebraic_oracle() -> None:
    maximum_strong_pair_xor = _reference_solve("2932")

    def algebraic_oracle(nums: tuple[int, ...]) -> int:
        best = 0
        for left, x in enumerate(nums):
            for y in nums[left:]:
                smaller, larger = sorted((x, y))
                if larger <= 2 * smaller:
                    best = max(best, x ^ y)
        return best

    for length in range(1, 6):
        for nums in product(range(1, 7), repeat=length):
            original = list(nums)
            assert maximum_strong_pair_xor(original) == algebraic_oracle(nums)
            assert original == list(nums)

    boundaries = [
        tuple([1] * 50),
        tuple([1, 2] * 25),
        tuple((index % 100) + 1 for index in range(50)),
        tuple(100 - (index % 17) for index in range(50)),
    ]
    for nums in boundaries:
        assert maximum_strong_pair_xor(list(nums)) == algebraic_oracle(nums)


def test_neighboring_xor_certificate_matches_exhaustive_reconstruction() -> None:
    does_valid_array_exist = _reference_solve("2683")

    def brute_force(derived: list[int]) -> bool:
        n = len(derived)
        for mask in range(1 << n):
            original = [(mask >> index) & 1 for index in range(n)]
            if all(
                derived[index] == (original[index] ^ original[(index + 1) % n])
                for index in range(n)
            ):
                return True
        return False

    for n in range(1, 9):
        for mask in range(1 << n):
            derived = [(mask >> index) & 1 for index in range(n)]
            assert does_valid_array_exist(derived) == brute_force(derived)


def test_infinite_method_object_certificate_covers_arbitrary_property_names() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript Proxy regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2690_infinite-method-object';
const { createInfiniteObject, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
const object = createInfiniteObject();
for (const testCase of cases) {
    const method = testCase.input.method;
    if (object[method]() !== method || solve(method) !== testCase.expected) {
        throw new Error(`${testCase.id}: property interception failed`);
    }
}
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_circular_game_certificate_covers_every_legal_pair() -> None:
    circular_game_losers = _reference_solve("2682")

    def oracle(n: int, k: int) -> list[int]:
        received: set[int] = set()
        current = 0
        turn = 1
        while current not in received:
            received.add(current)
            current = (current + turn * k) % n
            turn += 1
        return [friend for friend in range(1, n + 1) if friend - 1 not in received]

    for n in range(1, 51):
        for k in range(1, n + 1):
            assert circular_game_losers(n, k) == oracle(n, k)


def test_delayed_arrival_certificate_covers_every_legal_pair() -> None:
    find_arrival = _reference_solve("2651")

    for arrival_time in range(1, 24):
        for delayed_time in range(1, 25):
            expected = arrival_time + delayed_time
            while expected >= 24:
                expected -= 24
            assert find_arrival(arrival_time, delayed_time) == expected


def test_cancellable_function_scenarios_cover_async_control_contract() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript cancellation regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2650_design-cancellable-function';
const { solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
(async () => {
    for (const testCase of cases) {
        const actual = await solve(testCase.input.scenario, testCase.input.cancelledAt);
        if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
            throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
        }
    }
})().catch(error => { console.error(error); process.exitCode = 1; });
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_promise_all_settled_certificate_covers_parallel_settlement_contract() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript promise regression")

    script = r"""
const path = './dsa/leetcode/2795_parallel-execution-of-promises-for-individual-results-retrieval';
const { promiseAllSettled } = require(`${path}/variants/optimal/solution.js`);

(async () => {
    const started = [];
    const controls = [];
    const functions = [0, 1, 2].map((index) => () => new Promise((resolve, reject) => {
        started.push(index);
        controls[index] = { resolve, reject };
    }));

    const aggregate = promiseAllSettled(functions);
    if (JSON.stringify(started) !== '[0,1,2]') {
        throw new Error(`functions were not started eagerly: ${JSON.stringify(started)}`);
    }

    let completed = false;
    aggregate.then(() => { completed = true; });
    controls[2].resolve({ position: 'third' });
    controls[1].reject('second failed');
    await Promise.resolve();
    await Promise.resolve();
    if (completed) throw new Error('aggregate resolved before every promise settled');

    controls[0].resolve('first');
    const actual = await aggregate;
    const expected = [
        { status: 'fulfilled', value: 'first' },
        { status: 'rejected', reason: 'second failed' },
        { status: 'fulfilled', value: { position: 'third' } },
    ];
    if (JSON.stringify(actual) !== JSON.stringify(expected)) {
        throw new Error(`settlements lost input order: ${JSON.stringify(actual)}`);
    }

    const thrown = new Error('synchronous failure');
    const recovered = await promiseAllSettled([
        () => { throw thrown; },
        () => Promise.resolve(7),
    ]);
    if (recovered[0].status !== 'rejected' || recovered[0].reason !== thrown ||
        recovered[1].status !== 'fulfilled' || recovered[1].value !== 7) {
        throw new Error('synchronous invocation failure was not recorded');
    }
})().catch(error => { console.error(error); process.exitCode = 1; });
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_repeat_string_certificate_covers_binary_doubling_contract() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript string regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2796_repeat-string';
const nativeSource = fs.readFileSync(`${path}/variants/optimal/solutions/leetcode.js`, 'utf8');
if (/\.repeat\s*\(/.test(nativeSource)) {
    throw new Error('accepted source calls the prohibited built-in repeat method');
}

const originalRepeat = String.prototype.repeat;
String.prototype.repeat = function() { throw new Error('built-in repeat was called'); };
try {
    const { solve } = require(`${path}/variants/optimal/solution.js`);
    const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
    for (const testCase of cases) {
        const actual = solve(testCase.input.str, testCase.input.times);
        if (actual !== testCase.expected) {
            throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
        }
    }

    const maximumCount = 'xy'.replicate(100000);
    if (maximumCount.length !== 200000 ||
        maximumCount.slice(0, 6) !== 'xyxyxy' ||
        maximumCount.slice(-6) !== 'xyxyxy') {
        throw new Error('maximum repetition count lost content or length');
    }

    const maximumReceiver = Array(1001).join('q');
    const doubledReceiver = maximumReceiver.replicate(1024);
    if (doubledReceiver.length !== 1024000 ||
        doubledReceiver[0] !== 'q' || doubledReceiver[doubledReceiver.length - 1] !== 'q') {
        throw new Error('maximum receiver length failed power-of-two doubling');
    }
} finally {
    String.prototype.repeat = originalRepeat;
}
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_partial_function_certificate_covers_placeholder_merge_contract() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript partial-function regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2797_partial-function-with-placeholders';
const { partial, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
for (const testCase of cases) {
    const { behavior, args, restArgs, context } = testCase.input;
    const actual = solve(behavior, args, restArgs, context);
    if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
        throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
    }
}

const template = ['_', 2, '_'];
const wrapped = partial((...values) => values, template);
const first = wrapped(1, 3);
const second = wrapped(4, 5, 6);
if (JSON.stringify(first) !== '[1,2,3]' ||
    JSON.stringify(second) !== '[4,2,5,6]' ||
    JSON.stringify(template) !== '["_",2,"_"]') {
    throw new Error('wrapper reuse mutated or retained a merged invocation');
}

const receiverAware = partial(function(value) { return this.base + value; }, ['_']);
if (receiverAware.call({ base: 40 }, 2) !== 42) {
    throw new Error('dynamic receiver was not forwarded to the target');
}

    const maximumArgs = Array.from(
        { length: 50000 },
        (_, index) => index < 45000 ? '_' : 1,
    );
    const maximumRestArgs = Array(50000).fill(2);
    const boundary = solve('checksum', maximumArgs, maximumRestArgs, null);
    const expectedBoundary = { count: 55000, sum: 105000, first: 2, last: 2 };
if (JSON.stringify(boundary) !== JSON.stringify(expectedBoundary)) {
    throw new Error(`maximum array lengths failed: ${JSON.stringify(boundary)}`);
}
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_employee_target_certificate_matches_exhaustive_counting_oracle() -> None:
    count_employees = _reference_solve("2798")

    for length in range(1, 7):
        for hours in product(range(4), repeat=length):
            for target in range(5):
                expected = sum(worked >= target for worked in hours)
                assert count_employees(list(hours), target) == expected

    boundary_cases = [
        ([0], 0),
        ([0], 100_000),
        ([100_000], 100_000),
        ([0] * 50, 0),
        ([100_000] * 50, 100_000),
        ([0, 100_000] * 25, 100_000),
    ]
    for hours, target in boundary_cases:
        expected = sum(worked >= target for worked in hours)
        assert count_employees(hours, target) == expected


def test_shortest_containing_string_matches_exhaustive_generated_oracle() -> None:
    minimum_string = _reference_solve("2800")
    words = ["a", "b", "aa", "ab", "ba", "bb"]

    def oracle(required: tuple[str, str, str]) -> str:
        alphabet = sorted(set("".join(required)))
        for length in range(max(map(len, required)), sum(map(len, required)) + 1):
            for letters in product(alphabet, repeat=length):
                candidate = "".join(letters)
                if all(word in candidate for word in required):
                    return candidate
        raise AssertionError(required)

    for required in product(words, repeat=3):
        assert minimum_string(*required) == oracle(required)

    longest = "a" * 100
    result = minimum_string(longest, "a" * 99, "a" * 98)
    assert result == longest
    assert all(word in result for word in (longest, "a" * 99, "a" * 98))


def test_stepping_number_count_matches_enumeration_and_length_recurrence() -> None:
    count_stepping_numbers = _reference_solve("2801")
    modulus = 10**9 + 7

    def is_stepping(value: int) -> bool:
        digits = str(value)
        return all(
            abs(int(left) - int(right)) == 1
            for left, right in zip(digits, digits[1:])
        )

    prefix = [0]
    for value in range(1, 2001):
        prefix.append(prefix[-1] + int(is_stepping(value)))
        assert count_stepping_numbers("1", str(value)) == prefix[value]

    for low in range(1, 501, 17):
        for high in range(low, 2001, 37):
            assert count_stepping_numbers(str(low), str(high)) == (
                prefix[high] - prefix[low - 1]
            )

    endings = [0] + [1] * 9
    expected = sum(endings)
    for _length in range(2, 101):
        next_endings = [0] * 10
        for digit in range(10):
            if digit > 0:
                next_endings[digit] += endings[digit - 1]
            if digit < 9:
                next_endings[digit] += endings[digit + 1]
        endings = [count % modulus for count in next_endings]
        expected = (expected + sum(endings)) % modulus

    assert count_stepping_numbers("1", "9" * 100) == expected
    alternating = "10" * 50
    assert count_stepping_numbers(alternating, alternating) == 1
    nonstepping = "1" + "0" * 99
    assert count_stepping_numbers(nonstepping, nonstepping) == 0


def test_kth_lucky_number_matches_independent_level_order_enumeration() -> None:
    kth_lucky_number = _reference_solve("2802")
    expected: list[str] = []

    for length in range(1, 11):
        expected.extend("".join(digits) for digits in product("47", repeat=length))

    for k, lucky_number in enumerate(expected, start=1):
        assert kth_lucky_number(k) == lucky_number

    for length in range(1, 10):
        last_at_length = (1 << (length + 1)) - 2
        assert kth_lucky_number(last_at_length) == "7" * length
        assert kth_lucky_number(last_at_length + 1) == "4" * (length + 1)

    maximum = kth_lucky_number(10**9)
    assert maximum == "77477744774747744747444444447"
    assert len(maximum) == (10**9 + 1).bit_length() - 1
    assert set(maximum) == {"4", "7"}


def test_factorial_generator_cases_match_independent_recurrence() -> None:
    payload = json.loads(
        (leetcode_package_dir("lc_2803") / "cases.json").read_text(encoding="utf-8")
    )
    inputs = {case["input"]["n"] for case in payload["cases"]}
    assert {0, 1, 2, 18}.issubset(inputs)

    for case in payload["cases"]:
        n = case["input"]["n"]
        expected: list[int] = []
        product_value = 1
        for value in range(1, max(n, 1) + 1):
            product_value *= value
            expected.append(product_value)
        assert case["expected"] == expected

    maximum = next(
        case for case in payload["cases"] if case["input"]["n"] == 18
    )
    assert maximum["expected"][-1] == math.factorial(18)


def test_array_foreach_extension_matches_callback_contract() -> None:
    package = leetcode_package_dir("lc_2804")
    source_path = package / "variants" / "optimal" / "solutions" / "javascript.js"
    cases_path = package / "cases.json"
    node = shutil.which("node")
    assert node is not None

    script = r"""
const fs = require("fs");
const sourcePath = process.argv[1];
const casesPath = process.argv[2];
const { solve } = require(sourcePath);
const cases = JSON.parse(fs.readFileSync(casesPath, "utf8")).cases;
for (const testCase of cases) {
    const actual = solve(
        testCase.input.arr,
        testCase.input.callback,
        testCase.input.context,
    );
    if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
        throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
    }
}

const values = [10, 20, 30];
const context = { marker: "bound" };
const calls = [];
const returned = values.forEach(function(value, index, array) {
    calls.push([value, index, array === values, this === context]);
}, context);
if (returned !== undefined) throw new Error("forEach must return undefined");
if (JSON.stringify(calls) !== JSON.stringify([
    [10, 0, true, true],
    [20, 1, true, true],
    [30, 2, true, true],
])) throw new Error(`callback contract: ${JSON.stringify(calls)}`);

const boundary = Array.from({ length: 100000 }, (_, index) => index);
let count = 0;
boundary.forEach(function(value, index, array) {
    if (value !== index || array !== boundary) throw new Error("boundary arguments");
    count++;
}, context);
if (count !== 100000) throw new Error(`boundary count: ${count}`);
"""
    completed = subprocess.run(
        [node, "-e", script, str(source_path), str(cases_path)],
        cwd=package,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_custom_interval_matches_deterministic_scheduler_contract() -> None:
    package = leetcode_package_dir("lc_2805")
    source_path = package / "variants" / "optimal" / "solutions" / "javascript.js"
    cases_path = package / "cases.json"
    node = shutil.which("node")
    assert node is not None

    script = r"""
const fs = require("fs");
const sourcePath = process.argv[1];
const casesPath = process.argv[2];

let nextNativeId = 1;
const pending = new Map();
global.setTimeout = (callback, delay) => {
    const handle = { nativeId: nextNativeId++ };
    pending.set(handle, { callback, delay });
    return handle;
};
global.clearTimeout = (handle) => pending.delete(handle);

const { customInterval, customClearInterval, solve } = require(sourcePath);
const cases = JSON.parse(fs.readFileSync(casesPath, "utf8")).cases;
for (const testCase of cases) {
    const { delay, period, cancelTime } = testCase.input;
    const actual = solve(delay, period, cancelTime);
    if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
        throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
    }
}

const takeOnlyPending = () => {
    if (pending.size !== 1) throw new Error(`expected one timeout, got ${pending.size}`);
    const [handle, job] = pending.entries().next().value;
    pending.delete(handle);
    return job;
};

const calls = [];
const id = customInterval(() => calls.push(calls.length + 1), 50, 20);
if (!Number.isInteger(id)) throw new Error(`custom id is not numeric: ${id}`);
let job = takeOnlyPending();
if (job.delay !== 50) throw new Error(`first delay: ${job.delay}`);
job.callback();
job = takeOnlyPending();
if (job.delay !== 70) throw new Error(`second delay: ${job.delay}`);
job.callback();
job = takeOnlyPending();
if (job.delay !== 90) throw new Error(`third delay: ${job.delay}`);
customClearInterval(id);
if (pending.size !== 0) throw new Error("clear left a pending timeout");
if (JSON.stringify(calls) !== JSON.stringify([1, 2])) throw new Error("wrong calls");

const firstId = customInterval(() => {}, 20, 20);
const secondId = customInterval(() => {}, 20, 20);
if (!Number.isInteger(firstId) || !Number.isInteger(secondId) || firstId === secondId) {
    throw new Error("interval ids must be distinct numbers");
}
if (pending.size !== 2) throw new Error("independent intervals missing");
customClearInterval(firstId);
if (pending.size !== 1) throw new Error("clearing one interval affected another");
customClearInterval(secondId);

let selfId;
let selfCalls = 0;
selfId = customInterval(() => {
    selfCalls++;
    customClearInterval(selfId);
}, 30, 10);
job = takeOnlyPending();
job.callback();
if (selfCalls !== 1 || pending.size !== 0) {
    throw new Error("self-cancellation scheduled another timeout");
}

const maximum = solve(20, 20, 1000);
if (maximum.length !== 9 || maximum.at(-1) !== 900) {
    throw new Error(`maximum schedule: ${JSON.stringify(maximum)}`);
}
"""
    completed = subprocess.run(
        [node, "-e", script, str(source_path), str(cases_path)],
        cwd=package,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_delay_all_matches_deterministic_settlement_contract() -> None:
    package = leetcode_package_dir("lc_2821")
    source_path = package / "variants" / "optimal" / "solutions" / "javascript.js"
    cases_path = package / "cases.json"
    node = shutil.which("node")
    assert node is not None

    script = r"""
const fs = require("fs");
const sourcePath = process.argv[1];
const casesPath = process.argv[2];

const pending = [];
global.setTimeout = (callback, delay) => {
    const handle = { callback, delay };
    pending.push(handle);
    return handle;
};

const { delayAll, solve } = require(sourcePath);
const cases = JSON.parse(fs.readFileSync(casesPath, "utf8")).cases;

const flushMicrotasks = async () => {
    await Promise.resolve();
    await Promise.resolve();
};

const runPending = () => {
    while (pending.length > 0) pending.shift().callback();
};

(async () => {
    for (const testCase of cases) {
        const result = solve(testCase.input.tasks, testCase.input.ms);
        runPending();
        await flushMicrotasks();
        runPending();
        const actual = await result;
        if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
            throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
        }
    }

    const starts = [];
    const sources = [
        () => {
            starts.push("fulfilled");
            return Promise.resolve({ answer: 42 });
        },
        () => {
            starts.push("rejected");
            return Promise.reject("original reason");
        },
        () => {
            starts.push("second fulfillment");
            return Promise.resolve("last");
        },
    ];
    const delayed = delayAll(sources, 40);
    if (delayed.length !== sources.length || starts.length !== 0) {
        throw new Error("construction must preserve length without eager calls");
    }

    const outcomes = delayed.map((wrapper) =>
        wrapper().then(
            (value) => ({ status: "resolved", value }),
            (reason) => ({ status: "rejected", reason }),
        )
    );
    if (JSON.stringify(starts) !== JSON.stringify([
        "fulfilled",
        "rejected",
        "second fulfillment",
    ])) {
        throw new Error(`wrong invocation order: ${JSON.stringify(starts)}`);
    }

    await flushMicrotasks();
    if (pending.length !== 3 || pending.some((timer) => timer.delay !== 40)) {
        throw new Error(`wrong delayed timers: ${JSON.stringify(pending)}`);
    }
    runPending();
    const settled = await Promise.all(outcomes);
    const expected = [
        { status: "resolved", value: { answer: 42 } },
        { status: "rejected", reason: "original reason" },
        { status: "resolved", value: "last" },
    ];
    if (JSON.stringify(settled) !== JSON.stringify(expected)) {
        throw new Error(`outcomes changed: ${JSON.stringify(settled)}`);
    }

    let calls = 0;
    const [repeatable] = delayAll(
        [() => Promise.resolve(++calls)],
        500,
    );
    const repeated = [
        repeatable(),
        repeatable(),
    ];
    await flushMicrotasks();
    if (calls !== 2 || pending.length !== 2 ||
        pending.some((timer) => timer.delay !== 500)) {
        throw new Error("repeated calls did not create independent timers");
    }
    runPending();
    if (JSON.stringify(await Promise.all(repeated)) !== JSON.stringify([1, 2])) {
        throw new Error("repeated calls did not preserve independent values");
    }

    const maximumSources = Array.from(
        { length: 10 },
        (_, index) => () => Promise.resolve(index),
    );
    const maximumDelayed = delayAll(maximumSources, 10);
    const maximumResults = maximumDelayed.map((wrapper) => wrapper());
    await flushMicrotasks();
    if (pending.length !== 10 || pending.some((timer) => timer.delay !== 10)) {
        throw new Error("maximum legal array did not schedule ten timers");
    }
    runPending();
    if (JSON.stringify(await Promise.all(maximumResults)) !==
        JSON.stringify(Array.from({ length: 10 }, (_, index) => index))) {
        throw new Error("maximum legal array changed order");
    }
})().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
"""
    completed = subprocess.run(
        [node, "-e", script, str(source_path), str(cases_path)],
        cwd=package,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_invert_object_matches_independent_grouping_oracle() -> None:
    package = leetcode_package_dir("lc_2822")
    source_path = package / "variants" / "optimal" / "solutions" / "javascript.js"
    cases_path = package / "cases.json"
    benchmark_path = package / "benchmark.json"
    node = shutil.which("node")
    assert node is not None

    script = r"""
const fs = require("fs");
const sourcePath = process.argv[1];
const casesPath = process.argv[2];
const benchmarkPath = process.argv[3];
const { invertObject, solve } = require(sourcePath);

const hasOwn = (object, key) =>
    Object.prototype.hasOwnProperty.call(object, key);

const oracle = (obj) => {
    const groups = Object.create(null);
    for (const [key, value] of Object.entries(obj)) {
        if (!hasOwn(groups, value)) groups[value] = [];
        groups[value].push(key);
    }

    const result = Object.create(null);
    for (const value of Object.keys(groups)) {
        result[value] = groups[value].length === 1
            ? groups[value][0]
            : groups[value];
    }
    return result;
};

const canonical = (value) => {
    if (Array.isArray(value)) return ["array", value.map(canonical)];
    if (value !== null && typeof value === "object") {
        return [
            "object",
            Object.keys(value)
                .sort()
                .map((key) => [key, canonical(value[key])]),
        ];
    }
    return ["value", value];
};

const equal = (left, right) =>
    JSON.stringify(canonical(left)) === JSON.stringify(canonical(right));

for (const filename of [casesPath, benchmarkPath]) {
    const cases = JSON.parse(fs.readFileSync(filename, "utf8")).cases;
    for (const testCase of cases) {
        const expected = oracle(testCase.input.obj);
        if (!equal(testCase.expected, expected)) {
            throw new Error(`${testCase.id}: invalid expected output`);
        }
        if (!equal(invertObject(testCase.input.obj), expected)) {
            throw new Error(`${testCase.id}: invertObject mismatch`);
        }
        if (!equal(solve(testCase.input.obj), expected)) {
            throw new Error(`${testCase.id}: solve mismatch`);
        }
    }
}

const values = ["", "x", "0", "__proto__"];
for (let length = 0; length <= 7; length++) {
    const count = values.length ** length;
    for (let mask = 0; mask < count; mask++) {
        let encoded = mask;
        const array = [];
        for (let index = 0; index < length; index++) {
            array.push(values[encoded % values.length]);
            encoded = Math.floor(encoded / values.length);
        }
        if (!equal(invertObject(array), oracle(array))) {
            throw new Error(`array mismatch: ${JSON.stringify(array)}`);
        }
    }
}

const objectKeys = ["10", "2", "a", "constructor", "__proto__"];
const assignmentCount = values.length ** objectKeys.length;
for (let mask = 0; mask < assignmentCount; mask++) {
    let encoded = mask;
    const entries = [];
    for (const key of objectKeys) {
        entries.push([key, values[encoded % values.length]]);
        encoded = Math.floor(encoded / values.length);
    }
    const object = Object.fromEntries(entries);
    if (!equal(invertObject(object), oracle(object))) {
        throw new Error(`object mismatch: ${JSON.stringify(object)}`);
    }
}

const special = invertObject({
    first: "__proto__",
    second: "constructor",
    third: "toString",
    fourth: "__proto__",
});
if (!hasOwn(special, "__proto__") ||
    !equal(special.__proto__, ["first", "fourth"]) ||
    special.constructor !== "second" ||
    special.toString !== "third") {
    throw new Error("prototype-like values were not preserved as data");
}

const boundary = Object.fromEntries(
    Array.from(
        { length: 5000 },
        (_, index) => [`key-${index}`, `value-${index}`],
    ),
);
const boundaryResult = invertObject(boundary);
if (Object.keys(boundaryResult).length !== 5000 ||
    boundaryResult["value-0"] !== "key-0" ||
    boundaryResult["value-4999"] !== "key-4999") {
    throw new Error("boundary inversion failed");
}
"""
    completed = subprocess.run(
        [node, "-e", script, str(source_path), str(cases_path), str(benchmark_path)],
        cwd=package,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_deep_filter_matches_independent_bottom_up_pruning_oracle() -> None:
    package = leetcode_package_dir("lc_2823")
    source_path = package / "variants" / "optimal" / "solutions" / "javascript.js"
    cases_path = package / "cases.json"
    benchmark_path = package / "benchmark.json"
    node = shutil.which("node")
    assert node is not None

    script = r"""
const fs = require("fs");
const sourcePath = process.argv[1];
const casesPath = process.argv[2];
const benchmarkPath = process.argv[3];
const { deepFilter, predicates, solve } = require(sourcePath);

const define = (object, key, value) => {
    Object.defineProperty(object, key, {
        value,
        enumerable: true,
        writable: true,
        configurable: true,
    });
};

const oracle = (container, fn) => {
    const array = Array.isArray(container);
    const retained = array ? [] : {};

    for (const [key, child] of Object.entries(container)) {
        let filtered;
        if (child !== null && typeof child === "object") {
            filtered = oracle(child, fn);
            if (filtered === undefined) continue;
        } else {
            if (!fn(child)) continue;
            filtered = child;
        }

        if (array) retained.push(filtered);
        else define(retained, key, filtered);
    }

    return Object.keys(retained).length === 0 ? undefined : retained;
};

const canonical = (value) => {
    if (value === undefined) return ["undefined"];
    if (Array.isArray(value)) return ["array", value.map(canonical)];
    if (value !== null && typeof value === "object") {
        return [
            "object",
            Object.keys(value)
                .sort()
                .map((key) => [key, canonical(value[key])]),
        ];
    }
    return ["value", value];
};

const equal = (left, right) =>
    JSON.stringify(canonical(left)) === JSON.stringify(canonical(right));

const adapter = (value) =>
    value === undefined ? { defined: false } : { defined: true, value };

for (const filename of [casesPath, benchmarkPath]) {
    const cases = JSON.parse(fs.readFileSync(filename, "utf8")).cases;
    for (const testCase of cases) {
        const { obj, predicate } = testCase.input;
        const fn = predicates[predicate];
        const before = JSON.stringify(obj);
        const expected = oracle(obj, fn);
        if (!equal(testCase.expected, adapter(expected))) {
            throw new Error(`${testCase.id}: invalid expected output`);
        }
        if (!equal(deepFilter(obj, fn), expected)) {
            throw new Error(`${testCase.id}: deepFilter mismatch`);
        }
        if (!equal(solve(obj, predicate), adapter(expected))) {
            throw new Error(`${testCase.id}: solve mismatch`);
        }
        if (JSON.stringify(obj) !== before) {
            throw new Error(`${testCase.id}: input was mutated`);
        }
    }
}

const leaves = [null, 0, 1, -1, "", "x", false, true];
for (let length = 0; length <= 5; length++) {
    const count = leaves.length ** length;
    for (let mask = 0; mask < count; mask++) {
        let encoded = mask;
        const inner = [];
        for (let index = 0; index < length; index++) {
            inner.push(leaves[encoded % leaves.length]);
            encoded = Math.floor(encoded / leaves.length);
        }
        const structure = [inner, { branch: [...inner] }, ...inner];
        for (const fn of Object.values(predicates)) {
            if (!equal(deepFilter(structure, fn), oracle(structure, fn))) {
                throw new Error(`exhaustive mismatch: ${JSON.stringify(structure)}`);
            }
        }
    }
}

let predicateCalls = 0;
const primitiveOnly = deepFilter(
    { a: [1, { b: 2 }], c: { d: 3 }, e: null },
    (value) => {
        if (value !== null && typeof value === "object") {
            throw new Error("predicate received a container");
        }
        predicateCalls++;
        return true;
    },
);
if (predicateCalls !== 4 ||
    !equal(primitiveOnly, { a: [1, { b: 2 }], c: { d: 3 }, e: null })) {
    throw new Error("predicate was not applied exactly once per leaf");
}

const specialInput = JSON.parse(
    '{"__proto__":{"keep":1,"drop":0},"constructor":{"keep":2}}',
);
const special = deepFilter(specialInput, predicates.truthy);
if (!Object.prototype.hasOwnProperty.call(special, "__proto__") ||
    !equal(special.__proto__, { keep: 1 }) ||
    !equal(special.constructor, { keep: 2 })) {
    throw new Error("special object keys were not preserved");
}

const boundary = Array.from(
    { length: 5000 },
    (_, index) => index % 2 === 0
        ? { keep: index, drop: -index - 1 }
        : [index, -index],
);
const boundaryResult = deepFilter(boundary, predicates.positive);
if (!Array.isArray(boundaryResult) || boundaryResult.length !== 4999) {
    throw new Error("wide boundary result has the wrong size");
}
"""
    completed = subprocess.run(
        [node, "-e", script, str(source_path), str(cases_path), str(benchmark_path)],
        cwd=package,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_rounded_purchase_balance_matches_complete_legal_domain() -> None:
    account_balance = _reference_solve("2806")

    for purchase_amount in range(101):
        tens, remainder = divmod(purchase_amount, 10)
        rounded_amount = (tens + (remainder >= 5)) * 10
        assert account_balance(purchase_amount) == 100 - rounded_amount


def test_insert_gcd_nodes_matches_independent_adjacent_pair_oracle() -> None:
    insert_gcds = _reference_solve("2807")
    package = leetcode_package_dir("lc_2807")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))
    benchmark_payload = json.loads(
        (package / "benchmark.json").read_text(encoding="utf-8")
    )

    def expected_values(values: list[int]) -> list[int]:
        result: list[int] = []
        for index, value in enumerate(values):
            result.append(value)
            if index + 1 < len(values):
                result.append(math.gcd(value, values[index + 1]))
        return result

    for case in payload["cases"]:
        values = case["input"]["head"]
        assert case["expected"] == expected_values(values)
        result = insert_gcds(_list_node_from_values(values))
        assert _list_node_to_values(result) == case["expected"]

    for case in benchmark_payload["cases"]:
        values = case["input"]["head"]
        assert case["size"] == len(values)
        assert case["expected"] == expected_values(values)

    boundary = [840 if index % 2 == 0 else 360 for index in range(5000)]
    result = _list_node_to_values(insert_gcds(_list_node_from_values(boundary)))
    assert len(result) == 9999
    assert result[:5] == [840, 120, 360, 120, 840]
    assert result[-3:] == [840, 120, 360]


def test_minimum_equalization_seconds_matches_circular_distance_oracle() -> None:
    minimum_seconds = _reference_solve("2808")
    package = leetcode_package_dir("lc_2808")

    def oracle(nums: list[int]) -> int:
        n = len(nums)
        best = n
        for value in set(nums):
            sources = [index for index, entry in enumerate(nums) if entry == value]
            required = max(
                min(min((index - source) % n, (source - index) % n) for source in sources)
                for index in range(n)
            )
            best = min(best, required)
        return best

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            nums = case["input"]["nums"]
            assert case["expected"] == oracle(nums)
            assert minimum_seconds(nums) == case["expected"]

    for length in range(1, 8):
        for nums in product(range(1, 4), repeat=length):
            values = list(nums)
            assert minimum_seconds(values) == oracle(values)


def test_minimum_time_to_limit_matches_exhaustive_reset_order_oracle() -> None:
    minimum_time = _reference_solve("2809")
    package = leetcode_package_dir("lc_2809")

    def oracle(nums1: list[int], nums2: list[int], x: int) -> int:
        n = len(nums1)
        initial_sum = sum(nums1)
        growth_sum = sum(nums2)
        for seconds in range(n + 1):
            best_reduction = max(
                sum(
                    nums1[index] + nums2[index] * operation
                    for operation, index in enumerate(order, start=1)
                )
                for order in permutations(range(n), seconds)
            )
            if initial_sum + growth_sum * seconds - best_reduction <= x:
                return seconds
        return -1

    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))
    for case in payload["cases"]:
        inputs = case["input"]
        expected = oracle(inputs["nums1"], inputs["nums2"], inputs["x"])
        assert case["expected"] == expected
        assert minimum_time(**inputs) == expected

    benchmark = json.loads(
        (package / "benchmark.json").read_text(encoding="utf-8")
    )
    for case in benchmark["cases"]:
        assert case["size"] == len(case["input"]["nums1"])
        assert case["expected"] == case["size"]
        assert minimum_time(**case["input"]) == case["expected"]

    for n in range(1, 5):
        for nums1 in product((1, 2), repeat=n):
            for nums2 in product((0, 1), repeat=n):
                for x in range(0, 9):
                    first = list(nums1)
                    second = list(nums2)
                    assert minimum_time(first, second, x) == oracle(first, second, x)


def test_faulty_keyboard_matches_literal_reversal_simulation() -> None:
    final_string = _reference_solve("2810")
    package = leetcode_package_dir("lc_2810")

    def oracle(s: str) -> str:
        text = ""
        for character in s:
            if character == "i":
                text = text[::-1]
            else:
                text += character
        return text

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            s = case["input"]["s"]
            assert case["expected"] == oracle(s)
            assert final_string(s) == case["expected"]

    for length in range(1, 9):
        for first in "ab":
            for suffix in product("abi", repeat=length - 1):
                s = first + "".join(suffix)
                assert final_string(s) == oracle(s)


def test_split_array_criterion_matches_exhaustive_legal_splits() -> None:
    can_split_array = _reference_solve("2811")
    package = leetcode_package_dir("lc_2811")

    def oracle(nums: list[int], m: int) -> bool:
        @lru_cache(maxsize=None)
        def splittable(values: tuple[int, ...]) -> bool:
            if len(values) == 1:
                return True
            for cut in range(1, len(values)):
                left = values[:cut]
                right = values[cut:]
                left_good = len(left) == 1 or sum(left) >= m
                right_good = len(right) == 1 or sum(right) >= m
                if (
                    left_good
                    and right_good
                    and splittable(left)
                    and splittable(right)
                ):
                    return True
            return False

        return splittable(tuple(nums))

    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))
    for case in payload["cases"]:
        inputs = case["input"]
        expected = oracle(inputs["nums"], inputs["m"])
        assert case["expected"] is expected
        assert can_split_array(**inputs) is expected

    benchmark = json.loads(
        (package / "benchmark.json").read_text(encoding="utf-8")
    )
    for case in benchmark["cases"]:
        assert case["size"] == len(case["input"]["nums"])
        assert case["expected"] is False
        assert can_split_array(**case["input"]) is False

    for length in range(1, 8):
        for nums in product(range(1, 4), repeat=length):
            values = list(nums)
            for m in range(1, 7):
                assert can_split_array(values, m) is oracle(values, m)


def test_maximum_safeness_matches_threshold_connectivity_oracle() -> None:
    maximum_safeness = _reference_solve("2812")
    package = leetcode_package_dir("lc_2812")

    def oracle(grid: list[list[int]]) -> int:
        n = len(grid)
        thieves = [
            (row, column)
            for row in range(n)
            for column in range(n)
            if grid[row][column] == 1
        ]
        distance = [
            [
                min(abs(row - tr) + abs(column - tc) for tr, tc in thieves)
                for column in range(n)
            ]
            for row in range(n)
        ]

        def reachable(threshold: int) -> bool:
            if distance[0][0] < threshold:
                return False
            queue = [(0, 0)]
            seen = {(0, 0)}
            for row, column in queue:
                if (row, column) == (n - 1, n - 1):
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_column = row + dr, column + dc
                    if (
                        0 <= next_row < n
                        and 0 <= next_column < n
                        and (next_row, next_column) not in seen
                        and distance[next_row][next_column] >= threshold
                    ):
                        seen.add((next_row, next_column))
                        queue.append((next_row, next_column))
            return False

        return max(threshold for threshold in range(2 * n) if reachable(threshold))

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            grid = case["input"]["grid"]
            assert case["expected"] == oracle(grid)
            assert maximum_safeness(grid) == case["expected"]

    for n in range(1, 4):
        for mask in range(1, 1 << (n * n)):
            grid = [
                [(mask >> (row * n + column)) & 1 for column in range(n)]
                for row in range(n)
            ]
            assert maximum_safeness(grid) == oracle(grid)


def test_maximum_elegance_matches_exhaustive_subsets() -> None:
    maximum_elegance = _reference_solve("2813")
    package = leetcode_package_dir("lc_2813")

    def oracle(items: list[list[int]], k: int) -> int:
        return max(
            sum(items[index][0] for index in chosen)
            + len({items[index][1] for index in chosen}) ** 2
            for chosen in combinations(range(len(items)), k)
        )

    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))
    for case in payload["cases"]:
        inputs = case["input"]
        expected = oracle(inputs["items"], inputs["k"])
        assert case["expected"] == expected
        assert maximum_elegance(**inputs) == expected

    benchmark = json.loads(
        (package / "benchmark.json").read_text(encoding="utf-8")
    )
    for case in benchmark["cases"]:
        assert case["size"] == len(case["input"]["items"])
        assert maximum_elegance(**case["input"]) == case["expected"]

    for n in range(1, 7):
        for categories in product(range(1, 4), repeat=n):
            items = [[index + 1, categories[index]] for index in range(n)]
            for k in range(1, n + 1):
                assert maximum_elegance(items, k) == oracle(items, k)


def test_drowning_escape_matches_second_by_second_simulation() -> None:
    minimum_seconds = _reference_solve("2814")
    package = leetcode_package_dir("lc_2814")

    def oracle(land: list[list[str]]) -> int:
        rows, columns = len(land), len(land[0])
        flooded = {
            (row, column)
            for row in range(rows)
            for column in range(columns)
            if land[row][column] == "*"
        }
        start = next(
            (row, column)
            for row in range(rows)
            for column in range(columns)
            if land[row][column] == "S"
        )
        positions = {start}
        seen = {start}
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for time in range(1, rows * columns + 1):
            next_flooded = set(flooded)
            for row, column in flooded:
                for dr, dc in directions:
                    next_row, next_column = row + dr, column + dc
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and land[next_row][next_column] == "."
                    ):
                        next_flooded.add((next_row, next_column))

            next_positions = set()
            for row, column in positions:
                for dr, dc in directions:
                    next_row, next_column = row + dr, column + dc
                    if not (0 <= next_row < rows and 0 <= next_column < columns):
                        continue
                    if land[next_row][next_column] == "D":
                        return time
                    coordinate = (next_row, next_column)
                    if (
                        land[next_row][next_column] == "."
                        and coordinate not in next_flooded
                        and coordinate not in seen
                    ):
                        seen.add(coordinate)
                        next_positions.add(coordinate)
            flooded = next_flooded
            positions = next_positions
            if not positions:
                return -1
        return -1

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            land = case["input"]["land"]
            assert case["expected"] == oracle(land)
            assert minimum_seconds(land) == case["expected"]

    cells = range(9)
    for start, destination, flood in permutations(cells, 3):
        land = [["."] * 3 for _ in range(3)]
        land[start // 3][start % 3] = "S"
        land[destination // 3][destination % 3] = "D"
        land[flood // 3][flood % 3] = "*"
        assert minimum_seconds(land) == oracle(land)


def test_max_pair_sum_matches_direct_pair_enumeration() -> None:
    max_pair_sum = _reference_solve("2815")
    package = leetcode_package_dir("lc_2815")

    def largest_digit(number: int) -> int:
        return max(map(int, str(number)))

    def oracle(nums: list[int]) -> int:
        answer = -1
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if largest_digit(nums[left]) == largest_digit(nums[right]):
                    answer = max(answer, nums[left] + nums[right])
        return answer

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            nums = case["input"]["nums"]
            assert case["expected"] == oracle(nums)
            assert max_pair_sum(nums) == case["expected"]

    values = (1, 9, 12, 21, 55, 91)
    for length in range(2, 6):
        for nums in product(values, repeat=length):
            entries = list(nums)
            assert max_pair_sum(entries) == oracle(entries)


def test_double_linked_list_matches_decimal_carry_oracle() -> None:
    double_digits = _reference_solve("2816")
    package = leetcode_package_dir("lc_2816")

    def oracle(digits: list[int]) -> list[int]:
        doubled = [0] * len(digits)
        carry = 0
        for index in range(len(digits) - 1, -1, -1):
            value = digits[index] * 2 + carry
            doubled[index] = value % 10
            carry = value // 10
        if carry:
            doubled.insert(0, carry)
        return doubled

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            digits = case["input"]["head"]
            assert case["expected"] == oracle(digits)
            result = double_digits(_list_node_from_values(digits))
            assert _list_node_to_values(result) == case["expected"]

    suffix_digits = (0, 4, 5, 9)
    for length in range(1, 7):
        for first in range(1, 10):
            for suffix in product(suffix_digits, repeat=length - 1):
                digits = [first, *suffix]
                result = double_digits(_list_node_from_values(digits))
                assert _list_node_to_values(result) == oracle(digits)

    boundary = [9] * 10_000
    result = _list_node_to_values(double_digits(_list_node_from_values(boundary)))
    assert result == [1, *([9] * 9_999), 8]


def test_minimum_constrained_difference_matches_pair_enumeration() -> None:
    minimum_difference = _reference_solve("2817")
    package = leetcode_package_dir("lc_2817")

    def oracle(nums: list[int], x: int) -> int:
        if x == 0:
            return 0
        return min(
            abs(nums[left] - nums[right])
            for left in range(len(nums))
            for right in range(left + x, len(nums))
        )

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            nums = case["input"]["nums"]
            x = case["input"]["x"]
            assert case["expected"] == oracle(nums, x)
            assert minimum_difference(nums, x) == case["expected"]

    values = (1, 4, 9)
    for length in range(1, 7):
        for entries in product(values, repeat=length):
            nums = list(entries)
            for x in range(length):
                assert minimum_difference(nums, x) == oracle(nums, x)

    boundary = list(range(1, 100_001))
    assert minimum_difference(boundary, 99_999) == 99_999


def test_maximum_operation_score_matches_subarray_enumeration() -> None:
    maximum_score = _reference_solve("2818")
    package = leetcode_package_dir("lc_2818")
    modulus = 1_000_000_007

    def prime_score(value: int) -> int:
        score = 0
        divisor = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                score += 1
                while value % divisor == 0:
                    value //= divisor
            divisor += 1
        return score + (value > 1)

    def oracle(nums: list[int], k: int) -> int:
        scores = [prime_score(value) for value in nums]
        factors: list[int] = []
        for left in range(len(nums)):
            winner = left
            for right in range(left, len(nums)):
                if scores[right] > scores[winner]:
                    winner = right
                factors.append(nums[winner])
        factors.sort(reverse=True)
        answer = 1
        for factor in factors[:k]:
            answer = answer * factor % modulus
        return answer

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            nums = case["input"]["nums"]
            k = case["input"]["k"]
            assert case["expected"] == oracle(nums, k)
            assert maximum_score(nums, k) == case["expected"]

    values = (1, 2, 6, 30)
    for length in range(1, 6):
        subarray_count = length * (length + 1) // 2
        operation_counts = {1, (subarray_count + 1) // 2, subarray_count}
        for entries in product(values, repeat=length):
            nums = list(entries)
            for k in operation_counts:
                assert maximum_score(nums, k) == oracle(nums, k)

    boundary = [100_000] * 100_000
    assert maximum_score(boundary, 1_000_000_000) == pow(
        100_000, 1_000_000_000, modulus
    )


def test_minimum_relative_losses_match_transformed_loss_sorting() -> None:
    minimum_losses = _reference_solve("2819")
    package = leetcode_package_dir("lc_2819")

    def oracle(prices: list[int], queries: list[list[int]]) -> list[int]:
        answers: list[int] = []
        for threshold, count in queries:
            losses = [
                price if price <= threshold else 2 * threshold - price
                for price in prices
            ]
            losses.sort()
            answers.append(sum(losses[:count]))
        return answers

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            prices = case["input"]["prices"]
            queries = case["input"]["queries"]
            assert case["expected"] == oracle(prices, queries)
            assert minimum_losses(prices.copy(), queries) == case["expected"]

    values = (1, 4, 9)
    for length in range(1, 7):
        queries = [
            [threshold, count]
            for threshold in (1, 3, 5, 10)
            for count in range(1, length + 1)
        ]
        for entries in product(values, repeat=length):
            prices = list(entries)
            assert minimum_losses(prices.copy(), queries) == oracle(prices, queries)

    boundary = list(range(1, 100_001))
    queries = [[1, 100_000], [1_000_000_000, 100_000], [50_000, 1]]
    assert minimum_losses(boundary.copy(), queries) == oracle(boundary, queries)


def test_election_results_match_exact_fractional_vote_oracle() -> None:
    package = leetcode_package_dir("lc_2820")
    query = (
        package / "variants" / "optimal" / "solutions" / "sql.sql"
    ).read_text(encoding="utf-8")

    def oracle(rows: list[dict[str, str | None]]) -> list[list[str]]:
        choices: dict[str, int] = {}
        for row in rows:
            if row["candidate"] is not None:
                voter = str(row["voter"])
                choices[voter] = choices.get(voter, 0) + 1

        totals: dict[str, Fraction] = {}
        for row in rows:
            candidate = row["candidate"]
            if candidate is None:
                continue
            voter = str(row["voter"])
            candidate_name = str(candidate)
            totals[candidate_name] = totals.get(candidate_name, Fraction()) + Fraction(
                1, choices[voter]
            )

        if not totals:
            return []
        maximum = max(totals.values())
        return [[candidate] for candidate in sorted(
            candidate for candidate, total in totals.items() if total == maximum
        )]

    def execute(rows: list[dict[str, str | None]]) -> list[list[str]]:
        with sqlite3.connect(":memory:") as connection:
            connection.execute("CREATE TABLE Votes (voter TEXT, candidate TEXT)")
            connection.executemany(
                "INSERT INTO Votes (voter, candidate) VALUES (?, ?)",
                [(row["voter"], row["candidate"]) for row in rows],
            )
            return [list(row) for row in connection.execute(query).fetchall()]

    for filename in ("cases.json", "benchmark.json"):
        payload = json.loads((package / filename).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            rows = case["input"]["tables"]["Votes"]
            expected = oracle(rows)
            assert case["expected"]["columns"] == ["candidate"]
            assert case["expected"]["rows"] == expected
            assert execute(rows) == expected

    options = (
        (None,),
        ("A",),
        ("B",),
        ("C",),
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("A", "B", "C"),
    )
    for voter_choices in product(options, repeat=3):
        rows = [
            {"voter": f"v{voter}", "candidate": candidate}
            for voter, candidates in enumerate(voter_choices)
            for candidate in candidates
        ]
        assert execute(rows) == oracle(rows)

    boundary = [
        {"voter": f"v{voter}", "candidate": candidate}
        for voter in range(2_000)
        for candidate in ("Alpha", f"C{voter:04d}")
    ]
    assert execute(boundary) == [["Alpha"]]


def test_nested_array_generator_cases_match_recursive_inorder_oracle() -> None:
    payload = json.loads(
        (leetcode_package_dir("lc_2649") / "cases.json").read_text(encoding="utf-8")
    )

    def flatten(value: list[object]) -> list[int]:
        result: list[int] = []
        for entry in value:
            if isinstance(entry, list):
                result.extend(flatten(entry))
            else:
                assert isinstance(entry, int) and not isinstance(entry, bool)
                result.append(entry)
        return result

    for case in payload["cases"]:
        assert case["expected"] == flatten(case["input"]["arr"])


def test_fibonacci_generator_cases_match_independent_recurrence() -> None:
    payload = json.loads(
        (leetcode_package_dir("lc_2648") / "cases.json").read_text(encoding="utf-8")
    )
    call_counts = {case["input"]["callCount"] for case in payload["cases"]}
    assert {0, 1, 2, 50}.issubset(call_counts)

    for case in payload["cases"]:
        expected: list[int] = []
        previous, current = 0, 1
        for _ in range(case["input"]["callCount"]):
            expected.append(previous)
            previous, current = current, previous + current
        assert case["expected"] == expected


def test_color_red_triangle_construction_matches_bound_and_small_exhaustive_oracle() -> None:
    color_red = _reference_solve("2647")

    for n in range(1, 65):
        result = color_red(n)
        assert len(result) == math.ceil(n * (n + 3) / 4)
        assert _color_red_triangle_match(result, n)

    def percolates(n: int, seeds: tuple[tuple[int, int], ...]) -> bool:
        red = set(seeds)
        changed = True
        while changed:
            changed = False
            for row in range(1, n + 1):
                for column in range(1, 2 * row):
                    coordinate = (row, column)
                    if coordinate in red:
                        continue
                    adjacent = {(row, column - 1), (row, column + 1)}
                    if column % 2 == 1:
                        adjacent.add((row + 1, column + 1))
                    else:
                        adjacent.add((row - 1, column - 1))
                    if len(red & adjacent) >= 2:
                        red.add(coordinate)
                        changed = True
            if len(red) == n * n:
                return True
        return len(red) == n * n

    for n in range(1, 5):
        coordinates = tuple(
            (row, column)
            for row in range(1, n + 1)
            for column in range(1, 2 * row)
        )
        minimum = math.ceil(n * (n + 3) / 4)
        assert percolates(n, tuple(map(tuple, color_red(n))))
        assert not any(
            percolates(n, seeds)
            for size in range(minimum)
            for seeds in combinations(coordinates, size)
        )


def test_count_dividing_digits_matches_independent_oracle() -> None:
    count_digits = _reference_solve("2520")

    for length in range(1, 6):
        for digits in product("123456789", repeat=length):
            value = int("".join(digits))
            expected = sum(value % int(digit) == 0 for digit in digits)
            assert count_digits(value) == expected

    for value in (111111111, 123456789, 222222222, 987654321, 999999999):
        expected = sum(value % int(digit) == 0 for digit in str(value))
        assert count_digits(value) == expected


def test_alternating_digit_sum_matches_independent_oracle() -> None:
    alternating_sum = _reference_solve("2544")

    def oracle(value: int) -> int:
        return sum(
            int(digit) if index % 2 == 0 else -int(digit)
            for index, digit in enumerate(str(value))
        )

    for value in range(1, 100_001):
        assert alternating_sum(value) == oracle(value)

    for value in (101010101, 123456789, 909090909, 999999999, 1_000_000_000):
        assert alternating_sum(value) == oracle(value)


def test_maximum_difference_by_remapping_matches_exhaustive_oracle() -> None:
    min_max_difference = _reference_solve("2566")

    def oracle(value: int) -> int:
        digits = str(value)
        remapped = [
            int(digits.replace(source, destination))
            for source in "0123456789"
            for destination in "0123456789"
        ]
        return max(remapped) - min(remapped)

    for value in range(1, 10_001):
        assert min_max_difference(value) == oracle(value)

    for value in (10_000_000, 11_891_118, 90_909_090, 99_999_999, 100_000_000):
        assert min_max_difference(value) == oracle(value)


def test_count_distinct_numbers_on_board_matches_exhaustive_simulation() -> None:
    count_distinct = _reference_solve("2549")

    def simulate(initial: int) -> int:
        board = {initial}
        while True:
            expanded = board | {
                candidate
                for value in board
                for candidate in range(1, initial + 1)
                if value % candidate == 1
            }
            if expanded == board:
                return len(board)
            board = expanded

    for initial in range(1, 101):
        assert count_distinct(initial) == simulate(initial)


def test_x_matrix_matches_every_binary_three_by_three_matrix() -> None:
    check_x_matrix = _reference_solve("2319")
    diagonal = {(index, index) for index in range(3)}
    diagonal.update((index, 2 - index) for index in range(3))

    for values in product(range(2), repeat=9):
        grid = [list(values[offset : offset + 3]) for offset in range(0, 9, 3)]
        expected = all(
            (grid[row][column] != 0)
            if (row, column) in diagonal
            else (grid[row][column] == 0)
            for row in range(3)
            for column in range(3)
        )
        assert check_x_matrix(grid) is expected


def test_strictly_palindromic_number_has_a_witness_for_every_legal_input() -> None:
    is_strictly_palindromic = _reference_solve("2396")

    for n in range(4, 100_001):
        assert is_strictly_palindromic(n) is False
        if n == 4:
            assert [1, 0, 0] != [1, 0, 0][::-1]
        else:
            base = n - 2
            assert divmod(n, base) == (1, 2)
            assert [1, 2] != [1, 2][::-1]

    def digits_in_base(value: int, base: int) -> list[int]:
        digits: list[int] = []
        while value:
            value, digit = divmod(value, base)
            digits.append(digit)
        return digits

    for n in range(4, 201):
        expected = all(
            (digits := digits_in_base(n, base)) == digits[::-1]
            for base in range(2, n - 1)
        )
        assert is_strictly_palindromic(n) is expected


def test_optimal_partition_matches_independent_dynamic_programming() -> None:
    partition_string = _reference_solve("2405")

    def oracle(value: str) -> int:
        best = [len(value) + 1] * (len(value) + 1)
        best[0] = 0
        for start in range(len(value)):
            used: set[str] = set()
            for end in range(start, min(len(value), start + 26)):
                if value[end] in used:
                    break
                used.add(value[end])
                best[end + 1] = min(best[end + 1], best[start] + 1)
        return best[-1]

    for length in range(1, 9):
        for letters in product("abc", repeat=length):
            value = "".join(letters)
            assert partition_string(value) == oracle(value)

    state = 0x2405
    for length in (26, 257, 4096):
        letters = []
        for _ in range(length):
            state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
            letters.append(chr(ord("a") + state % 26))
        value = "".join(letters)
        assert partition_string(value) == oracle(value)


def test_maximum_xor_matches_exhaustive_reachable_submasks() -> None:
    maximum_xor = _reference_solve("2317")

    def submasks(value: int) -> list[int]:
        values = []
        submask = value
        while True:
            values.append(submask)
            if submask == 0:
                return values
            submask = (submask - 1) & value

    def oracle(nums: tuple[int, ...]) -> int:
        best = 0
        for transformed in product(*(submasks(value) for value in nums)):
            candidate = 0
            for value in transformed:
                candidate ^= value
            best = max(best, candidate)
        return best

    for length in range(1, 4):
        for nums in product(range(8), repeat=length):
            assert maximum_xor(list(nums)) == oracle(nums)


def test_equal_digit_count_matches_direct_count_oracle() -> None:
    digit_count = _reference_solve("2283")

    def oracle(num: str) -> bool:
        return all(num.count(str(index)) == int(required) for index, required in enumerate(num))

    for length in range(1, 6):
        for digits in product("0123456789", repeat=length):
            num = "".join(digits)
            assert digit_count(num) == oracle(num)

    values = {
        "0",
        "1",
        "1210",
        "2020",
        "21200",
        "030",
        "010",
        "6210001000",
        "9999999999",
    }
    state = 2283
    for length in range(6, 11):
        for _ in range(4000):
            digits = []
            for _ in range(length):
                state = (
                    state * 6364136223846793005 + 1442695040888963407
                ) & ((1 << 64) - 1)
                digits.append(str(state % 10))
            values.add("".join(digits))

    for num in values:
        assert digit_count(num) == oracle(num)


def test_cookie_distribution_bounded_domain_matches_assignment_oracle() -> None:
    distribute = _reference_solve("2305")

    def oracle(cookies: list[int], k: int) -> int:
        best = sum(cookies)
        for assignment in product(range(k), repeat=len(cookies)):
            loads = [0] * k
            for bag, child in zip(cookies, assignment):
                loads[child] += bag
            best = min(best, max(loads))
        return best

    fixtures = [
        ([8, 15, 10, 20, 8], 2),
        ([6, 1, 3, 2, 2, 4, 1, 2], 3),
        ([1, 2], 2),
        ([9, 8, 7, 6, 5, 4, 3, 2], 2),
        ([9, 8, 7, 6, 5, 4, 3, 2], 8),
    ]
    state = 2305
    for _ in range(500):
        state = (state * 6364136223846793005 + 1442695040888963407) & (
            (1 << 64) - 1
        )
        count = 2 + state % 5
        cookies = []
        for _ in range(count):
            state = (
                state * 6364136223846793005 + 1442695040888963407
            ) & ((1 << 64) - 1)
            cookies.append(1 + state % 20)
        state = (state * 6364136223846793005 + 1442695040888963407) & (
            (1 << 64) - 1
        )
        fixtures.append((cookies, 2 + state % (count - 1)))

    for cookies, k in fixtures:
        assert distribute(cookies, k) == oracle(cookies, k)


def test_units_digit_sum_bounded_domain_matches_all_legal_pairs() -> None:
    minimum_numbers = _reference_solve("2310")

    for k in range(10):
        possible = [False] * 3001
        possible[0] = True
        for total in range(1, 3001):
            possible[total] = any(
                total >= value and possible[total - value]
                for value in range(k or 10, total + 1, 10)
            )

        for num in range(3001):
            if num == 0:
                expected = 0
            else:
                expected = next(
                    (
                        count
                        for count in range(1, 11)
                        if count * k <= num and count * k % 10 == num % 10
                    ),
                    -1,
                )
            assert minimum_numbers(num, k) == expected
            assert possible[num] == (expected != -1)


def test_maximum_even_split_matches_cardinality_boundaries() -> None:
    maximum_even_split = _reference_solve("2178")

    values = set(range(1, 10_001))
    state = 2178
    for _ in range(500):
        state = (state * 6364136223846793005 + 1442695040888963407) % (
            10**10
        ) + 1
        values.update({max(1, state - 1), state, min(10**10, state + 1)})
    values.add(10**10)

    for final_sum in values:
        result = maximum_even_split(final_sum)
        if final_sum % 2:
            assert result == []
            continue
        maximum_count = (math.isqrt(1 + 4 * final_sum) - 1) // 2
        assert len(result) == maximum_count
        assert len(result) == len(set(result))
        assert all(value > 0 and value % 2 == 0 for value in result)
        assert sum(result) == final_sum


def test_sum_of_three_matches_algebraic_boundaries() -> None:
    sum_of_three = _reference_solve("2177")

    for num in range(100_001):
        result = sum_of_three(num)
        if num % 3:
            assert result == []
        else:
            assert result == [num // 3 - 1, num // 3, num // 3 + 1]

    state = 2177
    values = {0, 1, 2, 3, 10**15 - 2, 10**15 - 1, 10**15}
    for _ in range(20_000):
        state = (state * 6364136223846793005 + 1442695040888963407) % (
            10**15 + 1
        )
        values.update({max(0, state - 1), state, min(10**15, state + 1)})

    for num in values:
        result = sum_of_three(num)
        assert (result == []) == (num % 3 != 0)
        if result:
            assert result[1] == result[0] + 1
            assert result[2] == result[1] + 1
            assert sum(result) == num


def test_remove_ones_ii_bounded_domain_matches_bottom_up_oracle() -> None:
    remove_ones = _reference_solve("2174")

    def expected_answers(rows: int, columns: int) -> list[int]:
        cells = rows * columns
        clear_masks = []
        for row in range(rows):
            for column in range(columns):
                clear_mask = 0
                for other_column in range(columns):
                    clear_mask |= 1 << (row * columns + other_column)
                for other_row in range(rows):
                    clear_mask |= 1 << (other_row * columns + column)
                clear_masks.append(clear_mask)

        answers = [0] * (1 << cells)
        for state in range(1, 1 << cells):
            answers[state] = 1 + min(
                answers[state & ~clear_masks[position]]
                for position in range(cells)
                if state & (1 << position)
            )
        return answers

    for rows in range(1, 4):
        for columns in range(1, 4):
            answers = expected_answers(rows, columns)
            for state, expected in enumerate(answers):
                grid = [
                    [
                        (state >> (row * columns + column)) & 1
                        for column in range(columns)
                    ]
                    for row in range(rows)
                ]
                assert remove_ones(grid) == expected

    for rows, columns in ((1, 15), (3, 5), (5, 3), (15, 1)):
        answers = expected_answers(rows, columns)
        states = {
            0,
            1,
            (1 << (rows * columns)) - 1,
            sum(1 << index for index in range(0, rows * columns, 2)),
            sum(1 << index for index in range(1, rows * columns, 2)),
        }
        value = rows * 1000 + columns
        for _ in range(2500):
            value = (value * 1103515245 + 12345) & 0x7FFFFFFF
            states.add(value & ((1 << (rows * columns)) - 1))

        for state in states:
            grid = [
                [
                    (state >> (row * columns + column)) & 1
                    for column in range(columns)
                ]
                for row in range(rows)
            ]
            assert remove_ones(grid) == answers[state]


def test_smallest_rearranged_number_matches_digit_frequency_oracle() -> None:
    smallest = _reference_solve("2165")

    for value in range(-99999, 100000):
        assert smallest(value) == _smallest_number_frequency_oracle(value)

    boundary_values = (
        -10**15,
        -(10**15 - 1),
        -987654321001234,
        -100000000000001,
        100000000000001,
        987654321001234,
        10**15 - 1,
        10**15,
    )
    for value in boundary_values:
        assert smallest(value) == _smallest_number_frequency_oracle(value)

    state = 2165
    for _ in range(10000):
        state = (state * 6364136223846793005 + 1442695040888963407) % (
            2 * 10**15 + 1
        )
        value = state - 10**15
        assert smallest(value) == _smallest_number_frequency_oracle(value)


def _smallest_number_frequency_oracle(num: int) -> int:
    if num == 0:
        return 0

    counts = [0] * 10
    magnitude = abs(num)
    while magnitude:
        counts[magnitude % 10] += 1
        magnitude //= 10

    ordered_digits: list[int] = []
    if num < 0:
        for digit in range(9, -1, -1):
            ordered_digits.extend([digit] * counts[digit])
    else:
        first = next(digit for digit in range(1, 10) if counts[digit])
        ordered_digits.append(first)
        counts[first] -= 1
        for digit in range(10):
            ordered_digits.extend([digit] * counts[digit])

    result = 0
    for digit in ordered_digits:
        result = 10 * result + digit
    return -result if num < 0 else result


def test_largest_integer_by_parity_matches_digit_frequency_oracle() -> None:
    largest_integer = _reference_solve("2231")

    values = set(range(1, 100_001))
    values.update({1, 9, 10, 999_999_999, 1_000_000_000})
    state = 2231
    for _ in range(20_000):
        state = (state * 6364136223846793005 + 1442695040888963407) % (
            10**9
        ) + 1
        values.add(state)

    for value in values:
        assert largest_integer(value) == _largest_integer_parity_oracle(value)


def _largest_integer_parity_oracle(num: int) -> int:
    counts = [0] * 10
    for character in str(num):
        counts[int(character)] += 1

    result = 0
    for character in str(num):
        parity = int(character) % 2
        digit = 9 if parity else 8
        while counts[digit] == 0:
            digit -= 2
        counts[digit] -= 1
        result = result * 10 + digit
    return result


def test_minimized_parentheses_match_independent_placement_evaluation() -> None:
    minimize_result = _reference_solve("2232")

    expressions = {
        f"{left}+{right}"
        for left in range(1, 100)
        for right in range(1, 100)
    }
    state = 2232
    for _ in range(20_000):
        state = (state * 6364136223846793005 + 1442695040888963407) % (
            10**9
        ) + 1
        digits = str(state).replace("0", "1")
        if len(digits) == 1:
            digits += "1"
        split = 1 + state % (len(digits) - 1)
        expressions.add(f"{digits[:split]}+{digits[split:]}")

    for expression in expressions:
        result = minimize_result(expression)
        assert result.replace("(", "").replace(")", "") == expression
        assert _parenthesized_expression_value(result) == min(
            _placement_value(expression, left, right)
            for left in range(expression.index("+"))
            for right in range(expression.index("+") + 2, len(expression) + 1)
        )


def test_add_two_integers_matches_every_legal_operand_pair() -> None:
    add_two_integers = _reference_solve("2235")

    for num1 in range(-100, 101):
        for num2 in range(-100, 101):
            assert add_two_integers(num1, num2) == num1 + num2


def test_root_sum_check_matches_all_child_pairs_and_boundaries() -> None:
    check_tree = _reference_solve("2236")

    class Node:
        def __init__(self, value: int) -> None:
            self.val = value
            self.left = None
            self.right = None

    def evaluate(root_value: int, left_value: int, right_value: int) -> bool:
        root = Node(root_value)
        root.left = Node(left_value)
        root.right = Node(right_value)
        return check_tree(root)

    for left_value in range(-100, 101):
        for right_value in range(-100, 101):
            child_sum = left_value + right_value
            if -100 <= child_sum <= 100:
                assert evaluate(child_sum, left_value, right_value)
                if child_sum > -100:
                    assert not evaluate(child_sum - 1, left_value, right_value)
                if child_sum < 100:
                    assert not evaluate(child_sum + 1, left_value, right_value)
            assert evaluate(-100, left_value, right_value) == (child_sum == -100)
            assert evaluate(100, left_value, right_value) == (child_sum == 100)


def _placement_value(expression: str, left: int, right: int) -> int:
    plus = expression.index("+")
    prefix = int(expression[:left]) if left else 1
    left_addend = int(expression[left:plus])
    right_addend = int(expression[plus + 1:right])
    suffix = int(expression[right:]) if right < len(expression) else 1
    return prefix * (left_addend + right_addend) * suffix


def _parenthesized_expression_value(expression: str) -> int:
    opening = expression.index("(")
    closing = expression.index(")")
    plus = expression.index("+")
    prefix = int(expression[:opening]) if opening else 1
    left_addend = int(expression[opening + 1:plus])
    right_addend = int(expression[plus + 1:closing])
    suffix = int(expression[closing + 1:]) if closing + 1 < len(expression) else 1
    return prefix * (left_addend + right_addend) * suffix


def test_microwave_cost_certificate_matches_all_targets_and_starting_digits() -> None:
    minimum_cost = _reference_solve("2162")
    entries_by_duration: dict[int, list[str]] = {}

    for value in range(1, 10000):
        digits = str(value)
        normalized = digits.zfill(4)
        duration = 60 * int(normalized[:2]) + int(normalized[2:])
        entries_by_duration.setdefault(duration, []).append(digits)

    cost_pairs = ((1, 1), (1, 100000), (100000, 1), (7, 13))
    for target in range(1, 6040):
        entries = entries_by_duration[target]
        for start_at in range(10):
            for move_cost, push_cost in cost_pairs:
                expected = min(
                    _microwave_entry_cost(
                        digits,
                        start_at=start_at,
                        move_cost=move_cost,
                        push_cost=push_cost,
                    )
                    for digits in entries
                )
                assert (
                    minimum_cost(start_at, move_cost, push_cost, target)
                    == expected
                )


def _microwave_entry_cost(
    digits: str,
    *,
    start_at: int,
    move_cost: int,
    push_cost: int,
) -> int:
    finger = str(start_at)
    total = 0
    for digit in digits:
        if digit != finger:
            total += move_cost
            finger = digit
        total += push_cost
    return total


def test_minimum_four_digit_sum_certificate_matches_exhaustive_splits() -> None:
    minimum_sum = _reference_solve("2160")

    for value in range(1000, 10000):
        digits = str(value)
        expected = min(
            int("".join(order[:split])) + int("".join(order[split:]))
            for order in permutations(digits)
            for split in range(1, 4)
        )
        assert minimum_sum(value) == expected


def test_fill_cups_certificate_matches_every_unordered_legal_triple() -> None:
    import heapq

    fill_cups = _reference_solve("2335")

    for cold in range(101):
        for warm in range(cold, 101):
            for hot in range(warm, 101):
                heap = [-value for value in (cold, warm, hot) if value]
                heapq.heapify(heap)
                expected = 0
                while heap:
                    largest = -heapq.heappop(heap) - 1
                    second_largest = -heapq.heappop(heap) - 1 if heap else -1
                    if largest:
                        heapq.heappush(heap, -largest)
                    if second_largest > 0:
                        heapq.heappush(heap, -second_largest)
                    expected += 1
                assert fill_cups([cold, warm, hot]) == expected


def test_best_poker_hand_certificate_covers_every_rank_and_suit_signature() -> None:
    best_hand = _reference_solve("2347")
    suit_symbols = ["a", "b", "c", "d"]

    for ranks in product(range(1, 14), repeat=5):
        largest_count = max(ranks.count(rank) for rank in set(ranks))
        if largest_count == 5:
            continue

        occurrences: dict[int, int] = {}
        suits = []
        for rank in ranks:
            occurrence = occurrences.get(rank, 0)
            suits.append(suit_symbols[occurrence])
            occurrences[rank] = occurrence + 1
        if len(set(suits)) == 1:
            suits[-1] = "b"

        expected = (
            "Three of a Kind"
            if largest_count >= 3
            else "Pair"
            if largest_count == 2
            else "High Card"
        )
        assert best_hand(list(ranks), suits) == expected

    distinct_ranks = [1, 2, 3, 4, 5]
    for suits in product(suit_symbols, repeat=5):
        expected = "Flush" if len(set(suits)) == 1 else "High Card"
        assert best_hand(distinct_ranks, list(suits)) == expected


def test_double_reversal_certificate_matches_exhaustive_digit_reversal() -> None:
    is_same = _reference_solve("2119")

    def reverse(value: int) -> int:
        reversed_value = 0
        while value:
            reversed_value = reversed_value * 10 + value % 10
            value //= 10
        return reversed_value

    for value in range(1_000_001):
        assert is_same(value) == (reverse(reverse(value)) == value)


def _reference_source(frontend_id: str, language: str) -> str:
    path = leetcode_solution_path(f"lc_{frontend_id}", language)
    assert path is not None and path.is_file()
    return path.read_text(encoding="utf-8")


def test_followers_count_certificate_matches_independent_group_counts() -> None:
    package = leetcode_package_dir("lc_1729")
    assert package is not None
    source = _reference_source("1729", "sql")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))

    for case in payload["cases"]:
        tables = case["input"]["tables"]
        counts: dict[int, int] = {}
        for relationship in tables["Followers"]:
            user_id = relationship["user_id"]
            counts[user_id] = counts.get(user_id, 0) + 1
        expected = [[user_id, counts[user_id]] for user_id in sorted(counts)]

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": ["user_id", "followers_count"],
            "rows": expected,
        }


def test_employee_reports_certificate_matches_independent_direct_aggregates() -> None:
    package = leetcode_package_dir("lc_1731")
    assert package is not None
    source = _reference_source("1731", "sql")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))

    for case in payload["cases"]:
        employees = case["input"]["tables"]["Employees"]
        by_id = {employee["employee_id"]: employee for employee in employees}
        reports: dict[int, list[int]] = {}
        for employee in employees:
            manager_id = employee["reports_to"]
            if manager_id is not None:
                reports.setdefault(manager_id, []).append(employee["age"])

        expected = []
        for manager_id in sorted(reports):
            ages = reports[manager_id]
            average_age = math.floor(sum(ages) / len(ages) + 0.5)
            expected.append(
                [
                    manager_id,
                    by_id[manager_id]["name"],
                    len(ages),
                    average_age,
                ]
            )

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": {"Employees": employees}},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": [
                "employee_id",
                "name",
                "reports_count",
                "average_age",
            ],
            "rows": expected,
        }


def test_employee_time_certificate_matches_independent_duration_groups() -> None:
    package = leetcode_package_dir("lc_1741")
    assert package is not None
    source = _reference_source("1741", "sql")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))

    for case in payload["cases"]:
        employees = case["input"]["tables"]["Employees"]
        totals: dict[tuple[str, int], int] = {}
        for visit in employees:
            key = (visit["event_day"], visit["emp_id"])
            totals[key] = totals.get(key, 0) + visit["out_time"] - visit["in_time"]
        expected = [[day, emp_id, totals[(day, emp_id)]] for day, emp_id in sorted(totals)]

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": {"Employees": employees}},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": ["day", "emp_id", "total_time"],
            "rows": expected,
        }


def test_highest_altitude_bounded_domain_matches_prefix_oracle() -> None:
    highest_altitude = _reference_solve("1732")

    fixtures = [
        [-5, 1, 5, 0, -7],
        [-4, -3, -2, -1, 4, 3, 2],
        [100],
        [-100],
        [0] * 100,
        [100, -100] * 50,
        [-100] * 50 + [100] * 50,
    ]
    for gain in fixtures:
        altitudes = [0]
        for change in gain:
            altitudes.append(altitudes[-1] + change)
        assert highest_altitude(gain) == max(altitudes)

    state = 0x1732
    for length in range(1, 101):
        gain = []
        for _ in range(length):
            state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
            gain.append(state % 201 - 100)
        altitudes = [0]
        for change in gain:
            altitudes.append(altitudes[-1] + change)
        assert highest_altitude(gain) == max(altitudes)


def test_latest_hidden_time_bounded_domain_matches_every_valid_pattern() -> None:
    maximum_time = _reference_solve("1736")
    candidates = [
        f"{hour:02d}:{minute:02d}"
        for hour in range(24)
        for minute in range(60)
    ]
    patterns: set[str] = set()

    for candidate in candidates:
        digit_indexes = (0, 1, 3, 4)
        for mask in range(1 << len(digit_indexes)):
            pattern = list(candidate)
            for bit, index in enumerate(digit_indexes):
                if mask & (1 << bit):
                    pattern[index] = "?"
            patterns.add("".join(pattern))

    for pattern in patterns:
        expected = max(
            candidate
            for candidate in candidates
            if all(
                hidden == "?" or hidden == actual
                for hidden, actual in zip(pattern, candidate)
            )
        )
        assert maximum_time(pattern) == expected


def test_chessboard_color_bounded_domain_matches_all_sixty_four_squares() -> None:
    square_is_white = _reference_solve("1812")

    for rank in range(1, 9):
        expected_white = rank % 2 == 0
        for column in range(8):
            coordinate = f"{chr(ord('a') + column)}{rank}"
            assert square_is_white(coordinate) is expected_white
            expected_white = not expected_white


def test_sentence_similarity_bounded_domain_matches_contiguous_deletion_oracle() -> None:
    are_similar = _reference_solve("1813")

    def brute_force(first: str, second: str) -> bool:
        shorter = first.split()
        longer = second.split()
        if len(shorter) > len(longer):
            shorter, longer = longer, shorter
        return any(
            longer[:start] + longer[end:] == shorter
            for start in range(len(longer) + 1)
            for end in range(start, len(longer) + 1)
        )

    sentences = [
        " ".join(words)
        for length in range(1, 6)
        for words in product(("A", "B"), repeat=length)
    ]
    for first in sentences:
        for second in sentences:
            assert are_similar(first, second) is brute_force(first, second)

    maximum = " ".join(["a"] * 50)
    assert len(maximum) == 99
    assert are_similar("a a", maximum)


def test_fresh_donuts_bounded_domain_matches_independent_bitmask_oracle() -> None:
    from functools import lru_cache

    maximum_happy = _reference_solve("1815")

    def bitmask_oracle(batch_size: int, groups: list[int]) -> int:
        remainders = tuple(group % batch_size for group in groups)

        @lru_cache(maxsize=None)
        def search(mask: int, leftover: int) -> int:
            if mask == (1 << len(remainders)) - 1:
                return 0
            return max(
                (1 if leftover == 0 else 0)
                + search(mask | (1 << index), (leftover + remainder) % batch_size)
                for index, remainder in enumerate(remainders)
                if not mask & (1 << index)
            )

        return search(0, 0)

    for batch_size in range(1, 6):
        values = tuple(range(1, batch_size + 1))
        for length in range(1, 6):
            for groups in product(values, repeat=length):
                expected = bitmask_oracle(batch_size, list(groups))
                assert maximum_happy(batch_size, list(groups)) == expected

    assert maximum_happy(1, [10**9] * 30) == 30
    assert maximum_happy(9, [1] * 30) == 4
    assert maximum_happy(9, [9] * 30) == 30


def _reference_solve(frontend_id: str):
    source_path = leetcode_solution_path(f"lc_{frontend_id}", "python")
    assert source_path is not None
    import typing
    ns = _run_native_module(
        str(source_path),
        init_globals={
            "List": list,
            "Dict": dict,
            "Tuple": tuple,
            "Set": set,
            "Optional": typing.Optional,
            "Union": typing.Union,
            "Any": typing.Any,
            "ListNode": _JudgeListNode,
            "TreeNode": _JudgeTreeNode,
            "Node": _JudgeNode,
            "Point": _JudgePoint,
        },
    )
    from server.app.engine_runner import _bind_leetcode_solution_runner
    from challenges.registry import CHALLENGE_REGISTRY
    ch = CHALLENGE_REGISTRY[f"lc_{frontend_id}"]()
    return _bind_leetcode_solution_runner(ns, challenge=ch)


def test_knights_tour_bounded_domain_validates_every_legal_tuple() -> None:
    tour = _reference_solve("2664")
    legal_inputs = [(1, 1, 0, 0)]
    legal_inputs.extend((3, 4, row, column) for row in range(3) for column in (0, 3))
    legal_inputs.extend((4, 3, row, column) for row in (0, 3) for column in range(3))
    legal_inputs.extend((4, 5, row, column) for row in (0, 3) for column in range(5))
    legal_inputs.extend((5, 4, row, column) for row in range(5) for column in (0, 3))
    legal_inputs.extend(
        (5, 5, row, column)
        for row in range(5)
        for column in range(5)
        if (row + column) % 2 == 0
    )
    assert len(legal_inputs) == 46

    for m, n, start_row, start_column in legal_inputs:
        board = tour(m, n, start_row, start_column)
        assert len(board) == m
        assert all(len(row) == n for row in board)

        positions: list[tuple[int, int] | None] = [None] * (m * n)
        for row in range(m):
            for column in range(n):
                visit = board[row][column]
                assert isinstance(visit, int)
                assert 0 <= visit < m * n
                assert positions[visit] is None
                positions[visit] = (row, column)

        assert positions[0] == (start_row, start_column)
        for visit in range(1, m * n):
            previous = positions[visit - 1]
            current = positions[visit]
            assert previous is not None and current is not None
            differences = sorted(
                (abs(previous[0] - current[0]), abs(previous[1] - current[1]))
            )
            assert differences == [1, 2]


def test_counter_ii_certificate_covers_stateful_operation_sequences() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript counter regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2665_counter-ii';
const { createCounter, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
for (const testCase of cases) {
    const actual = solve(testCase.input.init, testCase.input.calls);
    if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
        throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
    }
}
const first = createCounter(10);
const second = createCounter(-4);
if (first.increment() !== 11 || second.decrement() !== -5 || first.reset() !== 10) {
    throw new Error('counter instances did not retain independent closure state');
}
"""
    completed = subprocess.run(
        ["node", "-e", script],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_once_wrapper_certificate_covers_forwarding_and_suppression() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript once regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2666_allow-one-function-call';
const { once, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
for (const testCase of cases) {
    const actual = solve(testCase.input.operation, testCase.input.calls);
    if (JSON.stringify(actual) !== JSON.stringify(testCase.expected)) {
        throw new Error(`${testCase.id}: ${JSON.stringify(actual)}`);
    }
}
let calls = 0;
const receiver = { base: 7, run: once(function(value) { calls += 1; return this.base + value; }) };
if (receiver.run(5) !== 12 || receiver.run(8) !== undefined || calls !== 1) {
    throw new Error('receiver forwarding or suppression failed');
}
const throwsOnce = once(() => { throw new Error('expected'); });
try { throwsOnce(); } catch (error) { if (error.message !== 'expected') throw error; }
if (throwsOnce() !== undefined) throw new Error('throwing call did not consume permission');
"""
    completed = subprocess.run(
        ["node", "-e", script], cwd=Path.cwd(), capture_output=True,
        text=True, timeout=10, check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_hello_world_certificate_ignores_every_argument_shape() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript hello-world regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2667_create-hello-world-function';
const { createHelloWorld, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;
for (const testCase of cases) {
    const actual = solve(testCase.input.args);
    if (actual !== testCase.expected) throw new Error(`${testCase.id}: ${actual}`);
}
const f = createHelloWorld();
if (f() !== 'Hello World' || f(Symbol('ignored'), () => 1) !== 'Hello World') {
    throw new Error('non-JSON arguments changed the constant result');
}
"""
    completed = subprocess.run(
        ["node", "-e", script], cwd=Path.cwd(), capture_output=True,
        text=True, timeout=10, check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_distinct_difference_bounded_domain_matches_set_oracle() -> None:
    distinct_difference = _reference_solve("2670")

    def oracle(nums: tuple[int, ...]) -> list[int]:
        return [
            len(set(nums[: index + 1])) - len(set(nums[index + 1 :]))
            for index in range(len(nums))
        ]

    for length in range(1, 7):
        for nums in product(range(1, 5), repeat=length):
            assert distinct_difference(list(nums)) == oracle(nums)

    boundaries = [
        tuple([1] * 50),
        tuple(range(1, 51)),
        tuple((index % 7) + 1 for index in range(50)),
    ]
    for nums in boundaries:
        assert distinct_difference(list(nums)) == oracle(nums)


def test_throttle_bounded_domain_matches_deterministic_timer_oracle() -> None:
    if shutil.which("node") is None:
        pytest.skip("Node.js is required for the JavaScript throttle regression")

    script = r"""
const fs = require('fs');
const path = './dsa/leetcode/2676_throttle';
const { throttle, solve } = require(`${path}/variants/optimal/solution.js`);
const cases = JSON.parse(fs.readFileSync(`${path}/cases.json`, 'utf8')).cases;

function runClosure(t, calls) {
    let now = 0;
    let order = 0;
    const queue = calls.map((call) => ({
        time: call.t,
        order: order++,
        callback: null,
        inputs: call.inputs,
    }));
    const output = [];
    const originalSetTimeout = global.setTimeout;
    global.setTimeout = (callback, delay) => {
        queue.push({ time: now + delay, order: order++, callback, inputs: null });
    };
    try {
        const wrapped = throttle((...inputs) => output.push({ t: now, inputs }), t);
        for (const event of queue) {
            if (event.callback === null) event.callback = () => wrapped(...event.inputs);
        }
        while (queue.length > 0) {
            queue.sort((left, right) => left.time - right.time || left.order - right.order);
            const event = queue.shift();
            now = event.time;
            event.callback();
        }
    } finally {
        global.setTimeout = originalSetTimeout;
    }
    return output;
}

for (const testCase of cases) {
    const { t, calls } = testCase.input;
    const simulated = solve(t, calls);
    const actual = runClosure(t, calls);
    const expected = JSON.stringify(testCase.expected);
    if (JSON.stringify(simulated) !== expected || JSON.stringify(actual) !== expected) {
        throw new Error(`${testCase.id}: solve=${JSON.stringify(simulated)} closure=${JSON.stringify(actual)}`);
    }
}
"""
    completed = subprocess.run(
        ["node", "-e", script], cwd=Path.cwd(), capture_output=True, text=True, timeout=10, check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_k_mirror_bounded_domain_matches_independent_numeric_generator() -> None:
    k_mirror = _reference_solve("2081")

    def mirror(half: int, odd_length: bool) -> int:
        value = half
        remainder = half // 10 if odd_length else half
        while remainder:
            value = value * 10 + remainder % 10
            remainder //= 10
        return value

    def is_palindrome_in_base(number: int, base: int) -> bool:
        original = number
        reversed_digits = 0
        while number:
            reversed_digits = reversed_digits * base + number % base
            number //= base
        return reversed_digits == original

    for base in range(2, 10):
        prefix_sums: list[int] = []
        running_sum = 0
        length = 1
        while len(prefix_sums) < 30:
            half_length = (length + 1) // 2
            for half in range(10 ** (half_length - 1), 10**half_length):
                candidate = mirror(half, length % 2 == 1)
                if not is_palindrome_in_base(candidate, base):
                    continue
                running_sum += candidate
                prefix_sums.append(running_sum)
                if len(prefix_sums) == 30:
                    break
            length += 1

        for count, expected in enumerate(prefix_sums, start=1):
            assert k_mirror(base, count) == expected


def test_distanced_sequence_bounded_domain_matches_exhaustive_small_oracle_and_boundaries() -> None:
    construct = _reference_solve("1718")

    def exhaustive_maximum(n: int) -> list[int]:
        sequence = [0] * (2 * n - 1)
        best: list[int] | None = None

        def place(value: int) -> None:
            nonlocal best
            if value == 1:
                for index, current in enumerate(sequence):
                    if current != 0:
                        continue
                    sequence[index] = 1
                    candidate = sequence.copy()
                    if best is None or candidate > best:
                        best = candidate
                    sequence[index] = 0
                return

            for index in range(len(sequence) - value):
                paired_index = index + value
                if sequence[index] != 0 or sequence[paired_index] != 0:
                    continue
                sequence[index] = sequence[paired_index] = value
                place(value - 1)
                sequence[index] = sequence[paired_index] = 0

        place(n)
        assert best is not None
        return best

    for n in range(1, 8):
        assert construct(n) == exhaustive_maximum(n)

    for n in range(1, 21):
        sequence = construct(n)
        assert len(sequence) == 2 * n - 1
        assert all(1 <= value <= n for value in sequence)
        assert sequence.count(1) == 1
        for value in range(2, n + 1):
            positions = [index for index, current in enumerate(sequence) if current == value]
            assert len(positions) == 2
            assert positions[1] - positions[0] == value


def test_job_assignment_bounded_domain_matches_exhaustive_canonical_instances() -> None:
    from itertools import combinations_with_replacement, product

    minimum_time = _reference_solve("1723")

    def exhaustive(jobs: tuple[int, ...], worker_count: int) -> int:
        best = sum(jobs)
        for assignment in product(range(worker_count), repeat=len(jobs)):
            workloads = [0] * worker_count
            for duration, worker in zip(jobs, assignment):
                workloads[worker] += duration
            best = min(best, max(workloads))
        return best

    for job_count in range(1, 7):
        for jobs in combinations_with_replacement(range(1, 5), job_count):
            for worker_count in range(1, job_count + 1):
                assert minimum_time(list(jobs), worker_count) == exhaustive(jobs, worker_count)

    assert minimum_time([10_000_000] * 12, 6) == 20_000_000
    assert minimum_time(list(range(1, 13)), 12) == 12


def test_string_halves_certificate_matches_exhaustive_case_sensitive_counts() -> None:
    from itertools import product

    solve = _reference_solve("1704")
    vowels = set("aeiouAEIOU")
    alphabet = "aAbB"

    for length in (2, 4, 6):
        middle = length // 2
        for characters in product(alphabet, repeat=length):
            value = "".join(characters)
            expected = sum(c in vowels for c in value[:middle]) == sum(
                c in vowels for c in value[middle:]
            )
            assert solve(value) is expected


def test_ball_fall_certificate_matches_recursive_simulation_on_small_grids() -> None:
    from itertools import product

    solve = _reference_solve("1706")

    def expected(grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        columns = len(grid[0])

        def fall(row: int, column: int) -> int:
            if row == rows:
                return column
            next_column = column + grid[row][column]
            if (
                next_column < 0
                or next_column >= columns
                or grid[row][next_column] != grid[row][column]
            ):
                return -1
            return fall(row + 1, next_column)

        return [fall(0, column) for column in range(columns)]

    for rows in range(1, 4):
        for columns in range(1, 4):
            for values in product((-1, 1), repeat=rows * columns):
                grid = [
                    list(values[row * columns : (row + 1) * columns])
                    for row in range(rows)
                ]
                assert solve(grid) == expected(grid)


def test_days_together_certificate_covers_fixed_calendar_domain() -> None:
    solve = _reference_solve("2409")
    month_lengths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dates = [
        f"{month:02d}-{day:02d}"
        for month, length in enumerate(month_lengths, start=1)
        for day in range(1, length + 1)
    ]

    for alice_day, alice_date in enumerate(dates, start=1):
        for bob_day, bob_date in enumerate(dates, start=1):
            assert solve(alice_date, alice_date, bob_date, bob_date) == (
                1 if alice_day == bob_day else 0
            )

    for start in range(1, 366):
        for end in range(start, 366):
            arrive = dates[start - 1]
            leave = dates[end - 1]
            assert solve(arrive, leave, "01-01", "12-31") == end - start + 1
            assert solve(arrive, leave, "01-01", "01-01") == (1 if start == 1 else 0)
            assert solve(arrive, leave, "12-31", "12-31") == (1 if end == 365 else 0)

    state = 2409
    for _ in range(20_000):
        ordinals = []
        for _field in range(4):
            state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
            ordinals.append(state % 365 + 1)
        alice_start, alice_end = sorted(ordinals[:2])
        bob_start, bob_end = sorted(ordinals[2:])
        expected = len(
            set(range(alice_start, alice_end + 1))
            & set(range(bob_start, bob_end + 1))
        )
        assert solve(
            dates[alice_start - 1],
            dates[alice_end - 1],
            dates[bob_start - 1],
            dates[bob_end - 1],
        ) == expected


def test_smallest_even_multiple_certificate_covers_every_legal_input() -> None:
    solve = _reference_solve("2413")

    for n in range(1, 151):
        candidate = n
        while candidate % 2 != 0:
            candidate += n
        assert solve(n) == candidate


def test_hourglass_maximum_matches_independent_mask_oracle() -> None:
    solve = _reference_solve("2428")
    offsets = (
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, 1),
        (2, 2),
    )

    def oracle(grid: list[list[int]]) -> int:
        return max(
            sum(grid[row + row_offset][column + column_offset] for row_offset, column_offset in offsets)
            for row in range(len(grid) - 2)
            for column in range(len(grid[0]) - 2)
        )

    for values in product(range(2), repeat=9):
        grid = [list(values[offset:offset + 3]) for offset in range(0, 9, 3)]
        assert solve(grid) == oracle(grid)

    state = 2428
    for rows in range(3, 9):
        for columns in range(3, 9):
            for _ in range(20):
                grid = []
                for _row in range(rows):
                    current = []
                    for _column in range(columns):
                        state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
                        current.append(state % 1001)
                    grid.append(current)
                assert solve(grid) == oracle(grid)


def test_minimize_xor_bounded_domain_matches_independent_oracles() -> None:
    solve = _reference_solve("2429")

    candidates_by_count = {
        count: [
            candidate
            for candidate in range(1, 1 << 8)
            if candidate.bit_count() == count
        ]
        for count in range(1, 8)
    }
    for num1 in range(1, 1 << 7):
        for num2 in range(1, 1 << 7):
            expected = min(
                candidates_by_count[num2.bit_count()],
                key=lambda candidate: candidate ^ num1,
            )
            assert solve(num1, num2) == expected

    def bit_cost_oracle(num1: int, num2: int) -> int:
        costs = [
            (-(1 << bit) if num1 & (1 << bit) else 1 << bit, bit)
            for bit in range(30)
        ]
        return sum(
            1 << bit
            for _cost, bit in sorted(costs)[: num2.bit_count()]
        )

    values = {
        1,
        2,
        3,
        (1 << 29) - 1,
        1 << 29,
        10**9 - 1,
        10**9,
    }
    state = 2429
    pairs = [(left, right) for left in values for right in values]
    for _ in range(20_000):
        state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
        num1 = state % 10**9 + 1
        state = (1_103_515_245 * state + 12_345) & 0x7FFFFFFF
        num2 = state % 10**9 + 1
        pairs.append((num1, num2))

    for num1, num2 in pairs:
        result = solve(num1, num2)
        assert result.bit_count() == num2.bit_count()
        assert result == bit_cost_oracle(num1, num2)


def test_valid_clock_times_certificate_covers_every_legal_pattern() -> None:
    count_time = _reference_solve("2437")
    expected_counts: dict[str, int] = {}
    digit_positions = (0, 1, 3, 4)

    for hour in range(24):
        for minute in range(60):
            concrete = f"{hour:02d}:{minute:02d}"
            for mask in range(1 << len(digit_positions)):
                pattern = list(concrete)
                for bit, position in enumerate(digit_positions):
                    if mask & (1 << bit):
                        pattern[position] = "?"
                value = "".join(pattern)
                expected_counts[value] = expected_counts.get(value, 0) + 1

    assert len(expected_counts) == 2926
    for pattern, expected in expected_counts.items():
        assert count_time(pattern) == expected


def test_event_conflict_certificate_covers_clock_order_and_interval_relations() -> None:
    have_conflict = _reference_solve("2446")
    minute_labels = [f"{minute // 60:02d}:{minute % 60:02d}" for minute in range(1440)]

    for first_index, first in enumerate(minute_labels):
        first_event = [first, first]
        for second_index, second in enumerate(minute_labels):
            assert have_conflict(first_event, [second, second]) == (first_index == second_index)

    reduced_labels = minute_labels[:12]
    intervals = [
        [reduced_labels[start], reduced_labels[end]]
        for start in range(len(reduced_labels))
        for end in range(start, len(reduced_labels))
    ]
    for first in intervals:
        first_start = reduced_labels.index(first[0])
        first_end = reduced_labels.index(first[1])
        for second in intervals:
            second_start = reduced_labels.index(second[0])
            second_end = reduced_labels.index(second[1])
            expected = max(first_start, second_start) <= min(first_end, second_end)
            assert have_conflict(first, second) == expected

    assert have_conflict(["00:00", "23:59"], ["00:00", "00:00"])
    assert have_conflict(["00:00", "23:59"], ["23:59", "23:59"])


def test_permutation_difference_matches_independent_index_oracle() -> None:
    permutation_difference = _reference_solve("3146")

    def oracle(s: str, t: str) -> int:
        return sum(abs(s.index(character) - t.index(character)) for character in s)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for length in range(1, 10):
        s = alphabet[:length]
        for order in permutations(s):
            t = "".join(order)
            assert permutation_difference(s, t) == oracle(s, t)

    rng = random.Random(3146)
    for _ in range(100_000):
        length = rng.randint(1, 26)
        s = "".join(rng.sample(alphabet, length))
        t_chars = list(s)
        rng.shuffle(t_chars)
        t = "".join(t_chars)
        assert permutation_difference(s, t) == oracle(s, t)


def test_adjacent_digit_differences_matches_exhaustive_numeric_oracle() -> None:
    solve = _reference_solve("3931")
    package = leetcode_package_dir("lc_3931")
    assert package is not None
    native_path = (
        package / "variants" / "optimal" / "solutions" / "leetcode.py"
    )
    namespace: dict[str, object] = {}
    source = native_path.read_text(encoding="utf-8")
    exec(compile(source, str(native_path), "exec"), namespace)  # noqa: S102
    native = namespace["Solution"]().isAdjacentDiffAtMostTwo

    for length in range(2, 6):
        for digits in product("0123456789", repeat=length):
            s = "".join(digits)
            expected = all(
                abs(int(left) - int(right)) <= 2
                for left, right in zip(s, s[1:], strict=False)
            )
            assert solve(s) is expected
            assert native(s) is expected


def test_all_non_scaling_certificates_are_strictly_valid() -> None:
    for frontend_id, method in CERTIFIED_METHODS.items():
        status = leetcode_complexity_certificate_status(f"lc_{frontend_id}")
        assert status.complete, (frontend_id, status.errors)
        assert status.method == method
        assert status.required_time.startswith("O(")
        path = leetcode_complexity_certificate_path(f"lc_{frontend_id}")
        assert path is not None and path.is_file()


def test_elapsed_seconds_bounded_domain_matches_fixed_position_oracle() -> None:
    elapsed_seconds = _reference_solve("3986")
    package = leetcode_package_dir("lc_3986")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_elapsed_seconds = native_namespace["Solution"]().secondsBetweenTimes

    def label(total_seconds: int) -> str:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def oracle(start_time: str, end_time: str) -> int:
        def fixed_position_seconds(time: str) -> int:
            hours = int(time[0:2])
            minutes = int(time[3:5])
            seconds = int(time[6:8])
            return 3600 * hours + 60 * minutes + seconds

        return fixed_position_seconds(end_time) - fixed_position_seconds(start_time)

    first = "00:00:00"
    last = "23:59:59"
    for total_seconds in range(86_400):
        current = label(total_seconds)
        assert elapsed_seconds(first, current) == total_seconds
        assert native_elapsed_seconds(first, current) == total_seconds
        remaining = 86_399 - total_seconds
        assert elapsed_seconds(current, last) == remaining
        assert native_elapsed_seconds(current, last) == remaining

    rng = random.Random(3986)
    for _ in range(100_000):
        start_seconds = rng.randrange(86_400)
        end_seconds = rng.randrange(start_seconds, 86_400)
        start_time = label(start_seconds)
        end_time = label(end_seconds)
        expected = oracle(start_time, end_time)
        assert elapsed_seconds(start_time, end_time) == expected
        assert native_elapsed_seconds(start_time, end_time) == expected

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        start_time = case["input"]["startTime"]
        end_time = case["input"]["endTime"]
        expected = oracle(start_time, end_time)
        assert case["expected"] == expected
        assert elapsed_seconds(start_time, end_time) == expected
        assert native_elapsed_seconds(start_time, end_time) == expected


def test_exact_path_grid_bounded_domain_validates_every_legal_tuple() -> None:
    create_grid = _reference_solve("3988")
    package = leetcode_package_dir("lc_3988")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_create_grid = native_namespace["Solution"]().createGrid

    def path_count(grid: list[str]) -> int:
        if not grid:
            return 0
        columns = len(grid[0])
        paths = [0] * columns
        for row, cells in enumerate(grid):
            for column, cell in enumerate(cells):
                if cell == "#":
                    paths[column] = 0
                elif row == 0 and column == 0:
                    paths[column] = 1
                else:
                    paths[column] += paths[column - 1] if column else 0
        return paths[-1]

    def assert_valid(result: list[str], m: int, n: int, k: int) -> None:
        possible = math.comb(m + n - 2, m - 1) >= k
        assert bool(result) is possible
        if not result:
            return
        assert len(result) == m
        assert all(len(row) == n for row in result)
        assert all(cell in ".#" for row in result for cell in row)
        assert path_count(result) == k

    checked = 0
    for m in range(1, 11):
        for n in range(1, 11):
            for k in range(1, 5):
                assert_valid(create_grid(m, n, k), m, n, k)
                assert_valid(native_create_grid(m, n, k), m, n, k)
                checked += 1
    assert checked == 400


def test_bounded_exact_path_grid_ii_validates_every_legal_input() -> None:
    create_grid = _reference_solve("3990")
    package = leetcode_package_dir("lc_3990")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_create_grid = native_namespace["Solution"]().createGrid

    def path_count(grid: list[str]) -> int:
        columns = len(grid[0])
        paths = [0] * columns
        for row, cells in enumerate(grid):
            for column, cell in enumerate(cells):
                if cell == "#":
                    paths[column] = 0
                elif row == 0 and column == 0:
                    paths[column] = 1
                else:
                    paths[column] += paths[column - 1] if column else 0
        return paths[-1]

    def assert_valid(result: list[str], k: int) -> None:
        assert 1 <= len(result) <= 25
        assert 1 <= len(result[0]) <= 25
        assert all(len(row) == len(result[0]) for row in result)
        assert all(cell in ".#" for row in result for cell in row)
        assert path_count(result) == k

    for k in range(1, 1_001):
        assert_valid(create_grid(k), k)
        assert_valid(native_create_grid(k), k)

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    assert len(cases) == 20
    for case in cases:
        assert_valid(case["expected"], case["input"]["k"])


def test_digit_frequency_score_bounded_domain_matches_decimal_oracle() -> None:
    digit_frequency_score = _reference_solve("3945")

    for value in range(1, 1_000_001):
        expected = sum(int(digit) for digit in str(value))
        assert digit_frequency_score(value) == expected

    rng = random.Random(3945)
    for _ in range(50_000):
        value = rng.randint(1, 1_000_000_000)
        expected = sum(int(digit) for digit in str(value))
        assert digit_frequency_score(value) == expected

    assert digit_frequency_score(1_000_000_000) == 1


def test_exactly_one_consecutive_set_bits_matches_complete_domain_oracle() -> None:
    solve = _reference_solve("3950")
    package = leetcode_package_dir("lc_3950")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().consecutiveSetBits

    for value in range(100_001):
        bits = f"{value:b}"
        expected = (
            sum(
                left == right == "1"
                for left, right in zip(bits, bits[1:], strict=False)
            )
            == 1
        )
        assert solve(value) is expected
        assert native(value) is expected


def test_compatible_numbers_in_range_matches_complete_domain_oracle() -> None:
    solve = _reference_solve("3954")
    package = leetcode_package_dir("lc_3954")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().sumOfGoodIntegers

    for n in range(1, 101):
        for k in range(1, 101):
            expected = sum(
                value
                for value in range(1, 201)
                if abs(n - value) <= k and n & value == 0
            )
            assert solve(n, k) == expected
            assert native(n, k) == expected


def test_valid_binary_strings_matches_complete_domain_oracle() -> None:
    solve = _reference_solve("3955")
    package = leetcode_package_dir("lc_3955")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().generateValidStrings

    checked = 0
    for n in range(1, 13):
        for k in range(n * (n - 1) // 2 + 1):
            expected = {
                "".join(bits)
                for bits in product("01", repeat=n)
                if "11" not in "".join(bits)
                and sum(index for index, bit in enumerate(bits) if bit == "1") <= k
            }
            for actual in (solve(n, k), native(n, k)):
                assert len(actual) == len(set(actual))
                assert set(actual) == expected
            checked += 1

    assert checked == 298


def test_check_good_integer_matches_decimal_digit_oracle() -> None:
    solve = _reference_solve("3959")
    package = leetcode_package_dir("lc_3959")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().checkGoodInteger

    def oracle(value: int) -> bool:
        digits = [int(digit) for digit in str(value)]
        return sum(digit * digit - digit for digit in digits) >= 50

    for value in range(1, 1_000_001):
        expected = oracle(value)
        assert solve(value) is expected
        assert native(value) is expected

    boundaries = [1, 9, 10, 19, 73, 732, 999_999_999, 1_000_000_000]
    for value in boundaries:
        expected = oracle(value)
        assert solve(value) is expected
        assert native(value) is expected


def test_create_grid_has_exactly_one_path_for_every_legal_dimension() -> None:
    solve = _reference_solve("3963")
    package = leetcode_package_dir("lc_3963")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().createGrid

    def path_count(grid: list[str], rows: int, columns: int) -> int:
        assert len(grid) == rows
        assert all(len(row) == columns and set(row) <= {".", "#"} for row in grid)
        paths = [0] * columns
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "#":
                    paths[column] = 0
                elif row == 0 and column == 0:
                    paths[column] = 1
                else:
                    paths[column] += paths[column - 1] if column else 0
        return paths[-1]

    for rows in range(1, 26):
        for columns in range(1, 26):
            assert path_count(solve(rows, columns), rows, columns) == 1
            assert path_count(native(rows, columns), rows, columns) == 1


def test_good_integer_range_count_matches_enumeration_and_digit_recurrence() -> None:
    solve = _reference_solve("3966")
    package = leetcode_package_dir("lc_3966")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native = native_namespace["Solution"]().goodIntegers

    def is_good(value: int, limit: int) -> bool:
        digits = str(value)
        return all(
            abs(int(left) - int(right)) <= limit
            for left, right in zip(digits, digits[1:])
        )

    for limit in range(10):
        prefix = 0
        for value in range(1, 2001):
            prefix += int(is_good(value, limit))
            if value >= 10:
                expected = prefix - 9
                assert solve(10, value, limit) == expected
                assert native(10, value, limit) == expected

    def iterative_count(bound: int, limit: int) -> int:
        states = {(10, True, False): 1}
        for bound_digit in map(int, str(bound)):
            next_states: dict[tuple[int, bool, bool], int] = {}
            for (previous, tight, started), ways in states.items():
                maximum = bound_digit if tight else 9
                for digit in range(maximum + 1):
                    next_tight = tight and digit == bound_digit
                    if not started and digit == 0:
                        state = (10, next_tight, False)
                    elif not started or abs(previous - digit) <= limit:
                        state = (digit, next_tight, True)
                    else:
                        continue
                    next_states[state] = next_states.get(state, 0) + ways
            states = next_states
        return sum(
            ways
            for (_previous, _tight, started), ways in states.items()
            if started
        )

    boundaries = [10, 99, 100, 101010101010101, 999999999999999, 10**15]
    for limit in range(10):
        for upper in boundaries:
            expected = iterative_count(upper, limit) - 9
            assert solve(10, upper, limit) == expected
            assert native(10, upper, limit) == expected


def test_two_egg_drop_bounded_domain_matches_every_legal_floor_count() -> None:
    solve = _reference_solve("1884")
    moves = 0
    covered = 0

    for floors in range(1, 1001):
        while covered < floors:
            moves += 1
            covered += moves
        assert solve(floors) == moves


def test_check_move_bounded_domain_covers_every_direction_and_span() -> None:
    solve = _reference_solve("1958")
    directions = [
        (row_step, column_step)
        for row_step in (-1, 0, 1)
        for column_step in (-1, 0, 1)
        if (row_step, column_step) != (0, 0)
    ]

    for color in ("B", "W"):
        opposite = "W" if color == "B" else "B"
        for row_step, column_step in directions:
            start_row = 0 if row_step >= 0 else 7
            start_column = 0 if column_step >= 0 else 7
            if row_step == 0:
                start_row = 3
            if column_step == 0:
                start_column = 3

            for span in range(2, 8):
                board = [["." for _ in range(8)] for _ in range(8)]
                for offset in range(1, span):
                    board[
                        start_row + offset * row_step
                    ][
                        start_column + offset * column_step
                    ] = opposite
                end_row = start_row + span * row_step
                end_column = start_column + span * column_step
                board[end_row][end_column] = color

                assert solve(board, start_row, start_column, color)

                board[end_row][end_column] = "."
                assert not solve(board, start_row, start_column, color)


def test_tournament_rounds_bounded_domain_matches_every_legal_pair() -> None:
    solve = _reference_solve("1900")

    @lru_cache(None)
    def oracle(player_count: int, first: int, second: int) -> tuple[int, int]:
        if first + second == player_count + 1:
            return 1, 1

        match_options: list[tuple[tuple[bool, bool], ...]] = []
        for left in range(1, player_count // 2 + 1):
            right = player_count + 1 - left
            if first in (left, right):
                winners = (first,)
            elif second in (left, right):
                winners = (second,)
            else:
                winners = (left, right)
            match_options.append(
                tuple((winner < first, winner < second) for winner in winners)
            )

        if player_count % 2:
            middle = player_count // 2 + 1
            match_options.append((((middle < first), (middle < second)),))

        next_states = {
            (
                1 + sum(contribution[0] for contribution in outcome),
                1 + sum(contribution[1] for contribution in outcome),
            )
            for outcome in product(*match_options)
        }
        child_results = [
            oracle((player_count + 1) // 2, next_first, next_second)
            for next_first, next_second in next_states
        ]
        return (
            1 + min(result[0] for result in child_results),
            1 + max(result[1] for result in child_results),
        )

    for player_count in range(2, 29):
        for first in range(1, player_count):
            for second in range(first + 1, player_count + 1):
                assert solve(player_count, first, second) == list(
                    oracle(player_count, first, second)
                )


def test_full_chess_rounds_bounded_domain_matches_every_clock_pair() -> None:
    solve = _reference_solve("1904")
    clock_text = [f"{minute // 60:02d}:{minute % 60:02d}" for minute in range(1440)]
    round_starts = list(range(0, 2880, 15))
    round_ends = [start + 15 for start in round_starts]

    for login in range(1440):
        for logout in range(1440):
            if login == logout:
                continue
            normalized_logout = logout + (1440 if logout < login else 0)
            expected = max(
                0,
                bisect_right(round_ends, normalized_logout)
                - bisect_left(round_starts, login),
            )
            assert solve(clock_text[login], clock_text[logout]) == expected


def test_matrix_rotation_optimality_matches_physical_rotations() -> None:
    solve = _reference_solve("1886")

    def matrix(bits: tuple[int, ...], size: int) -> list[list[int]]:
        return [
            list(bits[row * size : (row + 1) * size])
            for row in range(size)
        ]

    def rotate(grid: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in zip(*grid[::-1])]

    matrices = [matrix(bits, 2) for bits in product((0, 1), repeat=4)]
    for source in matrices:
        rotations = []
        current = source
        for _ in range(4):
            rotations.append(current)
            current = rotate(current)
        for target in matrices:
            assert solve(source, target) is (target in rotations)


def test_missing_binary_string_optimality_constructs_an_absent_value() -> None:
    solve = _reference_solve("1980")

    for length in range(1, 4):
        values = [format(value, f"0{length}b") for value in range(1 << length)]
        for originals in permutations(values, length):
            actual = solve(list(originals))
            assert len(actual) == length
            assert set(actual) <= {"0", "1"}
            assert actual not in originals

    maximum_case = [format(value, "016b") for value in range(16)]
    maximum_actual = solve(maximum_case)
    assert len(maximum_actual) == 16
    assert maximum_actual not in maximum_case


def test_sorted_vowel_formula_matches_dynamic_program_for_complete_domain() -> None:
    solve = _reference_solve("1641")
    ending_counts = [1] * 5

    for n in range(1, 51):
        if n > 1:
            running = 0
            next_counts = []
            for count in ending_counts:
                running += count
                next_counts.append(running)
            ending_counts = next_counts
        assert solve(n) == sum(ending_counts)


def test_kth_instruction_unranking_matches_enumeration_and_boundaries() -> None:
    from itertools import product

    solve = _reference_solve("1643")
    for row in range(1, 5):
        for column in range(1, 5):
            paths = sorted(
                "".join(path)
                for path in product("HV", repeat=row + column)
                if path.count("H") == column
            )
            for k, expected in enumerate(paths, 1):
                assert solve([row, column], k) == expected

    boundary_count = math.comb(30, 15)
    assert solve([15, 15], 1) == "H" * 15 + "V" * 15
    assert solve([15, 15], boundary_count) == "V" * 15 + "H" * 15


def test_hopper_working_percentages_match_independent_calendar_oracle() -> None:
    package = leetcode_package_dir("lc_1645")
    assert package is not None
    source = _reference_source("1645", "sql")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))

    for case in payload["cases"]:
        tables = case["input"]["tables"]
        rides = {ride["ride_id"]: ride for ride in tables["Rides"]}
        rows = []
        for month in range(1, 13):
            cutoff = date(2021, 1, 1) if month == 12 else date(2020, month + 1, 1)
            active = sum(
                date.fromisoformat(driver["join_date"]) < cutoff
                for driver in tables["Drivers"]
            )
            working = {
                accepted["driver_id"]
                for accepted in tables["AcceptedRides"]
                if accepted["ride_id"] in rides
                and date.fromisoformat(rides[accepted["ride_id"]]["requested_at"]).year == 2020
                and date.fromisoformat(rides[accepted["ride_id"]]["requested_at"]).month == month
            }
            percentage = round(100.0 * len(working) / active, 2) if active else 0.0
            rows.append([month, percentage])

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, (case["id"], result.error_message)
        assert result.value == {
            "columns": ["month", "working_percentage"],
            "rows": rows,
        }


def test_hopper_three_month_averages_match_independent_calendar_oracle() -> None:
    package = leetcode_package_dir("lc_1651")
    assert package is not None
    source = _reference_source("1651", "sql")
    payload = json.loads((package / "cases.json").read_text(encoding="utf-8"))

    for case in payload["cases"]:
        tables = case["input"]["tables"]
        rides = {ride["ride_id"]: ride for ride in tables["Rides"]}
        distances = [0] * 12
        durations = [0] * 12
        for accepted in tables["AcceptedRides"]:
            ride = rides[accepted["ride_id"]]
            requested_at = date.fromisoformat(ride["requested_at"])
            if requested_at.year != 2020:
                continue
            index = requested_at.month - 1
            distances[index] += accepted["ride_distance"]
            durations[index] += accepted["ride_duration"]

        rows = [
            [
                month + 1,
                round(sum(distances[month:month + 3]) / 3.0, 2),
                round(sum(durations[month:month + 3]) / 3.0, 2),
            ]
            for month in range(10)
        ]
        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, (case["id"], result.error_message)
        assert result.value == {
            "columns": ["month", "average_ride_distance", "average_ride_duration"],
            "rows": rows,
        }


def test_generated_array_maximum_matches_recursive_oracle_for_complete_domain() -> None:
    from functools import lru_cache

    solve = _reference_solve("1646")

    @lru_cache(maxsize=None)
    def value(index: int) -> int:
        if index <= 1:
            return index
        half = index // 2
        return value(half) if index % 2 == 0 else value(half) + value(half + 1)

    for n in range(101):
        assert solve(n) == max(value(index) for index in range(n + 1))


def test_certificate_validator_rejects_a_generic_waiver() -> None:
    status = validate_complexity_certificate(
        {
            "schema_version": 1,
            "challenge_id": "lc_1",
            "status": "verified",
            "method": "bounded_domain",
            "required_time": "O(1)",
            "summary": "This deliberately incomplete certificate must never become a generic waiver.",
            "replacement_checks": [],
        },
        expected_challenge_id="lc_1",
    )
    assert not status.complete
    assert any("workload_bound" in error for error in status.errors)
    assert any("replacement_checks" in error for error in status.errors)


def test_hit_counter_certificate_covers_window_and_call_boundaries() -> None:
    solve = _reference_solve("362")
    package = leetcode_package_dir("lc_362")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_counter = native_namespace["HitCounter"]

    def run_native(operations: list[list]) -> list[int]:
        counter = native_counter()
        results: list[int] = []
        for name, timestamp in operations:
            if name == "hit":
                counter.hit(timestamp)
            else:
                results.append(counter.getHits(timestamp))
        return results

    no_hits = [["getHits", 1]]
    assert solve(no_hits) == [0]
    assert run_native(no_hits) == [0]

    start = 1000
    for age in range(301):
        operations = [["hit", start], ["getHits", start + age]]
        expected = [int(age < 300)]
        assert solve(operations) == expected
        assert run_native(operations) == expected

    reused_slot = [["hit", 1], ["hit", 301], ["getHits", 301]]
    assert solve(reused_slot) == [1]
    assert run_native(reused_slot) == [1]

    maximum_burst = [["hit", 2_000_000_000] for _ in range(299)]
    maximum_burst.append(["getHits", 2_000_000_000])
    assert solve(maximum_burst) == [299]
    assert run_native(maximum_burst) == [299]


def test_shuffle_array_certificate_covers_length_and_call_boundaries() -> None:
    package = leetcode_package_dir("lc_384")
    assert package is not None

    source_paths = (
        (package / "variants" / "optimal" / "solutions" / "solve.py", {}),
        (
            package / "variants" / "optimal" / "solutions" / "leetcode.py",
            {"List": list},
        ),
    )
    values = list(range(-25, 25))

    for source_path, init_globals in source_paths:
        if not source_path.is_file():
            continue
        namespace = _run_native_module(str(source_path), init_globals=init_globals)
        solution_type = namespace["Solution"]

        single = solution_type([7])
        assert single.shuffle() == [7]
        assert single.reset() == [7]

        solution = solution_type(values)
        reset_result = solution.reset()
        assert reset_result == values
        reset_result[0] = 1_000_000
        assert solution.reset() == values

        choices: list[tuple[int, int]] = []

        def choose_last(i: int, stop: int) -> int:
            choices.append((i, stop))
            return stop - 1

        shuffle_globals = solution.shuffle.__func__.__globals__
        shuffle_globals["randrange"] = choose_last
        expected = values.copy()
        for i in range(len(expected) - 1):
            expected[i], expected[-1] = expected[-1], expected[i]
        assert solution.shuffle() == expected
        assert choices == [(i, len(values)) for i in range(len(values) - 1)]

        shuffle_globals["randrange"] = lambda i, _stop: i
        for call in range(10_000):
            result = solution.shuffle() if call % 2 == 0 else solution.reset()
            assert result == values


def test_small_finite_domains_are_exhaustively_verified() -> None:
    binary_watch = _reference_solve("401")
    for turned_on in range(11):
        expected = [
            f"{hour}:{minute:02d}"
            for hour in range(12)
            for minute in range(60)
            if hour.bit_count() + minute.bit_count() == turned_on
        ]
        assert binary_watch(turned_on) == expected

    palindrome = _reference_solve("479")
    expected_residues = (9, 987, 123, 597, 677, 1218, 877, 475)
    assert tuple(palindrome(n) for n in range(1, 9)) == expected_residues

    days_in_month = _reference_solve("1118")
    for year in range(1583, 2101):
        for month in range(1, 13):
            assert days_in_month(year, month) == calendar.monthrange(year, month)[1]

    tribonacci = _reference_solve("1137")
    values = [0, 1, 1]
    for _ in range(3, 38):
        values.append(sum(values[-3:]))
    assert [tribonacci(n) for n in range(38)] == values

    day_of_year = _reference_solve("1154")
    current = date(1900, 1, 1)
    end = date(2019, 12, 31)
    while current <= end:
        assert day_of_year(current.isoformat()) == current.timetuple().tm_yday
        current += timedelta(days=1)


def test_armstrong_number_bounded_domain_matches_decimal_string_oracle() -> None:
    is_armstrong = _reference_solve("1134")
    package = leetcode_package_dir("lc_1134")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_is_armstrong = native_namespace["Solution"]().isArmstrong

    def oracle(value: int) -> bool:
        digits = str(value)
        exponent = len(digits)
        return sum(int(digit) ** exponent for digit in digits) == value

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        value = case["input"]["n"]
        expected = oracle(value)
        assert case["expected"] is expected
        assert is_armstrong(value) is expected
        assert native_is_armstrong(value) is expected

    boundaries: set[int] = {1, 100_000_000}
    for exponent in range(1, 9):
        lower = 1 if exponent == 1 else 10 ** (exponent - 1)
        upper = 10**exponent - 1
        boundaries.update((lower, lower + 1, upper - 1, upper))
    boundaries.update(
        {
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            153, 370, 371, 407,
            1_634, 8_208, 9_474,
            54_748, 92_727, 93_084,
            548_834,
            1_741_725, 4_210_818, 9_800_817, 9_926_315,
            24_678_050, 24_678_051, 88_593_477,
        }
    )
    for value in sorted(boundaries):
        expected = oracle(value)
        assert is_armstrong(value) is expected
        assert native_is_armstrong(value) is expected

    rng = random.Random(1134)
    for _ in range(20_000):
        value = rng.randint(1, 100_000_000)
        expected = oracle(value)
        assert is_armstrong(value) is expected
        assert native_is_armstrong(value) is expected


def test_similar_rgb_bounded_domain_matches_every_channel_byte() -> None:
    similar_rgb = _reference_solve("800")
    package = leetcode_package_dir("lc_800")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_similar_rgb = native_namespace["Solution"]().similarRGB

    def channel_oracle(value: int) -> int:
        return min(range(0, 256, 17), key=lambda candidate: abs(value - candidate))

    def color_oracle(color: str) -> str:
        channels = (
            channel_oracle(int(color[start : start + 2], 16))
            for start in (1, 3, 5)
        )
        return "#" + "".join(f"{channel:02x}" for channel in channels)

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        color = case["input"]["color"]
        expected = color_oracle(color)
        assert case["expected"] == expected
        assert similar_rgb(color) == expected
        assert native_similar_rgb(color) == expected

    for value in range(256):
        digits = f"{value:02x}"
        for color in (f"#{digits}0000", f"#00{digits}00", f"#0000{digits}"):
            expected = color_oracle(color)
            assert similar_rgb(color) == expected
            assert native_similar_rgb(color) == expected


def test_confusing_number_bounded_domain_matches_rotation_oracle() -> None:
    confusing_number = _reference_solve("1056")
    package = leetcode_package_dir("lc_1056")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_confusing_number = native_namespace["Solution"]().confusingNumber
    rotated_digit = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    def oracle(n: int) -> bool:
        digits = str(n)
        if any(digit not in rotated_digit for digit in digits):
            return False
        rotated = int("".join(rotated_digit[digit] for digit in reversed(digits)))
        return rotated != n

    def assert_matches(n: int) -> None:
        expected = oracle(n)
        assert confusing_number(n) is expected
        assert native_confusing_number(n) is expected

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        n = case["input"]["n"]
        expected = oracle(n)
        assert case["expected"] is expected
        assert_matches(n)

    for n in range(100_000):
        assert_matches(n)

    for length in range(1, 10):
        for position in range(length):
            for invalid_digit in "23457":
                digits = ["1"] * length
                digits[position] = invalid_digit
                assert_matches(int("".join(digits)))

    rng = random.Random(1056)
    for _ in range(10_000):
        assert_matches(rng.randint(0, 10**9))


def test_clock_angle_bounded_domain_matches_exact_half_degree_oracle() -> None:
    angle_clock = _reference_solve("1344")
    for hour in range(1, 13):
        for minutes in range(60):
            hour_position = (hour % 12) * 60 + minutes
            minute_position = minutes * 12
            half_degree_difference = abs(hour_position - minute_position)
            expected = min(half_degree_difference, 720 - half_degree_difference) / 2
            assert angle_clock(hour, minutes) == expected


def test_reformat_date_bounded_domain_matches_every_valid_date() -> None:
    reformat_date = _reference_solve("1507")
    month_names = (
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    )

    def suffix(day: int) -> str:
        if 10 < day % 100 < 14:
            return "th"
        return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    current = date(1900, 1, 1)
    end = date(2100, 12, 31)
    while current <= end:
        source = f"{current.day}{suffix(current.day)} {month_names[current.month - 1]} {current.year}"
        assert reformat_date(source) == current.isoformat()
        current += timedelta(days=1)


def test_water_bottles_bounded_domain_matches_every_legal_pair() -> None:
    water_bottles = _reference_solve("1518")

    for num_bottles in range(1, 101):
        for num_exchange in range(2, 101):
            full = num_bottles
            empty = 0
            expected = 0
            while full:
                expected += full
                empty += full
                full, empty = divmod(empty, num_exchange)
            assert water_bottles(num_bottles, num_exchange) == expected


def test_thousand_separator_bounded_domain_matches_forward_grouping_oracle() -> None:
    thousand_separator = _reference_solve("1556")

    def expected(value: int) -> str:
        digits = str(value)
        first_group_width = len(digits) % 3 or 3
        result = digits[:first_group_width]
        for index in range(first_group_width, len(digits), 3):
            result += "." + digits[index:index + 3]
        return result

    values = set(range(100_001))
    values.add(2**31 - 1)
    for power in range(1, 10):
        boundary = 10**power
        values.update({boundary - 1, boundary, min(boundary + 1, 2**31 - 1)})

    state = 1_556
    for _ in range(10_000):
        state = (1_103_515_245 * state + 12_345) % (2**31)
        values.add(state)

    for value in sorted(values):
        actual = thousand_separator(value)
        assert actual == expected(value)
        assert actual.replace(".", "") == str(value)
        groups = actual.split(".")
        assert 1 <= len(groups[0]) <= 3
        assert all(len(group) == 3 for group in groups[1:])


def test_max_difference_bounded_domain_matches_digit_pair_oracle() -> None:
    max_difference = _reference_solve("1432")

    def expected(num: int) -> int:
        digits = str(num)
        results = []
        for source in "0123456789":
            for replacement in "0123456789":
                changed = digits.replace(source, replacement)
                if changed[0] != "0":
                    results.append(int(changed))
        return max(results) - min(results)

    values = set(range(1, 10_000))
    values.update({10_000, 10_001, 90_909, 9_999_999, 99_999_999, 100_000_000})
    for value in sorted(values):
        assert max_difference(value) == expected(value)


def test_average_salary_bounded_domain_matches_sort_and_slice_oracle() -> None:
    average_salary = _reference_solve("1491")

    for length in range(3, 101):
        values = [1000 + index * 7919 for index in range(length)]
        if length % 2 == 0:
            values.reverse()
        else:
            offset = length // 2
            values = values[offset:] + values[:offset]

        ordered = sorted(values)
        expected = sum(ordered[1:-1]) / (length - 2)
        assert abs(average_salary(values) - expected) <= 1e-12

    boundary_fixtures = [
        [1000, 1001, 1_000_000],
        [1_000_000, 1000, 999_999, 1001, 500_000],
        [4000, 3000, 1000, 2000],
        [1000, 2000, 3001, 9000],
    ]
    for values in boundary_fixtures:
        ordered = sorted(values)
        expected = sum(ordered[1:-1]) / (len(values) - 2)
        assert abs(average_salary(values) - expected) <= 1e-12


def test_network_quality_bounded_domain_matches_full_grid_oracle() -> None:
    best_coordinate = _reference_solve("1620")

    def expected(towers: list[list[int]], radius: int) -> list[int]:
        best = [0, 0]
        best_quality = -1
        radius_squared = radius * radius
        for x in range(51):
            for y in range(51):
                quality = 0
                for tower_x, tower_y, tower_quality in towers:
                    distance_squared = (x - tower_x) ** 2 + (y - tower_y) ** 2
                    if distance_squared <= radius_squared:
                        quality += math.floor(
                            tower_quality / (1 + math.sqrt(distance_squared))
                        )
                if quality > best_quality:
                    best_quality = quality
                    best = [x, y]
        return best

    fixtures = [
        ([[50, 50, 0]], 1),
        ([[0, 0, 10], [2, 0, 10]], 1),
        ([[0, 0, 20], [3, 4, 20]], 5),
        ([[50, 50, 50], [0, 0, 1]], 50),
    ]
    state = 1_620
    for fixture_index in range(24):
        towers = []
        for _ in range(1 + fixture_index % 8):
            state = (1_103_515_245 * state + 12_345) % (2**31)
            x = state % 51
            state = (1_103_515_245 * state + 12_345) % (2**31)
            y = state % 51
            state = (1_103_515_245 * state + 12_345) % (2**31)
            quality = state % 51
            towers.append([x, y, quality])
        fixtures.append((towers, 1 + fixture_index % 50))

    for towers, radius in fixtures:
        assert best_coordinate(towers, radius) == expected(towers, radius)


def test_valid_country_triplets_matches_cartesian_oracle() -> None:
    package = leetcode_package_dir("lc_1623")
    assert package is not None
    source = _reference_source("1623", "sql")

    fixtures = [
        {
            "SchoolA": [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}],
            "SchoolB": [{"student_id": 3, "student_name": "Tom"}],
            "SchoolC": [{"student_id": 3, "student_name": "Tom"}, {"student_id": 2, "student_name": "Jerry"}, {"student_id": 10, "student_name": "Alice"}],
        },
        {
            "SchoolA": [{"student_id": 1, "student_name": "A1"}, {"student_id": 2, "student_name": "A2"}],
            "SchoolB": [{"student_id": 3, "student_name": "B1"}, {"student_id": 4, "student_name": "B2"}],
            "SchoolC": [{"student_id": 5, "student_name": "C1"}, {"student_id": 6, "student_name": "C2"}],
        },
        {
            "SchoolA": [{"student_id": 7, "student_name": "Same"}],
            "SchoolB": [{"student_id": 8, "student_name": "Other"}],
            "SchoolC": [{"student_id": 7, "student_name": "Third"}, {"student_id": 9, "student_name": "Same"}],
        },
    ]

    for tables in fixtures:
        expected = sorted(
            [a["student_name"], b["student_name"], c["student_name"]]
            for a in tables["SchoolA"]
            for b in tables["SchoolB"]
            for c in tables["SchoolC"]
            if len({a["student_id"], b["student_id"], c["student_id"]}) == 3
            and len({a["student_name"], b["student_name"], c["student_name"]}) == 3
        )
        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": ["member_A", "member_B", "member_C"],
            "rows": expected,
        }


def test_contest_percentages_match_independent_counter_oracle() -> None:
    package = leetcode_package_dir("lc_1633")
    assert package is not None
    source = _reference_source("1633", "sql")

    fixtures = [
        {
            "Users": [
                {"user_id": 1, "user_name": "A"},
                {"user_id": 2, "user_name": "B"},
                {"user_id": 3, "user_name": "C"},
            ],
            "Register": [
                {"contest_id": 9, "user_id": 1},
                {"contest_id": 9, "user_id": 3},
                {"contest_id": 2, "user_id": 2},
            ],
        },
        {
            "Users": [
                {"user_id": index, "user_name": f"U{index}"}
                for index in range(1, 7)
            ],
            "Register": [
                *({"contest_id": 4, "user_id": index} for index in range(1, 6)),
                {"contest_id": 1, "user_id": 6},
                {"contest_id": 7, "user_id": 1},
            ],
        },
        {
            "Users": [
                {"user_id": index, "user_name": f"U{index}"}
                for index in range(1, 5)
            ],
            "Register": [
                {"contest_id": 30, "user_id": 1},
                {"contest_id": 10, "user_id": 2},
                {"contest_id": 20, "user_id": 3},
            ],
        },
    ]

    for tables in fixtures:
        counts: dict[int, int] = {}
        for registration in tables["Register"]:
            contest_id = registration["contest_id"]
            counts[contest_id] = counts.get(contest_id, 0) + 1
        user_count = len(tables["Users"])
        expected = [
            [contest_id, round(count * 100.0 / user_count, 2)]
            for contest_id, count in counts.items()
        ]
        expected.sort(key=lambda row: (-row[1], row[0]))

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": ["contest_id", "percentage"],
            "rows": expected,
        }


def test_hopper_monthly_counts_match_independent_calendar_oracle() -> None:
    package = leetcode_package_dir("lc_1635")
    assert package is not None
    source = _reference_source("1635", "sql")

    fixtures = [
        {
            "Drivers": [
                {"driver_id": 1, "join_date": "2019-12-31"},
                {"driver_id": 2, "join_date": "2020-02-01"},
                {"driver_id": 3, "join_date": "2020-12-31"},
                {"driver_id": 4, "join_date": "2021-01-01"},
            ],
            "Rides": [
                {"ride_id": 10, "user_id": 1, "requested_at": "2020-02-29"},
                {"ride_id": 11, "user_id": 2, "requested_at": "2020-03-01"},
                {"ride_id": 12, "user_id": 3, "requested_at": "2021-01-01"},
            ],
            "AcceptedRides": [
                {"ride_id": 10, "driver_id": 1, "ride_distance": 5, "ride_duration": 6},
                {"ride_id": 12, "driver_id": 2, "ride_distance": 7, "ride_duration": 8},
            ],
        },
        {
            "Drivers": [
                {"driver_id": 1, "join_date": "2020-07-01"},
                {"driver_id": 2, "join_date": "2022-01-01"},
            ],
            "Rides": [
                {"ride_id": 1, "user_id": 1, "requested_at": "2020-07-01"},
                {"ride_id": 2, "user_id": 2, "requested_at": "2020-07-31"},
                {"ride_id": 3, "user_id": 3, "requested_at": "2020-08-01"},
            ],
            "AcceptedRides": [
                {"ride_id": ride_id, "driver_id": 1, "ride_distance": 1, "ride_duration": 1}
                for ride_id in (1, 2, 3)
            ],
        },
    ]

    for tables in fixtures:
        accepted_ids = {row["ride_id"] for row in tables["AcceptedRides"]}
        expected = []
        for month in range(1, 13):
            next_month = date(2021, 1, 1) if month == 12 else date(2020, month + 1, 1)
            active_drivers = sum(
                date.fromisoformat(row["join_date"]) < next_month
                for row in tables["Drivers"]
            )
            accepted_rides = sum(
                row["ride_id"] in accepted_ids
                and date.fromisoformat(row["requested_at"]).year == 2020
                and date.fromisoformat(row["requested_at"]).month == month
                for row in tables["Rides"]
            )
            expected.append([month, active_drivers, accepted_rides])

        result = run_special_environment(
            category="database",
            source=source,
            input_data={"tables": tables},
        )
        assert result.ok, result.error_message
        assert result.value == {
            "columns": ["month", "active_drivers", "accepted_rides"],
            "rows": expected,
        }


def test_circle_rectangle_overlap_matches_axis_gap_oracle() -> None:
    overlaps = _reference_solve("1401")

    for radius in range(1, 5):
        for x_center in range(-4, 5):
            for y_center in range(-4, 5):
                for x1 in range(-3, 3):
                    for x2 in range(x1 + 1, 4):
                        for y1 in range(-3, 3):
                            for y2 in range(y1 + 1, 4):
                                x_gap = max(x1 - x_center, 0, x_center - x2)
                                y_gap = max(y1 - y_center, 0, y_center - y2)
                                expected = x_gap * x_gap + y_gap * y_gap <= radius * radius
                                assert overlaps(
                                    radius,
                                    x_center,
                                    y_center,
                                    x1,
                                    y1,
                                    x2,
                                    y2,
                                ) == expected


def test_temperature_conversion_matches_every_legal_hundredth() -> None:
    convert_temperature = _reference_solve("2469")

    for hundredths in range(100_001):
        celsius = hundredths / 100
        kelvin, fahrenheit = convert_temperature(celsius)
        assert math.isclose(kelvin, celsius + 273.15, abs_tol=1e-12)
        assert math.isclose(fahrenheit, celsius * 1.8 + 32.0, abs_tol=1e-12)


def test_hexspeak_bounded_domain_matches_an_independent_oracle() -> None:
    hexspeak = _reference_solve("1271")

    def expected(value: int) -> str:
        translated = format(value, "X").translate(str.maketrans({"0": "O", "1": "I"}))
        return translated if all(character in "ABCDEFIO" for character in translated) else "ERROR"

    values = set(range(1, 4097))
    values.update(16**power for power in range(10))
    values.update({2827, 64206, 703710, 10**12 - 1, 10**12})
    for value in sorted(values):
        assert hexspeak(str(value)) == expected(value)


def test_number_of_ships_bounded_domain_matches_hidden_points_within_query_cap() -> None:
    count_ships = _reference_solve("1274")
    fixtures = [
        ([], [1000, 1000], [0, 0]),
        ([[0, 0]], [0, 0], [0, 0]),
        ([[0, 0], [0, 1000], [1000, 0], [1000, 1000]], [1000, 1000], [0, 0]),
        ([[500, 0], [500, 17], [500, 499], [500, 1000], [499, 17]], [500, 1000], [500, 0]),
        (
            [[0, 0], [1000, 1000], [0, 1000], [1000, 0], [500, 500], [250, 750],
             [750, 250], [125, 375], [625, 875], [999, 511]],
            [1000, 1000],
            [0, 0],
        ),
    ]
    for ships, top_right, bottom_left in fixtures:
        sea = _JudgeSea(ships)
        expected = sum(
            bottom_left[0] <= x <= top_right[0] and bottom_left[1] <= y <= top_right[1]
            for x, y in ships
        )
        assert count_ships(
            sea,
            _JudgePoint(*top_right),
            _JudgePoint(*bottom_left),
        ) == expected
        assert sea.query_count <= 400


def test_traffic_light_bounded_concurrency_preserves_safety_progress_and_callbacks() -> None:
    source = _reference_source("1279", "python")
    package = leetcode_package_dir("lc_1279")
    assert package is not None
    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    maximum_case = next(case for case in cases if case["id"] == "trial-twenty")

    for case in [*cases, maximum_case, maximum_case, maximum_case]:
        result = run_special_environment(
            category="concurrency",
            source=source,
            input_data=case["input"],
            challenge_id="lc_1279",
            timeout_seconds=3.0,
        )
        assert result.ok, result.error_message
        assert result.value["violations"] == []

        green_road = 1
        crossed = []
        for event in result.value["events"]:
            if event["kind"] == "green":
                assert event["road"] != green_road
                green_road = event["road"]
            else:
                assert event["kind"] == "cross"
                assert event["road"] == green_road
                crossed.append(event["car"])
        assert sorted(crossed) == sorted(case["expected"]["cars"])
        assert len(crossed) == len(case["expected"]["cars"])

    redundant = run_special_environment(
        category="concurrency",
        source="""
class TrafficLight:
    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        turnGreen()
        crossCar()
""",
        input_data={"cars": [1], "directions": [1], "arrival_times": [0]},
        challenge_id="lc_1279",
    )
    assert redundant.ok, redundant.error_message
    assert "redundant-green-change" in redundant.value["violations"]

    unsafe_overlap = run_special_environment(
        category="concurrency",
        source="""
from threading import Barrier

class TrafficLight:
    def __init__(self):
        self.ready = Barrier(2)

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        if roadId == 2:
            turnGreen()
        self.ready.wait()
        crossCar()
""",
        input_data={"cars": [1, 2], "directions": [1, 3], "arrival_times": [0, 0]},
        challenge_id="lc_1279",
    )
    assert unsafe_overlap.ok, unsafe_overlap.error_message
    assert set(unsafe_overlap.value["violations"]) & {"red-road-crossing", "cross-road-overlap"}

    duplicate_crossing = run_special_environment(
        category="concurrency",
        source="""
class TrafficLight:
    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        crossCar()
        crossCar()
""",
        input_data={"cars": [1], "directions": [1], "arrival_times": [0]},
        challenge_id="lc_1279",
    )
    assert duplicate_crossing.ok, duplicate_crossing.error_message
    assert sum(event["kind"] == "cross" for event in duplicate_crossing.value["events"]) == 2
    assert not _traffic_light_match(duplicate_crossing.value, {"cars": [1]})

    missing_crossing = run_special_environment(
        category="concurrency",
        source="""
class TrafficLight:
    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        pass
""",
        input_data={"cars": [1], "directions": [1], "arrival_times": [0]},
        challenge_id="lc_1279",
    )
    assert missing_crossing.ok, missing_crossing.error_message
    assert not _traffic_light_match(missing_crossing.value, {"cars": [1]})

    deadlock = run_special_environment(
        category="concurrency",
        source="""
from threading import Event

class TrafficLight:
    def __init__(self):
        self.never = Event()

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        self.never.wait()
""",
        input_data={"cars": [1], "directions": [1], "arrival_times": [0]},
        challenge_id="lc_1279",
        timeout_seconds=0.2,
    )
    assert not deadlock.ok
    assert "deadlocked or timed out" in deadlock.error_message


def test_tic_tac_toe_bounded_domain_matches_every_reachable_board_state() -> None:
    tictactoe = _reference_solve("1275")
    winning_lines = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
    )

    def expected(board: dict[tuple[int, int], str]) -> str:
        for player in ("A", "B"):
            if any(all(board.get(cell) == player for cell in line) for line in winning_lines):
                return player
        return "Draw" if len(board) == 9 else "Pending"

    pending = [([], {})]
    seen: set[tuple[tuple[int, int, str], ...]] = set()
    while pending:
        moves, board = pending.pop()
        state = tuple(sorted((row, column, player) for (row, column), player in board.items()))
        if state in seen:
            continue
        seen.add(state)
        verdict = expected(board)
        if moves:
            assert tictactoe(moves) == verdict
        if verdict != "Pending":
            continue
        player = "A" if len(moves) % 2 == 0 else "B"
        for row in range(3):
            for column in range(3):
                if (row, column) not in board:
                    pending.append((moves + [[row, column]], {**board, (row, column): player}))


def test_digit_product_minus_sum_matches_every_legal_integer() -> None:
    subtract_product_and_sum = _reference_solve("1281")

    for value in range(1, 100_001):
        digits = [int(character) for character in str(value)]
        product = 1
        for digit in digits:
            product *= digit
        assert subtract_product_and_sum(value) == product - sum(digits)


def test_maximum_69_number_matches_every_legal_digit_string() -> None:
    maximum_69_number = _reference_solve("1323")

    for length in range(1, 5):
        for mask in range(1 << length):
            digits = ["9" if mask & (1 << index) else "6" for index in range(length)]
            value = int("".join(digits))
            candidates = [value]
            for index, digit in enumerate(digits):
                flipped = list(digits)
                flipped[index] = "6" if digit == "9" else "9"
                candidates.append(int("".join(flipped)))
            assert maximum_69_number(value) == max(candidates)


def test_minimum_matrix_flips_matches_every_legal_state() -> None:
    minimum_flips = _reference_solve("1284")

    for rows in range(1, 4):
        for columns in range(1, 4):
            cells = rows * columns
            flip_masks = []
            for row in range(rows):
                for column in range(columns):
                    mask = 0
                    for row_delta, column_delta in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + row_delta
                        next_column = column + column_delta
                        if 0 <= next_row < rows and 0 <= next_column < columns:
                            mask ^= 1 << (next_row * columns + next_column)
                    flip_masks.append(mask)

            expected = [-1] * (1 << cells)
            for subset in range(1 << cells):
                state = 0
                for cell, flip_mask in enumerate(flip_masks):
                    if subset & (1 << cell):
                        state ^= flip_mask
                flips = subset.bit_count()
                if expected[state] == -1 or flips < expected[state]:
                    expected[state] = flips

            for state, answer in enumerate(expected):
                matrix = [
                    [(state >> (row * columns + column)) & 1 for column in range(columns)]
                    for row in range(rows)
                ]
                assert minimum_flips(matrix) == answer


def test_binary_linked_list_conversion_matches_bounded_patterns() -> None:
    decimal_value = _reference_solve("1290")

    for length in range(1, 13):
        for encoded in range(1 << length):
            bits = [
                (encoded >> shift) & 1
                for shift in range(length - 1, -1, -1)
            ]
            assert decimal_value(_list_node_from_values(bits)) == encoded

    boundaries = [
        [0] * 30,
        [1] * 30,
        [1] + [0] * 29,
        [index % 2 for index in range(30)],
        [(index + 1) % 2 for index in range(30)],
    ]
    for bits in boundaries:
        expected = int("".join(map(str, bits)), 2)
        assert decimal_value(_list_node_from_values(bits)) == expected


def test_sequential_digits_matches_every_candidate_boundary_interval() -> None:
    sequential_digits = _reference_solve("1291")
    candidates = []
    for start in range(1, 9):
        value = start
        for next_digit in range(start + 1, 10):
            value = value * 10 + next_digit
            candidates.append(value)
    candidates.sort()

    boundaries = {10, 10**9}
    for value in candidates:
        boundaries.update({max(10, value - 1), value, min(10**9, value + 1)})
    ordered_boundaries = sorted(boundaries)
    for low_index, low in enumerate(ordered_boundaries):
        for high in ordered_boundaries[low_index:]:
            expected = [value for value in candidates if low <= value <= high]
            assert sequential_digits(low, high) == expected


def test_large_integer_reader_binary_search_matches_boundaries_and_query_cap() -> None:
    get_index = _reference_solve("1533")

    for length in range(2, 129):
        for large_index in range(length):
            values = [7] * length
            values[large_index] = 8
            reader = _JudgeArrayReader(values)
            assert get_index(reader) == large_index
            assert reader.query_count <= 20

    samples = [
        (257, 0),
        (257, 128),
        (257, 256),
        (999, 731),
        (65_535, 32_767),
        (500_000, 499_999),
    ]
    for length, large_index in samples:
        values = [99] * length
        values[large_index] = 100
        reader = _JudgeArrayReader(values)
        assert get_index(reader) == large_index
        assert reader.query_count <= 20


def test_hidden_binary_majority_reader_matches_exhaustive_arrays_and_query_cap() -> None:
    from itertools import product

    guess_majority = _reference_solve("1538")

    for length in range(5, 13):
        for values_tuple in product((0, 1), repeat=length):
            values = list(values_tuple)
            reader = _JudgeMajorityReader(values)
            result = guess_majority(reader)
            ones = sum(values)
            zeros = length - ones
            assert reader.query_count <= 2 * length
            if ones == zeros:
                assert result == -1
            else:
                assert 0 <= result < length
                assert values[result] == (1 if ones > zeros else 0)

    values = [1 if index % 2 == 0 else 0 for index in range(100_000)]
    reader = _JudgeMajorityReader(values)
    result = guess_majority(reader)
    assert result == -1
    assert reader.query_count == len(values)


def test_verbal_arithmetic_matches_an_independent_bounded_oracle() -> None:
    is_solvable = _reference_solve("1307")

    def exhaustive_oracle(words: list[str], result: str) -> bool:
        from itertools import permutations

        letters = sorted(set("".join(words) + result))
        leading = {word[0] for word in [*words, result] if len(word) > 1}
        coefficients = {letter: 0 for letter in letters}
        for word in words:
            for place, letter in enumerate(reversed(word)):
                coefficients[letter] += 10**place
        for place, letter in enumerate(reversed(result)):
            coefficients[letter] -= 10**place

        for digits in permutations(range(10), len(letters)):
            values = dict(zip(letters, digits))
            if any(values[letter] == 0 for letter in leading):
                continue
            if sum(coefficients[letter] * values[letter] for letter in letters) == 0:
                return True
        return False

    fixtures = [
        (["A", "B"], "A"),
        (["A", "A"], "B"),
        (["AB", "C"], "DE"),
        (["AB", "BA"], "CC"),
        (["ABC", "D"], "EFA"),
        (["NO", "NO", "TOO"], "LATE"),
    ]
    for words, result in fixtures:
        assert is_solvable(words, result) == exhaustive_oracle(words, result)

    # All ten letters have fixed, independent boundary evidence.
    assert 526485 + 197485 == 723970
    assert is_solvable(["DONALD", "GERALD"], "ROBERT")
    # Nine distinct addend digits have minimum sum 0+...+8 = 36, so they
    # cannot equal the remaining single digit.
    assert not is_solvable(list("ABCDEFGHI"), "J")


def test_capture_queen_bounded_domain_matches_every_legal_placement() -> None:
    capture = _reference_solve("3001")
    squares = [(row, column) for row in range(1, 9) for column in range(1, 9)]

    def ray_attacks(
        piece: tuple[int, int],
        target: tuple[int, int],
        blocker: tuple[int, int],
        directions: tuple[tuple[int, int], ...],
    ) -> bool:
        for row_step, column_step in directions:
            row, column = piece
            while 1 <= row + row_step <= 8 and 1 <= column + column_step <= 8:
                row += row_step
                column += column_step
                if (row, column) == blocker:
                    break
                if (row, column) == target:
                    return True
        return False

    rook_directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    bishop_directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    checked = 0

    for rook in squares:
        for bishop in squares:
            if bishop == rook:
                continue
            for queen in squares:
                if queen == rook or queen == bishop:
                    continue
                direct = ray_attacks(rook, queen, bishop, rook_directions) or ray_attacks(
                    bishop, queen, rook, bishop_directions
                )
                assert capture(*rook, *bishop, *queen) == (1 if direct else 2)
                checked += 1

    assert checked == 64 * 63 * 62


def test_minimum_keypad_pushes_matches_every_legal_distinct_length() -> None:
    minimum_pushes = _reference_solve("3014")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    slot_costs = sorted(
        push_count
        for push_count in range(1, 5)
        for _ in range(8)
    )

    for length in range(1, 27):
        word = alphabet[:length]
        assert minimum_pushes(word) == sum(slot_costs[:length])


def test_even_knight_moves_bounded_domain_matches_every_cell_pair() -> None:
    from collections import deque

    can_reach = _reference_solve("3996")
    package = leetcode_package_dir("lc_3996")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_can_reach = native_namespace["Solution"]().canReach

    moves = (
        (1, 2),
        (2, 1),
        (-1, 2),
        (-2, 1),
        (1, -2),
        (2, -1),
        (-1, -2),
        (-2, -1),
    )

    def even_targets(start: tuple[int, int]) -> set[tuple[int, int]]:
        queue = deque([(start[0], start[1], 0)])
        seen = {(start[0], start[1], 0)}
        while queue:
            x, y, parity = queue.popleft()
            for dx, dy in moves:
                next_x = x + dx
                next_y = y + dy
                state = (next_x, next_y, parity ^ 1)
                if (
                    0 <= next_x < 8
                    and 0 <= next_y < 8
                    and state not in seen
                ):
                    seen.add(state)
                    queue.append(state)
        return {(x, y) for x, y, parity in seen if parity == 0}

    checked = 0
    for start_x in range(8):
        for start_y in range(8):
            expected_targets = even_targets((start_x, start_y))
            start = [start_x, start_y]
            for target_x in range(8):
                for target_y in range(8):
                    target = [target_x, target_y]
                    expected = (target_x, target_y) in expected_targets
                    assert can_reach(start, target) is expected
                    assert native_can_reach(start, target) is expected
                    checked += 1

    assert checked == 4096

    cases = json.loads((package / "cases.json").read_text(encoding="utf-8"))["cases"]
    for case in cases:
        start = case["input"]["start"]
        target = case["input"]["target"]
        expected = tuple(target) in even_targets(tuple(start))
        assert case["expected"] is expected
        assert can_reach(start, target) is expected
        assert native_can_reach(start, target) is expected


def test_largest_integer_bounded_domain_matches_exhaustive_enumeration() -> None:
    largest_integer = _reference_solve("4000")
    package = leetcode_package_dir("lc_4000")
    assert package is not None
    native_namespace = _run_native_module(
        _optimal_solution_path(package, "py")
    )
    native_largest_integer = native_namespace["Solution"]().largestInteger

    checked = 0
    for digit_limit in range(1, 6):
        best_by_sum = [-1] * 101
        for value in range(10**digit_limit):
            digit_sum = sum(int(digit) for digit in str(value))
            best_by_sum[digit_sum] = value

        for required_sum, expected in enumerate(best_by_sum):
            assert largest_integer(digit_limit, required_sum) == expected
            assert native_largest_integer(digit_limit, required_sum) == expected
            checked += 1

    assert checked == 5 * 101


def test_migration_audit_accepts_certificates_as_explicit_complexity_checks() -> None:
    report = build_report()
    entries = {entry["frontend_id"]: entry for entry in report["entries"]}

    assert report["counts"]["complexity_certified"] >= len(CERTIFIED_METHODS)
    for frontend_id, method in CERTIFIED_METHODS.items():
        checks = entries[frontend_id]["checks"]
        assert checks["complexity_certificate"]["complete"]
        assert not checks["benchmarks"]["complete"]
        assert checks["complexity"] == {
            "complete": True,
            "method": method,
            "benchmark_complete": False,
            "certificate_complete": True,
            "conflict": False,
        }


class ComplexityCertificateRouteTest(conftest._Base):
    def test_reference_sources_pass_real_test_by_certificate_without_fake_runtime(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        for frontend_id, method in CERTIFIED_METHODS.items():
            with self.subTest(frontend_id=frontend_id):
                package = leetcode_package_dir(f"lc_{frontend_id}")
                self.assertIsNotNone(package)
                assert package is not None
                metadata = json.loads((package / "metadata.json").read_text(encoding="utf-8"))
                if not category_is_runnable(metadata) or metadata.get("category") == "database":
                    continue
                challenge_id = f"lc_{frontend_id}"
                language = primary_language_for_challenge(challenge_id)
                source_path = leetcode_solution_path(challenge_id, language)
                if source_path is None or not source_path.is_file():
                    self.fail(f"No runnable reference source for lc_{frontend_id}")
                source = source_path.read_text(encoding="utf-8")
                response = self.client.post(
                    f"/api/challenges/lc_{frontend_id}/run",
                    json={"language": language, "source": source, "mode": "real_test"},
                )
                self.assertEqual(response.status_code, 200, response.text)
                body = response.json()
                self.assertTrue(body["correct"], body)
                self.assertTrue(body["passed"], body)
                self.assertTrue(body["within_threshold"], body)
                self.assertFalse(body["runtime_check"], body)
                self.assertTrue(body["complexity_check"], body)
                self.assertTrue(body["complexity_passed"], body)
                self.assertEqual(body["complexity_method"], method)
                self.assertIn("certificate", body["complexity_message"].lower())
                self.assertFalse(any(case["kind"] == "benchmark" for case in body["case_results"]))
