# Rearranging Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2561 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Greedy, Sort |
| Official Link | [rearranging-fruits](https://leetcode.com/problems/rearranging-fruits/) |

## Problem Description & Examples
### Goal
Given two baskets of fruits represented by integer arrays, determine the minimum cost to make both baskets identical. A swap operation between two fruits (one from each basket) costs the minimum value of the two fruits being swapped. If it is impossible to make the baskets identical, return -1.

### Function Contract
**Inputs**

- `basket1`: A list of integers representing the fruits in the first basket.
- `basket2`: A list of integers representing the fruits in the second basket.

**Return value**

- An integer representing the minimum cost to equalize the baskets, or -1 if equalization is impossible.

### Examples
**Example 1**

- Input: `basket1 = [4,2,2,2], basket2 = [1,4,1,2]`
- Output: `5`

**Example 2**

- Input: `basket1 = [2,3,4,1], basket2 = [3,2,5,1]`
- Output: `5`

**Example 3**

- Input: `basket1 = [8,4,5,3], basket2 = [3,2,5,1]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach** combined with **Frequency Counting**. First, we calculate the total frequency of each fruit across both baskets. If the total count of any fruit is odd, it is impossible to distribute them equally, so we return -1. We then identify the "excess" fruits in each basket (those that appear more than half the total count). We collect these excess fruits, sort them, and pair them up to minimize the swap cost. The cost of swapping two fruits is the minimum of the two, so we also consider swapping with the global minimum fruit available in either basket to potentially reduce costs.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of fruits in each basket, primarily due to sorting the excess fruits.
- **Space Complexity**: `O(N)` to store the frequency maps and the lists of excess fruits.
