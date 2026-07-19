# Longest Word With All Prefixes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1858 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-with-all-prefixes/) |

## Problem Description
### Goal
You are given an array `words` containing lowercase English words. A word is
eligible when every nonempty prefix obtained by taking its first $1, 2, \ldots,
\lvert w \rvert$ characters also occurs as an element of `words`. Thus the word
itself must be present, as must the one-character word that begins its prefix
chain and every intermediate length.

Return the longest eligible word. When several eligible words have the same
maximum length, choose the lexicographically smallest one. If no input word has
all of its required prefixes, return the empty string.

### Function Contract
**Inputs**

- `words`: an array of between $1$ and $10^5$ nonempty strings. Every character
  is a lowercase English letter, each word has length at most $10^5$, and the
  total number of input characters is at most $10^5$.

Define the total input length as

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

A string: the longest word whose every nonempty prefix belongs to `words`,
breaking length ties lexicographically, or `""` if no such word exists.

### Examples
**Example 1**

- Input: `words = ["k","ki","kir","kira","kiran"]`
- Output: `"kiran"`

Every prefix along the chain from `"k"` through `"kiran"` is present.

**Example 2**

- Input: `words = ["a","banana","app","appl","ap","apply","apple"]`
- Output: `"apple"`

Both five-letter words have complete prefix chains, and `"apple"` is
lexicographically smaller than `"apply"`.

**Example 3**

- Input: `words = ["abc","bc","ab","qwe"]`
- Output: `""`

No one-letter word is present, so no word can begin a complete prefix chain.
