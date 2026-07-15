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

### Required Complexity
- **Time:** $O((n+m)\alpha(n))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reject an insufficient cable supply**

Any connected graph on `n` vertices needs at least $n-1$ edges. Moving a cable does not change the total, so when `len(connections) < n - 1`, connection is impossible and the answer is `-1`.

**Count components with disjoint sets**

Otherwise, initialize one disjoint-set component per computer. For every cable `[u, v]`, unite the components containing its endpoints. Union by size and path compression keep these operations nearly constant in amortized time. Each successful union reduces the component count by one; cables whose endpoints already share a root are redundant.

If $k$ components remain, at least $k-1$ moves are necessary because one new cable can merge at most two components. The initial edge-count check also guarantees enough redundant cables: a forest spanning the existing components uses $n-k$ cables, leaving at least $(n-1)-(n-k)=k-1$ cables available to relocate. Thus exactly $k-1$ operations are both necessary and achievable.

#### Complexity detail

Initializing the disjoint-set arrays costs $O(n)$. Processing $m$ cables with union by size and path compression costs $O(m\alpha(n))$, for $O((n+m)\alpha(n))$ total time. The parent and size arrays use $O(n)$ space.

#### Alternatives and edge cases

- **DFS or BFS:** Build an adjacency list and count connected components in $O(n+m)$ time and space; this is equally suitable but stores both directions of every cable.
- **Repeated reachability searches:** Recomputing a traversal from every computer can take $O(n(n+m))$ time and repeats the same component work.
- **Too few cables:** Return `-1` immediately even if most computers already belong to one large component.
- **Redundant cycles:** A cable on a cycle can be removed without disconnecting its current component and is available for relocation.
- **Already connected:** One remaining component requires 0 operations.
- **Isolated computers:** Each isolated vertex is its own component and must be joined once, provided enough redundant cables exist elsewhere.

</details>
