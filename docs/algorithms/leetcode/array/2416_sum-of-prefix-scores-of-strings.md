# Sum of Prefix Scores of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2416 |
| Difficulty | Hard |
| Topics | Array, String, Trie, Counting |
| Official Link | [sum-of-prefix-scores-of-strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/) |

## Problem Description & Examples
### Goal
Given an array of strings, calculate the "score" for each string. The score of a string is defined as the sum of the counts of all its prefixes that appear as a prefix in any of the strings within the input array.

### Function Contract
**Inputs**

- `words`: A list of strings (`List[str]`) consisting of lowercase English letters.

**Return value**

- A list of integers (`List[int]`) where the $i$-th element represents the total prefix score of `words[i]`.

### Examples
**Example 1**

- Input: `words = ["abc","ab","bc","b"]`
- Output: `[5,4,3,2]`
- Explanation: 
  - "abc": prefixes "a" (1), "ab" (2), "abc" (1). Sum = 1+2+1 = 4. Wait, "b" is also a prefix of "bc" and "b". Let's re-evaluate: "a" appears in "abc", "ab" (2). "ab" appears in "abc", "ab" (2). "abc" appears in "abc" (1). Total = 5.

**Example 2**

- Input: `words = ["abcd"]`
- Output: `[4]`

**Example 3**

- Input: `words = ["z","x","y"]`
- Output: `[1,1,1]`

---

## Underlying Base Algorithm(s)
The problem is best solved using a **Trie (Prefix Tree)** data structure. Each node in the Trie will store a `count` representing how many strings in the input array pass through that specific node (i.e., share that prefix). By inserting all strings into the Trie and incrementing the `count` at each node visited, we can subsequently traverse the Trie for each word to sum the counts of its constituent prefixes.

---

## Complexity Analysis
- **Time Complexity**: $O(\sum |words[i]|)$, where $\sum |words[i]|$ is the total number of characters across all strings. We perform one pass to build the Trie and one pass to calculate scores.
- **Space Complexity**: $O(\sum |words[i]| \times \Sigma)$, where $\Sigma$ is the alphabet size (26). In the worst case, every character of every string creates a new node in the Trie.
