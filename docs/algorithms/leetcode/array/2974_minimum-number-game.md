# Minimum Number Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2974 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue), Simulation |
| Official Link | [minimum-number-game](https://leetcode.com/problems/minimum-number-game/) |

## Problem Description & Examples
### Goal
Given an array of integers with an even length, simulate a game where Alice and Bob repeatedly remove the two smallest elements from the array. In each round, Alice removes the smallest element, followed by Bob removing the next smallest. They then append these elements to a result array in the order [Bob's element, Alice's element]. The process continues until the original array is empty.

### Function Contract
**Inputs**

- `nums`: A list of integers where `len(nums)` is even and `2 <= len(nums) <= 100`.

**Return value**

- A list of integers representing the result array after all rounds are completed.

### Examples
**Example 1**

- Input: `nums = [5, 4, 2, 3]`
- Output: `[3, 2, 5, 4]`

**Example 2**

- Input: `nums = [2, 5]`
- Output: `[5, 2]`

**Example 3**

- Input: `nums = [10, 20, 30, 40, 50, 60]`
- Output: `[20, 10, 40, 30, 60, 50]`

---

## Underlying Base Algorithm(s)
The problem is solved by sorting the input array in non-decreasing order. Once sorted, the elements at index `i` and `i+1` represent the smallest and second-smallest elements of the remaining set, respectively. By iterating through the sorted array with a step of 2, we can swap the positions of these pairs to satisfy the game's requirement of appending Bob's element (the larger of the pair) before Alice's element (the smaller of the pair).

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the length of the input array, due to the sorting operation. The subsequent linear scan is `O(N)`.
- **Space Complexity**: `O(N)` to store the resulting array. Depending on the sorting implementation, the space complexity for the sort itself is `O(N)` or `O(log N)`.
