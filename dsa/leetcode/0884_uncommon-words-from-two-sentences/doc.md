# Uncommon Words from Two Sentences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 884 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/uncommon-words-from-two-sentences/) |

## Problem Description
### Goal
A sentence is a string of lowercase-letter words separated by single spaces. Neither of the two given sentences has a leading or trailing space.

A word is uncommon when it appears exactly once in one of the sentences and does not appear at all in the other sentence. Given `s1` and `s2`, return every uncommon word. The words in the returned list may be in any order.

### Function Contract
Let $L = \lvert \texttt{s1} \rvert + \lvert \texttt{s2} \rvert$ be the total number of characters in the two sentences.

**Inputs**

- `s1`: a single-space-separated sentence of lowercase English words, with $1 \leq \lvert \texttt{s1} \rvert \leq 200$.
- `s2`: a sentence with the same format, with $1 \leq \lvert \texttt{s2} \rvert \leq 200$.

**Return value**

Return a list containing exactly the words that occur once in one sentence and zero times in the other; the result order is unrestricted.

### Examples
**Example 1**

- Input: `s1 = "this apple is sweet", s2 = "this apple is sour"`
- Output: `["sweet","sour"]`

The shared words occur in both sentences, while `sweet` and `sour` each occur only once overall.

**Example 2**

- Input: `s1 = "apple apple", s2 = "banana"`
- Output: `["banana"]`

The repeated word `apple` is not uncommon even though it is absent from `s2`.

**Example 3**

- Input: `s1 = "red blue red", s2 = "green blue gold"`
- Output: `["green","gold"]`
