# Time Needed to Buy Tickets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2073 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/time-needed-to-buy-tickets/) |

## Problem Description

### Goal

$n$ people stand in a ticket queue from index $0$ at the front through index $n-1$ at the back. `tickets[i]` is the total number of tickets person $i$ wants.

The front person buys exactly one ticket in one second. If that person still needs tickets, they instantly rejoin the back; otherwise they leave. Return the number of seconds elapsed when the person who initially occupied index `k` buys their final ticket. The process stops at that exact moment, before anyone behind them takes another turn.

### Function Contract

**Inputs**

- `tickets`: an array of $n$ positive ticket counts, where $1 \le n \le 100$ and $1 \le \texttt{tickets[i]}\le100$.
- `k`: the tracked person's zero-based initial index, where $0 \le k<n$.

**Return value**

- Return the number of one-second purchases made through and including person `k`'s final purchase.

### Examples

**Example 1**

- Input: `tickets = [2,3,2], k = 2`
- Output: `6`
- Explanation: The tracked person finishes on the sixth purchase after two complete passes through the original queue.

**Example 2**

- Input: `tickets = [5,1,1,1], k = 0`
- Output: `8`
- Explanation: Everyone buys once, then the tracked person buys the remaining four tickets alone.
