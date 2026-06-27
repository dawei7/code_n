# Maximum XOR Score Subarray Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3277 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-xor-score-subarray-queries](https://leetcode.com/problems/maximum-xor-score-subarray-queries/) |

## Problem Description & Examples
### Goal
Given an array of integers, define the "XOR score" of a subarray as the result of recursively applying the XOR operation to adjacent elements until a single value remains. Specifically, for a subarray of length $k$, the score is the result of the $(k-1)$-th iteration of XORing adjacent elements. You must answer multiple queries, each specifying a range $[l, r]$, by returning the maximum XOR score possible for any subarray contained entirely within that range.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the source array.
- `queries`: A list of pairs $[l, r]$, where each pair defines the inclusive bounds of a subarray query.

**Return value**

- A list of integers where each element corresponds to the maximum XOR score found in the specified query range.

### Examples
**Example 1**

- Input: `nums = [2, 8, 4, 32, 16, 13], queries = [[0, 2], [1, 4], [0, 5]]`
- Output: `[12, 60, 60]`

**Example 2**

- Input: `nums = [0, 7, 8, 5, 6, 5, 1, 6, 10], queries = [[0, 7], [1, 5], [2, 4], [0, 8]]`
- Output: `[7, 14, 14, 14]`

**Example 3**

- Input: `nums = [1, 2, 3], queries = [[0, 2]]`
- Output: `[2]`

---

## Underlying Base Algorithm(s)
The problem is solved using 2D Dynamic Programming. First, we precompute the XOR score for every possible subarray $[i, j]$ using the relation: `score(i, j) = score(i, j-1) ^ score(i+1, j)`. After filling this table, we compute a second DP table where `max_score[i][j]` stores the maximum XOR score of any subarray within the range $[i, j]$. This is derived from `max_score[i][j] = max(score(i, j), max_score[i+1][j], max_score[i][j-1])`.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2 + q)$, where $n$ is the length of the array and $q$ is the number of queries. The DP table construction takes $O(n^2)$ and each query is answered in $O(1)$.
- **Space Complexity**: $O(n^2)$ to store the precomputed XOR scores and the maximum range scores.
