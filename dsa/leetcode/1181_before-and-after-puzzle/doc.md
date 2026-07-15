# Before and After Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1181 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/before-and-after-puzzle/) |

## Problem Description

### Goal

A phrase contains lowercase English words separated by single spaces. A Before and After puzzle is formed from two different phrase indices when the last word of the first phrase equals the first word of the second phrase. Merge the phrases in that order, writing the shared boundary word only once.

Consider every ordered pair `(i, j)` with `i != j`; reversing a pair can therefore produce another result. Return all distinct merged phrases after removing duplicates, sorted in lexicographic order. Equal phrase text at two different indices still represents two eligible phrases.

### Function Contract

**Inputs**

- `phrases`: Between $1$ and $100$ strings, each with length from $1$ through $100$. A phrase contains only lowercase English letters and spaces, has no leading or trailing space, and has no consecutive spaces.
- Define

$$
S=\sum_{x\in\texttt{phrases}} \lvert x\rvert.
$$

- Let $R$ be the number of distinct returned phrases and let $G$ be the total character count of all compatible merged candidates constructed before deduplication.

**Return value**

- The lexicographically sorted list of distinct Before and After puzzle strings formed from different input indices.

### Examples

**Example 1**

- Input: `phrases = ["writing code","code rocks"]`
- Output: `["writing code rocks"]`

**Example 2**

- Input: `phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]`
- Output: `["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]`

**Example 3**

- Input: `phrases = ["a","b","a"]`
- Output: `["a"]`

The two `"a"` entries have different indices, so they may be paired even though their text is equal.

### Required Complexity

- **Time:** $O(S+G+R\log R)$
- **Space:** $O(S+G)$

<details>
<summary>Approach</summary>

#### General

**Extract only the boundary words once.** Split every phrase to obtain its first and last word. Also retain the suffix that begins immediately after the first word; this suffix includes its leading space when the phrase has more words and is empty for a one-word phrase.

**Index possible after phrases.** Build a hash map from each first word to the indices of phrases beginning with it. For phrase `i` as the before part, only indices stored under its last word can match. Skip `j == i`, because a phrase cannot be paired with itself. For every other candidate, form `phrases[i] + suffix[j]`, which keeps the shared word from the before phrase and omits its duplicate at the start of the after phrase.

**Deduplicate before sorting.** Insert each merged candidate into a set, so different ordered pairs producing identical text contribute only once. Sorting that set at the end establishes the required lexicographic order. Duplicate input text at different indices remains usable because the map stores indices rather than unique phrase strings.

#### Complexity detail

Parsing and indexing examine $S$ characters. Hash lookup avoids testing incompatible pairs; constructing all compatible candidates processes $G$ characters. Sorting the $R$ distinct results costs $O(R\log R)$ comparisons under the usual string-key abstraction, giving $O(S+G+R\log R)$ time. Parsed phrases, the boundary index, and generated strings use $O(S+G)$ space.

#### Alternatives and edge cases

- **Test every ordered pair:** This is straightforward and correct but performs $O(n^2)$ boundary comparisons even when no phrases can match.
- **Deduplicate input phrases first:** This is incorrect because equal text at different indices may pair with one another while a lone phrase may not pair with itself.
- **One-word phrase:** Its first and last word are the same, and its after suffix is empty.
- **Pair direction:** `(i, j)` and `(j, i)` are separate possibilities and may yield different puzzles.
- **Duplicate merged results:** Multiple pairs may create the same text; only one copy belongs in the result.
- **No compatible boundary:** The correct result is an empty list.
- **Shared word placement:** The matching word appears once, with the remaining words of the after phrase appended in order.

</details>
