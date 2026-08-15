# Count Elements With Strictly Smaller and Greater Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2148 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-elements-with-strictly-smaller-and-greater-elements](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/) |

## Problem Description

### Goal

Given an integer array `nums`, examine each element occurrence independently.
An occurrence qualifies when some element in the same array has a strictly
smaller value and some element has a strictly greater value.

Return the number of qualifying occurrences. Equal values remain separate
elements when counted: if a value lies strictly between the array's smallest
and greatest values, every occurrence of that value qualifies. An occurrence
equal to either extreme cannot qualify.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 100$ and
  $-10^5 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return the number of element occurrences for which both a strictly smaller
array element and a strictly greater array element exist.

### Examples

#### Example 1

- **Input:** `nums = [11, 7, 2, 15]`
- **Output:** `2`
- **Explanation:** The occurrences `7` and `11` each have values on both sides of
  them.

#### Example 2

- **Input:** `nums = [-3, 3, 3, 90]`
- **Output:** `2`
- **Explanation:** Both occurrences of `3` lie strictly between `-3` and `90`, so
  both are counted.
