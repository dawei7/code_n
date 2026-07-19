# Maximize Grid Happiness

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1659 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Bit Manipulation, Memoization, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-grid-happiness/) |

## Problem Description
### Goal
Arrange any chosen number of introverts and extroverts in distinct cells of an $m \times n$ grid. You may leave cells empty and do not have to place every available person. An introvert begins with 120 happiness and loses 30 for each neighbor, while an extrovert begins with 40 happiness and gains 20 for each neighbor.

Only people in cells directly north, east, south, or west are neighbors. A neighboring pair affects both participants, so two introverts change the total by $-60$, two extroverts by $+40$, and a mixed pair by $-10$. Choose the occupied cells and person types that maximize the sum of all residents' happiness.

### Function Contract
**Inputs**

- `m`: the number of grid rows, where $1 \le m \le 5$.
- `n`: the number of grid columns, where $1 \le n \le 5$.
- `introvertsCount`: the number of available introverts, between 0 and $\min(mn,6)$.
- `extrovertsCount`: the number of available extroverts, between 0 and $\min(mn,6)$.

Let $r=\max(m,n)$, $c=\min(m,n)$, $I=\texttt{introvertsCount}$, and $E=\texttt{extrovertsCount}$.

**Return value**

Return the maximum achievable total happiness. Leaving some or all people unplaced is allowed.

### Examples
**Example 1**

- Input: `m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2`
- Output: `240`

An introvert can be isolated while the two extroverts occupy adjacent cells, contributing $120+60+60$.

**Example 2**

- Input: `m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1`
- Output: `260`

Placing the extrovert between the two introverts gives individual happiness values 90, 80, and 90.

**Example 3**

- Input: `m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0`
- Output: `240`
