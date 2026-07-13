# Remove Outermost Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1021 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-outermost-parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-outermost-parentheses/).

### Goal
Given a valid parentheses string, split it into its primitive balanced components and remove the outermost pair of parentheses from each component.

### Function Contract
**Inputs**

- `s`: Valid parentheses string.

**Return value**

String remaining after removing each primitive component's outer parentheses.

### Examples
**Example 1**

- Input: `s = "(()())(())"`
- Output: `"()()()"`

**Example 2**

- Input: `s = "(()())(())(()(()))"`
- Output: `"()()()()(())"`

**Example 3**

- Input: `s = "()()"`
- Output: `""`

---

## Solution
### Approach
Track the current nesting depth while scanning the string. For an opening parenthesis, append it only if the current depth is already positive, because depth zero means it is the outer opening of a primitive block. For a closing parenthesis, reduce the depth first and append it only if the resulting depth remains positive.

This keeps every inner parenthesis and skips only the primitive boundaries.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(n)` for the output string.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
