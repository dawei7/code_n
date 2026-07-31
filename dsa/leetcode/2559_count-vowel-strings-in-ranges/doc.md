# Count Vowel Strings in Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2559 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Vowel Strings in Ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges/) |

## Problem Description

### Goal

You are given a 0-indexed array `words` and a list of inclusive index ranges `queries`. A word qualifies as a vowel string when both its first character and its last character are vowels. For this problem, the vowels are exactly `a`, `e`, `i`, `o`, and `u`.

Each query is a pair `[left, right]` asking how many qualifying words occur from index `left` through index `right`, including both endpoints. Return one count per query in the original query order.

### Function Contract

**Inputs**

- `words`: A list of $n$ nonempty strings containing only lowercase English letters, where $1 \le n \le 10^5$, each length is at most $40$, and their combined length is at most $3\cdot10^5$.
- `queries`: A list of $q$ pairs `[left, right]`, where $1 \le q \le 10^5$ and $0 \le \texttt{left} \le \texttt{right} < n$.

**Return value**

- A list of $q$ integers in which entry $i$ is the number of words that start and end with a vowel inside the inclusive range given by `queries[i]`.

### Examples

**Example 1**

- Input: `words = ["aba", "bcb", "ece", "aa", "e"], queries = [[0, 2], [1, 4], [1, 1]]`
- Output: `[2, 3, 0]`
- Explanation: The qualifying words are `aba`, `ece`, `aa`, and `e`; each range counts only those indices it contains.

**Example 2**

- Input: `words = ["a", "e", "i"], queries = [[0, 2], [0, 1], [2, 2]]`
- Output: `[3, 2, 1]`
- Explanation: Every word begins and ends with a vowel.

**Example 3**

- Input: `words = ["apple", "owl", "ice"], queries = [[0, 2], [1, 1]]`
- Output: `[2, 0]`
- Explanation: `apple` and `ice` qualify, while `owl` ends with a consonant.
