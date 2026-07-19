# Number of Valid Words in a Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2047 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-valid-words-in-a-sentence/) |

## Problem Description

### Goal

A sentence contains lowercase letters, digits, spaces, hyphens, and the
punctuation marks `"!"`, `"."`, and `","`. One or more spaces separate its
nonempty tokens.

Count the tokens that form valid words. A valid token contains no digit, uses
at most one hyphen and only between two lowercase letters, and uses at most one
punctuation mark and only as its final character. A punctuation mark alone is
valid. Every rule must hold simultaneously; invalid tokens are ignored rather
than making the entire sentence invalid.

### Function Contract

Let $L$ be the sentence length.

**Inputs**

- `sentence`: a string with $1 \le L \le 1000$, containing only lowercase
  letters, digits, spaces, hyphens, and `"!"`, `"."`, or `","`.
- At least one nonempty token is present; tokens may be separated by multiple
  spaces.

**Return value**

- The number of tokens satisfying all valid-word rules.

### Examples

**Example 1**

- Input: `sentence = "cat and  dog"`
- Output: `3`

**Example 2**

- Input: `sentence = "!this  1-s b8d!"`
- Output: `0`
- Explanation: The first token has misplaced punctuation, while the other two
  contain digits.

**Example 3**

- Input: `sentence = "alice and  bob are playing stone-game10"`
- Output: `5`
- Explanation: The first five words are valid; the final token contains digits.
