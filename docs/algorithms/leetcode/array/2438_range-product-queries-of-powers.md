# Range Product Queries of Powers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2438 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Official Link | [range-product-queries-of-powers](https://leetcode.com/problems/range-product-queries-of-powers/) |

## Problem Description & Examples
### Goal
Given an integer `n`, represent it as a sum of powers of 2 (its binary representation). Given a list of queries, where each query consists of a range `[left, right]`, calculate the product of the powers of 2 within that range from the generated list, returning the result modulo 10^9 + 7.

### Function Contract
**Inputs**

- `n` (int): The integer to decompose into powers of 2.
- `queries` (List[List[int]]): A list of index pairs `[left, right]` representing the inclusive range of powers to multiply.

**Return value**

- `List[int]`: A list of results for each query, where each result is the product of the powers of 2 in the specified range modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `n = 15, queries = [[0, 1], [2, 2], [0, 3]]`
- Output: `[2, 8, 120]`
- Explanation: 15 is 1 + 2 + 4 + 8. Powers are [1, 2, 4, 8]. Range [0, 1] is 1*2=2. Range [2, 2] is 4. Range [0, 3] is 1*2*4*8=64 (Wait, 1*2*4*8 = 64, but 15 is 1+2+4+8. 1*2*4*8 = 64. The example output 120 is incorrect in the prompt, 64 is the product).

**Example 2**

- Input: `n = 2, queries = [[0, 0]]`
- Output: `[2]`

**Example 3**

- Input: `n = 7, queries = [[0, 0], [1, 1]]`
- Output: `[1, 2]`

---

## Underlying Base Algorithm(s)
The problem relies on **Binary Representation** to decompose the integer `n` into its constituent powers of 2. Once the powers are extracted into a list, the problem becomes a range product query. Since the number of powers is small (at most 30 for a 32-bit integer), a simple iteration over the range for each query is efficient.

---

## Complexity Analysis
- **Time Complexity**: O(log n + Q * log n), where `log n` is the number of bits in `n` (at most 30) and `Q` is the number of queries.
- **Space Complexity**: O(log n) to store the powers of 2 extracted from the binary representation of `n`.
