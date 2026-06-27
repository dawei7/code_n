# Mice and Cheese

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2611 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [mice-and-cheese](https://leetcode.com/problems/mice-and-cheese/) |

## Problem Description & Examples
### Goal
Two mice are tasked with eating $n$ pieces of cheese. Each piece of cheese has a specific point value if eaten by the first mouse and a different point value if eaten by the second mouse. Given that the first mouse must eat exactly $k$ pieces of cheese, determine the maximum total points achievable by both mice combined.

### Function Contract
**Inputs**

- `reward1`: A list of integers representing the points gained if the first mouse eats the $i$-th piece of cheese.
- `reward2`: A list of integers representing the points gained if the second mouse eats the $i$-th piece of cheese.
- `k`: An integer representing the exact number of pieces the first mouse must consume.

**Return value**

- An integer representing the maximum total points possible.

### Examples
**Example 1**

- Input: `reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2`
- Output: `15`

**Example 2**

- Input: `reward1 = [1,1], reward2 = [1,1], k = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. We assume initially that the second mouse eats all $n$ pieces of cheese, yielding a base sum of all values in `reward2`. To satisfy the constraint that the first mouse eats exactly $k$ pieces, we calculate the "gain" of switching a piece from the second mouse to the first: `gain = reward1[i] - reward2[i]`. By selecting the $k$ pieces with the largest positive gains, we maximize the total score.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the sorting of the gain differences, where $n$ is the number of cheese pieces.
- **Space Complexity**: $O(n)$ to store the list of gain differences.
