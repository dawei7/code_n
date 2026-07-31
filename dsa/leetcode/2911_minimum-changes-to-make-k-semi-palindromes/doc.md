# Minimum Changes to Make K Semi-palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2911 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/) |

## Problem Description
### Goal
Partition the lowercase string `s` into exactly $k$ nonempty contiguous substrings. Characters may be replaced, and the objective is to minimize the total number of replacements needed to turn every part into a semi-palindrome.

A string of length $L$ is a semi-palindrome when there is a positive proper divisor $d$ of $L$. For each residue $r$ from $0$ through $d-1$, read the characters at offsets $r,r+d,r+2d,\ldots$ within the string. Every one of these $d$ interleaved sequences must be a palindrome. The divisor must be smaller than $L$, so a one-character string is never a valid part. For example, `"abcabc"` is a semi-palindrome with $d=3$ because its interleaved sequences are `"aa"`, `"bb"`, and `"cc"`.

### Function Contract
**Inputs**

- `s`: A string of length $n$ containing only lowercase English letters, where $2\le n\le 200$.
- `k`: The exact number of contiguous parts, where $1\le k\le\lfloor n/2\rfloor$.

**Return value**

Return the minimum total number of character replacements required to make all $k$ parts semi-palindromes.

### Examples
**Example 1**

- Input: `s = "abcac", k = 2`
- Output: `1`
- Explanation: Split into `"ab"` and `"cac"`. Replacing one character makes the first part a palindrome for $d=1$; the second already qualifies.

**Example 2**

- Input: `s = "abcdef", k = 2`
- Output: `2`
- Explanation: Splitting into `"abc"` and `"def"` requires one replacement in each part.

**Example 3**

- Input: `s = "aabbaa", k = 3`
- Output: `0`
- Explanation: The parts `"aa"`, `"bb"`, and `"aa"` are already semi-palindromes.
