## Problem Description & Examples
### Goal
Given a string `s` and a dictionary of strings `word_dict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

### Function Contract
**Inputs**

- `s`: str
- `word_dict`: List[str]

**Return value**

bool - True if partition exists

### Examples
**Example 1**

- Input: `s = "leetcode", word_dict = ["leet", "code"]`
- Output: `True`

**Example 2**

- Input: `s = 'leetcode', word_dict = ['leet', 'code', 'apple', 'pen']`
- Output: `True`

**Example 3**

- Input: `s = 'applepenapple', word_dict = ['leet', 'code', 'apple', 'pen']`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
