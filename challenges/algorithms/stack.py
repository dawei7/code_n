"""Stack algorithms.

Three classic problems from GFG's stack-data-structures catalog:

  01 Balanced Parentheses     - validate ()[]{} nesting
  02 Next Greater Element    - for each index, the next larger value to the right
  03 Stock Span Problem      - for each day, the number of consecutive
    days before it with a lower (or equal) price

All three use a Python list as the underlying stack. Setup
is deterministic and keeps n small (4-16) so brute-force
verify is fast.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === stack_01: Balanced Parentheses ===

STACK_01_SOURCE = '''\
"""Optimal solution for stack_01: Balanced Parentheses.

Walk the string; push each opening bracket, and on a closing
bracket pop the top and check that it pairs correctly. Return
True iff the stack is empty at the end. O(n).
"""


def solve(s, n):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
'''


def _setup_balanced_parens(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    # Build a random valid-or-invalid string.
    valid_count = rng.randint(1, max(1, n // 2))
    # Generate `valid_count` matching pairs.
    openers = "([{"
    closers = ")]}"
    pairs = []
    for _ in range(valid_count):
        idx = rng.randint(0, 2)
        pairs.append((openers[idx], closers[idx]))
    rng.shuffle(pairs)
    # Nest them so the result is well-formed.
    s = ""
    opens = []
    for o, c in pairs:
        s += o
        opens.append(c)
    rng.shuffle(opens)
    s += "".join(opens)
    # Optionally add a stray closer to break the validity.
    if rng.random() < 0.5 and len(s) > 1:
        s += rng.choice(closers)
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_balanced_parens(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    s = challenge._s
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return result is False
            stack.pop()
    return result is (not stack)


# === stack_02: Next Greater Element ===

STACK_02_SOURCE = '''\
"""Optimal solution for stack_02: Next Greater Element.

Monotonic stack: walk left to right, maintaining a stack of
indices whose next-greater hasn't been found yet. When arr[i]
is greater than the top, pop and record i as the answer for
the popped index. O(n).
"""


def solve(arr, n):
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
'''


def _setup_next_greater(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(0, 99) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_next_greater(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    # Brute-force: for each i, find the first j > i with arr[j] > arr[i].
    expected = []
    for i in range(len(arr)):
        nxt = -1
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                nxt = arr[j]
                break
        expected.append(nxt)
    return result == expected


# === stack_03: Stock Span Problem ===

STACK_03_SOURCE = '''\
"""Optimal solution for stack_03: Stock Span Problem.

