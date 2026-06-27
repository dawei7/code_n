# Apple Redistribution into Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3074 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting |
| Official Link | [apple-redistribution-into-boxes](https://leetcode.com/problems/apple-redistribution-into-boxes/) |

## Problem Description & Examples
### Goal
Given a collection of apples distributed across several packs and a set of empty boxes with varying capacities, determine the minimum number of boxes required to store all the apples. You can move apples freely between packs and boxes.

### Function Contract
**Inputs**

- `apple`: A list of integers where each element represents the number of apples in a specific pack.
- `capacity`: A list of integers where each element represents the maximum number of apples a specific box can hold.

**Return value**

- An integer representing the minimum number of boxes needed to contain the total sum of apples.

### Examples
**Example 1**

- Input: `apple = [1, 3, 2]`, `capacity = [4, 3, 1, 5, 2]`
- Output: `2`

**Example 2**

- Input: `apple = [5, 5, 5]`, `capacity = [2, 4, 2, 7]`
- Output: `4`

**Example 3**

- Input: `apple = [9, 10]`, `capacity = [1, 2, 3, 4, 5]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. By calculating the total number of apples and sorting the box capacities in descending order, we can iteratively select the largest available boxes until the total capacity meets or exceeds the total number of apples.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N + M \log M)$, where $N$ is the number of apple packs and $M$ is the number of boxes. This is dominated by the sorting of the `capacity` array.
- **Space Complexity**: $O(1)$ or $O(M)$ depending on the sorting implementation's space requirements.
