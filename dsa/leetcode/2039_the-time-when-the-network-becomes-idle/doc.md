# The Time When the Network Becomes Idle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2039 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-time-when-the-network-becomes-idle](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/).

### Goal
Messages travel from data servers to server `0` and replies return along shortest paths. Servers resend messages periodically until their first reply arrives. Find when the whole network becomes idle.

### Function Contract
**Inputs**

- `edges`: undirected network edges.
- `patience`: resend interval for each server.

**Return value**

Return the first second when no messages are in transit.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2]], patience = [0,2,1]`
- Output: `8`

**Example 2**

- Input: `edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]`
- Output: `3`

**Example 3**

- Input: `edges = [[0,1]], patience = [0,1]`
- Output: `2`

---

## Solution
### Approach
BFS from server `0` gives shortest edge distances. A server's round trip time is `2 * distance`. Its last resend occurs before the reply arrives: `((roundTrip - 1) // patience[i]) * patience[i]`. The network is idle one second after the latest final reply.

### Complexity Analysis
- **Time Complexity**: `O(n + e)`
- **Space Complexity**: `O(n + e)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
