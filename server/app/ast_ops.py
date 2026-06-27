"""AST-based op counter — counts "real" operations by walking
the source's AST.

Why this exists
---------------
The engine's runtime ``OperationCounter`` (in ``code_n.counter``)
counts ops that flow through the ``TrackedList`` /
``TrackedValue`` proxies — reads, writes, compares, swaps, calls.
It does NOT count:

  * Plain attribute access (``obj.attr``)
  * Subscript access on a non-tracked list (``arr[i]`` when
    ``arr`` is a regular list)
  * BinOp / UnaryOp on plain values (``i + 1``, ``-x``)
  * Attribute-assignment targets (``self.x = ...``)
  * ``if`` / ``while`` conditions
  * Loop overhead (the per-iteration compare for ``for i in
    range(n):``)

That gap matters when the user wants to know "how many real
operations does this code do?" — e.g. for the Complexity tab.
We count the operations that the user can SEE in the source
(``if``, ``for``, ``arr[i]``, ``x > 0``) so the count matches
their intuition.

The counter
----------
We walk the AST once, multiplying by an enclosing-loop
multiplier:

  * Each ``Compare`` / ``BinOp`` / ``UnaryOp`` / ``BoolOp`` /
    ``Call`` / ``Subscript`` / ``Attribute`` node = 1 op.
  * Calls to common Python/C-library operations include their hidden
    traversal cost.  For example, ``Counter(data)`` and ``sum(data)``
    cost ``n``, ``sorted(data)`` costs ``n log n``, and heap/bisect
    operations cost ``log n`` rather than one opaque call.
  * Each ``If`` adds 1 (the condition check), plus the
    body.
  * Each ``For`` multiplies the body by the iteration count
    (we infer this from ``range(...)`` calls; for
    ``range(n)`` it's ``n``; for ``range(n - 1)`` it's
    ``n - 1``; for unknown ranges we fall back to ``n``).
  * Each ``While`` multiplies the body by ``n`` (we can't
    know the exact trip count statically).
  * Each ``Assign`` / ``AugAssign`` / ``AnnAssign`` adds 1
    for the assignment, plus the value-side.

The result is a single integer: the "theoretical" op count
for this source under input size ``n``. Used by the Complexity
tab to compare the user's count against the reference's
count, with a deterministic ±5% tolerance band.
"""
from __future__ import annotations

import ast
import math
from typing import Optional


# AST node types that we count as "one operation each". This
# is the set of nodes the user can see in their code that
# would have a runtime cost.
_OP_NODES: tuple[type[ast.AST], ...] = (
    ast.Compare,
    ast.BinOp,
    ast.UnaryOp,
    ast.BoolOp,
    ast.Call,
    ast.Subscript,
    ast.Attribute,
)


