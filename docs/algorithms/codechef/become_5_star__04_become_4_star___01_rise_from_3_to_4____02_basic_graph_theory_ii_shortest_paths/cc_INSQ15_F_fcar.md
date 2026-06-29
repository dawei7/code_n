# FCAR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSQ15_F |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [INSQ15_F](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/INSQ15_F) |

---

## Problem Statement

Cars of future no longer need fuel to run, but they are fitted with special engines which can only operate in one of the two **modes** at a time ,either go **up the road**, or go **down the road**.

There are **N** towns in country. ith town is at height **H[i] (1 ≤ i ≤ N)** above the sea level.

Changing mode of the car requires permissions from mayor of the town you are currently at. Mayor of **ith **town charges amount **C[i] (1 ≤ i ≤ n)** for giving permission to change mode of the car.

These N towns are connected by **R** bidirectional roads. Initially no mode is set, so you need permissions to set a mode.

You have to travel from town 1 to N, in minimum amount of cost. Print minimum money required to make the travel. If it is impossible print -1.

**Note:**

- Go up the road mode: when you are at town A and want to go to town B, where H[A] <= H[B]

- Go down the road mode: when you are at town A and want to go to town B, where H[A] >= H[B]

- If you continue with the same mode, you do not need to take permissions from mayor.

### Input

- First line contains two space separated integer N and R, number of towns and number of roads.

- Next line contains N space separated integer where ith integer is H[i], height of ith town.

- Next line contains N space separated integer where ith integer is C[i], cost charged by mayor of ith town to give permission for changing the mode.

- Next R lines contains two space separated integer u and v, specifying there is a bidirectional road between town u and v.

### Output

Print minimum cost required for travel. If it is impossible print -1.

### Constraints

- **2** ≤ **N** ≤ **100000**

- **1** ≤ **R** ≤ **500000**

- **1** ≤ **H[i]** ≤ **109**

- **1** ≤ **C[i]** ≤ **109**

### Example
`**Input:**
6 6
10 5 7 15 20 6
1 1 1 1 1 1
1 2
2 3
3 6
1 4
4 5
5 6

**Output:**
2
`

### Explanation

There are two paths from 1 - 6

**P1: (1, 2, 3, 6)**

You need to pay $1 to mayor of town 1 to chose down mode. (H[1] >= H[2])

You need to pay $1 to mayor of town 2 to chose up mode. (H[2] <= H[3])
You need to pay $1 to mayor of town 3 to chose down mode. (H[3] >= H[6])

Total cost = $3

**P2: (1, 4, 5, 6)**

You need to pay $1 to mayor of town 1 to chose up mode. (H[1] <= H[4])

You continue with the previous up mode. (H[4] <= H[5])

You need to pay $1 to mayor of town 5 to chose down mode. (H[5] >= H[6])

Total cost = $2

So minimum money required is $2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/INSQ15_F)

