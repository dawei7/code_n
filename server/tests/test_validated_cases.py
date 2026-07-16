"""Validated-case judge behavior for the user-facing run API."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from challenges.registry import CHALLENGE_REGISTRY
from server.app.engine_runner import (
    _accounts_merge_match,
    _alternating_groups_subsequence_match,
    _all_one_trace_match,
    _anagram_mapping_match,
    _anagram_groups_match,
    _avoid_flood_match,
    _advantage_shuffle_match,
    _fair_candy_swap_match,
    _beautiful_arrangement_ii_match,
    _beautiful_array_match,
    _circular_doubly_tree_match,
    _closest_leaf_match,
    _custom_sorted_string_match,
    _de_bruijn_sequence_match,
    _di_string_match,
    _duplicate_subtrees_match,
    _float_close_match,
    _float_list_close_match,
    _float_matrix_close_match,
    _flattened_multilevel_list_match,
    _fibonacci_split_match,
    _frequency_sorted_string_match,
    _gray_code_match,
    _circular_gray_code_match,
    _good_subset_matrix_match,
    _hamming_alternating_subsequence_match,
    _index_value_pair_match,
    _indexed_parity_match,
    _immutable_list_node_from_values,
    _immutable_list_print_match,
    _k_smallest_pairs_match,
    _list_node_param_names,
    _list_node_from_values,
    _list_node_to_values,
    _longest_happy_string_match,
    _lcp_string_match,
    _largest_divisible_subset_match,
    _linked_list_random_draws_match,
    _matrix_margins_match,
    _minimum_unique_rows_matrix_match,
    _minimum_subsequence_match,
    _minimum_unique_abbreviation_match,
    _master_guessed_match,
    _most_similar_path_match,
    _next_right_pointers_match,
    _neither_min_nor_max_match,
    _ordered_unordered_groups_match,
    _parity_partition_match,
    _pancake_sort_match,
    _peak_index_match,
    _parent_tree_node_from_fixture,
    _pre_post_tree_match,
    _phone_directory_trace_match,
    _prepare_validated_kwargs,
    _randomized_set_trace_match,
    _randomized_collection_trace_match,
    _random_pick_indices_match,
    _random_flip_matrix_trace_match,
    _queue_reconstruction_match,
    _quad_tree_match,
    _question_mark_replacement_match,
    _rearranged_k_distance_match,
    _robot_room_cleaner_match,
    _sudoku_solution_match,
    _stamping_sequence_match,
    _string_without_triples_match,
    _three_equal_parts_match,
    _runtime_check_from_scaling,
    _runtime_check_python_cases,
    _shuffle_array_trace_match,
    _shortest_common_supersequence_match,
    _shortest_superstring_match,
    _split_bst_match,
    _returns_in_place,
    _returns_list_node,
    _returns_tree,
    _tree_param_names,
    _tree_from_level_order,
    _three_equal_binary_parts_match,
    _JudgeSea,
    _JudgeBinaryMatrix,
    _JudgePoint,
    _JudgeMaster,
    _unique_bsts_match,
    _unordered_nested_list_matches,
    _ordered_groups_unordered_items_match,
    _validated_case_matches,
    _vps_split_match,
    _wiggle_sort_matches,
)
from server.app.validated_cases import NoValidatedCases, ValidatedCase, _load_case_file, load_case_suite

from . import conftest


LC_153_SOURCE = CHALLENGE_REGISTRY["lc_153"]()._spec.source
LC_1_QUADRATIC_SOURCE = '''
def solve(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
'''


class ValidatedCasesTest(conftest._Base):
    def test_most_similar_path_validator_accepts_any_optimal_tie(self) -> None:
        roads = [[0, 1], [1, 2], [2, 3], [3, 0]]
        names = ["A", "B", "A", "B"]
        target = ["A", "B", "A"]

        self.assertTrue(_most_similar_path_match([0, 1, 2], 4, roads, names, target))
        self.assertTrue(_most_similar_path_match([2, 3, 0], 4, roads, names, target))
        self.assertFalse(_most_similar_path_match([1, 2, 1], 4, roads, names, target))
        self.assertFalse(_most_similar_path_match([0, 2, 1], 4, roads, names, target))
        self.assertFalse(_most_similar_path_match([0, 1], 4, roads, names, target))

    def test_master_validator_requires_secret_within_guess_budget(self) -> None:
        words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
        master = _JudgeMaster("acckzz", words, 2)

        self.assertEqual(master.guess("ccbazz"), 3)
        self.assertEqual(master.guess("acckzz"), 6)
        self.assertTrue(_master_guessed_match(master))

        over_budget = _JudgeMaster("acckzz", words, 1)
        over_budget.guess("ccbazz")
        over_budget.guess("acckzz")
        self.assertFalse(_master_guessed_match(over_budget))

    def test_fibonacci_split_validator_accepts_any_valid_full_split(self) -> None:
        digits = "1101111"

        self.assertTrue(_fibonacci_split_match([11, 0, 11, 11], [11, 0, 11, 11], digits))
        self.assertTrue(_fibonacci_split_match([110, 1, 111], [11, 0, 11, 11], digits))
        self.assertFalse(_fibonacci_split_match([11, 0, 11], [11, 0, 11, 11], digits))
        self.assertFalse(_fibonacci_split_match([1, 10, 11, 11], [11, 0, 11, 11], digits))
        self.assertFalse(_fibonacci_split_match([2**31, 0, 2**31], [], str(2**31) * 2))
        self.assertTrue(_fibonacci_split_match([], [], "0123"))

    def test_anagram_mapping_validator_accepts_any_matching_duplicate_index(self) -> None:
        left = [12, 28, 12]
        right = [28, 12, 12]

        self.assertTrue(_anagram_mapping_match([1, 0, 2], left, right))
        self.assertTrue(_anagram_mapping_match([2, 0, 2], left, right))
        self.assertFalse(_anagram_mapping_match([0, 1, 2], left, right))
        self.assertFalse(_anagram_mapping_match([1, 0], left, right))
        self.assertFalse(_anagram_mapping_match([True, 0, 2], left, right))

    def test_split_bst_validator_serializes_both_result_roots(self) -> None:
        smaller = _tree_from_level_order([2, 1])
        greater = _tree_from_level_order([4, 3, 6, None, None, 5, 7])

        self.assertTrue(
            _split_bst_match([smaller, greater], [[2, 1], [4, 3, 6, None, None, 5, 7]])
        )
        self.assertTrue(_split_bst_match([None, greater], [[], [4, 3, 6, None, None, 5, 7]]))
        self.assertFalse(_split_bst_match([smaller], [[2, 1], []]))

    def test_closest_leaf_validator_accepts_any_minimum_distance_tie(self) -> None:
        root = [1, 2, 3, 4, 5]

        self.assertTrue(_closest_leaf_match(4, root, 2))
        self.assertTrue(_closest_leaf_match(5, root, 2))
        self.assertFalse(_closest_leaf_match(3, root, 2))
        self.assertFalse(_closest_leaf_match(True, root, 2))

    def test_de_bruijn_validator_accepts_any_minimum_covering_sequence(self) -> None:
        self.assertTrue(_de_bruijn_sequence_match("00110", 2, 2))
        self.assertTrue(_de_bruijn_sequence_match("01100", 2, 2))
        self.assertTrue(_de_bruijn_sequence_match("210", 1, 3))
        self.assertFalse(_de_bruijn_sequence_match("00100", 2, 2))
        self.assertFalse(_de_bruijn_sequence_match("001102", 2, 2))
        self.assertFalse(_de_bruijn_sequence_match(True, 2, 2))

    def test_accounts_merge_validator_ignores_outer_order_but_requires_sorted_emails(self) -> None:
        expected = [
            ["John", "a@example.com", "b@example.com"],
            ["Mary", "m@example.com"],
        ]
        self.assertTrue(
            _accounts_merge_match(
                [["Mary", "m@example.com"], ["John", "a@example.com", "b@example.com"]],
                expected,
            )
        )
        self.assertFalse(
            _accounts_merge_match(
                [["John", "b@example.com", "a@example.com"], ["Mary", "m@example.com"]],
                expected,
            )
        )
        self.assertFalse(
            _accounts_merge_match(
                [["John", "a@example.com", "b@example.com"]],
                expected,
            )
        )

    def test_random_flip_matrix_trace_validator_tracks_resets_and_uniqueness(self) -> None:
        operations = ["flip", "flip", "reset", "flip"]
        self.assertTrue(
            _random_flip_matrix_trace_match([[0, 0], [1, 1], None, [0, 0]], 2, 2, operations)
        )
        self.assertFalse(
            _random_flip_matrix_trace_match([[0, 0], [0, 0], None, [1, 1]], 2, 2, operations)
        )
        self.assertFalse(
            _random_flip_matrix_trace_match([[0, 0], [2, 0], None, [1, 1]], 2, 2, operations)
        )
        self.assertFalse(
            _random_flip_matrix_trace_match([[0, 0], [1, 1], [], [0, 0]], 2, 2, operations)
        )

    def test_sql_benchmark_rejects_correlated_quadratic_query(self) -> None:
        source = '''
SELECT DISTINCT
    activity.player_id,
    (SELECT MIN(other.event_date)
     FROM Activity AS other
     WHERE other.player_id = activity.player_id) AS first_login
FROM Activity AS activity
ORDER BY activity.player_id;
'''
        response = self.client.post(
            "/api/challenges/lc_511/run",
            json={"source": source, "language": "sql", "mode": "real_test"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["correct"], body)
        self.assertTrue(body["runtime_check"], body)
        self.assertFalse(body["runtime_passed"], body)
        self.assertFalse(body["passed"], body)
        self.assertIn("Scaling too slow", body["runtime_message"])

    def test_parent_pointer_fixture_selects_node_and_node_value_validator(self) -> None:
        node = _parent_tree_node_from_fixture({"tree": [2, 1, 3], "target_index": 1})
        self.assertEqual(node.val, 1)
        self.assertEqual(node.parent.val, 2)
        self.assertIs(node.parent.left, node)

        case = ValidatedCase(
            id="parent-node",
            name="parent node",
            kind="sample",
            input={},
            expected=2,
            validator={"kind": "node_value"},
        )
        self.assertTrue(_validated_case_matches(case, node.parent, 2))
        self.assertFalse(_validated_case_matches(case, node, 2))
        self.assertTrue(_validated_case_matches(case, None, None))

    def test_cloned_tree_fixture_preserves_original_target_identity(self) -> None:
        kwargs = _prepare_validated_kwargs(
            {
                "original": {"tree": [7, 4, 7, None, None, 6, 8], "target_index": 2},
                "cloned": {"clone_of": "original"},
                "target": {"target_of": "original"},
            },
            ("original", "cloned", "target"),
            (),
        )
        original = kwargs["original"]
        cloned = kwargs["cloned"]
        target = kwargs["target"]

        self.assertIs(target, original.right)
        self.assertIsNot(target, cloned.right)
        self.assertEqual(target.val, cloned.right.val)
        self.assertEqual(target.left.val, cloned.right.left.val)

    def test_robot_room_cleaner_fixture_preserves_interface_and_checks_reachability(self) -> None:
        kwargs = _prepare_validated_kwargs(
            {"robot": {"room": [[1, 1, 1]], "row": 0, "col": 1, "direction": 1}},
            (),
            (),
        )
        robot = kwargs["robot"]
        robot.clean()
        self.assertTrue(robot.move())
        robot.clean()
        robot.turnRight()
        robot.turnRight()
        self.assertTrue(robot.move())
        self.assertTrue(robot.move())
        self.assertFalse(_robot_room_cleaner_match(robot, 3))
        robot.clean()
        self.assertTrue(_robot_room_cleaner_match(robot, 3))

    def test_sea_fixture_preserves_inclusive_queries_and_enforces_the_budget(self) -> None:
        kwargs = _prepare_validated_kwargs(
            {"sea": {"ships": [[0, 0], [3, 2]], "max_queries": 2}},
            (),
            (),
        )
        sea = kwargs["sea"]
        self.assertIsInstance(sea, _JudgeSea)
        self.assertTrue(sea.hasShips(_JudgePoint(3, 2), _JudgePoint(3, 2)))
        self.assertFalse(sea.hasShips(_JudgePoint(2, 2), _JudgePoint(1, 1)))
        self.assertEqual(sea.query_count, 2)
        with self.assertRaisesRegex(RuntimeError, "2-query limit"):
            sea.hasShips(_JudgePoint(0, 0), _JudgePoint(0, 0))

        with self.assertRaisesRegex(ValueError, "ordered corners"):
            _JudgeSea([]).hasShips(_JudgePoint(0, 0), _JudgePoint(1, 0))

    def test_binary_matrix_fixture_exposes_judge_methods_and_enforces_the_budget(self) -> None:
        kwargs = _prepare_validated_kwargs(
            {
                "binary_matrix": {
                    "matrix": [[0, 0, 1], [0, 1, 1]],
                    "max_queries": 2,
                }
            },
            (),
            (),
        )
        binary_matrix = kwargs["binary_matrix"]
        self.assertIsInstance(binary_matrix, _JudgeBinaryMatrix)
        self.assertEqual(binary_matrix.dimensions(), [2, 3])
        self.assertEqual(binary_matrix.get(0, 2), 1)
        self.assertEqual(binary_matrix.get(1, 0), 0)
        self.assertEqual(binary_matrix.query_count, 2)
        with self.assertRaisesRegex(RuntimeError, "2-query limit"):
            binary_matrix.get(1, 1)
        with self.assertRaisesRegex(ValueError, "outside the matrix"):
            _JudgeBinaryMatrix([[0]]).get(0, 1)
        with self.assertRaisesRegex(ValueError, "non-decreasing"):
            _JudgeBinaryMatrix([[1, 0]])

    def test_immutable_list_fixture_exposes_only_judge_methods_and_captures_prints(self) -> None:
        head = _immutable_list_node_from_values([1, 2, 3])

        self.assertFalse(hasattr(head, "val"))
        self.assertFalse(hasattr(head, "next"))
        tail = head.getNext().getNext()
        tail.printValue()
        head.getNext().printValue()
        head.printValue()

        self.assertTrue(_immutable_list_print_match(head, [3, 2, 1]))
        self.assertFalse(_immutable_list_print_match(head, [1, 2, 3]))

    def test_challenge_detail_exposes_visible_cases(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        response = self.client.get("/api/challenges/lc_153")
        self.assertEqual(response.status_code, 200, response.text)
        cases = response.json()["test_cases"]
        self.assertGreaterEqual(len(cases), 3)
        self.assertEqual(cases[0]["id"], "sample-1")
        self.assertTrue(cases[0]["visible"])
        self.assertIn('"nums"', cases[0]["input_repr"])

    def test_run_selected_visible_case(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "case_ids": ["trial-two-items"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertEqual(body["selected_case_ids"], ["trial-two-items"])
        self.assertEqual(len(body["case_results"]), 1)
        self.assertTrue(body["runtime_check"])

    def test_run_all_trial_cases(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "case_ids": ["__all_trial__"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertGreaterEqual(len(body["case_results"]), 3)
        self.assertIn("sample-1", body["selected_case_ids"])
        self.assertIn("trial-two-items", body["selected_case_ids"])

    def test_custom_json_input_uses_reference_expected_value(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "custom_input": {"nums": [4, 5, 6, 1, 2, 3]}},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertEqual(body["selected_case_ids"], ["custom"])
        self.assertEqual(body["case_results"][0]["expected_repr"], "1")

    def test_named_user_cases_can_run_individually_or_with_all_authored_cases(self) -> None:
        custom_cases = [
            {"id": "user-left", "name": "Left rotation", "input": {"nums": [3, 4, 5, 1, 2]}},
            {"id": "user-sorted", "name": "Already sorted", "input": {"nums": [1, 2, 3, 4]}},
        ]
        single = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "case_ids": ["user-left"], "custom_cases": custom_cases},
        )
        self.assertEqual(single.status_code, 200, single.text)
        self.assertEqual(single.json()["selected_case_ids"], ["user-left"])
        self.assertEqual(single.json()["case_results"][0]["name"], "Left rotation")

        all_cases = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "case_ids": ["__all_trial__"], "custom_cases": custom_cases},
        )
        self.assertEqual(all_cases.status_code, 200, all_cases.text)
        selected = all_cases.json()["selected_case_ids"]
        self.assertIn("sample-1", selected)
        self.assertIn("user-left", selected)
        self.assertIn("user-sorted", selected)

        real = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "mode": "real_test", "custom_cases": custom_cases},
        )
        self.assertEqual(real.status_code, 200, real.text)
        self.assertIn("user-left", real.json()["selected_case_ids"])
        self.assertIn("user-sorted", real.json()["selected_case_ids"])

    def test_real_test_uses_hidden_cases_and_benchmarks(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": LC_153_SOURCE, "mode": "real_test"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertEqual(
            body["selected_case_ids"],
            [
                "sample-1",
                "sample-2",
                "trial-not-rotated",
                "trial-two-items",
                "real-last-drop",
                "benchmark-wide-rotation",
                "benchmark-wide-rotation-medium",
                "benchmark-wide-rotation-large",
            ],
        )
        self.assertTrue(body["runtime_check"])
        self.assertGreater(body["runtime_reference_ms"], 0)
        self.assertGreaterEqual(body["runtime_limit_ms"], body["runtime_reference_ms"] * 1.5)
        self.assertIn("Scaling OK", body["runtime_message"])
        hidden_results = body["case_results"][-4:]
        self.assertEqual(
            [case["name"] for case in hidden_results],
            ["Hidden case 1", "Hidden case 2", "Hidden case 3", "Hidden case 4"],
        )
        self.assertTrue(all(case["hidden"] for case in hidden_results))
        self.assertTrue(all(case["counts_toward_verdict"] for case in hidden_results))
        self.assertTrue(all(case["input_repr"] == "" for case in hidden_results))
        self.assertTrue(all(case["return_value_repr"] == "" for case in hidden_results))
        self.assertTrue(all(case["expected_repr"] is None for case in hidden_results))
        self.assertTrue(all(case["message"] == "" for case in hidden_results))

    def test_runtime_benchmark_alternates_order_and_normalizes_amplification(self) -> None:
        case = ValidatedCase(
            id="benchmark-paired",
            name="benchmark: paired",
            kind="benchmark",
            input={"value": 7},
            expected=14,
        )

        def user(value: int) -> int:
            return value * 2

        def reference(value: int) -> int:
            return value * 2

        order: list[str] = []

        def fake_timed_call(func, kwargs, iterations, **_options):
            label = "reference" if func is reference else "user"
            order.append(label)
            per_execution_ms = 1.0 if label == "reference" else 1.2
            return kwargs["value"] * 2, per_execution_ms * iterations

        with patch("server.app.engine_runner._timed_reference_iterations", side_effect=fake_timed_call):
            check = _runtime_check_python_cases(
                solve_fn=user,
                reference_solve=reference,
                cases=[case],
                param_names=["value"],
            )

        self.assertTrue(check.checked)
        self.assertTrue(check.passed)
        self.assertEqual(check.trials, 7)
        self.assertAlmostEqual(check.reference_ms or 0, 1.0)
        self.assertAlmostEqual(check.user_ms or 0, 1.2)
        self.assertEqual(
            order,
            [
                "reference",  # pilot
                "user",       # shared-amplification pilot
                "reference", "user",
                "user", "reference",
                "reference", "user",
                "user", "reference",
                "reference", "user",
                "user", "reference",
                "reference", "user",
            ],
        )

    def test_scaling_gate_accepts_constant_overhead_and_rejects_worse_growth(self) -> None:
        same_class = _runtime_check_from_scaling(
            [
                {"size": 32, "user_ms": 3.0, "reference_ms": 1.0, "ratio": 3.0},
                {"size": 128, "user_ms": 6.2, "reference_ms": 2.0, "ratio": 3.1},
                {"size": 512, "user_ms": 12.0, "reference_ms": 4.0, "ratio": 3.0},
            ],
            trials=7,
            language="python",
        )
        worse_growth = _runtime_check_from_scaling(
            [
                {"size": 32, "user_ms": 1.2, "reference_ms": 1.0, "ratio": 1.2},
                {"size": 128, "user_ms": 3.6, "reference_ms": 2.0, "ratio": 1.8},
                {"size": 512, "user_ms": 9.6, "reference_ms": 4.0, "ratio": 2.4},
            ],
            trials=7,
            language="python",
        )

        self.assertTrue(same_class.passed)
        self.assertFalse(worse_growth.passed)
        self.assertEqual(same_class.limit_ms, 32.0)
        self.assertIn("Scaling too slow", worse_growth.message)

    def test_two_sum_has_three_ordered_scaling_tiers(self) -> None:
        benchmarks = [case for case in load_case_suite("lc_1") if case.kind == "benchmark"]
        self.assertEqual([case.size for case in benchmarks], [32, 128, 512])

    def test_two_sum_quadratic_solution_is_a_complexity_failure_not_a_wrong_case(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_1/run",
            json={"source": LC_1_QUADRATIC_SOURCE, "mode": "real_test"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["correct"], body)
        self.assertTrue(all(case["correct"] for case in body["case_results"]), body)
        self.assertTrue(body["runtime_check"], body)
        self.assertFalse(body["runtime_passed"], body)
        self.assertFalse(body["passed"], body)
        self.assertIn("Scaling too slow", body["runtime_message"])

    def test_real_test_reports_custom_failure_without_rejecting_submission(self) -> None:
        source = LC_153_SOURCE.replace(
            "def solve(nums):\n",
            "def solve(nums):\n    if nums == [42, 1]:\n        return -1\n",
        )
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={
                "source": source,
                "mode": "real_test",
                "custom_cases": [
                    {"id": "user-diagnostic", "name": "My edge case", "input": {"nums": [42, 1]}},
                ],
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["correct"], body)
        self.assertTrue(body["passed"], body)
        custom = next(case for case in body["case_results"] if case["id"] == "user-diagnostic")
        self.assertFalse(custom["correct"])
        self.assertFalse(custom["counts_toward_verdict"])
        self.assertFalse(custom["hidden"])

    def test_real_test_continues_after_failures_and_redacts_hidden_failure(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": "def solve(nums):\n    return None\n", "mode": "real_test"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertFalse(body["correct"])
        self.assertEqual(len(body["case_results"]), 8)
        self.assertTrue(all(not case["correct"] for case in body["case_results"]))
        hidden_results = body["case_results"][-4:]
        self.assertEqual(
            [case["name"] for case in hidden_results],
            ["Hidden case 1", "Hidden case 2", "Hidden case 3", "Hidden case 4"],
        )
        self.assertTrue(all(case["input_repr"] == "" for case in hidden_results))
        self.assertTrue(all(case["return_value_repr"] == "" for case in hidden_results))
        self.assertTrue(all(case["expected_repr"] is None for case in hidden_results))
        self.assertTrue(all(case["message"] == "" for case in hidden_results))

    def test_hidden_only_failure_has_no_hidden_evidence_side_channel(self) -> None:
        source = LC_153_SOURCE.replace(
            "def solve(nums):\n",
            "def solve(nums):\n    if nums == [8, 9, 10, 11, 12, 3, 4, 5, 6, 7]:\n        return -1\n",
        )
        response = self.client.post(
            "/api/challenges/lc_153/run",
            json={"source": source, "mode": "real_test"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertFalse(body["correct"])
        self.assertEqual(body["message"], "One or more hidden cases failed.")
        self.assertEqual(body["return_value_repr"], "1")
        self.assertEqual(body["reference_return_value_repr"], "1")
        self.assertIsNone(body["setup_data_repr"])
        hidden = body["case_results"][-4]
        self.assertFalse(hidden["correct"])
        self.assertEqual(hidden["input_repr"], "")
        self.assertEqual(hidden["return_value_repr"], "")
        self.assertIsNone(hidden["expected_repr"])
        benchmarks = body["case_results"][-3:]
        self.assertTrue(all(case["correct"] for case in benchmarks))
        self.assertEqual(
            [case["name"] for case in benchmarks],
            ["Hidden case 2", "Hidden case 3", "Hidden case 4"],
        )
        self.assertTrue(all(case["hidden"] for case in benchmarks))

    def test_benchmark_sidecar_cases_load_with_main_suite(self) -> None:
        main_payload = json.loads(Path("dsa/leetcode/2615_sum-of-distances/cases.json").read_text(encoding="utf-8"))
        self.assertNotIn("benchmark", {case["kind"] for case in main_payload["cases"]})
        self.assertTrue(Path("dsa/leetcode/2615_sum-of-distances/benchmark.json").is_file())
        benchmark = next(case for case in load_case_suite("lc_2615") if case.kind == "benchmark")
        self.assertEqual(len(benchmark.input["nums"]), 6500)
        self.assertEqual(benchmark.input["nums"][:3], [4, 4, 4])
        stats_benchmarks = [case for case in load_case_suite("lc_1093") if case.kind == "benchmark"]
        self.assertEqual(len(stats_benchmarks), 3)
        stats_benchmark = stats_benchmarks[0]
        self.assertEqual(len(stats_benchmark.input["count"]), 256)
        self.assertEqual(stats_benchmark.size, 128)
        self.assertEqual(stats_benchmark.input["count"][128], 64)
        self.assertEqual(stats_benchmark.input["count"][64], 16)
        self.assertEqual(stats_benchmark.input["count"][192], 32)

    def test_main_case_file_rejects_inline_benchmark_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.json"
            path.write_text(
                json.dumps(
                    {
                        "challenge_id": "demo",
                        "cases": [
                            {
                                "id": "benchmark-inline",
                                "name": "benchmark inline",
                                "kind": "benchmark",
                                "input": {"nums": [1, 2, 3]},
                                "expected": 6,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(NoValidatedCases, "must live in demo.benchmark.json"):
                _load_case_file(path, "demo", benchmark_sidecar=False)

    def test_benchmark_sidecar_rejects_non_benchmark_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.benchmark.json"
            path.write_text(
                json.dumps(
                    {
                        "challenge_id": "demo",
                        "cases": [
                            {
                                "id": "sample-in-sidecar",
                                "name": "sample in sidecar",
                                "kind": "sample",
                                "input": {"nums": [1, 2, 3]},
                                "expected": 6,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(NoValidatedCases, "must use kind 'benchmark'"):
                _load_case_file(path, "demo", benchmark_sidecar=True)

    def test_multi_tier_benchmark_requires_strict_ordered_integer_sizes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.benchmark.json"
            path.write_text(
                json.dumps(
                    {
                        "challenge_id": "demo",
                        "cases": [
                            {
                                "id": "small",
                                "kind": "benchmark",
                                "size": 32,
                                "input": {"nums": [1]},
                                "expected": 1,
                            },
                            {
                                "id": "large",
                                "kind": "benchmark",
                                "size": 32.5,
                                "input": {"nums": [1, 2]},
                                "expected": 3,
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(NoValidatedCases, "must be a positive integer"):
                _load_case_file(path, "demo", benchmark_sidecar=True)

    def test_challenge_without_cases_returns_no_fallback_error(self) -> None:
        with patch(
            "server.app.routes.run.select_cases_for_run",
            side_effect=NoValidatedCases("fixture has no validated test cases"),
        ):
            response = self.client.post(
                "/api/challenges/lc_1003/run",
                json={"source": CHALLENGE_REGISTRY["lc_1003"]()._spec.source},
            )
        self.assertEqual(response.status_code, 422, response.text)
        detail = response.json()["detail"]
        self.assertEqual(detail["error"], "no_validated_cases")
        self.assertIn("no validated test cases", detail["message"])

    def test_balanced_bst_validator_accepts_alternate_valid_tree(self) -> None:
        source = '''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(nums):
    def build(left, right):
        if left > right:
            return None
        mid = (left + right + 1) // 2
        return TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right))
    return build(0, len(nums) - 1)
'''
        response = self.client.post(
            "/api/challenges/lc_108/run",
            json={"source": source, "case_ids": ["sample-2"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertIn("[3, 1]", body["return_value_repr"])

        tree_case = ValidatedCase(
            id="tree-input",
            name="tree input",
            kind="sample",
            input={"root": [1, None, 2, None, 3]},
            expected=[2, 1, 3],
            validator={
                "kind": "balanced_bst",
                "values_param": "root",
                "values_from_tree": True,
            },
        )
        self.assertTrue(_validated_case_matches(tree_case, [2, 1, 3], tree_case.expected))
        self.assertFalse(_validated_case_matches(tree_case, [1, None, 2, None, 3], tree_case.expected))

    def test_pre_post_tree_validator_accepts_single_child_orientation_ties(self) -> None:
        preorder = [1, 2, 3]
        postorder = [3, 2, 1]

        self.assertTrue(_pre_post_tree_match([1, 2, None, 3], preorder, postorder))
        self.assertTrue(_pre_post_tree_match([1, None, 2, None, 3], preorder, postorder))
        self.assertFalse(_pre_post_tree_match([1, 3, 2], preorder, postorder))
        self.assertFalse(_pre_post_tree_match([1, 2, None, 3, 4], preorder, postorder))

    def test_wiggle_sort_validator_supports_non_strict_problem_variant(self) -> None:
        self.assertTrue(_wiggle_sort_matches([2, 2, 2], [2, 2, 2], strict=False))
        self.assertFalse(_wiggle_sort_matches([2, 2, 2], [2, 2, 2], strict=True))
        self.assertTrue(_wiggle_sort_matches([1, 3, 2, 4], [1, 2, 3, 4], strict=False))

    def test_parity_partition_validator_accepts_any_valid_permutation(self) -> None:
        values = [3, 1, 2, 4, 2]
        case = ValidatedCase(
            id="parity",
            name="parity",
            kind="sample",
            input={"nums": values},
            expected=[2, 4, 2, 3, 1],
            validator={"kind": "parity_partition"},
        )

        self.assertTrue(_parity_partition_match([4, 2, 2, 1, 3], values))
        self.assertTrue(_validated_case_matches(case, [2, 2, 4, 3, 1], case.expected))
        self.assertFalse(_parity_partition_match([2, 3, 4, 2, 1], values))
        self.assertFalse(_parity_partition_match([4, 2, 2, 1, 1], values))
        self.assertFalse(_parity_partition_match([4, 2, True, 1, 3], values))

    def test_indexed_parity_validator_accepts_any_valid_permutation(self) -> None:
        values = [4, 2, 5, 7]
        case = ValidatedCase(
            id="indexed-parity",
            name="indexed parity",
            kind="sample",
            input={"nums": values},
            expected=[4, 5, 2, 7],
            validator={"kind": "indexed_parity"},
        )

        self.assertTrue(_indexed_parity_match([2, 7, 4, 5], values))
        self.assertTrue(_validated_case_matches(case, [4, 7, 2, 5], case.expected))
        self.assertFalse(_indexed_parity_match([2, 4, 5, 7], values))
        self.assertFalse(_indexed_parity_match([2, 7, 4, 7], values))
        self.assertFalse(_indexed_parity_match([2, 7, True, 5], values))

    def test_three_equal_binary_parts_validator_accepts_any_valid_split(self) -> None:
        values = [0, 0, 0, 0, 0]
        case = ValidatedCase(
            id="three-parts",
            name="three equal binary parts",
            kind="sample",
            input={"arr": values},
            expected=[0, 2],
            validator={"kind": "three_equal_binary_parts"},
        )

        self.assertTrue(_three_equal_binary_parts_match([1, 3], values))
        self.assertTrue(_validated_case_matches(case, [2, 4], case.expected))
        self.assertFalse(_three_equal_binary_parts_match([-1, -1], values))
        self.assertTrue(_three_equal_binary_parts_match([-1, -1], [1, 0, 1, 0]))
        self.assertFalse(_three_equal_binary_parts_match([0, 2], [1, 0, 1, 0, 1]))

    def test_beautiful_array_validator_accepts_any_valid_permutation(self) -> None:
        case = ValidatedCase(
            id="beautiful-array",
            name="beautiful array",
            kind="sample",
            input={"n": 4},
            expected=[2, 1, 4, 3],
            validator={"kind": "beautiful_array"},
        )

        self.assertTrue(_beautiful_array_match([1, 3, 2, 4], 4))
        self.assertTrue(_validated_case_matches(case, [3, 1, 2, 4], case.expected))
        self.assertFalse(_beautiful_array_match([1, 2, 3, 4], 4))
        self.assertFalse(_beautiful_array_match([1, 3, 2, 2], 4))
        self.assertFalse(_beautiful_array_match([1, 3, True, 4], 4))

    def test_di_string_validator_accepts_any_matching_permutation(self) -> None:
        case = ValidatedCase(
            id="di-string",
            name="DI string",
            kind="sample",
            input={"s": "IDID"},
            expected=[0, 4, 1, 3, 2],
            validator={"kind": "di_string"},
        )

        self.assertTrue(_di_string_match([0, 4, 1, 3, 2], "IDID"))
        self.assertTrue(_validated_case_matches(case, [1, 4, 0, 3, 2], case.expected))
        self.assertFalse(_di_string_match([0, 1, 2, 3, 4], "IDID"))
        self.assertFalse(_di_string_match([0, 4, 1, 3, 3], "IDID"))
        self.assertFalse(_di_string_match([0, 4, 1, 3, True], "IDID"))

    def test_vps_split_validator_accepts_any_optimal_assignment(self) -> None:
        case = ValidatedCase(
            id="vps-split",
            name="VPS split",
            kind="sample",
            input={"seq": "(()())"},
            expected=[0, 1, 1, 1, 1, 0],
            validator={"kind": "vps_split"},
        )

        self.assertTrue(_vps_split_match([1, 0, 0, 0, 0, 1], "(()())"))
        self.assertTrue(_validated_case_matches(case, [0, 1, 1, 1, 1, 0], case.expected))
        self.assertFalse(_vps_split_match([0, 0, 0, 0, 0, 0], "(()())"))
        self.assertFalse(_vps_split_match([0, 1, 1, 0, 1, 0], "(()())"))
        self.assertFalse(_vps_split_match([0, 1, 1, 1, 1, True], "(()())"))

    def test_shortest_superstring_validator_accepts_optimal_ties(self) -> None:
        words = ["abc", "bca", "cab"]
        case = ValidatedCase(
            id="shortest-superstring",
            name="shortest superstring",
            kind="sample",
            input={"words": words},
            expected="abcab",
            validator={"kind": "shortest_superstring"},
        )

        self.assertTrue(_shortest_superstring_match("bcabc", case.expected, words))
        self.assertTrue(_validated_case_matches(case, "cabca", case.expected))
        self.assertFalse(_shortest_superstring_match("abcabc", case.expected, words))
        self.assertFalse(_shortest_superstring_match("abcax", case.expected, words))
        self.assertFalse(_shortest_superstring_match(["abcab"], case.expected, words))

    def test_shortest_common_supersequence_validator_accepts_optimal_ties(self) -> None:
        case = ValidatedCase(
            id="shortest-common-supersequence",
            name="shortest common supersequence",
            kind="sample",
            input={"str1": "ab", "str2": "ac"},
            expected="acb",
            validator={"kind": "shortest_common_supersequence"},
        )

        self.assertTrue(_shortest_common_supersequence_match("abc", "ab", "ac"))
        self.assertTrue(_validated_case_matches(case, "acb", case.expected))
        self.assertFalse(_shortest_common_supersequence_match("abac", "ab", "ac"))
        self.assertFalse(_shortest_common_supersequence_match("abc", "ab", "ca"))
        self.assertFalse(_shortest_common_supersequence_match(["abc"], "ab", "ac"))

    def test_stamping_sequence_validator_accepts_any_valid_move_order(self) -> None:
        case = ValidatedCase(
            id="stamping",
            name="stamping sequence",
            kind="sample",
            input={"stamp": "abc", "target": "ababc"},
            expected=[0, 2],
            validator={"kind": "stamping_sequence"},
        )

        self.assertTrue(_stamping_sequence_match([1, 0, 2], case.expected, "abc", "ababc"))
        self.assertTrue(_validated_case_matches(case, [0, 2], case.expected))
        self.assertFalse(_stamping_sequence_match([0], case.expected, "abc", "ababc"))
        self.assertFalse(_stamping_sequence_match([3], case.expected, "abc", "ababc"))
        self.assertTrue(_stamping_sequence_match([], [], "ab", "ac"))
        self.assertFalse(_stamping_sequence_match([], [0], "a", "a"))

    def test_pancake_sort_validator_accepts_any_bounded_sorting_sequence(self) -> None:
        case = ValidatedCase(
            id="pancake-sort",
            name="pancake sort",
            kind="sample",
            input={"arr": [3, 2, 4, 1]},
            expected=[4, 2, 4, 3],
            validator={"kind": "pancake_sort"},
        )

        self.assertTrue(_pancake_sort_match([3, 4, 2, 3, 2], case.input["arr"]))
        self.assertTrue(_validated_case_matches(case, [4, 2, 4, 3], case.expected))
        self.assertTrue(_pancake_sort_match([], [1, 2, 3]))
        self.assertFalse(_pancake_sort_match([0], [2, 1]))
        self.assertFalse(_pancake_sort_match([3], [2, 1]))
        self.assertFalse(_pancake_sort_match([True], [2, 1]))
        self.assertFalse(_pancake_sort_match([2] * 21, [2, 1]))

    def test_string_without_triples_validator_accepts_any_valid_arrangement(self) -> None:
        case = ValidatedCase(
            id="semantic",
            name="semantic",
            kind="trial",
            visible=True,
            input={"a": 2, "b": 2},
            expected="aabb",
            validator={"kind": "string_without_triples"},
        )

        self.assertTrue(_validated_case_matches(case, "abba", case.expected))
        self.assertTrue(_string_without_triples_match("aabaa", 4, 1))
        self.assertFalse(_string_without_triples_match("aaabb", 3, 2))
        self.assertFalse(_string_without_triples_match("aabb", 3, 1))
        self.assertFalse(_string_without_triples_match("aabc", 2, 2))
        self.assertFalse(_string_without_triples_match(123, 1, 2))

    def test_longest_happy_string_validator_accepts_any_optimal_arrangement(self) -> None:
        case = ValidatedCase(
            id="longest-happy",
            name="longest happy",
            kind="trial",
            visible=True,
            input={"a": 1, "b": 1, "c": 7},
            expected="ccaccbcc",
            validator={"kind": "longest_happy_string"},
        )

        self.assertTrue(_validated_case_matches(case, "ccbccacc", case.expected))
        self.assertTrue(_longest_happy_string_match("aabbcc", 2, 2, 2))
        self.assertTrue(_longest_happy_string_match("ccaccbcc", 1, 1, 7))
        self.assertFalse(_longest_happy_string_match("ccaccbcca", 1, 1, 7))
        self.assertFalse(_longest_happy_string_match("ccc", 0, 0, 3))
        self.assertFalse(_longest_happy_string_match("aabd", 2, 1, 1))
        self.assertFalse(_longest_happy_string_match(123, 1, 1, 1))

    def test_three_equal_parts_validator_accepts_alternate_zero_splits(self) -> None:
        bits = [0, 0, 0, 0, 0]
        case = ValidatedCase(
            id="three-parts",
            name="three parts",
            kind="sample",
            input={"arr": bits},
            expected=[0, 2],
            validator={"kind": "three_equal_parts"},
        )

        self.assertTrue(_three_equal_parts_match([1, 3], case.expected, bits))
        self.assertTrue(_validated_case_matches(case, [1, 3], case.expected))
        self.assertFalse(_three_equal_parts_match([0, 1], case.expected, bits))
        self.assertFalse(_three_equal_parts_match([0, 5], case.expected, bits))
        self.assertFalse(_three_equal_parts_match([True, 3], case.expected, bits))
        self.assertTrue(_three_equal_parts_match([-1, -1], [-1, -1], [1, 1, 0, 1, 1]))
        self.assertFalse(_three_equal_parts_match([-1, -1], [0, 3], [1, 0, 1, 0, 1]))

    def test_distance_order_validator_accepts_alternate_tie_order(self) -> None:
        source = '''
def solve(rows, cols, r_center, c_center):
    cells = [[row, col] for row in range(rows) for col in range(cols)]
    cells.sort(key=lambda cell: (abs(cell[0] - r_center) + abs(cell[1] - c_center), -cell[0], -cell[1]))
    return cells
'''
        response = self.client.post(
            "/api/challenges/lc_1030/run",
            json={"source": source, "case_ids": ["sample-2"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)

    def test_distant_barcodes_validator_accepts_alternate_arrangement(self) -> None:
        source = '''
from collections import Counter
from heapq import heappop, heappush, heapify

def solve(barcodes):
    heap = [(-count, -value) for value, count in Counter(barcodes).items()]
    heapify(heap)
    previous = None
    result = []
    while heap:
        count, value = heappop(heap)
        value = -value
        result.append(value)
        if previous is not None:
            heappush(heap, previous)
        previous = (count + 1, -value) if count + 1 < 0 else None
    return result
'''
        response = self.client.post(
            "/api/challenges/lc_1054/run",
            json={"source": source, "case_ids": ["sample-1"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)

    def test_rearranged_k_distance_validator_accepts_any_valid_arrangement(self) -> None:
        self.assertTrue(_rearranged_k_distance_match("acbacb", "abcabc", "aabbcc", 3))
        self.assertFalse(_rearranged_k_distance_match("abccab", "abcabc", "aabbcc", 3))
        self.assertFalse(_rearranged_k_distance_match("abcabd", "abcabc", "aabbcc", 3))
        self.assertTrue(_rearranged_k_distance_match("", "", "aaabc", 3))
        self.assertFalse(_rearranged_k_distance_match("", "abcabc", "aabbcc", 3))

    def test_reorganized_string_validator_uses_adjacent_distance(self) -> None:
        case = ValidatedCase(
            id="reorganize",
            name="reorganize",
            kind="trial",
            input={"s": "aabbc"},
            expected="ababc",
            validator={"kind": "reorganized_string"},
        )

        self.assertTrue(_validated_case_matches(case, "abcab", case.expected))
        self.assertFalse(_validated_case_matches(case, "aabbc", case.expected))

    def test_reformatted_string_validator_accepts_any_valid_alternation(self) -> None:
        case = ValidatedCase(
            id="reformat",
            name="reformat",
            kind="trial",
            input={"s": "a0b1c2"},
            expected="0a1b2c",
            validator={"kind": "reformatted_string"},
        )

        self.assertTrue(_validated_case_matches(case, "a0b1c2", case.expected))
        self.assertTrue(_validated_case_matches(case, "2c1b0a", case.expected))
        self.assertFalse(_validated_case_matches(case, "0a1bc2", case.expected))
        self.assertFalse(_validated_case_matches(case, "0a1b2d", case.expected))

        impossible = ValidatedCase(
            id="impossible",
            name="impossible",
            kind="trial",
            input={"s": "abcd1"},
            expected="",
            validator={"kind": "reformatted_string"},
        )
        self.assertTrue(_validated_case_matches(impossible, "", impossible.expected))
        self.assertFalse(_validated_case_matches(impossible, "a1bcd", impossible.expected))


    def test_group_people_validator_accepts_alternate_group_order(self) -> None:
        source = '''
def solve(group_sizes):
    buckets = {}
    groups = []
    for index, size in enumerate(group_sizes):
        bucket = buckets.setdefault(size, [])
        bucket.append(index)
        if len(bucket) == size:
            groups.append(list(reversed(bucket)))
            buckets[size] = []
    return list(reversed(groups))
'''
        response = self.client.post(
            "/api/challenges/lc_1282/run",
            json={"source": source, "case_ids": ["sample-2"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)

    def test_unique_sum_zero_validator_accepts_alternate_values(self) -> None:
        source = '''
def solve(n):
    values = []
    for value in range(1, n // 2 + 1):
        values.extend([-value, value])
    if n % 2:
        values.insert(0, 0)
    return values
'''
        response = self.client.post(
            "/api/challenges/lc_1304/run",
            json={"source": source, "case_ids": ["sample-1"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)

    def test_no_zero_sum_validator_accepts_an_alternate_pair(self) -> None:
        source = '''
def solve(n):
    if n == 11:
        return [8, 3]
    for first in range(1, n):
        second = n - first
        if "0" not in str(first) and "0" not in str(second):
            return [first, second]
'''
        response = self.client.post(
            "/api/challenges/lc_1317/run",
            json={"source": source, "case_ids": ["sample-2"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)

    def test_minimum_subsequence_validator_checks_property_and_minimality(self) -> None:
        nums = [8, 3, 3, 3, 1, 1]
        self.assertTrue(_minimum_subsequence_match([8, 3], nums))
        self.assertFalse(_minimum_subsequence_match([8, 3, 3], nums))
        self.assertFalse(_minimum_subsequence_match([3, 8], nums))

    def test_lcp_string_validator_requires_lexicographically_smallest_string(self) -> None:
        lcp = [[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]
        self.assertTrue(_lcp_string_match("abab", lcp))
        self.assertFalse(_lcp_string_match("baba", lcp))
        long_same = [[27 - max(i, j) for j in range(27)] for i in range(27)]
        self.assertTrue(_lcp_string_match("a" * 27, long_same))

    def test_minimum_unique_rows_matrix_validator_accepts_alternate_rows(self) -> None:
        nums = [1, 3, 4, 1, 2, 3, 1]
        self.assertTrue(_minimum_unique_rows_matrix_match([[1, 3], [1, 3], [1, 4, 2]], nums))
        self.assertFalse(_minimum_unique_rows_matrix_match([[1, 3, 4, 2], [1, 3], [1], []], nums))
        self.assertFalse(_minimum_unique_rows_matrix_match([[1, 1], [3, 4, 2], [1, 3]], nums))

    def test_matrix_margins_validator_accepts_any_non_negative_integer_solution(self) -> None:
        self.assertTrue(_matrix_margins_match([[3, 0], [1, 7]], [3, 8], [4, 7]))
        self.assertTrue(_matrix_margins_match([[1, 2], [3, 5]], [3, 8], [4, 7]))
        self.assertFalse(_matrix_margins_match([[3, 0], [1, 6]], [3, 8], [4, 7]))
        self.assertFalse(_matrix_margins_match([[3, -1], [1, 8]], [2, 9], [4, 7]))
        self.assertFalse(_matrix_margins_match([[True, 2], [3, 5]], [3, 8], [4, 7]))

    def test_float_close_validator_accepts_small_probability_drift(self) -> None:
        self.assertTrue(_float_close_match(0.6666666667, 0.66667, 1e-4))
        self.assertFalse(_float_close_match(0.65, 0.66667, 1e-4))

    def test_sudoku_solution_validator_checks_units_and_preserves_clues(self) -> None:
        solved = [list(row) for row in (
            "534678912", "672195348", "198342567",
            "859761423", "426853791", "713924856",
            "961537284", "287419635", "345286179",
        )]
        clues = [[value if (row + column) % 3 == 0 else "." for column, value in enumerate(values)] for row, values in enumerate(solved)]
        self.assertTrue(_sudoku_solution_match(solved, clues))
        changed_clue = [row[:] for row in solved]
        changed_clue[0][0], changed_clue[0][1] = changed_clue[0][1], changed_clue[0][0]
        self.assertFalse(_sudoku_solution_match(changed_clue, clues))
        duplicate = [row[:] for row in solved]
        duplicate[0][0] = duplicate[0][1]
        self.assertFalse(_sudoku_solution_match(duplicate, [["."] * 9 for _ in range(9)]))

    def test_anagram_groups_validator_ignores_both_ordering_levels(self) -> None:
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertTrue(
            _anagram_groups_match([["bat"], ["nat", "tan"], ["ate", "tea", "eat"]], expected)
        )
        self.assertFalse(_anagram_groups_match([["bat"], ["nat"], ["ate", "tea", "eat"]], expected))

    def test_frequency_sorted_string_validator_accepts_tied_groups(self) -> None:
        self.assertTrue(_frequency_sorted_string_match("eert", "tree"))
        self.assertTrue(_frequency_sorted_string_match("eetr", "tree"))
        self.assertFalse(_frequency_sorted_string_match("etre", "tree"))
        self.assertFalse(_frequency_sorted_string_match("eeer", "tree"))

    def test_custom_sorted_string_validator_allows_unranked_characters_anywhere(self) -> None:
        self.assertTrue(_custom_sorted_string_match("dccbaax", "cba", "abcdaxc"))
        self.assertTrue(_custom_sorted_string_match("xdccbaa", "cba", "abcdaxc"))
        self.assertFalse(_custom_sorted_string_match("acbaxcd", "cba", "abcdaxc"))
        self.assertFalse(_custom_sorted_string_match("dccbaay", "cba", "abcdaxc"))

    def test_question_mark_replacement_validator_accepts_any_valid_completion(self) -> None:
        self.assertTrue(_question_mark_replacement_match("azs", "?zs"))
        self.assertTrue(_question_mark_replacement_match("bzs", "?zs"))
        self.assertTrue(_question_mark_replacement_match("acba", "a??a"))
        self.assertFalse(_question_mark_replacement_match("aas", "?zs"))
        self.assertFalse(_question_mark_replacement_match("aza", "?zs"))
        self.assertFalse(_question_mark_replacement_match("az?", "?zs"))

    def test_gray_code_validator_checks_cycle_and_domain(self) -> None:
        self.assertTrue(_gray_code_match([0, 1, 3, 2], 2))
        self.assertTrue(_gray_code_match([0, 2, 3, 1], 2))
        self.assertFalse(_gray_code_match([0, 1, 2, 3], 2))
        self.assertFalse(_gray_code_match([0, 1, 3, 3], 2))

    def test_circular_gray_code_validator_respects_requested_start(self) -> None:
        self.assertTrue(_circular_gray_code_match([3, 2, 0, 1], 2, 3))
        self.assertTrue(_circular_gray_code_match([3, 1, 0, 2], 2, 3))
        self.assertFalse(_circular_gray_code_match([0, 1, 3, 2], 2, 3))
        self.assertFalse(_circular_gray_code_match([3, 2, 1, 0], 2, 3))

    def test_unordered_nested_list_validator_ignores_both_ordering_levels(self) -> None:
        expected = [[], [1], [2], [1, 2]]
        self.assertTrue(_unordered_nested_list_matches([[2, 1], [2], [], [1]], expected))
        self.assertFalse(_unordered_nested_list_matches([[2, 1], [2], [], [2]], expected))

    def test_ordered_groups_validator_preserves_categories(self) -> None:
        expected = [[0, 1], [2, 3, 4]]
        self.assertTrue(_ordered_groups_unordered_items_match([[1, 0], [4, 2, 3]], expected))
        self.assertFalse(_ordered_groups_unordered_items_match([[4, 2, 3], [1, 0]], expected))
        self.assertFalse(_ordered_groups_unordered_items_match([[0, 1], [2, 3]], expected))

    def test_ordered_unordered_groups_validator_preserves_round_order(self) -> None:
        expected = [[4, 5, 3], [2], [1]]
        self.assertTrue(_ordered_unordered_groups_match([[3, 4, 5], [2], [1]], expected))
        self.assertFalse(_ordered_unordered_groups_match([[2], [3, 4, 5], [1]], expected))
        self.assertFalse(_ordered_unordered_groups_match([[3, 4], [2], [1]], expected))

    def test_circular_doubly_tree_validator_checks_order_links_and_closure(self) -> None:
        class Node:
            def __init__(self, value: int) -> None:
                self.val = value
                self.left = None
                self.right = None

        nodes = [Node(value) for value in (1, 2, 3)]
        for index, node in enumerate(nodes):
            node.left = nodes[index - 1]
            node.right = nodes[(index + 1) % len(nodes)]

        self.assertTrue(_circular_doubly_tree_match(nodes[0], [1, 2, 3]))
        self.assertFalse(_circular_doubly_tree_match(nodes[1], [1, 2, 3]))
        nodes[1].left = nodes[1]
        self.assertFalse(_circular_doubly_tree_match(nodes[0], [1, 2, 3]))
        self.assertTrue(_circular_doubly_tree_match(None, []))

    def test_quad_tree_validator_checks_leaf_values_and_quadrant_order(self) -> None:
        from types import SimpleNamespace

        def leaf(value: bool):
            return SimpleNamespace(
                val=value,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )

        root = SimpleNamespace(
            val=True,
            isLeaf=False,
            topLeft=leaf(True),
            topRight=leaf(False),
            bottomLeft=leaf(False),
            bottomRight=leaf(True),
        )
        expected = {
            "leaf": False,
            "children": [
                {"leaf": True, "value": 1},
                {"leaf": True, "value": 0},
                {"leaf": True, "value": 0},
                {"leaf": True, "value": 1},
            ],
        }
        self.assertTrue(_quad_tree_match(root, expected))
        root.bottomRight.val = False
        self.assertFalse(_quad_tree_match(root, expected))

    def test_flattened_multilevel_validator_checks_prev_and_cleared_children(self) -> None:
        from types import SimpleNamespace

        nodes = [SimpleNamespace(val=value, prev=None, next=None, child=None) for value in (1, 2, 3)]
        for index in range(1, len(nodes)):
            nodes[index - 1].next = nodes[index]
            nodes[index].prev = nodes[index - 1]

        self.assertTrue(_flattened_multilevel_list_match(nodes[0], [1, 2, 3]))
        nodes[1].child = nodes[2]
        self.assertFalse(_flattened_multilevel_list_match(nodes[0], [1, 2, 3]))
        nodes[1].child = None
        nodes[2].prev = nodes[0]
        self.assertFalse(_flattened_multilevel_list_match(nodes[0], [1, 2, 3]))
        self.assertTrue(_flattened_multilevel_list_match(None, []))

    def test_all_one_trace_validator_accepts_tied_extreme_keys(self) -> None:
        operations = [
            ["inc", "alpha"],
            ["inc", "beta"],
            ["getMaxKey"],
            ["getMinKey"],
            ["inc", "alpha"],
            ["getMaxKey"],
            ["getMinKey"],
            ["dec", "alpha"],
            ["dec", "alpha"],
            ["dec", "beta"],
            ["getMaxKey"],
        ]
        self.assertTrue(_all_one_trace_match(["beta", "alpha", "alpha", "beta", ""], operations))
        self.assertFalse(_all_one_trace_match(["alpha", "beta", "beta", "alpha", ""], operations))

    def test_largest_divisible_subset_validator_accepts_optimal_ties(self) -> None:
        values = [1, 2, 3]
        self.assertTrue(_largest_divisible_subset_match([1, 3], [1, 2], values))
        self.assertTrue(_largest_divisible_subset_match([3, 1], [1, 2], values))
        self.assertFalse(_largest_divisible_subset_match([1], [1, 2], values))
        self.assertFalse(_largest_divisible_subset_match([1, 2, 2], [1, 2, 3], values))
        self.assertFalse(_largest_divisible_subset_match([2, 3], [1, 2], values))

    def test_k_smallest_pairs_validator_accepts_ties_and_checks_multiplicity(self) -> None:
        nums1 = [1, 1, 2]
        nums2 = [1, 2]
        self.assertTrue(_k_smallest_pairs_match([[1, 1], [1, 1], [1, 2]], nums1, nums2, 3))
        self.assertTrue(_k_smallest_pairs_match([[1, 1], [1, 1], [2, 1]], nums1, nums2, 3))
        self.assertFalse(_k_smallest_pairs_match([[1, 1], [1, 1], [1, 1]], nums1, nums2, 3))
        self.assertFalse(_k_smallest_pairs_match([[1, 1], [1, 1], [2, 2]], nums1, nums2, 3))
        self.assertTrue(_k_smallest_pairs_match([], [], nums2, 3))

    def test_phone_directory_trace_validator_accepts_alternate_allocations(self) -> None:
        operations = [["get"], ["get"], ["check", 2], ["release", 1], ["check", 1], ["get"]]
        self.assertTrue(_phone_directory_trace_match([1, 0, True, True, 1], 3, operations))
        self.assertTrue(_phone_directory_trace_match([2, 1, False, True, 1], 3, operations))
        self.assertFalse(_phone_directory_trace_match([1, 1, True, True, 1], 3, operations))
        self.assertFalse(_phone_directory_trace_match([1, 0, False, True, 1], 3, operations))
        self.assertTrue(_phone_directory_trace_match([0, -1], 1, [["get"], ["get"]]))

    def test_randomized_set_trace_validator_accepts_any_current_member(self) -> None:
        operations = [["insert", 1], ["insert", 2], ["getRandom"], ["remove", 1], ["getRandom"]]
        self.assertTrue(_randomized_set_trace_match([True, True, 1, True, 2], operations))
        self.assertTrue(_randomized_set_trace_match([True, True, 2, True, 2], operations))
        self.assertFalse(_randomized_set_trace_match([True, True, 3, True, 2], operations))
        self.assertFalse(_randomized_set_trace_match([True, True, 1, False, 2], operations))
        self.assertFalse(_randomized_set_trace_match([True, True, 1, True, 1], operations))

    def test_randomized_collection_trace_validator_tracks_multiplicity(self) -> None:
        operations = [["insert", 1], ["insert", 1], ["remove", 1], ["getRandom"], ["remove", 1]]
        self.assertTrue(_randomized_collection_trace_match([True, False, True, 1, True], operations))
        self.assertFalse(_randomized_collection_trace_match([True, True, True, 1, True], operations))
        self.assertFalse(_randomized_collection_trace_match([True, False, True, 2, True], operations))
        self.assertFalse(_randomized_collection_trace_match([True, False, True, 1, False], operations))

    def test_linked_list_random_draws_validator_accepts_any_list_value(self) -> None:
        self.assertTrue(_linked_list_random_draws_match([1, 3, 2, 3], [1, 2, 3], 4))
        self.assertTrue(_linked_list_random_draws_match([-5, -5], [-5], 2))
        self.assertTrue(_linked_list_random_draws_match([], [1, 2], 0))
        self.assertFalse(_linked_list_random_draws_match([1, 4], [1, 2, 3], 2))
        self.assertFalse(_linked_list_random_draws_match([1], [1, 2, 3], 2))
        self.assertFalse(_linked_list_random_draws_match([], [], 0))

    def test_shuffle_array_trace_validator_checks_permutations_and_resets(self) -> None:
        operations = ["shuffle", "reset", "shuffle"]
        self.assertTrue(_shuffle_array_trace_match([[2, 1, 2], [1, 2, 2], [2, 2, 1]], [1, 2, 2], operations))
        self.assertTrue(_shuffle_array_trace_match([[1, 2], [1, 2]], [1, 2], ["shuffle", "reset"]))
        self.assertFalse(_shuffle_array_trace_match([[2, 1, 2], [2, 1, 2], [1, 2, 2]], [1, 2, 2], operations))
        self.assertFalse(_shuffle_array_trace_match([[1, 2, 3]], [1, 2, 2], ["shuffle"]))
        self.assertFalse(_shuffle_array_trace_match([[1, 2]], [1, 2], ["rotate"]))

    def test_random_pick_indices_validator_accepts_any_matching_occurrence(self) -> None:
        nums = [1, 2, 3, 3, 3]
        targets = [3, 1, 3]
        self.assertTrue(_random_pick_indices_match([2, 0, 4], nums, targets))
        self.assertTrue(_random_pick_indices_match([3, 0, 3], nums, targets))
        self.assertFalse(_random_pick_indices_match([1, 0, 4], nums, targets))
        self.assertFalse(_random_pick_indices_match([2, 0], nums, targets))
        self.assertFalse(_random_pick_indices_match([5, 0, 2], nums, targets))

    def test_float_list_close_validator_applies_tolerance_per_result(self) -> None:
        self.assertTrue(_float_list_close_match([6.0000001, 0.5, -1], [6.0, 0.5, -1.0], 1e-5))
        self.assertFalse(_float_list_close_match([6.01, 0.5], [6.0, 0.5], 1e-5))
        self.assertFalse(_float_list_close_match([1.0], [1.0, 2.0], 1e-5))
        self.assertFalse(_float_list_close_match([True], [1.0], 1e-5))

    def test_float_matrix_close_validator_applies_tolerance_per_coordinate(self) -> None:
        self.assertTrue(
            _float_matrix_close_match(
                [[1.0, 2.0], [3.0, 4.0]],
                [[1.0, 2.000001], [3.0, 4.0]],
                1e-5,
            )
        )
        self.assertFalse(_float_matrix_close_match([[1.0, 2.0]], [[1.0, 2.1]], 1e-5))

    def test_queue_reconstruction_validator_checks_multiset_and_front_counts(self) -> None:
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        self.assertTrue(_queue_reconstruction_match([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]], people))
        self.assertFalse(_queue_reconstruction_match([[7, 0], [5, 0], [5, 2], [6, 1], [4, 4], [7, 1]], people))
        self.assertFalse(_queue_reconstruction_match([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [6, 1]], people))
        self.assertFalse(_queue_reconstruction_match([[5, 0], [7, 0]], people))

    def test_advantage_shuffle_validator_checks_permutation_and_optimal_wins(self) -> None:
        nums1 = [2, 7, 11, 15]
        nums2 = [1, 10, 4, 11]
        self.assertTrue(_advantage_shuffle_match([2, 11, 7, 15], nums1, nums2))
        self.assertFalse(_advantage_shuffle_match([15, 11, 7, 2], nums1, nums2))
        self.assertFalse(_advantage_shuffle_match([2, 11, 7, 16], nums1, nums2))
        self.assertTrue(_advantage_shuffle_match([2, 2, 3], [2, 2, 3], [1, 1, 2]))
        self.assertFalse(_advantage_shuffle_match([True], [1], [0]))

    def test_fair_candy_swap_validator_accepts_any_balancing_pair(self) -> None:
        alice_sizes = [1, 2, 3, 4]
        bob_sizes = [3, 4, 5, 6]

        self.assertTrue(_fair_candy_swap_match([1, 5], alice_sizes, bob_sizes))
        self.assertTrue(_fair_candy_swap_match([2, 6], alice_sizes, bob_sizes))
        self.assertTrue(_fair_candy_swap_match((1, 5), alice_sizes, bob_sizes))
        self.assertFalse(_fair_candy_swap_match([1, 6], alice_sizes, bob_sizes))
        self.assertFalse(_fair_candy_swap_match([9, 13], alice_sizes, bob_sizes))
        self.assertFalse(_fair_candy_swap_match([True, 5], alice_sizes, bob_sizes))

    def test_minimum_unique_abbreviation_validator_checks_meaning_and_token_length(self) -> None:
        self.assertTrue(_minimum_unique_abbreviation_match("a4", "a4", "apple", ["blade"]))
        self.assertFalse(_minimum_unique_abbreviation_match("4e", "a4", "apple", ["blade"]))
        self.assertFalse(_minimum_unique_abbreviation_match("3l1", "a4", "apple", ["blade"]))
        self.assertFalse(_minimum_unique_abbreviation_match("05", "a4", "apple", ["blade"]))

    def test_unique_bsts_validator_checks_count_order_and_structure(self) -> None:
        class TreeNode:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        valid = [TreeNode(1, right=TreeNode(2)), TreeNode(2, left=TreeNode(1))]
        self.assertTrue(_unique_bsts_match(valid, 2))
        self.assertFalse(_unique_bsts_match(valid[:1], 2))
        self.assertFalse(_unique_bsts_match([valid[0], valid[0]], 2))
        self.assertFalse(_unique_bsts_match([TreeNode(2, right=TreeNode(1)), valid[1]], 2))

    def test_duplicate_subtrees_validator_serializes_representatives_and_ignores_order(self) -> None:
        class TreeNode:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        leaf = TreeNode(4)
        branch = TreeNode(2, left=TreeNode(4))
        self.assertTrue(_duplicate_subtrees_match([leaf, branch], [[2, 4], [4]]))
        self.assertFalse(_duplicate_subtrees_match([leaf], [[2, 4], [4]]))
        self.assertFalse(_duplicate_subtrees_match([leaf, TreeNode(2)], [[2, 4], [4]]))
        self.assertFalse(_duplicate_subtrees_match([[4]], [[4]]))

    def test_beautiful_arrangement_ii_validator_checks_permutation_and_difference_count(self) -> None:
        self.assertTrue(_beautiful_arrangement_ii_match([1, 4, 2, 3], 4, 3))
        self.assertTrue(_beautiful_arrangement_ii_match([1, 3, 2, 4], 4, 2))
        self.assertFalse(_beautiful_arrangement_ii_match([1, 2, 3, 4], 4, 2))
        self.assertFalse(_beautiful_arrangement_ii_match([1, 4, 2, 2], 4, 3))
        self.assertFalse(_beautiful_arrangement_ii_match([0, 3, 1, 2], 4, 3))

    def test_next_right_pointer_validator_checks_identity_links(self) -> None:
        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
                self.next = None

        root = Node(1, Node(2), Node(3))
        root.left.next = root.right
        self.assertTrue(_next_right_pointers_match(root, [1, 2, 3]))
        root.left.next = None
        self.assertFalse(_next_right_pointers_match(root, [1, 2, 3]))
        root.left.next = Node(3)
        self.assertFalse(_next_right_pointers_match(root, [1, 2, 3]))

    def test_avoid_flood_validator_accepts_alternate_valid_dry_plan(self) -> None:
        rains = [1, 2, 0, 0, 1]
        self.assertTrue(_avoid_flood_match([-1, -1, 1, 2, -1], [-1, -1, 1, 1, -1], rains))
        self.assertFalse(_avoid_flood_match([-1, -1, 2, 2, -1], [-1, -1, 1, 1, -1], rains))

    def test_good_subset_matrix_validator_accepts_alternate_valid_rows(self) -> None:
        grid = [[1, 0, 0], [0, 1, 0], [1, 1, 1], [0, 0, 0]]
        self.assertTrue(_good_subset_matrix_match([0, 1], grid, [3]))
        self.assertTrue(_good_subset_matrix_match([3], grid, [3]))
        self.assertFalse(_good_subset_matrix_match([0, 2], grid, [3]))
        self.assertFalse(_good_subset_matrix_match([1, 0], grid, [3]))

    def test_neither_min_nor_max_validator_accepts_any_middle_value(self) -> None:
        nums = [5, 1, 4, 2]
        self.assertTrue(_neither_min_nor_max_match(4, nums, 2))
        self.assertTrue(_neither_min_nor_max_match(2, nums, 2))
        self.assertFalse(_neither_min_nor_max_match(1, nums, 2))
        self.assertFalse(_neither_min_nor_max_match(5, nums, 2))

    def test_alternating_groups_validator_accepts_any_longest_subsequence(self) -> None:
        words = ["a", "b", "c", "d"]
        groups = [1, 0, 1, 1]
        self.assertTrue(_alternating_groups_subsequence_match(["a", "b", "c"], words, groups, ["a", "b", "c"]))
        self.assertTrue(_alternating_groups_subsequence_match(["a", "b", "d"], words, groups, ["a", "b", "c"]))
        self.assertFalse(_alternating_groups_subsequence_match(["a", "c"], words, groups, ["a", "b", "c"]))
        self.assertFalse(_alternating_groups_subsequence_match(["a", "c", "d"], words, groups, ["a", "b", "c"]))

    def test_hamming_alternating_validator_checks_word_distance(self) -> None:
        words = ["aaa", "aba", "abb", "bbb"]
        groups = [0, 1, 0, 1]
        self.assertTrue(_hamming_alternating_subsequence_match(["aaa", "aba", "abb", "bbb"], words, groups, ["aaa", "aba", "abb", "bbb"]))
        self.assertFalse(_hamming_alternating_subsequence_match(["aaa", "abb"], words, groups, ["aaa", "aba"]))
        self.assertFalse(_hamming_alternating_subsequence_match(["aaa", "aba"], words, [0, 0, 0, 1], ["aaa", "aba"]))

    def test_index_value_pair_validator_accepts_any_valid_pair(self) -> None:
        nums = [5, 1, 4, 1]
        self.assertTrue(_index_value_pair_match([0, 3], nums, 2, 4))
        self.assertTrue(_index_value_pair_match([3, 0], nums, 2, 4))
        self.assertFalse(_index_value_pair_match([0, 2], nums, 2, 4))
        self.assertTrue(_index_value_pair_match([-1, -1], [1, 2, 3], 2, 4))
        self.assertFalse(_index_value_pair_match([-1, -1], nums, 2, 4))

    def test_linked_list_input_hint_is_converted_for_validated_cases(self) -> None:
        spec = CHALLENGE_REGISTRY["lc_2326"]()._spec
        self.assertEqual(_list_node_param_names(spec), ["head"])

    def test_linked_list_return_is_normalized_for_validated_cases(self) -> None:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual(_list_node_to_values(head), [1, 2, 3])

    def test_list_of_linked_list_heads_is_normalized_for_validated_cases(self) -> None:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        parts = [ListNode(1, ListNode(2)), None, ListNode(3)]
        self.assertEqual(_list_node_to_values(parts), [[1, 2], [], [3]])
        self.assertEqual(_list_node_to_values([[1, 2], [], [3]]), [[1, 2], [], [3]])
        self.assertTrue(_returns_list_node("a list of linked-list heads"))

    def test_cyclic_linked_list_encoding_builds_requested_cycle(self) -> None:
        head = _list_node_from_values({"values": [3, 2, 0, -4], "pos": 1})
        self.assertEqual(head.val, 3)
        self.assertEqual(head.next.next.next.next, head.next)
        self.assertIsNone(_list_node_from_values({"values": [], "pos": -1}))

    def test_shared_tail_encoding_preserves_identity_across_two_heads(self) -> None:
        values = _prepare_validated_kwargs(
            {
                "head_a": {"prefix": [4, 1], "shared": [8, 4, 5]},
                "head_b": {"prefix": [5, 6, 1], "shared": [8, 4, 5]},
            },
            (),
            ("head_a", "head_b"),
        )
        intersection_a = values["head_a"].next.next
        intersection_b = values["head_b"].next.next.next
        self.assertIs(intersection_a, intersection_b)
        self.assertEqual(_list_node_to_values(intersection_a), [8, 4, 5])

    def test_nested_quad_tree_fixture_is_converted_to_node_objects(self) -> None:
        values = _prepare_validated_kwargs(
            {
                "quadTree1": {
                    "leaf": False,
                    "children": [
                        {"leaf": True, "value": 1},
                        {"leaf": True, "value": 0},
                        {"leaf": True, "value": 0},
                        {"leaf": True, "value": 1},
                    ],
                }
            },
            (),
        )
        root = values["quadTree1"]
        self.assertFalse(root.isLeaf)
        self.assertTrue(root.topLeft.isLeaf)
        self.assertTrue(root.topLeft.val)
        self.assertFalse(root.topRight.val)

    def test_peak_index_validator_accepts_any_strict_local_peak(self) -> None:
        nums = [1, 3, 2, 5, 4]
        self.assertTrue(_peak_index_match(1, nums))
        self.assertTrue(_peak_index_match(3, nums))
        self.assertFalse(_peak_index_match(2, nums))
        self.assertFalse(_peak_index_match(True, nums))

    def test_tree_root_node_hint_is_converted_for_validated_cases(self) -> None:
        spec = CHALLENGE_REGISTRY["lc_2458"]()._spec
        self.assertEqual(_tree_param_names(spec), ["root"])

    def test_tree_root_return_hint_is_normalized_for_validated_cases(self) -> None:
        spec = CHALLENGE_REGISTRY["lc_226"]()._spec
        self.assertTrue(_returns_tree(spec.returns))

    def test_optional_none_return_is_not_treated_as_in_place(self) -> None:
        self.assertFalse(
            _returns_in_place(
                "The pruned tree root, or `None` when the entire tree is removed."
            )
        )
        self.assertFalse(
            _returns_in_place(
                "List of method results; `set` returns `None` and `get` returns a value."
            )
        )

    def test_explicit_no_value_return_is_treated_as_in_place(self) -> None:
        self.assertTrue(_returns_in_place("`None`; mutate the tree in place."))
        self.assertTrue(_returns_in_place("Returns `None`; mutate the board in place."))
        self.assertTrue(_returns_in_place("Return nothing. Mutate `nums` in place."))
        self.assertTrue(_returns_in_place("No value is returned; `arr` is changed in place."))
