# Cosmic Temple

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COSTEMP |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [COSTEMP](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/COSTEMP) |

---

## Problem Statement

Nearly $10^{9} + 7$ trillion kilometers far away from the Milkyway, there exists a parallel Universe of Light called the Cosmos of Solon where each planet is called a Temple. There are total $N$ temples. Unlike humans, the Solomons (Giant aliens of the Light World) can travel from one temple to another through Cosmic Bridges and the distance observed by them between any two temples is $0$ units (Interesting? Well, they travel with more than the speed of light)

But the year $2020$, proved to be a curse for Solomons. This year, a Mega Star Urus struck their Universe and damaged many Cosmic Bridges. However the God of Light ensured that for any two distinct temples $u$ and $v$ there exists exactly one unique path through Cosmic Bridge(s), but the distance between two directly connected temples through a Bridge has now increased to $1$ units.

To prevail the existence of this Universe, the God of Light carved himself into exactly $N$ Solomons which now rule the $N$ temples and are independent of each other. One by one, the $i^{th}$ Solomon ($0 \leq i \leq N-1$) transmits Light pulses through the network of Cosmic Bridges and determines the sum of distances to the remaining $N-1$ Solomons.

Can you help them find these quantities so they can reunite into God of Light again?

###Input Format:

- The first line of the input contains $N$, the total no. of temples.
- Each of the next $N-1$ lines contain two space-separated integers $u$ and $v$ ($u \neq v$) denoting the bidirectional Cosmic Bridge between temples $u$ and $v$.

###Output Format:

Print $N$ space separated integers in a single line where the $i^{th}$ integer denotes the sum of distances from the $i^{th}$ ($0 \leq i \leq N-1$) Solomon to the rest of $N-1$ Solomons.

###Constraints:

- $1 \leq N \leq 10^{6}$
- $0 \leq u, v \leq N-1$

###Sample Input:

     5
     0 2
     0 3
     1 3
     3 4

###Sample Output:

     6 8 9 5 8

###Explanation:

- For temple $0$ : distance($1$) + distance($2$) + distance($3$) + distance($4$) = $2+1+1+2=6$
- For temple $1$ : distance($0$) + distance($2$) + distance($3$) + distance($4$) = $2+3+1+2=8$
- For temple $2$ : distance($0$) + distance($1$) + distance($3$) + distance($4$) = $1+3+2+3=9$
- For temple $3$ : distance($0$) + distance($1$) + distance($2$) + distance($4$) = $1+1+2+1=5$
- For temple $4$ : distance($0$) + distance($1$) + distance($2$) + distance($3$) = $2+2+3+1=8$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COSTEMP)

