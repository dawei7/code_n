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

### Required Complexity

- **Time:** $O(S+NL)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Share word prefixes in a trie:** Insert every word character by character. Mark the node reached at the end of each word as terminal. Common prefixes occupy the same path, so they are processed together rather than compared independently against the text.

**Walk from every possible start:** For each start index in increasing order, follow trie edges while moving the text end index rightward. Stop immediately if the next character has no trie edge, because no longer word can match that start. Whenever the reached node is terminal, append `[start, end]`.

**Produce sorted output directly:** Starts are visited from smallest to largest, and for a fixed start the end index only increases. The appended pairs are therefore already ordered by start and then end, so no separate sorting pass is needed.

Every reported terminal path spells a complete supplied word and exactly matches the corresponding contiguous text range. Conversely, any supplied word occurring at a start follows its trie path without encountering a missing edge and reaches a terminal node at its final character, so its pair is reported.

#### Complexity detail

Building the trie takes $O(S)$ time and space. From each of the $N$ starts, traversal examines at most $L$ characters, giving $O(NL)$ search time. The total time is $O(S+NL)$ and the trie uses $O(S)$ auxiliary space, excluding the required output.

#### Alternatives and edge cases

- **Check every word at every start:** Direct matching is simple but can take $O(NWL)$ time because common prefixes are compared repeatedly.
- **Search each word independently:** Repeated substring searches still need a final sort and may revisit the text for every word.
- **Aho-Corasick automaton:** It can scan the text in $O(S+N+R)$ time for $R$ matches, but failure links add complexity unnecessary for these bounds.
- **Overlapping matches:** Advancing to the next start rather than past a match ensures none are skipped.
- **Nested words:** Terminal markers at multiple depths report both a short word and a longer word beginning at the same index.
- **No match:** No terminal node is reached, so return an empty list.
- **Word longer than remaining text:** Traversal simply reaches the end of `text` before reaching that terminal.

</details>
