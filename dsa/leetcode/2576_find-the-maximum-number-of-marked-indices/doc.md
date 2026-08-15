# Find the Maximum Number of Marked Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2576 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-maximum-number-of-marked-indices](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. Initially, every index is unmarked.

You may repeatedly choose two different indices `i` and `j` that are both still unmarked and satisfy `2 * nums[i] <= nums[j]`. That operation marks both selected indices, so neither may participate in another operation.

Return the maximum number of indices that can be marked after performing any number of valid operations.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

The length satisfies $1 \le n \le 10^5$, and every element satisfies $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the greatest even number of indices that can be partitioned into valid pairs under the doubling condition.

### Examples

#### Example 1

- **Input:** `nums = [3,5,2,4]`
- **Output:** `2`
- **Explanation:** Values `2` and `5` can form one valid pair. No second disjoint valid pair exists.

#### Example 2

- **Input:** `nums = [9,2,5,4]`
- **Output:** `4`
- **Explanation:** Pair `4` with `9` and `2` with `5`, marking every index.

#### Example 3

- **Input:** `nums = [7,6,8]`
- **Output:** `0`
- **Explanation:** No two values satisfy the required inequality.
