# Minimum Number of Operations to Make Array Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2870 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing positive integers. You may perform either of the following operations any number of times:

- choose two elements with equal values and delete both;
- choose three elements with equal values and delete all three.

Find the minimum number of operations needed to delete every element. If the array cannot be made empty using these operations, return `-1`.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $2 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- The minimum number of equal-pair and equal-triple deletions needed to empty `nums`, or `-1` when no valid sequence exists.

### Examples

#### Example 1

- **Input:** `nums = [2,3,3,2,2,4,2,3,4]`
- **Output:** `4`
- **Explanation:** Delete the four copies of `2` as two pairs, the three copies of `3` as one triple, and the two copies of `4` as one pair.

#### Example 2

- **Input:** `nums = [2,1,2,2,3,3]`
- **Output:** `-1`
- **Explanation:** The only occurrence of `1` cannot be included in either permitted operation.
