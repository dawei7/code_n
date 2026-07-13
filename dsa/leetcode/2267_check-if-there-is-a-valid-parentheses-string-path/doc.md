#  Check if There Is a Valid Parentheses String Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2267 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-there-is-a-valid-parentheses-string-path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/).

### Goal
Move from the top-left to the bottom-right of a parentheses grid using only right and down steps. Determine whether the characters along some path form a valid parentheses string.

### Function Contract
**Inputs**

- `grid`: a matrix containing `"("` and `")"` characters.

**Return value**

`true` if at least one path spells a balanced parentheses sequence; otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]`
- Output: `true`

**Example 2**

- Input: `grid = [[")", ")"], ["(", "("]]`
- Output: `false`

**Example 3**

- Input: `grid = [["(", ")"]]`
- Output: `true`

---

## Solution
### Approach
Use dynamic programming over cells and open-parenthesis balance. Entering `"("` adds one and entering `")"` subtracts one; discard negative balances because no continuation can repair an already invalid prefix. Merge reachable balances from the top and left. The destination is valid exactly when balance zero is reachable. Reject odd path lengths early.

### Complexity Analysis
- **Time Complexity**: `O(mn(m + n))`
- **Space Complexity**: `O(mn(m + n))`, reducible with rolling rows

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
