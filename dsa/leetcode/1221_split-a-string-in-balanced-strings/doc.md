# Split a String in Balanced Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1221 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [split-a-string-in-balanced-strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/split-a-string-in-balanced-strings/).

### Goal
Split the input string into the maximum number of non-empty balanced substrings. A balanced substring contains the same number of `L` and `R` characters.

### Function Contract
**Inputs**

- `s: str` - A balanced string containing only `L` and `R`.

**Return value**

`int` - The maximum number of balanced pieces.

### Examples
**Example 1**

- Input: `s = "RLRRLLRLRL"`
- Output: `4`

**Example 2**

- Input: `s = "RLRRRLLRLL"`
- Output: `2`

**Example 3**

- Input: `s = "LLLLRRRR"`
- Output: `1`

---

## Solution
### Approach
Scan the string once with a balance counter, adding `1` for `R` and subtracting `1` for `L`. Every time the balance returns to zero, the current prefix is balanced and can be cut immediately. Greedily cutting at the earliest zero balance maximizes the number of pieces.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n = len(s)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
