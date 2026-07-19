# Rotate Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 189 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-array/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` and a nonnegative integer `k`, rotate the array to the right. One rightward step moves the final element to index zero and shifts every other element one position later; apply this transformation `k` times conceptually.

Modify `nums` in place and return nothing. Because a full array-length rotation restores the original order, values of `k` larger than the length wrap around rather than extending the array. Preserve every element and duplicate occurrence exactly once, and use the required constant extra space instead of returning or retaining a separate rotated copy.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list
- `k`: a nonnegative rotation count

**Return value**

Return nothing. Mutate `nums` in place to contain the right rotation.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5,6,7], k = 3`
- Mutated value: `[5,6,7,1,2,3,4]`

**Example 2**

- Input: `nums = [-1,-100,3,99], k = 2`
- Mutated value: `[3,99,-1,-100]`

**Example 3**

- Input: `nums = [1,2], k = 4`
- Mutated value: `[1,2]`
