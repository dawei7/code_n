# Greatest English Letter in Upper and Lower Case

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2309 |
| Difficulty | Easy |
| Topics | Hash Table, String, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) |

## Problem Description
### Goal
Given a string `s` of English letters, find the alphabetically greatest letter
that occurs in both lowercase and uppercase somewhere in the string.

Return that letter in uppercase. If no alphabet letter has both forms present,
return the empty string. One letter is greater than another when it appears
later in the English alphabet. Occurrence order and repetition counts do not
affect which qualifying letter is greatest.

### Function Contract
**Inputs**

- `s`: A string of lowercase and uppercase English letters.

The contract guarantees $1\le\lvert\texttt{s}\rvert\le1000$.

**Return value**

The uppercase form of the greatest letter whose two cases both occur, or `""`
when no such letter exists.

### Examples
**Example 1**

- Input: `s = "lEeTcOdE"`
- Output: `"E"`
- Explanation: `e` and `E` are both present, and no greater letter has both
  cases.

**Example 2**

- Input: `s = "arRAzFif"`
- Output: `"R"`
- Explanation: `A`, `F`, and `R` qualify; `R` is greatest.

**Example 3**

- Input: `s = "AbCdEfGhIjK"`
- Output: `""`
- Explanation: No letter occurs in both cases.
