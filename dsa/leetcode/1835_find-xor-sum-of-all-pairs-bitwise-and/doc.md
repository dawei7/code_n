# Find XOR Sum of All Pairs Bitwise AND

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1835 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-xor-sum-of-all-pairs-bitwise-and](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/).

### Goal
Compute the XOR of `(a & b)` for every pair where `a` comes from `arr1` and `b` comes from `arr2`.

### Function Contract
**Inputs**

- `arr1`: the first integer array.
- `arr2`: the second integer array.

**Return value**

Return the XOR sum of all pairwise bitwise AND values.

### Examples
**Example 1**

- Input: `arr1 = [1,2,3], arr2 = [6,5]`
- Output: `0`

**Example 2**

- Input: `arr1 = [12], arr2 = [4]`
- Output: `4`

**Example 3**

- Input: `arr1 = [5,1], arr2 = [3,7]`
- Output: `4`

---

## Solution
### Approach
Use bitwise distributivity over XOR: `(a1 & b) XOR (a2 & b) == (a1 XOR a2) & b`. Therefore the XOR of all pairwise ANDs equals `(xor of arr1) & (xor of arr2)`.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
