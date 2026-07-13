# Longest Word in Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 720 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary/) |

## Problem Description
### Goal
Given an array `words` representing an English dictionary, find a word that can be built one character at a time using other words in the dictionary. Building proceeds from left to right by appending one character, so every nonempty prefix of the chosen word must also occur in `words`.

Return the longest buildable word. If several answers have the same maximum length, return the lexicographically smallest one. If no word can begin from a one-letter dictionary entry, return the empty string.

### Function Contract
**Inputs**

- `words`: a nonempty array of distinct lowercase English words

**Return value**

- The longest word constructible one character at a time through dictionary prefixes, breaking ties lexicographically; return the empty string if no one-letter starting word exists

### Examples
**Example 1**

- Input: `words = ["w","wo","wor","worl","world"]`
- Output: `"world"`

**Example 2**

- Input: `words = ["a","banana","app","appl","ap","apply","apple"]`
- Output: `"apple"`

**Example 3**

- Input: `words = ["t","to","tea","ted","ten","i","in","inn"]`
- Output: `"inn"`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Represent every prefix once in a trie**

Insert all words into a trie with one child slot per lowercase letter. Store the complete word at its terminal node. Shared prefixes then occupy shared nodes, and insertion touches exactly one node per input character.

**Traverse only buildable nodes**

Begin at the empty root. A child is eligible for traversal only when its node terminates a dictionary word. Reaching that child proves the new prefix exists, while having reached its parent proves every shorter prefix exists. Descendants behind a missing prefix are never visited.

**Select by the complete candidate word**

Every visited terminal node supplies its stored word. Replace the answer when that word is longer, or when it has the same length and is lexicographically smaller. Explicit comparison makes traversal order irrelevant.

**Why eligibility captures the construction rule**

A visited node is reached through a chain of terminal parent nodes, so every nonempty prefix of its word belongs to the dictionary. Conversely, a valid word has a terminal node at every prefix along its root-to-word path, so the traversal follows that entire path and considers it. The final length and lexicographic comparison therefore chooses exactly the required valid word.

#### Complexity detail

Let `S` be the total number of input characters. Trie construction creates at most `S` nodes, and traversal examines a constant 26 child slots per visited node. The total time and space are both $O(S)$.

#### Alternatives and edge cases

- **Hash set plus length ordering:** process words from shorter to longer and accept a word when its immediate prefix is already buildable; sorting adds $O(n \log n)$ comparisons.
- **Lexicographic sorting with a buildable set:** each word's prefix sorts before it, allowing a compact solution, though sorting still prevents linear total time.
- **List-based prefix searches:** checking every prefix with linear membership scans is correct but can become quadratic in the number of words.
- One-letter words are buildable directly from the empty starting prefix.
- Missing any intermediate prefix invalidates all longer words on that trie branch.
- Equal-length valid words require lexicographic comparison, not input-order preference.
- If no one-letter word is present, no dictionary word can begin a valid construction and the answer is empty.

</details>
