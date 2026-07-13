# Word Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 290 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-pattern/) |

## Problem Description
### Goal
Given a character pattern and a string of words separated by single spaces, decide whether the word sequence follows the pattern. Each letter in the pattern must map to exactly one unique word, and each unique word must map to exactly one pattern letter.

The same mapping must hold at every corresponding position: a pattern letter cannot change words later, and two letters cannot share one word. Return `True` only when the number of words equals the pattern length and all positions satisfy both directions of the mapping. A matching prefix with extra pattern characters or extra words is not valid.

### Function Contract
**Inputs**

- `pattern`: a character pattern
- `s`: words separated by single spaces

**Return value**

`True` exactly when equal pattern characters map to equal words and different characters map to different words.

### Examples
**Example 1**

- Input: `pattern = "abba", s = "dog cat cat dog"`
- Output: `true`

**Example 2**

- Input: `pattern = "abba", s = "dog cat cat fish"`
- Output: `false`

**Example 3**

- Input: `pattern = "aaaa", s = "dog cat cat dog"`
- Output: `false`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**A pattern match requires a bijection, not one map**

Split the sentence and reject a length mismatch. For each character-word pair, require any existing character mapping to match the word and any existing word mapping to match the character; otherwise install both mappings.

After every processed position, the two maps are inverses over all character-word pairs seen so far.

**The inverse maps enforce both directions**

A forward conflict would assign two words to one pattern character; a reverse conflict would assign one word to two characters. Rejecting both kinds makes the relation one-to-one and consistent. If every aligned pair passes and the sequence lengths match, the two maps form exactly the required bijection over all positions.

#### Complexity detail

Each of `n` positions performs expected-constant-time hash operations, and at most `k` distinct mappings are stored.

#### Alternatives and edge cases

- **Compare first-occurrence indices by rescanning:** can take $O(n^2)$.
- A word-count mismatch fails immediately; repeating both the character and its word is valid.

</details>