For each day i, the span is the number of consecutive days
just before i with a price <= arr[i] (plus today). Monotonic
stack: walk left to right, popping while the top's price is
<= today's. The span is i - (top index after popping), or
i + 1 if the stack is empty. O(n).
"""


def solve(arr, n):
    spans = [0] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans
'''


def _setup_stock_span(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    arr = [rng.randint(1, 99) for _ in range(n)]
    challenge._arr = list(arr)
    return {"arr": list(arr), "n": n}


def _verify_stock_span(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    arr = challenge._arr
    # Brute-force: for each i, count j <= i with arr[j] <= arr[i] consecutively.
    expected = []
    for i in range(len(arr)):
        span = 1
        j = i - 1
        while j >= 0 and arr[j] <= arr[i]:
            span += 1
            j -= 1
        expected.append(span)
    return result == expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="stack_01",
        name="Balanced Parentheses",
        category="stack",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the input string of ()[]{} characters is\n"
            "well-balanced. Push each opener; on a closer, pop and check\n"
            "the pair. The string is balanced iff the stack ends empty.\n"
            "Source: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/"
        ),
        source_url="https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/",
        params=["s", "n"],
        inputs={
            "s": "string of n characters in ()[]{}.",
            "n": "length of s.",
        },
        returns="True iff s is well-balanced.",
        source=STACK_01_SOURCE,
        setup_fn=_setup_balanced_parens,
        verify_fn=_verify_balanced_parens,
        samples=[
            Sample('s = "{([])}", n = 6', "True"),
            Sample('s = "([)]", n = 4', "False"),
            Sample('s = "((()))", n = 6', "True"),
        ],
        hint="On an opener, push. On a closer, pop and check the pair.",
        parents=["recursion_04"],
        children=["stack_02"],
    ),
    AlgorithmSpec(
        id="stack_02",
        name="Next Greater Element",
        category="stack",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "For each index i, return the next value to the right that's\n"
            "strictly greater than arr[i], or -1 if none. Monotonic stack\n"
            "of indices: pop while arr[i] > arr[top], record arr[i] as the\n"
            "answer for the popped index.\n"
            "Requirement: O(n) time.\n"
            "Source: https://www.geeksforgeeks.org/next-greater-element/"
        ),
        source_url="https://www.geeksforgeeks.org/next-greater-element/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n random integers.",
            "n": "length of arr.",
        },
        returns="a list of n values (each the next greater to the right, or -1).",
        source=STACK_02_SOURCE,
        setup_fn=_setup_next_greater,
        verify_fn=_verify_next_greater,
        samples=[
            Sample("arr = [4, 5, 2, 25], n = 4", "[5, 25, 25, -1]"),
            Sample("arr = [13, 7, 6, 12], n = 4", "[-1, 12, 12, -1]"),
        ],
        hint="Monotonic stack of indices. Pop when arr[i] > arr[top] and record the answer.",
        parents=["stack_01"],
        children=["stack_03"],
    ),
    AlgorithmSpec(
        id="stack_03",
        name="Stock Span Problem",
        category="stack",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "For each day i, the span is the number of consecutive days\n"
            "ending at i with a price <= arr[i] (including today).\n"
            "Monotonic stack of strictly-greater indices: pop while\n"
            "arr[top] <= arr[i]; the span is i - top_index, or i + 1\n"
            "if the stack is empty.\n"
            "Source: https://www.geeksforgeeks.org/the-stock-span-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/the-stock-span-problem/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n daily prices.",
            "n": "length of arr.",
        },
        returns="a list of n spans (one per day).",
        source=STACK_03_SOURCE,
        setup_fn=_setup_stock_span,
        verify_fn=_verify_stock_span,
        samples=[
            Sample("arr = [100, 80, 60, 70, 60, 75, 85], n = 7", "[1, 1, 1, 2, 1, 4, 6]"),
            Sample("arr = [10, 4, 5, 90, 120, 80], n = 6", "[1, 1, 2, 4, 5, 1]"),
        ],
        hint="Stack of indices where arr[index] is strictly greater than today's. Pop <= and read the gap.",
        parents=["stack_02"],
        children=["stack_04"],
    ),
]


# === stack_04: Largest Rectangle in Histogram ===

STACK_04_SOURCE = '''\
"""Optimal solution for stack_04: Largest Rectangle in Histogram.

Monotonic stack of bar indices with increasing heights. For each
bar popped, the rectangle extends from the previous-smaller on
the left to the current on the right. Track the max area across
all pops. O(n).
"""


def solve(heights, n):
    if n == 0:
        return 0
    stack = []  # indices with increasing heights
    best = 0
    for i in range(n + 1):
        cur_h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > cur_h:
            top = stack.pop()
            h = heights[top]
            left = stack[-1] + 1 if stack else 0
            right = i - 1
            area = h * (right - left + 1)
            if area > best:
                best = area
        stack.append(i)
    return best
'''


def _setup_largest_rect(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    heights = [rng.randint(0, 20) for _ in range(n)]
    challenge._heights = list(heights)
    return {"heights": list(heights), "n": n}


def _verify_largest_rect(challenge, result):
    if not isinstance(result, int):
        return False
    heights = challenge._heights
    n = len(heights)
    # Brute force: for each (i, j), area = min(heights[i..j]) * (j - i + 1).
    best = 0
    for i in range(n):
        for j in range(i, n):
            area = min(heights[k] for k in range(i, j + 1)) * (j - i + 1)
            if area > best:
                best = area
    return result == best


# === stack_05: Min Stack ===

STACK_05_SOURCE = '''\
"""Optimal solution for stack_05: Min Stack.

