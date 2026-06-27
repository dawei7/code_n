# Maximum and Minimum Sums of at Most Size K Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3428 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Sorting, Combinatorics |
| Official Link | [maximum-and-minimum-sums-of-at-most-size-k-subsequences](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the sum of the minimum element and the maximum element for every possible non-empty subsequence of size at most $k$. Since the result can be very large, return the total sum modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the maximum allowed size of a subsequence.

**Return value**

- An integer representing the sum of all minimums and maximums of all valid subsequences, modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `14`
- Explanation: Subsequences: [1], [2], [3], [1,2], [1,3], [2,3]. Min sums: 1+2+3+1+1+2 = 10. Max sums: 1+2+3+2+3+3 = 14. Total = 24. (Wait, example logic: Min: 1+2+3+1+1+2=10, Max: 1+2+3+2+3+3=14. Sum = 24).

**Example 2**

- Input: `nums = [5, 0, 6], k = 1`
- Output: `22`

**Example 3**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `10`

---

## Underlying Base Algorithm(s)
The problem relies on sorting the array to easily identify the rank of each element. For a sorted array, an element at index $i$ acts as the minimum for all subsequences where it is the smallest element (i.e., it is chosen, and other elements are chosen from the $n-1-i$ elements to its right) and as the maximum where it is the largest (chosen with elements from the $i$ elements to its left). We use combinatorial combinations $\binom{n}{r}$ to count how many subsequences of size $1$ to $k$ include a specific element as the min/max.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to sorting, where $n$ is the length of the array. The combinatorial summation takes $O(n)$ time.
- **Space Complexity**: $O(n)$ to store precomputed factorials and inverse factorials for combinations.
