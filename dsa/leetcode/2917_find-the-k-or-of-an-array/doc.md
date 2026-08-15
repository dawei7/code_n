# Find the K-or of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2917 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-or-of-an-array/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer threshold `k`, extend the
standard bitwise OR operation to form the array's K-or. Consider every binary
bit position independently: that position is `1` in the result exactly when
at least `k` array elements have a `1` there.

Return the integer represented by all qualifying positions. Repeated values
remain separate array elements and each contributes to the count. Positions
appearing in fewer than `k` elements are `0` in the result, even when they
occur in some values.

### Function Contract

**Inputs**

- `nums`: A non-empty list of non-negative integers.
- `k`: The minimum number of array elements that must contain a bit.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are
$1\le n\le 50$, $0\le\texttt{nums[i]}<2^{31}$, and $1\le\texttt{k}\le n$.

**Return value**

- The K-or of `nums`.

### Examples

#### Example 1

- **Input:** `nums = [7, 12, 9, 8, 9, 15], k = 4`
- **Output:** `9`
- **Explanation:** Bit 0 occurs in `7`, both copies of `9`, and `15`. Bit 3
  occurs in five values. Those are the only positions reaching four
  occurrences, so the result is `1001` in binary.

#### Example 2

- **Input:** `nums = [2, 12, 1, 11, 4, 5], k = 6`
- **Output:** `0`
- **Explanation:** No bit is present in every one of the six values.

#### Example 3

- **Input:** `nums = [10, 8, 5, 9, 11, 6, 8], k = 1`
- **Output:** `15`
- **Explanation:** With a threshold of one, every bit appearing anywhere
  qualifies, which is the ordinary bitwise OR of the array.
