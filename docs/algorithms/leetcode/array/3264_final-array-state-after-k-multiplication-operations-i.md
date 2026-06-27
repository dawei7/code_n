# Final Array State After K Multiplication Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3264 |
| Difficulty | Easy |
| Topics | Array, Math, Heap (Priority Queue), Simulation |
| Official Link | [final-array-state-after-k-multiplication-operations-i](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/) |

## Problem Description & Examples
### Goal
Given an array of integers and a multiplier, perform exactly K operations. In each operation, identify the smallest element in the array (if there are ties, pick the leftmost one) and replace it with the product of that element and the multiplier. Return the final state of the array after all K operations are completed.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the number of multiplication operations to perform.
- `multiplier`: An integer used to multiply the smallest element in each step.

**Return value**

- A list of integers representing the array after K operations.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 5, 6], k = 5, multiplier = 2`
- Output: `[8, 4, 6, 5, 6]`

**Example 2**

- Input: `nums = [1, 2], k = 3, multiplier = 4`
- Output: `[16, 8]`

**Example 3**

- Input: `nums = [10, 7, 13], k = 2, multiplier = 2`
- Output: `[20, 14, 13]`

---

## Underlying Base Algorithm(s)
The problem is best solved using a Min-Heap (Priority Queue). By storing pairs of `(value, index)` in the heap, we can efficiently extract the minimum element in $O(\log N)$ time. After multiplying the value, we push the updated pair back into the heap. This simulation approach ensures we always process the smallest element correctly according to the tie-breaking rule.

---

## Complexity Analysis
- **Time Complexity**: $O(K \log N + N)$, where $N$ is the length of the array. We perform $K$ heap operations, each taking $O(\log N)$ time, and the initial heap construction takes $O(N)$.
- **Space Complexity**: $O(N)$ to store the heap containing all elements of the array.
