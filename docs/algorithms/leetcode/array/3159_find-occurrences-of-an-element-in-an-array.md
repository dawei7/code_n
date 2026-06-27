# Find Occurrences of an Element in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3159 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [find-occurrences-of-an-element-in-an-array](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/) |

## Problem Description & Examples
### Goal
Given an integer array `nums`, a target integer `x`, and an array of queries `queries`, determine the original index of the $k$-th occurrence of `x` in `nums` for each query $k$. If the $k$-th occurrence does not exist, return -1 for that query.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the source array.
- `x`: An integer representing the target element to search for.
- `queries`: A list of integers where each element represents the $k$-th occurrence to locate.

**Return value**

- A list of integers containing the indices corresponding to each query, or -1 if the occurrence is out of bounds.

### Examples
**Example 1**

- Input: `nums = [1, 3, 1, 7], x = 1, queries = [1, 3, 2]`
- Output: `[0, -1, 2]`

**Example 2**

- Input: `nums = [1, 2, 3], x = 10, queries = [1]`
- Output: `[-1]`

**Example 3**

- Input: `nums = [1, 2, 1, 2, 1, 2], x = 1, queries = [1, 2, 3]`
- Output: `[0, 2, 4]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Precomputation/Indexing** strategy. We first perform a single linear scan of the array to store the indices of all occurrences of `x` in a list. Once this mapping is established, each query can be answered in $O(1)$ time by accessing the precomputed list using the query value as an index.

---

## Complexity Analysis
- **Time Complexity**: $O(N + Q)$, where $N$ is the length of `nums` and $Q$ is the number of queries. We traverse the array once to build the index list and then iterate through the queries.
- **Space Complexity**: $O(N)$ in the worst case, as we store the indices of all occurrences of `x` in a separate list.
