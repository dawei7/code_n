# Maximum Total Subarray Value I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3689 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-i/) |

## Problem Description

### Goal

Choose exactly `k` nonempty subarrays of `nums`. The chosen intervals may overlap, and an interval with the same endpoints may be chosen more than once. For any selected subarray, its value is its maximum element minus its minimum element.

Add the values of all `k` choices and maximize that total. Return the greatest total possible. The permission to repeat an identical subarray is material: each choice is independent and does not consume, alter, or reserve any array position for later choices.

### Function Contract

**Inputs**

- `nums`: A nonempty list of $n$ integers, where $1 \le n \le 5\cdot10^4$ and $0 \le \texttt{nums[i]} \le 10^9$.
- `k`: The exact number of subarrays to choose, with $1 \le k \le 10^5$.

**Return value**

Return the maximum sum of the ranges of exactly `k` chosen nonempty subarrays. The result may exceed 32-bit integer range.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 2], k = 2`
- **Output:** `4`

The global range is 2, and two choices can each achieve it.

#### Example 2

- **Input:** `nums = [4, 2, 5, 1], k = 3`
- **Output:** `12`

Each choice can use a subarray containing both 5 and 1 and contribute 4.

#### Example 3

- **Input:** `nums = [7], k = 10`
- **Output:** `0`

Every nonempty subarray of a singleton has range zero, even when selected repeatedly.
