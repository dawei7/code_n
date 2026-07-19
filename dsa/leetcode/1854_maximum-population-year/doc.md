# Maximum Population Year

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-population-year/) |
| Frontend ID | 1854 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each entry `[birth, death]` in `logs` describes one person's lifetime by calendar year. That person contributes to the population in every year from `birth` through `death - 1`: the birth year is included, while the death year is not.

For every year covered by the allowed range, determine how many logged people are alive. Return the earliest year whose population equals the maximum population attained by any year. Thus, when several years share the same largest count, the smaller year must win.

### Function Contract

**Inputs**

- `logs`: a list of between 1 and 100 pairs `[birth, death]`.
- Each pair satisfies $1950 \le \texttt{birth}<\texttt{death}\le 2050$.
- Let $n=\lvert\texttt{logs}\rvert$.
- Let $Y=101$ be the number of difference-array positions from 1950 through 2050.

**Return value**

- Return the earliest year with the largest number of people satisfying $\texttt{birth}\le\texttt{year}<\texttt{death}$.

### Examples

**Example 1**

- Input: `logs = [[1993, 1999], [2000, 2010]]`
- Output: `1993`

Both occupied ranges have population 1, so the earlier year wins.

**Example 2**

- Input: `logs = [[1950, 1961], [1960, 1971], [1970, 1981]]`
- Output: `1960`

**Example 3**

- Input: `logs = [[2000, 2001], [2001, 2002]]`
- Output: `2000`

The first person's death year is excluded, so both years have population 1.
