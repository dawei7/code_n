"""Tests for the AST-based op counter (``server.app.ast_ops``).

The counter walks the source's AST and sums operations,
multiplied by the enclosing loop iteration count. These
tests pin down the algorithm's behavior for the patterns
that show up in the cOde(n) solution corpus: simple loops,
nested loops, comparisons, subscripts, binops, conditionals.
"""
from __future__ import annotations

import unittest

from server.app.ast_ops import _count_block, _eval_int, _range_iter_count, count_ops


class CountOpsTest(unittest.TestCase):
    """The high-level ``count_ops(source, n)`` entry point."""

    def test_empty_source_is_zero(self) -> None:
        self.assertEqual(count_ops("", 10), 0)

    def test_syntax_error_is_zero(self) -> None:
        # Gracefully handled — a syntax error is surfaced
        # elsewhere; the counter just returns 0.
        self.assertEqual(count_ops("def solve(:\n    pass\n", 10), 0)

    def test_pure_assignment_is_one(self) -> None:
        # ``x = 1`` is one Assign (1 op) + one Constant (no op).
        self.assertEqual(count_ops("x = 1", 10), 1)

    def test_simple_if_no_else(self) -> None:
        # ``if x > 0: pass`` is one Compare (1) + one If (1) + pass (0).
        # The def itself is not counted (one-time setup).
        self.assertEqual(count_ops("def solve(x):\n    if x > 0:\n        pass\n", 10), 2)

    def test_if_with_else(self) -> None:
        # ``if x > 0: a = 1 else: a = 2``
        # 1 compare + 1 if + 1 assign (then) + 1 assign (else) = 4
        self.assertEqual(
            count_ops("def solve(x):\n    if x > 0:\n        a = 1\n    else:\n        a = 2\n", 10),
            4,
        )

    def test_single_loop_runs_n_times(self) -> None:
        # ``for i in range(n): x = i`` is:
        #   - 1 for (the for itself)
        #   - n × (1 assign)  = n
        # Total: 1 + n
        self.assertEqual(count_ops("for i in range(n):\n    x = i\n", 16), 1 + 16)

    def test_nested_loop_runs_n_squared_times(self) -> None:
        # ``for i in range(n): for j in range(n): x = i + j``
        # Outer: 1 for + n × (1 for + n × (1 binop + 1 assign))
        #     = 1 + n × (1 + n × 2)
        #     = 1 + n + 2n²
        self.assertEqual(
            count_ops(
                "for i in range(n):\n    for j in range(n):\n        x = i + j\n",
                16,
            ),
            1 + 16 + 2 * 16 * 16,
        )

    def test_subscript_counts(self) -> None:
        # ``arr[i]`` is 1 subscript; ``arr[i + 1]`` is 1 subscript
        # + 1 binop (the i+1 inside). The outer ``arr[i] + arr[i+1]``
        # is 1 outer binop. The assignment is 1 op. So per
        # iteration: 1 (assign) + 1 (outer binop) + 1 (left subs)
        # + 2 (right subs + inner binop) = 5.
        # Plus 1 for the for itself: 1 + n × 5.
        self.assertEqual(
            count_ops(
                "for i in range(n):\n    s = arr[i] + arr[i + 1]\n",
                10,
            ),
            1 + 5 * 10,
        )

    def test_attribute_access_counts(self) -> None:
        # ``obj.attr`` is 1 Attribute; ``obj.method()`` is 1 Attr + 1 Call.
        source = (
            "for i in range(n):\n"
            "    x = obj.value + obj.method()\n"
        )
        # 1 (for) + n × (1 assign + 1 binop + 1 attr + 1 attr + 1 call) = 1 + 5n
        self.assertEqual(count_ops(source, 10), 1 + 5 * 10)

    def test_function_call_in_loop(self) -> None:
        # ``sorted(data)`` is 1 Call. ``for x in data: helper(x)`` is
        # 1 for + n × (1 call).
        source = (
            "for x in data:\n"
            "    helper(x)\n"
        )
        # 1 (for) + n × (1 call) = 1 + n
        # We treat the ``for x in data`` iter count as n
        # (it's a Name, not a range call, so the conservative
        # fallback applies).
        self.assertEqual(count_ops(source, 16), 1 + 16)

    def test_range_with_start_stop(self) -> None:
        # ``range(1, n)`` iterates n-1 times.
        # 1 (for) + (n-1) × (1 assign) = 1 + (n-1) = n
        source = "for i in range(1, n):\n    x = i\n"
        self.assertEqual(count_ops(source, 16), 16)

    def test_range_with_step(self) -> None:
        # ``range(0, n, 2)`` iterates ceil(n/2) times.
        # 1 (for) + ceil(n/2) × (1 assign) = 1 + ceil(n/2)
        source = "for i in range(0, n, 2):\n    x = i\n"
        self.assertEqual(count_ops(source, 16), 1 + 8)

    def test_nested_loop_with_inner_range_n_minus_1(self) -> None:
        # ``for i in range(n-1): for j in range(n-1-i): ...``
        # Inner range iter count is (n-1) - i. The inner body runs
        # sum_{i=0}^{n-2} (n-1-i) = (n-1)n/2 times.
        # We don't try to be that precise; the test just
        # ensures the count is positive and bounded.
        source = (
            "for i in range(n - 1):\n"
            "    for j in range(n - 1 - i):\n"
            "        if data[j] > data[j + 1]:\n"
            "            data[j], data[j + 1] = data[j + 1], data[j]\n"
        )
        count = count_ops(source, 16)
        # We don't assert an exact number (the inner range's
        # iteration count depends on i, which we approximate
        # as n-1), but the count must be > 0 and bounded.
        self.assertGreater(count, 100)
        self.assertLess(count, 10_000)

    def test_compare_with_and(self) -> None:
        # ``a and b`` is 1 BoolOp (with 2 values). Each side is 1 Name.
        # In a loop: 1 (for) + n × (1 boolop + 1 if) = 1 + 2n.
        source = (
            "for i in range(n):\n"
            "    if a and b:\n"
            "        pass\n"
        )
        # 1 (for) + n × (1 boolop + 1 if + 0 pass) = 1 + 2n
        self.assertEqual(count_ops(source, 10), 1 + 2 * 10)

    def test_unary_op_counts(self) -> None:
        # ``-x`` is 1 UnaryOp. In a loop: 1 + 2n.
        source = (
            "for i in range(n):\n"
            "    y = -x\n"
        )
        # 1 (for) + n × (1 assign + 1 unary) = 1 + 2n
        self.assertEqual(count_ops(source, 10), 1 + 2 * 10)

    def test_dict_literal_in_loop(self) -> None:
        # ``{x: 1}`` is 1 Dict (no op). Just the loop + 1 assign.
        source = (
            "for i in range(n):\n"
            "    d = {i: 1}\n"
        )
        self.assertEqual(count_ops(source, 10), 1 + 10)

    def test_while_loop(self) -> None:
        # ``while x: pass`` is conservatively n × (1 while + 0 pass).
        source = (
            "while x:\n"
            "    pass\n"
        )
        # n × (1 while + 0 pass) = n
        self.assertEqual(count_ops(source, 10), 10)


