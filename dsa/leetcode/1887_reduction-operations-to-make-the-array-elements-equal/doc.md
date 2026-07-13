# Reduction Operations to Make the Array Elements Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1887 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reduction-operations-to-make-the-array-elements-equal](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/).

### Goal
In one operation, choose an element with the current largest value and reduce it to the next smaller distinct value in the array. Count how many operations are needed until all elements are equal.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the minimum number of reduction operations.

### Examples
**Example 1**

- Input: `nums = [5,1,3]`
- Output: `3`

**Example 2**

- Input: `nums = [1,1,1]`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,2,2,3]`
- Output: `4`

---

## Solution
### Approach
Sort the array. Each time a new larger distinct value appears, all elements at that value and above will need one additional reduction step to eventually reach the minimum. Scan sorted values and add the number of distinct smaller levels seen whenever the value changes.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
