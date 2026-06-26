# Maximum XOR With an Element From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1707 |
| Difficulty | Hard |
| Topics | Array, Bit Manipulation, Trie |
| Official Link | [maximum-xor-with-an-element-from-array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) |

## Problem Description & Examples
### Goal
For each query `[x, m]`, find the maximum value of `x XOR num` using a number from `nums` that is at most `m`. If no eligible number exists, answer `-1`.

### Function Contract
**Inputs**

- `nums`: a list of non-negative integers.
- `queries`: a list of `[x, m]` query pairs.

**Return value**

Return the answer for every query in the original order.

### Examples
**Example 1**

- Input: `nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]`
- Output: `[3,3,7]`

**Example 2**

- Input: `nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]`
- Output: `[15,-1,5]`

**Example 3**

- Input: `nums = [1,7,9], queries = [[4,0],[4,8],[4,10]]`
- Output: `[-1,5,13]`

---

## Underlying Base Algorithm(s)
Sort `nums` ascending and process queries in ascending `m`, keeping original query indices. Insert every number whose value is at most the current limit into a binary trie. To answer a query, walk the trie preferring the opposite bit of `x` at each level to maximize XOR. If the trie is empty, return `-1`.

---

## Complexity Analysis
- **Time Complexity**: `O((n + q) log(n + q) + (n + q) * B)`, where `B` is the bit width
- **Space Complexity**: `O(n * B)`
