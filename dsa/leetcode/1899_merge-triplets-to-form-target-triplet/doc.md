# Merge Triplets to Form Target Triplet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1899 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) |

## Problem Description

### Goal

You are given an array `triplets`, whose elements each contain exactly three integers, and a three-integer `target`. In one operation, choose two distinct triplet indices `i` and `j`, then replace `triplets[j]` by the coordinate-wise maximum of those two triplets. Thus each coordinate of the destination can stay unchanged or increase, but can never decrease.

You may perform this operation any number of times, including zero. Determine whether `target` can appear as one of the triplets after some sequence of operations. Return `True` when it can be formed and `False` otherwise.

### Function Contract

**Inputs**

- `triplets`: an array of $n$ triplets, with $1 \le n \le 10^5$.
- `target`: the desired triplet.
- Every coordinate in `triplets` and `target` is an integer from $1$ through $1000$.

**Return value**

Return `True` if coordinate-wise maximum operations between distinct triplets can make some element equal `target`; otherwise return `False`.

### Examples

**Example 1**

- Input: `triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5]`
- Output: `True`
- Explanation: Merging the first triplet into the third gives `[2, 7, 5]`. The middle triplet is not used because its second coordinate exceeds the target.

**Example 2**

- Input: `triplets = [[3, 4, 5], [4, 5, 6]], target = [3, 2, 5]`
- Output: `False`
- Explanation: No coordinate-wise maximum can produce `2` in the second position because both available values are already larger.

**Example 3**

- Input: `triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target = [5, 5, 5]`
- Output: `True`
- Explanation: Eligible triplets collectively provide exact values `5` in all three coordinates without exceeding the target.
