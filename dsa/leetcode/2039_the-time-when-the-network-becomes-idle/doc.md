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

### Required Complexity

- **Time:** $O(N+E)$
- **Space:** $O(N+E)$

<details>
<summary>Approach</summary>

#### General

**Find every shortest round-trip time**

Because every channel takes one second, breadth-first search from server `0`
gives the shortest edge distance $d_i$ to each server $i$. Its first request
and reply require

$$
R_i = 2d_i
$$

seconds for the round trip.

**Locate the final resend before the first reply**

Server $i$ sends at seconds $0,p_i,2p_i,\ldots$ only while it has not received
the first reply. Since the reply arriving at second $R_i$ is checked before a
possible resend, the last send time is the greatest multiple of $p_i$ strictly
less than $R_i$:

$$
L_i =
\left\lfloor\frac{R_i-1}{p_i}\right\rfloor p_i.
$$

The reply to that last copy arrives at second $L_i+R_i$. This formula also
covers the no-resend case: when $p_i \ge R_i$, it gives $L_i=0$.

**Wait one second beyond the final arrival**

No later copy can exist for a server because $L_i$ is its last send, and every
copy uses the same shortest round-trip duration. Therefore the latest message
activity anywhere in the network occurs at the maximum of $L_i+R_i$ over all
data servers. The network is first idle at the following second, so return that
maximum plus one.

#### Complexity detail

Building the adjacency lists and performing BFS takes $O(N+E)$ time. Computing
the final arrival for each server takes another $O(N)$ time. The graph,
distance array, and BFS queue occupy $O(N+E)$ space.

#### Alternatives and edge cases

- **Shortest-path search from every server:** Repeating BFS is correct but can
  take $O(N(N+E))$ time; one BFS from the common master suffices.
- **Second-by-second message simulation:** Explicitly generating every resend
  can be enormous when patience is small and obscures the closed-form final
  send time.
- A patience value equal to the round-trip time causes no resend at that time,
  because the first reply is processed first.
- With patience `1`, the last resend occurs exactly one second before the first
  reply.
- Multiple shortest paths do not affect timing because only their common
  length matters.
- The master has patience `0` but never sends an originating request, so it is
  excluded from the resend calculation.
- The requested answer is one second after the latest arrival, not the arrival
  second itself.

</details>
