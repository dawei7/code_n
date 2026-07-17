# Maximum Erasure Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1695 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-erasure-value/) |

## Problem Description
### Goal

You are given an array `nums` of positive integers. Erase exactly one subarray whose elements are all unique. A subarray is a contiguous segment `nums[left:right + 1]`; elements cannot be skipped or reordered when choosing it.

The score earned by erasing the chosen subarray is the sum of its elements. Return the maximum score obtainable from any nonempty contiguous segment with no repeated value. Different occurrences of the same value conflict even when they are far apart inside the candidate segment.

### Function Contract
**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$

**Return value**

The largest sum among all nonempty subarrays whose values are pairwise distinct.

### Examples
**Example 1**

- Input: `nums = [4, 2, 4, 5, 6]`
- Output: `17`

The segment `[2, 4, 5, 6]` is unique and has the maximum sum.

**Example 2**

- Input: `nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]`
- Output: `8`

Either `[5, 2, 1]` or `[1, 2, 5]` achieves the best score.

**Example 3**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`

All values are unique, so erasing the entire array is optimal.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Maintain one maximal unique window**

Move a right boundary from left to right while storing the values in the current window, its left boundary, and its running sum. Before adding `nums[right]`, check whether that value is already present. If it is, repeatedly remove `nums[left]` from the set and sum and advance `left` until the earlier occurrence has been removed. Adding the new value then restores pairwise uniqueness.

Each step leaves the earliest possible left boundary for a unique window ending at `right`. Any other unique subarray ending there must start no earlier, because it also has to exclude the duplicate that forced the shrink. Since every array value is positive, removing additional leading values can only decrease the score. The maintained window is therefore the highest-scoring valid subarray for that right endpoint.

**Track the best endpoint score**

After inserting the new value, compare the running sum with the global maximum. Every nonempty unique subarray has some right endpoint, and the maintained window for that endpoint scores at least as much as any shorter valid suffix. Taking the best maintained sum across all endpoints consequently yields the global optimum.

Although the inner removal loop may execute several times for one new value, each array element enters the window once and leaves it at most once. The two boundaries move only forward.

#### Complexity detail

The right boundary visits all $n$ values once and the left boundary advances at most $n$ times in total, so the running time is $O(n)$. The membership set contains at most $n$ distinct values and uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every starting index:** extending each start until its first duplicate is correct but takes $O(n^2)$ time on an all-distinct array.
- **Prefix sums plus last positions:** jumping `left` past a duplicate and using prefix sums also achieves $O(n)$ time, with a map from values to their latest indices.
- **Sort the values:** sorting destroys contiguity and cannot identify which values coexist in a subarray.
- **Single value:** the only legal subarray is the element itself.
- **All values equal:** every valid subarray has length one, so the answer is that repeated positive value.
- **Positive-value guarantee:** it justifies preferring the longest valid suffix for each endpoint; the same reasoning would fail if removed prefixes could have negative sums.
- **Duplicate at the left boundary:** remove through the earlier copy, not merely one arbitrary value, before inserting the new occurrence.

</details>
