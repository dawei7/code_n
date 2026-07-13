# Divide Array Into Increasing Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1121 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [divide-array-into-increasing-sequences](https://leetcode.com/problems/divide-array-into-increasing-sequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/divide-array-into-increasing-sequences/).

### Goal
Given a sorted nondecreasing array, decide whether all elements can be split into one or more strictly increasing subsequences, each of length at least `k`.

### Function Contract
**Inputs**

- `nums`: Sorted nondecreasing list of integers.
- `k`: Required minimum subsequence length.

**Return value**

Boolean indicating whether such a division is possible.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 3, 3, 4, 4], k = 3`
- Output: `true`

**Example 2**

- Input: `nums = [1, 2, 2, 3, 3, 4, 4], k = 4`
- Output: `false`

**Example 3**

- Input: `nums = [1, 2, 3, 4], k = 3`
- Output: `true`

---

## Solution
### Approach
In a strictly increasing subsequence, duplicate values cannot appear together. Therefore the most frequent value determines the minimum number of subsequences needed. If the maximum frequency is `f`, at least `f` subsequences are required.

All subsequences must have length at least `k`, so the total array length must be at least `f * k`. Because the array is sorted, this condition is also sufficient.

### Complexity Analysis
- **Time Complexity**: `O(n)` to find the maximum frequency.
- **Space Complexity**: `O(1)` extra space when scanning the sorted array.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
