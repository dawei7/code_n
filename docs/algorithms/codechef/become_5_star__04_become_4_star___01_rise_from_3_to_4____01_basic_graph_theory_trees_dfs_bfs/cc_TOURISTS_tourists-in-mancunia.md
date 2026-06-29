# Tourists in Mancunia

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOURISTS |
| Difficulty Rating | 2133 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [TOURISTS](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/TOURISTS) |

---

## Problem Statement

The grand kingdom of Mancunia is famous for its tourist attractions and visitors flock to it throughout the year. King Mancunian is the benevolent ruler of the prosperous country whose main source of revenue is, of course, tourism.

The country can be represented by a network of **unidirectional** roads between the cities. But Mancunian, our benign monarch, has a headache. The road network of the country is not **tourist-friendly** and this is affecting revenue. To increase the GDP of the nation, he wants to redirect some of the roads to make the road network **tourist-friendly** and hence, ensure happiness and prosperity for his loyal subjects.

Now is the time for some formal definitions. :(

A road network is said to be **tourist-friendly** if for every city in the country, if a tourist starts his journey there, there is a path she can take to visit each and every city of the nation and traverse each road **exactly once** before ending up at the city where she started.

Given a description of the road network of Mancunia, can you come up with a scheme to redirect some (possibly none) of the roads to make it **tourist-friendly**?

### Input

The first line contains two integers **N** and **E** denoting the number of cities and roads in the beautiful country of Mancunia respectively.

Each of the next **E** lines contains two integers **a** and **b** implying that there is a unidirectional road from city **a** to city **b**.

It is guaranteed that there aren't multiple roads in the exact same direction and that there is no road from a city to itself.

### Output

If there is no solution, print "NO" (without quotes). Else, print "YES" (without quotes), followed by exactly **E** lines.

The **ith** line of output should represent the **ith** road in the input. It should have two integers **a** and **b** denoting that the final orientation of that road is from **a** to **b**.

### Constraints

- **1** ≤ **N** ≤ **100000**

- **1** ≤ **E** ≤ **200000**

- **1** ≤ **a, b** ≤ **N**

**Subtask 1: (20 points)**

- **1** ≤ **N** ≤ **20**

- **1** ≤ **E** ≤ **21**

**Subtask 2: (80 points)**

- **Same as original constraints**

---

## Examples

**Example 1**

**Input**

```text
3 3
1 2
2 3
3 1
```

**Output**

```text
YES
1 2
2 3
3 1
```

**Example 2**

**Input**

```text
3 2
1 2
2 3
```

**Output**

```text
NO
```

**Example 3**

**Input**

```text
5 6
1 2
2 3
3 4
2 4
2 5
1 5
```

**Output**

```text
YES
1 2
2 3
3 4
4 2
2 5
5 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/TOURISTS)

[Contest](https://www.codechef.com/JAN17/problems/TOURISTS)

**Author:**  [Satyaki Upadhyay](https://www.codechef.com/users/satyaki3794)

**Tester:**  [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Misha Chorniy](https://www.codechef.com/users/mgch)

## Difficulty:

Easy

# Pre-Requisites:

graphs, Euler Circuits

## Problem Statement

Given an directed graph, orient each edge in such way that exists way which going over all edges and passes on each edge only once from every node and visits all nodes at least once.

## Quick Explanation

We need to check whether is given graph exists Euler Circuit and if it’s connected. In the positive case, such tour as in the statement exists.

## Explanation

Assume that graph is undirected, and we need to direct every edge in it. If the graph is not connected, then road network in the kingdom of Mancunia can not be tourist-friendly in any way. Because no one tour can visit all cities.

Consider desired orientation of edges, and path from some city s, (u_{1}, u_{2}), (u_{2}, u_{3}), .... (u_{E-1}, u_{E}), (u_{E}, u_{1}). What we can say about this path, it passes over all cities, so if we rotate this sequence, we can obtain path which satisfied the statement for any city. Denote in_{a}, out_{a} - [indegree and outdegree](https://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree) for city a respectively. In the path, how many times we will enter the city, as many time we will leave him, so  in_{a} = out_{a}, but this criterion is very well-known in Graphs Theory, it’s criteria of existing of [ Euler Circuit. ](https://www.math.ku.edu/~jmartin/courses/math105-F11/Lectures/chapter5-part2.pdf) As we have the undirected graph, we need to check, if every node has even degree, this one is enough for existing of Euler Circuit.

How to find Euler Circuit in the graph? You can read about algorithms [ here](https://en.wikipedia.org/wiki/Eulerian_path#Constructing_Eulerian_trails_and_circuits). Let’s write some code for this problem here using Hierholzer’s algorithm:

``
S[v] - set of adjacent nodes to v if graph is undirected
DFS(v) 	//recursive function
	while !S[v].empty()	//While exists undirected edges from node v
		to = minimalValue(S[v])	//Choose any undirected edge
		S[v].erase(to);		//Erase edge (v, to)
		S[to].erase(v);
		//Orient edge in direction (v->to)
		DFS(to)

``

After finding of the circuit, let’s orient edges in that order.

The overall complexity of this solution is O(N+E) or O((N+E) log N)

## Solution:

Setter’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Setter/TOURISTS.cpp)

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Tester/TOURISTS.cpp)

**Please feel free to post comments if anything is not clear to you.**

</details>
