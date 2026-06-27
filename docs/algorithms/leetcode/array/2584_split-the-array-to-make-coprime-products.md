# Split the Array to Make Coprime Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2584 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Number Theory |
| Official Link | [split-the-array-to-make-coprime-products](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) |

## Problem Description & Examples
### Goal
Determine if an array can be partitioned into two non-empty contiguous subarrays such that the product of all elements in the left subarray and the product of all elements in the right subarray share no common prime factors (i.e., their greatest common divisor is 1).

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le nums[i] \le 10^6$.

**Return value**

- An integer representing the index $i$ such that the prefix `nums[0...i]` and suffix `nums[i+1...n-1]` are coprime, or `-1` if no such split exists.

### Examples
**Example 1**

- Input: `nums = [4,7,8,15,3,5]`
- Output: `2`
- Explanation: Left product is $4 \times 7 \times 8 = 224$. Right product is $15 \times 3 \times 5 = 225$. $\gcd(224, 225) = 1$.

**Example 2**

- Input: `nums = [4,7,15,8,3,5]`
- Output: `-1`

**Example 3**

- Input: `nums = [2,3,3]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The solution relies on **Prime Factorization** and **Interval Tracking**. Since the products can be extremely large, we avoid computing them directly. Instead, we track the "first" and "last" occurrence of every prime factor present in the array. A split is valid at index $i$ if no prime factor present in the prefix `nums[0...i]` appears in the suffix `nums[i+1...n-1]`. This is equivalent to checking if the maximum "last occurrence" index of all prime factors in the prefix is less than or equal to $i$.

---

## Complexity Analysis
- **Time Complexity**: $O(N \sqrt{M})$, where $N$ is the length of the array and $M$ is the maximum value in the array (due to prime factorization). This can be optimized to $O(N \log \log M)$ using a precomputed sieve.
- **Space Complexity**: $O(P)$, where $P$ is the number of distinct prime factors across all elements in the array.
