# Maximize the Minimum Powered City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2528 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum |
| Official Link | [maximize-the-minimum-powered-city](https://leetcode.com/problems/maximize-the-minimum-powered-city/) |

## Problem Description & Examples
### Goal
Given an array representing the power stations in a city and a range `r`, each station provides power to all cities within distance `r`. The total power of a city is the sum of power from all stations within its range. You are allowed to add at most `k` new power stations anywhere in the city. The objective is to maximize the minimum power value across all cities after optimally placing the `k` stations.

### Function Contract
**Inputs**

- `stations`: A list of integers where `stations[i]` is the number of power stations at index `i`.
- `r`: An integer representing the range of each power station.
- `k`: An integer representing the maximum number of additional power stations you can add.

**Return value**

- An integer representing the maximum possible value of the minimum power among all cities.

### Examples
**Example 1**

- Input: `stations = [1,2,4,5,0], r = 1, k = 2`
- Output: `5`

**Example 2**

- Input: `stations = [4,4,4,4], r = 0, k = 3`
- Output: `4`

**Example 3**

- Input: `stations = [1,1,1,1], r = 1, k = 1`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer** combined with a **Greedy approach** and a **Sliding Window/Difference Array** technique. Since the minimum power is monotonic (if a value `x` is achievable, any value less than `x` is also achievable), we binary search for the maximum possible minimum power. For a fixed target power, we use a greedy strategy to add stations at the rightmost possible position to cover the leftmost city that currently falls below the target.

---

## Complexity Analysis
- **Time Complexity**: `O(n log(max_power + k))`, where `n` is the number of cities. The binary search runs in logarithmic time relative to the potential power range, and the check function runs in `O(n)` using a sliding window or difference array.
- **Space Complexity**: `O(n)` to store the current power levels of the cities.
