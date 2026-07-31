# Maximum Number of Operations With the Same Score II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3040 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/) |

## Problem Description
### Goal
You are given an integer array `nums`. While at least two elements remain, an operation may delete either the first two elements, the last two elements, or the first and last elements. The operation's score is the sum of the two deleted values.

Choose a sequence of operations of maximum possible length subject to every operation having the same score. The first operation determines that common score, but both the first choice and every later choice may affect how many additional operations remain possible.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An integer array with $2 \le n \le 2000$ and $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the maximum number of legal operations whose scores are all equal.

### Examples
**Example 1**

- Input: `nums = [3,2,1,2,3,4]`
- Output: `3`
- Explanation: Remove `[3,2]`, then the current first and last values `1` and `4`, then `2` and `3`. Each score is `5`, and the array becomes empty.

**Example 2**

- Input: `nums = [3,2,6,1,4]`
- Output: `2`
- Explanation: Remove the first two values `3` and `2`, then the last two values `1` and `4`. Both scores are `5`; no sequence can perform more than two operations.
