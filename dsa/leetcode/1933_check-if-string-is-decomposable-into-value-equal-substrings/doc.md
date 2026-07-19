# Check if String Is Decomposable Into Value-Equal Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1933 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/) |

## Problem Description
### Goal
A value-equal string contains only copies of one character. Given a digit
string `s`, split the entire string into consecutive, nonempty substrings, each
of which must be value-equal. Every selected character must remain in its
original position because the pieces are substrings, not subsequences.

Exactly one piece in the decomposition must have length two. Every other piece
must have length three; no piece of another length is allowed. Return whether
at least one decomposition satisfying all of these rules exists.

### Function Contract
**Inputs**

- `s`: a string of $N$ digits from `"0"` through `"9"`, where
  $1 \le N \le 1000$.

**Return value**

- `true` if `s` can be decomposed into exactly one value-equal substring of
  length two and any number of value-equal substrings of length three;
  otherwise `false`.

### Examples
**Example 1**

- Input: `s = "000111000"`
- Output: `false`

The natural three groups all have length three, so no required length-two
piece exists.

**Example 2**

- Input: `s = "00011111222"`
- Output: `true`

One valid decomposition is `["000", "111", "11", "222"]`.

**Example 3**

- Input: `s = "011100022233"`
- Output: `false`

The initial one-character run cannot form an allowed piece.
