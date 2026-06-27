# Sorted GCD Pair Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3312 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum |
| Official Link | [sorted-gcd-pair-queries](https://leetcode.com/problems/sorted-gcd-pair-queries/) |

## Problem Description & Examples
### Goal
Given an array of integers, consider all possible pairs $(nums[i], nums[j])$ where $i < j$. Calculate the greatest common divisor (GCD) for every such pair. The objective is to return the GCD values corresponding to a list of provided indices, assuming all generated GCDs are sorted in non-decreasing order.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `queries`: A list of long integers representing the 0-indexed positions in the sorted list of all pair GCDs.

**Return value**

- A list of integers where each element is the GCD value at the specified query index.

### Examples
**Example 1**

- Input: `nums = [2, 3, 4]`, `queries = [0, 2, 2]`
- Output: `[1, 2, 2]`
- Explanation: Pairs are (2,3) gcd=1, (2,4) gcd=2, (3,4) gcd=1. Sorted GCDs: [1, 1, 2]. Queries [0, 2, 2] map to [1, 2, 2].

**Example 2**

- Input: `nums = [4, 4, 2, 1]`, `queries = [5, 3, 1, 0]`
- Output: `[4, 4, 1, 1]`

**Example 3**

- Input: `nums = [2, 2]`, `queries = [0]`
- Output: `[2]`

---

## Underlying Base Algorithm(s)
The solution utilizes the Principle of Inclusion-Exclusion (PIE) to count the frequency of each possible GCD value. By counting how many numbers in the input are multiples of $g$, we can determine how many pairs have a GCD that is a multiple of $g$. Using PIE, we isolate the exact count of pairs whose GCD is exactly $g$. Finally, we use prefix sums to build a cumulative distribution of GCD frequencies, allowing us to answer each query in logarithmic time using binary search.

---

## Complexity Analysis
- **Time Complexity**: $O(M \log M + N + Q \log M)$, where $M$ is the maximum value in `nums`, $N$ is the length of `nums`, and $Q$ is the number of queries. The $M \log M$ term arises from the harmonic series summation used to count multiples.
- **Space Complexity**: $O(M)$ to store the frequency counts and the prefix sum array of GCD occurrences.
