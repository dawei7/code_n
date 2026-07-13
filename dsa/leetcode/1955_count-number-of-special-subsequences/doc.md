# Count Number of Special Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1955 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-special-subsequences](https://leetcode.com/problems/count-number-of-special-subsequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-special-subsequences/).

### Goal
Count subsequences that consist of one or more `0`s, followed by one or more `1`s, followed by one or more `2`s.

### Function Contract
**Inputs**

- `nums`: an array containing only `0`, `1`, and `2`.

**Return value**

Return the count modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [0,1,2,2]`
- Output: `3`

**Example 2**

- Input: `nums = [2,2,0,0]`
- Output: `0`

**Example 3**

- Input: `nums = [0,1,2,0,1,2]`
- Output: `7`

---

## Solution
### Approach
Track counts for valid subsequences ending in the `0` phase, `1` phase, and `2` phase. A new `0` doubles existing zero-only subsequences and can start a new one; a `1` doubles one-phase subsequences and can extend zero-only ones; a `2` doubles completed subsequences and can extend one-phase ones.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
