# Longest Chunked Palindrome Decomposition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1147 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Greedy, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) |

## Problem Description

### Goal

Given a string `text`, split it into $k$ non-empty substrings $(t_1,t_2,\ldots,t_k)$. Concatenating the substrings in order must reproduce all of `text`; chunks cannot overlap, omit characters, or change their order.

The sequence of chunks must itself be palindromic: $t_i=t_{k-i+1}$ for every $1 \le i \le k$. Individual chunks do not need to be palindromes, and their lengths may differ from other, nonpaired chunks. Return the largest possible value of $k$ among all decompositions satisfying these conditions.

### Function Contract

**Inputs**

- `text`: a string of length $n$, where $1 \le n \le 1000$.
- `text` consists only of lowercase English characters.

**Return value**

The maximum number of non-empty chunks in a valid chunked palindrome decomposition.

### Examples

**Example 1**

- Input: `text = "ghiabcdefhelloadamhelloabcdefghi"`
- Output: `7`
- Explanation: One maximum decomposition is `(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)`.

**Example 2**

- Input: `text = "merchant"`
- Output: `1`
- Explanation: No proper matching outer chunks exist, so the complete string is the only chunk.

**Example 3**

- Input: `text = "antaprezatepzapreanta"`
- Output: `11`
- Explanation: It can be decomposed as `(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)`.