[Contest](https://www.codechef.com/INSQ2015/problems/INSQ15_F)

**Author:** [vishfrnds](http://www.codechef.com/users/vishfrnds)

**Tester:** [codefor6768](http://www.codechef.com/users/codefor6768)

**Editorialist:** [vishfrnds](http://www.codechef.com/users/vishfrnds)

### DIFFICULTY:

MEDIUM

### PREREQUISITES:

[dijkstra’s algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

basic graph theory

### PROBLEM:

Given a graph of N nodes.

i-th node has a height H[i], and cost C[i].

You can travel nodes in one of the mode either non-decreasing order of height or non-increasing order of height of nodes. Whenever you change mode on i-th node it will cost you C[i].

Find the path of minimum cost from node 1 to N.

### QUICK EXPLANATION:

Split the given graph into two graphs each of N nodes. Where each graph have a subset directed edges of 0 cost, representing single mode only. Connect the corresponding nodes from both graph with undirected edge of cost C[i].

Add a source node and connect it with node 1 of both graphs with cost C[i].

Add a destination node and connect it with node N of both graphs with cost 0.

Apply Dijkstra algorithm to find smallest cost path between source and destination.

### EXPLANATION:

Make a copy of given graph G1, let it be G2.

G1 will have a directed edge from node A to B if and only if H[A] <= H[B] and there was edge between A and B in orignal graph, delete all other edges.

G2 will have a directed edge from node A to B if and only if H[A] >= H[B] and there was edge between A and B in orignal graph, delete all other edges.

Now G1 represents mode “up the road” (i.e. non-decreasing mode).

Now G2 represents mode “down the road” (i.e. non-increasing mode).

All the edges in G1 and G2 have cost 0. This represent it will not cost you anything as long as you are in single graph.

Now to allow changing of mode we will connect corresponding nodes of both the graph with cost C[i] of that node.

Thus, whenever you will change mode on i-th node it will cost C[i].

Now we will add a source and destination node.

Source node will be connected to node 1 of G1 with cost C[1] and node 1 of G2 with cost C[1]. Because you need to pay to chose initial mode.

Destination node will be connected to node N of G1 with cost 0 and node N of G2 with cost 0. Because it makes no difference wether you end up on G1’s node N or G2’s node N.

So if given graph had n nodes e edges, final graph will have node N = 2 * n + 2 and edges E = e + n + 4

Now we will use dijkstra’s algorithm to find minimum cost path from source to destination in this new graph.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution.

`` /* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Vishwas Tripathi
 * CSE, MNNIT-ALLAHABAD
 * vishfrnds@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

#define MP make_pair
#define pb push_back
#define X first
#define Y second

typedef long long ll;

#define INF (ll)1e18

long long dijk (int st, int end, vector<pair<int, int> > G[], int n) {
	vector<long long> dist (n, INF);
	dist[st] = 0;
	set<pair<long long, int> > q; // cost, node
	q.insert (make_pair (0, st));
	while (!q.empty ()) {
		pair<long long, int> top = *q.begin ();
		q.erase (q.begin ());
		int v = top.second;
		long long d = top.first;
		if (v == end)
			break;
		for (vector<pair<int, int> >::iterator it = G[v].begin (); it != G[v].end (); it++) {
			int v2 = it->first;
			long long cost = it->second;
			if (dist[v2] > dist[v] + cost) {
				if (dist[v2] != INF) {
					q.erase (q.find (make_pair (dist[v2], v2)));
				}
				dist[v2] = dist[v] + cost;
				q.insert (make_pair (dist[v2], v2));
			}
		}
	}
	if (dist[end] == INF) {
		return -1;
	}
	return dist[end];
}

int main()
{
	int t, n, m, i, j, x, y;
	cin >> n >> m;
	vector<int> h(n + 1), c(n + 1);
	vector<pair<int, int> > G[2 * n + 2];
	for (i = 1; i <= n; i++) {
		cin >> h[i];
	}
	//G1 from 1 to N
	//G2 from N + 1 to 2 * N
	for (i = 1; i <= n; i++) {
		cin >> c[i];
		G[i].pb (MP (n + i, c[i]));
		G[n + i].pb (MP (i, c[i]));
	}
	for (i = 1; i < m; i++) {
		cin >> x >> y;
		if (h[x] <= h[y])
			G[x].pb (MP (y, 0));
		if (h[x] >= h[y])
			G[n + x].pb (MP (n + y, 0));
		if (h[y] <= h[x])
			G[y].pb (MP (x, 0));
		if (h[y] >= h[x])
			G[n + y].pb (MP (n + x, 0));
	}
	G[0].pb(MP (1, c[1]));
	G[0].pb(MP (n + 1, c[1]));
	G[n].pb(MP (2 * n + 1, 0));
	G[2 * n].pb(MP (2 * n + 1, 0));
	cout << dijk(0, 2 * n + 1, G, 2 * n + 2);
    return 0;
}
``

</details>
