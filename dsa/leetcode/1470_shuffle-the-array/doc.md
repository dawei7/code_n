# Shuffle the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1470 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-the-array/) |

## Problem Description
### Goal

The array `nums` contains exactly $2n$ elements arranged as two consecutive halves:

$$
[x_1,x_2,\ldots,x_n,y_1,y_2,\ldots,y_n].
$$

Construct and return a new array that alternates corresponding elements from the two halves, producing

$$
[x_1,y_1,x_2,y_2,\ldots,x_n,y_n].
$$

The pairing is positional: the first item of the first half is matched with the first item of the second half, and so on through position $n$. Equal values remain separate occurrences and do not change this mapping.

### Function Contract
**Inputs**

- `nums`: an integer array of length exactly $2n$.
- `n`: the length of either half, where $1 \le n \le 500$.
- Every value in `nums` lies in the inclusive range $[1,1000]$.

**Return value**

Return an array of length $2n$ in which `nums[i]` is followed by `nums[i + n]` for every index $0 \le i < n$.

### Examples
**Example 1**

- Input: `nums = [2,5,1,3,4,7], n = 3`
- Output: `[2,3,5,4,1,7]`
- Explanation: The halves `[2,5,1]` and `[3,4,7]` are interleaved pair by pair.

**Example 2**

- Input: `nums = [1,2,3,4,4,3,2,1], n = 4`
- Output: `[1,4,2,3,3,2,4,1]`

**Example 3**

- Input: `nums = [1,1,2,2], n = 2`
- Output: `[1,2,1,2]`
- Explanation: Repeated values retain their positions; the operation rearranges indices, not distinct values.
