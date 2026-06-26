# Count Pairs Of Similar Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2506 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Official Link | [count-pairs-of-similar-strings](https://leetcode.com/problems/count-pairs-of-similar-strings/) |

## Problem Description & Examples
### Goal
Determine the number of pairs of indices `(i, j)` such that `i < j` and the strings at these indices consist of the exact same set of unique characters.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the total count of pairs `(i, j)` where `i < j` and `words[i]` is "similar" to `words[j]`.

### Examples
**Example 1**

- Input: `words = ["aba","aabb","abcd","bac","aabc"]`
- Output: `2`

**Example 2**

- Input: `words = ["aabb","ab","ba"]`
- Output: `3`

**Example 3**

- Input: `words = ["nba","cyp","ocm"]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem relies on **canonical representation** of sets. Since the order and frequency of characters do not matter, we can represent each string by the set of unique characters it contains. This can be implemented efficiently using a **bitmask** (where the $k$-th bit represents the presence of the $k$-th letter of the alphabet) or by sorting the unique characters of the string. Using a **Hash Map (Frequency Table)** allows us to count occurrences of each canonical form in linear time.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot K)$, where $N$ is the number of words and $K$ is the maximum length of a word. We iterate through each word once and process its characters to build a set or bitmask.
- **Space Complexity**: $O(N)$, as we store the frequency of each unique canonical representation in a hash map.
