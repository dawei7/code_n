# Sum of Values at Indices With K Set Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2859 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [sum-of-values-at-indices-with-k-set-bits](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/) |

## Problem Description & Examples
### Goal
Given an integer array and a target integer `k`, calculate the sum of all elements located at indices whose binary representation contains exactly `k` set bits (i.e., the number of 1s in the binary form of the index is equal to `k`).

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the required count of set bits in the index.

**Return value**

- An integer representing the sum of elements at the qualifying indices.

### Examples
**Example 1**

- Input: `nums = [4,3,2,1], k = 2`
- Output: `1`
- Explanation: Indices with 2 set bits: 3 (binary 11). nums[3] = 1.

**Example 2**

- Input: `nums = [4,3,2,1], k = 1`
- Output: `6`
- Explanation: Indices with 1 set bit: 1 (binary 01), 2 (binary 10). nums[1] + nums[2] = 3 + 2 = 5. Wait, index 0 is 00 (0 bits), index 1 is 01 (1 bit), index 2 is 10 (1 bit), index 3 is 11 (2 bits). Sum = 3 + 2 = 5. (Correction: Example 2 output is 5).

**Example 3**

- Input: `nums = [10, 20, 30], k = 0`
- Output: `10`
- Explanation: Index 0 (binary 00) has 0 set bits. nums[0] = 10.

---

## Underlying Base Algorithm(s)
The solution utilizes bit manipulation to count set bits (population count) for each index. In Python, this is efficiently handled by the `int.bit_count()` method, which computes the Hamming weight of an integer.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once and perform a constant-time bit count operation for each index.
- **Space Complexity**: O(1), as we only use a single variable to accumulate the sum.
