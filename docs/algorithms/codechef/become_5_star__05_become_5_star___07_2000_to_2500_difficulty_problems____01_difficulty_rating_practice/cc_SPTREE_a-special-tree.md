# A Special Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPTREE |
| Difficulty Rating | 2350 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SPTREE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SPTREE) |

---

## Problem Statement

You are given a tree with $N$ nodes (numbered $1$ through $N$). There are $K$ special nodes $f_1,f_2,\ldots,f_K$ in this tree.

We define $d(p,q)$ to be the number of edges on the unique path from node $p$ to node $q$.

You are given a node $a$. For each node $b$ from $1$ to $N$, find the maximum value of $d(a,u)-d(b,u)$ where $u$ is a special node, as well as any special node $u$ for which that maximum value is attained.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $K$, $a$.
- The second line contains $K$ space-separated integers $f_1,f_2,\ldots,f_K$.
- $N-1$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $u_i$ and $v_i$ denoting an edge of the tree.

---

## Output Format

For each test case, print two lines.

In the first line print $N$ space-separated integers. For each valid $i$, the $i$-th integer should be the maximum value of $d(a,u)-d(i,u)$ where $u$ is a special node.

In the second line print $N$ space-separated integers. For each valid $i$, the $i$-th integer should be any special node $u$ for which the maximum of $d(a,u)-d(i,u)$ is attained.

---

## Constraints

