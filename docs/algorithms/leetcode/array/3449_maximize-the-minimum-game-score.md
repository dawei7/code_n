# Maximize the Minimum Game Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3449 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy |
| Official Link | [maximize-the-minimum-game-score](https://leetcode.com/problems/maximize-the-minimum-game-score/) |

## Problem Description & Examples
### Goal
Given an array of points representing the score gained by visiting each index and a maximum number of moves allowed, determine the maximum possible value for the minimum score among all indices after distributing the moves. You can move to an adjacent index or stay at the current index, and each visit adds the index's point value to its total score.

### Function Contract
**Inputs**

- `points`: A list of integers representing the score awarded for visiting each index.
- `m`: An integer representing the total number of moves available.

**Return value**

- An integer representing the maximum possible value of the minimum score across all indices.

### Examples
**Example 1**

- Input: `points = [2, 6], m = 6`
- Output: `6`

**Example 2**

- Input: `points = [1, 2, 3], m = 5`
- Output: `2`

**Example 3**

- Input: `points = [10, 20], m = 1`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the minimum score is monotonic (if a minimum score $X$ is achievable, any value less than $X$ is also achievable), we search for the largest $X$ in the range $[0, \text{total\_points} \times m]$. For a fixed target $X$, we use a **Greedy approach** to check if it is possible to achieve at least $X$ at every index using at most $m$ moves.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log(\text{max\_score}))$, where $n$ is the length of the `points` array and $\text{max\_score}$ is the upper bound of the binary search.
- **Space Complexity**: $O(n)$ to store the number of visits required for each index during the greedy check.
