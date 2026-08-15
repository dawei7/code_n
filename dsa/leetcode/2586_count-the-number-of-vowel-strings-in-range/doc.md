# Count the Number of Vowel Strings in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2586 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/) |

## Problem Description

### Goal

You are given a 0-indexed array `words` and two indices, `left` and `right`. A word is a vowel string when both its first and last characters belong to `a`, `e`, `i`, `o`, or `u`.

Only the endpoint characters determine this classification; characters between them do not matter. Every supplied word is nonempty and contains only lowercase English letters, so both endpoints always exist and uppercase handling is unnecessary.

Count the vowel strings whose indices lie in the inclusive range `[left, right]`. Words before `left` or after `right` must not affect the result.

### Function Contract

**Inputs**

- `words`: A nonempty list of lowercase English strings. The list has at most $1000$ entries, and every word has length from $1$ through $10$.
- `left`: The first index included in the inspected range.
- `right`: The last index included in the inspected range, with $0 \leq \texttt{left} \leq \texttt{right} < \lvert\texttt{words}\rvert$.

**Return value**

- The number of words in the inclusive range that start and end with vowels.

### Examples

#### Example 1

- **Input:** `words = ["are","amy","u"], left = 0, right = 2`
- **Output:** `2`

`"are"` and `"u"` start and end with vowels; `"amy"` does not.

#### Example 2

- **Input:** `words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4`
- **Output:** `3`

The qualifying words in that range are `"aeo"`, `"ooo"`, and `"artro"`.
