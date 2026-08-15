# Next Greater Element IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2454 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Sorting, Heap (Priority Queue), Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Next Greater Element IV](https://leetcode.com/problems/next-greater-element-iv/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of non-negative integers. For every index `i`, find the value at the second later index whose value is strictly greater than `nums[i]`.

More precisely, `nums[j]` is the second greater value for index `i` when $j>i$, `nums[j] > nums[i]`, and exactly one index `k` with $i<k<j$ also satisfies `nums[k] > nums[i]`. Values equal to `nums[i]` do not count. Return `-1` at positions for which no such second greater value exists.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers, where $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- A length-$n$ list whose entry at index `i` is `nums[i]`'s second strictly greater value to the right, or `-1` when it does not exist.

### Examples

#### Example 1

- **Input:** `nums = [2, 4, 0, 9, 6]`
- **Output:** `[9, 6, 6, -1, -1]`
- **Explanation:** For 2, the greater values arrive as 4 then 9. For 4, they arrive as 9 then 6. To the right of 0, they arrive as 9 then 6.

#### Example 2

- **Input:** `nums = [3, 3]`
- **Output:** `[-1, -1]`
- **Explanation:** Equal values are not strictly greater, and neither index has two qualifying later values.
