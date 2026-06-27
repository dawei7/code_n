# Find the K-or of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2917 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [find-the-k-or-of-an-array](https://leetcode.com/problems/find-the-k-or-of-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, calculate a new integer (the "K-or") where the $i$-th bit is set to 1 if and only if at least `k` elements in the input array have their $i$-th bit set to 1. Otherwise, the $i$-th bit of the result is 0.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: An integer representing the threshold count for bit activation.

**Return value**

- An integer representing the calculated K-or value.

### Examples
**Example 1**

- Input: `nums = [7, 12, 9, 8, 9, 15], k = 4`
- Output: `9`

**Example 2**

- Input: `nums = [1, 2, 3], k = 1`
- Output: `3`

**Example 3**

- Input: `nums = [10, 8, 5, 9, 11, 6, 8], k = 1`
- Output: `15`

---

## Underlying Base Algorithm(s)
The problem utilizes bitwise manipulation and frequency counting. Since the input integers are typically within a 32-bit range, we can iterate through each bit position (0 to 31). For each position, we count how many numbers in the array have that specific bit set. If the count meets or exceeds `k`, we set the corresponding bit in our result using the bitwise OR operator.

---

## Complexity Analysis
- **Time Complexity**: $O(n \cdot \log(\max(nums)))$, where $n$ is the length of the array. Given the constraints (usually 32 bits), this simplifies to $O(n)$.
- **Space Complexity**: $O(1)$, as we only use a constant amount of extra space regardless of the input size.
