# Minimum Impossible OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2568 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Brainteaser |
| Official Link | [minimum-impossible-or](https://leetcode.com/problems/minimum-impossible-or/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the smallest positive integer (a power of two) that cannot be represented as the bitwise OR of any subset of the given array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the smallest power of two that cannot be formed by the bitwise OR of any subset of `nums`.

### Examples
**Example 1**

- Input: `nums = [2, 1]`
- Output: `4`

**Example 2**

- Input: `nums = [5, 3, 2]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 2, 4, 8]`
- Output: `16`

---

## Underlying Base Algorithm(s)
The problem relies on the property of powers of two. Any integer that is a power of two ($2^k$) can only be formed if the number $2^k$ itself exists in the input array. If we sort the array or use a set to check for the presence of $1, 2, 4, 8, \dots$, the first power of two that is missing from the input set is the smallest value that cannot be formed by any combination of OR operations, because any OR combination involving smaller powers of two will never result in a higher power of two unless that specific bit is explicitly provided by an element in the array.

---

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of elements in the input array, as we iterate through the array once to store elements in a set and then iterate through powers of two up to the maximum possible value.
- **Space Complexity**: $O(N)$ to store the unique elements of the input array in a hash set.
