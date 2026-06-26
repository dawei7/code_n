# Maximum Tastiness of Candy Basket

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2517 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sorting |
| Official Link | [maximum-tastiness-of-candy-basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/) |

## Problem Description & Examples
### Goal
Given an array of candy prices and an integer `k`, select `k` candies such that the minimum absolute difference between any two selected candies is maximized. This maximized minimum difference is defined as the "tastiness" of the basket.

### Function Contract
**Inputs**

- `price`: A list of integers representing the prices of available candies.
- `k`: An integer representing the number of candies to be selected.

**Return value**

- An integer representing the maximum possible tastiness of the basket.

### Examples
**Example 1**

- Input: `price = [13, 5, 1, 8, 21, 2], k = 3`
- Output: `8`
- Explanation: Selecting candies with prices [1, 8, 21] gives differences [7, 13, 20]. The minimum difference is 7. Selecting [1, 9, 17] isn't possible, but [1, 9, 21] gives min diff 8.

**Example 2**

- Input: `price = [1, 3, 1], k = 2`
- Output: `2`

**Example 3**

- Input: `price = [7, 7, 7, 7], k = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the tastiness value is monotonic (if a tastiness `x` is achievable, any value less than `x` is also achievable), we can binary search for the largest possible minimum difference. A **Greedy** approach is used within the check function to verify if a specific difference `d` is possible by picking candies sequentially.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + N log M)`, where `N` is the number of candies and `M` is the range of prices (max - min). Sorting takes `O(N log N)`, and the binary search performs `log M` iterations, each taking `O(N)` to verify.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.
