# Special Array With X Elements Greater Than or Equal X

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1608 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) |

## Problem Description
### Goal
An array `nums` of non-negative integers is special when some number $x$ has exactly $x$ array elements greater than or equal to $x$. Elements below $x$ do not contribute to this count, and the number $x$ need not occur in the array itself.

Return this $x$ when it exists; otherwise return `-1`. A qualifying value is guaranteed to be unique.

### Function Contract
**Inputs**

- `nums`: an array of $n$ non-negative integers, where $1 \le n \le 100$ and $0 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the unique integer $x$ for which exactly $x$ elements are at least $x$, or `-1` if no such integer exists.

### Examples
**Example 1**

- Input: `nums = [3, 5]`
- Output: `2`
- Explanation: Both elements are at least 2, so exactly two elements meet the threshold.

**Example 2**

- Input: `nums = [0, 0]`
- Output: `-1`

**Example 3**

- Input: `nums = [0, 4, 3, 0, 4]`
- Output: `3`
- Explanation: The three values 4, 3, and 4 are at least 3.
