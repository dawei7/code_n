# Minimum Number of Operations to Make Arrays Similar

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2449 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Number of Operations to Make Arrays Similar](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/) |

## Problem Description

### Goal

You are given two positive-integer arrays, `nums` and `target`, with the same length. In one operation, choose two distinct indices `i` and `j`, increase `nums[i]` by 2, and decrease `nums[j]` by 2.

Two arrays are similar when every integer has the same frequency in both arrays; their positions do not have to match. Return the minimum number of operations needed to make `nums` similar to `target`. The input guarantees that such a transformation is possible.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers representing the initial multiset.
- `target`: A list of $n$ positive integers representing the required multiset.

For both arrays, $1 \le n \le 10^5$ and every value is between 1 and $10^6$, inclusive. The arrays are guaranteed to be transformable under the stated operation.

**Return value**

- The minimum number of operations required to make the value frequencies in `nums` equal those in `target`.

### Examples

#### Example 1

- **Input:** `nums = [8, 12, 6], target = [2, 14, 10]`
- **Output:** `2`
- **Explanation:** Two transfers of 2 can produce the multiset `{2, 10, 14}`.

#### Example 2

- **Input:** `nums = [1, 2, 5], target = [4, 1, 3]`
- **Output:** `1`
- **Explanation:** Increasing 2 to 4 while decreasing 5 to 3 completes the transformation.

#### Example 3

- **Input:** `nums = [1, 1, 1, 1, 1], target = [1, 1, 1, 1, 1]`
- **Output:** `0`
- **Explanation:** The arrays are already similar.