- $1 \le T \le 200$
- $1 \le K \le N \le 2 \cdot 10^5$
- $1 \le a \le N$
- $1 \le f_i \le N$ for each valid $i$
- $f_i \neq f_j$ for each valid $i$ and $j$ such that $i \neq j$
- $1 \le u_i,v_i \le N$ for each valid $i$
- the graph described on the input is a tree
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5 1 3
2
1 2
1 3
2 4
2 5
8 3 2
6 5 8
1 2
2 3
2 4
2 5
4 6
5 7
5 8
```

**Output**

```text
1 2 0 1 1
2 2 2 2 2
-1 0 -1 1 1 2 0 2
5 5 5 6 5 6 5 8
```

**Explanation**

**Example case 1:**  The following picture shows the tree in the first example case with special nodes in bold:

The only special node is the node $2$ and $a=3$. Therefore, the desired maximum is $d(a,2)-d(b,2)=d(3,2)-d(b,2)=2-d(b,2)$ for each node $b$ and it is always attained for the special node $u=2$.

**Example case 2:** The following picture shows the tree in the second example case with special nodes bolded:

The special nodes are $6$, $5$ and $8$, and $a=2$. The maximum values of $d(a,u)-d(b,u)$ ($u$ being a special node) for each $b$ are as follows:

- $b=1$: The maximum value of $d(2,u)-d(1,u)$ is $-1$ and it is achieved for $u=5$ since $d(2,5)-d(1,5)=1-2=-1$.

- $b=2$: The maximum value of $d(2,u)-d(2,u)$ is $0$ and it is achieved for $u=5$ since $d(2,5)-d(2,5)=1-1=0$.

- $b=3$: The maximum value of $d(2,u)-d(3,u)$ is $-1$ and it is achieved for $u=5$ since $d(2,5)-d(3,5)=1-2=-1$.

- $b=4$: The maximum value of $d(2,u)-d(4,u)$ is $1$ and it is achieved for $u=6$ since $d(2,6)-d(4,6)=2-1=1$.

- $b=5$: The maximum value of $d(2,u)-d(5,u)$ is $1$ and it is achieved for $u=5$ since $d(2,5)-d(5,5)=1-0=1$.

- $b=6$: The maximum value of $d(2,u)-d(6,u)$ is $2$ and it is achieved for $u=6$ since $d(2,6)-d(6,6)=2-0=2$.

- $b=7$: The maximum value of $d(2,u)-d(7,u)$ is $0$ and it is achieved for $u=5$ since $d(2,5)-d(7,5)=1-1=0$.

- $b=8$: The maximum value of $d(2,u)-d(8,u)$ is $2$ and it is achieved for $u=8$ since $d(2,8)-d(8,8)=2-0=2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME95A/problems/)

[Contest Division 2](https://www.codechef.com/LTIME95B/problems/)

[Contest Division 3](https://www.codechef.com/LTIME95C/problems/)

[Practice](https://www.codechef.com/problems/)

**Setter:** [](https://www.codechef.com/users/)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Binary Lifting, LCA.

# PROBLEM

Given a tree with N nodes, among with K nodes are marked as special. You are also given a node A. For each node B, determine the maximum value of d(A, X)-d(B, X) where d(a, b) denotes the number of edges on unique path from a to b, and X is any special node. Also, find one X node which maximizes d(A, X)-d(B, X) for each B.

# QUICK EXPLANATION

- Rooting the tree at node A. For node B, it is optimum to choose X such that the depth of LCA(X, B) is maximized.

- It is equivalent to finding the deepest ancestor P of node B such that subtree of P contains atleast 1 special node. Maximum value of d(A, X)-d(B, X) = d(A, P)-d(B, P)

# EXPLANATION

Let’s consider the following tree with A = 1 and consider B = 10, and special nodes are 5, 6 and 9.

Following images depict d(A, X) and d(B, X) by red and purple path respectively.

With X = 6

With X = 5

With X = 9

What we are looking for is the maximum value of d(A, X)-d(B, X).

These paths have common path d(L, X) for each X where L is the first common vertex on the path from A to X and path B to X.

If we root the tree on A, the first common vertex L is by definition the Lowest Common Ancestor of B and X.

Now, In order to maximize d(A, X)-d(B, X) = d(A, L)-d(B, L) where L lies on path from A to B, we can see that we need to maximize d(A, L) and minimize d(B, L) which implies we should select L closest to B such that there exists some special node X corresponding to such L.

Restating, **for a fixed B, we are looking for the lowest ancestor L of B such that subtree of L contains at least one special node.**

If you have managed to follow till here, you have solved the hard part of the problem. All that is left is implementation here.

Let’s assume for each node u, we have computed sp(u) which returns any special descendent in subtree of node u or -1 if there’s no special node in subtree of node u.

Naive way would be to consider each node B one by one and keep moving to its parent till sp(u) \neq -1.

One way to optimize is to notice the fact that if we consider all nodes on path from A to B in the order they appear, some non-prefix of nodes shall have sp(u) \neq -1 and remaining suffix (possibly empty) of nodes in this list shall have sp(u) = -1. We need to find the last node having sp(u) \neq -1.

Hence, we can use binary lifting to find the lowest ansestor of node B.

### Bonus

It is possible to solve this problem in O(N) too.

How?

Run a dfs to find sp(u) for each node u and another dfs passing the deepest node x on path from root to current node having sp(x) \neq -1 shall work. Implementation is left as an exercize.

# TIME COMPLEXITY

The time complexity of binary lifting solution is O(N*log(N)) per test case.

# SOLUTIONS

Setter's Solution O(N)
``#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 3e5+45;

int n,k,a;
int spc[N];
vector <int> g[N];
int has[N];
int dep[N],closest[N],spnode[N];

void prep(int x,int par){
    has[x] |= spc[x];

    int spn = 0;
    for(auto f : g[x]){
        if(f == par) continue;
        dep[f] = dep[x]+1;
        prep(f,x);
        has[x] |= has[f];
        if(has[f]) spn = spnode[f];
    }

    if(spc[x]) spnode[x] = x;
    else spnode[x] = spn;
}

void dfs(int x,int par){
    if(has[x]) closest[x] = x;
    else closest[x] = closest[par];
    for(auto f : g[x]){
        if(f == par) continue;
        dfs(f,x);
    }
}

void solve(){
    cin >> n >> k >> a;
    for(int i = 1; i <= n; i++){
        g[i].clear();
        spc[i] = dep[i] = closest[i] = has[i] = spnode[i] = 0;
    }

    for(int i = 1; i <= k; i++){
        int x;
        cin >> x;
        spc[x] = 1;
    }

    for(int i = 1; i < n; i++){
        int u,v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    dep[a] = 0;
    prep(a,0);
    dfs(a,0);

    for(int i = 1; i <= n; i++){
        int maxval = 2*dep[closest[i]]-dep[i];
        cout << maxval;
        if(i < n) cout << " ";
        else cout << endl;
    }

    for(int i = 1; i <= n; i++){
        cout << spnode[closest[i]];
        if(i < n) cout << " ";
        else cout << endl;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class SPTREE{
    //SOLUTION BEGIN
    int B = 18;
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), K = ni(), root = ni()-1;
        boolean[] special = new boolean[N];
        for(int i = 0; i< K; i++)special[ni()-1] = true;
        int[] from = new int[N-1], to = new int[N-1];
        for(int i = 0; i< N-1; i++){
            from[i] = ni()-1;
            to[i] = ni()-1;
        }
        int[][] tree = make(N, N-1, from, to, true);

        int[] depth = new int[N];
        int[][] par = new int[B][N];
        for(int b = 0; b< B; b++)Arrays.fill(par[b], -1);
        int[] specialDescendent = new int[N];
        Arrays.fill(specialDescendent, -1);
        dfs(tree, par, depth, special, specialDescendent, root, -1);

        int[] ans = new int[N];
        Arrays.fill(ans, Integer.MIN_VALUE);
        int[] node = new int[N];
        Arrays.fill(node, -1);
        for(int u = 0; u< N; u++){
            int cur = u;
            for(int b = B-1; b >= 0; b--)
                if(par[b][cur] != -1 && specialDescendent[par[b][cur]] == -1)
                    cur = par[b][cur];
            if(specialDescendent[cur] == -1)cur = par[0][cur];
            node[u] = specialDescendent[cur];
            ans[u] = 2*depth[cur]-depth[u];
        }
        StringBuilder o = new StringBuilder();
        for(int x:ans)o.append(x+" ");
        o.append("\n");
        for(int x:node)o.append((1+x)+" ");
        pn(o.toString());
    }
    void dfs(int[][] tree, int[][] par, int[] d, boolean[] special, int[] specialDescendent, int u, int p){
        for(int b = 1; b< B; b++)
            if(par[b-1][u] != -1)
                par[b][u] = par[b-1][par[b-1][u]];
        if(special[u])specialDescendent[u] = u;
        for(int v:tree[u])
            if(v != p){
                d[v] = d[u]+1;
                par[0][v] = u;
                dfs(tree, par, d, special, specialDescendent, v, u);
                if(specialDescendent[u] == -1)specialDescendent[u] = specialDescendent[v];
            }
    }
    int[][] make(int n, int e, int[] from, int[] to, boolean f){
        int[][] g = new int[n][];int[]cnt = new int[n];
        for(int i = 0; i< e; i++){
            cnt[from[i]]++;
            if(f)cnt[to[i]]++;
        }
        for(int i = 0; i< n; i++)g[i] = new int[cnt[i]];
        for(int i = 0; i< e; i++){
            g[from[i]][--cnt[from[i]]] = to[i];
            if(f)g[to[i]][--cnt[to[i]]] = from[i];
        }
        return g;
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
//        new SPTREE().run();
        new Thread(null, new Runnable() {public void run(){try{new SPTREE().run();}catch(Exception e){e.printStackTrace();System.exit(1);}}}, "1", 1 << 28).start();
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
