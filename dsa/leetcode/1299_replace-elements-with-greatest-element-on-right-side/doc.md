# Replace Elements with Greatest Element on Right Side

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1299 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) |

## Problem Description
### Goal
Given an integer array `arr`, replace the value at every index with the greatest value among the elements strictly to its right. The original value at the current index is not part of that comparison, even when it is larger than every later value.

The final index has no element to its right, so its replacement is always `-1`. Return the array after every position has been replaced according to this rule.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 10^4$ and $1 \le \texttt{arr[i]} \le 10^5$.

**Return value**

The transformed array whose index $i<n-1$ contains $\max(\texttt{arr[i+1:]})$ from the original input and whose final value is `-1`.

### Examples
**Example 1**

- Input: `arr = [17,18,5,4,6,1]`
- Output: `[18,6,6,6,1,-1]`
- Explanation: Each value is the maximum of the original suffix beginning one position later.

**Example 2**

- Input: `arr = [400]`
- Output: `[-1]`
- Explanation: The only position has no value to its right.

**Example 3**

- Input: `arr = [9,8,7]`
- Output: `[8,7,-1]`
- Explanation: In a strictly decreasing array, each position is replaced by its immediate successor.
