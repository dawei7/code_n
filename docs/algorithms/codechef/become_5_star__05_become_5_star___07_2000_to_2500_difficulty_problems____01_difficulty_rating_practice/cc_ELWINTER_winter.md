# Winter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ELWINTER |
| Difficulty Rating | 2007 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ELWINTER](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ELWINTER) |

---

## Problem Statement

Uneori îmi spun: am să mor
atât de singuratecă-n mijlocul lor;
limba simplă a bucuriilor n-am învâțat;
am să mor ca o pasăre care prea mult a zburat,
dar n-a făcut cuib nicăieri.

― Oamenii ma uimesc, Magda Isafost
__________________________________________________________

As of writing the informal statement, the winter just came and the statement was in season. Now, it is not winter anymore, so here is the formal statement instead:

You are given a connected graph with $N$ nodes and $M$ edges. You are given $Q$ queries of the following types:
- $\texttt{1 u}$: Given node $u$ $(1 \leq u \leq N)$, set the state of the node $u$ to frozen.
- $\texttt{2 t}$: Given $t$, let $t$ units of time pass by.
- $\texttt{3 v}$: Given node $v$ $(1 \leq v \leq N)$, answer if node $v$ is currently frozen.

Initially, **no** node is frozen.
The graph has the following property:
- If, at time $T$, a node $u$ is frozen, then, at time $(T+1)$, **all neighbours** of $u$ become frozen.

For each query of type $3$, answer whether the node is currently frozen.

**Note:**
- If a node is already frozen, it remains unaffected after a type $1$ query.
- If, for a frozen node $u$, a neighbour $v$ of node $u$ is frozen at time $T$, node $v$ remains unaffected at time $(T+1)$.

---

## Input Format

- The first line of input contains three integers $N, M,$ and $Q$.
- $M$ lines follow, the $i^{th}$ of which contains two integers $u_i$ and $v_i$, representing there is an edge between nodes $u_i$ and $v_i$.
- Then, $Q$ lines follow, the $j^{th}$ of which contains two integers $type_j$ and $x_j$.
If $type_j$ is $1$ or $2$, it indicates that you must effectuate an update of the type $type_j$ with parameter $x_j$. Otherwise, answer the query with parameter $x_j$

---

## Output Format

For each query of type $3$, print $\texttt{YES}$ if the queried node is frozen. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \le N, Q \le 10^5$
- $1 \le M \le 3 \cdot 10^5$
- $1 \le u_i, v_i \le N$
- $1 \le type_j \le 3$
- $1 \le x_j \le N$, if the query type is $1$ or $3$.
- $1 \le x_j \le 10^9$, if the query type is $2$.

---

## Examples

**Example 1**

**Input**

