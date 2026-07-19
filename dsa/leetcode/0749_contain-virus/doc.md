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
