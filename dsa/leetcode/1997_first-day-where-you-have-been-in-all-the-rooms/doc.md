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

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Focus only on first-arrival days.** Because an odd visit never moves to a room with a larger number, rooms are first reached in the order $0,1,\ldots,N-1$. Let $D_i$ be the first day room $i$ is visited. Then $D_0=0$, and the requested answer is $D_{N-1}$.

**Describe the detour before the next new room.** On day $D_i$, room $i$ has just been visited for the first time, so its visit count is odd. The next day jumps back to $k=\texttt{nextVisit[i]}$. The established visit process from the first arrival at $k$ through the first arrival at $i$ has length $D_i-D_k$. Replaying that interval brings the process back to room $i$ for its even-numbered visit. One day starts the detour and one further day advances from $i$ to $i+1$.

Therefore,

$$
D_{i+1}=D_i+1+(D_i-D_k)+1
=2D_i-D_k+2,
\qquad k=\texttt{nextVisit[i]}.
$$

**Evaluate the recurrence from left to right.** Every referenced $D_k$ is already known because $k\le i$. Store each result modulo $10^9+7$; modular subtraction is valid because the recurrence uses only addition and subtraction. Once $D_{N-1}$ is computed, all rooms have been seen for the first time.

#### Complexity detail

The recurrence performs constant work for each of the first $N-1$ rooms, for $O(N)$ time. The first-arrival table contains $N$ values and uses $O(N)$ space.

#### Alternatives and edge cases

- **Simulate every day:** The rule is easy to implement directly, but the first complete day can grow exponentially with $N$, making simulation infeasible.
- **Memoize room transitions:** Visit parity depends on the entire history, so a state keyed only by the current room is insufficient; the first-arrival recurrence captures the reusable structure directly.
- `nextVisit[i] = i` creates the shortest possible detour at room $i$: visit it twice consecutively before advancing.
- Repeated jumps to room $0$ can make the unreduced answer very large, so every recurrence value should be reduced modulo the required constant.
- The value `nextVisit[N - 1]` cannot affect the answer because the process stops being relevant on the first arrival at the last room.

</details>
