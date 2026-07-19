# Decoded String at Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 880 |
| Difficulty | Medium |
| Topics | String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/decoded-string-at-index/) |

## Problem Description
### Goal
Read the encoded string `s` from left to right to form a tape. A lowercase letter is appended to the current tape. A digit `d` writes the entire current tape another `d - 1` times, so the tape becomes `d` consecutive copies of what it was before the digit.

Given a one-based position `k`, return the letter occupying that position in the fully decoded tape. The decoded string may be enormously larger than the encoding and should not need to be constructed.

### Function Contract
**Inputs**

- `s`: an encoded string of length $q$, where $2 \leq q \leq 100$. It begins with a lowercase English letter, and every other character is a lowercase letter or a digit from `2` through `9`.
- `k`: a one-based decoded position, where $1 \leq \texttt{k} \leq 10^9$ and the decoded tape has at least `k` letters.
- The complete decoded length is guaranteed to be less than $2^{63}$.

**Return value**

Return the single lowercase letter at one-based position `k` in the decoded tape.

### Examples
**Example 1**

- Input: `s = "leet2code3", k = 10`
- Output: `"o"`

The tape is `"leetleetcodeleetleetcodeleetleetcode"`.

**Example 2**

- Input: `s = "ha22", k = 5`
- Output: `"h"`

The tape is `"hahahaha"`.

**Example 3**

- Input: `s = "a2345678999999999999999", k = 1`
- Output: `"a"`

The tape contains only repetitions of `"a"`, even though its total length is enormous.
