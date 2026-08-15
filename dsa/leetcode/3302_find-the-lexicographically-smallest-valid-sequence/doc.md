# Find the Lexicographically Smallest Valid Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3302 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) |

## Problem Description

### Goal

Two equal-length strings are almost equal when changing at most one character of the first can make it identical to the second. Given `word1` and the shorter `word2`, select exactly `word2.length` indices from `word1` in strictly ascending order. Reading the source characters at those indices must produce a string almost equal to `word2`.

Return the lexicographically smallest valid sequence of indices: minimize its first index, then its second if tied, and so on. The ordering is based on the numeric index array rather than on the selected characters. Return an empty list when no selection can meet the at-most-one-mismatch rule.

### Function Contract

**Inputs**

- `word1`: The lowercase source string from which indices are selected.
- `word2`: The lowercase target string compared with the selected subsequence.

The target is non-empty and strictly shorter than the source, and `word1.length` is at most $3\cdot10^5$.

**Return value**

- The lexicographically smallest ascending index list whose selected characters differ from `word2` in at most one position, or `[]` if none exists.

### Examples

#### Example 1

- **Input:** `word1 = "vbcca"`, `word2 = "abc"`
- **Output:** `[0,1,2]`
- **Explanation:** The selected string is `"vbc"`; changing its first character makes `"abc"`.

#### Example 2

- **Input:** `word1 = "bacdc"`, `word2 = "abc"`
- **Output:** `[1,2,4]`
- **Explanation:** The selection is `"adc"`, with only its middle character mismatching.

#### Example 3

- **Input:** `word1 = "aaaaaa"`, `word2 = "aaabc"`
- **Output:** `[]`
- **Explanation:** Any length-five selection differs from the target in at least two positions.

#### Example 4

- **Input:** `word1 = "abc"`, `word2 = "ab"`
- **Output:** `[0,1]`
- **Explanation:** The earliest two indices already select the target exactly.
