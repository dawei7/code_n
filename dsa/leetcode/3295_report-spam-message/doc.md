# Report Spam Message

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3295 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/report-spam-message/) |

## Problem Description

### Goal

You are given a sequence of lowercase words in `message` and another sequence `bannedWords`. A message word is a match when it is exactly equal to any banned word; partial, prefix, or substring matches do not count.

The message is spam when at least two of its word positions are matches. The two positions may contain the same word, so distinct banned values are not required. Return `true` for spam and `false` when fewer than two message words match.

### Function Contract

**Inputs**

- `message`: A list of lowercase English words to inspect.
- `bannedWords`: A list of lowercase English words defining exact banned matches.

Each list contains from 1 through $10^5$ words, and every word has length from 1 through 15.

**Return value**

- `true` when at least two positions in `message` contain banned words; otherwise `false`.

### Examples

**Example 1**

- Input: `message = ["hello","world","leetcode"]`, `bannedWords = ["world","hello"]`
- Output: `true`
- Explanation: Both `"hello"` and `"world"` are exact banned matches.

**Example 2**

- Input: `message = ["hello","programming","fun"]`, `bannedWords = ["world","programming","leetcode"]`
- Output: `false`
- Explanation: Only `"programming"` matches.
