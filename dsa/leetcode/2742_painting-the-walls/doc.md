# Painting the Walls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2742 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/painting-the-walls/) |

## Problem Description

### Goal

Two painters are available for $n$ distinct walls. If the paid painter handles wall $i$, that wall costs `cost[i]` and occupies the painter for `time[i]` time units. A free painter can paint any wall in one time unit at no monetary cost, but may work only while the paid painter is occupied.

Choose which walls the paid painter handles so that the free painter has enough concurrent working time to finish every remaining wall. Return the minimum total amount paid. The assignments may use the paid work periods collectively; only the total available occupied time and the number of remaining walls matter.

### Function Contract

Let $n$ be the common length of the two arrays.

**Inputs**

- `cost`: The paid-painter prices, where $1 \le n \le 500$ and $1 \le \texttt{cost}[i] \le 10^6$.
- `time`: The matching paid-painter durations, with `time.length == cost.length` and $1 \le \texttt{time}[i] \le 500$.

**Return value**

Return the minimum total cost of paid assignments that allow all $n$ walls to be painted.

### Examples

#### Example 1

- **Input:** `cost = [1,2,3,2], time = [1,2,3,2]`
- **Output:** `3`
- **Explanation:** Paying for walls `0` and `1` costs `3`; their three occupied time units let the free painter finish the other two walls.

#### Example 2

- **Input:** `cost = [2,3,4,2], time = [1,1,1,1]`
- **Output:** `4`
- **Explanation:** Pay for walls `0` and `3`; the two units of paid work allow the two remaining walls to be painted for free.

#### Example 3

- **Input:** `cost = [10,1,8,7], time = [1,3,1,1]`
- **Output:** `1`
- **Explanation:** Paying for wall `1` covers that wall and supplies enough occupied time for the free painter to finish the other three.
