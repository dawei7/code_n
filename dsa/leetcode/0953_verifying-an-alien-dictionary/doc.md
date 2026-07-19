# Verifying an Alien Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 953 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [verifying-an-alien-dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) |

## Problem Description

### Goal

An alien language uses the same 26 lowercase English letters, but its alphabet may place them in a different order. The string `order` is a permutation of those letters from smallest to largest.

Given a sequence of alien `words`, determine whether it is sorted lexicographically according to that alphabet. At the first differing character, the word containing the earlier alien letter must come first. If one word is a prefix of the other, the shorter word must come first.

### Function Contract

Define

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Inputs**

- `words`: a list of 1 through 100 strings, each containing 1 through 20 lowercase English letters.
- `order`: a length-26 permutation of the lowercase English letters.

**Return value**

Return `true` exactly when `words` is in non-decreasing alien lexicographic order.

### Examples

**Example 1**

- Input: `words = ["hello","leetcode"]`, `order = "hlabcdefgijkmnopqrstuvwxyz"`
- Output: `true`
- Explanation: The first differing letters are `h` and `l`, and `h` comes earlier in the alien alphabet.

**Example 2**

- Input: `words = ["word","world","row"]`, `order = "worldabcefghijkmnpqstuvxyz"`
- Output: `false`
- Explanation: In the first pair, `d` comes after `l` in the supplied order.

**Example 3**

- Input: `words = ["apple","app"]`, `order = "abcdefghijklmnopqrstuvwxyz"`
- Output: `false`
- Explanation: `"app"` is a prefix of `"apple"` and therefore must appear first.
