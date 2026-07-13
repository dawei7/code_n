# Divisor Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1025 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [divisor-game](https://leetcode.com/problems/divisor-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/divisor-game/).

### Goal
Two players take turns choosing a positive divisor `x` of the current number `n`, where `x < n`, and replacing `n` with `n - x`. The player who cannot move loses. Determine whether the first player wins with optimal play.

### Function Contract
**Inputs**

- `n`: Starting positive integer.

**Return value**

Boolean indicating whether the first player can force a win.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `true`

**Example 2**

- Input: `n = 3`
- Output: `false`

**Example 3**

- Input: `n = 4`
- Output: `true`

---

## Solution
### Approach
The winning pattern is parity. If `n` is even, the first player can choose `x = 1`, leaving an odd number. From any odd number, every valid divisor is odd, so the next state is even. Therefore the first player can keep handing the opponent odd numbers until the opponent reaches `1` and loses.

If `n` is odd, every move leaves an even number, giving the opponent the winning parity.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
