# Maximum Strong Pair XOR I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2932 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Trie, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-strong-pair-xor-i/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, call two selected integers $x$ and $y$
a strong pair when

$$
\lvert x-y\rvert\le\min(x,y).
$$

Choose two integers from the array that form a strong pair and maximize their
bitwise XOR. The same array element's value may be selected twice, so every
input always has at least the self-pairs $(x,x)$ with XOR zero. Return the
largest XOR value among all qualifying choices.

### Function Contract

**Inputs**

- `nums`: The positive integers from which both members of the pair are selected.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le50$ and
$1\le\texttt{nums[i]}\le100$.

**Return value**

- The maximum value of `x ^ y` over all strong pairs selected from `nums`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `7`
- Explanation: `(3, 4)` is strong and `3 ^ 4 = 7`, the largest qualifying XOR.

**Example 2**

- Input: `nums = [10, 100]`
- Output: `0`
- Explanation: The distinct values are too far apart, so only self-pairs qualify.

**Example 3**

- Input: `nums = [5, 6, 25, 30]`
- Output: `7`
- Explanation: `(25, 30)` is strong and gives the maximum XOR `7`.
