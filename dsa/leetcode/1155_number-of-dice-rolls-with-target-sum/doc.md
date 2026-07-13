# Number of Dice Rolls With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-dice-rolls-with-target-sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/).

### Goal
Count how many ways `n` identical dice with faces `1` through `k` can be rolled so their sum is exactly `target`. Return the count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `n`: Number of dice.
- `k`: Number of faces on each die.
- `target`: Desired total sum.

**Return value**

Number of valid roll sequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `n = 1`, `k = 6`, `target = 3`
- Output: `1`

**Example 2**

- Input: `n = 2`, `k = 6`, `target = 7`
- Output: `6`

**Example 3**

- Input: `n = 30`, `k = 30`, `target = 500`
- Output: `222616187`

---

## Solution
### Approach
Use dynamic programming by dice count and current sum. Let `dp[s]` be the number of ways to reach sum `s` after the processed dice.

For each new die, `next[s]` is the sum of the previous states `dp[s - 1]` through `dp[s - k]`. Maintain that range with a sliding prefix window so each target sum is updated in constant time.

### Complexity Analysis
- **Time Complexity**: `O(n * target)`.
- **Space Complexity**: `O(target)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
