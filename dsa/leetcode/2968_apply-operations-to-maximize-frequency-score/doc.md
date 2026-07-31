# Apply Operations to Maximize Frequency Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2968 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums` and a nonnegative operation
budget `k`. One operation chooses any array index and increases or decreases
that element by exactly one. You may perform at most `k` operations.

After the changes, the array's score is the frequency of its most frequent
value. Return the greatest score that any permitted sequence of operations can
produce. Elements not contributing to the most frequent value may remain
unchanged or be modified without affecting the requested maximum.

### Function Contract
**Inputs**

- `nums`: the positive integer values that may be incremented or decremented
- `k`: the maximum total number of unit changes

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$, $1\le\texttt{nums[i]}\le10^9$, and
$0\le k\le10^{14}$.

**Return value**

The maximum possible frequency of one value after at most `k` unit increment
or decrement operations.

### Examples
**Example 1**

- Input: `nums = [1,2,6,4], k = 3`
- Output: `3`
- Explanation: Increase `1` to `2` and decrease `4` to `2`, using three operations and producing three copies of `2`.

**Example 2**

- Input: `nums = [1,4,4,2,4], k = 0`
- Output: `3`
- Explanation: No operation is available, and `4` already occurs three times.
