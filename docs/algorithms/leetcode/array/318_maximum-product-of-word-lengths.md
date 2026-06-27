# Maximum Product of Word Lengths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 318 |
| Difficulty | Medium |
| Topics | Array, String, Bit Manipulation |
| Official Link | [maximum-product-of-word-lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) |

## Problem Description & Examples
### Goal
Given a list of strings, identify two strings that do not share any common characters. Among all such pairs, calculate the maximum possible product of their lengths. If no such pair exists, return zero.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the maximum product of the lengths of two words that share no common characters.

### Examples
**Example 1**

- Input: `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`
- Output: `16`
- Explanation: The two words are "abcw" and "xtfn".

**Example 2**

- Input: `words = ["a","ab","abc","d","cd","bcd","abcd"]`
- Output: `4`
- Explanation: The two words are "ab" and "cd".

**Example 3**

- Input: `words = ["a","aa","aaa","aaaa"]`
- Output: `0`
- Explanation: No two words share no common characters.

---

## Underlying Base Algorithm(s)
The problem is solved using **Bit Manipulation**. Since there are only 26 lowercase English letters, each word can be represented as a 32-bit integer (a bitmask), where the $i$-th bit is set to 1 if the $i$-th letter of the alphabet is present in the word. Two words share no common characters if and only if the bitwise AND of their masks is 0.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L + N^2)$, where $N$ is the number of words and $L$ is the average length of a word. We iterate through all words to build masks ($O(N \cdot L)$) and then compare all pairs ($O(N^2)$).
- **Space Complexity**: $O(N)$ to store the bitmask representation for each word.
