# Count Pairs Of Similar Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2506 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-of-similar-strings/) |

## Problem Description
### Goal
You are given a 0-indexed array of strings `words`. Two strings are **similar** when the set of characters appearing in one string is exactly the same as the set appearing in the other. Character order and the number of occurrences do not matter; for example, `"abca"` and `"cba"` are similar because both contain only `a`, `b`, and `c`.

Return the number of index pairs `(i, j)` such that $0 \le i < j < n$ and `words[i]` is similar to `words[j]`.

### Function Contract
**Inputs**

- `words`: A list of $n$ nonempty strings containing only lowercase English letters.

The constraints are $1 \le n \le 100$ and $1 \le \lvert\texttt{words[i]}\rvert \le 100$.

**Return value**

An integer equal to the number of similar index pairs.

### Examples
**Example 1**

- Input: `words = ["aba","aabb","abcd","bac","aabc"]`
- Output: `2`
- Explanation: Indices `(0, 1)` both use `{a, b}`, while `(3, 4)` both use `{a, b, c}`.

**Example 2**

- Input: `words = ["aabb","ab","ba"]`
- Output: `3`
- Explanation: Every word has the same character set, so all three index pairs qualify.

**Example 3**

- Input: `words = ["nba","cba","dba"]`
- Output: `0`
- Explanation: The three character sets are different, so there is no similar pair.
