# Travelling in the Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRAVELLING |
| Difficulty Rating | 2108 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TRAVELLING](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TRAVELLING) |

---

## Problem Statement

You are given a graph with $N$ vertices (numbered $1$ to $N$) and $M$ bidirectional edges, which doesn't contain multiple edges or self-loops — that is, the given graph is a simple undirected graph.

For each pair of vertices $a, b$ such that $1 \leq a, b \leq N$, it is possible to add a new edge between vertices $a$ and $b$ to the graph, with a cost of $(a - b)^2$.

Find the minimum cost of adding edges so that vertex $N$ is reachable from vertex $1$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $2$ space-separated integers, $N$ and $M$.
- The $i^{th}$ of the next $M$ lines contains $2$ space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between vertex $u_i$ and vertex $v_i$ in the graph.

---

## Output Format

For each test case, output the answer in a single line.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \leq M \leq 2 \cdot 10^5$
- $1 \leq u_i, v_i \leq N$
- The graph doesn't contain self-loops or multiple edges
- Sum of $N$ over all testcases is no more than $2 \cdot 10^5$.
- Sum of $M$ over all testcases is no more than $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2 0
5 4
3 2
1 4
5 3
4 2
6 3
1 2
3 2
1 3
```

**Output**

```text
1
0
3
```

**Explanation**

**Test Case $1$:** Add an edge between vertices $1$ and $2$, with cost $(1-2)^2 = 1$.

**Test Case $2$:** Vertices $1$ and $5$ are already connected, so no edges need to be added.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28A/problems/TRAVELLING)

[Contest Division 2](https://www.codechef.com/START28B/problems/TRAVELLING)

[Contest Division 3](https://www.codechef.com/START28C/problems/TRAVELLING)

[Contest Division 4](https://www.codechef.com/START28D/problems/TRAVELLING)

Setter: [ Vishesh Saraswat](https://www.codechef.com/users/vishesh_s)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

You should be familiar with the concept of shortest paths in a weighted graph. Specifically, this problem requires [Dijkstra’s Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

#
[](#problem-4)PROBLEM:

You are given a graph with N vertices (numbered 1 to N) and M bidirectional edges, which doesn’t contain multiple edges or self-loops — that is, the given graph is a simple undirected graph.

For each pair of vertices a, b such that 1 \leq a, b \leq N, it is possible to add a new edge between vertices a and b to the graph, with a cost of (a - b)^2.

Find the minimum cost of adding edges so that vertex N is reachable from vertex 1.

#
[](#quick-explanation-5)QUICK EXPLANATION:

-

Let us assume that in the optimal solution, we have added an edge (u, v). Let u < v and v - u \geq 2. We can show that instead of adding this edge, we could have added (u , u+1), (u+1, u+2) \ldots (v-1, v). This would have costed v - u.

-

Consider the edge (i, i+1). If it is already present in the graph, then it’s cost is 0, otherwise it’s cost is 1. Cost of all other edges which are already present in the graph is 0.

-

In the above graph, we want to find out the length of shortest path from 1 to N.

#
[](#explanation-6)EXPLANATION:

First of all, let us analyze our cost function. One of the most important observation to solve this problem is to observe that if we want to add an edge (u, v), such that u < v and v - u \geq 2. We can instead add the edges (u , u+1), (u+1, u+2) \ldots (v-1, v). This would result in a lower cost. Also, the cost of adding any one of this edge would be 1.

Now, our problem reduces to finding out the minimum number of edges of the form (i, i+1), that we need to add in our graph, so that we can reach from 1 to N.

Let us add the edges (i, i+1) in the above graph if they were not already present. Also, let us assign the weight 0 to all the edges that were already present in the graph, and 1 to the edges that we have just added. We can see that our problem is exactly same as finding the length of shortest path in the newly formed graph.

To find the shortest path, we can use [Dijkstra’s Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) or [0-1 BFS](https://cp-algorithms.com/graph/01_bfs.html).

#
[](#time-complexity-7)TIME COMPLEXITY:

O(M \cdot \log{N}) or O(N+M), depending on the implementation.

#
[](#solution-8)SOLUTION:

Setter's Solution
``#include "bits/stdc++.h"
using namespace std;
/*
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using ordered_set = tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>;
*/

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define sz(x) (int)(x).size()

using ll = long long;
const int mod = 1e9+7;
const int inf = (1<<30);

void solve(int tc) {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n);
    vector<bool> hasedge(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        if (u > v)
            swap(u, v);
        adj[u].push_back({v, 0});
        adj[v].push_back({u, 0});
        if (u + 1 == v)
            hasedge[u] = true;
    }
    for (int i = 0; i < n-1; ++i) {
        if (!hasedge[i]) {
            adj[i].push_back({i+1, 1});
            adj[i+1].push_back({i, 1});
        }
    }
    vector<int> dist(n, inf);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    dist[0] = 0;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (dist[u] < d)
            continue;
        for (auto [v, w]: adj[u]) {
            if (dist[v] > d + w) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
        }
    }
    cout << dist[n-1] << '\n';
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);
    int tc = 1;
    cin >> tc;
    for (int i = 1; i <= tc; ++i) solve(i);
    return 0;
}

``

Tester-1's solution
``#include <bits/stdc++.h>
using namespace std;
long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
        char g = getchar();
        if (g == '-') {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9') {
            x *= 10;
            x += g - '0';
            if (cnt == 0) {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd) {
            assert(cnt > 0);
            if (is_neg) {
                x = -x;
            }
            assert(l <= x && x <= r);
            return x;
        }
        else {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd) {
    string ret = "";
    int cnt = 0;
    while (true) {
        char g = getchar();
        assert(g != -1);
        if (g == endd) {
            break;
        }
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  int t;
  t=readInt(1,1000,'\n');
  int ns=0;
  while(t--){
    int n, m;
    n=readInt(2,200000,' ');
    m=readInt(0,200000,'\n');
    ns+=n;
    assert(ns<=200000);
    int a[n] = {};
    set<pair<int,int>> st;
    vector<pair<int, int>> gr[n + 1];
    for(int i = 0; i < m; i++){
      int u, v;
      u=readInt(1,n,' ');
      v=readInt(1,n,'\n');
      assert(u!=v);
      st.insert({min(u,v),max(u,v)});
      if(abs(u - v) == 1){
        a[min(u, v)] = 1;
      }
      gr[u].push_back({v, 0});
      gr[v].push_back({u, 0});
    }
    assert(st.size()==m);
    for(int i = 1; i < n; i++){
      if(a[i] == 0){
        gr[i].push_back({i + 1, 1});
        gr[i + 1].push_back({i, 1});
      }
    }
    set<pair<int, int>> s;
    int vis[n + 1] = {};
    int ans;
    s.insert({0, 1});
    while(s.size()){
      auto it = s.begin();
      int y = (*it).first;
      int x = (*it).second;
      if(x == n){
        ans = y;
        break;
      }
      s.erase(it);
      if(vis[x] == 0){
        vis[x] = 1;
        for(int i = 0; i < gr[x].size(); i++){
          s.insert({y + gr[x][i].second, gr[x][i].first});
        }
      }
    }
    cout<<ans<<"\n";
  }
  return 0;
}
``

Tester-2's solution
``#include <bits/stdc++.h>
using namespace std;

/*
------------------------Input Checker----------------------------------
*/

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

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

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

/*
------------------------Main code starts here----------------------------------
*/

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int sum_n = 0, sum_m = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

vector<vector<pair<int,int> > > adj;
vector<int> vis;

void solve()
{
    int n = readIntSp(2,2e5);
    int m = readIntLn(0,2e5);

    sum_n+=n, sum_m+=m;
    max_n = max(max_n, n);
    max_m = max(max_m, m);

    adj.assign(n, vector<pair<int,int> >());
    vis.assign(n, -1);

    int x,y;

    rep(i,m){
        x = readIntSp(1,n);
        y = readIntLn(1,n);

        --x, --y;

        adj[x].push_back(mp(y,0));
        adj[y].push_back(mp(x,0));
    }

    rep(i,n-1){
        adj[i].push_back(mp(i+1,1));
        adj[i+1].push_back(mp(i,1));
    }

    vector<int> dis(n,n);
    dis[0]=0;

    set<pair<int,int> > pq;
    pq.insert({0,0});

    while(!pq.empty()){
        auto z = *(pq.begin());

        for(auto h:adj[z.ss]){
            if(dis[h.ff]>z.ff+h.ss){
                dis[h.ff] = z.ff+h.ss;
                pq.insert(mp(dis[h.ff], h.ff));
            }
        }

        pq.erase(z);
    }

    cout<<dis[n-1]<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_n<=2e5 && sum_m<=2e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<" "<<sum_m<<'\n';
    cerr<<"Maximum length : " << max_n <<" "<<max_m<<'\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}

``

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
#define pll pair<ll ,ll>
using namespace std ;
const ll z = 998244353 ;

void shortest_path(vector<pll> adj[] , int n , vector<ll> &vis , vector<ll> &dist)
{
    set<pll> s ;
    s.insert({0 , 0}) ;

    while(!s.empty())
    {
        pll g = (*s.begin()) ;
        s.erase(s.begin()) ;

        ll u = g.second , curr_dist = g.first ;
        //cout << "u = " << u << " curr_dist = " << curr_dist << endl ;
        if(vis[u] == 1)
        {
            continue ;
        }

        vis[u] = 1 ;
        dist[u] = curr_dist ;

        for(int i = 0 ; i < adj[u].size() ; i++)
        {
            ll v = adj[u][i].first ;
            ll w = adj[u][i].second ;
            //cout << "v = " << v << " w = " << w << endl ;

            if(vis[v] == 0)
                s.insert({curr_dist + w , v}) ;
        }
    }

    return ;
}

void solve()
{
    int n , m ;
    cin >> n >> m ;
    vector<pll> adj[n] ;
    for(int i = 0 ; i < m ; i++)
    {
        int u , v ;
        cin >> u >> v ;
        u-- ; v-- ;
        adj[u].push_back({v , 0}) ;
        adj[v].push_back({u , 0}) ;
    }

    for(int i = 0 ; i < n-1 ; i++)
    {
        adj[i].push_back({i+1, 1}) ;
        adj[i+1].push_back({i , 1}) ;
    }

    vector<ll> vis(n) , dist(n) ;
    shortest_path(adj , n , vis , dist) ;
    cout << dist[n-1] << endl ;
    return ;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    ll t;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    return 0;
}
``

</details>
