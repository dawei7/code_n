# Smallest Subsequence of Distinct Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1081 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-subsequence-of-distinct-characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/).

### Goal
Return the lexicographically smallest subsequence of `s` that contains every distinct character from `s` exactly once.

### Function Contract
**Inputs**

- `s`: Lowercase English string.

**Return value**

Smallest valid subsequence containing each distinct character once.

### Examples
**Example 1**

- Input: `s = "bcabc"`
- Output: `"abc"`

**Example 2**

- Input: `s = "cbacdcbc"`
- Output: `"acdb"`

**Example 3**

- Input: `s = "abacb"`
- Output: `"abc"`

---

## Solution
### Approach
Track the last occurrence of each character. Build the answer with a stack and a set of characters already in the stack. For each character, skip it if it is already included. Otherwise, while the stack top is larger than the current character and appears again later, pop it to make the result lexicographically smaller.

After the popping step, push the current character. The final stack is the desired subsequence.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(1)` for lowercase letters, excluding the output.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
