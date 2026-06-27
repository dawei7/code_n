# Maximize Score of Numbers in Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3281 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sorting |
| Official Link | [maximize-score-of-numbers-in-ranges](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/) |

## Problem Description & Examples
### Goal
Given a sorted array of intervals `start` and an integer `d`, select one integer $x_i$ from each interval $[start[i], start[i] + d]$ such that the minimum absolute difference between any two selected integers $|x_i - x_j|$ is maximized.

### Function Contract
**Inputs**

- `start`: A list of integers representing the starting points of intervals.
- `d`: An integer representing the length of each interval.

**Return value**

- An integer representing the maximum possible minimum difference between any two chosen numbers.

### Examples
**Example 1**

- Input: `start = [6, 0, 3], d = 2`
- Output: `4`
- Explanation: We can pick 0, 4, and 8. The differences are |4-0|=4, |8-4|=4, |8-0|=8. The minimum is 4.

**Example 2**

- Input: `start = [2, 6, 13, 13], d = 5`
- Output: `5`
- Explanation: We can pick 2, 7, 12, 17. The minimum difference is 5.

**Example 3**

- Input: `start = [1, 10], d = 1`
- Output: `9`
- Explanation: We can pick 1 and 10. The difference is 9.

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the minimum difference is monotonic (if a difference $k$ is achievable, any difference $k' < k$ is also achievable), we can binary search for the largest possible value of $k$. The feasibility check is performed greedily: for a target difference $k$, we pick the smallest possible value for the first interval, then for each subsequent interval, we pick the smallest value that is at least $k$ greater than the previously chosen value.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log(M))$, where $n$ is the length of the `start` array and $M$ is the range of possible differences (max value of `start` + `d`). Sorting takes $O(n \log n)$, and the binary search performs $O(\log M)$ checks, each taking $O(n)$.
- **Space Complexity**: $O(1)$ (excluding the space required for sorting).
