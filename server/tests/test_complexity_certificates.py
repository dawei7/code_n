"""Non-scaling complexity-certificate validation and run integration."""

from __future__ import annotations

import calendar
import runpy
from datetime import date, timedelta
from pathlib import Path

from engine.complexity_certificates import validate_complexity_certificate
from server.app.engine_runner import (
    _JudgeArrayReader,
    _JudgeMajorityReader,
    _JudgePoint,
    _JudgeSea,
    _list_node_from_values,
)
from server.app.challenge_packages import (
    leetcode_complexity_certificate_path,
    leetcode_complexity_certificate_status,
    leetcode_package_dir,
)
from tools.audit_leetcode_migration import build_report

from . import conftest


CERTIFIED_METHODS = {
    "401": "bounded_domain",
    "405": "bounded_domain",
    "479": "bounded_domain",
    "999": "bounded_domain",
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
}


def _reference_solve(frontend_id: str):
    package = leetcode_package_dir(f"lc_{frontend_id}")
    assert package is not None
    return runpy.run_path(
        str(package / "solutions" / "python.py"),
        init_globals={"Point": _JudgePoint},
    )["solve"]


def test_all_non_scaling_certificates_are_strictly_valid() -> None:
    for frontend_id, method in CERTIFIED_METHODS.items():
        status = leetcode_complexity_certificate_status(f"lc_{frontend_id}")
        assert status.complete, (frontend_id, status.errors)
        assert status.method == method
        assert status.required_time.startswith("O(")
        path = leetcode_complexity_certificate_path(f"lc_{frontend_id}")
        assert path is not None and path.is_file()


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
                source_path = Path(package) / "solutions" / "python.py"
                source = source_path.read_text(encoding="utf-8")
                response = self.client.post(
                    f"/api/challenges/lc_{frontend_id}/run",
                    json={"language": "python", "source": source, "mode": "real_test"},
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