def count_ops(source: str, n: int) -> int:
    """Count operations in ``source`` as if it ran on input
    size ``n``.

    Returns 0 if the source doesn't parse.

    The count is deterministic — same source, same ``n``,
    same result. No randomness, no runtime data needed.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return 0
    return _count_block(tree.body, multiplier=1, n=n)


def _count_block(
    body: list[ast.stmt],
    multiplier: int,
    n: int,
) -> int:
    """Sum the op counts of every statement in ``body``,
    scaled by the enclosing ``multiplier``.

    ``multiplier`` is the product of the iteration counts of
    all enclosing loops. For top-level code, it's 1. For the
    body of a single ``for i in range(n):`` loop at the top
    level, it's ``n``. For ``for i in range(n): for j in
    range(n):``, the inner body has multiplier ``n * n``.

    Loops in the middle of a block inherit the multiplier;
    only the loop's own iteration count is multiplied in.
    """
    if multiplier == 0:
        return 0
    total = 0
    for stmt in body:
        total += _count_stmt(stmt, multiplier, n)
    return total


def _count_stmt(stmt: ast.stmt, multiplier: int, n: int) -> int:
    """Count ops for a single statement, given the
    enclosing-loop multiplier."""
    if multiplier == 0:
        return 0
    if isinstance(stmt, ast.For):
        # Iteration count from range(...). We fall back to n
        # for unknown ranges.
        iters = _range_iter_count(stmt.iter, n)
        # Building an iterator is normally constant, but its expression may
        # eagerly do substantial work (``for x in sorted(data)``).  ``range``
        # itself is lazy and remains part of the loop bookkeeping below.
        iter_setup = 0
        if not (isinstance(stmt.iter, ast.Call)
                and _call_name(stmt.iter.func) == "range"):
            iter_setup = _count_expr(stmt.iter, multiplier, n)
        body_ops = _count_block(stmt.body, multiplier * iters, n)
        # The ``for`` itself adds 1 (the per-iteration
        # bookkeeping the runtime incurs).
        return iter_setup + body_ops + multiplier
    if isinstance(stmt, ast.While):
        # We can't statically know the trip count. Be
        # conservative: assume it runs n times.
        body_ops = _count_block(stmt.body, multiplier * n, n)
        return body_ops + multiplier * n
    if isinstance(stmt, ast.If):
        # The condition is evaluated once per enclosing
        # iteration. The body of the if is evaluated 0 or 1
        # times per enclosing iteration — we don't know which
        # statically, so we count it as if it always runs
        # (worst case). The if itself is 1 op (the branch
        # check) per enclosing iteration.
        cond = _count_expr(stmt.test, multiplier, n)
        then_ops = _count_block(stmt.body, multiplier, n)
        else_ops = _count_block(stmt.orelse, multiplier, n) if stmt.orelse else 0
        return cond + then_ops + else_ops + multiplier
    if isinstance(stmt, ast.FunctionDef):
        # The def itself is a one-time setup (not part of
        # the algorithm's runtime cost) — we don't count
        # it. We DO count the default values of the
        # parameters (they're evaluated once per call) and
        # the function body (runs with the same multiplier
        # as the surrounding scope).
        ops = 0
        for default in stmt.args.defaults:
            ops += _count_expr(default, multiplier, n)
        ops += _count_block(stmt.body, multiplier, n)
        return ops
    if isinstance(stmt, ast.Assign):
        # One assignment + the LHS targets + the RHS value.
        ops = multiplier
        for target in stmt.targets:
            ops += _count_expr(target, multiplier, n)
        ops += _count_expr(stmt.value, multiplier, n)
        return ops
    if isinstance(stmt, ast.AugAssign):
        ops = multiplier
        ops += _count_expr(stmt.target, multiplier, n)
        ops += _count_expr(stmt.value, multiplier, n)
        # The augmented op is a read + write + binop = 3.
        ops += 3 * multiplier
        return ops
    if isinstance(stmt, ast.Expr):
        # A bare expression statement (e.g. ``print(x)``).
        return _count_expr(stmt.value, multiplier, n)
    if isinstance(stmt, ast.Return):
        ops = 0
        if stmt.value is not None:
            ops += _count_expr(stmt.value, multiplier, n)
        return ops
    if isinstance(stmt, ast.Pass):
        return 0
    if isinstance(stmt, ast.Break):
        return multiplier
    if isinstance(stmt, ast.Continue):
        return multiplier
    # Fallback: walk all child nodes and count any
    # "operation" types we find. This handles ``import``,
    # ``class``, ``with``, ``try``, and other constructs we
    # don't count specifically — the inner expressions of
    # those (e.g. default values, except handlers) still
    # get counted.
    return _count_expr(stmt, multiplier, n)


def _count_expr(expr: ast.AST, multiplier: int, n: int) -> int:
    """Count ops for an expression subtree. Each matching
    AST node (``Compare``, ``Call``, etc.) counts as 1 op
    per enclosing iteration."""
    if multiplier == 0:
        return 0
    count = 0
    for node in ast.walk(expr):
        if isinstance(node, _OP_NODES):
            count += 1
        if isinstance(node, ast.Call):
            # ``Call`` already contributes one through ``_OP_NODES``.
            # Add only the work hidden inside well-known builtins and
            # standard-library C implementations.
            count += _hidden_call_cost(node, n) - 1
    return count * multiplier


def _hidden_call_cost(node: ast.Call, n: int) -> int:
    """Return the total cost of a recognized call (minimum one).

    This is deliberately a syntactic allow-list.  Guessing the cost of an
    arbitrary user function or method would be less accurate than leaving it
    opaque.  Container sizes that cannot be proved from a literal are modeled
    using the challenge input size ``n``.
    """
    name = _call_name(node.func)
    if not name:
        return 1
    leaf = name.rsplit(".", 1)[-1]
    size = _iterable_size(node.args[0], n) if node.args else n

    # Full traversal / construction.
    linear_functions = {
        "Counter", "list", "tuple", "set", "dict", "deque",
        "sum", "any", "all", "accumulate", "heapify",
    }
    if leaf in linear_functions and node.args:
        return max(1, size)
    # min/max with multiple positional arguments are constant in n.
    if leaf in {"min", "max"} and len(node.args) == 1:
        return max(1, size)
    if leaf == "sorted" and node.args:
        return _n_log_n(size)

    # List/string/set/dict methods whose implementation scans or copies the
    # receiver or supplied iterable.  We generally cannot infer the receiver's
    # size, so use n; for methods driven by an argument, use its size.
    if leaf in {"sort"}:
        return _n_log_n(n)
    if leaf in {
        "copy", "count", "index", "join", "reverse", "remove",
        "split", "rsplit", "splitlines", "replace", "find", "rfind",
        "strip", "lstrip", "rstrip", "lower", "upper", "casefold",
        "elements", "fromkeys",
    }:
        return max(1, n)
    if leaf in {"extend", "update", "intersection", "union", "difference"}:
        arg_size = _iterable_size(node.args[0], n) if node.args else n
        return max(1, arg_size)

    if leaf in {"heappush", "heappop", "heapreplace", "heappushpop",
                "bisect", "bisect_left", "bisect_right", "insort",
                "insort_left", "insort_right"}:
        return max(1, math.ceil(math.log2(max(n, 2))))
    if leaf == "most_common":
        # Counter.most_common(k) uses a heap for small k; asking for all
        # entries sorts them.  k=1 is linear, which is a frequent pattern.
        if node.args and isinstance(node.args[0], ast.Constant):
            k = node.args[0].value
            if isinstance(k, int) and k <= 1:
                return max(1, n)
        return _n_log_n(n)
    if leaf in {"nlargest", "nsmallest"}:
        return _n_log_n(n)
    if leaf == "pop" and node.args:
        # list.pop(0) shifts the remaining elements; pop() / pop(-1) does not.
        index = _eval_int(node.args[0], n)
        if index == 0:
            return max(1, n)
    return 1


def _call_name(func: ast.AST) -> str:
    """Return a dotted syntactic call name such as ``heapq.heappush``."""
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        prefix = _call_name(func.value)
        return f"{prefix}.{func.attr}" if prefix else func.attr
    return ""


def _iterable_size(node: ast.AST, n: int) -> int:
    """Best-effort size of an iterable expression used by a known call."""
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return len(node.elts)
    if isinstance(node, ast.Dict):
        return len(node.keys)
    if isinstance(node, ast.Constant) and isinstance(node.value, (str, bytes)):
        return len(node.value)
    if isinstance(node, ast.Call) and _call_name(node.func) == "range":
        return _range_iter_count(node, n)
    # Slices, comprehensions, generators, names, and nested calls are assumed
    # to scale with the canonical input.  This preserves the asymptotic class.
    return n


def _n_log_n(size: int) -> int:
    if size <= 1:
        return 1
    return max(1, math.ceil(size * math.log2(size)))


def _range_iter_count(iter_node: ast.AST, n: int) -> int:
    """Infer the iteration count of a ``for ... in <iter>:``
    header. Supports:

      * ``range(stop)``              → ``stop``
      * ``range(start, stop)``       → ``stop - start``
      * ``range(start, stop, step)`` → ``ceil((stop - start) / step)``
      * ``range(len(x))``            → ``n`` (we treat ``len()``
        of the canonical input as ``n``)
      * anything else (variable, generator) → ``n`` (conservative)

    Only literal numeric arguments are handled. If the
    source uses a variable for the range bound (e.g.
    ``range(k)`` where ``k`` is a parameter), we fall back
    to ``n``.
    """
    if not isinstance(iter_node, ast.Call):
        return n
    func = iter_node.func
    # ``range(...)`` only
    if not (isinstance(func, ast.Name) and func.id == "range"):
        return n
    args = iter_node.args
    if not args:
        return n
    if len(args) == 1:
        stop = _eval_int(args[0], n)
        return max(0, stop) if stop is not None else n
    if len(args) == 2:
        start = _eval_int(args[0], n) or 0
        stop = _eval_int(args[1], n)
        return max(0, (stop or n) - start)
    if len(args) >= 3:
        start = _eval_int(args[0], n) or 0
        stop = _eval_int(args[1], n)
        step = _eval_int(args[2], n) or 1
        if stop is None:
            return n
        if step == 0:
            return n
        # Compute the number of iterations for
        # ``range(start, stop, step)``. We use the standard
        # Python formula: ``max(0, ceil((stop - start) / step))``.
        # We don't ``max(1, step)`` here — that would clamp
        # negative steps (e.g. ``range(n - 1, 0, -1)``) to +1
        # and incorrectly report 0 iterations.
        diff = stop - start
        # Python's range() iteration count for the given
        # step: ceil(diff / step) when diff and step have
        # the same sign, floor otherwise. We use the
        # general ``math.ceil`` (which works for both
        # signs in Python because the division rounds toward
        # negative infinity for negative numbers).
        if (diff > 0 and step > 0) or (diff < 0 and step < 0):
            iters = math.ceil(diff / step)
        else:
            # diff / step is non-positive. Either we've
            # already passed the stop (iters <= 0) or step
            # points the wrong way. Treat as zero iterations.
            return 0
        return max(0, iters)
    return n


def _eval_int(node: ast.AST, n: int) -> Optional[int]:
    """Evaluate a literal int expression. Returns ``n`` for
    any non-literal node (conservative fallback).

    Supports:
      * ``123``              → 123
      * ``n``                → n
      * ``len(x)``           → n
      * ``-x`` / ``+x``       → negation
      * ``a + b``             → sum (if both literals)
      * ``a - b``             → difference
    Anything else (variable, attribute, call) → None.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.Name):
        if node.id == "n":
            return n
        return None
    if isinstance(node, ast.UnaryOp):
        inner = _eval_int(node.operand, n)
        if inner is None:
            return None
        if isinstance(node.op, ast.USub):
            return -inner
        if isinstance(node.op, ast.UAdd):
            return inner
        return None
    if isinstance(node, ast.BinOp):
        left = _eval_int(node.left, n)
        right = _eval_int(node.right, n)
        if left is None or right is None:
            return None
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return int(left / right) if right != 0 else None
        return None
    if isinstance(node, ast.Call):
        # ``len(x)`` → n (we treat the canonical input
        # length as n). This is the common case in
        # algorithms that take ``data`` and a ``n`` arg.
        if (isinstance(node.func, ast.Name)
                and node.func.id == "len"
                and len(node.args) == 1):
            inner = _eval_int(node.args[0], n)
            if inner is not None:
                return inner
            return n
        return None
    return None
