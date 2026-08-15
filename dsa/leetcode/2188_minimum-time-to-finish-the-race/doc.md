# Minimum Time to Finish the Race

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2188 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-finish-the-race/) |

## Problem Description

### Goal

Each tire type is described by a pair `[f, r]`. Its first consecutive lap
takes `f` seconds, and its $x$-th consecutive lap on the same tire takes
$f r^{x-1}$ seconds. Thus, retaining a tire makes its lap time grow
geometrically.

Complete exactly `numLaps` laps as quickly as possible. Any tire may be used at
the start without a setup delay. After a lap, you may either keep that tire or
wait `changeTime` seconds and install a fresh tire of any listed type, including
another copy of the current type. Every tire type has an unlimited supply.

### Function Contract

**Inputs**

- `tires`: an array of pairs `[f, r]`, where
  $1\le\lvert\texttt{tires}\rvert\le10^5$, $1\le f\le10^5$, and
  $2\le r\le10^5$.
- `changeTime`: the fixed tire-change delay, in $[1,10^5]$ seconds.
- `numLaps`: the number of laps to complete, in $[1,1000]$.

Let $T=\lvert\texttt{tires}\rvert$, $N=\texttt{numLaps}$, and let $L$ be the
largest potentially useful consecutive-lap stint: its final lap is no slower
than changing tires and running the fastest available fresh lap.

**Return value**

Return the minimum total number of seconds needed to complete all $N$ laps.

### Examples

#### Example 1

- **Input:** `tires = [[2,3],[3,4]]`, `changeTime = 5`, `numLaps = 4`
- **Output:** `21`

#### Example 2

- **Input:** `tires = [[1,10],[2,2],[3,4]]`, `changeTime = 6`, `numLaps = 5`
- **Output:** `25`

#### Example 3

- **Input:** `tires = [[2,2]]`, `changeTime = 100`, `numLaps = 4`
- **Output:** `30`
