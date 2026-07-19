# Maximum Repeating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1668 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Dynamic Programming, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-repeating-substring/) |

## Problem Description
### Goal
A string `word` is called $k$-repeating within `sequence` when the concatenation of exactly $k$ consecutive copies of `word` occurs as a substring of `sequence`. The copies must touch one another; separate occurrences elsewhere in `sequence` do not combine into a larger value.

Given the two nonempty lowercase strings, return the greatest integer $k$ for which that repeated block occurs. If even one copy of `word` is absent from `sequence`, return $0$. A repeated block may begin and end anywhere inside `sequence`; it does not need to consume the entire string.

### Function Contract
**Inputs**

- `sequence`: a nonempty string of lowercase English letters in which to search.
- `word`: a nonempty lowercase English string whose adjacent repetitions are counted.

Let $n = \lvert\texttt{sequence}\rvert$ and $m = \lvert\texttt{word}\rvert$.

**Return value**

Return the maximum nonnegative integer $k$ such that $k$ consecutive copies of `word` form a substring of `sequence`.

### Examples
**Example 1**

- Input: `sequence = "ababc", word = "ab"`
- Output: `2`
- Explanation: `"abab"` occurs in `sequence`.

**Example 2**

- Input: `sequence = "ababc", word = "ba"`
- Output: `1`
- Explanation: one copy occurs, but `"baba"` does not.

**Example 3**

- Input: `sequence = "ababc", word = "ac"`
- Output: `0`
