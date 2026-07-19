# Palindrome Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1246 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-removal/) |

## Problem Description

### Goal

You are given an integer array `arr`. In one move, choose any nonempty contiguous subarray that is a palindrome and remove all of its elements. After removal, the elements on its left and right concatenate and become adjacent.

Repeat until the array is empty, and return the minimum possible number of moves. A single element is always a palindrome, but removing some middle elements first may bring equal values together and allow a larger palindrome to be removed in fewer later moves.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le100$ and $1\le\texttt{arr[i]}\le20$.

**Return value**

- The minimum number of palindromic-subarray removals needed to delete the entire array.

### Examples

**Example 1**

- Input: `arr = [1,2]`
- Output: `2`

The two unequal values must be removed separately.

**Example 2**

- Input: `arr = [1,3,4,1,5]`
- Output: `3`

Remove `[4]`, then `[1,3,1]`, then `[5]`.

**Example 3**

- Input: `arr = [1,2,1]`
- Output: `1`

The full array is already a palindrome.
