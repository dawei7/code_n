"""Spec generator input - 3 new stack specs for Session 1.

Covers the remaining GfG stack-data-structures topics that
stack_01..05 don't already cover:

  stack_06  Trapping Rain Water          (canonical stack problem)
  stack_07  Infix to Postfix Conversion  (shunting-yard)
  stack_08  Evaluate Reverse Polish Notation (RPN)

After this batch, stack.py covers the canonical GfG stack
catalog including the most-asked Trapping Rain Water.

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module stack \\
        --input batch_stack_session1.py
"""


SPECS_TO_ADD = [
    # ============================================================
    # stack_06: Trapping Rain Water
    # ============================================================
    {
        "id": "stack_06",
        "name": "Trapping Rain Water",
        "category": "stack",
        "difficulty": 5,
        "complexity": "O_N",
        "description": (
            "Given a non-negative integer array heights where each\n"
            "element represents a bar of width 1, compute how much\n"
            "rainwater can be trapped between the bars after it\n"
            "rains. A classic stack-based solution: walk through\n"
            "the bars; whenever you see a bar taller than the\n"
            "stack's top, pop until the stack is empty or the\n"
            "new bar is shorter than the top. The trapped water\n"
            "at each pop is bounded by the popped bar's height,\n"
            "the current bar, and the new stack top. O(n) time,\n"
            "O(n) extra space.\n"
            "Source: https://www.geeksforgeeks.org/trapping-rain-water/"
        ),
        "source_url": "https://www.geeksforgeeks.org/trapping-rain-water/",
        "params": ["heights", "n"],
        "inputs": {
            "heights": "list of n non-negative integers (bar heights).",
            "n": "length of heights.",
        },
        "returns": "the total units of trapped rainwater.",
        "solve": '''
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
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 16))
heights = [rng.randint(0, 8) for _ in range(n)]
challenge._heights = list(heights)
return {"heights": list(heights), "n": n}
''',
        "verify": '''
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
''',
        "samples": [
            ("heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], n = 12", "6"),
            ("heights = [4, 2, 0, 3, 2, 5], n = 6", "9"),
        ],
        "hint": "Stack of indices with increasing heights. When you see a taller bar, pop the top - the popped bar is the bottom of a pool bounded by the new top and the current bar.",
        "parents": ["stack_05"],
        "children": ["stack_07"],
    },

    # ============================================================
    # stack_07: Infix to Postfix (Shunting Yard)
    # ============================================================
    {
        "id": "stack_07",
        "name": "Infix to Postfix Conversion",
        "category": "stack",
        "difficulty": 4,
        "complexity": "O_N",
        "description": (
            "Convert an infix arithmetic expression (operators\n"
            "between operands, with parentheses) into a postfix\n"
            "expression (Reverse Polish Notation - operators\n"
            "after operands). Use the shunting-yard algorithm\n"
            "with a stack of operators. Precedence: */ higher\n"
            "than +-. Left-associative throughout. Operands are\n"
            "single lowercase letters or digits in this spec.\n"
            "O(n) time, O(n) space.\n"
            "Source: https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/"
        ),
        "source_url": "https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/",
        "params": ["expr", "n"],
        "inputs": {
            "expr": "string of operands (lowercase letters/digits), operators (+,-,*,/), and parentheses.",
            "n": "length of expr.",
        },
        "returns": "the postfix expression as a string.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("expr = 'a+b*c', n = 5", "'abc*+'"),
            ("expr = '(a+b)*c', n = 7", "'ab+c*'"),
            ("expr = 'a+b*c-d/e', n = 9", "'abc*+de/-'"),
        ],
        "hint": "Operands go to output. On '(', push. On ')', pop until '('. On an operator, pop while the stack top has >= precedence (left-assoc), then push.",
        "parents": ["stack_06"],
        "children": ["stack_08"],
    },

    # ============================================================
    # stack_08: Evaluate Reverse Polish Notation
    # ============================================================
    {
        "id": "stack_08",
        "name": "Evaluate Reverse Polish Notation",
        "category": "stack",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Evaluate a postfix (Reverse Polish Notation) arithmetic\n"
            "expression given as a list of tokens. Operands are\n"
            "integers; operators are +, -, *, /. Use a stack:\n"
            "on an operand, push it; on an operator, pop the top\n"
            "two, apply, push the result. Integer division truncates\n"
            "toward zero (Python's default). O(n) time, O(n) space.\n"
            "Source: https://www.geeksforgeeks.org/evaluation-of-postfix-expression/"
        ),
        "source_url": "https://www.geeksforgeeks.org/evaluation-of-postfix-expression/",
        "params": ["tokens", "n"],
        "inputs": {
            "tokens": "list of n string tokens; operands are integer strings, operators are +, -, *, /.",
            "n": "length of tokens.",
        },
        "returns": "the integer result of evaluating the postfix expression.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("tokens = ['2','1','+','3','*'], n = 5", "9 (postfix for (2+1)*3)"),
            ("tokens = ['4','13','5','/','+'], n = 5", "6 (4 + 13/5 = 4 + 2 = 6)"),
        ],
        "hint": "On operand: push. On operator: pop two, apply, push result. Integer division truncates toward zero.",
        "parents": ["stack_07"],
        "children": [],
    },
]
