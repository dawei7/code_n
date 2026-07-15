# Occurrences After Bigram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1078 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/occurrences-after-bigram/) |

## Problem Description

### Goal

Two given strings, `first` and `second`, define a bigram. Within `text`, consider every consecutive three-word occurrence of the form `first second third`: `second` must come immediately after `first`, and `third` must come immediately after `second`.

Return an array containing the word `third` from every such occurrence, preserving the occurrences' order in `text`. The text contains lowercase English words separated by single spaces, with no leading or trailing space; `first` and `second` also contain only lowercase English letters.

### Function Contract

**Inputs**

- `text`: a sentence of $N$ characters and $W$ single-space-separated words, with $1 \le N \le 1000$.
- `first`: the first bigram word, with length from 1 through 10.
- `second`: the second bigram word, with length from 1 through 10.

**Return value**

- A list of every word immediately following a consecutive `first second` pair, in sentence order.

### Examples

**Example 1**

- Input: `text = "alice is a good girl she is a good student"`, `first = "a"`, `second = "good"`
- Output: `["girl", "student"]`

**Example 2**

- Input: `text = "we will we will rock you"`, `first = "we"`, `second = "will"`
- Output: `["we", "rock"]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Expose word boundaries once:** Split `text` on its guaranteed single spaces. This produces the words in their original order without empty tokens.

**Inspect each possible triple:** For every index `i` from zero through `len(words) - 3`, compare `words[i]` with `first` and `words[i + 1]` with `second`. When both match, append `words[i + 2]`. Overlapping occurrences are handled because the index advances by one rather than skipping past a match.

Every appended word follows a matching adjacent pair by the two comparisons. Conversely, every valid three-word occurrence begins at one inspected index, so its third word is appended exactly once and in sentence order.

#### Complexity detail

Splitting and scanning process $N$ characters in $O(N)$ time. The word list and returned strings require $O(N)$ space in total. There are $W-2$ candidate triples when $W \ge 3$.

#### Alternatives and edge cases

- **Regular expression:** A lookahead can capture overlapping matches, but careful word boundaries and escaping make it less direct than token scanning.
- **Repeated prefix reconstruction:** Rebuilding or rescanning a prefix for every candidate remains correct but can take quadratic time.
- **Fewer than three words:** No word can follow a complete bigram, so the answer is empty.
- **Bigram at the end:** A final `first second` pair contributes nothing because no `third` word follows it.
- **Overlapping matches:** A reported third word may also begin the next matching bigram and must not be skipped.
- **Repeated output words:** Preserve every occurrence; do not deduplicate the result.

</details>
