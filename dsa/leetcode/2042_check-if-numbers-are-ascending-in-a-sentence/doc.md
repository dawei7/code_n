# Check if Numbers Are Ascending in a Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2042 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/) |

## Problem Description

### Goal

A sentence consists of tokens separated by single spaces, with no space at
either end. Every token is either a lowercase English word or the decimal
representation of a positive integer. Numeric tokens have no leading zeros.

Read only the numeric tokens from left to right, ignoring the words. Return
whether every number is strictly smaller than the next numeric token in the
sentence. Equality does not count as increasing.

### Function Contract

Let $L$ be the length of `s`.

**Inputs**

- `s`: a valid sentence with $3 \le L \le 200$, between `2` and `100` tokens,
  and at least two numeric tokens.
- Every numeric token represents an integer from $1$ through $99$.

**Return value**

- `true` when the numeric tokens are strictly increasing from left to right;
  otherwise `false`.

### Examples

**Example 1**

- Input: `s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"`
- Output: `true`
- Explanation: The numeric sequence is `1, 3, 4, 6, 12`.

**Example 2**

- Input: `s = "hello world 5 x 5"`
- Output: `false`
- Explanation: Equal consecutive numeric values are not strictly increasing.

**Example 3**

- Input: `s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"`
- Output: `false`
- Explanation: The numeric sequence decreases from `51` to `50`.
