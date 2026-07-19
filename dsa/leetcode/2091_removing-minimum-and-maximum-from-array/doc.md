# Removing Minimum and Maximum From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) |

## Problem Description

### Goal

You are given a zero-indexed array `nums` whose integer values are distinct. Consequently, the array has one uniquely positioned minimum element and one uniquely positioned maximum element; when the array has length one, that sole element serves as both.

One deletion removes the current first element or the current last element. Perform deletions until both original extreme elements have been removed, and return the minimum possible number of deletions. Other elements may be removed along with them.

### Function Contract

**Input**

- `nums`: an array of $n$ distinct integers.
- $1 \le n \le 10^5$ and $-10^5 \le \texttt{nums}[i] \le 10^5$.

**Return value**

Return the minimum number of front and back deletions needed to remove both the minimum and maximum elements.

### Examples

**Example 1**

- Input: `nums = [2, 10, 7, 5, 4, 1, 8, 6]`
- Output: `5`
- Explanation: Remove two elements from the front to include `10` and three from the back to include `1`.

**Example 2**

- Input: `nums = [0, -4, 19, 1, 8, -2, -3, 5]`
- Output: `3`
- Explanation: Removing the first three elements removes both extremes.

**Example 3**

- Input: `nums = [101]`
- Output: `1`
