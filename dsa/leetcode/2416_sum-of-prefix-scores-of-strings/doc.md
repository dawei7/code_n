# Sum of Prefix Scores of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2416 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/) |

## Problem Description

### Goal

For a string `term`, define its score as the number of input words having `term` as a prefix. For example, among `["a","ab","abc","cab"]`, the score of `"ab"` is 2 because both `"ab"` and `"abc"` begin with it. A word is considered a prefix of itself.

For every non-empty input word, enumerate all of its non-empty prefixes conceptually and add their scores. Return these sums in the original word order. Duplicate words are separate array entries and must each contribute to every prefix count they share.

### Function Contract

**Inputs**

- `words`: A non-empty array of non-empty lowercase English strings.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w\rvert.
$$

There are at most 1,000 words, and each word has length at most 1,000.

**Return value**

Return an integer array where element $i$ is the sum of the scores of every non-empty prefix of `words[i]`.

### Examples

**Example 1**

- Input: `words = ["abc","ab","bc","b"]`
- Output: `[5,4,3,2]`

**Example 2**

- Input: `words = ["abcd"]`
- Output: `[4]`

**Example 3**

- Input: `words = ["a","aa","aaa"]`
- Output: `[3,5,6]`
