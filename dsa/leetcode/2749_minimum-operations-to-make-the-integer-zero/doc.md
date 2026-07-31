# Minimum Operations to Make the Integer Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2749 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation, Brainteaser, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/) |

## Problem Description

### Goal

You are given integers `num1` and `num2`. In one operation, choose an integer exponent $i$ with $0 \le i \le 60$, then subtract $2^i+\texttt{num2}$ from the current value of `num1`. The exponent may be chosen independently on every operation, including repeated choices.

Determine the minimum number of operations required to make the changing value exactly zero. Intermediate values are not required to stay positive. Return `-1` when no sequence of permitted subtractions can reach zero.

### Function Contract

**Inputs**

- `num1`: The positive starting value, where $1 \le \texttt{num1} \le 10^9$.
- `num2`: The fixed term included in every subtraction, where $-10^9 \le \texttt{num2} \le 10^9$.

**Return value**

Return the minimum number of operations that makes `num1` equal zero, or `-1` if this is impossible.

### Examples

**Example 1**

- Input: `num1 = 3, num2 = -2`
- Output: `3`
- Explanation: Powers $4$, $4$, and $1$ contribute $9$; together with three copies of $-2$, they sum to the starting value $3$.

**Example 2**

- Input: `num1 = 5, num2 = 7`
- Output: `-1`
- Explanation: No allowed sequence of operations has total subtraction exactly equal to $5$.
