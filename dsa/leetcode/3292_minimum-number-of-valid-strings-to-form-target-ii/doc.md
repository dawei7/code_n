# Minimum Number of Valid Strings to Form Target II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3292 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/) |

## Problem Description

### Goal

You are given an array of lowercase strings `words` and a lowercase string `target`. Any nonempty prefix of any string in `words` is valid, whether or not that prefix appears as a complete word in the array.

Construct `target` by concatenating valid strings and return the minimum number of pieces required. A valid prefix may be reused, and pieces may be drawn from different words. Return `-1` if no concatenation covers the entire target. This version permits a target of length 50,000, so checking every target substring is too slow.

### Function Contract

**Inputs**

- `words`: A list of lowercase English strings.
- `target`: The lowercase English string to construct.

Let $W$ be the number of words, $S$ their total length, and $T$ the target length. The constraints guarantee $1 \le W \le 100$, $S \le 10^5$, and $1 \le T \le 5\cdot10^4$; each word has length at most $5\cdot10^4$.

**Return value**

- The minimum number of valid prefixes whose concatenation equals `target`, or `-1` if construction is impossible.

### Examples

#### Example 1

- **Input:** `words = ["abc","aaaaa","bcdef"]`, `target = "aabcdabc"`
- **Output:** `3`
- **Explanation:** `"aa" + "bcd" + "abc"` uses three valid prefixes.

#### Example 2

- **Input:** `words = ["abababab","ab"]`, `target = "ababaababa"`
- **Output:** `2`
- **Explanation:** Two copies of the valid prefix `"ababa"` form the target.

#### Example 3

- **Input:** `words = ["abcdef"]`, `target = "xyz"`
- **Output:** `-1`
- **Explanation:** No valid prefix can begin the target.
