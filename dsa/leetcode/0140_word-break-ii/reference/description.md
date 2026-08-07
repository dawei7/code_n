## Description

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.
### Function Contract

**Inputs**

- `s`: The string into which spaces must be inserted.
- `wordDict`: The available non-empty dictionary words.

**Return value**

Return every complete dictionary-word sentence obtainable from `s`, in any order.

### Examples
#### Example 1

- **Input:** `s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]`
- **Output:** `["cats and dog","cat sand dog"]`
#### Example 2

- **Input:** `s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]`
- **Output:** `["pine apple pen apple","pineapple pen apple","pine applepen apple"]`
- **Explanation:** Note that you are allowed to reuse a dictionary word.
#### Example 3

- **Input:** `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`
- **Output:** `[]`
### Constraints

- $1 \le \text{s.length} \le 20$

- $1 \le \text{wordDict.length} \le 1000$

- $1 \le \text{wordDict}[i].length \le 10$

- `s` and $\text{wordDict}[i]$ consist of only lowercase English letters.

- All the strings of `wordDict` are **unique**.

- Input is generated in a way that the length of the answer doesn't exceed $10^{5}$.