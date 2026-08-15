# Shortest Uncommon Substring in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3076 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/) |

## Problem Description

### Goal

You are given an array `arr` containing $n$ non-empty strings. Construct an array `answer` of the same length by choosing a substring for each input string independently.

For every index $i$, `answer[i]` must be a substring of `arr[i]` that does not occur as a substring of any other string in `arr`. Among all substrings satisfying that condition, choose one with the shortest length. If several shortest choices remain, choose the lexicographically smallest one. If `arr[i]` has no substring absent from every other string, place the empty string at index $i$.

Return the completed `answer` array.

### Function Contract

**Inputs**

- `arr`: An array of $n$ non-empty strings, each containing only lowercase English letters.

The input satisfies $2 \le n \le 100$, and every string has length from $1$ through $20$.

**Return value**

- An array in which element $i$ is the shortest uncommon substring of `arr[i]`, with lexicographic order breaking equal-length ties, or `""` when no such substring exists.

### Examples

#### Example 1

- **Input:** `arr = ["cab", "ad", "bad", "c"]`
- **Output:** `["ab", "", "ba", ""]`
- **Explanation:** For `"cab"`, both `"ab"` and `"ca"` are shortest substrings absent from the other words, so `"ab"` wins lexicographically. The word `"bad"` contributes `"ba"`. Every substring of `"ad"` or `"c"` appears in another word, so those answers are empty.

#### Example 2

- **Input:** `arr = ["abc", "bcd", "abcd"]`
- **Output:** `["", "", "abcd"]`
- **Explanation:** Every substring of each shorter word occurs in `"abcd"`. For the last word, every proper substring appears in one of the other two words, leaving the full string `"abcd"` as its shortest uncommon substring.
