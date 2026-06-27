# Maximum Element-Sum of a Complete Subset of Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2862 |
| Difficulty | Hard |
| Topics | Array, Math, Number Theory |
| Official Link | [maximum-element-sum-of-a-complete-subset-of-indices](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify a "complete subset" of indices. A subset of indices is complete if, for any two indices in the subset, their product is a perfect square. The objective is to find the maximum possible sum of elements located at the indices forming such a subset.

### Function Contract
**Inputs**

- `nums`: A list of integers (1-indexed for the purpose of the problem, where `nums[i]` corresponds to index `i+1`).

**Return value**

- An integer representing the maximum sum of elements whose indices form a complete subset.

### Examples
**Example 1**

- Input: `nums = [8, 7, 3, 5, 7, 2, 4, 9]`
- Output: `16`
- Explanation: The indices {1, 4} form a complete subset because 1 * 4 = 4 (a perfect square). The sum is nums[0] + nums[3] = 8 + 5 = 13. However, the subset {8} gives 9, and {7} gives 7. The maximum sum is 16 (from index 7, where 7 is a perfect square itself).

**Example 2**

- Input: `nums = [5, 10, 3, 10, 1, 13, 7, 9, 4]`
- Output: `22`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- Output: `19`

---

## Underlying Base Algorithm(s)
The core insight is that two numbers $i$ and $j$ have a product $i \times j$ that is a perfect square if and only if their "square-free parts" are identical. The square-free part of an integer $n$ is obtained by dividing $n$ by the largest perfect square that divides it. We can group all indices $i \in [1, n]$ by their square-free part and sum the values of `nums` for each group.

---

## Complexity Analysis
- **Time Complexity**: $O(N \sqrt{N})$, where $N$ is the length of the array. We iterate through each index and compute its square-free part by checking divisors up to $\sqrt{N}$.
- **Space Complexity**: $O(N)$ to store the sums associated with each unique square-free part.
