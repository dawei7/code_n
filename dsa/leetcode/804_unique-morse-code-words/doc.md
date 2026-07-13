# Unique Morse Code Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 804 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-morse-code-words/) |

## Problem Description

### Goal

International Morse Code maps each lowercase English letter to its fixed sequence of dots and dashes. Transform a word by replacing every letter with that code and concatenating the pieces without separators.

Given an array `words`, return the number of distinct Morse transformations produced. Different words can have the same concatenated representation and then count only once, while repeated input words do not create additional distinct transformations.

### Function Contract

**Inputs**

- `words`: a nonempty list of lowercase English words.

**Return value**

- The number of distinct Morse-code strings produced by the words.

### Examples

**Example 1**

- Input: `words = ["gin","zen","gig","msg"]`
- Output: `2`
- Explanation: `gin` and `zen` share one transformation, while `gig` and `msg` share another.

**Example 2**

- Input: `words = ["a","et"]`
- Output: `1`
- Explanation: Both words concatenate to `.-` because transformation boundaries do not preserve letter separators.

**Example 3**

- Input: `words = ["abc","def","ghi"]`
- Output: `3`
- Explanation: The three resulting Morse strings are different.

### Required Complexity

- **Time:** $O(c)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**Map letters by alphabet index**

Store the 26 prescribed Morse codes in alphabet order. For each character, subtract the code point of `a` to select its Morse fragment. Concatenate the fragments for a word without separators, exactly matching the transformation rule.

**Deduplicate complete transformations**

Insert every completed Morse string into a hash set. Equal transformations collapse to one entry even when they came from different spellings; unequal strings occupy distinct entries. The final set size is therefore exactly the requested count.

Every character is replaced by its unique prescribed fragment in its original order, so the constructed string is the word's required transformation. Set membership identifies equality of those entire strings and no other property, making the number of stored keys precisely the number of distinct transformations.

#### Complexity detail

Let `c` be the total number of letters across all words. Each letter contributes a constant-length Morse fragment, so constructing and hashing all transformations takes $O(c)$ expected time. The set and its stored transformation strings use $O(c)$ space in the worst case.

#### Alternatives and edge cases

- **Sort transformations:** Build all encoded strings, sort them, and count adjacent changes; this uses $O(c + w \log w)$ time for `w` words.
- **Compare against a list:** Linearly checking every prior distinct transformation is correct but can require $O(w^2)$ comparisons.
- **Trie of dots and dashes:** A trie can share prefixes but is unnecessary when hashing complete strings is direct.
- **Duplicate input words:** They necessarily produce one shared transformation and do not increase the count.
- **Different words may collide:** Letter boundaries are omitted, so strings such as `a` and `et` can encode identically.
- **Single word:** Exactly one transformation exists.
- **No separators:** Adding delimiters between letter codes would change the required equivalence relation.

</details>
