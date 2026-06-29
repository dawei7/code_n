# Chef Shortest Route

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSERVER |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [CHEFSERVER](https://www.codechef.com/learn/course/graphs/GRAPHTRAVERS/problems/CHEFSERVER) |

---

## Problem Statement

Chef wants to send a message to Chefina through a cloud provider’s network of servers.
The network is modeled as an **undirected graph**, where servers act as nodes and connections act as edges.

Chef is located at **server 1**, and Chefina is located at **server N**.

Your task is to determine:

* Whether a route exists from server `1` to server `N`
* If it exists, return the **minimum number of servers** used along such a route (including both start and destination)

## Function Declaration

### Function Name

$getMinimumServers$ - This function finds the minimum number of servers required to send a message from **server 1** to **server N**.

If server `N` cannot be reached, the function returns `-1`.

### Parameters

* $n$ : The total number of servers in the network.

* $serverConnections$ : Each pair represents a **bidirectional connection** between server `a` and server `b`.

## Return Value

* Returns an integer:

  * The **minimum number of servers** on the shortest route from server `1` to server `n`
  * Returns `-1` if no route exists

## Constraints

* $1 \leq n \leq 200000$
* $1 \leq m \leq 200000$
* $1 \leq a, b \leq n$
* $a \neq b$
* No self-loops or duplicate connections
* The graph is undirected

---

## Input Format

* The first line contains two integers $n$ and $m$, representing the number of servers and connections.
* The next $m$ lines each contain two integers $a$ and $b$, representing a bidirectional connection between servers $a$ and $b$.

---

## Output Format

* Print a single integer:

  * The minimum number of servers needed to connect server $1$ to server $n$
  * Print $-1$ if no such route exists

---

## Constraints

- $1 \leq N \leq 200000$
- $1 \leq M \leq N(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.

---

## Examples

**Example 1**

**Input**

```text
5 6
1 2
2 3
1 3
3 5
2 4
4 5
```

**Output**

```text
3
```

**Explanation**

One of the shortest paths discovered by BFS is:

```
1 -> 3 -> 5
```

* Number of connections = 2
* Number of servers = 2 + 1 = **3**

Hence, the output is `3`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, BFS.

**Problem:** Chef needs to send a message to Chefina through a cloud provider’s network that spans across N locations with M connections between them. The task is to determine whether Chef can send a message to Chefina and, if possible, find the minimum number of servers on such a route. Servers are numbered from 1 to N, with Chef’s server being 1 and Chefina’s server being N.

**Solution Approach:** We can use BFS to solve the problem. If the node N is in same connected component as node 1, then the minimum no. of servers would be the ones on the shortest path from 1 to N else answer would be -1. By modeling the network as a graph and using Breadth-First Search (BFS), we can efficiently explore the graph in a level-by-level manner. The inherent nature of BFS makes it suitable for finding the shortest path in an unweighted graph, ensuring that the first occurrence of Chefina’s server is reached using the minimum number of servers.

**Key Points:**

- *Level-by-Level Exploration:*

- BFS traverses the graph level by level, starting from the source node (Chef’s server) and moving outward.

- At each level, all vertices at the same distance from the source are explored before moving to the next level.

- *Shortest Path Guarantee:*

- In an unweighted graph, BFS guarantees that the first occurrence of a target node (Chefina’s server) is reached with the minimum number of edges.

- As BFS explores the graph level by level, the first time Chefina’s server is encountered, it will be through the shortest possible path.

Since the shortest distance between two nodes stores no. of edges, we add 1 to the shortest distance as we need no. of nodes (i.e., no. of servers).

**Time complexity:** The time complexity is O(N + M), where N is the number of servers, and M is the number of connections. Each server and connection is processed once during the BFS traversal.

**Space complexity:** O(N) as the space complexity of BFS is O(N).

</details>
