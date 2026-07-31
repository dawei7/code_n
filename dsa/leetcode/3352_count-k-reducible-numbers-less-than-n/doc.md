# Count K-Reducible Numbers Less Than N

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3352 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/) |

## Problem Description

### Goal

A binary string `s` without leading zeros represents a positive integer $n$. For any positive integer $x$, one reduction operation replaces $x$ with the number of set bits in its binary representation. The integer is `k`-reducible when applying this operation at most `k` times can reach $1$.

Count the positive integers $x$ that are strictly less than $n$ and are `k`-reducible. The upper bound itself must never be counted. Return the count modulo $10^9+7$; `s` may be too long to convert to a native integer.

### Function Contract

**Inputs**

- `s`: The binary representation of $n$, with no leading zero.
- `k`: The maximum permitted number of set-bit-count operations.

Let $m=\lvert\texttt{s}\rvert$. The source guarantees $1 \le m \le 800$, every character of `s` is `0` or `1`, and $1 \le k \le 5$.

**Return value**

- Return the number of positive `k`-reducible integers strictly below $n$, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "111", k = 1`
- Output: `3`
- Explanation: Here $n=7$. The qualifying integers are $1$, $2$, and $4$, each of which is already one or becomes one after a single set-bit count.

**Example 2**

- Input: `s = "1000", k = 2`
- Output: `6`
- Explanation: Here $n=8$. The integers $1$ through $6$ are 2-reducible, while $7$ needs more than two operations.

**Example 3**

- Input: `s = "1", k = 3`
- Output: `0`
- Explanation: The represented bound is $1$, so there is no positive integer strictly below it.
