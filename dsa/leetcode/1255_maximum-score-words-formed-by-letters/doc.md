# Maximum Score Words Formed by Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1255 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) |

## Problem Description

### Goal

You are given candidate lowercase `words`, a multiset of available lowercase `letters`, and a 26-element `score` array. The value of a letter is `score[0]` for `"a"`, `score[1]` for `"b"`, and so on.

Choose any subset of the words. Every occurrence of a letter used by the chosen words must be supplied by a distinct occurrence in `letters`, so an available letter cannot be reused. A word may be selected at most once. Return the maximum total score of all letters in a feasible chosen subset; selecting no words is allowed and scores zero.

### Function Contract

**Inputs**

- `words`: $w$ lowercase words, where $1 \le w \le 14$ and each word has length from $1$ through $15$.
- `letters`: between $1$ and $100$ available lowercase letters, with multiplicity.
- `score`: 26 nonnegative letter scores, each at most `10`.
- Let $L=\sum_{x\in\texttt{words}}\lvert x\rvert$.

**Return value**

- Return the largest total letter score of any subset formable from `letters`.

### Examples

**Example 1**

- Input: `words = ["dog", "cat", "dad", "good"]`, `letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]`
- Output: `23`

**Example 2**

- Input: `words = ["xxxz", "ax", "bx", "cx"]`, `letters = ["z", "a", "b", "c", "x", "x", "x"]`
- Output: `27`

**Example 3**

- Input: `words = ["leetcode"]`, `letters = ["l", "e", "t", "c", "o", "d"]`
- Output: `0`
- Explanation: The missing second `"e"` prevents forming the only candidate word.
