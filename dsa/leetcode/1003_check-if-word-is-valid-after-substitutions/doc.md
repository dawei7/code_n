# Check If Word Is Valid After Substitutions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1003 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-word-is-valid-after-substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/).

### Goal
Determine whether a string can be built by repeatedly inserting the substring `abc` into an initially empty string. Equivalently, the string is valid if all of its characters can be removed by repeatedly deleting adjacent `abc` groups.

### Function Contract
**Inputs**

- `s`: String containing lowercase letters.

**Return value**

Boolean indicating whether `s` is a valid result of the repeated `abc` insertion process.

### Examples
**Example 1**

- Input: `s = "aabcbc"`
- Output: `true`

**Example 2**

- Input: `s = "abcabcababcc"`
- Output: `true`

**Example 3**

- Input: `s = "abccba"`
- Output: `false`

---

## Solution
### Approach
Use a stack to simulate reducing completed `abc` blocks. Scan characters from left to right, pushing each character onto the stack. Whenever the top three stack entries form `a`, `b`, `c`, remove them because that block could have been the last inserted block in a valid construction.

At the end, the string is valid exactly when the stack is empty. If any characters remain, no sequence of `abc` removals can consume the whole string.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(n)` for the stack in the worst case.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
