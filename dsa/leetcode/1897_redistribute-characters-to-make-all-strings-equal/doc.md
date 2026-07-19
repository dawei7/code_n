# Redistribute Characters to Make All Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1897 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/) |

## Problem Description

### Goal

An operation chooses two different word indices, removes any one character from a nonempty source word, and inserts that character at any position in the destination word. The operation may be repeated any number of times, and the selected source and destination can change between operations.

Given an array of lowercase words, decide whether these moves can make every word exactly equal. Character order and the initial word lengths may change, but no character can be created, deleted, or changed into another letter.

### Function Contract

**Inputs**

- `words`: an array of $N$ nonempty lowercase English strings, where $1 \le N \le 100$ and every initial word has length from $1$ through $100$.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

Return `true` if character moves can make all $N$ strings identical; otherwise return `false`.

### Examples

**Example 1**

- Input: `words = ["abc","aabc","bc"]`
- Output: `true`
- Explanation: Moving one `a` from the second word to the third produces three copies of `"abc"`.

**Example 2**

- Input: `words = ["ab","a"]`
- Output: `false`

**Example 3**

- Input: `words = ["ab","ba"]`
- Output: `true`
- Explanation: The combined counts contain two copies of each letter, so each of two final words can receive one.
