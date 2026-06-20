# Balanced Parentheses

| | |
|---|---|
| **ID** | `stack_01` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |

## Problem statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Input:** A string `s`.
**Output:** A boolean representing whether the string is perfectly balanced.

**Example 1:**
`s = "()[]{}"`
Output: `True`.

**Example 2:**
`s = "([)]"`
Output: `False`. (The `]` tries to close the `[` while the `(` is still actively open).

## When to use it

- This is the textbook introduction to the **Stack** data structure.
- Used universally in compilers and syntax linters to verify code structure.

## Approach

A Stack follows the **LIFO** (Last-In, First-Out) principle. This perfectly models nested structures, because the *most recently opened* bracket is the one that must be closed *first*.

1. Initialize an empty stack.
2. Iterate through each character in the string:
   - If the character is an **opening bracket** (`(`, `{`, `[`), push it onto the stack.
   - If the character is a **closing bracket** (`)`, `}`, `]`):
     - If the stack is empty, it means we are trying to close a bracket that was never opened. Return `False`.
     - Pop the top element from the stack.
     - Check if the popped opening bracket matches the type of the current closing bracket. If they don't match, return `False`.
3. After the loop finishes, check the stack. If it's empty, all opened brackets were successfully closed (return `True`). If it still contains elements, some brackets were opened but never closed (return `False`).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
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
```

</details>

## Walk-through

`s = "{[()]}"`

1. `char = '{'`. Opening. Push. Stack: `['{']`.
2. `char = '['`. Opening. Push. Stack: `['{', '[']`.
3. `char = '('`. Opening. Push. Stack: `['{', '[', '(']`.
4. `char = ')'`. Closing. 
   - Pop top: `'('`. 
   - Does `'('` match `matching_bracket[')']`? Yes.
   - Stack: `['{', '[']`.
5. `char = ']'`. Closing.
   - Pop top: `'['`.
   - Does `'['` match `matching_bracket[']']`? Yes.
   - Stack: `['{']`.
6. `char = '}'`. Closing.
   - Pop top: `'{'`.
   - Does `'{'` match `matching_bracket['}']`? Yes.
   - Stack: `[]`.

Loop ends. Stack is empty. Return `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

We process each character in the string exactly once. Dictionary lookups and stack `push`/`pop` operations take $O(1)$ time. Time complexity is $O(N)$.
In the worst case (e.g., `s = "(((((((((("`), we push all N characters onto the stack. Space complexity is $O(N)$.

## Variants & optimizations

- **Single Bracket Type $O(1)$ Space:** If the string ONLY contains `(` and `)`, you do not need a stack! You can just maintain an integer `count`. Increment on `(`, decrement on `)`. If `count` ever dips below 0, return `False`. At the end, return `count == 0`.
- **Longest Valid Parentheses (DP):** A much harder problem that asks for the length of the longest valid contiguous substring.

## Real-world applications

- **HTML/XML Parsing:** Browsers use this exact stack logic to ensure that an `<h1>` tag is closed by an `</h1>` tag before the parent `<div>` is closed.

## Related algorithms in cOde(n)

- **[stack_08 - Evaluate Reverse Polish Notation](stack_08_evaluate-reverse-polish-notation.md)** — Another fundamental application of Stacks processing linear strings sequentially.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
