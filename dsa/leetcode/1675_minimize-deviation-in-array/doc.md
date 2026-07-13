# Minimize Deviation in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1675 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-deviation-in-array](https://leetcode.com/problems/minimize-deviation-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-deviation-in-array/).

### Goal
You may double odd numbers and halve even numbers any number of times while the operation remains valid. Minimize the difference between the maximum and minimum value in the array.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the smallest possible deviation.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `1`

**Example 2**

- Input: `nums = [4,1,5,20,3]`
- Output: `3`

**Example 3**

- Input: `nums = [2,10,8]`
- Output: `3`

---

## Solution
### Approach
Normalize every number to its largest useful value by doubling odds once; all values are then even or already fixed at their maximum. Track the current minimum and keep the values in a max-heap. Repeatedly reduce the current maximum while it is even, updating the best `max - min` range after each step. Stop when the maximum is odd because it cannot be lowered further.

### Complexity Analysis
- **Time Complexity**: `O(n log n log M)`, where `M` is the largest value
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
