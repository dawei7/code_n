# Maximum GCD-Sum of a Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2941 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/) |

## Problem Description
### Goal
Given a positive-integer array `nums` and an integer `k`, consider each
subarray containing at least `k` elements. For such a subarray, let $S$ be
the sum of its elements and let $G$ be their greatest common divisor. Its
gcd-sum is the product $S\cdot G$.

Return the largest gcd-sum among all eligible subarrays. A subarray is a
contiguous, nonempty segment of `nums`, and the length requirement is at
least `k`, not exactly `k`.

### Function Contract
**Inputs**

- `nums`: the positive integers from which a contiguous subarray is selected
- `k`: the minimum permitted subarray length

Let $N=\lvert\texttt{nums}\rvert$ and
$V=\max(\texttt{nums})$. The contract guarantees $1 \le N \le 10^5$,
$1 \le V \le 10^6$, and $1 \le k \le N$.

**Return value**

The maximum value of $S\cdot G$ over every subarray of length at least `k`.

### Examples
**Example 1**

- Input: `nums = [2,1,4,4,4,2], k = 2`
- Output: `48`
- Explanation: The subarray `[4,4,4]` has sum `12`, greatest common divisor
  `4`, and gcd-sum `48`.

**Example 2**

- Input: `nums = [7,3,9,4], k = 1`
- Output: `81`
- Explanation: The one-element subarray `[9]` has both sum and greatest
  common divisor equal to `9`.

**Example 3**

- Input: `nums = [5,5,5,5], k = 2`
- Output: `100`
- Explanation: Selecting all four elements gives sum `20` and greatest common
  divisor `5`.
