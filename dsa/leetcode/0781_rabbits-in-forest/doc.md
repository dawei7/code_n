# Rabbits in Forest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 781 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rabbits-in-forest/) |

## Problem Description

### Goal

Each surveyed rabbit reports how many other rabbits in the forest have the same color. An answer `y` therefore describes a possible color group containing exactly $y + 1$ rabbits, including the respondent.

Given all reported answers, return the minimum total number of rabbits that could be in the forest. Rabbits giving different answers cannot share a color, while rabbits giving the same answer may belong to one group or to several separate groups of that size. Unsurveyed group members must still be counted.

### Function Contract

**Inputs**

- `answers`: a list of nonnegative integers, where an entry `y` claims that exactly `y` other rabbits have the respondent's color.

**Return value**

- The minimum forest population consistent with every response.

### Examples

**Example 1**

- Input: `answers = [1,1,2]`
- Output: `5`
- Explanation: The two rabbits answering `1` can form one color group of two; the rabbit answering `2` requires a group of three.

**Example 2**

- Input: `answers = [10,10,10]`
- Output: `11`
- Explanation: All three respondents can belong to a single color group of size eleven.

**Example 3**

- Input: `answers = []`
- Output: `0`
- Explanation: No surveyed rabbits impose any required population.
