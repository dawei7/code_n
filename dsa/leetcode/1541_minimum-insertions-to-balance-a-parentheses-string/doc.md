# Minimum Insertions to Balance a Parentheses String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1541 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) |

## Problem Description
### Goal
You are given a nonempty string containing only `(` and `)`. Under this problem's balancing rule, every opening parenthesis must be matched by two consecutive closing parentheses `))`, and the opening parenthesis must occur before its matching pair. Thus `(` acts as one opening token while `))` acts as one closing token.

You may insert either parenthesis character at any position without deleting or rearranging existing characters. Return the minimum number of insertions required to make the entire string balanced, including repairs for unmatched closing pairs, incomplete pairs of closing parentheses, and openings left unmatched at the end.

### Function Contract
**Inputs**

- `s`: a string of `(` and `)` with length $n$, where $1 \le n \le 10^5$.

**Return value**

The minimum number of inserted parentheses needed to satisfy the two-consecutive-closing rule.

### Examples
**Example 1**

- Input: `s = "(()))"`
- Output: `1`
- Explanation: One final `)` completes the closing pair for the first opening parenthesis.

**Example 2**

- Input: `s = "())"`
- Output: `0`
- Explanation: One opening parenthesis is already followed by its required `))` token.

**Example 3**

- Input: `s = "))())("`
- Output: `3`
- Explanation: Insert one `(` before the initial `))` and two `)` after the final `(`.
