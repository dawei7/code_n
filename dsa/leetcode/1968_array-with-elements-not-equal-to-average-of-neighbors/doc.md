# Array With Elements Not Equal to Average of Neighbors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1968 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) |

## Problem Description
### Goal
You are given a 0-indexed array `nums` containing distinct integers. Rearrange
all of its elements so that no interior element equals the arithmetic average
of its two immediate neighbors.

More precisely, for every index $i$ satisfying $1 \le i < N - 1$, the returned
array must obey

$$
2\cdot\texttt{nums[i]} \ne \texttt{nums[i - 1]}+\texttt{nums[i + 1]}.
$$

Return any permutation that meets this condition. The first and last elements
have only one neighbor and therefore impose no average constraint.

### Function Contract
**Inputs**

- `nums`: a list of $N$ distinct integers, where
  $3 \le N \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Any permutation of all input values in which every interior value differs
  from the average of its immediate neighbors.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `[1, 2, 4, 5, 3]`

**Example 2**

- Input: `nums = [6, 2, 0, 9, 7]`
- Output: `[9, 7, 6, 2, 0]`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `[2, 1, 3]`
