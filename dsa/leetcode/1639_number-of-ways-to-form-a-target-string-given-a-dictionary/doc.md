# Number of Ways to Form a Target String Given a Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1639 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-to-form-a-target-string-given-a-dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/).

### Goal
Count how many ways to form `target` by choosing characters from left to right
columns of equal-length words. Once a column is used, later choices must use
strictly later columns.

### Function Contract
**Inputs**

- `words`: equal-length source words.
- `target`: the string to form.

**Return value**

The number of ways modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `words = ["acca", "bbbb", "caca"], target = "aba"`
- Output: `6`

**Example 2**

- Input: `words = ["abba", "baab"], target = "bab"`
- Output: `4`

**Example 3**

- Input: `words = ["abcd"], target = "abcd"`
- Output: `1`

---

## Solution
### Approach
Precompute character frequencies for each column. Use dynamic programming over
target prefixes: when processing a column, update target positions from right to
left, adding `dp[i] * count[column][target[i]]` to `dp[i + 1]`. This either uses
the current column for the next target character or skips it.

### Complexity Analysis
- **Time Complexity**: `O(W * L + L * T)`, where `W` is word count, `L` is word length, and `T` is target length.
- **Space Complexity**: `O(L * alphabet + T)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
