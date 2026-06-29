# Per Capita Income

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERCAPTA |
| Difficulty Rating | 2132 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [PERCAPTA](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/PERCAPTA) |

---

## Problem Statement

Chefland consists of $N$ provinces (numbered $1$ through $N$) connected by $M$ bidirectional roads (numbered $1$ through $M$). For each valid $i$, the $i$-th road connects provinces $U_i$ and $V_i$. It is possible to travel from each province to any other province using these roads.

For each valid $i$, the annual income of the $i$-th province is $A_i$ and its population is $B_i$. The per-capita income of some provinces is lower than that of some other provinces. For this reason, the king of Chefland wants to choose one or more provinces to keep in his kingdom and abandon the rest, in such a way that the per-capita income of the whole resulting kingdom, i.e. the sum of annual incomes of the chosen provinces divided by the sum of their populations, would be maximum possible. However, it should also be possible to travel from each of the chosen provinces to any other chosen province without visiting any of the abandoned provinces. Among all such ways to form the new kingdom, the king would prefer the number of chosen provinces to be as large as possible.

Can you help the king choose which provinces should form the new kingdom? If there are multiple solutions that maximise the per-capita income, you should choose one with the maximum number of chosen provinces. If there are still multiple solutions, you may choose any one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.
- $M$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $U_i$ and $V_i$.

### Output
Print two lines.
- The first of these lines should contain a single integer $K$ denoting the number of provinces the king should choose.
- The second line should contain $K$ space-separated integers denoting these provinces.

