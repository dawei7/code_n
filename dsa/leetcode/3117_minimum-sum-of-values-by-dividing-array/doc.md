# Minimum Sum of Values by Dividing Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3117 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Bit Manipulation, Segment Tree, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$ and an integer array `andValues` of length $m$. The value of a nonempty array is its last element. Divide `nums` into exactly $m$ disjoint, nonempty, contiguous subarrays that together preserve the original order and cover every element exactly once.

For the $i$-th subarray, the bitwise AND of all its elements must equal `andValues[i]`. Among every division satisfying all $m$ targets, minimize the sum of the subarray values—that is, the sum of the elements at the chosen right endpoints. Return that minimum sum, or return $-1$ when no valid division exists.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers to partition.
- `andValues`: A list of $m$ required bitwise-AND values, one for each subarray in order.

The constraints are $1 \le n \le 10^4$, $1 \le m \le \min(n,10)$, $1 \le \texttt{nums[i]} < 10^5$, and $0 \le \texttt{andValues[j]} < 10^5$. Let $V=\max(\texttt{nums})$.

**Return value**

Return the minimum possible sum of the last elements of the $m$ subarrays, or $-1$ if the required partition is impossible.

### Examples

#### Example 1

- **Input:** `nums = [1, 4, 3, 3, 2], andValues = [0, 3, 3, 2]`
- **Output:** `12`
- **Explanation:** The only valid division is `[1, 4]`, `[3]`, `[3]`, `[2]`. Its endpoint sum is `4 + 3 + 3 + 2 = 12`.

#### Example 2

- **Input:** `nums = [2, 3, 5, 7, 7, 7, 5], andValues = [0, 7, 5]`
- **Output:** `17`
- **Explanation:** Ending the first subarray at `5` and the second at the first `7` gives endpoint sum `5 + 7 + 5 = 17`, smaller than the other valid divisions.

#### Example 3

- **Input:** `nums = [1, 2, 3, 4], andValues = [2]`
- **Output:** `-1`
- **Explanation:** With one required subarray, all of `nums` must be used, but its bitwise AND is $0$ rather than $2$.
