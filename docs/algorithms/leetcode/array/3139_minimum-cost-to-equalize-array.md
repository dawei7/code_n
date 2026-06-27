# Minimum Cost to Equalize Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3139 |
| Difficulty | Hard |
| Topics | Array, Greedy, Enumeration |
| Official Link | [minimum-cost-to-equalize-array](https://leetcode.com/problems/minimum-cost-to-equalize-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the minimum cost to make all elements equal to some target value $T$, where $T \ge \max(\text{nums})$. You can increment any element by 1 at a cost of `cost1`, or increment two distinct elements by 1 at a cost of `cost2`. The goal is to find the minimum total cost across all possible target values $T$ (specifically, $T$ can range from $\max(\text{nums})$ to $2 \times \max(\text{nums})$).

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `cost1`: An integer representing the cost to increment a single element.
- `cost2`: An integer representing the cost to increment two distinct elements.

**Return value**

- An integer representing the minimum cost to make all elements equal, modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [4,1], cost1 = 5, cost2 = 2`
- Output: `15`

**Example 2**

- Input: `nums = [2,3,3,3,5], cost1 = 2, cost2 = 1`
- Output: `6`

**Example 3**

- Input: `nums = [3,5,3], cost1 = 1, cost2 = 3`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved by iterating over possible target values $T$. For a fixed $T$, let $S$ be the sum of differences $(T - \text{nums}[i])$ and $M$ be the maximum difference. If $2 \times M \le S$, we can pair up increments efficiently using `cost2` as much as possible. If $2 \times M > S$, we are forced to use `cost1` for the remaining increments of the maximum element after pairing all other elements. We use mathematical optimization to calculate the cost for each $T$ and take the minimum.

---

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the length of the array, due to the initial pass to find the sum and max, followed by a linear scan over the possible target values.
- **Space Complexity**: $O(1)$, as we only store a few variables regardless of input size.
