# Ancient Berland Roads

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABROADS |
| Difficulty Rating | 2324 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ABROADS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ABROADS) |

---

## Problem Statement

In Ancient Berland, there were **N** towns, along with **M** bidirectional roads connecting them. With time, some roads became unusable, and nobody repaired them.

As a person who is fond of Ancient Berland history, you now want to undertake a small research study. For this purpose, you want to write a program capable of processing the following kinds of queries:

- D** K** : meaning that the road numbered **K** in the input became unusable. The road numbers are 1-indexed.

- P** A x** : meaning that the population of the **A**th town became **x**.

Let's call a subset of towns a **region** if it is possible to get from each town in the subset to every other town in the subset by the usable (those, which haven't already been destroyed) roads, possibly, via some intermediary cities of this subset. The **population** of the region is, then, the sum of populations of all the towns in the region.

You are given the initial road system, the initial population in each town and **Q** queries, each being one of two types above. Your task is to maintain the size of the most populated region after each query.

### Input

The first line of each test case contains three space-separated integers — **N**, **M**, and **Q** — denoting the number of cities, the number of roads, and the number of queries, respectively.

The following line contains **N** space-separated integers, the **i**th of which denotes the initial population of the **i**th city.

The **j**th of the following **M** lines contains a pair of space-separated integers — **Xj, Yj** — denoting that there is a bidirectional road connecting the cities numbered **Xj** and **Yj**.

Each of the following **Q** lines describes a query in one of the forms described earlier.

### Output

Output **Q** lines. On the **i**th line, output the size of the most populated region after performing **i** queries.

### Constraints

- **1** ≤ **Xj**, **Yj** ≤ **N**

- Roads' numbers are 1-indexed.

- There is no road that gets removed twice or more.

- **1** ≤ **Pi** ≤ **105**

- Subtask 1 (30 points) : **1** ≤ **N**, **M**, **Q** ≤ **103**

- Subtask 2 (70 points) : **1** ≤ **N**, **M**, **Q** ≤ **5 × 105**

### Example
`**Input:**
3 3 6
1 2 3
1 2
2 3
3 1
P 1 3
D 1
P 2 3
D 2
P 3 10
D 3

**Output:**
8
8
9
6
13
10
`

### Explanation

- After the first query, the populations are **(3, 2, 3)** and the most populated region is **{1, 2, 3}**.

- After the second query the populations and the regions remain the same.

- After the third query the populations are **(3, 3, 3)** and the most populated region is again **{1, 2, 3}**.

- After the fourth query the populations remain the same, but we have two regions: **{1, 3}** and **{2}**. The most populated region is **{1, 3}**.

- After the fifth query the populations become equal to **(3, 3, 10)** respectively, and the most populated region is again **{1, 3}**.

- After the last query we have populations the same, but now every city forms it own separate region, and the most populated region is region **{3}**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/ABROADS)

[Contest](http://www.codechef.com/LTIME31/problems/ABROADS/)

# Difficulty:

Medium

# Pre-requisites:

Disjoint Set Union

# Problem:

Maintain the size of the most populated region after each query.

# Explanation:

## Solution for the subtask 1 (21 points):

The solution of this subtask is to use [breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) after applying each query to find all the regions’ city sets. If we have all the regions’ cities sets, we can easily find the maximal populated region.

Let’s describe this approach in more details.

Let’s denote:

-

Integer array P, where P[i] is the population of city numbered the ith.

-

Boolean array D, where D[j] is **true**, if the road numbered the jth has been destroyed, and **false** otherwise.

-

[Adjacency list](https://en.wikipedia.org/wiki/Adjacency_list) Adj. We can store this list efficiently, for example, using STL vector in C++. For every adjacent node, let’s store a structure, containing the following fields:

- The number of the adjacent node, denoted by node.

- The ID of the corresponding edge, denoted by edge.

Having all this, we can process the queries in the following way:

-

P x y - change the population of the city numbered the xth to y. In this case, we just make a single assignment: P[x] = y. This operation is performed in O(1).

-

D x - destroy the road numbered the xth. Again, this is just a single assignment (D[x] = **true**), so it is also performed in O(1).

Now, how to find the size of the maximal populated region.

We will make use of [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) data structure.

Let’s iterate through all the nodes. Whenever we find a node which was not included in any connected component, we start the breadth first search. Let’s describe it in brief:

- Add the first node of the region to the queue.

- While the queue is not empty, pick the node from the head of the queue and add all its’ not yet added neighbors.

Let’s denote Boolean array Used, where Used[i] is **true**, if ith city was added to queue, and **false** otherwise.

The pseudocode of the algorithm for finding the size of the most populated region is given below.

``ans = 0;
For i := 1 to N
	used[i] = false
For i := 1 to N
	if not used[i]
 		queue.add(i);
		population = 0;
		while queue is not empty do
			curNode = queue.pop();
			population += P[curNode];
 			For j := 0 to Adj[curNode].Length
				if ((not D[Adj[curNode][j].edge]) and (not Used[Adj[curNode][j].node]))
					Used[Adj[curNode][j].node] = true;
					queue.add[Adj[curNode][j].node];
		ans = Max(ans, population);
return ans

``

The complexity is O(Q*(N+M)).

## Solution for all subtasks:

We will use the data structure called [Disjoint Set Union](https://en.wikipedia.org/wiki/Disjoint-set_data_structure).

Let’s have N elements numbered 1 to N and N sets. Initially, the ith set contains the ith element.

Disjoint Set Union maintains two basic operations:

-

Uniting two sets.

-

Finding the set containing the given element.

The amortized time per operation is O(\alpha(N)), where \alpha(N) is less than 5 for all remotely practical values of N.

Note that you don’t have to output the size of the most populated region before reading the next query. So, you can read all the queries in advance and solve the task in reverse order.

Assume that all Q queries were performed. Let’s add all connected components (regions) to the DSU. Obviously, we can determine the most populated region.

Let’s create the DSU with N elements denoting the cities and N sets denoting the regions. Along with each set (say, the Xth), let’s maintain the value of P[X], denoting the total population of the cities in the Xth set. Now, the DSU corresponds to the road system with N cities, given populations and without roads. Note that we should take the populations that are obtained after the performing of all the queries.

Now, assume that all the queries has already been performed. Then, there is a set of roads, which has not been deleted. Let’s add all of them. The addition of the road is simply merging two corresponding sets in the DSU structure. Since we have one non-standard operation here, namely, handling the sizes of the regions, let?s give a pseudocode for it.

Given that we need to add a road connecting the city numbered the Xth and the city numbered the Yth.

``
Merge (X, Y)
	setX = FindSet(X)
	setY = FindSet(Y)
	if (setX == setY)
		return;
	SetParent(setY, setX)
	P[setX] = P[setX] + P[setY]

``

Now, let’s “rollback” the queries starting with the last one. The “rollback” of the change population query is changing the value of the corresponding P[X], and the “rollback” of the road deletion query is adding the road like we’ve described above.

Meanwhile, we can also maintain a priority queue of an STL set for determining the size of the largest region quickly. This way, we can answer on the maximal region population in O(\log N).

The complexity is O(N + M \alpha(N) + Q \log N).

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/LTIME31/Setter/ABROADS.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/LTIME31/Tester/ABROADS.cpp)

</details>