[Contest](https://www.codechef.com/CVXH2020/problems/COSTEMP)

*Author:*  [Nishikant Parmar](https://www.codechef.com/users/niksparmar)

*Editorialist:* [Nishikant Parmar](https://www.codechef.com/users/niksparmar)

# DIFFICULTY:

EASY-MEDIUM

# PREREQUISITES:

Depth-First Search, Dynamic Programming on Trees

# PROBLEM:

Given a tree with N vertices numbered from 0 to N-1 and N-1 edges, output an array where the i^{th} element of the array denotes the sum of distances of the vertex i to all other vertices in the tree.

Note : Here the distance between two vertices connected through an edge is 1 units.

# QUICK EXPLANATION:

Let, nodesCount[v] be no. of nodes which are in the subtree of node v (including v) and ans[v] be the sum of distances of the node v to the remaining nodes.

Then,  ans[v] = ans[u] + N - 2*nodesCount[v] (where, u is the parent of v)

# EXPLANATION:

Throughout the editorial consider u to be parent of v.

Suppose, down[v] denotes sum of distances to all nodes in the subtree of node v and let us define nodesCount[v], ans[v] same as above.

**Calculation of** nodesCount[u] :

nodesCount[u] = 1 + \sum\limits_{for\;all\;children\;v\;of\;u} nodesCount[v]

**Calculation of** down[u] :

down[u] = \sum\limits_{for\;all\;children\;v\;of\;u} (nodesCount[v] + down[v])

To get the sum of distances from u to all nodes in the subtree of v we need to add 1 unit extra distance for each node in subtree of v. Since, there are nodesCount[v] many nodes hence, we add this to down[v] to get the sum of distances from u to all nodes in subtree of v and take the sum over all children v of u.

Now, if we calculate up[v] i.e. sum of distances to all nodes from v that are **not** a part of subtree of v then,

ans[v] = down[v] + up[v]

**Calculation of** up[u] :

up[v] = ans[u] - (nodesCount[v] + down[v]) + (N - nodesCount[v])

Here, we assume that we already know ans[u].

When we subtract (nodesCount[v] + down[v]) from ans[u] we get sum of distances to all nodes from u to the nodes which are **not** in the subtree of v. Now, to make it the sum of distances from v we add the number of nodes which are not in subtree of v (This is similar to calculating down[u] from down[v] by adding nodesCount[v])

**Calculation of** ans[u]:

ans[v] = down[v] + up[v]

\implies ans[v] = down[v] + ans[u] - (nodesCount[v] + down[v]) + (N - nodesCount[v])

\implies ans[v] = ans[u] - N - 2*nodesCount[v]

We had assumed that we already know ans[u] while calculating up[v]. We can incrementally calculate ans[u] and use it for up[v] calculation using another Depth-First Search. Here, the base case is ans[root] = down[root], since for root all nodes lie in its subtree and up[root] = 0.

# SOLUTIONS:

Setter's Solution
``
#include <bits/stdc++.h>
using namespace std;

void DFS(int u, vector<vector<int>> &GRAPH, vector<bool> &visited, vector<int> &down, vector<int> &nodesCount){

    visited[u] = true;
    nodesCount[u]++;

    for(int v:GRAPH[u]){
        if(!visited[v]){
            DFS(v, GRAPH, visited, down,nodesCount);
            nodesCount[u]+=nodesCount[v];
            down[u]+=nodesCount[v]+down[v];
        }
    }
}

void DFS2(int u, vector<vector<int>> &GRAPH, vector<bool> &visited,vector<int> &nodesCount, vector<int> &ans){

    visited[u] = true;
    int N = visited.size();

    for(int v:GRAPH[u]){
        if(!visited[v]){
            ans[v] = ans[u] + N - 2*nodesCount[v];
            DFS2(v,GRAPH,visited,nodesCount,ans);
        }
    }
}

int main(){

    int N;
    cin>>N;
    vector<vector<int>> GRAPH(N);

    for(int i=0;i<N-1;i++){
        int u, v;
        cin>>u;cin>>v;
        GRAPH[u].push_back(v);
        GRAPH[v].push_back(u);
    }

    // DFS 1
    vector<int> down(N, 0);
    vector<bool> visited(N, false);
    vector<int> nodesCount(N, 0);
    DFS(0, GRAPH, visited, down,nodesCount);

    // DFS 2
    vector<int> ans(N, 0);
    for(int i=0;i<N;i++) visited[i] = false;
    ans[0] = down[0];

    DFS2(0,GRAPH,visited,nodesCount,ans);
    for(int x:ans) cout << x << " ";

    return 0;

}

``

Editorialist's Solution
``
import sys
sys.setrecursionlimit(10**6)

N = int(input())
GRAPH = [[] for i in range(N)]

for i in range(N-1):
    u, v = map(int, input().split())
    GRAPH[u].append(v)
    GRAPH[v].append(u)

visited = [False for i in range(N)]
down = [0 for i in range(N)]
nodesCount = [0 for i in range(N)]

def DFS(u):
    visited[u] = True
    nodesCount[u]+=1

    for v in GRAPH[u]:
        if not visited[v]:
            DFS(v)
            nodesCount[u]+=nodesCount[v]
            down[u]+=nodesCount[v]+down[v]

def DFS2(u):
    visited[u] = True
    for v in GRAPH[u]:
        if not visited[v]:
            ans[v] = ans[u] + N - 2*nodesCount[v]
            DFS2(v)

DFS(0)

visited = [False for i in range(N)]
ans = [0 for i in range(N)]
ans[0] = down[0]
DFS2(0)

for x in ans:
    print(x, end="")
    print(" ", end="")
``

</details>
