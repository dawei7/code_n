# Path-etic Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PATHSUMS |
| Difficulty Rating | 1838 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [PATHSUMS](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/PATHSUMS) |

---

## Problem Statement

You are given a tree with $N$ nodes (numbered $1$ through $N$). A tree is a connected undirected graph without cycles.

You have to assign an integer to each node; for each valid $i$, let's denote the integer assigned to node $i$ by $A_i$. This assignment must satisfy the following conditions:
- For each valid $i$, $1 \le A_i \le 10^5$.
- For each simple path in the tree which contains at least two nodes, let's denote the set of nodes in this path by $S$. Then, $\sum_{v \in S} A_v$ is not divisible by $|S|$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Each of the next $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

### Output
For each test case, print a single line containing $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

If there are multiple solutions, you may find any one of them. It can be proved that a solution always exists under the given constraints.

### Constraints
- $1 \le T \le 200$
- $2 \le N \le 100$
- $1 \le u, v \le N$

---

## Examples

**Example 1**

**Input**

```text
2
7
1 2
4 6
3 5
1 4
7 5
5 1
3
1 2
2 3
```

**Output**

```text
4 9 12 1 9 8 4
4 3 6
```

**Explanation**

**Example case 1:**

This assignment satisfies all the conditions. For example, for the path $3 \rightarrow 5 \rightarrow 1 \rightarrow 2$, the sum $12 + 9  + 4 + 9 = 34$ is not divisible by $4$ (the number of nodes in the path).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
1 2
4 6
3 5
1 4
```

**Output for this case**

```text
4 9 12 1 9 8 4
```



#### Test case 2

**Input for this case**

```text
7 5
5 1
3
1 2
2 3
```

**Output for this case**

```text
4 3 6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PATHSUMS)

[Contest](https://www.codechef.com/COOK123A/problems/PATHSUMS)

**Setter:** [Shahjalal Shohag](https://www.codechef.com/users/sjshohag)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Easy

# PREREQUISITES:

Ad-hoc and DFS/BFS

# PROBLEM:

You are given a tree with N nodes. You have to assign each node i an integer A_i such that :

-
1 \leq A_i \leq 10^{5}.

- For each simple path containing 2 or more nodes, let’s denote the set of nodes in this path by S. Then \sum_{v \epsilon S} A_{v} is not divisible by|S|

# EXPLANATION:

So we have to make the sum of the values of the nodes on the simple path non-divisible by the number of nodes on the path.

For simplicity let us consider a simple path and represent the sum of the values of the nodes as Sum and the number of nodes as Len. So we can represent Sum = p*Len + r, where p and r are integers and r < Len, so we have to assign values to the nodes such that for any simple path r is non-zero. One way to do this is to root the tree at any node and assign value x to all nodes at even depth and value x+1 to all nodes at odd depth, where x lies in the range [1, 10^5)). Now let us see what will happen when we do the above assignment. If we choose a path with the number of nodes = Len, some nodes will contribute x and some nodes will contribute x+1  so the Sum = Len*x + y, where y is the number of nodes which have value x+1 and note that for any path with the number of nodes greater than or equal to 2, y will always be less than the number of nodes in the path (Floor( \frac{Len}{2} ) or Ceil( \frac{Len}{2} ) to be exact as values of the nodes in the path will take value x and x+1 in alternation) , which will make the Sum non-divisible by the Len leaving the remainder y.

One example will be to root the tree at node 1 and we can assign value 1 to all nodes at even depth and value 2 to all nodes at odd depth.

# TIME COMPLEXITY:

- Time complexity per test case is O(N).

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

const int N = 105;

vector<int> g[N];
int d[N];
void dfs(int u, int p = 0) {
  d[u] = d[p] ^ 1;
  for (auto v: g[u]) {
    if (v != p) {
      dfs(v, u);
    }
  }
}
mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  assert(1 <= t && t <= 200);
  while (t--) {
    int n; cin >> n;
    assert(2 <= n && n <= 100);
    for (int i = 1; i < n; i++) {
      int u, v; cin >> u >> v;
      g[u].push_back(v);
      g[v].push_back(u);
    }
    memset(d, 0, sizeof d);
    dfs(1);
    for (int i = 1; i <= n; i++) {
      cout << d[i] + 1 << ' ';
    }
    cout << '\n';
    for (int i = 1; i <= n; i++) {
      g[i].clear();
    }
  }
  return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
#ifndef rd
#define trace(...)
#define endl '\n'
#endif
#define pb push_back
#define fi first
#define se second
#define int long long
typedef long long ll;
typedef long double f80;
#define double long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int infi=0x3f3f3f3f;
const int mod=998244353;
//const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
	uniform_int_distribution<int> uid(0,lim-1);
	return uid(rang);
}
int powm(int a, int b) {
	int res=1;
	while(b) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

long long readInt(long long l,long long r,char endd){
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true){
		char g=getchar();
		if(g=='-'){
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g && g<='9'){
			x*=10;
			x+=g-'0';
			if(cnt==0){
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd){
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l,int r,char endd){
	string ret="";
	int cnt=0;
	while(true){
		char g=getchar();
		assert(g!=-1);
		if(g==endd){
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt && cnt<=r);
	return ret;
}
long long readIntSp(long long l,long long r){
	return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
	return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
	return readString(l,r,'\n');
}
string readStringSp(int l,int r){
	return readString(l,r,' ');
}

vi gra[105];
int total=0;
int ans[105];
void dfs(int fr, int at) {
	total++;
	ans[at]=ans[fr]^3;
	for(int i:gra[at])
		if(i!=fr)
			dfs(at,i);
}
void solve() {
	total=0;
	int n=readIntLn(1,100);
	fr(i,1,n)
		gra[i].clear();
	rep(i,1,n) {
		int u=readIntSp(1,n);
		int v=readIntLn(1,n);
		assert(u!=v);
		gra[u].pb(v);
		gra[v].pb(u);
	}
	ans[1]=1;
	dfs(1,1);
	assert(total==n);
	fr(i,1,n)
		cout<<ans[i]<<" ";
	cout<<endl;
}
signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(8);
	int t=1;
//	cin>>t;
	t=readIntLn(1,200);
	fr(i,1,t) {
		solve();
	}
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
	return 0;
}

``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<int> value;

void dfs(int node, int parent, int d) {
	if(d % 2) value[node] = 2;
	else value[node] = 1;
	for(auto i : graph[node]) {
		if(i == parent) continue;
		dfs(i, node, d+1);
	}
}

void Solve() {
	int N;
	cin >> N;
	graph.clear();
	graph.resize(N+1);
	value.assign(N+1, 0);
	for(int i = 1; i < N; i ++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	dfs(1, -1, 1);
	for(int i = 1; i <= N; i ++) {
		cout << value[i] << " ";
	}
	cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int test_case = 1;
	cin >> test_case;
	for(int i = 1; i <= test_case; i ++) {
		Solve();
	}

	return 0;
}
``

# VIDEO EDITORIAL:

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
