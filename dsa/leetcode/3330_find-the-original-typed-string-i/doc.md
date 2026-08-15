# Find the Original Typed String I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3330 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-original-typed-string-i/) |

## Problem Description

### Goal

Alice intended to type a particular string, but she may have held one key too long, causing that character to appear repeatedly on the screen. She knows this mistake happened at most once: either the displayed string is exactly what she intended, or one consecutive group of equal characters is longer than the corresponding group in her intended text.

Given the final displayed string `word`, count how many distinct original strings Alice might have intended. When a repeated group is the possible mistake, its original length may be any positive length smaller than the displayed group; all other characters remain unchanged.

### Function Contract

**Inputs**

- `word`: The final displayed string, consisting only of lowercase English letters.

Its length $n$ satisfies $1\leq n\leq100$.

**Return value**

Return the number of distinct intended strings consistent with zero or one long key press.

### Examples

#### Example 1

- **Input:** `word = "abbcccc"`
- **Output:** `5`
- **Explanation:** The possible originals are `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, and `"abcccc"`.

#### Example 2

- **Input:** `word = "abcd"`
- **Output:** `1`
- **Explanation:** No group is repeated, so only the displayed word itself is possible.

#### Example 3

- **Input:** `word = "aaaa"`
- **Output:** `4`
- **Explanation:** The intended run of `a` may have length one, two, three, or four.
