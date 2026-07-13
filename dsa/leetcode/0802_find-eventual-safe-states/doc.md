# Find Eventual Safe States

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 802 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-eventual-safe-states/) |

## Problem Description

### Goal

A directed graph has nodes labeled `0` through $n - 1$. A terminal node has no outgoing edges, and a node is eventually safe when every possible path starting from it ultimately reaches a terminal node or another safe node rather than continuing around a cycle forever.

Return all safe node labels sorted in ascending order. The requirement covers every possible outgoing choice, so a node is unsafe if even one reachable path can enter a directed cycle, regardless of whether another path reaches a terminal node.

### Function Contract

**Inputs**

- `graph`: a directed graph represented by adjacency lists, where `graph[i]` contains every destination of an edge leaving node `i`.

**Return value**

- All eventual safe node numbers in increasing order.

### Examples

**Example 1**

- Input: `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`
- Output: `[2,4,5,6]`
- Explanation: Nodes `0`, `1`, and `3` can enter a cycle; every route from the other nodes terminates.

**Example 2**

- Input: `graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]`
- Output: `[4]`
- Explanation: Node `4` is terminal, while each other node is in or can reach a cycle.

**Example 3**

- Input: `graph = [[],[],[]]`
- Output: `[0,1,2]`
- Explanation: Every node is already terminal and therefore safe.

### Required Complexity

- **Time:** $O(V + E)$
- **Space:** $O(V + E)$

<details>
<summary>Approach</summary>

#### General

**Reverse the direction of dependency**

A terminal node is safe immediately. A nonterminal node becomes safe once every node it points to is known safe. Build the reverse graph so that, when a node becomes safe, all of its predecessors can be updated directly. Also store each node's current count of outgoing edges not yet proved safe.

**Eliminate from terminal nodes backward**

Put every node with outdegree zero into a queue. When removing a safe node, decrement the remaining outdegree of each predecessor. If a predecessor's count reaches zero, all of its possible next steps are safe, so mark and enqueue it. Finally, scan node numbers in order and return those marked safe.

Every initially queued node terminates immediately. Inductively, a later queued node has only edges to nodes already proved safe, so every path from it also terminates. Conversely, consider any safe node: all paths below it are finite, so working backward from their terminal endpoints eventually removes every outgoing edge of that node and enqueues it. Nodes left unmarked are therefore exactly those in or able to reach a cycle.

#### Complexity detail

Let `V` be the number of nodes and `E` the number of directed edges. Building the reverse graph and processing each node and edge at most once takes $O(V + E)$ time. The reverse adjacency lists, outdegrees, safe marks, and queue use $O(V + E)$ space.

#### Alternatives and edge cases

- **DFS coloring:** Mark nodes as unvisited, active, unsafe, or safe; detecting an edge to an active node identifies a cycle and also gives $O(V + E)$ time.
- **Fresh DFS from every node:** Checking each start independently is correct but repeats reachable subgraphs and can take $O(V \cdot (V + E))$ time.
- **Strongly connected components:** Condensing cycles into components can identify unsafe reachability, but it is more machinery than reverse elimination needs.
- **Terminal nodes:** They are safe even when disconnected from the rest of the graph.
- **Self-loop:** A node pointing to itself is unsafe, as is any node that can reach it.
- **One unsafe choice:** Safety requires every possible path to terminate; a single outgoing route to a cycle makes a node unsafe.
- **Output order:** Scan the boolean result by node number so the returned list is increasing.

</details>
