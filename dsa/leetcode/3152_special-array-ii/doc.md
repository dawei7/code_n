# Special Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/special-array-ii/) |

## Problem Description
### Goal
An array is **special** when every adjacent pair contains values of different parity. You are given an integer array `nums` and a list of inclusive index ranges `queries`.

For each `queries[i] = [from_i, to_i]`, determine whether the subarray from `nums[from_i]` through `nums[to_i]` is special. Return one boolean per query in the same order. A one-element range is special because it contains no adjacent pair that can violate the condition.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `queries`: A list of $q$ pairs `[from_i, to_i]`, where $1 \le q \le 10^5$ and $0 \le \texttt{from_i} \le \texttt{to_i} < n$.

**Return value**

Return a list `answer` of $q$ booleans. Its $i$-th value is `true` exactly when every adjacent pair inside the inclusive range `[from_i, to_i]` has different parity.

### Examples
**Example 1**

- Input: `nums = [3,4,1,2,6]`, `queries = [[0,4]]`
- Output: `[false]`
- Explanation: The range contains adjacent even values `2` and `6`.

**Example 2**

- Input: `nums = [4,3,1,6]`, `queries = [[0,2],[2,3]]`
- Output: `[false,true]`
- Explanation: The first range contains the adjacent odd values `3` and `1`; the only pair in the second range alternates parity.

**Example 3**

- Input: `nums = [2,4,1,6]`, `queries = [[1,3],[0,0]]`
- Output: `[true,true]`
- Explanation: The violation between indices `0` and `1` lies outside the first query, and the second query is a singleton.
