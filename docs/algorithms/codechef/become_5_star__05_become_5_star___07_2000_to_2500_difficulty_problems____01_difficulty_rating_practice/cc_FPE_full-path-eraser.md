# Full Path Eraser

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FPE |
| Difficulty Rating | 2094 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [FPE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/FPE) |

---

## Problem Statement

There is a rooted tree of $N$ vertices rooted at vertex $1$. Each vertex $v$ has a value $A_v$ associated with it.

You choose a vertex $v$ (possibly the root) from the tree and remove all vertices on the path from the root to the vertex $v$, also including $v$. This will result in a forest of zero or more connected components.

The beauty of a connected component is the $\mathrm{GCD}$ of the values of all vertices in the component. Find the maximum value of the sum of beauties of the obtained connected components for any choice of $v$.

Here, $\mathrm{GCD}$ stands for [Greatest Common Divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the tree.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the values associated with each vertex.
- The next $N-1$ lines contain two space-separated integers $u$ and $v$ — denoting an undirected edge between nodes $u$ and $v$.

It is guaranteed that the edges given in the input form a tree.

---

## Output Format

For each test case output the maximum value of the sum of beauties of the obtained connected components for any choice of $v$.

---

## Constraints

- $1 \leq T \leq 2\cdot10^4$
- $1 \leq N \leq 3\cdot10^5$
- $1 \leq A_i \leq 10^9$
- $1 \leq u,v \leq N$ and $u \neq v$
- It is guaranteed that the edges given in the input form a tree.
- The sum of $N$ over all test cases does not exceed $3\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
1
10
15 30 15 5 3 15 3 3 5 5
1 2
1 5
2 3
2 4
5 6
5 7
5 8
7 9
7 10
```

**Output**

```text
33
```

**Explanation**

The tree from the sample is as follows.

![tree_basic](https://s3.amazonaws.com/codechef_shared/download/Images/the_hyp0cr1t3/tree_basic.png =450x450)

If vertex $v = 7$ is chosen, vertices $1$, $5$ and $7$ are removed.

![tree_remove](https://s3.amazonaws.com/codechef_shared/download/Images/the_hyp0cr1t3/tree_remove.png =450x450)

The resulting forest contains five connected components $\{8\}, \{6\}, \{10\}, \{9\}$ and $\{2, 3, 4\}$.

![tree_value](https://s3.amazonaws.com/codechef_shared/download/Images/the_hyp0cr1t3/tree_value.png =450x450)

The beauties of the connected components are $3$, $15$, $5$, $5$ and $5$ respectively. Thus the answer is $3 + 15 + 5 + 5 + 5 = 33$.

It can be shown that this is the maximum value possible for any choice of $v$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE221A/problems/FPE)

[Contest Division 2](https://www.codechef.com/JUNE221B/problems/FPE)

[Contest Division 3](https://www.codechef.com/JUNE221C/problems/FPE)

[Contest Division 4](https://www.codechef.com/JUNE221D/problems/FPE)

Setter: [Ashish Gangwar](https://www.codechef.com/users/kryptonix171)

Tester: [Lavish Gupta](https://www.codechef.com/users/lavish_adm), [Abhinav sharma](https://www.codechef.com/users/inov_360),[ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

2094

#
[](#prerequisites-3)PREREQUISITES:

[Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search), [Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming), [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor), [Trees](https://en.wikipedia.org/wiki/Tree_(data_structure))

#
[](#problem-4)PROBLEM:

There is a rooted tree of N vertices rooted at vertex 1. Each vertex v has a value A_v associated with it.

You choose a vertex v (possibly the root) from the tree and remove all vertices on the path from the root to the vertex v, also including v. This will result in a forest of zero or more connected components.

The beauty of a connected component is the \mathrm{GCD} of the values of all vertices in the component. Find the maximum value of the sum of beauties of the obtained connected components for any choice of v.

Here, \mathrm{GCD} stands for [Greatest Common Divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

#
[](#explanation-5)EXPLANATION:

Let us look at what happens when we remove the path from a node to the root of the tree (node 1 ) . Let initially the tree look like what is shown below.

And lets say we decided to remove path from node 7 to node 1 from this tree. All the nodes on the path are removed. The Remaining nodes still form a forest of zero or more connected components (trees). All the children of node removed (7 here) are disconnected from each other and form different connected components (subtrees of node 10 and 9 here). For each node on the path till root (ancestors) all children of that node other than the child which is included in the path from node u to node 1 form different connected components.

Therefore for every node u in the tree we need to find the sum of beauties of subtrees of all its children and sum of beauties of subtrees of all the children, except u, of all ancestors (all nodes other than u that lie on the path to the root) of node u. The maximum of this value over all nodes of the tree is the answer to the problem.

Removing every node and its path to the root and calculating the answer naively takes O(N^2) time which is not fast enough to pass the test cases for large values of N.

To improve the runtime of the solution, let us perform some calculations first,

Let G_u represent the gcd of all node values A_v present in the subtree of u and SumofG_u represent the sum of G_x for all children x of node u

Formally, G_u=gcd(all(A_v),\:\: v\in Subtree of  u.

SumofG_u = \sum G_x   where x is a child of node u.

Both of these parameters for all nodes N of the tree can be done in O(Nlog(max(A_v))) by a single dfs traversal of the tree starting from root node and basic dynamic programming.

Calculation of the parameters defined above for all nodes
``void dfsforgcd(int u, int p = -1)
{
  g[u] = a[u];
  sumofg[u] = 0;
  for (auto x : v[u])
  {
    if (x == p)
      continue;
    dfsforgcd(x, u);
    g[u] = gcd(g[u], g[x]);
    sumofg[u] += g[x];
  }
}
``

Sum of beauties of connected components we get after removing the path from node u to node 1 = SumofG_u+\sum (SumofG_p-g_p)- g_u where p are all the nodes on the path from root node 1 to node u (except u).

The maximum of this value over all nodes of the tree is the answer to the problem.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N\cdot log(max(A_i))) for each test case. log(max(A_i)) factor is added due to the calculations of the gcd which takes logarithmic time.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include <bits/stdc++.h>
#define int long long int
#define debug cout<<"K"
#define mod 1000000007

using namespace std;

vector<int> a(300001);
vector<int> adj[300001];
bool visited[300001];
vector<int>subtree(300001,0);
int ans=0;

void dfs(int node)
{
    visited[node]=true;
    for(int next:adj[node])
    {
        if(!visited[next])
        {
        dfs(next);
        subtree[node]=__gcd(subtree[node],subtree[next]);
        }
    }
}

void nfs(int node,int above)
{
    visited[node]=true;
    int sum=0;
    for(int next:adj[node])
    {
        if(!visited[next])
        sum+=subtree[next];
    }
    ans=max(ans,above+sum);
    for(int next:adj[node])
    {
        if(!visited[next])
        {
        nfs(next,above+sum-subtree[next]);
        }
    }
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t>0)
    {
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
        {cin>>a[i];
        subtree[i+1]=a[i];}
        for(int i=0;i<n-1;i++)
        {
            int x,y;
            cin>>x>>y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }
        dfs(1);
        for(int i=1;i<=n;i++)
        visited[i]=false;
        nfs(1,0);
        cout<<ans<<"\n";
        for(int i=1;i<=n;i++)
        {
            adj[i].clear();
            visited[i]=false;
            subtree[i]=0;
            a[i]=0;
        }
        ans=0;
        t--;
    }
    return 0;
}

``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 3e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
inline ll gcd(ll a, ll b)
{
  if (b == 0)
    return a;
  a %= b;
  return gcd(b, a);
}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
ll a[N], maxbeauty, g[N], sumofg[N];
vll v[N];
void dfsforgcd(int u, int p = -1)
{
  g[u] = a[u];
  sumofg[u] = 0;
  for (auto x : v[u])
  {
    if (x == p)
      continue;
    dfsforgcd(x, u);
    g[u] = gcd(g[u], g[x]);
    sumofg[u] += g[x];
  }
}
void dfs(int u, int p, ll beautytillparent)
{
  ll beauty = beautytillparent;
  if (p != -1)
    beauty += sumofg[p] - g[u];
  beautytillparent = beauty;
  for (auto x : v[u])
  {
    if (x == p)
      continue;
    dfs(x, u, beautytillparent);
    beauty += g[x];
  }

  maxbeauty = max(maxbeauty, beauty);
}
void sol(void)
{
  int n;
  cin >> n;
  maxbeauty = 0;
  for (int i = 1; i <= n; i++)
    cin >> a[i], v[i].clear();
  for (int i = 1; i <= n - 1; i++)
  {
    int x, y;
    cin >> x >> y;
    v[x].pb(y);
    v[y].pb(x);
  }
  dfsforgcd(1);
  dfs(1, -1, 0);
  cout << maxbeauty << '\n';
  return;
}
int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL), cout.tie(NULL);
  int test = 1;
  cin >> test;
  while (test--)
    sol();
}

``

</details>
