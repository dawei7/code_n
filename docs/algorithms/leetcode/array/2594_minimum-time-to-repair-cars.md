# Minimum Time to Repair Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2594 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [minimum-time-to-repair-cars](https://leetcode.com/problems/minimum-time-to-repair-cars/) |

## Problem Description & Examples
### Goal
Given an array of integers representing the rank of each mechanic and the total number of cars to be repaired, determine the minimum time required to complete all repairs. Each mechanic with rank `r` can repair `n` cars in `r * n^2` time. Mechanics work simultaneously.

### Function Contract
**Inputs**

- `ranks`: A list of integers where `ranks[i]` is the rank of the i-th mechanic.
- `cars`: An integer representing the total number of cars that need to be repaired.

**Return value**

- An integer representing the minimum time required to repair all cars.

### Examples
**Example 1**

- Input: `ranks = [4, 2, 3, 1], cars = 10`
- Output: `16`

**Example 2**

- Input: `ranks = [5, 1, 8], cars = 6`
- Output: `16`

**Example 3**

- Input: `ranks = [1], cars = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem exhibits a monotonic property: if it is possible to repair all cars within time `T`, it is also possible to repair them in any time `T' > T`. This allows us to use **Binary Search on the Answer**. We define the search space between 1 and the worst-case scenario (the fastest mechanic repairing all cars alone). For a given time `t`, the number of cars a mechanic with rank `r` can repair is `floor(sqrt(t / r))`.

---

## Complexity Analysis
- **Time Complexity**: `O(N * log(M))`, where `N` is the number of mechanics and `M` is the maximum possible time (rank of the fastest mechanic * cars^2).
- **Space Complexity**: `O(1)`, as we only use a few variables for the binary search bounds.