class EvalIntTest(unittest.TestCase):
    """The literal-int evaluator used to infer range bounds."""

    def test_literal_int(self) -> None:
        self.assertEqual(_eval_int(__import__("ast").parse("42").body[0].value, 10), 42)

    def test_name_n(self) -> None:
        self.assertEqual(_eval_int(__import__("ast").parse("n").body[0].value, 10), 10)

    def test_name_other_is_none(self) -> None:
        self.assertIsNone(_eval_int(__import__("ast").parse("k").body[0].value, 10))

    def test_unary_neg(self) -> None:
        ast = __import__("ast")
        self.assertEqual(_eval_int(ast.parse("-n").body[0].value, 10), -10)

    def test_binop(self) -> None:
        ast = __import__("ast")
        # ``n - 1``
        self.assertEqual(_eval_int(ast.parse("n - 1").body[0].value, 16), 15)
        # ``2 * 4``
        self.assertEqual(_eval_int(ast.parse("2 * 4").body[0].value, 16), 8)

    def test_len_call_returns_n(self) -> None:
        ast = __import__("ast")
        self.assertEqual(_eval_int(ast.parse("len(x)").body[0].value, 10), 10)


class RangeIterCountTest(unittest.TestCase):
    """Inferring the iteration count of a ``for x in range(...):``."""

    def test_range_stop(self) -> None:
        ast = __import__("ast").parse("for i in range(n): pass").body[0]
        self.assertEqual(_range_iter_count(ast.iter, 10), 10)

    def test_range_start_stop(self) -> None:
        ast = __import__("ast").parse("for i in range(0, n): pass").body[0]
        self.assertEqual(_range_iter_count(ast.iter, 10), 10)

    def test_range_start_stop_step(self) -> None:
        ast = __import__("ast").parse("for i in range(0, n, 2): pass").body[0]
        self.assertEqual(_range_iter_count(ast.iter, 10), 5)

    def test_range_with_minus_1(self) -> None:
        ast = __import__("ast").parse("for i in range(n - 1): pass").body[0]
        self.assertEqual(_range_iter_count(ast.iter, 16), 15)

    def test_unknown_iter_falls_back_to_n(self) -> None:
        # ``for x in data:`` — the iter is a Name, not a
        # range call, so we fall back to n.
        ast = __import__("ast").parse("for x in data: pass").body[0]
        self.assertEqual(_range_iter_count(ast.iter, 16), 16)
