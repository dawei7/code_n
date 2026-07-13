# Substring with Concatenation of All Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 30 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |

## Problem Description
### Goal
You are given a string `s` and a nonempty list `words` whose entries all have the same positive length. Form a target block by concatenating every listed word exactly once in any ordering, with no characters inserted between words.

Return every zero-based index where a substring of `s` equals one such complete block. Duplicate words in the list are separate required occurrences, so a candidate must match their exact multiplicities. Valid blocks may overlap, and the returned start indices may appear in any order; return an empty list when none exists.

### Function Contract
**Inputs**

- `s`: `str`
- `words`: non-empty `List[str]` of equal-length strings

**Return value**

A `List[int]` containing all valid start indices in any order.

### Examples
**Example 1**

- Input: `s = "barfoothefoobarman", words = ["foo", "bar"]`
- Output: `[0, 9]`

**Example 2**

- Input: `s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]`
- Output: `[]`

**Example 3**

- Input: `s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]`
- Output: `[6, 9, 12]`

### Required Complexity

- **Time:** $O(n \cdot L)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Separate the `L` possible token alignments**

Let every word have length `L` and let `k` be the number of words. A valid concatenation has total length `kL` and consists entirely of `L`-character token boundaries. Its start has exactly one residue modulo `L`.

For each offset from `0` through $L - 1$, scan tokens beginning only at positions with that residue. This turns the string into `L` independent token streams. Within one stream, maintain a sliding window, a count map for words currently inside it, and the number of tokens in the window.

**Reset on foreign words and shrink on excess copies**

If a token does not appear in the required frequency map, no valid concatenation in the current alignment can cross it. Clear the window counts and restart immediately after that token.

Otherwise add the token. If its count now exceeds the required multiplicity, remove whole tokens from the left until the excess copy has been expelled. Shrinking only until all counts are legal keeps the widest viable suffix; removing more could skip a valid overlapping window.

When the legal window contains exactly `k` tokens, its counts must equal the required multiset, so record its left boundary. Then remove exactly its leftmost token. This prepares the window to discover a match beginning one token later, including overlaps.

**The window is the longest legal suffix of its token stream**

After each token has been normalized, the window contains only required words, no word exceeds its target multiplicity, and its count table exactly describes the tokens between `left` and the right boundary. It is also the longest suffix of the processed aligned stream satisfying those conditions: a reset proves nothing can cross a foreign token, and shrinking stops as soon as the excess is removed.

Because no count exceeds its target, a window of `k` tokens cannot be missing one required copy without exceeding another. Its multiset is therefore exactly `words`.

**Trace duplicates and overlapping windows**

For `barfoothefoobarman` with `foo, bar`, offset zero reads `bar` then `foo`, producing a two-token valid window at index 0. After recording it, the leftmost `bar` is removed. The foreign token `the` later clears the window; scanning resumes and eventually recognizes `foo, bar` at index 9.

Multiplicity matters for required words `foo, foo, bar`. Seeing a third `foo` forces the left boundary forward until only two copies remain. A set would be insufficient because it could not distinguish the legal two copies from the excess third copy.

**Offset classes and multiplicities leave no missed start**

Every possible concatenation start has one residue modulo the word length, so exactly one aligned scan examines it. If that start is valid, all following `k` tokens belong to the dictionary and never exceed required multiplicity; neither an invalid-token reset nor an excess-count shrink can move the left boundary past it before the full window is recognized.

Conversely, a reported window contains exactly `k` aligned dictionary tokens and no count above its required value. Since the required multiset also has size `k`, every count must match exactly. The index therefore begins a valid concatenation, establishing both completeness and soundness.

#### Complexity detail

Across all offsets there are $O(n)$ aligned token positions in total. Each token enters once and leaves at most once. Ordinary substring extraction and hashing cost $O(L)$, which explains the stated $O(n \cdot L)$ time; with constant-time substring views or prehashed tokens, the window operations themselves are $O(n)$. The two count maps contain at most `k` distinct words and use $O(k)$ space.

#### Alternatives and edge cases

- **Check every character start independently:** rebuilds a word multiset for each candidate and can require $O(nkL)$ time.
- **Sort each candidate's tokens:** adds $O(k \log k)$ comparison work per start.
- **Rolling hashes for tokens:** can reduce substring materialization costs but needs collision-safe verification and more machinery.
- If `kL > len(s)`, no start can fit the concatenation. All words have equal nonzero length by contract; without that property, residue-class token windows would not apply.
- Duplicate words must be counted, not deduplicated. Result order is unrestricted because offsets are scanned independently.

</details>
