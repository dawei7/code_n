# Make Lexicographically Smallest Array by Swapping Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2948 |
| Difficulty | Medium |
| Topics | Array, Union-Find, Sorting |
| Official Link | [make-lexicographically-smallest-array-by-swapping-elements](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) |

## Problem Description & Examples
### Goal
Given an array of integers and a threshold value, you are permitted to swap any two elements if their absolute difference is less than or equal to the threshold. The objective is to rearrange the array to achieve the lexicographically smallest possible sequence by performing any number of these valid swaps.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `limit`: An integer representing the maximum allowed absolute difference between two elements for a swap to be valid.

**Return value**

- A list of integers representing the lexicographically smallest array achievable.

### Examples
**Example 1**

- Input: `nums = [1, 5, 3, 9, 8], limit = 2`
- Output: `[1, 3, 5, 8, 9]`

**Example 2**

- Input: `nums = [1, 7, 6, 18, 2, 1], limit = 3`
- Output: `[1, 1, 6, 7, 18, 2]`

**Example 3**

- Input: `nums = [1, 7, 28, 19, 10], limit = 3`
- Output: `[1, 7, 28, 19, 10]`

---

## Underlying Base Algorithm(s)
The problem can be modeled as finding connected components in a graph where an edge exists between two indices if the values at those indices can be swapped. Since transitivity applies (if $a$ can swap with $b$, and $b$ with $c$, then $a$ can effectively move to $c$'s position), we can group elements into "swappable sets." By sorting the array and identifying contiguous segments where the difference between adjacent sorted elements is $\le$ `limit`, we can partition the indices into groups. Within each group, the values can be rearranged in any order, so we sort the values and place them back into the sorted indices of that group.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of the array. This is dominated by the initial sorting of the elements.
- **Space Complexity**: $O(N)$ to store the sorted array, the groups, and the resulting output array.
