# Minimize the Maximum Adjacent Element Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3357 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy |
| Official Link | [minimize-the-maximum-adjacent-element-difference](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/) |

## Problem Description & Examples
### Goal
Given an array containing integers and placeholders (represented by -1), replace every -1 with a positive integer such that the maximum absolute difference between any two adjacent elements in the resulting array is minimized.

### Function Contract
**Inputs**

- `nums`: A list of integers where -1 represents a value that must be replaced.

**Return value**

- An integer representing the minimum possible value for the maximum adjacent difference.

### Examples
**Example 1**

- Input: `nums = [1, 2, -1, 10, 8]`
- Output: `4`
- Explanation: Replacing -1 with 6 results in `[1, 2, 6, 10, 8]`. Differences are `|1-2|=1, |2-6|=4, |6-10|=4, |10-8|=2`. Max is 4.

**Example 2**

- Input: `nums = [-1, -1]`
- Output: `0`
- Explanation: Replacing both with the same value (e.g., 1) results in `[1, 1]`. Max difference is 0.

**Example 3**

- Input: `nums = [10, -1, 3, -1, 10]`
- Output: `4`
- Explanation: Replacing with 7 and 7 results in `[10, 7, 3, 7, 10]`. Max difference is 4.

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the maximum difference is monotonic (if a difference $X$ is achievable, any $Y > X$ is also achievable), we search for the smallest $X$ in the range $[0, 10^9]$. For a fixed $X$, we use a **Greedy** approach to validate if it is possible to fill the -1s such that no adjacent difference exceeds $X$.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log M)$, where $N$ is the length of the array and $M$ is the maximum possible value in the array ($10^9$). The binary search takes $\log M$ steps, and each check takes $O(N)$.
- **Space Complexity**: $O(N)$ to store the processed array or auxiliary structures during the validation check.
