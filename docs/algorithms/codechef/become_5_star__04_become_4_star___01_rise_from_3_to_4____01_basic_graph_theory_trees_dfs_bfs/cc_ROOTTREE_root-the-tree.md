# Root the Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROOTTREE |
| Difficulty Rating | 1934 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [ROOTTREE](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/ROOTTREE) |

---

## Problem Statement

A *directed tree* is a directed graph such that if all edges were undirected, this graph would be a tree. A *rooted directed tree* is a directed tree in which there is one vertex (the *root*, let's denote it by $r$) such that it is possible to reach all vertices of the graph from $r$ by moving along the directed edges.

You are given a directed tree with $N$ vertices (numbered $1$ through $N$). You may perform the following operation on it any number of times (including zero):
- Choose some edge which currently exists in the graph.
- Remove this edge.
- Add a new edge in such a way that the graph becomes a directed tree again.

What is the smallest number of operations which need to be performed in order to make the directed tree rooted?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Each of the next $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that there is a directed edge from $u$ to $v$ in the tree.

### Output
For each test case, print a single line containing one integer ― the smallest number of operations we need to perform to create a rooted directed tree.

### Constraints
- $1 \le N \le 10^4$
- $1 \le u, v \le N$
- the graph described on the input is a directed tree
- the sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
**Subtask #1 (20 points):** for each edge, $u = 1$ or $v = 1$ (the graph is a directed star)

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2
3 2
3
1 2
2 3
```

**Output**

```text
1
0
```

**Explanation**

**Example case 1:** We can delete the edge from vertex $3$ to vertex $2$ and insert an edge from $3$ to $1$. Then, the graph becomes a rooted directed tree with vertex $3$ as the root. However, there are many other possible solutions.

**Example case 2:** The graph is already a rooted directed tree; the root is vertex $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2
3 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
1 2
2 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Division 1](https://www.codechef.com/LTIME88A/problems/ROOTTREE)

[Division 2](https://www.codechef.com/LTIME88B/problems/ROOTTREE)

[Practice](https://www.codechef.com/problems/ROOTTREE)

**Author:** [Anton Trygub](https://www.codechef.com/users/anton_trygub)

**Tester:** [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:** [Colin Galen](https://www.codechef.com/users/galencolin)

[(My) video](https://youtu.be/TB_krkk_U9A?t=835)

[Official video](https://www.youtube.com/watch?v=Joezp9YzE5M)

# DIFFICULTY:

Easy

# PREREQUISITES:

Graphs, Trees

# PROBLEM:

You’re given a directed tree (if the graph was undirected, the edges would form a tree) with n vertices. You want to give this tree a “root” - a vertex r where you can reach all other vertices by traversing some edges starting from r. You can perform some number of the following operation: remove some edge, then add another edge such that the graph remains a directed tree. Find the mininum required number of such operations to root the tree.

# QUICK EXPLANATION:

Subtask 1

Either the final root will be vertex 1 (the center of the star), or some other vertex v. In the first case, the answer is the indegree of the center. In the second case, that node must point toward the star and the star must point to every other vertex, so the answer is the cost of flipping the edge 1 \to v if necessary, plus the cost of flipping all other edges to point away from 1.

Main solution

The only condition is that each vertex must have indegree \leq 1. One operation can decrease the indegree of exactly one vertex by 1, so the required number of operations is the number of operations to decrease each indegree to a number \leq 1, which can be summarized as \displaystyle \sum_{i = 1}^{n}{max(indegree[i] - 1, 0)}.

# EXPLANATION:

Subtask 1

Either the final root will be vertex 1 (the center of the star), or some other vertex v. Let’s consider both cases separately.

In the first case, the answer is the indegree of the center 1, since everything has to be outgoing from the center. You can flip an edge in 1 operation, and you can’t do better because either you have to connect the newly detached vertex (from removing the edge) to the center, or to some other vertex, but either way it essentially only affects that vertex.

In the second case, that vertex v must point toward the star and the star must point to every other vertex, so the answer is the cost of flipping the edge 1 \to v if necessary, plus the cost of flipping all other edges to point away from 1. This can be done in O(1) for each v with a bit of casework.

The final answer is the minimum over both cases.

Main solution

One commonly used property of trees is that every vertex except the root has exactly one parent. If we consider the final, rooted tree that we’ll get after some operations, this will also be true in the directed version. Indeed, if any vertex has more than one parent, you wouldn’t be able to move from one parent to another, and thus the tree wouldn’t be rooted.

If every vertex except the root has one parent, then the tree is also automatically rooted.

Proof

Consider any vertex v. Either v is the root, or it has a parent. In the second case, we can set v to v's parent and restart the process. Because the graph is a directed tree, there are no cycles, so we’ll never visit any vertex multiple times. Thus, this process will eventually stop at the root, meaning we can reach v from the root through that sequence of edges.

So this condition is both necessary and sufficient for the tree being rooted.

Any parent of a vertex v, by the definition of the problem, has an edge directed toward v. If a vertex has more than one parent, then its indegree - the number of edges that go into it - will be greater than 1. So in the final tree, **we need all indegrees to be at most** 1 (the root itself will have indegree 0). Note that it’s not possible for more than one vertex to have indegree 0 in the final tree, because if so, we can use the pigeonhole principle to show that some other vertex has indegree > 1.

So we need to decrease the indegree of each vertex to \leq 1. When we remove an edge, it decreases the indegree of exactly one vertex by 1, so the required number of operations is either 0 if the indegree is already \leq 1, or the indegree minus 1 if we need to do some operations on it. This can be succinctly written as \max(indegree - 1, 0), and the answer is the sum of this quantity over all vertices.

The final part is showing that the new edges we introduce don’t create more operations we have to do. If we reverse the pigeonhole principle, we can show that if we have a vertex with indegree > 1, we have at least two with indegree 0. So we can create an edge that goes into one of those vertices and points from some vertex in the other component we got from removing the edge, not creating extra operations we have to do in the future.

# TIME COMPLEXITY:

Subtask 1

O(n) for reading in the input, computing the star, and computing all other vertices (O(1) each).

Main solution

O(n) for reading in the input and computing indegrees.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin>>n;
    vector<int> in(n);
    for (int i = 0; i<n-1; i++)
    {
        int u, v;
        cin>>u>>v;
        u--; v--;
        in[v]++;
    }
    int cnt = 0;
    for (auto it: in) if (it==0) cnt++;
    cout<<cnt-1<<endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    int t; cin>>t;
    while (t--) solve();
}
``

Note that counting 0's is equivalent to counting edges we need to remove, because we also have the constraint that the final array of degrees has exactly one 0.

Tester's Solution
``#include <bits/stdc++.h>

using namespace std;
using nagai = long long;

int main() {
	 cin.tie(0);
	 ios::sync_with_stdio(false);
	 int t;
	 cin >> t;
	 while(t--) {
		  int n;
			cin >> n;
			vector<int>in(n), out(n);
			for(int i=0;i<n-1;++i) {
				 int a, b;
				 cin >> a >> b;
				 --a, --b;
				 ++out[a];
				 ++in[b];
			}
			sort(in.begin(),in.end());
			int ans = in.front();
			for(int i=1;i<n;++i)
				ans += max(0, in[i] - 1);
			cout << ans << '\n';
	 }
	 return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define send {ios_base::sync_with_stdio(false);}
#define help {cin.tie(NULL); cout.tie(NULL);}
typedef long long ll;

void solve(int tc = 0) {
	ll n;
	cin >> n;

	ll id[n] = {0};
	for (ll i = 0; i < n - 1; i++) {
		ll x, y;
		cin >> x >> y;
		--x; --y;
		++id[y];
	}

	ll ans = 0;
	for (ll i = 0; i < n; i++) ans += max(0LL, id[i] - 1);

	cout << ans << '\n';
}

int main() {
	send help

	int tc = 1;
	cin >> tc;
	for (int t = 0; t < tc; t++) solve(t);
}
``

# Video Editorial(s)

My video: [https://youtu.be/TB_krkk_U9A?t=835](https://youtu.be/TB_krkk_U9A?t=835)

Official video: [https://www.youtube.com/watch?v=Joezp9YzE5M](https://www.youtube.com/watch?v=Joezp9YzE5M)

</details>
