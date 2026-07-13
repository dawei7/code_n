# Smallest Integer Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1015 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-integer-divisible-by-k](https://leetcode.com/problems/smallest-integer-divisible-by-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-integer-divisible-by-k/).

### Goal
Find the length of the shortest positive integer made only of digit `1` that is divisible by `k`. Return `-1` when no such integer exists.

### Function Contract
**Inputs**

- `k`: Positive integer divisor.

**Return value**

Length of the smallest all-ones integer divisible by `k`, or `-1` if impossible.

### Examples
**Example 1**

- Input: `k = 1`
- Output: `1`

**Example 2**

- Input: `k = 2`
- Output: `-1`

**Example 3**

- Input: `k = 3`
- Output: `3`

---

## Solution
### Approach
An all-ones number can never be divisible by a number that has factor `2` or `5`, so those cases return `-1` immediately. For all other `k`, build the number only through its remainder:

`remainder = (remainder * 10 + 1) % k`

After each added digit, if the remainder becomes zero, the current length is the answer. At most `k` distinct remainders are possible, so a solution must appear within `k` steps when it exists.

### Complexity Analysis
- **Time Complexity**: `O(k)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
