# Sequence Reconstruction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 444 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/sequence-reconstruction/) |

## Problem Description
### Goal
Given a proposed sequence `nums` and a collection of subsequences, each subsequence imposes relative-order constraints on its listed values. Determine whether those constraints represent every required value and force one complete ordering.

Return `True` only when `nums` is the unique sequence satisfying all imposed precedences. If another topological ordering is possible, a constraint contradicts `nums`, a cycle exists, or a required value is never represented, return `False`. Individual subsequences need not be contiguous portions of `nums`, but their values must appear in the same relative order. Do not accept uniqueness of only a partial represented set.

### Function Contract
**Inputs**

- `nums`: the proposed permutation to reconstruct
- `sequences`: subsequences whose relative orders impose precedence constraints

**Return value**

- Return `True` exactly when every value is represented and `nums` is the unique topological order satisfying all subsequences.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], sequences = [[1, 2], [1, 3]]`
- Output: `False`

**Example 2**

- Input: `nums = [1, 2, 3], sequences = [[1, 2], [1, 3], [2, 3]]`
- Output: `True`

**Example 3**

- Input: `nums = [1], sequences = [[1]]`
- Output: `True`
