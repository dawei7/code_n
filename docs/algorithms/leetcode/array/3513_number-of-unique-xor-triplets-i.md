# Number of Unique XOR Triplets I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3513 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [number-of-unique-xor-triplets-i](https://leetcode.com/problems/number-of-unique-xor-triplets-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the number of triplets (i, j, k) such that 0 <= i < j <= k < n, where the XOR sum of the elements in the range [i, j-1] is equal to the XOR sum of the elements in the range [j, k].

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 1000.

**Return value**

- An integer representing the total count of valid triplets (i, j, k) satisfying the XOR condition.

### Examples
**Example 1**

- Input: `nums = [0, 2, 2]`
- Output: `2`
- Explanation: Valid triplets are (0, 1, 2) and (0, 2, 2).

**Example 2**

- Input: `nums = [1, 2, 3]`
- Output: `1`
- Explanation: Valid triplet is (0, 1, 2).

**Example 3**

- Input: `nums = [4, 3, 2, 1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Prefix XOR sums. By precomputing the prefix XOR array, the XOR sum of any subarray [a, b] can be calculated in O(1) time as `prefix[b+1] ^ prefix[a]`. The condition `XOR(i, j-1) == XOR(j, k)` simplifies to `prefix[j] ^ prefix[i] == prefix[k+1] ^ prefix[j]`, which is equivalent to `prefix[i] == prefix[k+1]`.

---

## Complexity Analysis
- **Time Complexity**: O(n^2), where n is the length of the array. We iterate through all possible pairs of (i, k) and check the condition.
- **Space Complexity**: O(n) to store the prefix XOR array.
