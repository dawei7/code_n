# Remove All Adjacent Duplicates in String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1209 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-all-adjacent-duplicates-in-string-ii](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/).

### Goal
Repeatedly remove groups of exactly `k` adjacent equal characters from the string until no such group remains. Return the final string.

### Function Contract
**Inputs**

- `s`: Input string.
- `k`: Group size to remove.

**Return value**

String after all removals.

### Examples
**Example 1**

- Input: `s = "abcd"`, `k = 2`
- Output: `"abcd"`

**Example 2**

- Input: `s = "deeedbbcccbdaa"`, `k = 3`
- Output: `"aa"`

**Example 3**

- Input: `s = "pbbcggttciiippooaais"`, `k = 2`
- Output: `"ps"`

---

## Solution
### Approach
Use a stack of `(character, count)` pairs. When the current character matches the stack top, increment the count; otherwise push a new pair. If a count reaches `k`, pop that pair because the group disappears.

At the end, rebuild the string from the remaining stack entries.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
