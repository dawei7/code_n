# Verbal Arithmetic Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1307 |
| Difficulty | Hard |
| Topics | Array, Math, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/verbal-arithmetic-puzzle/) |

## Problem Description
### Goal
A verbal arithmetic equation represents each uppercase letter by one decimal digit. The same letter must always use the same digit, different letters must use different digits, and a word containing more than one character may not begin with 0.

The strings in `words` are the addends and `result` is their sum. After substituting digits for letters, every string is interpreted as an ordinary base-10 integer. Determine whether there is at least one digit assignment for which the sum of all represented addends equals the represented result while satisfying every uniqueness and leading-zero rule.

### Function Contract
**Inputs**

- `words`: between 2 and 5 nonempty uppercase strings.
- `result`: a nonempty uppercase string.
- Every input string has length at most 7.
- Across all addends and the result, there are at most 10 distinct letters.

Let $U$ be the number of distinct letters and $L$ the maximum input-string length. The source bounds give $U\le10$ and $L\le7$.

**Return value**

`true` if a valid one-to-one letter-to-digit assignment makes the represented equation hold; otherwise, `false`.

### Examples
**Example 1**

- Input: `words = ["SEND","MORE"]`, `result = "MONEY"`
- Output: `true`
- Explanation: A valid assignment makes the equation $9567+1085=10652$.

**Example 2**

- Input: `words = ["SIX","SEVEN","SEVEN"]`, `result = "TWENTY"`
- Output: `true`

**Example 3**

- Input: `words = ["LEET","CODE"]`, `result = "POINT"`
- Output: `false`
