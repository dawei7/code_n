# Minimum Fuel Cost to Report to the Capital

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2477 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/) |

## Problem Description

### Goal

A country has `n` cities numbered from `0` through `n - 1`, connected by `n - 1` bidirectional roads that form a tree. City `0` is the capital. Each city has one representative and one car, and every car has exactly `seats` seats.

All representatives must attend a meeting in the capital. They may drive their local cars, share cars, or transfer into another representative's car at any city. Traversing one road with one car consumes one liter of fuel, regardless of the number of passengers. Return the minimum total fuel needed for every representative to reach city `0`.

### Function Contract

**Inputs**

- `roads`: The tree edges, where each `[a, b]` joins cities `a` and `b`. If there are `n` cities, the array contains exactly `n - 1` edges.
- `seats`: The common positive seating capacity of every car.

The constraints satisfy $1 \le n \le 10^5$ and $1 \le \texttt{seats} \le 10^5$.

**Return value**

Return an integer: the minimum number of liters consumed while bringing all representatives to city `0`.

### Examples

**Example 1**

- Input: `roads = [[0,1],[0,2],[0,3]], seats = 5`
- Output: `3`
- Explanation: Each non-capital representative crosses its direct road once, using three liters total.

**Example 2**

- Input: `roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2`
- Output: `7`
- Explanation: Representatives combine cars while moving toward the capital, minimizing the cars crossing each edge.

**Example 3**

- Input: `roads = [], seats = 1`
- Output: `0`
- Explanation: The only representative already starts in the capital.