### Constraints
- $1 \le T \le 5$
- $1 \le N, M \le 2 \cdot 10^5$
- $1 \le U_i, V_i \le N$ for each valid $i$
- $U_i \neq V_i$ for each valid $i$
- there is at most one road between each pair of provinces
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
1
3 3
10 1 2
5 1 1 
1 2
2 3
1 3
```

**Output**

```text
2
1 3
```

**Explanation**

If the king chooses provinces $1$ and $3$, then the per-capita income is $\frac{10 + 2}{5 + 1} = 2$. This is the only optimal solution.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PERCAPTA)

[Contest: Division 1](https://www.codechef.com/COOK119A/problems/PERCAPTA)

[Contest: Division 2](https://www.codechef.com/COOK119B/problems/PERCAPTA)

**Setter:** [Rezwan Arefin](https://www.codechef.com/users/rezwanarefin01)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Easy

# PREREQUISITES:

Basic Maths, DSU, or DFS/BFS on a graph (flood fill).

# PROBLEM:

Given a graph with N nodes (represented by cities) and M bidirectional edges (represented by roads between cities). Each city has a given total annual income (given by A_i) and a population (given by B_i).

You are required to find the largest connected subgraph such that the per capita income of the chosen subgraph is maximum possible.

# QUICK EXPLANATION

- We only choose those cities into subgraph which have the largest per capita income. We discard the rest.

- After discarding, the largest connected component of the remaining cities is the largest possible connected subgraph we can get, which has maximum per capita income.

# EXPLANATION

First, let us consider two cities 1 and 2, such that the annual income of cities are A and C, and the populations of cities are B and D respectively. WLOG assume \displaystyle\frac{A}{B} < \frac{C}{D}.

Then, if we decide to keep the both cities, the resulting per capita income shall be \displaystyle\frac{A+C}{B+D}. But we know that \displaystyle\frac{A}{B} < \frac{A+C}{B+D} < \frac{C}{D} holds.

You can find the mathematical proof [here](https://www.quora.com/Why-does-a-c-b-d-lie-between-a-b-and-c-d), I’ll explain how to theoretically interpret this.

See, Say E =\displaystyle \frac{A}{B} and F = \displaystyle\frac{C}{D}, then we can see that the per capita income of subgraph with above two cities must lie between E and F.

Proof by contradiction

Let’s assume the per capita income of the graph containing both cities, is less than \displaystyle\frac{A}{B}.

This means \displaystyle\frac{A+C}{B+D} < \frac{A}{B}

We get (A+C)*B < A*(B+D), giving C*B < A*D which implies \displaystyle\frac{C}{D} < \frac{A}{B}, but this goes against our assumption, hence \displaystyle\frac{A+C}{B+D} > \frac{A}{B}

We can similarly prove \displaystyle\frac{A+C}{B+D} < \frac{C}{D}

Hence, selecting a single city u with maximum \displaystyle\frac{A_u}{B_u} gives the best per capita income, so any city v with \displaystyle\frac{A_v}{B_v} < \frac{A_u}{B_u} are never included in final subgraph. So, let’s remove all such cities from graph.

Now we are left with the problem to select the largest number of cities such that each node in the selected subset is reachable from each other. We can easily use either [DFS](https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/)  or [Disjoint Set Union](https://cp-algorithms.com/data_structures/disjoint_set_union.html) to find the largest connected component in the remaining graph.

For the DSU approach, we also need to keep track of the size of each component, or we can just find the frequency of each root (termed as the leader on the cp-algorithms page) and choose all the nodes whose root has a maximum frequency.

# TIME COMPLEXITY

For the DFS solution, the time complexity is O(N) per test case.

For the DSU solution, the time complexity is O(N*\alpha(N)) per test case where \alpha(N) is [Inverse Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function#Inverse)

# SOLUTIONS:

Setter's solution
``#include  <bits/stdc++.h>
using namespace std;

using ll = long long;
using ii = pair<long long, long long>;
const int maxn = 2e5 + 5;

int n, m, par[maxn], sz[maxn];

int find(int u) {
	return par[u] == u ? u : par[u] = find(par[u]);
}

void unite(int u, int v) {
	u = find(u), v = find(v);
	if(u == v) return;
	if(sz[u] > sz[v]) swap(u, v);
	sz[v] += sz[u];
	par[u] = v;
}

int main(int argc, char const *argv[]) {
	// freopen("in", "r", stdin);
	int t;
	scanf("%d", &t);
	while(t--) {
		scanf("%d %d", &n, &m);
		for(int i = 0; i <= n; ++i) par[i] = sz[i] = 0;

		vector<ii> R(n);
		ii opt(0, 1);
		for(int i = 0; i < n; i++) {
			scanf("%lld", &R[i].first);
		}
		for(int i = 0; i < n; i++) {
			scanf("%lld", &R[i].second);
			int g = __gcd(R[i].first, R[i].second);
			R[i].first /= g;
			R[i].second /= g;
			if(opt.first * R[i].second < R[i].first * opt.second) {
				opt = R[i];
			}
		}
		for(int i = 0; i < n; i++) {
			par[i] = i, sz[i] = 1;
		}
		for(int i = 0; i < m; i++) {
			int u, v;
			scanf("%d %d", &u, &v);
			u--, v--;
			if(R[u] == opt and R[v] == opt) {
				unite(u, v);
			}
		}

		int mx_sz = 0, arg = -1;
		for(int i = 0; i < n; i++) {
			int rep = find(i);
			if(sz[rep] >= mx_sz) {
				mx_sz = sz[rep];
				arg = rep;
			}
		}

		printf("%d\n", mx_sz);
		for(int i = 0; i < n; i++) {
			if(find(i) == arg) {
				printf("%d ", i + 1);
			}
		} putchar('\n');
	}
	return 0;
}
``

Tester's Solution (uses DFS approach)
``//raja1999

//#pragma comment(linker, "/stack:200000000")
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//setbase - cout << setbase (16)a; cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 <<endl;prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
using namespace __gnu_pbds;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >
#define int ll

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

//std::ios::sync_with_stdio(false);
int vis[200005],choose[200005],a[200005],b[210005];
vector<vi>adj(200005);
vi provinces;
vi res;
int dfs(int u){
	vis[u]=1;
	int i;
	provinces.pb(u);
	rep(i,adj[u].size()){
		if(vis[adj[u][i]]==0 && choose[adj[u][i]]==1){
			dfs(adj[u][i]);
		}
	}
}
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,m,i,u,v,ans=0,num,den,max_id;
		provinces.clear();
		res.clear();
		cin>>n>>m;
		rep(i,n){
			adj[i].clear();
			vis[i]=0;
			choose[i]=0;
			cin>>a[i];
		}
		rep(i,n){
			cin>>b[i];
		}
		rep(i,m){
			cin>>u>>v;
			u--;
			v--;
			adj[u].pb(v);
			adj[v].pb(u);
		}
		num=a[0];
		den=b[0];
		f(i,1,n){
			if(a[i]*den>num*b[i]){
				num=a[i];
				den=b[i];
			}
		}
		rep(i,n){
			if(a[i]*den==num*b[i]){
				choose[i]=1;
			}
			else{
				choose[i]=0;
			}
		}
		fd(i,n-1,0){
			if(vis[i]==0 && choose[i]==1){
				provinces.clear();
				dfs(i);
				if(provinces.size()>res.size())
					res=provinces;
			}
		}
		cout<<res.size()<<endl;
		int siz=res.size();
		// fd(i,siz-1,0){
		random_shuffle(all(res));
		rep(i,siz){
			cout<<res[i]+1<<" ";
		}
		cout<<endl;
	}
	return 0;
}
``

Editorialist's Solution (uses DSU approach)
``import java.util.*;
import java.io.*;
class PERCAPTA{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni(), M = ni();
	    long[] A = new long[N], B = new long[N];
	    for(int i = 0; i< N; i++)A[i] = nl();
	    for(int i = 0; i< N; i++)B[i] = nl();
	    long num = 0, den = 1;
	    int[] set = new int[N], sz = new int[N];
	    for(int i = 0; i< N; i++){
	        set[i] = i;sz[i] = 1;
	        if(A[i]*den > num*B[i]){
	            num = A[i];
	            den = B[i];
	        }
	    }
	    for(int i = 0; i< M; i++){
	        int u = ni()-1, v = ni()-1;
	        if(A[u]*den == B[u]*num && A[v]*den == B[v]*num){//If edge connects two maximum per capita income nodes
	            if(find(set, u) != find(set, v)){
	                sz[find(set, u)] += sz[find(set, v)];
	                set[find(set, v)] = find(set, u);
	            }
	        }
	    }
	    int root = 0;
	    for(int i = 0; i< N; i++)if(sz[find(set, i)] > sz[root])root = find(set, i);//finding largest sized component
	    pn(sz[root]);
	    for(int i = 0; i< N; i++)if(find(set, i) == root)p(1+i+" ");pn("");
	}
	//Union disjoint sets with path compression
	int find(int[] set, int u){
	    return set[u] = set[u] == u?u:find(set, set[u]);
	}
	//SOLUTION END
	void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
	static boolean multipleTC = true;
	FastReader in;PrintWriter out;
	void run() throws Exception{
	    in = new FastReader();
	    out = new PrintWriter(System.out);
	    //Solution Credits: Taranpreet Singh
	    int T = (multipleTC)?ni():1;
	    pre();for(int t = 1; t<= T; t++)solve(t);
	    out.flush();
	    out.close();
	}
	public static void main(String[] args) throws Exception{
	    new PERCAPTA().run();
	}
	int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
	void p(Object o){out.print(o);}
	void pn(Object o){out.println(o);}
	void pni(Object o){out.println(o);out.flush();}
	String n()throws Exception{return in.next();}
	String nln()throws Exception{return in.nextLine();}
	int ni()throws Exception{return Integer.parseInt(in.next());}
	long nl()throws Exception{return Long.parseLong(in.next());}
	double nd()throws Exception{return Double.parseDouble(in.next());}

	class FastReader{
	    BufferedReader br;
	    StringTokenizer st;
	    public FastReader(){
	        br = new BufferedReader(new InputStreamReader(System.in));
	    }

	    public FastReader(String s) throws Exception{
	        br = new BufferedReader(new FileReader(s));
	    }

	    String next() throws Exception{
	        while (st == null || !st.hasMoreElements()){
	            try{
	                st = new StringTokenizer(br.readLine());
	            }catch (IOException  e){
	                throw new Exception(e.toString());
	            }
	        }
	        return st.nextToken();
	    }

	    String nextLine() throws Exception{
	        String str = "";
	        try{
	            str = br.readLine();
	        }catch (IOException e){
	            throw new Exception(e.toString());
	        }
	        return str;
	    }
	}
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
