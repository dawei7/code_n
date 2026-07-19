# Reverse Subarray To Maximize Array Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1330 |
| Difficulty | Hard |
| Topics | Array, Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/) |

## Problem Description
### Goal
The value of an integer array is the sum of the absolute differences between every adjacent pair. For `nums`, it is

$$
V=\sum_{i=0}^{n-2}\lvert\texttt{nums[i]}-\texttt{nums[i+1]}\rvert.
$$

Choose one contiguous subarray and reverse its elements. The operation may cover any nonempty range, including the entire array; ranges of length one leave the array unchanged.

Return the maximum possible value after this one allowed reversal. Array elements may be negative, and the result is guaranteed to fit in a signed 32-bit integer.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $2\le n\le3\cdot10^4$ and $-10^5\le\texttt{nums[i]}\le10^5$.

**Return value**

The greatest adjacent-difference sum obtainable after reversing one contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [2,3,1,5,4]`
- Output: `10`
- Explanation: Reversing `[3,1,5]` produces `[2,5,1,3,4]`, whose adjacent differences sum to 10.

**Example 2**

- Input: `nums = [2,4,9,24,2,1,10]`
- Output: `68`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `3`
- Explanation: Reversing the first two values yields `[2,1,3]`.
