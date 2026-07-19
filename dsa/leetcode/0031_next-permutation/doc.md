# Next Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 31 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/next-permutation/) |

## Problem Description
### Goal
An integer array `nums` represents one permutation of its multiset of values. In lexicographic order, one permutation precedes another when its first differing position contains the smaller value. Rearrange the array into the smallest permutation that is still greater than its current ordering.

If no lexicographically greater permutation exists because the array is in descending order, rearrange it into the lowest possible order, sorted in ascending order. Duplicate values remain with their original multiplicities. Perform the transformation in place with constant auxiliary space; the caller observes the mutated array rather than a separate returned permutation.

### Function Contract
**Inputs**

- `nums`: non-empty `List[int]`

**Return value**

`None`; the app and platform judge inspect the mutated `nums` array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `nums = [1, 3, 2]`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `nums = [1, 2, 3]`

**Example 3**

- Input: `nums = [1, 1, 5]`
- Output: `nums = [1, 5, 1]`
