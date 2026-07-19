# Preimage Size of Factorial Zeroes Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 793 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) |

## Problem Description

### Goal

Define `z(x)` as the number of trailing zeroes in the decimal representation of factorial $x!$. Given a non-negative integer `k`, consider the preimage of `k` under this function.

Return the number of non-negative integers `x` satisfying $z(x) = k$. The answer is always either `5`, when one block of five consecutive factorial arguments has exactly that zero count, or `0`, when the function skips `k`.

### Function Contract

**Inputs**

- `k`: a nonnegative target number of factorial trailing zeroes.

**Return value**

- The size of ${x \ge 0: z(x) = k}$, which is always either `5` or `0`.

### Examples

**Example 1**

- Input: `k = 0`
- Output: `5`
- Explanation: $0!$ through $4!$ have no trailing zeroes.

**Example 2**

- Input: `k = 5`
- Output: `0`
- Explanation: The zero count jumps from `4` at $24!$ to `6` at $25!$, so it never equals five.

**Example 3**

- Input: `k = 3`
- Output: `5`
- Explanation: $15!$ through $19!$ each have three trailing zeroes.
