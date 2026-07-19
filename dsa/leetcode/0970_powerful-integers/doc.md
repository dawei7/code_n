# Powerful Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 970 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [powerful-integers](https://leetcode.com/problems/powerful-integers/) |

## Problem Description

### Goal

For non-negative integers $i$ and $j$, a powerful integer has the form $x^i+y^j$. Given positive bases `x` and `y` together with an inclusive upper limit `bound`, find every distinct powerful integer whose value is at most `bound`.

The exponents may independently be zero, so each base contributes $1$ as its first power. Return each qualifying value once, in any order, even when several exponent pairs produce the same sum.

### Function Contract

**Inputs**

- `x` and `y`: integer bases satisfying $1 \le x,y \le 100$.
- `bound`: an inclusive upper bound satisfying $0 \le \texttt{bound} \le 10^6$.
- Let $P_x$ and $P_y$ be the distinct powers of the two bases that need consideration, beginning with exponent zero and ending once further growth cannot participate in a bounded sum. Define $A=\lvert P_x\rvert$ and $B=\lvert P_y\rvert$.
- Let $R$ be the number of distinct returned sums.

**Return value**

Return every distinct value $x^i+y^j\le\texttt{bound}$ for integers $i,j\ge0$, in any order.

### Examples

**Example 1**

- Input: `x = 2, y = 3, bound = 10`
- Output: `[2,3,4,5,7,9,10]`

**Example 2**

- Input: `x = 3, y = 5, bound = 15`
- Output: `[2,4,6,8,10,14]`
