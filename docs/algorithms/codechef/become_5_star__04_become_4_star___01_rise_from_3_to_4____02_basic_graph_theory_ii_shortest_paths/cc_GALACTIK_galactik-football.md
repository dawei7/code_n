# Galactik Football

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GALACTIK |
| Difficulty Rating | 1860 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [GALACTIK](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/GALACTIK) |

---

## Problem Statement

It's Galactik Football time! The Galactik Football Assosiation (GFA) has announced a football tournament between all the teams of all the planets in the galaxy.

Each planet of the galaxy has a government. Some governments have a mutual agreement between them. If planet $A$ has mutual agreement with planet $B$, then there is a bidirectional spaceway between $A$ and $B$, using which anybody can go from $A$ to $B$ and vice-versa. People can use these spaceways to travel from one planet to another, if there exists a path between them using some of the spaceways.

Each planet has its own football ground. The GFA has planned the matches in such a way that a team can have a match at any of these grounds. The GFA has come across some problems in the execution of their plan. They have found out that there are many pairs of planets between which there does not exist any path, so the football team of one of those planets can't reach the other planet. They requested the corresponding governments to make a spaceway between them, but they can’t because of the absence of a mutual agreement. So the GFA suggested that they will make teleportation devices between some pairs of planets which will be used only by the football teams to travel.

But there are two types of governments in the galaxy
1. Some of the governments are greedy and they want to make money through the GFA. Each of these government has asked the GFA for a tax value which it has to pay if it wants to make a teleport ending at their planet.
2. Others want to sponsor the event, so they will give money to the GFA if they make a teleport ending at their planet. The GFA would always avoid such governments no matter what the consequences are, because these kind of governments always have some dirty plans up their sleeves.

Now, the GFA wants to make bi-directional teleports between planets such that the football teams of any planet can reach any other planet to play a football match, using spaceways between the planets and/or teleports made by the GFA.

The GFA also has financial problems and want to spend as little money as possible. They have come to you so that you can help them calculate the minimum amount of money needed to fulfil their plan.

### Input
- The first line of the input consists of two space separated integers - $N$ and $M$. $N$ is the number of planets and $M$ is the number of spaceways. The description of the spaceways follows.
- The next $M$ lines, each contain two space separated integers $A$ and $B$, denoting a mutual agreement and hence a spaceway to travel, between planet $A$ and planet $B$.
- The next $N$ lines each contain a single integer, the integer on the $i^{th}$ line representing $C_i$. If $C_i \geq 0$, then it represents the tax value which the GFA has to pay to the government of planet $i$ (it's a type $1$ government). If $C_i < 0$, then it represents the money that the $i^{th}$ government will pay to the GFA (it's a type $2$ government).

### Output
Print the minimum amount needed for the GFA to fulfil their plan. If there is no way to do so, print "-1" (without quotes).

### Constraints
- $1 \leq N \leq 10^5$
- $0 \leq M \leq 10^6$
- $0 \leq |C| \leq 10^4$
- $1 \leq A,B \leq N$
- $A \neq B$

---

## Examples

**Example 1**

**Input**

```text
6 6
1 2
2 3
1 3
4 5
5 6
4 6
1
3
5
2
4
6
```

**Output**

```text
3
```

**Example 2**

**Input**

```text
3 1
2 3
1
-1
-1
```

**Output**

```text
-1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](http://www.codechef.com/problems/GALACTIK)

[Contest](http://www.codechef.com/JULY13/problems/GALACTIK)

### DIFFICULTY

EASY

### PREREQUISITES

[Disjoint Set Data Structure](http://en.wikipedia.org/wiki/Disjoint-set_data_structure), Simple Math

### PROBLEM

There are **N** nodes in a graph labeled from **1** to **N**. Each node has an associated cost with it, given by cost array. You wish to connect this graph by constructing edges between the nodes.

- You can construct an edge between two nodes **a** and **b** iff **cost[a] ? 0 AND cost[b] ? 0**

- The cost of the construction of the edge is equal to **cost[a] + cost[b]**

Some edges already exist. Hence, some nodes are already connected. You wish to find the minimum cost of connecting the entire graph.

### QUICK EXPLANATION

We will be using a **Disjoin Set Data Structure** that supports the following operations

-
**init(N)**, initialize **N** disjoint sets.

-
**find(A)**, get the id of the disjoint set to which **A** belongs.

-
**join(A,B)**, merge the two disjoint sets in which **A** and **B** belong respectively.

**Union-Find** along with **Union by Rank** and **Path Compression** is the asymptotically optical way of maintaining **Disjoint Sets**.

After considering the existing set of edges, we will have some disjoint sets, where there are one or more nodes in each set. Let us assume there are **K** disjoint sets.

**We only need to put K-1 edges**

This is easily proven by considering that adding each edge reduces the number of disjoint sets by **1**. If it doesn’t, then the edge is connecting two nodes that are already connecetd.

Thus, we only consider **K-1** edges at most.

### EXPLANATION

As we dwell deeper into discussing the solution to the problem we will encounter a lot of difficulty discussing the ideas if we keep reminding ourselves of **ignoring the vertices with negative costs**. To be able to handle them in the discussion below (and maybe in your implementation as well), we assume that each negative cost is replaced by a **very large positive cost**. We will see soon that doing this does not affect the **optimal answer**.

We can consider each disjoint set as an independent vertex and try to build a [minimum spanning tree](http://en.wikipedia.org/wiki/Minimum_spanning_tree) on the graph. The problem is, that for **K** disjoint sets, there may be as many as **KC2** edges. We know that we can solve the problem of finding the **minimum spanning tree** by greedily considering the edges in **increasing order of weights**.

Here comes to our rescue the definition of the weight of edges in the problem statement.

**Edge Weight for edge from a to b = cost[a] + cost[b]**

Let **x** be the vertex for which **cost[x]** is **smallest**. An edge between **x** and any other vertex will have a lower cost than **any other edges** in the graph.

Also, considering all the edges with one end point on **x** means we are considering sufficient edges for a connected graph!

Note how assuming that all negative cost vertices were actually **very large positive cost** edges allows us to get around several edge cases

- The lowest cost vertex, **x**, is automatically the lowest non-negative cost vertex

- We will consider all the edges from **x** to other vertices in the order of increasing weights, thus we avoid considering edges to vertices with negative weights

- If we are forced to consider an edge to a vertex with large weight (negative cost vertex originally), then we know that we **could not have** connected to the connected component of that vertex through any vertex whose weight was positive (otherwise we already would be connected to that component).

Hence, if the answer could be reached **before** connecting to any vertex with very large weight, we can print the answer, otherwise, we will print **-1**.

Note that we can avoid the sorting step altogether and consider the **minimum cost vertices** in each **connected component**. This way, if we know the **sum of costs** of the **minimum cost vertices** in each component, the answer is simply

`cost[x] * (K-1) + sum - cost[x]
`

Where **x** is the vertex with the smallest cost.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/July/Setter/GALACTIK.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/July/Tester/GALACTIK.cpp).

</details>
