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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count turns instead of rotating the queue**

Let $t=\texttt{tickets[k]}$. The tracked person participates in exactly $t$ passes and the process ends during the $t$th pass. Every person at an index at most `k` gets a turn before or at that stopping point in all $t$ passes, unless they finish earlier. Their contribution is therefore $\min(\texttt{tickets[i]},t)$.

**The suffix misses the final pass**

People after `k` do not act after the tracked person's final purchase. They can participate in at most the first $t-1$ passes, so each contributes $\min(\texttt{tickets[i]},t-1)$. Sum the appropriate contribution for every index.

Each actual purchase belongs to one person and one pass. The two formulas count exactly the passes that occur before the stopping event for positions before, at, and after `k`; they also cap each person at their requested total. Hence their sum equals the elapsed number of one-second purchases without simulating queue movement.

#### Complexity detail

The algorithm scans the $n$ ticket counts once and performs constant work per person, giving $O(n)$ time. It retains only the target count and running sum, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Queue simulation:** Rotating active people exactly reproduces the process, but its time is proportional to the number of tickets purchased before `k` finishes, which can be $O(n\cdot\texttt{tickets[k]})$.
- **Repeated array passes:** Decrementing active counts from left to right avoids an explicit queue but has the same demand-dependent running time.
- A person before `k` may buy as many tickets as the tracked person before the stop.
- A person after `k` gets at most `tickets[k] - 1` turns.
- When `tickets[k] == 1`, nobody after `k` buys before the process stops.
- With one person, the answer is that person's requested ticket count.

</details>
