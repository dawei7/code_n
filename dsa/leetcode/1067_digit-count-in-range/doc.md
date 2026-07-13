# Digit Count in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1067 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [digit-count-in-range](https://leetcode.com/problems/digit-count-in-range/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/digit-count-in-range/).

### Goal
Count how many times digit `d` appears in the decimal representations of all integers from `low` through `high`, inclusive.

### Function Contract
**Inputs**

- `d`: Digit from `0` to `9`.
- `low`: Lower bound.
- `high`: Upper bound.

**Return value**

Total number of occurrences of digit `d` in the inclusive range.

### Examples
**Example 1**

- Input: `d = 1, low = 1, high = 13`
- Output: `6`

**Example 2**

- Input: `d = 0, low = 1, high = 10`
- Output: `1`

**Example 3**

- Input: `d = 5, low = 50, high = 55`
- Output: `7`

---

## Solution
### Approach
Compute a helper `count_up_to(n, d)` that counts occurrences of digit `d` from `1` to `n`, then return `count_up_to(high, d) - count_up_to(low - 1, d)`.

The helper can inspect each decimal position independently. For a position with factor `10^k`, split `n` into higher, current, and lower parts to determine how many full cycles contribute digit `d` at that position. Digit `0` needs special handling to avoid counting leading zeros.

### Complexity Analysis
- **Time Complexity**: `O(log high)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
