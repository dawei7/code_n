# Tree Coloring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREECLR |
| Difficulty Rating | 1898 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [TREECLR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/TREECLR) |

---

## Problem Statement

Given a [tree](https://en.wikipedia.org/wiki/Tree_(data_structure)) containing $N$ nodes.

Each node can be coloured using exactly one of the $C$ colours. Find the number of colourings of the tree such that:
- All nodes in a path of length at most **two** have **distinct** colours.

As the answer can be huge, print it modulo $(10 ^ 9 + 7)$.

Note:
- Two colourings of a tree are different if there exists at least one node having different colours in both the colourings.
- A path in a tree is a sequence of (zero or more) connected nodes.
- The path length between two nodes is defined as the total number of edges in the shortest path from one node to other.

---

## Input Format

- The first line of the input will contain two integers $N$ and $C$, the number of nodes in the tree and the number of colours available respectively.
- The next $(N - 1)$ lines will describe the given tree. Each line contains two integers $U$ and $V$ meaning that there is an edge between node $U$ and node $V$.

---

## Output Format

- Output the number of ways to colour the tree satisfying the given condition, modulo $10^9 + 7$.

---

## Constraints

- $ 1 \leq N \leq 10^6$
- $ 1 \leq C \leq 10^6$
- $ 1 \leq U, V \leq N$

---

## Examples

**Example 1**

**Input**

```text
3 3
1 2
1 3
```

**Output**

```text
6
```

**Explanation**

The valid colourings of nodes $1, 2,$ and $3$ are: $\{1, 2, 3\}, \{1, 3, 2\}, \{2, 1, 3\}, \{2, 3, 1\}, \{3, 1, 2\},$ and $\{3, 2, 1\}$.

Paths having length at most $2$ are: $1 - 2, 1 - 3,$ and $2 - 1 - 3$. Note that for any valid colouring, all the nodes in each of these paths have distinct colours.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TREECLR)

[Contest: Division 1](https://www.codechef.com/LTIME111A/problems/TREECLR)

[Contest: Division 2](https://www.codechef.com/LTIME111B/problems/TREECLR)

[Contest: Division 3](https://www.codechef.com/LTIME111C/problems/TREECLR)

[Contest: Division 4](https://www.codechef.com/LTIME111D/problems/TREECLR)

***Author:*** [Sachin Deb](https://www.codechef.com/users/viratkohlifan)

***Testers:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1898

#
[](#prerequisites-3)PREREQUISITES:

Depth-first search

#
[](#problem-4)PROBLEM:

You are given a tree T and an integer C. Count the number of ways to color the vertices of T with colors 1, 2, \ldots, C such that no two vertices with a distance of \leq 2 have the same color.

#
[](#explanation-5)EXPLANATION:

First, root the tree at some node, say 1. Let us try to color the tree in top-down fashion, i.e, from the root down to the leaves.

Look at some vertex u. What restriction do we have on its possible choice of colors, in relation to vertices that have been colored already?

Answer

Let p be the parent of u, and let g be the parent of p. For now, assume p and g both exist.

p and g have been colored already, and so u cannot have the same color as either p or g. p and g must also have distinct colors, so we are left with C-2 choices.

Further, u also cannot have the same color as some other vertex v that is a child of p and has already been colored. Note that each such vertex will also have a distinct color.

So, suppose s children of p have been colored already. Then, there are C-s-2 choices for the color of u.

Note that when either p or g (or both) don’t exist, the number of choices becomes C-s-1 or C-s respectively: make sure to not forget those cases.

Once we know the number of choices for each vertex u, the final answer is simply their product.

Implementing this is relatively simple, and can be done with a single DFS. Checking whether p and g exist is straightforward, and computing s is also trivial since we know how many children of p we have processed already.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;

#define ALL(a) a.begin(), a.end()
#define FastIO ios::sync_with_stdio(false); cin.tie(0);cout.tie(0)
#define IN freopen("input.txt","r+",stdin)
#define OUT freopen("output.txt","w+",stdout)

#define DBG(a) cerr<< "line "<<__LINE__ <<" : "<< #a <<" --> "<<(a)<<endl
#define NL cerr<<endl

template < class T1,class T2>
ostream &operator <<(ostream &os,const pair < T1,T2 > &p)
{
    os<<"{"<<p.first<<","<<p.second<<"}";
    return os;
}

long long bigmod ( long long a, long long p, long long m )
{
    long long res = 1;
    long long x = a;

    while ( p )
    {
        if ( p & 1 ) //p is odd
        {
            res = ( res * x ) % m;
        }
        x = ( x * x ) % m;
        p = p >> 1;
    }

    return res;
}

const int N=1e6+1;
const ll oo=1e9+7;

vector<int> g[N];

ll fact[N];
ll inv_fact[N];

void init()
{
    fact[0]=1;
    for(ll i=1;i<N;i++)
        fact[i]=(fact[i-1]*i)%oo;
    inv_fact[N-1] = bigmod(fact[N-1],oo-2,oo);
    for(ll i=N-2;i>=0;i--)
        inv_fact[i]=(inv_fact[i+1]*(i+1))%oo;
}

ll ncr(int n,int r)
{
    if(r>n) return 0;
    return fact[n]*inv_fact[r]%oo*inv_fact[n-r]%oo;
}

int n,c;
ll dfs(int u,int p)
{
    int x = 0;
    ll ret=1;
    for(int v: g[u])
    {
        if(v==p) continue;
        x++;
        ret=(ret*dfs(v,u))%oo;
    }
    ret = (ret*ncr(c-2,x))%oo * fact[x] % oo;
    return ret;
}

int32_t main()
{
    FastIO;
    cin>>n>>c;
    for(int i=1;i<n;i++)
    {
        int u,v;
        cin>>u>>v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    init();
    ll ans = c;
    for(int v: g[1])
    {
        ans = ans * dfs(v,1)%oo;
    }
    ans = ans * ncr(c-1,g[1].size()) % oo * fact[g[1].size()] % oo;
    cout<<ans<<"\n";
}
``

Tester's code (C++)
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=1e9+7;
const int N=2e6+1;
ll n,k;
vector<int>adj[N];
ll ans=1;
void dfs(int id,int p,int hp){
	ans=ans*(k-hp)%mod;
	int shp=1+(p!=0);
	for(auto c:adj[id]){
		if(c==p) continue;
		dfs(c,id,shp);
		shp++;
	}
}
void solve(){
	cin >> n >> k;
	for(int i=1; i<n ;i++){
		int u,v;cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	dfs(1,0,0);
	cout << ans << '\n';
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	solve();
}
``

Editorialist's code (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int n, c; cin >> n >> c;
	vector<vector<int>> adj(n);
	for (int i = 0; i < n-1; ++i) {
		int u, v; cin >> u >> v;
		adj[--u].push_back(--v);
		adj[v].push_back(u);
	}

	const int mod = 1e9 + 7;
	int ans = c;

	auto dfs = [&] (const auto &self, int u, int p) -> void {
		int poss = c-2 + (u == 0);
		for (int v : adj[u]) {
			if (v == p) continue;
			ans = (1LL * ans * poss)%mod;
			--poss;
			self(self, v, u);
		}
	};
	dfs(dfs, 0, 0);
	cout << ans << '\n';
}
``

</details>
