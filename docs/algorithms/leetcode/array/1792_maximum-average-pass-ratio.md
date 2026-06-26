# Maximum Average Pass Ratio

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1792 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [maximum-average-pass-ratio](https://leetcode.com/problems/maximum-average-pass-ratio/) |

## Problem Description & Examples
### Goal
Each class has passed students and total students. Assign extra students who are guaranteed to pass, one at a time, to maximize the average pass ratio across all classes.

### Function Contract
**Inputs**

- `classes`: a list of `[passed, total]` pairs.
- `extraStudents`: number of guaranteed-passing students to assign.

**Return value**

Return the maximum possible average pass ratio.

### Examples
**Example 1**

- Input: `classes = [[1,2],[3,5],[2,2]], extraStudents = 2`
- Output: `0.78333`

**Example 2**

- Input: `classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4`
- Output: `0.53485`

**Example 3**

- Input: `classes = [[5,5]], extraStudents = 3`
- Output: `1.00000`

---

## Underlying Base Algorithm(s)
For each class, compute the marginal gain from adding one passing student. Use a max-heap keyed by that gain. Repeatedly assign an extra student to the class with the largest current gain, update its counts, and push its new gain back.

---

## Complexity Analysis
- **Time Complexity**: `O((n + extraStudents) log n)`
- **Space Complexity**: `O(n)`
