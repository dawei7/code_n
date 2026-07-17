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

### Required Complexity
- **Time:** $O(rc3^c(I+1)(E+1))$
- **Space:** $O(rc3^c(I+1)(E+1))$

<details>
<summary>Approach</summary>

#### General

**Reduce the frontier by orienting the grid.** Rotate the dimensions conceptually so the shorter side has $c$ cells. Process the resulting $r \times c$ grid in row-major order. When deciding the current cell, only its left neighbor and the cell directly above can already be occupied; interactions with right and lower neighbors will be counted when those cells are processed.

**Encode the preceding cells in base three.** Store the last $c$ cell types as a ternary mask: 0 for empty, 1 for introvert, and 2 for extrovert. The oldest ternary digit identifies the person above the current cell, while the newest digit identifies the left neighbor except at a row boundary. Appending the current type and discarding the oldest digit produces the next frontier mask.

**Memoize placement resources and position.** A state consists of the row-major position, frontier mask, and remaining introvert and extrovert counts. Try leaving the cell empty. When the corresponding count is positive, also try placing either person type, adding its base happiness plus the complete pair effect with the already processed upper and left neighbors. Memoization merges all partial layouts that expose the same future-relevant state.

**Why local pair scoring yields the global total.** Every resident's base happiness is added exactly when that resident is placed. Every horizontal or vertical neighboring pair is encountered exactly once, when its later row-major endpoint is placed, and the pair adjustment already combines both people's reactions. Thus each completed DP path has precisely the happiness of its represented grid. Taking the maximum across all empty, introvert, and extrovert choices includes every legal partial placement, including choices that leave available people unused.

#### Complexity detail

There are $rc$ positions, $3^c$ frontier masks, and at most $(I+1)(E+1)$ remaining-count pairs. Each state considers at most three constant-time choices, giving $O(rc3^c(I+1)(E+1))$ time. The memo table and recursion stack are bounded by $O(rc3^c(I+1)(E+1))$ space.

#### Alternatives and edge cases

- **Row-state dynamic programming:** Precompute each ternary row's residents, internal happiness, and compatibility with every preceding row. This has the same profile-DP principle but trades simpler transitions for a $3^c \times 3^c$ compatibility table.
- **Enumerate complete grids:** Trying empty, introvert, and extrovert for every cell costs $O(3^{mn})$ before count pruning and repeats equivalent frontiers.
- **Greedy placement by base happiness:** Always preferring introverts or locally favorable cells misses pair effects and the benefit of leaving a person unplaced.
- With no available people, the maximum is zero.
- When both types are available for one cell, placing the introvert is better than placing the extrovert, and leaving the other person unused is legal.
- Two diagonal occupants are not neighbors and cause no pair adjustment.
- A mixed adjacent pair changes total happiness by $-10$, not by either participant's individual change alone.
- Rotating the dimensions changes no adjacency relation and minimizes the exponential mask width.
- Counts may exceed the number worth placing; the empty transition ensures negative marginal placements are never forced.

</details>
