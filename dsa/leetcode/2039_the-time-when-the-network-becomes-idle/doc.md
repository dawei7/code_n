# The Time When the Network Becomes Idle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2039 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/) |

## Problem Description

### Goal

An undirected connected network contains $N$ servers labeled from `0` through
`N - 1`. Each channel carries any number of messages in either direction and
crossing one channel takes one second. Server `0` is the master; every other
server sends an initial request at the beginning of second `0`. Requests follow
a shortest path, the master replies instantly, and each reply follows its
request's path in reverse.

Before receiving its first reply, data server $i$ resends at the beginning of
every `patience[i]`-th second since its previous send. A reply arriving at the
beginning of a second is observed before that second's resend decision. Once a
server has received a reply, it sends no more copies. Return the earliest
second from whose beginning no request or reply remains in transit or arrives.

### Function Contract

Let $E$ be the number of channels.

**Inputs**

- `edges`: $E$ distinct undirected pairs `[u, v]` describing a connected
  network with $2 \le N \le 10^5$ and $1 \le E \le 10^5$.
- `patience`: a length-$N$ array where `patience[0] = 0` and
  $1 \le \texttt{patience[i]} \le 10^5$ for every data server.

**Return value**

- The first integer second at whose beginning the entire network is idle.

### Examples

**Example 1**

- Input: `edges = [[0, 1], [1, 2]], patience = [0, 2, 1]`
- Output: `8`
- Explanation: Server `2` has round-trip time `4` and last resends at second
  `3`; that final reply arrives at second `7`.

**Example 2**

- Input: `edges = [[0, 1], [0, 2], [1, 2]], patience = [0, 10, 10]`
- Output: `3`
- Explanation: Both data servers receive their only reply at second `2`.

**Example 3**

- Input: `edges = [[0, 1]], patience = [0, 1]`
- Output: `4`
- Explanation: The resend at second `1` returns at second `3`, so the network
  is first idle at second `4`.
