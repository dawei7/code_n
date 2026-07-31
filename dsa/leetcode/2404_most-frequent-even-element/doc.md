# Most Frequent Even Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2404 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-frequent-even-element/) |

## Problem Description

### Goal

Given an integer array `nums`, consider only its even elements and determine
which even value occurs most frequently. Repeated occurrences of odd values
do not affect the result, and zero is an even value.

If several even values share the greatest frequency, return the smallest of
those tied values. If the array contains no even value at all, return `-1`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 2000$ and
  $0 \le \texttt{nums[i]} \le 10^5$.

Let $u$ be the number of distinct even values in `nums`.

**Return value**

Return the even value with maximum occurrence count, breaking equal-count ties
by smaller numeric value. Return `-1` when $u=0$.

### Examples

**Example 1**

- Input: `nums = [0,1,2,2,4,4,1]`
- Output: `2`
- Explanation: Values 2 and 4 both occur twice, so the smaller is returned.

**Example 2**

- Input: `nums = [4,4,4,9,2,4]`
- Output: `4`
- Explanation: Four occurrences make 4 the unique most frequent even value.

**Example 3**

- Input: `nums = [29,47,21,41,13,37,25,7]`
- Output: `-1`
- Explanation: The array contains no even element.
