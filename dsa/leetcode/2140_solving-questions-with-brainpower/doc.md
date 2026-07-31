# Solving Questions With Brainpower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2140 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [solving-questions-with-brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) |

## Problem Description

### Goal

An exam is represented by a 0-indexed array `questions`, where
`questions[i] = [points, brainpower]`. Process its questions in order and
decide whether to solve or skip each one.

Solving question `i` earns its `points`, but makes the next `brainpower`
questions unavailable. After those forced skips, decisions resume at the next
question. Skipping question `i` earns nothing and permits an immediate decision
about question `i + 1`.

Return the maximum total number of points that can be earned from the exam.

### Function Contract

**Inputs**

- `questions`: A 0-indexed list of `[points, brainpower]` pairs. Its length is
  between $1$ and $10^5$, inclusive; every pair has exactly two elements; and
  both values in every pair are between $1$ and $10^5$, inclusive.

**Return value**

Return the greatest points sum obtainable by processing questions in order and
respecting every forced-skip interval.

### Examples

**Example 1**

- Input: `questions = [[3,2],[4,3],[4,4],[2,5]]`
- Output: `5`
- Explanation: Solving questions `0` and `3` earns $3+2=5$ points.

**Example 2**

- Input: `questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]`
- Output: `7`
- Explanation: Skip question `0`, then solve questions `1` and `4` for
  $2+5=7$ points.
