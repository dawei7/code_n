# Find the Peaks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2951 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [find-the-peaks](https://leetcode.com/problems/find-the-peaks/) |

## Problem Description & Examples
### Goal
Identify all indices in a given integer array that represent "peaks." A peak is defined as an element that is strictly greater than its immediate neighbors. Note that the first and last elements of the array cannot be peaks because they lack two neighbors.

### Function Contract
**Inputs**

- `mountain`: A list of integers (`List[int]`) representing the elevation profile.

**Return value**

- A list of integers (`List[int]`) containing the indices of all identified peaks in increasing order.

### Examples
**Example 1**

- Input: `mountain = [2, 4, 4]`
- Output: `[]`

**Example 2**

- Input: `mountain = [1, 4, 3, 8, 5]`
- Output: `[1, 3]`

**Example 3**

- Input: `mountain = [1, 2, 3, 4, 5]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The problem utilizes a **Linear Scan (Enumeration)** approach. By iterating through the array from index `1` to `n-2` (where `n` is the length of the array), we perform a constant-time comparison for each element against its left and right neighbors to determine if it satisfies the peak condition.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input array, as we perform a single pass through the list.
- **Space Complexity**: `O(k)`, where `k` is the number of peaks found, required to store the resulting indices. In the worst case, this is `O(n)`.
