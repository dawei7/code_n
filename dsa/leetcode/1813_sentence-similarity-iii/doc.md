# Sentence Similarity III

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sentence-similarity-iii/) |
| Frontend ID | 1813 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each of `sentence1` and `sentence2` is a non-empty sequence of words. Words contain only uppercase and lowercase English letters, consecutive words are separated by exactly one space, and neither sentence has leading or trailing spaces.

The sentences are similar when an arbitrary sentence, possibly empty, can be inserted at one word boundary inside either original sentence to make the two strings equal. The inserted words must remain separated from existing words by spaces; characters cannot be inserted into an existing word. Return whether one permitted insertion can make `sentence1` and `sentence2` identical.

### Function Contract

**Inputs**

- `sentence1`, `sentence2`: valid sentence strings whose lengths are each from 1 through 100 characters.
- Let $n$ and $m$ be their respective numbers of words.
- Word comparison is case-sensitive.

**Return value**

- Return `true` if the longer sentence can be obtained by inserting one contiguous sequence of whole words into the shorter sentence.
- The inserted sequence may be empty or may occur before the first word, between two words, or after the last word.
- Return `false` otherwise.

### Examples

**Example 1**

- Input: `sentence1 = "My name is Haley", sentence2 = "My Haley"`
- Output: `true`

Insert `"name is"` between the two words of `sentence2`.

**Example 2**

- Input: `sentence1 = "of", sentence2 = "A lot of words"`
- Output: `false`

The shorter word matches an interior word, leaving unmatched words on both sides; one insertion cannot preserve the shorter sentence's order at a single boundary.

**Example 3**

- Input: `sentence1 = "Eating right now", sentence2 = "Eating"`
- Output: `true`

Insert `"right now"` after the shorter sentence.

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(n + m)$

<details>
<summary>Approach</summary>

#### General

**Make the insertion direction explicit**

Split both sentences into word lists and swap the lists when necessary so `shorter` never has more words than `longer`. Similarity then asks whether deleting one contiguous block from `longer` leaves exactly `shorter`.

**Consume the common prefix**

Advance from the beginning while corresponding words match. These words must remain before any inserted block. Stop at the first mismatch or after consuming every shorter word.

**Consume a nonoverlapping common suffix**

Compare words from the end while they match, but stop once suffix matches would overlap the already consumed prefix in `shorter`. These words can remain after the inserted block. Any unmatched words of `longer` between the matched prefix and suffix form the one candidate insertion.

The sentences are similar exactly when the prefix and suffix together cover every word of `shorter`. If they do, removing the intervening block of `longer` reconstructs `shorter`. If some shorter word remains uncovered, mismatches occur in more than one retained region, so deleting one contiguous block cannot make the lists equal.

#### Complexity detail

Splitting reads all words and characters in both sentences. The prefix and suffix pointers together compare at most $n$ shorter words, so total time is $O(n+m)$. The two word lists use $O(n+m)$ space.

#### Alternatives and edge cases

- **Try every inserted interval:** Removing every possible contiguous block from the longer list and comparing the remainder is correct but takes cubic work with repeated list construction.
- **Deque end matching:** Repeatedly remove equal words from either the front or back until the shorter deque is empty; this is also linear but mutates both lists.
- **Identical sentences:** The allowed inserted sentence may be empty, so equality is similar.
- **Insertion at the beginning:** A full suffix match covers the shorter sentence.
- **Insertion at the end:** A full prefix match covers it.
- **Insertion in the middle:** The shorter sentence contributes both a matching prefix and suffix.
- **Interior-only match:** Matching a shorter word somewhere inside the longer sentence is insufficient when unmatched words remain on both sides.
- **Whole-word boundary:** `"Frog"` cannot become `"Frogs"` by inserting `"s"` because insertion cannot split a word.
- **Repeated words:** Prevent prefix and suffix pointers from covering the same shorter position twice.
- **Case sensitivity:** Words such as `"Word"` and `"word"` do not match.

</details>
