# Maximum Nesting Depth of Two Valid Parentheses Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1111 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-nesting-depth-of-two-valid-parentheses-strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/).

### Goal
Split a valid parentheses string into two valid subsequences `A` and `B`. Return an assignment array where `0` means the character goes to `A` and `1` means it goes to `B`, minimizing the larger nesting depth between `A` and `B`.

### Function Contract
**Inputs**

- `seq`: Valid parentheses string.

**Return value**

List of `0` and `1` assignments. Any assignment with minimum possible maximum depth is valid.

### Examples
**Example 1**

- Input: `seq = "(()())"`
- Output: `[0, 1, 1, 1, 1, 0]`

**Example 2**

- Input: `seq = "()(())()"`
- Output: `[0, 0, 0, 1, 1, 0, 0, 0]`

**Example 3**

- Input: `seq = "()"`
- Output: `[0, 0]`

---

## Solution
### Approach
Assign parentheses by depth parity. As the nesting depth changes, alternating depths between `A` and `B` keeps both subsequences balanced while splitting the deepest nesting as evenly as possible.

For each opening parenthesis, increase depth and assign based on the new depth parity. For each closing parenthesis, assign based on the current depth parity and then decrease depth.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `seq`.
- **Space Complexity**: `O(n)` for the assignment array.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
