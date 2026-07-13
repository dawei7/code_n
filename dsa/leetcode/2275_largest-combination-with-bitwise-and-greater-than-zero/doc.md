# Largest Combination With Bitwise AND Greater Than Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-combination-with-bitwise-and-greater-than-zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/).

### Goal
Choose the largest subset of positive integers whose bitwise AND is greater than zero.

### Function Contract
**Inputs**

- `candidates`: positive integers.

**Return value**

The maximum possible subset size.

### Examples
**Example 1**

- Input: `candidates = [16, 17, 71, 62, 12, 24, 14]`
- Output: `4`

**Example 2**

- Input: `candidates = [8, 8]`
- Output: `2`

**Example 3**

- Input: `candidates = [1, 2, 4]`
- Output: `1`

---

## Solution
### Approach
A subset has positive AND exactly when all its values share at least one set bit. Count, for every bit position, how many candidates contain that bit. The largest count is achievable by selecting all values with that common bit and is optimal.

### Complexity Analysis
- **Time Complexity**: `O(nB)`, where `B` is the number of relevant bit positions
- **Space Complexity**: `O(B)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
