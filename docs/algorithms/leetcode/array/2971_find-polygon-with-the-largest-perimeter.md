# Find Polygon With the Largest Perimeter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2971 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Official Link | [find-polygon-with-the-largest-perimeter](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/) |

## Problem Description & Examples
### Goal
Given an array of positive integers representing side lengths, determine the maximum possible perimeter of a polygon that can be formed using a subset of these lengths. A polygon with $k$ sides ($k \ge 3$) can be formed if and only if the length of the longest side is strictly less than the sum of the lengths of all other sides.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available side lengths.

**Return value**

- An integer representing the maximum perimeter possible. If no polygon can be formed, return -1.

### Examples
**Example 1**

- Input: `nums = [5, 5, 5]`
- Output: `15`

**Example 2**

- Input: `nums = [1, 12, 1, 2, 5, 50, 3]`
- Output: `12`

**Example 3**

- Input: `nums = [5, 5, 50]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem relies on a **Greedy** approach combined with **Sorting** and **Prefix Sums**. By sorting the array in non-decreasing order, we can iterate through the elements and maintain a running sum of all elements encountered so far. For any element at index `i`, the sum of all elements from index `0` to `i-1` represents the potential sum of the "other sides." If this sum is strictly greater than `nums[i]`, then `nums[i]` can serve as the longest side of a valid polygon.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the sorting step, where $n$ is the number of elements in the input array. The subsequent linear scan takes $O(n)$.
- **Space Complexity**: $O(1)$ or $O(n)$ depending on the sorting implementation's space requirements (Python's Timsort uses $O(n)$ in the worst case).
