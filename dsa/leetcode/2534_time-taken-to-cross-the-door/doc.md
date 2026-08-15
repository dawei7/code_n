# Time Taken to Cross the Door

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2534 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/time-taken-to-cross-the-door/) |

## Problem Description

### Goal

There are $n$ people numbered from $0$ through $n-1$ and one door that takes one second to cross. The non-decreasing array `arrival` gives each person's arrival second. `state[i]` is `0` when person $i$ wants to enter and `1` when they want to exit. A person may wait after arriving, and only one person crosses in any second.

When both directions have waiting people, the previous second determines priority. If the door was unused, exiting has priority. If it was used, the same direction has priority. Among people waiting for the chosen direction, the smallest index crosses first. Return every person's actual crossing second.

### Function Contract

**Inputs**

- `arrival`: The people's non-decreasing arrival times in index order.
- `state`: The aligned desired directions, where `0` means enter and `1` means exit.

Let $n = \lvert\texttt{arrival}\rvert = \lvert\texttt{state}\rvert$. The constraints are $1 \le n \le 10^5$, $0 \le \texttt{arrival[i]} \le n$, and every state is `0` or `1`.

**Return value**

Return an array `answer` of length $n$ where `answer[i]` is the second when person $i$ crosses the door.

### Examples

#### Example 1

- **Input:** `arrival = [0, 1, 1, 2, 4], state = [0, 1, 0, 0, 1]`
- **Output:** `[0, 3, 1, 2, 4]`
- **Explanation:** Entering retains priority at seconds `1` and `2`; the waiting exiting person then crosses at `3`.

#### Example 2

- **Input:** `arrival = [0, 0, 0], state = [1, 0, 1]`
- **Output:** `[0, 2, 1]`
- **Explanation:** The unused-door rule selects exiting, and smaller index `0` wins the first exiting tie.
