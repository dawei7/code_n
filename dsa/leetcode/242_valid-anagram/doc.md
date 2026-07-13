# Valid Anagram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 242 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-anagram/) |

## Problem Description
### Goal
Given two strings `s` and `t` made from lowercase English letters, determine whether `t` is an anagram of `s`. An anagram may reorder characters arbitrarily but must use exactly the characters supplied by the original string.

Return `True` only when both strings have the same length and every letter occurs with the same multiplicity in each one. Matching sets of letters are insufficient when their counts differ, and no character may be added, deleted, or substituted. A one-character string is an anagram only of the same character, while a length mismatch immediately makes the answer `False`.

### Function Contract
**Inputs**

- `s`: a lowercase English string
- `t`: another lowercase English string

**Return value**

`True` when `t` is an anagram of `s`; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "anagram", t = "nagaram"`
- Output: `True`

**Example 2**

- Input: `s = "rat", t = "car"`
- Output: `False`

**Example 3**

- Input: `s = "", t = ""`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Unequal lengths fail before counting**

Anagrams use every character exactly once, so different lengths cannot match.

**Track the net balance of each lowercase letter**

Use 26 counters. Increment for each character of `s` and decrement for the aligned character of `t`. All counters must finish at zero.

After processing a prefix of both strings, each counter equals that letter's occurrences in the processed part of `s` minus its occurrences in the processed part of `t`.

**A zero balance vector is exactly the anagram condition**

If every final counter is zero, both strings contain each lowercase letter equally often, so one can be rearranged into the other. If any counter is nonzero, that letter occurs a different number of times and no rearrangement can repair the mismatch.

#### Complexity detail

The strings are scanned once, giving $O(n)$ time. The 26-entry counter array is fixed-size, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sorting both strings:** is concise but costs $O(n \log n)$.
- **General hash maps:** support arbitrary characters but use alphabet-dependent space.
- Empty strings are anagrams; equal character sets with different counts are not.

</details>
