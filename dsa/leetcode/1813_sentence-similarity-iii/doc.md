# Sentence Similarity III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1813 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sentence-similarity-iii](https://leetcode.com/problems/sentence-similarity-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sentence-similarity-iii/).

### Goal
Two sentences are similar if one can become the other by inserting an arbitrary sentence into a single position. Determine whether two given sentences are similar under that rule.

### Function Contract
**Inputs**

- `sentence1`: the first sentence.
- `sentence2`: the second sentence.

**Return value**

Return `True` if the sentences are similar, otherwise `False`.

### Examples
**Example 1**

- Input: `sentence1 = "My name is Haley", sentence2 = "My Haley"`
- Output: `True`

**Example 2**

- Input: `sentence1 = "of", sentence2 = "A lot of words"`
- Output: `False`

**Example 3**

- Input: `sentence1 = "Eating right now", sentence2 = "Eating"`
- Output: `True`

---

## Solution
### Approach
Split both sentences into word arrays and make the shorter one the target to match. Count matching words from the front, then matching words from the back without crossing the unmatched middle. The sentences are similar if every word of the shorter sentence is covered by the matching prefix and suffix.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)` for split words

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
