# Count Prefix and Suffix Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3045 |
| Difficulty | Hard |
| Topics | Array, String, Trie, Rolling Hash, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/) |

## Problem Description
### Goal
You are given a 0-indexed array of lowercase strings named `words`. Define `isPrefixAndSuffix(str1, str2)` to be true exactly when `str1` is both a prefix and a suffix of `str2`.

For example, `isPrefixAndSuffix("aba", "ababa")` is true because `"ababa"` begins and ends with `"aba"`. In contrast, `isPrefixAndSuffix("abc", "abcd")` is false because the second string does not end with the first.

Return the number of index pairs `(i, j)` for which $i<j$ and `isPrefixAndSuffix(words[i], words[j])` is true. Equal strings at different indices qualify. The input may contain many long words, so enumerating all index pairs is not feasible.

### Function Contract
Let $n=\lvert\texttt{words}\rvert$ and define the total input length

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

**Inputs**

- `words`: An array of $n$ nonempty strings containing only lowercase English letters.

The constraints are $1\le n\le10^5$, every word has length at most $10^5$, and $S\le5\cdot10^5$.

**Return value**

Return the number of ordered index pairs `(i, j)` with $i<j$ for which `words[i]` is simultaneously a prefix and a suffix of `words[j]`.

### Examples
**Example 1**

- Input: `words = ["a","aba","ababa","aa"]`
- Output: `4`
- Explanation: The valid pairs are `(0,1)`, `(0,2)`, `(0,3)`, and `(1,2)`.

**Example 2**

- Input: `words = ["pa","papa","ma","mama"]`
- Output: `2`
- Explanation: The valid pairs are `(0,1)` and `(2,3)`.

**Example 3**

- Input: `words = ["abab","ab"]`
- Output: `0`
- Explanation: The earlier word is longer than the later word and cannot be its prefix or suffix.
