# Minimize String Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2716 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimize-string-length/) |

## Problem Description

### Goal

Given a lowercase English string `s`, an operation chooses an index $i$ and uses the character currently stored there. One permitted form deletes the closest equal character strictly to the left of $i$, if one exists. The other deletes the closest equal character strictly to the right, if one exists.

Apply either operation any number of times, including zero times, to make the remaining string as short as possible. Deleting a character closes the gap and changes subsequent indices, but it does not change the relative order or identity of the other characters. Return the minimum achievable length.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 100$, containing only lowercase English letters.

**Return value**

Return the smallest possible number of characters remaining after valid deletions.

### Examples

#### Example 1

- **Input:** `s = "aaabc"`
- **Output:** `3`
- **Explanation:** Two copies of `'a'` can be deleted, leaving one each of `'a'`, `'b'`, and `'c'`.

#### Example 2

- **Input:** `s = "cbbd"`
- **Output:** `3`
- **Explanation:** Delete either copy of `'b'`; the three distinct characters cannot be reduced further.

#### Example 3

- **Input:** `s = "baadccab"`
- **Output:** `4`
- **Explanation:** Repeated operations can leave exactly one occurrence of each of `'a'`, `'b'`, `'c'`, and `'d'`.
