# Maximal Score Path

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RG_01 |
| Difficulty Rating | 1836 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [RG_01](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/RG_01) |

---

## Problem Statement

### Problem Statement Given a weighted and undirected graph G = (V, E), let us define the score of an edge as its weight, and the score of a path as the minimum of the scores of its edges. For each pair of vertices (u, v), let us define a best path as a path with the maximal score, that starts at u and ends at v. Your task is to find out the score of a best path over all pairs of distinct vertices (u, v) given the description of the graph G.

### Input

 The first line contains V, the number of vertices, and E, the number of edges in the graph. The graph will be weighted, undirected, simple (no self loops and no parallel edges), and connected. Each of the next E lines contains three non-negative integers u, v, and w, denoting that there is an edge (u, v) in the graph with a score of w. u and v are guaranteed to be distinct, and no edge will repeat in the input.

### Output

 Output a total of V lines each containing V integers. The vth integer on the uth line should be 0 if u = v, or the score of a best path that starts at vertex u and ends at vertex v.

### Constraints
2 ≤ V ≤ 1000

V - 1 ≤ E ≤ V(V - 1)/2

0 ≤ u, v ≤ V - 1

0 ≤ w ≤ 10^8

###  Warning Large Input/Output. Use faster Input/Output techniques.

---

## Examples

**Example 1**

**Input**

```text
3 3
0 1 1
1 2 2
0 2 3
```

**Output**

```text
0 2 3
2 0 2
3 2 0
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/RG_01/)

[Contest](http://www.codechef.com/JUNE11/problems/RG_01/)

### DIFFICULTY

EASY

### EXPLANATION

The problem is of finding a path such that the weight of the edge with minimal weight, on the path, is maximized for all pairs of distinct vertices (u, v). Let us call such a path, a maximal path for (u, v). Let’s first try to understand a simple and slower dynamic programming solution similar to that of Floyd-Warshall’s All Pairs Shortest Paths. Let minimal[u][v][k] denote the minimal weight of an edge for a path that starts at node u, ends at node v, and the only intermediates are vertices 1, 2, …, k where the nodes are numbered from 1. We set minimal[u][v][0] to the weight of the edge (u, v), if it exists, or otherwise we set it to 0. We can compute minimal[u][v][k + 1] given minimal[x][y][k], for all x, y in V, as follows:

Clearly, the maximal path either passes through vertex k + 1, or it does not. This allows us to write:

minimal[x][y][k + 1] = MAX(MIN(minimal[x][k + 1][k], minimal[k + 1][y][k]), minimal[x][y][k])

So we can use O(V ^ 3) time and O(V ^ 3) space to solve the problem, but clearly the constraints are much higher.

Let us look at a next approach: Let us maintain a disjoint set data structure to keep track of vertices which are in same/different components. We start with the heaviest weight edge, and process edges in order of decreasing weight. Each time we find an edge that connects two vertices u and v, with different components, we merge the two components and for each vertex x that is in the first component, and for each vertex y in the second component, we set the value of minimal[x][y] to the weight of the edge (u -> v). We do this since there will be always be an edge on a path connecting x and y such that the weight of this edge will be lesser than or equal to the weight of the edge (u -> v), and so we know that this strategy will result in an optimal solution. We can reduce this problem further by seeing that we are computing nothing but the maximum spanning tree of the graph. We can compute the maximum spanning tree of the graph using Kruskal’s Algorithm in O(E * log(V)) time by sorting the edges, but this is likely to timeout because sorting the edges will take O(V ^ 2 * log(V)) time. We can use Radix Sort in base 2 ^ 15 (to speed up modulus calculations) and sort the edges in linear time, O(E) (2 ^ 15 is much less than the maximal number of edges). If we use path compression, and the union by rank heuristic, we’ll get a running time of O(V ^ 2 * alpha(V)), where alpha(n) is the inverse of the ackermann function. Once the maximum spanning tree has been computed, we can run a dfs/bfs from each vertex of the graph and fill the entries of the minimal array in O(V ^ 2) time. The time limits of this problem were kept strict so that solutions using weaker methods could not pass the system tests.

### SETTER’S SOLUTION

Can be found [here1](http://www.codechef.com/download/Solutions/2011/June/Setter/MaxSpanningTree.cpp) & [here2](http://www.codechef.com/download/Solutions/2011/June/Setter/FloydWarshall.cpp)

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/June/Tester/RG_01.cpp)

</details>
