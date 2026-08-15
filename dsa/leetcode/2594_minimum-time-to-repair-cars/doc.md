# Minimum Time to Repair Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2594 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-repair-cars/) |

## Problem Description

### Goal

You are given the positive integer ranks of several mechanics. A mechanic with rank $r$ needs $r n^2$ minutes to repair $n$ cars.

There are `cars` vehicles waiting, and every mechanic may work simultaneously. The vehicles may be distributed among the mechanics in any way; a mechanic may also receive no vehicles.

Return the minimum number of minutes in which the mechanics can collectively repair all waiting cars.

### Function Contract

**Inputs**

- `ranks`: A list containing one positive rank for each mechanic.
- `cars`: The positive total number of cars that must be repaired.

Let $m = \lvert\texttt{ranks}\rvert$ and $c = \texttt{cars}$. The constraints are $1 \leq m \leq 10^5$, $1 \leq \texttt{ranks[i]} \leq 100$, and $1 \leq c \leq 10^6$.

**Return value**

- The smallest integer time for which the mechanics' combined repair capacity is at least `cars`.

### Examples

#### Example 1

- **Input:** `ranks = [4,2,3,1], cars = 10`
- **Output:** `16`

In 16 minutes, the four mechanics can repair `2`, `2`, `2`, and `4` cars respectively. That repairs all 10 cars, and no smaller time is sufficient.

#### Example 2

- **Input:** `ranks = [5,1,8], cars = 6`
- **Output:** `16`

The mechanics can repair `1`, `4`, and `1` cars respectively within 16 minutes, for a total of 6.
