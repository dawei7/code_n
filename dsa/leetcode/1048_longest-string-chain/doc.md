# Longest String Chain

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-string-chain/) |

## Problem Description

### Goal

The array `words` contains lowercase English words. A word $A$ is a **predecessor** of a word $B$ if and only if inserting exactly one letter anywhere in $A$, without changing the order of its existing characters, produces $B$. For example, `"abc"` precedes `"abac"`, but `"cba"` does not precede `"bcad"`.

A **word chain** is a sequence of one or more chosen words in which each word is a predecessor of the next. A single word is a valid chain of length one. Return the greatest possible number of words in a chain built from `words`.

### Function Contract

**Inputs**

- `words`: $W$ lowercase English words, where $1 \le W \le 1000$ and every word has length from $1$ through $L$, with $L \le 16$.

**Return value**

- The maximum length of a word chain whose members are selected from `words`.

### Examples

**Example 1**

- Input: `words = ["a","b","ba","bca","bda","bdca"]`
- Output: `4`
- Explanation: One longest chain is `["a","ba","bda","bdca"]`.

**Example 2**

- Input: `words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]`
- Output: `5`
- Explanation: All five words form `["xb","xbc","cxbc","pcxbc","pcxbcf"]`.

**Example 3**

- Input: `words = ["abcd","dbqca"]`
- Output: `1`
- Explanation: The second word cannot be formed from the first while preserving character order, so only trivial one-word chains exist.
