# XOR Operation in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1486 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-operation-in-an-array/) |

## Problem Description
### Goal

Given integers `n` and `start`, define a zero-indexed array `nums` of length `n` by

$$
\texttt{nums[i]} = \texttt{start} + 2i
$$

for every $0 \le i < n$. Return the bitwise XOR of all generated elements. The array is conceptual; it does not have to be stored.

The first term is `start`, and every later term is exactly two larger than the preceding term. Include all `n` positions once, combine them with bitwise XOR rather than addition or exponentiation, and return the resulting integer. Because only the aggregate is requested, an implementation may derive it without materializing `nums`.

### Function Contract
**Inputs**

- `n`: the number of generated values, with $1 \le n \le 1000$.
- `start`: the first generated value, with $0 \le \texttt{start} \le 1000$.

**Return value**

Return

$$
\bigoplus_{i=0}^{n-1}(\texttt{start}+2i),
$$

where $\oplus$ denotes bitwise XOR.

### Examples
**Example 1**

- Input: `n = 5, start = 0`
- Generated values: `[0,2,4,6,8]`
- Output: `8`

**Example 2**

- Input: `n = 4, start = 3`
- Generated values: `[3,5,7,9]`
- Output: `8`
