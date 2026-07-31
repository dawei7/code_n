# Circular Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2490 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/circular-sentence/) |

## Problem Description

### Goal

A sentence consists of one or more words made only from uppercase and lowercase English letters. Consecutive words are separated by exactly one space, with no space before the first word or after the last word. Letter comparisons are case-sensitive.

Determine whether the sentence is circular. For every neighboring pair of words, the final character of the earlier word must equal the first character of the later word. The same rule must also close the cycle: the final character of the last word must equal the first character of the first word.

### Function Contract

**Inputs**

- `sentence`: A valid nonempty sentence using English letters and single spaces between words.

The string length is between $1$ and $500$, inclusive.

**Return value**

Return `true` when every word boundary, including the wraparound boundary, has matching letters; otherwise return `false`.

### Examples

**Example 1**

- Input: `sentence = "leetcode exercises sound delightful"`
- Output: `true`
- Explanation: Each word ends with the letter that begins the next word, and the final `l` also matches the first `l`.

**Example 2**

- Input: `sentence = "eetcode"`
- Output: `true`
- Explanation: The only word starts and ends with `e`, so it closes its own cycle.

**Example 3**

- Input: `sentence = "Leetcode is cool"`
- Output: `false`
- Explanation: `Leetcode` ends with `e`, while `is` begins with `i`.
