# Next Greater Element IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2454 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Stack, Sorting, Heap (Priority Queue), Monotonic Stack |
| Official Link | [next-greater-element-iv](https://leetcode.com/problems/next-given-element-iv/) |

## Problem Description & Examples
### Goal
Given an array of integers, for each element, identify the second integer to its right that is strictly greater than it. If no such element exists for a given position, return -1 for that index.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the second greater element for each index in the input array.

### Examples
**Example 1**

- Input: `nums = [2, 4, 0, 9, 6]`
- Output: `[9, 6, 6, -1, -1]`

**Example 2**

- Input: `nums = [3, 3]`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums = [1, 17, 18, 0, 18, 10, 20, 0]`
- Output: `[18, 18, 20, 18, 20, 20, -1, -1]`

---

## Underlying Base Algorithm(s)
The problem is solved using two monotonic stacks. The first stack maintains indices of elements that are waiting for their *first* greater element. Once an element finds its first greater element, it is moved to a second stack, where it waits for its *second* greater element. By processing the array linearly, we ensure that elements are moved from the "waiting for first" state to the "waiting for second" state efficiently.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is pushed and popped from each stack at most once.
- **Space Complexity**: `O(n)` to store the result array and the two monotonic stacks.
