# Minimum Number of Valid Strings to Form Target I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3291 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Trie, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/) |

## Problem Description

### Goal

You are given an array of lowercase strings `words` and another lowercase string `target`. A nonempty string is valid when it is a prefix of at least one string in `words`; it does not need to be an entire word.

Form `target` by concatenating valid strings and return the minimum number of pieces required. Pieces may reuse the same word prefix, and different pieces may come from different words. If no sequence of valid strings produces all of `target`, return `-1`.

### Function Contract

**Inputs**

- `words`: A list of lowercase English strings.
- `target`: The lowercase English string to construct.

Let $S$ be the sum of all word lengths and $T$ be the length of `target`. The constraints guarantee at most 100 words, $S \le 10^5$, and $1 \le T \le 5000$; each word has length from 1 through 5000.

**Return value**

- The minimum number of valid prefixes whose concatenation equals `target`, or `-1` when construction is impossible.

### Examples

#### Example 1

- **Input:** `words = ["abc","aaaaa","bcdef"]`, `target = "aabcdabc"`
- **Output:** `3`
- **Explanation:** The valid prefixes `"aa"`, `"bcd"`, and `"abc"` concatenate to the target.

#### Example 2

- **Input:** `words = ["abababab","ab"]`, `target = "ababaababa"`
- **Output:** `2`
- **Explanation:** Two copies of the valid prefix `"ababa"` form the target.

#### Example 3

- **Input:** `words = ["abcdef"]`, `target = "xyz"`
- **Output:** `-1`
- **Explanation:** No valid prefix begins with `"x"`.
