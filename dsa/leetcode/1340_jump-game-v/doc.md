# Jump Game V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1340 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-v/) |

## Problem Description
### Goal
Given an integer array `arr` and a maximum distance `d`, choose any index as a starting position. From index `i`, a jump may move left or right by between 1 and `d` positions without leaving the array.

A destination `j` is legal only when `arr[j] < arr[i]`. In addition, every position strictly between `i` and `j` must also have a value lower than `arr[i]`; the first value greater than or equal to the current value blocks that direction, including every position beyond it.

Return the maximum number of indices that can be visited in one valid sequence, counting its starting index.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1\le n\le1000$ and $1\le\texttt{arr[i]}\le10^5$.
- `d`: the inclusive maximum jump distance, where $1\le d\le n$.

**Return value**

The greatest number of positions in any valid strictly descending jump sequence started at an arbitrary index.

### Examples
**Example 1**

- Input: `arr = [6,4,14,6,8,13,9,7,10,6,12]`, `d = 2`
- Output: `4`

**Example 2**

- Input: `arr = [3,3,3,3,3]`, `d = 3`
- Output: `1`
- Explanation: Equal values are not lower destinations and immediately block further positions.

**Example 3**

- Input: `arr = [7,6,5,4,3,2,1]`, `d = 1`
- Output: `7`
