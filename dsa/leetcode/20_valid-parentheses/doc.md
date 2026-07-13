# Valid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 20 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-parentheses/) |

## Problem Description
### Goal
Given a nonempty string containing only parentheses `()`, square brackets `[]`, and braces `{}`, decide whether it forms a valid bracket sequence. Every opening bracket must eventually be closed by the matching type.

Closures must also respect nesting order: the most recently opened unmatched bracket must be the next one closed. A closing bracket cannot appear without a corresponding opener, and no opener may remain unmatched after the entire string is consumed. Return a boolean indicating whether all of these conditions hold.

### Function Contract
**Inputs**

- `s`: non-empty `str` containing `()[]{}`

**Return value**

`True` when the complete bracket sequence is valid; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "()"`
- Output: `True`

**Example 2**

- Input: `s = "()[]{}"`
- Output: `True`

**Example 3**

- Input: `s = "(]"`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The stack stores exactly the unfinished nesting**

Scan left to right. Push each opening bracket onto a stack. For a closing bracket, the most recently opened unclosed bracket must be its matching type; if the stack is empty or its top differs, return false immediately. Otherwise pop the matched opener. A small closing-to-opening mapping keeps the matching rule explicit.

After the scan, validity additionally requires an empty stack so no opener remains unmatched.

**Why only the top opener may close**

Before each character is processed, the stack contains exactly the unmatched opening brackets from the processed prefix, ordered from outermost to innermost. A closer can legally match only the top because any later opener must close before an earlier one. Matching anything below the top would leave an inner pair crossing an outer pair, which is not valid nesting.

**Distinguish wrong type, wrong order, and missing partners**

For `([])`, push `(`, then `[`. The `]` matches and removes `[`, and `)` matches and removes `(`. The empty final stack proves validity. For `([)]`, `)` encounters `[` at the top and fails immediately, detecting the crossing order.

The sequence `(]` fails because the closing type differs from the stack top. The sequence `([)]` fails even though every type occurs once, because `)` tries to cross the still-open `[`. The sequence `((` survives the scan but fails the final empty-stack check because its openers never receive partners.

**Why LIFO order is exactly nesting order**

In a properly nested sequence, the next closing bracket must match the most recently opened bracket that has not yet closed. The stack top is exactly that opener. A mismatched or absent top proves the closer cannot participate in any valid nesting, while a match completes the innermost outstanding pair without affecting outer pairs.

After the scan, any remaining stack entry is an opener with no closing partner. Thus the algorithm accepts precisely when every closer matched the required latest opener and no opener remains, which is equivalent to valid bracket type and nesting throughout the string.

#### Complexity detail

Each bracket is pushed at most once and popped at most once, so the scan takes $O(n)$ time. In a completely nested string, the stack contains $n / 2$ openers before any closes, giving $O(n)$ worst-case auxiliary space.

#### Alternatives and edge cases

- **Repeatedly remove `()`, `[]`, and `{}`:** eventually recognizes valid strings, but deeply nested input can require $O(n)$ full-string passes and $O(n^2)$ time.
- **Use three independent counters:** detects totals but cannot detect mismatched types or crossing order.
- **Recursive grammar parser:** correct, but uses recursion and is more machinery than the direct stack invariant.
- A closing bracket at the first position fails immediately because there is no opener to match.
- Under the stated non-empty-input contract, no special empty-string branch is needed; if empty input were allowed, it would be valid because the final stack is empty.

</details>
