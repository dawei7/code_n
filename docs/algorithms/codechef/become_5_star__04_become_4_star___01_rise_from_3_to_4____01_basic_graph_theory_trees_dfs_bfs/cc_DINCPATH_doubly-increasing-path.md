# Doubly Increasing Path

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DINCPATH |
| Difficulty Rating | 2493 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [DINCPATH](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/DINCPATH) |

---

## Problem Statement

You are given an undirected graph with $N$ nodes (numbered $1$ through $N$) and $M$ edges. Each node has a value; let's denote the value of node $i$ by $A_i$. Note that the graph is not necessarily simple.

A *doubly increasing path* is a directed path such that both the values of nodes and differences of values of nodes on this path are strictly increasing. Formally, it is a sequence of nodes $p_1, p_2, p_3, \ldots, p_k$ for some integer (the length of this path) $k \ge 1$ such that $0 \lt A_{p_2} - A_{p_1} \lt A_{p_3} - A_{p_2} \lt \ldots \lt A_{p_k} - A_{p_{k-1}}$ and for each valid $i$, nodes $p_i$ and $p_{i-1}$ are connected by an edge.

You need to find the length of the longest doubly increasing path in the graph.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- Each of the following $M$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

### Output
For each test case, print a single line containing one integer — the maximum length of a doubly increasing path.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le M \le 10^5$
- $1 \le u, v \le N$
- $|A_i| \le 10^{15}$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
2
5 4
1 2 3 4 5
2 4
1 5
1 3
3 5
5 4
1 2 3 4 5
3 5
1 2
4 5
5 2
```

**Output**

```text
2
3
```

**Explanation**

**Example case 1:** Any path with length $2$ from a smaller node to a larger one is doubly increasing. There is no doubly increasing path with length greater than $2$.

**Example case 2:** The path $1 \rightarrow 2 \rightarrow 5$ is doubly increasing.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4
1 2 3 4 5
2 4
1 5
1 3
3 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 4
1 2 3 4 5
3 5
1 2
4 5
5 2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/DINCPATH)

[Contest, div. 1](https://www.codechef.com/COOK105A/problems/DINCPATH)

[Contest, div. 2](https://www.codechef.com/COOK105B/problems/DINCPATH)

**Author:** [Udit Sanghi](http://www.codechef.com/users/mathecodician)

**Tester:** [Teja Vardhan Reddy](http://www.codechef.com/users/teja349)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

EASY

**PREREQUISITES**:

Topological sort, directed acyclic graphs, dp

**PROBLEM**:

You’re given undirected graph with N nodes and M edges. Each node has value A_i assigned to it. We will call a path doubly-increasing if both values and differences of values of nodes are strictly increasing. Formally for path p_1, \dots, p_k it should hold that:

0 <A_{p_2} - A_{p_1} < A_{p_3} - A_{p_2} < \dots < A_{p_k} - A_{p_{k-1}}

You need to find the length of the longest double increasing path in graph.

**EXPLANATION**:

Consider edge (u,v) such that A_u<A_v. Let’s  assign weight A_v - A_u to this edge and say that we may only move through it from u to v. Now we have directed graph, moreover this graph is acyclic. In this graph we should find the longest increasing path in terms of edges weights.

To do this we may store dp_{(u,v)} being equal to the maximum length of the path which we may obtain starting from the edge (u,v). You may see that if we sort all edges going from v by their weights, all edges (v,w) which may be used to extend path starting in (u,v) form contiguous suffix in this sorted list (according to condition A_w > 2A_v - A_u).

Thus we may take maximum possible dp_{(v,w)} by using binary search and keeping maximum values on suffixes in sorted lists of edges:

``vector<int> p(N);
iota(begin(p), end(p), 0);
sort(begin(p), end(p), [&](int a, int b){return A[a] > A[b];});
int ans = 1;
for(auto u: p) {
	sort(begin(g[u]), end(g[u]), [&](int a, int b){return A[a] > A[b];});
	int cur = 2;
	for(auto v: g[u]) {
		auto it = lower_bound(begin(g[v]), end(g[v]), 2 * A[v] - A[u],
			[&](int w, int c){
				return A[w] > c;
			});
		if(it != begin(g[v])) {
			cur = max(cur, 1 + dp[v][it - begin(g[v]) - 1]);
		}
		ans = max(ans, cur);
		dp[u].push_back(cur);
	}
}
cout << ans << endl;
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/scCzZm).

Tester’s solution can be found [here](https://ideone.com/sCZj7X).

Editorialist’s solution can be found [here](https://ideone.com/4AbmwN).

</details>
