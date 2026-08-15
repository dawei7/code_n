# Maximize Number of Subsequences in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2207 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/) |

## Problem Description

### Goal

You receive a lowercase string `text` and a lowercase string `pattern` of length two. Insert exactly one character into `text`: the inserted character must be either `pattern[0]` or `pattern[1]`, and its position may be anywhere, including before the first or after the last existing character.

After that insertion, count how many index pairs spell `pattern` as a subsequence. A subsequence keeps the relative order of selected characters but may omit any other characters. Return the largest count attainable by choosing both the inserted character and its position optimally.

### Function Contract

**Inputs**

- `text`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `pattern`: exactly two lowercase English letters; the letters may be equal.

**Return value**

Return the maximum number of subsequences equal to `pattern` after exactly one allowed insertion.

### Examples

#### Example 1

- **Input:** `text = "abdcdbc"`, `pattern = "ac"`
- **Output:** `4`
- **Explanation:** inserting another `a` sufficiently early lets it precede both existing `c` characters while preserving the two existing `ac` subsequences.

#### Example 2

- **Input:** `text = "aabb"`, `pattern = "ab"`
- **Output:** `6`
- **Explanation:** inserting `a` before the `b` characters or inserting `b` after the `a` characters creates two additional subsequences.

#### Example 3

- **Input:** `text = "aaaa"`, `pattern = "aa"`
- **Output:** `10`
- **Explanation:** after inserting another `a`, any two of the five positions form the pattern.
