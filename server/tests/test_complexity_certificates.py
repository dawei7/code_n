"""Non-scaling complexity-certificate validation and run integration."""

from __future__ import annotations

import calendar
import json
import math
import runpy
from bisect import bisect_left, bisect_right
from datetime import date, timedelta
from functools import lru_cache
from itertools import permutations, product

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
    leetcode_solution_path,
)
from server.app.special_environments import run_special_environment
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
}


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
    return runpy.run_path(
        str(source_path),
        init_globals={"Point": _JudgePoint},
    )["solve"]


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


def test_all_non_scaling_certificates_are_strictly_valid() -> None:
    for frontend_id, method in CERTIFIED_METHODS.items():
        status = leetcode_complexity_certificate_status(f"lc_{frontend_id}")
        assert status.complete, (frontend_id, status.errors)
        assert status.method == method
        assert status.required_time.startswith("O(")
        path = leetcode_complexity_certificate_path(f"lc_{frontend_id}")
        assert path is not None and path.is_file()


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
                python_path = leetcode_solution_path(f"lc_{frontend_id}", "python")
                sql_path = leetcode_solution_path(f"lc_{frontend_id}", "sql")
                if python_path is not None and python_path.is_file():
                    language = "python"
                    source_path = python_path
                elif sql_path is not None and sql_path.is_file():
                    language = "sql"
                    source_path = sql_path
                else:
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
