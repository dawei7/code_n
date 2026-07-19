# Index Pairs of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1065 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Trie, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/index-pairs-of-a-string/) |

## Problem Description

### Goal

Given a lowercase string `text` and an array of lowercase strings `words`, find every inclusive index pair `[i, j]` for which the contiguous substring `text[i:j + 1]` is exactly one of the supplied words.

Return all matching pairs ordered first by increasing start index `i` and, when starts are equal, by increasing end index `j`. Overlapping matches and matches nested inside longer matches must all be included; the task reports positions rather than only distinct matched words.

### Function Contract

**Inputs**

- `text`: a lowercase English string of length $N$, where $1 \le N \le 100$.
- `words`: an array of $W$ distinct lowercase English strings, where $1 \le W \le 20$ and each word has length at most $50$.
- Let $L$ be the maximum word length and let

$$
S=\sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

- Every inclusive pair `[i, j]` whose represented substring belongs to `words`, sorted by `i` and then `j`.

### Examples

**Example 1**

- Input: `text = "thestoryofleetcodeandme", words = ["story", "fleet", "leetcode"]`
- Output: `[[3, 7], [9, 13], [10, 17]]`

**Example 2**

- Input: `text = "ababa", words = ["aba", "ab"]`
- Output: `[[0, 1], [0, 2], [2, 3], [2, 4]]`
- Explanation: Matches sharing or overlapping positions are all reported.

**Example 3**

- Input: `text = "abc", words = ["d"]`
- Output: `[]`
