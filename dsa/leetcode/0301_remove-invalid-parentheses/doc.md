# Remove Invalid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 301 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/) |

## Problem Description
### Goal
Given a string containing letters and parentheses, delete some parenthesis characters so every opening parenthesis in the result has a later matching close and no prefix contains more closes than opens. Non-parenthesis characters cannot be removed or reordered.

Use the minimum possible number of deletions, then return every unique valid string obtainable with exactly that minimum. Return the answer in any order, and do not repeat text produced by different deletion choices. The empty string is a valid parenthesis structure when all parentheses must be removed, while an already valid input should be returned unchanged as the sole result.

### Function Contract
**Inputs**

- `s`: a string containing letters and parentheses

**Return value**

A list of all distinct valid strings obtainable with the minimum number of removals, in any order.

### Examples
**Example 1**

- Input: `s = "()())()"`
- Output: `["(())()", "()()()"]`

**Example 2**

- Input: `s = "(a)())()"`
- Output: `["(a())()", "(a)()()"]`

**Example 3**

- Input: `s = ")("`
- Output: `[""]`