```text
6 6 6
1 2
2 3
4 1
5 4
6 1
6 5
1 1
3 1
1 5
2 1
3 4
3 3
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test Case $1$:** The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine4.png)
- Query $1$: Freeze the node $1$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine2.png)
- Query $2$: Find the status of node $1$. Since node $1$ is frozen, we print $\texttt{YES}$.
- Query $3$: Freeze the node $5$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine5.png)
- Query $4$: $1$ unit of time passes. Before this, nodes $1$ and $5$ were frozen.
After $1$ second, all the neighbours of node $1$, i.e., nodes $2, 4,$ and $6$, and all the neighbours of node $5$, i.e., nodes $4$ and $6$ are frozen.
Thus, after this query, the frozen nodes in the graph are $1, 2, 4, 5,$ and $6$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine3.png)
- Query $5$: Find the status of node $4$. Since node $4$ is frozen, we print $\texttt{YES}$.
- Query $6$: Find the status of node $3$. Since node $3$ is not frozen, we print $\texttt{NO}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME106A/problems/ELWINTER)

[Contest Division 2](https://www.codechef.com/LTIME106B/problems/ELWINTER)

[Contest Division 3](https://www.codechef.com/LTIME106C/problems/ELWINTER)

[Contest Division 4](https://www.codechef.com/LTIME106D/problems/ELWINTER)

**Setter:** [ Voicu Mihai](https://www.codechef.com/users/kinto)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

BFS, Graphs

#
[](#problem-4)PROBLEM:

You are given a connected graph with N nodes and M edges. You are given Q queries of the following types:

-
???? u: Given node u(1\le u \le N), set the state of the node u to frozen.

-
???? ????: Given t, let t units of time pass by

-
???? ????: Given node v (1 \le v \le N), answer if node v is currently frozen.

Initially, **no** node is frozen.

The graph has the following property:

- If, at time T, a node u is frozen, then, at time (T+1), **all neighbours** of u become frozen.

For each query of type 3, answer whether the node is currently frozen.

#
[](#explanation-5)EXPLANATION:

Let us first see that the graph is connected, hence if you look at the 2^{nd} type of the query then you can realize that the if the any node is frozen at time x then the whole graph will get frozen at x+N-1 seconds at maximum because of the only single reason that the graph is connected.

Hence you need not to be afraid of such large constraints for the second query. Now as the problem says you need to do that and it’s a simple BFS.

While writing the editorial I remembered the analogy used by CP algorithms to explain BFS when I was new to BFS. I will paste that analogy and you will find it interesting as it’s what our question says:

“The algorithm can be understood as a fire spreading on the graph: at the zeroth step only the source s is on fire. At each step, the fire burning at each vertex spreads to all of its neighbors. In one iteration of the algorithm, the “ring of fire” is expanded in width by one unit (hence the name of the algorithm).”

They used this analogy to explain BFS and here are we our question is this analogy isn’t that. Hence we will be using BFS for the same. Now let’s see how we will be dealing with the queries.

-

1^{st} type of Query.

For this type of query you will be given a node which we want you to froze that. If the node is already frozen sorry for the query, you can forgave us. But if its not frozen just froze that and add to the queue.

-

2^{nd} type of Query.

For this type of query, as we told you need to perform the bfs till the current time to the given time. But remember you after a certain interval of time every node will get frozen and you can stop performing bfs after that and can simply ignore these type of queries from then.

-

3^{rd} type of Query.

For this type of query please check if the node is frozen and let us know. Thanks for your help.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(Q + N + M)

#
[](#solutions-7)SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

const int nmax = 3e5 + 5;

vector<int> g[nmax];

int frozen[nmax];
queue<pair<int,int> > que; // I used this to ensure that timelimits won't be against the use of the std::queue, although I know it is preffered to hand-write the queue

int currenttime;

static void timepass() {
  while(!que.empty()) {
    int t, x;
    tie(t, x) = que.front();
    if(t > currenttime)
      break;
    que.pop();
    for(auto y : g[x]) {
      if(frozen[y])
        continue;
      que.push({t + 1, y});
      frozen[y] = 1;
    }
  }
  currenttime++;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, m, q;
  cin >> n >> m >> q;
  for(int i = 0,x, y; i < m; i++) {
    cin >> x >> y;
    --x;
    --y;
    g[x].push_back(y);
    g[y].push_back(x);
  }
  for(int i = 0; i < q; i++) {
    int t, x;
    cin >> t >> x;
    if(t == 1) {
      --x;
      if(frozen[x] == 0)
        frozen[x] = 1, que.push({currenttime, x});
    }
    if(t == 2) {
      x = min(n + 1, x + currenttime);
      while(currenttime < x)
        timepass();
    }
    if(t == 3) {
      --x;
      cout << (frozen[x]? "YES\n" : "NO\n");
    }
  }
  return 0;
}

``

Tester
``#include <bits/stdc++.h>
using namespace std;
void sim(priority_queue<pair<int, int>> &pq, int vis[], int t, vector<int> gr[]){
  while(pq.size()){
    int x = -pq.top().first;
    int y = pq.top().second;
    if(x > t){
      break;
    }
    pq.pop();
    if(vis[y] != -1){
      continue;
    }
    vis[y] = x;
    for(int i = 0; i < gr[y].size(); i++){
      pq.push({-x - 1, gr[y][i]});
    }
  }
}
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  int n, m, q;
  cin>>n>>m>>q;
  vector<int> gr[n + 1];
  for(int i = 0; i < m; i++){
    int u, v;
    cin>>u>>v;
    gr[u].push_back(v);
    gr[v].push_back(u);
  }
  int vis[n + 1];
  memset(vis, -1, sizeof(vis));
  priority_queue<pair<int, int>> pq;
  int t = 0;
  bool f = false;
  while(q--){
    int x, y;
    cin>>x>>y;
    if(x == 1){
      pq.push({-t, y});
    }
    if(x == 2){
      t += y;
    }
    if(x == 3){
      sim(pq, vis, t, gr);
      if(vis[y] == -1){
        cout<<"NO\n";
      }else{
        cout<<"YES\n";
      }
    }
  }
  return 0;
}
``

</details>
