# Contain Virus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 749 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/contain-virus/) |

## Problem Description

### Goal

A virus occupies `1` cells of a binary grid and can spread to horizontally or vertically adjacent uninfected `0` cells. Each day, choose the connected infected region that threatens the greatest number of distinct healthy cells and quarantine that region permanently.

Build one wall segment along every infected-to-healthy boundary edge of the chosen region and add those segments to the total. Then let every other active infected region spread into all threatened neighboring cells. Repeat until no further spread is possible, and return the total number of wall segments built. The input guarantees a unique region to quarantine whenever a choice is needed.

### Function Contract

**Inputs**

- `isInfected`: a rectangular matrix where `1` is an active infected cell and `0` is a healthy cell. The daily region with the largest threatened frontier is unique whenever containment is still needed.

**Return value**

- The total number of infected-to-healthy grid edges blocked by all quarantines.

### Examples

**Example 1**

- Input: `isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]`
- Output: `10`
- Explanation: Quarantining the right-hand region first costs five walls; later containing the remaining spread costs five more.

**Example 2**

- Input: `isInfected = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `4`
- Explanation: The central healthy cell is threatened across four separate grid edges, so four wall segments are required.

### Required Complexity

- **Time:** $O((mn)^2)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Record cells, threatened cells, and boundary edges separately**

At the start of a day, traverse every still-active `1` component. For each component, collect three facts:

- its infected cells, so the selected region can be marked quarantined;
- a set of adjacent healthy cells, whose size determines which region is selected;
- the number of infected-to-healthy adjacencies, which is the number of wall segments required.

The frontier must be a set because several infected cells may threaten the same healthy cell. Wall segments are counted per edge instead: those separate contacts each need their own wall.

**Freeze one region before simultaneous spread**

Choose the component with the largest frontier. Add its boundary-edge count to the answer and change its cells to a permanent state such as `-1`, which future traversals and spreads ignore. For every other component, change all cells in its saved frontier to `1`. Using the frontiers recorded before any mutation makes the day's spread simultaneous, even when multiple regions target the same cell.

**Stop only when no healthy cell is threatened**

Repeat the full discovery after each spread, because components can grow or merge. If the largest frontier is empty, every active region has no healthy neighbor and no further walls or spread can occur.

The component traversal enumerates every active region exactly once for the current day. Its frontier size is therefore the problem's selection criterion, and its edge count is exactly the construction cost. Marking the chosen cells prevents their future participation; applying every other saved frontier performs precisely one day of spread. Repeating these faithful state transitions yields the required total.

#### Complexity detail

Let `m` and `n` be the grid dimensions. One day scans and stores $O(mn)$ cells. Each productive day permanently quarantines at least one active cell, so there are at most `mn` such days. The worst-case time is $O((mn)^2)$, and the region, frontier, traversal, and visited storage use $O(mn)$ space.

#### Alternatives and edge cases

- **Breadth-first component discovery:** A queue can replace the depth-first stack with the same state, correctness, and asymptotic bounds.
- **Rediscover a component from every infected cell:** Deduplicating complete region descriptions afterward can be correct, but one day's work can become quadratic instead of linear.
- **Count only frontier cells as walls:** This is incorrect when two infected cells touch the same healthy cell; distinct boundary edges require distinct wall segments.
- **All healthy cells:** No region exists, so the answer is `0`.
- **No threatened healthy cell:** An all-infected or already enclosed grid needs no additional walls.
- **Overlapping spread frontiers:** Several unquarantined regions may infect the same cell; setting it to `1` more than once has no extra effect.
- **Quarantined cells:** They remain blocked forever and must not reconnect active components.

</details>
