# Minimum Cost to Change the Final Value of Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1896 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/) |

## Problem Description

### Goal

A valid Boolean expression contains the literals `0` and `1`, the binary operators `&` and `|`, and properly matched, nonempty parentheses. Parentheses are evaluated first. Outside them, `&` has no precedence over `|`; operators at the same nesting depth are applied strictly from left to right.

One operation may flip a literal between `0` and `1`, or replace either operator with the other. Determine the fewest such operations needed to make the complete expression evaluate to the opposite Boolean value. Parentheses cannot be added, removed, or moved.

### Function Contract

**Inputs**

- `expression`: a valid string of length $N$, where $1 \le N \le 10^5$, containing only `0`, `1`, `&`, `|`, `(`, and `)`. All parentheses are matched and no pair is empty.

**Return value**

Return the minimum number of permitted single-character changes that makes the final value differ from the original expression's value.

### Examples

**Example 1**

- Input: `expression = "1&(0|1)"`
- Output: `1`
- Explanation: Replacing the inner `|` with `&` makes the expression false.

**Example 2**

- Input: `expression = "(0&0)&(0&0&0)"`
- Output: `3`

**Example 3**

- Input: `expression = "(0|(1|0&1))"`
- Output: `1`
- Explanation: Flipping the nested `1` to `0` changes the final result.
