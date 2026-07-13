# Maximum Number of Words Found in Sentences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2114 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-words-found-in-sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/).

### Goal
Find the sentence containing the most space-separated words.

### Function Contract
**Inputs**

- `sentences`: an array of non-empty sentences.

**Return value**

Return the maximum word count among the sentences.

### Examples
**Example 1**

- Input: `sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]`
- Output: `6`

**Example 2**

- Input: `sentences = ["please wait","continue to fight","continue to win"]`
- Output: `3`

**Example 3**

- Input: `sentences = ["one"]`
- Output: `1`

---

## Solution
### Approach
For each sentence, the word count is one plus the number of spaces. Return the maximum count.

### Complexity Analysis
- **Time Complexity**: `O(total characters)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
