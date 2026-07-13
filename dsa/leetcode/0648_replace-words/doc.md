# Replace Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 648 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-words/) |

## Problem Description
### Goal
In English, a root can be followed by additional letters to form a longer derivative. Given a dictionary of roots and a sentence whose words are separated by spaces, replace each derivative by a dictionary root that forms its prefix.

If more than one root can replace the same word, use the root with the shortest length. Leave a word unchanged when no dictionary root is its prefix, preserve the original word order, and return the transformed sentence with its single-space separation intact.

### Function Contract
**Inputs**

- `dictionary`: a list of lowercase root words
- `sentence`: lowercase words separated by single spaces

**Return value**

- The transformed sentence with original word order and single-space separation
- If several roots prefix the same word, the shortest root must be used

### Examples
**Example 1**

- Input: `dictionary = ["cat","bat","rat"]`, `sentence = "the cattle was rattled by the battery"`
- Output: `"the cat was rat by the bat"`

**Example 2**

- Input: `dictionary = ["a","b","c"]`, `sentence = "aadsfasf absbs bbab cadsfafs"`
- Output: `"a a b c"`

**Example 3**

- Input: `dictionary = ["c","cat"]`, `sentence = "cattle"`
- Output: `"c"`

### Required Complexity

- **Time:** $O(D + S)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Store dictionary paths in a trie**

Insert every root character by character and mark its final node. Shared prefixes share nodes, so looking up a word follows all possible root prefixes simultaneously rather than testing dictionary entries independently.

**Stop at the first terminal node**

Scan a sentence word from its first character through the trie. If the next edge is absent, no dictionary root can prefix the word and the original word remains. If a terminal node is reached, return the characters consumed so far immediately.

**Why the first terminal is the required root**

Trie depth equals prefix length. The traversal visits possible root endings in strictly increasing length order, so the first terminal is the shortest matching root. Any later terminal would represent a longer prefix and cannot be preferred.

**Transform words independently**

Split the sentence into words, apply the trie lookup to each, and join the replacements with spaces. Prefix decisions do not interact across word boundaries, so preserving order and spacing completes the sentence contract.

#### Complexity detail

Let `D` be the total number of characters in all dictionary roots and `S` the total number of sentence characters. Trie construction costs $O(D)$. Each sentence character is examined at most once before a match or mismatch, for $O(S)$ replacement time and $O(D + S)$ total time. Trie nodes use $O(D)$ space; the returned sentence occupies output space.

#### Alternatives and edge cases

- **Hash set of roots:** test each increasing prefix of a word for membership; it is simple and has similar logical work, though substring creation can add overhead.
- **Scan every dictionary root:** test roots in increasing length for every word; it is correct but can take $O(WD)$ work across `W` sentence words.
- **Sort roots and binary-search prefixes:** reduces some searching but makes prefix-range handling more complicated than trie traversal.
- A word equal to a root remains textually unchanged.
- Duplicate dictionary roots do not affect the result.
- When one root prefixes another, the shorter root always wins.
- Words with no matching first-character edge remain unchanged immediately.
- Replacement applies separately to every occurrence of a word.

</details>
