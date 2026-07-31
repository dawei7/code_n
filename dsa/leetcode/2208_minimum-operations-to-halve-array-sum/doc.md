# Minimum Operations to Halve Array Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) |

## Problem Description

### Goal

Start with an array `nums` of positive integers. In one operation, choose any current array value and replace it with exactly half of that value. A value already reduced by an earlier operation remains eligible to be chosen and halved again.

Minimize the number of operations needed to decrease the array's total sum by at least half of its original value. Halving may create fractional values; the target is based on the initial sum, not on a repeatedly changing fraction of the current sum.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^7$.

Let $k$ denote the minimum number of operations returned.

**Return value**

Return $k$, the fewest exact-halving operations whose combined reduction is at least half the original sum.

### Examples

**Example 1**

- Input: `nums = [5, 19, 8, 1]`
- Output: `3`
- Explanation: halving `19`, then `9.5`, then `8` reduces the sum from `33` to `14.75`.

**Example 2**

- Input: `nums = [3, 8, 20]`
- Output: `3`
- Explanation: halving `20` twice and `3` once removes `16.5`, at least half of `31`.

**Example 3**

- Input: `nums = [10]`
- Output: `1`
- Explanation: one halving changes the only value to `5`, exactly half the original sum.
