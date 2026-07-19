# Repeated DNA Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 187 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/repeated-dna-sequences/) |

## Problem Description
### Goal
Given a DNA string containing only the nucleotides `A`, `C`, `G`, and `T`, examine every contiguous substring of exactly ten characters. Occurrences may overlap, so moving the start position by one can create another instance of the same sequence.

Return each ten-character sequence that appears at least twice, listing a repeated sequence only once no matter how many occurrences it has. The answer may be returned in any order. Strings shorter than ten characters contain no candidate window, and a sequence appearing exactly once is excluded. The task concerns contiguous substrings, not subsequences formed by skipping characters.

### Function Contract
**Inputs**

- `s`: a string over `A`, `C`, `G`, and `T`

**Return value**

A list containing each repeated length-10 sequence once, in any order.

### Examples
**Example 1**

- Input: `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`
- Output: `"AAAAACCCCC"`, `"CCCCCAAAAA"`

**Example 2**

- Input: `"AAAAAAAAAAAAA"`
- Output: `"AAAAAAAAAA"`

**Example 3**

- Input length below 10
- Output: `[]`
