# Number of Operations to Make Network Connected

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1319 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) |

## Problem Description
### Goal
There are `n` computers numbered from 0 through `n - 1`. Each pair in `connections` represents one Ethernet cable joining two different computers, and computers can communicate whenever a direct or indirect route connects them.

In one operation, an existing cable may be removed from its current endpoints and placed between two computers that are not connected. Determine the minimum number of such cable moves needed to make the whole network connected. Return `-1` when the available cables cannot possibly connect all computers.

The input contains no repeated cable and no self-connection. A moved cable counts as one operation regardless of which disconnected components its new endpoints join.

### Function Contract
**Inputs**

- `n`: the number of computers, with $1\le n\le10^5$.
- `connections`: $m$ distinct undirected pairs `[u, v]`, where $0\le u,v<n$, $u\ne v$, and $m\le10^5$.

**Return value**

The minimum number of cable relocations that makes every computer mutually reachable, or `-1` if there are fewer than $n-1$ cables.

### Examples
**Example 1**

- Input: `n = 4, connections = [[0,1],[0,2],[1,2]]`
- Output: `1`
- Explanation: The cycle contains one redundant cable, which can connect computer 3 to the other three.

**Example 2**

- Input: `n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]`
- Output: `2`
- Explanation: Two redundant cables can attach the two isolated computers.

**Example 3**

- Input: `n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]`
- Output: `-1`
- Explanation: Four cables cannot connect six computers.
