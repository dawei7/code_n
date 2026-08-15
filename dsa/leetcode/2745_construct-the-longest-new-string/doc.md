# Construct the Longest New String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2745 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Greedy, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/construct-the-longest-new-string/) |

## Problem Description

### Goal

You have `x` copies of the two-character string `"AA"`, `y` copies of `"BB"`, and `z` copies of `"AB"`. Select any number of these available strings and concatenate the selected pieces in any order to create one new string. Each copy can be used at most once, and it is also valid to leave copies unused.

The resulting string must contain neither `"AAA"` nor `"BBB"` as a substring. Determine the greatest possible length of a new string satisfying this restriction. The return value counts characters, so every selected two-character piece contributes exactly $2$ to the length.

### Function Contract

**Inputs**

- `x`: The number of available `"AA"` pieces, where $1 \le x \le 50$.
- `y`: The number of available `"BB"` pieces, where $1 \le y \le 50$.
- `z`: The number of available `"AB"` pieces, where $1 \le z \le 50$.

**Return value**

Return the maximum number of characters in a valid concatenation that contains neither `"AAA"` nor `"BBB"`.

### Examples

#### Example 1

- **Input:** `x = 2, y = 5, z = 1`
- **Output:** `12`
- **Explanation:** Six pieces can be arranged without creating either forbidden substring.

#### Example 2

- **Input:** `x = 3, y = 2, z = 2`
- **Output:** `14`
- **Explanation:** All seven usable pieces can be included in a valid order.
