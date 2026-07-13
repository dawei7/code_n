# Word Break II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 140 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-break-ii/) |

## Problem Description
### Goal
Given a string and a dictionary of unique nonempty words, insert spaces so that every resulting token is a dictionary entry. A sentence must consume the entire string from left to right without deleting, rearranging, or leaving unmatched characters, and dictionary words may be reused.

Return all distinct valid sentences, preserving the original characters inside each sentence and separating adjacent words with one space. Different choices of boundaries must all be included, while partial segmentations are excluded. The sentences may appear in any order. If no complete segmentation exists, return an empty list rather than the original unsegmented string.

### Function Contract
**Inputs**

- `s`: the string to segment
- `word_dict`: available nonempty words

**Return value**

All valid fully segmented sentences in any order.

### Examples
**Example 1**

- Input: `s = "catsanddog", word_dict = ["cat","cats","and","sand","dog"]`
- Output: `["cats and dog", "cat sand dog"]`

**Example 2**

- Input: `s = "pineapplepenapple", word_dict = ["apple","pen","applepen","pine","pineapple"]`
- Output: three valid sentences

**Example 3**

- Input: `s = "catsandog", word_dict = ["cats","dog","sand","and","cat"]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n^2 + L)$
- **Space:** $O(n + L)$

<details>
<summary>Approach</summary>

#### General

**Memoize sentence sets by suffix boundary**

Memoize `sentences(start)`, the immutable collection of every valid sentence whose words concatenate to `s[start:]`. Different prefix choices often reach the same suffix; caching prevents reconstructing its entire sentence set repeatedly.

For `start = len(s)`, return one empty continuation rather than no continuations. This identity allows a dictionary word ending at the string boundary to form a complete sentence.

**Combine each valid first word with every suffix sentence**

For every `end > start`, test `s[start:end]` against the dictionary. For each cached continuation from `sentences(end)`, emit the word alone when the continuation is empty, otherwise join them with exactly one space. This conditional avoids a trailing space at sentence end.

**Cached sentences cover their suffix completely and only once per cut sequence**

The cached result for `start` contains exactly all dictionary sentences whose concatenation without spaces equals `s[start:]`.

**Trace two first-word choices sharing cached suffixes**

Prefix `cat` combines with suffix sentence `sand dog`; prefix `cats` combines with `and dog`. Other prefix boundaries are rejected, producing exactly two sentences.

**The first dictionary word uniquely decomposes each sentence**

Every valid sentence begins with one dictionary prefix ending at a specific boundary. The search tries that boundary, and the memoized suffix state supplies every valid sentence covering the remaining characters.

Combining the prefix with each complete suffix sentence constructs only full dictionary segmentations. Conversely, selecting the first word of any valid sentence leads to its suffix decomposition, so every sentence is generated without losing alternate continuations.

#### Complexity detail

Memoization bounds suffix-state and boundary exploration to $O(n^2)$ before output. Constructing all returned sentence characters costs `L`; cached sentences and output use $O(n+L)$ beyond dictionary storage.

#### Alternatives and edge cases

- **Unmemoized backtracking:** recomputes identical suffix sentence sets exponentially.
- **Boolean word-break DP:** decides existence but discards required sentences.
- **Greedy longest-prefix choice:** misses valid alternatives.
- If no dictionary prefix leads to a complete suffix sentence, cache an empty tuple/list for that boundary so future calls fail immediately.
- Output may be exponential; memoization removes repeated subproblem work but cannot avoid constructing every required sentence.

</details>
