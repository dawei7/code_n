# Valid Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 408 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-word-abbreviation/) |

## Problem Description
### Goal
Given a lowercase `word` and an abbreviation `abbr`, read the abbreviation from left to right. Letter tokens must match the next word character exactly, while a positive decimal number skips that many consecutive characters of the word.

Return `True` only when all abbreviation tokens are valid and consume the entire word exactly. Numeric tokens may contain several digits but cannot begin with zero, cannot represent a zero-length skip, and cannot move past the word's end. Matching only a prefix is insufficient, and abbreviation letters do not stand for arbitrary characters; they remain literal positions in the represented word.

### Function Contract
**Inputs**

- `word`: the original lowercase word
- `abbr`: an abbreviation containing lowercase letters and decimal digits

**Return value**

- Return `True` only when consuming every abbreviation token consumes the entire word without a leading-zero number, mismatch, or overshoot.

### Examples
**Example 1**

- Input: `word = "internationalization", abbr = "i12iz4n"`
- Output: `True`

**Example 2**

- Input: `word = "apple", abbr = "a2e"`
- Output: `False`

**Example 3**

- Input: `word = "substitution", abbr = "s10n"`
- Output: `True`

### Required Complexity

- **Time:** $O(w + a)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep one pointer in each string**

Let `word_index` mark the next unconsumed word character and `abbr_index` the next abbreviation token. A letter token must equal `word[word_index]`; if so, advance both pointers by one.

**Parse an entire numeric token before skipping**

When the abbreviation character is a digit, reject immediately if it is zero because that would be a forbidden leading zero. Accumulate all consecutive digits into one number, then advance only the word pointer by that skip length.

**Reject as soon as the word boundary is crossed**

After a skip, a word index greater than its length proves the abbreviation asks for nonexistent characters. At the end, both pointers must be exhausted: leftover word characters mean the abbreviation is too short, while the abbreviation loop already prevents leftover unmatched tokens.

**Why the scan matches abbreviation semantics exactly**

Each letter consumes exactly one equal word character, and each number consumes exactly its parsed positive count without inspecting those characters. These are the only token types. The pointers preserve source order, so reaching both ends witnesses a complete expansion equal to the word; every rejection corresponds to a violated rule.

#### Complexity detail

Each of the `w` word positions is advanced over at most once, and each of the `a` abbreviation characters is parsed once, for $O(w + a)$ time. Numeric accumulators and pointers use $O(1)$ space.

#### Alternatives and edge cases

- **Expand skipped positions into wildcard text:** can validate afterward but allocates $O(w)$ additional storage.
- **Consume strings through front slicing:** is logically correct but repeatedly copies suffixes and can take $O((w + a)^2)$ time.
- **Recursive token matching:** adds call-stack state even though every token has a deterministic effect.
- A number consisting of several digits is one skip count.
- Any numeric token beginning with zero is invalid.
- A skip may end exactly at the word boundary.
- Skipping beyond the word length is invalid.

</details>
