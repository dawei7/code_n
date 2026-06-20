# Evaluate Reverse Polish Notation

| | |
|---|---|
| **ID** | `stack_08` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |

## Problem statement

Evaluate the value of an arithmetic expression in **Reverse Polish Notation** (Postfix Notation).
Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.
The division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

**Input:** An array of strings `tokens` representing the RPN expression.
**Output:** An integer representing the final calculated result.

## When to use it

- To execute code! This is exactly how computers actually process math.

## Approach

**1. The Beauty of Postfix:**
Human math (Infix, like `3 + 4 * 2`) is terrible for computers because you have to scan ahead, find the `*`, calculate it, and then go backwards to calculate the `+`.
In Postfix (`3 4 2 * +`), the math is completely unambiguous and strictly Left-to-Right. There are no parentheses. There are no precedence rules.

**2. The Operand Stack:**
We process the tokens strictly from left to right.
- If we see a Number, we push it onto the Stack.
- If we see an Operator, we POP the top two numbers from the Stack!
  - The first number popped is the `Right Operand`.
  - The second number popped is the `Left Operand`.
  - We apply the operator to them: `Left [Operator] Right`.
  - We PUSH the resulting calculated integer back onto the Stack!
When the string is completely processed, there will be exactly ONE number remaining on the stack. That is the final answer!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_08: Evaluate Reverse Polish Notation.

Evaluate a postfix (Reverse Polish Notation) arithmetic
"""


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
```

</details>

## Walk-through

`tokens = ["2", "1", "+", "3", "*"]`

1. `"2"`: Operand -> Stack = `[2]`.
2. `"1"`: Operand -> Stack = `[2, 1]`.
3. `"+"`: Operator -> Pop `1` (b), Pop `2` (a). Calculate `2 + 1 = 3`. Push `3`.
   - Stack = `[3]`.
4. `"3"`: Operand -> Stack = `[3, 3]`.
5. `"*"`: Operator -> Pop `3` (b), Pop `3` (a). Calculate `3 * 3 = 9`. Push `9`.
   - Stack = `[9]`.
6. End of tokens. Return `stack[0]`.

Result: `9`. ✓
*(In human Infix notation, this was: `(2 + 1) * 3`)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every token is processed exactly once in a single linear pass. Pushing and Popping from the stack are $O(1)$ operations. Time complexity is strictly $O(N)$.
In the worst-case scenario (an expression with all numbers first, followed by all operators, e.g. `1 2 3 4 + + +`), the stack will temporarily hold N/2 numbers before evaluating them. Space complexity is $O(N)$.

## Variants & optimizations

- **Prefix Notation (Polish Notation):** E.g., `+ * 2 3 4`. The exact same algorithm applies, but you iterate through the tokens array entirely in reverse (Right-to-Left)! When you pop two elements for an operator, the first one popped is `a` (left) and the second is `b` (right).

## Real-world applications

- **JVM / Bytecode Execution:** The Java Virtual Machine (JVM) is fundamentally a Stack Machine. It does not use CPU registers to hold variables during math; it literally compiles Java code into Postfix bytecodes (`iload_1`, `iload_2`, `iadd`) and runs this exact algorithm!
- **HP Calculators:** Hewlett-Packard heavily popularized RPN in the 1970s for their engineering calculators, as it allowed users to evaluate complex formulas without needing to track parenthesis depth in their head.

## Related algorithms in cOde(n)

- **[stack_07 - Infix to Postfix Conversion](stack_07_infix-to-postfix-conversion.md)** — The engine that converts human math into the array that this algorithm processes.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
