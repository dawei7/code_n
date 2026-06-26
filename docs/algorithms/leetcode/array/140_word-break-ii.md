# Word Break II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_138` |
| Frontend ID | 140 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization |
| Official Link | [word-break-ii](https://leetcode.com/problems/word-break-ii/) |

## Problem Description & Examples
### Goal
Given a string `s` and a dictionary of strings `word_dict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order. Note that the same word in the dictionary may be reused multiple times in the segmentation.

### Function Contract
**Inputs**

- `s`: str
- `word_dict`: List[str]

**Return value**

List[str] - all valid sentences

### Examples
**Example 1**

- Input: `s = "catsanddog", word_dict = ["cat", "cats", "and", "sand", "dog"]`
- Output: `["cats and dog", "cat sand dog"]`

**Example 2**

- Input: `s = 'catsanddog', word_dict = ['cat', 'cats', 'and', 'sand', 'dog', 'catsanddog']`
- Output: `['cat sand dog', 'cats and dog', 'catsanddog']`

**Example 3**

- Input: `s = 'catsanddogdog', word_dict = ['cat', 'cats', 'and', 'sand', 'dog', 'catsanddog']`
- Output: `['cat sand dog dog', 'cats and dog dog', 'catsanddog dog']`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
