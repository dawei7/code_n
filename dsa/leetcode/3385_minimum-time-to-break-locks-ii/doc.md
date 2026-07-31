# Minimum Time to Break Locks II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3385 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-break-locks-ii/) |

## Problem Description

### Goal

There are $n$ locks, and lock $i$ requires at least `strength[i]` units of energy to break. A sword starts with zero energy and a growth factor $X=1$. During each minute, its energy increases by the current value of $X$.

You may break any remaining lock as soon as the sword has enough energy for it. Breaking a lock resets the sword's energy to zero and permanently increases $X$ by one. Thus, before the $j$-th lock is broken, the sword gains $j$ energy units per minute, but choosing that lock also determines which strength must be paid at that rate.

Choose the order in which to break all locks so that the total elapsed time is as small as possible, and return that minimum time.

### Function Contract

**Inputs**

- `strength`: A list of $n$ positive integers, where `strength[i]` is the energy required to break lock $i$.

The number of locks satisfies $1 \le n \le 80$, and every strength satisfies $1 \le \texttt{strength[i]} \le 10^6$.

**Return value**

Return the minimum number of whole minutes required to break every lock.

### Examples

**Example 1**

- Input: `strength = [3, 4, 1]`
- Output: `4`

**Example 2**

- Input: `strength = [2, 5, 4]`
- Output: `6`
