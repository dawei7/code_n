# First Day Where You Have Been in All the Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1997 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/) |

## Problem Description

### Goal

There are $N$ rooms numbered from $0$ through $N-1$, and exactly one room is visited per day. Day labels begin at $0$, when room $0$ receives its first visit. Future movement is determined by `nextVisit`.

After visiting room $i$, count all visits to that room including the current day. If the count is odd, the next day's room is `nextVisit[i]`, which is guaranteed to lie between $0$ and $i$. If the count is even, the next day's room is $(i+1)\bmod N$. The process is guaranteed eventually to visit every room. Return the first day label on which that has happened, modulo $10^9+7$.

### Function Contract

**Inputs**

- `nextVisit`: an array of length $N$, where $2 \le N \le 10^5$.
- For every room $i$, $0 \le \texttt{nextVisit[i]} \le i$.

**Return value**

Return the first day on which every room has been visited at least once, reduced modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `nextVisit = [0, 0]`
- Output: `2`
- Explanation: The visits are rooms $0,0,1$ on days $0,1,2$.

**Example 2**

- Input: `nextVisit = [0, 0, 2]`
- Output: `6`
- Explanation: The room sequence through the first visit to room $2$ is `0, 0, 1, 0, 0, 1, 2`.

**Example 3**

- Input: `nextVisit = [0, 1, 2, 0]`
- Output: `6`
- Explanation: The sequence begins `0, 0, 1, 1, 2, 2, 3`, so day $6$ is the first day covering every room.
