# Rearrange Characters to Make Target String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2287 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-characters-to-make-target-string/) |

## Problem Description
### Goal
Two 0-indexed strings, `s` and `target`, contain lowercase English letters.
Letters may be taken from `s` and rearranged to form copies of `target`.
Each occurrence in `s` can be used at most once, but unused letters do not
matter.

Return the maximum number of complete copies of `target` that can be assembled
simultaneously. Because rearrangement is allowed, only the available and
required frequency of each letter affects the answer; the original positions
do not.

### Function Contract
**Inputs**

- `s`: The source string whose individual letter occurrences may be consumed.
- `target`: The nonempty string to reproduce as many times as possible.

Both strings contain only lowercase English letters, with
$1 \le \lvert\texttt{s}\rvert \le 100$ and
$1 \le \lvert\texttt{target}\rvert \le 10$. Let
$S = \lvert\texttt{s}\rvert$ and $T = \lvert\texttt{target}\rvert$.

**Return value**

The greatest nonnegative integer number of complete copies of `target` that
the letters of `s` can form without reusing an occurrence.

### Examples
**Example 1**

- Input: `s = "ilovecodingonleetcode"`, `target = "code"`
- Output: `2`

**Example 2**

- Input: `s = "abcba"`, `target = "abc"`
- Output: `1`

**Example 3**

- Input: `s = "abbaccaddaeea"`, `target = "aaaaa"`
- Output: `1`
