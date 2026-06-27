# Minimum Division Operations to Make Array Non Decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3326 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Number Theory |
| Official Link | [minimum-division-operations-to-make-array-non-decreasing](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/) |

## Problem Description & Examples
### Goal
Given an array of integers, you are allowed to replace any element with its smallest proper divisor (a divisor other than the number itself). The objective is to determine the minimum number of operations required to transform the array into a non-decreasing sequence. If it is impossible to achieve this state, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where $1 \le nums[i] \le 10^6$.

**Return value**

- An integer representing the minimum operations, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [25, 7]`
- Output: `1`
- Explanation: Replace 25 with 5 (its smallest proper divisor). The array becomes [5, 7], which is non-decreasing.

**Example 2**

- Input: `nums = [7, 7, 6]`
- Output: `-1`
- Explanation: 6 cannot be reduced to a value $\le 7$ that maintains the non-decreasing property.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `0`
- Explanation: The array is already non-decreasing.

---

## Underlying Base Algorithm(s)
The problem relies on **Number Theory** (specifically precomputing the smallest prime factor using a **Sieve of Eratosthenes**) and a **Greedy** strategy. Since we want to make the array non-decreasing with minimum operations, we process the array from right to left. For each element, if it is greater than the element to its right, we replace it with its smallest proper divisor. If the resulting value is still greater than the right neighbor, it is impossible to satisfy the condition.

---

## Complexity Analysis
- **Time Complexity**: $O(N + M \log \log M)$, where $N$ is the length of the array and $M$ is the maximum value in the array ($10^6$). The sieve takes $O(M \log \log M)$ and the array traversal takes $O(N)$.
- **Space Complexity**: $O(M)$ to store the smallest prime factors for all numbers up to $10^6$.
