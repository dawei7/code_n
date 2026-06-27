# Palindrome Rearrangement Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2983 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Prefix Sum |
| Official Link | [palindrome-rearrangement-queries](https://leetcode.com/problems/palindrome-rearrangement-queries/) |

## Problem Description & Examples
### Goal
Given a string `s` of even length, determine if a series of independent queries can result in a palindrome. Each query specifies two substrings in the first and second halves of the string. You must determine if swapping characters within these specified ranges allows the entire string to form a palindrome, assuming the rest of the string remains fixed.

### Function Contract
**Inputs**

- `s` (str): An even-length string consisting of lowercase English letters.
- `queries` (List[List[int]]): A list of queries, where each query `[a, b, c, d]` represents swapping characters between `s[a...b]` and `s[c...d]`.

**Return value**

- `List[bool]`: A list of booleans where each index corresponds to whether the $i$-th query allows the string to become a palindrome.

### Examples
**Example 1**

- Input: `s = "abcabc", queries = [[0,0,5,5],[1,1,4,4]]`
- Output: `[true, false]`

**Example 2**

- Input: `s = "abbcdecbba", queries = [[0,2,7,9]]`
- Output: `[true]`

**Example 3**

- Input: `s = "acbcab", queries = [[1,2,4,5]]`
- Output: `[true]`

---

## Underlying Base Algorithm(s)
The solution relies on **Prefix Sums** (or frequency arrays) to track character counts in both halves of the string. Since a palindrome requires the first half to be the reverse of the second half, we compare the character frequencies of the fixed parts of the string against the modified parts. We use a prefix sum array to calculate character counts in $O(1)$ time for any range, allowing us to verify if the remaining segments match the required palindrome symmetry.

---

## Complexity Analysis
- **Time Complexity**: $O(n + q)$, where $n$ is the length of the string and $q$ is the number of queries. Precomputing prefix sums takes $O(n)$, and each query is processed in $O(1)$ (or $O(26)$ for alphabet size).
- **Space Complexity**: $O(n)$, required to store the prefix sum frequency table of size $n \times 26$.
