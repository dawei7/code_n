# Soup Servings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 808 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/soup-servings/) |

## Problem Description

### Goal

Soups A and B each begin with `n` milliliters. On every turn, choose independently and uniformly among serving `(100, 0)`, `(75, 25)`, `(50, 50)`, or `(25, 75)` milliliters from `(A, B)`; if less than a requested amount remains, serve all of that soup.

The process stops immediately after a turn empties either soup. Return the probability that A becomes empty before B plus one half of the probability that both become empty on the same turn. There is no operation that serves `(0, 100)`.

### Function Contract

**Inputs**

- `n`: the nonnegative initial amount of each soup in milliliters.

**Return value**

- $\Pr(A\text{ empties first}) + 0.5 \cdot \Pr(A\text{ and }B\text{ empty together})$, within the required floating-point tolerance.

### Examples

**Example 1**

- Input: `n = 50`
- Output: `0.625`
- Explanation: Averaging the four first-serving outcomes gives the weighted probability `0.625`.

**Example 2**

- Input: `n = 100`
- Output: `0.71875`
- Explanation: Several serving rounds may occur; combining their equally likely branches gives `0.71875`.

**Example 3**

- Input: `n = 0`
- Output: `0.5`
- Explanation: Both soups are empty together before any serving, so the tie contributes one half.
