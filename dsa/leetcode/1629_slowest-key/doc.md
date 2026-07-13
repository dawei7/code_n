# Slowest Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1629 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [slowest-key](https://leetcode.com/problems/slowest-key/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/slowest-key/).

### Goal
Given release times for typed keys, find the key with the longest press
duration. If multiple keys tie, return the lexicographically largest key.

### Function Contract
**Inputs**

- `releaseTimes`: cumulative release times for each key press.
- `keysPressed`: the string of keys pressed in order.

**Return value**

The slowest key character.

### Examples
**Example 1**

- Input: `releaseTimes = [9, 29, 49, 50], keysPressed = "cbcd"`
- Output: `"c"`

**Example 2**

- Input: `releaseTimes = [12, 23, 36, 46, 62], keysPressed = "spuda"`
- Output: `"a"`

**Example 3**

- Input: `releaseTimes = [1, 3, 5], keysPressed = "abc"`
- Output: `"c"`

---

## Solution
### Approach
Compute each press duration as `releaseTimes[i] - releaseTimes[i - 1]`, with
the first duration equal to `releaseTimes[0]`. Track the largest duration seen;
when a duration ties the current best, keep the larger character.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
