# Queries on a Permutation With Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1409 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/queries-on-a-permutation-with-key/) |

## Problem Description

### Goal

Start with the permutation `P = [1, 2, ..., m]`. Process the values in `queries` from left to right. For each query value, find its current zero-based index in `P` and append that index to the answer.

After recording the index, remove that occurrence from its current position and move it to the front of `P`. Each later query observes the permutation produced by every earlier move. Return the recorded indices in query order.

### Function Contract

**Inputs**

- `queries`: an array of $q$ values, where $1 \le q \le 1000$ and every value lies from 1 through `m`.
- `m`: the size and maximum value of the initial permutation, where $1 \le m \le 1000$.

**Return value**

- An array of $q$ zero-based positions, each measured immediately before its queried value moves to the front.

### Examples

**Example 1**

- Input: `queries = [3,1,2,1], m = 5`
- Output: `[2,1,2,1]`

**Example 2**

- Input: `queries = [4,1,2,2], m = 4`
- Output: `[3,1,2,0]`

**Example 3**

- Input: `queries = [7,5,5,8,3], m = 8`
- Output: `[6,5,0,7,5]`