Two parallel stacks: one for values, one for the running minimum.
push, pop, top, get_min are all O(1).
"""


def solve(ops, n):
    """Run a sequence of operations and return the result of get_min calls.

    ops is a list of (cmd, value) tuples where cmd is "push", "pop",
    or "get_min". For "pop" and "get_min" the value is unused.
    For "push" the value is the value to push. Returns a list of
    ints: for each "get_min", the min of the stack at that point;
    for each "pop", the value popped (or -1 if the stack was empty).
    """
    stack = []
    mins = []
    out = []
    for op in ops:
        cmd = op[0]
        if cmd == "push":
            v = op[1]
            stack.append(v)
            if not mins or v <= mins[-1]:
                mins.append(v)
        elif cmd == "pop":
            if not stack:
                out.append(-1)
            else:
                v = stack.pop()
                if mins and v == mins[-1]:
                    mins.pop()
                out.append(v)
        elif cmd == "get_min":
            out.append(mins[-1] if mins else -1)
    return out
'''


def _setup_min_stack(challenge, n, seed):
    rng = random.Random(seed)
    n_ops = max(1, min(n, 12))
    ops = []
    for _ in range(n_ops):
        cmd = rng.choices(["push", "pop", "get_min"], weights=[3, 1, 1])[0]
        if cmd == "push":
            v = rng.randint(-9, 9)
            ops.append(("push", v))
        else:
            ops.append((cmd, 0))
    challenge._ops = list(ops)
    return {"ops": list(ops), "n": len(ops)}


def _verify_min_stack(challenge, result):
    if not isinstance(result, list):
        return False
    # Brute force: just track a Python list and its min.
    stack = []
    expected = []
    for op in challenge._ops:
        cmd = op[0]
        if cmd == "push":
            stack.append(op[1])
        elif cmd == "pop":
            if not stack:
                expected.append(-1)
            else:
                expected.append(stack.pop())
        elif cmd == "get_min":
            expected.append(min(stack) if stack else -1)
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="stack_04",
        name="Largest Rectangle in Histogram",
        category="stack",
        difficulty=6,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Given an array of bar heights, return the area of the\n"
            "largest rectangle that fits entirely within the bars.\n"
            "Monotonic stack of indices with increasing heights; for\n"
            "each bar popped, the rectangle's width is the run of\n"
            "indices with height >= that bar.\n"
            "Source: https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-using-stack/"
        ),
        source_url="https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-using-stack/",
        params=["heights", "n"],
        inputs={
            "heights": "list of n bar heights.",
            "n": "length of heights.",
        },
        returns="the largest rectangle area.",
        source=STACK_04_SOURCE,
        setup_fn=_setup_largest_rect,
        verify_fn=_verify_largest_rect,
        samples=[
            Sample("heights = [2, 1, 5, 6, 2, 3], n = 6", "10 (5 * 2)"),
            Sample("heights = [2, 4], n = 2", "4"),
        ],
        hint="Monotonic stack. Pop bars while the current bar is shorter; the popped bar's rectangle is the run.",
        parents=["stack_03"],
        children=["stack_05"],
    ),
    AlgorithmSpec(
        id="stack_05",
        name="Min Stack",
        category="stack",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Implement a stack that supports push, pop, and get_min\n"
            "in O(1). Two parallel stacks: the main one and a stack\n"
            "of running minimums. Return a list of results: for each\n"
            "get_min, the current min; for each pop, the popped value.\n"
            "Source: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/"
        ),
        source_url="https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/",
        params=["ops", "n"],
        inputs={
            "ops": "list of (cmd, value) tuples; cmd in {push, pop, get_min}.",
            "n": "length of ops.",
        },
        returns="a list of results - one per pop or get_min op.",
        source=STACK_05_SOURCE,
        setup_fn=_setup_min_stack,
        verify_fn=_verify_min_stack,
        samples=[
            Sample('ops = [("push", 2), ("push", 0), ("get_min", 0), ("pop", 0), ("get_min", 0)], n = 5', "[0, 2, 2]"),
        ],
        hint="Parallel stack of running minimums. On push, append to mins if v <= mins[-1]. On pop, drop if equal.",
        parents=["stack_04"],
        children=[],
    ),
])


# === stack_06: Trapping Rain Water ===

STACK_06_SOURCE = '''
def solve(heights, n):
    """Trapping Rain Water via monotonic stack."""
    if n <= 2:
        return 0
    stack = []  # indices with increasing heights
    water = 0
    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            # Distance between current and new top of stack.
            dist = i - stack[-1] - 1
            # Bounded by min of the two walls minus the popped bottom.
            bounded = min(heights[i], heights[stack[-1]]) - heights[top]
            water += dist * bounded
        stack.append(i)
    return water
'''

def _setup_stack_06(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    heights = [rng.randint(0, 8) for _ in range(n)]
    challenge._heights = list(heights)
    return {"heights": list(heights), "n": n}

def _verify_stack_06(challenge, result):
    heights = challenge._heights
    n = len(heights)
    # Brute force: for each i, water[i] = min(max_left, max_right) - height[i].
    if n == 0:
        return result == 0
    max_left = [0] * n
    for i in range(n):
        max_left[i] = max(heights[:i + 1])
    max_right = [0] * n
    for i in range(n - 1, -1, -1):
        max_right[i] = max(heights[i:])
    expected = sum(max(min(max_left[i], max_right[i]) - heights[i], 0) for i in range(n))
    return result == expected



# === stack_07: Infix to Postfix Conversion ===

STACK_07_SOURCE = '''
def solve(expr, n):
    """Shunting-yard: infix -> postfix."""
    if n == 0:
        return ""
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    out = []
    for ch in expr:
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if stack:
                stack.pop()  # pop the "("
        else:  # operator
            while stack and stack[-1] != "(" and prec.get(stack[-1], 0) >= prec[ch]:
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    return "".join(out)
'''

def _setup_stack_07(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Build a small infix expression.
    n = max(1, min(n, 12))
    operands = "abcde"
    operators = ["+", "-", "*", "/"]
    # Build a random valid infix with balanced parens.
    parts = []
    depth = 0
    for _ in range(n):
        r = rng.random()
        if r < 0.5 and depth < 4:
            parts.append(rng.choice(operands))
        elif r < 0.85:
            parts.append(rng.choice(operators))
        elif r < 0.92 and depth < 4:
            parts.append("(")
            depth += 1
        elif depth > 0:
            parts.append(")")
            depth -= 1
    # Close any unclosed parens.
    while depth > 0:
        parts.append(")")
        depth -= 1
    expr = "".join(parts)
    challenge._expr = expr
    return {"expr": expr, "n": len(expr)}

def _verify_stack_07(challenge, result):
    # Reference: re-run the canonical algorithm and compare.
    expr = challenge._expr
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    out = []
    for ch in expr:
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while stack and stack[-1] != "(" and prec.get(stack[-1], 0) >= prec[ch]:
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    expected = "".join(out)
    return result == expected



# === stack_08: Evaluate Reverse Polish Notation ===

STACK_08_SOURCE = '''
def solve(tokens, n):
    """Evaluate a postfix expression and return the integer result."""
    if n == 0:
        return 0
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:  # "/"
                # Truncate toward zero (Python's int() does this).
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]
'''

def _setup_stack_08(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Build a random postfix expression: ~70% operands, 30% operators.
    n = max(1, min(n, 12))
    tokens = []
    # Push a few operands first, then operators in the right order.
    stack_depth = 0
    for _ in range(n):
        if stack_depth >= 2 and rng.random() < 0.4:
            tokens.append(rng.choice(["+", "-", "*"]))
            stack_depth -= 1
        else:
            v = rng.randint(1, 9)
            tokens.append(str(v))
            stack_depth += 1
    challenge._tokens = list(tokens)
    return {"tokens": list(tokens), "n": len(tokens)}

def _verify_stack_08(challenge, result):
    tokens = challenge._tokens
    # Re-run the canonical algorithm.
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    expected = stack[-1] if stack else 0
    return result == expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="stack_06",
        name="Trapping Rain Water",
        category="stack",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given a non-negative integer array heights where each
            element represents a bar of width 1, compute how much
            rainwater can be trapped between the bars after it
            rains. A classic stack-based solution: walk through
            the bars; whenever you see a bar taller than the
            stack's top, pop until the stack is empty or the
            new bar is shorter than the top. The trapped water
            at each pop is bounded by the popped bar's height,
            the current bar, and the new stack top. O(n) time,
            O(n) extra space.
            Source: https://www.geeksforgeeks.org/trapping-rain-water/
            """),
        source_url="https://www.geeksforgeeks.org/trapping-rain-water/",
        params=["heights", "n"],
        inputs={
            "heights": "list of n non-negative integers (bar heights).",
            "n": "length of heights.",
        },
        returns="the total units of trapped rainwater.",
        source=STACK_06_SOURCE,
        setup_fn=_setup_stack_06,
        verify_fn=_verify_stack_06,
        samples=[
            Sample("heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], n = 12", "6"),
            Sample("heights = [4, 2, 0, 3, 2, 5], n = 6", "9"),
        ],
        hint="Stack of indices with increasing heights. When you see a taller bar, pop the top - the popped bar is the bottom of a pool bounded by the new top and the current bar.",
        parents=["stack_05"],
        children=["stack_07"],
    ),
    AlgorithmSpec(
        id="stack_07",
        name="Infix to Postfix Conversion",
        category="stack",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Convert an infix arithmetic expression (operators
            between operands, with parentheses) into a postfix
            expression (Reverse Polish Notation - operators
            after operands). Use the shunting-yard algorithm
            with a stack of operators. Precedence: */ higher
            than +-. Left-associative throughout. Operands are
            single lowercase letters or digits in this spec.
            O(n) time, O(n) space.
            Source: https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/
            """),
        source_url="https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/",
        params=["expr", "n"],
        inputs={
            "expr": "string of operands (lowercase letters/digits), operators (+,-,*,/), and parentheses.",
            "n": "length of expr.",
        },
        returns="the postfix expression as a string.",
        source=STACK_07_SOURCE,
        setup_fn=_setup_stack_07,
        verify_fn=_verify_stack_07,
        samples=[
            Sample("expr = 'a+b*c', n = 5", "'abc*+'"),
            Sample("expr = '(a+b)*c', n = 7", "'ab+c*'"),
            Sample("expr = 'a+b*c-d/e', n = 9", "'abc*+de/-'"),
        ],
        hint="Operands go to output. On '(', push. On ')', pop until '('. On an operator, pop while the stack top has >= precedence (left-assoc), then push.",
        parents=["stack_06"],
        children=["stack_08"],
    ),
    AlgorithmSpec(
        id="stack_08",
        name="Evaluate Reverse Polish Notation",
        category="stack",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Evaluate a postfix (Reverse Polish Notation) arithmetic
            expression given as a list of tokens. Operands are
            integers; operators are +, -, *, /. Use a stack:
            on an operand, push it; on an operator, pop the top
            two, apply, push the result. Integer division truncates
            toward zero (Python's default). O(n) time, O(n) space.
            Source: https://www.geeksforgeeks.org/evaluation-of-postfix-expression/
            """),
        source_url="https://www.geeksforgeeks.org/evaluation-of-postfix-expression/",
        params=["tokens", "n"],
        inputs={
            "tokens": "list of n string tokens; operands are integer strings, operators are +, -, *, /.",
            "n": "length of tokens.",
        },
        returns="the integer result of evaluating the postfix expression.",
        source=STACK_08_SOURCE,
        setup_fn=_setup_stack_08,
        verify_fn=_verify_stack_08,
        samples=[
            Sample("tokens = ['2','1','+','3','*'], n = 5", "9 (postfix for (2+1)*3)"),
            Sample("tokens = ['4','13','5','/','+'], n = 5", "6 (4 + 13/5 = 4 + 2 = 6)"),
        ],
        hint="On operand: push. On operator: pop two, apply, push result. Integer division truncates toward zero.",
        parents=["stack_07"],
        children=[],
    ),
])
