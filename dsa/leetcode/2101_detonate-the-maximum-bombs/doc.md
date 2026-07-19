# Detonate the Maximum Bombs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Graph Theory, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/detonate-the-maximum-bombs/) |

## Problem Description

### Goal

Each bomb is represented by `[x, y, radius]`. Its effect covers the closed circle centered at $(x,y)$ with the given radius. When one bomb detonates, every other bomb whose center lies inside or on that circle also detonates. Each newly detonated bomb can trigger further bombs within its own range.

You may manually detonate exactly one starting bomb. Choose the start that produces the largest chain reaction and return the number of bombs that eventually detonate.

### Function Contract

Let $n$ be the number of bombs.

**Inputs**

- `bombs`: a list of $n$ triples `[x, y, radius]`, where $1 \le n \le 100$ and every coordinate and radius is between $1$ and $10^5$ inclusive.

**Return value**

Return the maximum number of bombs reachable through a chain reaction from one chosen starting bomb.

### Examples

**Example 1**

- Input: `bombs = [[2,1,3],[6,1,4]]`
- Output: `2`
- Explanation: The right bomb reaches the left bomb, although the left bomb does not reach the right one.

**Example 2**

- Input: `bombs = [[1,1,5],[10,10,5]]`
- Output: `1`
- Explanation: Neither center lies within the other bomb's range.

**Example 3**

- Input: `bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]`
- Output: `5`
- Explanation: Starting with bomb `0` triggers bombs `1` and `2`; later detonations continue the chain through bombs `3` and `4`.
