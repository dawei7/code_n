# Circular Array Loop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 457 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/circular-array-loop/) |

## Problem Description
### Goal
Given a nonempty circular integer array, position `i` jumps forward or backward by `nums[i]` steps, with indices wrapping around either end. Repeatedly applying jumps defines a directed route from every starting position.

Return `True` when some route contains a cycle visiting more than one distinct index and every jump in that cycle has the same sign. A one-position self-loop is invalid, and a cycle that mixes positive and negative jumps is invalid. Return `False` when no starting point meets both requirements. Detect cycles without allowing traversal state from a failed direction to fabricate another route.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array; `nums[i]` is the signed jump from index `i`, with indices wrapping around the array

**Return value**

- `True` if some cycle has length greater than one and consists entirely of positive jumps or entirely of negative jumps; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [2, -1, 1, 2, 2]`
- Output: `True`

**Example 2**

- Input: `nums = [-1, -2, -3, -4, -5, 6]`
- Output: `False`

**Example 3**

- Input: `nums = [1, -1, 5, 1, 4]`
- Output: `True`
