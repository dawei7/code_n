# Extra Characters in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2707 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/extra-characters-in-a-string/) |

## Problem Description

### Goal

You are given a 0-indexed lowercase string `s` and a collection of distinct lowercase words `dictionary`. Select one or more non-overlapping substrings of `s` such that every selected substring is exactly a dictionary word. Characters not covered by any selected substring are extra.

The selected dictionary occurrences may leave gaps and do not need to use every dictionary word. Choose their positions so that the total number of uncovered characters is as small as possible, and return that minimum. Different segmentations can overlap as candidates, but the occurrences in the final choice must not overlap.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \le n \le 50$.
- `dictionary`: Between $1$ and $50$ distinct lowercase words, each with length from $1$ through $50$.

Let

$$
W = \sum_{w \in \texttt{dictionary}} \lvert w \rvert.
$$

**Return value**

Return the minimum number of characters in `s` that remain outside all chosen, non-overlapping dictionary-word occurrences.

### Examples

**Example 1**

- Input: `s = "leetscode"`, `dictionary = ["leet","code","leetcode"]`
- Output: `1`
- Explanation: Use `"leet"` at indices $0$ through $3$ and `"code"` at indices $5$ through $8$; only `s[4]` remains extra.

**Example 2**

- Input: `s = "sayhelloworld"`, `dictionary = ["hello","world"]`
- Output: `3`
- Explanation: The prefix `"say"` is extra, while the remaining ten characters form two dictionary words.

**Example 3**

- Input: `s = "aaaa"`, `dictionary = ["a","aa"]`
- Output: `0`
- Explanation: Several non-overlapping segmentations cover the entire string.
