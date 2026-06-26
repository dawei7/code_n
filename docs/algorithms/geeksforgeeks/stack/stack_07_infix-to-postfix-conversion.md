# Infix to Postfix Conversion

| | |
|---|---|
| **ID** | `stack_07` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Convert Infix expression to Postfix expression](https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/) |

## Problem statement

Given a string representing an arithmetic expression in **Infix** notation (e.g., `A + B * C`), convert it to **Postfix** notation (e.g., `A B C * +`).
The conversion must respect standard mathematical operator precedence (e.g., `*` and `/` have higher precedence than `+` and `-`) and parentheses `()`.

**Input:** A string `s` representing the Infix expression.
**Output:** A string representing the Postfix expression.

## When to use it

- When designing a Compiler or an Interpreter. Modern computers mathematically cannot evaluate standard "human" Infix notation natively because of arbitrary precedence rules. They MUST convert it to Postfix (Reverse Polish Notation) or Abstract Syntax Trees first.

## Approach

**1. The Shunting-Yard Analogy:**
Invented by Edsger Dijkstra, this algorithm is analogous to a railroad shunting yard. Numbers (operands) are train cars that pass straight through to the output track. Operators (`+`, `*`) are diverted into a switching station (the Stack) to wait until their proper turn to leave, based on precedence.

**2. The Operator Stack Rules:**
We process the string left-to-right.
- If we see a Number/Letter, we immediately append it to the Output string. (Operands NEVER go into the Stack).
- If we see an Operator (e.g. `+`), we look at the Stack.
  - If the top of the Stack has an operator of **strictly lesser** precedence (e.g. Stack has `-`, and we are `*`), we just push our operator onto the Stack.
  - If the top of the Stack has an operator of **greater or equal** precedence (e.g. Stack has `*`, and we are `+`), the Stack operator gets priority! We POP the `*` from the Stack and append it to the Output. We keep popping until we find a lesser operator, and THEN we push our `+` onto the Stack.

**3. The Parentheses Rules:**
Parentheses physically override standard precedence.
- If we see `(`, we push it directly onto the Stack. It acts as an absolute wall.
- If we see `)`, we POP operators from the Stack and append them to the Output continuously until we hit the matching `(`. Then we discard both parentheses.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_07: Infix to Postfix Conversion.

Convert an infix arithmetic expression (operators
"""


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
```

</details>

## Walk-through

`expression = "A+B*C-D"`

1. `A`: Operand -> Output = `"A"`. Stack = `[]`.
2. `+`: Operator -> Stack is empty. Push `+`. Stack = `[+]`.
3. `B`: Operand -> Output = `"A B"`.
4. `*`: Operator -> Top is `+`. `*` > `+`. Push `*`. Stack = `[+, *]`.
5. `C`: Operand -> Output = `"A B C"`.
6. `-`: Operator -> Top is `*`. `-` <= `*`. Pop `*` to output!
   - Output = `"A B C *"`. Stack = `[+]`.
   - Top is `+`. `-` <= `+`. Pop `+` to output!
   - Output = `"A B C * +"`. Stack = `[]`.
   - Stack is empty. Push `-`. Stack = `[-]`.
7. `D`: Operand -> Output = `"A B C * + D"`.
8. End of string. Pop remaining Stack: `-`.
   - Output = `"A B C * + D -"`.

Result: `ABC*+D-`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every single character in the string is processed exactly once.
Even though there is a `while` loop inside the operator branch, an operator can only be pushed to the stack ONCE, and therefore can only be popped ONCE.
Thus, across the entire execution of the algorithm, the `while` loop executes a maximum of N times globally.
Time complexity is strictly $O(N)$.
Space complexity is $O(N)$ for the Stack and the Output array.

## Variants & optimizations

- **Abstract Syntax Tree (AST):** Instead of outputting a string, the algorithm can be trivially modified to output a Binary Tree Node! When an operator is popped, you pop the last two elements from the Output, attach them as the `left` and `right` children of the operator, and push the operator itself back to the Output!

## Real-world applications

- **Calculators / Math Parsers:** The foundational algorithm inside Python's `eval()` function and standard GUI Calculators to parse human input.

## Related algorithms in cOde(n)

- **[stack_08 - Evaluate Reverse Polish Notation](stack_08_evaluate-reverse-polish-notation.md)** — The sister algorithm that takes the Output generated here and actually executes the mathematical calculations.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
