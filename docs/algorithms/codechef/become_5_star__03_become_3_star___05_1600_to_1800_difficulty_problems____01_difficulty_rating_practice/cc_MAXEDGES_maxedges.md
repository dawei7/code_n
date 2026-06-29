# MaxEdges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXEDGES |
| Difficulty Rating | 1618 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [MAXEDGES](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/MAXEDGES) |

---

## Problem Statement

Tracy gives Charlie a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) with $N$ vertices. Among these $N$ vertices, $K$ vertices are *sources*, and $L$ vertices are *sinks*.

Find out the **maximum** number of edges this graph can have.

Note:
- A *source* is a vertex with **no incoming** edge.
- A *sink* is a vertex with **no outgoing** edge.
- A vertex can be **both**, a source, and a sink.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three space-separated integers $N, K,$ and $L$ - the number of vertices, the number of sources and the number of sinks respectively.

---

## Output Format

- For each test case, output in a single line, the **maximum** number of edges this graph can have.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^9$
- $1 \leq K \lt N$
- $1 \leq L \lt N$

---

## Examples

**Example 1**

**Input**

```text
2
3 1 1
5 3 3
```

**Output**

```text
3
4
```

**Explanation**

**Test case $1$:** Assume that the vertices are numbered $1,2,$ and $3$. Let $1$ be a source and $3$ be a sink. The edges of a possible DAG are $1\rightarrow 2, 2\rightarrow 3,$ and $1\rightarrow 3$.

The number of edges in this graph are $3$. It can be shown that this is the maximum number of edges possible under given constraints.

**Test case $2$:** Assume that the vertices are numbered $1,2,3,4,$ and $5$. Let $1,2,$ and $3$ be sources and $3, 4, $ and $5$ be  sinks. The edges of a possible DAG are $1\rightarrow 4, 2\rightarrow 4, 1\rightarrow 5$ and $2\rightarrow 5$.

The number of edges in this graph are $4$. It can be shown that this is the maximum number of edges possible under given constraints.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5 3 3
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXEDGES)

[Contest: Division 1](https://www.codechef.com/NOV221A/problems/MAXEDGES)

[Contest: Division 2](https://www.codechef.com/NOV221B/problems/MAXEDGES)

[Contest: Division 3](https://www.codechef.com/NOV221C/problems/MAXEDGES)

[Contest: Division 4](https://www.codechef.com/NOV221D/problems/MAXEDGES)

***Author:*** [Janmansh](https://www.codechef.com/users/janmansh)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1618

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A DAG has N vertices, K sources, and L sinks. What is the maximum number of vertices it can have?

#
[](#explanation-5)EXPLANATION:

One simple way to ensure that whichever graph we create is a dag is to direct all edges from the lower vertex to the higher one, i.e, if we have an edge i \to j then i \lt j must hold.

Note that this is the same as taking (1, 2, 3, \ldots, N) as a topological sort of the graph.

With this condition in mind, notice that without loss of generality:

- We can assign vertices 1, 2, \ldots, K to be sources

- We can assign vertices N, N-1, \ldots, N-L+1 to be sinks

- Everything in between is neither a source nor a sink

However, note that depending on the input, K+L \gt N may be true, in which case some vertices will be both sources and sinks.

Such vertices are going to be isolated since they cannot have incoming or outgoing edges, so we can essentially ignore them. We’d like the number of such vertices to be as small as possible though, since they don’t contribute any edges.

So, if K+L \gt N, let y = K+L-N. Then, we isolate y vertices and solve the problem for (N-y, K-y, L-y) instead, so it’s enough to consider the case when K+L \leq N.

Now, we have K+L \leq N, and as noted above, the first K of them are sources and the last L are sinks.

Let x = N - K - L be the number of vertices that are neither source nor sink. Then,

- We can create an edge from each source to each non-source. There are K\cdot (N-K) such edges.

- We can create an edge from each non-sink to each sink. Of these, the ones from sources have already been counted, so this leaves us with x\cdot L new edges.

- Finally, we can create edges between the non-source, non-sink vertices. There are x of them, and each pair can contribute one edge. This gives us x\cdot(x-1)/2 edges.

Add up those three values to obtain the final answer.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define pb push_back
#define mod 1000000007
#define mp make_pair

ll fact[200005];

ll powermod(ll x,ll y){
  if(y==0) return 1;
  ll temp = powermod( x,y/2 )%mod;
  if( y%2 ){
    return (((temp*temp)%mod)*x%mod);
  }
  return (temp*temp)%mod;
}

ll power(ll x,ll y){
  if(y==0) return 1;
  ll temp = power( x,y/2 );
  if( y%2 ){
    return (((temp*temp))*x);
  }
  return (temp*temp);
}

int gcd (int a, int b) {
    return b ? gcd (b, a % b) : a;
}

ll inv(ll a, ll p){
	return powermod(a,mod-2);
}

ll nCr(ll n, ll r, ll p){
	if(r > n) return 0;
	ll t1 = fact[n];
	ll t2 = inv(fact[r],p);
	ll t3 = inv(fact[n-r],p);

	return (((t1*t2)%p)*t3)%p;
}

void solve(){
  int i, j, n, l, k;
  cin >> n >> l >> k;
  //cout << "3 4\n";
  //return;
  if(l+k <= n){
    int ans = n*(n-1)/2;
    ans -= ((l*(l-1)/2) + (k*(k-1)/2));
    //ans %= mod;
    cout << ans << "\n";
  }
  else{
    int x = l + k - n;
    n -= x;
    l -= x;
    k -= x;
    int ans = n*(n-1)/2;
    ans -= ((l*(l-1)/2) + (k*(k-1)/2));
    //ans %= mod;
    cout << ans << "\n";
  }
  return;
}

signed main(){
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  ll t=1;
  cin>>t;
  //srand(time(0));
  // fact[0]=1;
  // for(int i=1;i<200001;i++){
  //   fact[i]=i*fact[i-1];
  //   fact[i]%=mod;
  // }
  while (t--){
    solve();
  }
  //cout << "3 4\n";
  return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
            now++;
        }
        return now;
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        int nxt = nextDelimiter();
        string res;
        while (pos < nxt) {
            res += buffer[pos];
            pos++;
        }
        // cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string& pattern = "") {
        assert(minl <= maxl);
        string res = readOne();
        assert(minl <= (int) res.size());
        assert((int) res.size() <= maxl);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int minv, int maxv) {
        assert(minv <= maxv);
        int res = stoi(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    long long readLong(long long minv, long long maxv) {
        assert(minv <= maxv);
        long long res = stoll(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    while (tt--) {
        int n = in.readInt(2, 1e9);
        in.readSpace();
        int k = in.readInt(1, n - 1);
        in.readSpace();
        int l = in.readInt(1, n - 1);
        in.readEoln();
        long long ans = 0;
        if ((k + l) > n) {
            int x = k + l - n;
            ans = (k - x) * 1LL * (l - x);
        } else {
            ans = k * 1LL * (n - k) + (n - k - l) * 1LL * l + (n - k - l) * 1LL * (n - k - l - 1) / 2;
        }
        cout << ans << '\n';
    }
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k, l = map(int, input().split())
    if k+l > n:
        common = k+l-n
        n -= common
        k -= common
        l -= common
    print(k*(n-k) + (n-k-l)*(n-k-l-1)//2 + (n-k-l)*l)
``

</details>
