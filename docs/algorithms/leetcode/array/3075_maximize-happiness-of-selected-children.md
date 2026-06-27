# Maximize Happiness of Selected Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3075 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximize-happiness-of-selected-children](https://leetcode.com/problems/maximize-happiness-of-selected-children/) |

## Problem Description & Examples
### Goal
Given an array representing the initial happiness levels of children and an integer representing the number of turns available, select children one by one to maximize the total happiness. Each time a child is selected, their happiness decreases by the number of children already chosen (starting from 0). If a child's happiness would drop below zero, it is treated as zero.

### Function Contract
**Inputs**

- `happiness`: A list of integers representing the initial happiness values of each child.
- `k`: An integer representing the total number of children to select.

**Return value**

- An integer representing the maximum possible sum of happiness values after selecting exactly `k` children.

### Examples
**Example 1**

- Input: `happiness = [1, 2, 3], k = 2`
- Output: `4`

**Example 2**

- Input: `happiness = [1, 1, 1, 1], k = 2`
- Output: `1`

**Example 3**

- Input: `happiness = [2, 3, 4, 5], k = 1`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. By sorting the happiness values in descending order, we ensure that we always pick the children with the highest current potential happiness first. Since the penalty (the number of children already picked) increases linearly with each selection, picking the largest available values early minimizes the impact of the penalty.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` where `N` is the number of children, primarily due to the sorting step. The subsequent iteration takes `O(k)` time.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(N)`).
