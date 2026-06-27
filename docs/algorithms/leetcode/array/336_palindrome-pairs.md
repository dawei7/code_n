# Palindrome Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 336 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Trie, Hash Function |
| Official Link | [palindrome-pairs](https://leetcode.com/problems/palindrome-pairs/) |

## Problem Description & Examples
### Goal
Given a collection of unique strings, identify all distinct pairs of indices `(i, j)` such that the concatenation of the strings at these indices, `words[i] + words[j]`, forms a valid palindrome.

### Function Contract
**Inputs**

- `words`: A list of unique strings consisting of lowercase English letters.

**Return value**

- A list of lists, where each inner list contains two integers representing the indices `[i, j]` that satisfy the palindrome condition.

### Examples
**Example 1**

- Input: `words = ["abcd","dcba","lls","s","sssll"]`
- Output: `[[0,1],[1,0],[3,2],[2,4]]`

**Example 2**

- Input: `words = ["bat","tab","cat"]`
- Output: `[[0,1],[1,0]]`

**Example 3**

- Input: `words = ["a",""]`
- Output: `[[0,1],[1,0]]`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes a Hash Map (dictionary) to store the indices of all words for $O(1)$ lookup. For each word, we split it into two parts at every possible position. If the left part is a palindrome, we check if the reverse of the right part exists in our map. If the right part is a palindrome, we check if the reverse of the left part exists. This covers all cases where one word is a prefix or suffix of the other to form a palindrome.

---

## Complexity Analysis
- **Time Complexity**: $O(n \cdot k^2)$, where $n$ is the number of words and $k$ is the maximum length of a word. We iterate through each word ($n$) and perform string slicing and palindrome checking for each character position ($k^2$).
- **Space Complexity**: $O(n \cdot k)$ to store the words in the hash map.
