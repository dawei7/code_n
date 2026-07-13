# Count Pairs With XOR in a Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1803 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-pairs-with-xor-in-a-range](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/).

### Goal
Count index pairs whose XOR value lies between `low` and `high`, inclusive.

### Function Contract
**Inputs**

- `nums`: a list of non-negative integers.
- `low`: lower bound of the allowed XOR range.
- `high`: upper bound of the allowed XOR range.

**Return value**

Return the number of pairs `(i, j)` with `i < j` and `low <= nums[i] XOR nums[j] <= high`.

### Examples
**Example 1**

- Input: `nums = [1,4,2,7], low = 2, high = 6`
- Output: `6`

**Example 2**

- Input: `nums = [9,8,4,2,1], low = 5, high = 14`
- Output: `8`

**Example 3**

- Input: `nums = [0,1,2], low = 1, high = 2`
- Output: `2`

---

## Solution
### Approach
Count pairs with XOR at most `limit`, then subtract `count(high) - count(low - 1)`. For the at-most query, scan numbers while inserting previous numbers into a binary trie. At each bit, use the trie counts to count previous values that keep the XOR prefix within the limit.

### Complexity Analysis
- **Time Complexity**: `O(n * B)`, where `B` is the bit width
- **Space Complexity**: `O(n * B)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
