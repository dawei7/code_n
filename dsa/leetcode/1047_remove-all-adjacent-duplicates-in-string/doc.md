# Remove All Adjacent Duplicates In String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1047 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-all-adjacent-duplicates-in-string](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/).

### Goal
Repeatedly remove pairs of equal adjacent characters from a string until no such pair remains. Return the final string.

### Function Contract
**Inputs**

- `s`: Lowercase English string.

**Return value**

String left after all possible adjacent duplicate-pair removals.

### Examples
**Example 1**

- Input: `s = "abbaca"`
- Output: `"ca"`

**Example 2**

- Input: `s = "azxxzy"`
- Output: `"ay"`

**Example 3**

- Input: `s = "a"`
- Output: `"a"`

---

## Solution
### Approach
Use a stack of characters representing the already reduced prefix. For each character, compare it with the stack top. If they match, pop the top because the pair disappears; otherwise push the new character.

The stack content after the scan is exactly the fully reduced string.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(n)` for the stack.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
