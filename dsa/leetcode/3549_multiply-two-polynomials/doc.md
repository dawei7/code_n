# Multiply Two Polynomials

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3549 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/multiply-two-polynomials/) |

## Problem Description

### Goal

Two integer arrays `poly1` and `poly2` encode polynomials in ascending exponent order. An entry at index $i$ is the coefficient multiplying $x^i$, so index `0` stores the constant term and trailing entries represent the highest supplied powers. Zero coefficients are meaningful positions and must not be discarded.

Multiply the two represented polynomials. Return every coefficient of the product in the same ascending-exponent order. If the input lengths are $n$ and $m$, the returned array must have exactly $n+m-1$ entries, including a zero coefficient at the highest position when cancellation or a supplied trailing zero produces one.

### Function Contract

**Inputs**

- `poly1`: The integer coefficients of the first polynomial, ordered from $x^0$ upward.
- `poly2`: The integer coefficients of the second polynomial in the same order.

Let $n=\lvert\texttt{poly1}\rvert$, $m=\lvert\texttt{poly2}\rvert$, and $L=n+m-1$. The constraints are $1 \le n,m \le 5\cdot10^4$ and $-10^3 \le \texttt{poly1[i]},\texttt{poly2[j]} \le 10^3$. Each input contains at least one nonzero coefficient.

**Return value**

Return an integer array of length $L$ whose entry at index $k$ is

$$
\sum_{i+j=k}\texttt{poly1[i]}\,\texttt{poly2[j]}.
$$

### Examples

**Example 1**

- Input: `poly1 = [3,2,5], poly2 = [1,4]`
- Output: `[3,14,13,20]`
- Explanation: Equal-exponent contributions combine, giving $3+(3\cdot4+2)x+(2\cdot4+5)x^2+20x^3$.

**Example 2**

- Input: `poly1 = [1,0,-2], poly2 = [-1]`
- Output: `[-1,0,2]`
- Explanation: Multiplication by the constant $-1$ negates every supplied coefficient while preserving the zero term.

**Example 3**

- Input: `poly1 = [1,5,-3], poly2 = [-4,2,0]`
- Output: `[-4,-18,22,-6,0]`
- Explanation: The result retains length $3+3-1=5$, including the final zero coefficient.

---
