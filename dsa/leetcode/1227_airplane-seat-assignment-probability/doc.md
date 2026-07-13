# Airplane Seat Assignment Probability

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1227 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Brainteaser, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [airplane-seat-assignment-probability](https://leetcode.com/problems/airplane-seat-assignment-probability/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/airplane-seat-assignment-probability/).

### Goal
Compute the probability that the `n`th passenger sits in their own seat when the first passenger chooses a random seat and every later passenger takes their own seat if available, otherwise a random remaining seat.

### Function Contract
**Inputs**

- `n: int` - Number of passengers and seats.

**Return value**

`float` - Probability that the last passenger gets seat `n`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1.0`

**Example 2**

- Input: `n = 2`
- Output: `0.5`

**Example 3**

- Input: `n = 3`
- Output: `0.5`

---

## Solution
### Approach
For `n = 1`, the first passenger is also the last passenger and must sit in their own seat. For any `n > 1`, the process eventually reaches a moment where either seat `1` or seat `n` is chosen; by symmetry both outcomes are equally likely. If seat `1` is chosen, the last passenger gets their own seat; if seat `n` is chosen, they do not.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
