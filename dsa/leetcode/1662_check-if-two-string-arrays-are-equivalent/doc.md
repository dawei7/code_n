# Check If Two String Arrays are Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1662 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |

## Problem Description
### Goal
Each input is an array of nonempty lowercase string fragments. An array represents the single string formed by concatenating all of its elements in their given order from left to right; fragment boundaries do not become part of that represented string.

Determine whether `word1` and `word2` represent exactly the same character sequence, even when the two arrays divide that sequence at different positions.

### Function Contract
**Inputs**

- `word1`: between 1 and $10^3$ nonempty lowercase fragments.
- `word2`: between 1 and $10^3$ nonempty lowercase fragments.

Each represented string contains at most $10^3$ characters. Let $N$ be the total number of characters across both arrays.

**Return value**

Return `true` when the ordered concatenations are identical; otherwise return `false`.

### Examples
**Example 1**

- Input: `word1 = ["ab", "c"], word2 = ["a", "bc"]`
- Output: `true`

Both arrays represent `"abc"`.

**Example 2**

- Input: `word1 = ["a", "cb"], word2 = ["ab", "c"]`
- Output: `false`

**Example 3**

- Input: `word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]`
- Output: `true`
