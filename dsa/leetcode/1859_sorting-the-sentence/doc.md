# Sorting the Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1859 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sorting-the-sentence/) |

## Problem Description
### Goal
A sentence consists of words separated by single spaces, with no space before
the first word or after the last. Each word contains only lowercase and
uppercase English letters. To shuffle such a sentence, append the word's
1-indexed original position to it, then rearrange the resulting marked words.

Given one shuffled sentence `s` containing at most nine words, restore the
original order. Remove the appended position digit from every word and return
the reconstructed words joined by single spaces.

### Function Contract
**Inputs**

- `s`: a shuffled sentence of length from $2$ through $200$. It contains one
  to nine space-separated marked words. Every marked word consists of English
  letters followed by its digit from `1` through `9`.

Let $S = \lvert s \rvert$ be the number of characters in the shuffled sentence.

**Return value**

The original sentence as a string, with position digits removed and words
separated by one space.

### Examples
**Example 1**

- Input: `s = "is2 sentence4 This1 a3"`
- Output: `"This is a sentence"`

**Example 2**

- Input: `s = "Myself2 Me1 I4 and3"`
- Output: `"Me Myself and I"`

**Example 3**

- Input: `s = "Hello1"`
- Output: `"Hello"`
