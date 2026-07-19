# Find and Replace Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 890 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/find-and-replace-pattern/) |

## Problem Description
### Goal
Given a list of lowercase strings `words` and a lowercase string `pattern`, identify every word that can be produced by consistently replacing the letters of `pattern`.

The replacement must be a permutation of letters: each pattern letter maps to one letter, the same source letter is replaced consistently, and two distinct source letters cannot map to the same destination letter. Return all matching words in any order.

### Function Contract
Let $N=\lvert\texttt{words}\rvert$ and $L=\lvert\texttt{pattern}\rvert$.

**Inputs**

- `words`: $N$ lowercase English words, where $1 \leq N \leq 50$ and every word has length $L$.
- `pattern`: a lowercase English string, where $1 \leq L \leq 20$.

**Return value**

Return every word that has a bijective letter mapping from `pattern`; the result order is unrestricted.

### Examples
**Example 1**

- Input: `words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"`
- Output: `["mee","aqq"]`

`ccc` fails because two distinct pattern letters would both have to map to `c`.

**Example 2**

- Input: `words = ["a","b","c"], pattern = "a"`
- Output: `["a","b","c"]`

**Example 3**

- Input: `words = ["aa","ab","cc","cd"], pattern = "xy"`
- Output: `["ab","cd"]`
