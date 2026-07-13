# Replace Non-Coprime Numbers in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2197 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [replace-non-coprime-numbers-in-array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/).

### Goal
Repeatedly replace adjacent numbers sharing a factor greater than one with their least common multiple until every adjacent pair is coprime. Return the final array; its result is independent of replacement order.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

The array after no adjacent non-coprime pair remains.

### Examples
**Example 1**

- Input: `nums = [6, 4, 3, 2, 7, 6, 2]`
- Output: `[12, 7, 6]`

**Example 2**

- Input: `nums = [2, 2, 1, 1, 3, 3, 3]`
- Output: `[2, 1, 1, 3]`

**Example 3**

- Input: `nums = [2, 3, 5]`
- Output: `[2, 3, 5]`

---

## Solution
### Approach
Use a stack for the settled prefix. Push each number, then while the top two values have gcd greater than one, pop both and push their lcm, computed as `a / gcd(a, b) * b`. Continue checking because the merged value may now share a factor with the preceding stack value.

### Complexity Analysis
- **Time Complexity**: `O(n log M)`, where `M` bounds values involved in gcd computations
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
