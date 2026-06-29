# Fire Escape Routes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIRESC |
| Difficulty Rating | 1671 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [FIRESC](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/FIRESC) |

---

## Problem Statement

There are $N$ people working in a building, and each one works in a separate cabin. Chef’s employees are numbered by integers from $1$ to $N$, inclusive. Chef wants to ensure the safety of his employees. He wants to have fire escapes in the building and wants to train the employees to use these by conducting mock drills.

Chef knows that the number of people working in his office can be very large. In order to avoid crowding of a common fire escape route during emergency, Chef has decided to build multiple fire escapes. For the safety of every employee, each cabin has a fire exit which is connected to one of the fire escape routes.

A lot of employees are friends with each other. The friendship is mutual. This means that if employee $i$ is a friend of employee $j$ then employee $j$ is a friend of employee $i$ as well. But friendship is NOT necessarily transitive. This means that if employee $i$ is a friend of employee $j$ AND employee $j$ is a friend of employee $k$, then employee $i$ and employee $k$ need not necessarily be friends.

If two employees are friends, they do not want to escape through different routes.
This complicates the task for the Chef. As already mentioned, he wants to have the maximum number of fire escape routes to ensure maximum safety. Also, for every escape route, one of the employees using that route needs to be appointed as the fire drill captain. The captain will be responsible for conducting the mock drills and train all the employees using that route. Your task is simple. Given the number of employees and the friendship list, you need to tell the Chef the maximum number of fire escape routes that he can have in the building and the number of ways of selecting the captains for every route. Since the number of ways can be really large, output this value modulo $10^{9} + 7$.

### Input
- The first line of the input contains a single integer $T$, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$, denoting the number of employees and the number of friendship relations, respectively.
- Each of the following $M$ lines contains two space-separated integers $i$ and $j$, denoting that employee $i$ and employee $j$ are friends.

### Output
For each test case, output a single line containing two space separated integers, denoting the maximum number of distinct fire escape routes that can be constructed and the number of ways of selecting the captains modulo $10^{9} + 7$.

### Constraints
- $1 \leq T \leq 5$
- $1 \leq N \leq 10^{5}$
- $0 \leq M \leq 10^{5}$
- $1 \leq i, j \leq N$
- $ i \neq j$
- For any pair of employees $i$ and $j$ such that $1 \leq i, j \leq N$, at most one pair among $(i, j)$ and $(j, i)$ will appear in the input

---

## Examples

**Example 1**

**Input**

```text
3
4 2
1 2
2 3
5 3
1 2
2 3
1 3
6 3
1 2
3 4
5 6
```

**Output**

```text
2 3
3 3
3 8
```

**Explanation**

**Example case 1:** Here employees $1$ and $2$ are friends and should share the same fire escape. Also employees $2$ and $3$ share the same fire escape. This means employees $1$, $2$, and $3$ will have a common route. But to maximize number of routes Chef could assign another route to employee $4$ since it is not a friend of other employee. So we have two escape routes with the following distribution of employees by routes: $\{1, 2, 3\}$, $\{4\}$. Therefore, there are $3$ ways to chose drill captains: $(1, 4)$, $(2, 4)$, $(3, 4)$, where first element in the pair denotes the captain for the first route and second element denotes the captain for the second route.

**Example case 2:** Here the optimal distribution of employees by routes is $\{1, 2, 3\}$, $\{4\}$, $\{5\}$. Therefore, there are $3$ ways to chose drill captains: $(1, 4, 5)$, $(2, 4, 5)$, $(3, 4, 5)$.

**Example case 3:** Here the optimal distribution of employees by routes is $\{1, 2\}$, $\{3, 4\}$, $\{5, 6\}$. Therefore, there are 8 ways to chose drill captains: $(1, 3, 5)$, $(1, 3, 6)$, $(1, 4, 5)$, $(1, 4, 6)$, $(2, 3, 5)$, $(2, 3, 6)$, $(2, 4, 5)$, $(2, 4, 6)$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/FIRESC)

[Contest](http://www.codechef.com/MARCH13/problems/FIRESC)

### DIFFICULTY

SIMPLE

### PREREQUISITES

Graph Theory, [Union Find](http://en.wikipedia.org/wiki/Disjoint-set_data_structure), [Depth First Search](http://en.wikipedia.org/wiki/Depth-first_search)

### PROBLEM

An Office has several people on which a relationship of **being mutual friends** is defined. Two people who are friends will always choose to accompany each other while escaping from fire.

Under these conditions, what are the maximum number of escape routes may be built such that none of them may be empty.

Also, each set of people who escape together, must have a captain assigned. Count the number of ways of assigning captains.

### QUICK EXPLANATION

Let us define a graph whose vertices are **people**. An **undirected** edge connects two people who are **friends**.

On this graph, two vertices will be of the same **color** if they share an edge. This represents that the two people should have to go in the same fire escape route. We wish to maximize the number of colors used.

**All the vertices in a connected component in this graph will have to be in the same color.**

The above is easy to see because

- If A and B are friends

- and B and C are friends

- Given that A and B should be the same color

- and B and C should be the same color

- A, B and C, all three should be the same color

This observation leads us to the following

**The maximum number of fire escape routes that may be built is equal to the number of connected components.**

The second part of the problem - Finding the ways to assign captains - is equal to the product of the number of vertices in each connected component. This can be derived by simple **permutation / combination**. (Since we need exactly 1 member from each set, the answer must be the product of the cardinality of the sets).

### EXPLANATION

The number of connected components can be found by use of either of the following techniques

## Depth First Search

Since this is an undirected graph, the number of times a Depth First Search starts from an **unvisited** vertex is equal to the number of **connected components**. We would like to store the graph as an **adjacency list** due to the large number of vertices (the number of edges are not too many).

Lets look at dfs implementation in pseudo-code. Both the Setter’s and Tester’s coe use DFS to solve the problem.

`for u = 1 to N
    if u is not visited
        connected_components++
        dfs(u)

dfs(u)
    mark_visited(u)
    for all children v, of u
        if v is not visited
            dfs(v)
`

## Union Find

Union Find or Disjoint Set Data structures allow you to **merge** two sets of items together dynamically and maintain for each item - to which set does it belongs. You can consume a **Union Find** data structure to **join** each pair of friends. At the end of this, just count the number of **distinct components** to get the answer.

`for u = 1 to N
    initialize-new-set-with-1-item(u)

for e = 1 to M /* all edges */
    join-sets( e.first, e.second )

Let cc = Array of size N
for u = 1 to N
    cc[ find-set-root(u) ]++

for u = 1 to N
    if cc[u] > 0
        connected_components++
`

There is one detail missing from the above two approaches. Handling of part 2 of the question. We wish to find the number of items in each connected component and find the product of these numbers.

- In the dfs approach, maintaining a global “size” and incrementing it can solve the problem

- or return the counts in the return value of dfs

- In the disjoint set approach, as demonstrated in the pseudo-code, the array cc stores the number of items in each connected component at the end

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Setter/FIRESC.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Tester/FIRESC.cpp).

</details>
