# Maximum Strong Pair XOR II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2935 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Trie, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-strong-pair-xor-ii/) |

## Problem Description

### Goal

Given a 0-indexed positive integer array `nums`, two selected integers $x$ and
$y$ form a strong pair when

$$
\lvert x-y\rvert\le\min(x,y).
$$

Select a strong pair whose bitwise XOR is as large as possible and return that
XOR value. The same integer may be selected twice, so self-pairs are permitted
and always provide a valid XOR of zero. The array can contain up to 50,000
values, requiring more than direct enumeration of all pairs.

### Function Contract

**Inputs**

- `nums`: The positive integers from which both values of the pair are selected.

Let $n=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. The constraints
are $1\le n\le5\cdot10^4$ and $1\le\texttt{nums[i]}<2^{20}$.

**Return value**

- The maximum `x ^ y` among all strong pairs selected from `nums`.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5]`
- **Output:** `7`
- **Explanation:** The strong pair `(3, 4)` has `3 ^ 4 = 7`.

#### Example 2

- **Input:** `nums = [10, 100]`
- **Output:** `0`
- **Explanation:** The distinct values are not strong together, leaving only zero-XOR self-pairs.

#### Example 3

- **Input:** `nums = [500, 520, 2500, 3000]`
- **Output:** `1020`
- **Explanation:** `(500, 520)` is strong and its XOR 1020 exceeds the XOR of the other distinct strong pair.
