# Append K Integers With Minimal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2195 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/append-k-integers-with-minimal-sum/) |

## Problem Description

### Goal

Choose exactly `k` positive integers to append to `nums`. The chosen integers
must be distinct from one another, and none may already occur anywhere in
`nums`; duplicates already present in `nums` impose only one exclusion.

Among all valid choices, minimize the sum of the appended integers and return
that minimum sum. Only the sum of the new integers is requested, not the sum
of the resulting full array.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1\le n\le10^5$ and each value
  lies in $[1,10^9]$.
- `k`: the number of distinct missing positive integers to append, with
  $1\le k\le10^8$.

**Return value**

Return the minimum possible sum of the `k` appended integers.

### Examples

**Example 1**

- Input: `nums = [1,4,25,10,25]`, `k = 2`
- Output: `5`

**Example 2**

- Input: `nums = [5,6]`, `k = 6`
- Output: `25`

**Example 3**

- Input: `nums = [1,1,2]`, `k = 3`
- Output: `12`
