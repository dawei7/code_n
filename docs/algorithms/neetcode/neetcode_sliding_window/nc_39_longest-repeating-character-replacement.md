## Problem Description & Examples
### Goal
Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix notation).

Valid operators: `+`, `-`, `*`, `/`. Division truncates toward zero. Each operand is an integer.

### Function Contract
**Inputs**

- `tokens`: List[str] - postfix tokens

**Return value**

int - result of the expression

### Examples
**Example 1**

- Input: `tokens = ["2", "1", "+", "3", "*"]`
- Output: `9`

**Example 2**

- Input: `tokens = ['15', '12', '/']`
- Output: `1`

**Example 3**

- Input: `tokens = ['47']`
- Output: `47`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
