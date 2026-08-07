## Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.
### Function Contract

**Inputs**

- `s`: The string to segment.
- `wordDict`: The available non-empty dictionary words.

**Return value**

Return `true` if a complete dictionary-word segmentation exists; otherwise return `false`.

### Examples
#### Example 1

- **Input:** `s = "leetcode", wordDict = ["leet","code"]`
- **Output:** `true`
- **Explanation:** Return true because "leetcode" can be segmented as "leet code".
#### Example 2

- **Input:** `s = "applepenapple", wordDict = ["apple","pen"]`
- **Output:** `true`
- **Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
#### Example 3

- **Input:** `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`
- **Output:** `false`
### Constraints

- $1 \le \text{s.length} \le 300$

- $1 \le \text{wordDict.length} \le 1000$

- $1 \le \text{wordDict}[i].length \le 20$

- `s` and $\text{wordDict}[i]$ consist of only lowercase English letters.

- All the strings of `wordDict` are **unique**.