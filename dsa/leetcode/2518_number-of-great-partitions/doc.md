# Number of Great Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2518 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-great-partitions/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers and an integer `k`.

Assign every array element to exactly one of two ordered groups. A partition is great when the sum of each group is at least `k`. Because the two groups are ordered, exchanging them produces a different partition.

Elements are distinguished by their array positions. Consequently, two assignments are different whenever some `nums[i]` belongs to different groups, even if several elements have the same value.

Return the number of distinct great partitions modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The minimum required sum of each group, where $1 \le k \le 1000$.

**Return value**

Return, modulo $10^9 + 7$, the number of ordered assignments of all elements to two groups such that both group sums are at least `k`.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4], k = 4`
- **Output:** `6`
- **Explanation:** There are three qualifying divisions of the indexed elements, and each division has two orders for its groups.

#### Example 2

- **Input:** `nums = [3, 3, 3], k = 4`
- **Output:** `0`
- **Explanation:** Every split leaves one group with sum below `4`.

#### Example 3

- **Input:** `nums = [6, 6], k = 2`
- **Output:** `2`
- **Explanation:** Either indexed `6` may be assigned to the first group; the equal values do not make those two assignments identical.
