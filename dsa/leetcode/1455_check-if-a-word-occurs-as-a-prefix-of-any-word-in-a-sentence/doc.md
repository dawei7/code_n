# Check If a Word Occurs As a Prefix of Any Word in a Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1455 |
| Difficulty | Easy |
| Topics | Two Pointers, String, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) |

## Problem Description
### Goal

Given a lowercase sentence whose words are separated by single spaces and a
lowercase `searchWord`, determine whether `searchWord` is a prefix of any whole
word in the sentence. A prefix must begin at the word's first character and
continue contiguously; finding the same letters only in the middle does not
qualify.

Return the 1-based index of the first word having that prefix. If several words
match, the smallest index is required. If no word matches, return `-1`.

### Function Contract
**Inputs**

- `sentence`: a non-empty string of length $N$, with
  $1 \le N \le 100$, containing lowercase English words separated by one
  space.
- `searchWord`: a lowercase English string with length between $1$ and $10$.

**Return value**

Return the smallest 1-based word index whose word starts with `searchWord`, or
`-1` if no such word exists.

### Examples
**Example 1**

- Input: `sentence = "i love eating burger", searchWord = "burg"`
- Output: `4`

**Example 2**

- Input: `sentence = "this problem is an easy problem", searchWord = "pro"`
- Output: `2`
- Explanation: Both occurrences of `"problem"` match, so return the earlier
  word index.

**Example 3**

- Input: `sentence = "i am tired", searchWord = "you"`
- Output: `-1`
