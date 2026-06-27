# Check if Bitwise OR Has Trailing Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2980 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [check-if-bitwise-or-has-trailing-zeros](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/) |

## Problem Description & Examples
### Goal
Determine if it is possible to select at least two elements from a given array of positive integers such that their bitwise OR operation results in a number with at least one trailing zero in its binary representation.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- `bool`: Returns `True` if there exist two distinct indices `i` and `j` such that `(nums[i] | nums[j])` ends in a zero bit, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `True`
- Explanation: `2 | 4 = 6` (binary `110`), which has a trailing zero.

**Example 2**

- Input: `nums = [1, 3, 5, 7]`
- Output: `False`
- Explanation: Any pair ORed together will result in an odd number (no trailing zero).

**Example 3**

- Input: `nums = [2, 4, 8, 16]`
- Output: `True`
- Explanation: `2 | 4 = 6` (binary `110`), which has a trailing zero.

---

## Underlying Base Algorithm(s)
The problem relies on the property that a number has a trailing zero if and only if it is even (i.e., its least significant bit is 0). The bitwise OR of two numbers `a` and `b` will have a trailing zero if both `a` and `b` are even. Therefore, the problem simplifies to checking if the input array contains at least two even numbers.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we only need to iterate through the list once to count the even numbers.
- **Space Complexity**: `O(1)`, as we only use a single counter variable regardless of the input size.
