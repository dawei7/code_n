# Most Frequent Even Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2404 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [most-frequent-even-element](https://leetcode.com/problems/most-frequent-even-element/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the even number that appears most frequently. If multiple even numbers share the same maximum frequency, return the smallest one among them. If no even numbers exist in the input array, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the most frequent even element, or -1 if none exist.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 2, 4, 4, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [4, 4, 4, 9, 2, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [29, 47, 21, 41, 13, 37, 25, 7]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Frequency Map (Hash Table). We iterate through the array once to count the occurrences of all even numbers. We then iterate through the map to find the key with the highest frequency, applying a tie-breaking rule (choosing the smaller key) when frequencies are equal.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the input array, as we perform a single pass to count elements and a single pass over the unique even elements.
- **Space Complexity**: `O(K)`, where `K` is the number of unique even elements in the array, used to store the frequency map.
