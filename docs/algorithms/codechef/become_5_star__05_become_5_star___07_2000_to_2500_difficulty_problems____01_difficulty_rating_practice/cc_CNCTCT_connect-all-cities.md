# Connect All Cities

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNCTCT |
| Difficulty Rating | 2417 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CNCTCT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CNCTCT) |

---

## Problem Statement

The country of Berland initially has $N$ isolated cities, the $i$-th city has a significance of $A_i$. The President of Berland wants to connect all the cities. He can construct a bidirectional road of length $L$ $(L > 0)$ from city $X$ to city $Y$ if $(A_X \& A_Y \& L) = L$, where $\&$ represents the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

What is the minimum total length of roads he has to construct, in order to connect all the cities in Berland? Print $-1$ if it is impossible.

Note: City $X$ and City $Y$ are said to be connected if there exists a sequence of cities $C_1, C_2, \ldots, C_K$ $(K \ge 1)$ such that $C_1 = X$, $C_K = Y$, and there exists a road from $C_i$ to $C_{i+1}$, $(1 \le i < K)$. All the cities in Berland are said to be connected when every pair of cities in Berland are connected.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains $N$ — the number of cities.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the significance of each of the $N$ cities.

---

## Output Format

For each test case, output on a new line the minimum total length of roads to connect all the cities in Berland, or $-1$ if it is impossible.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
4
4 4 4 4
3
2 4 6
```

**Output**

```text
12
6
```

**Explanation**

**Test case 1:** The following roads with minimum total length can be constructed to connect Berland:
- A road with $L=4$ between city $1$ and city $2$, since ($A_1 \& A_2 \& 4) = 4$.
- A road with $L=4$ between city $2$ and city $3$, since ($A_2 \& A_3 \& 4) = 4$.
- A road with $L=4$ between city $3$ and city $4$, since ($A_3 \& A_4 \& 4) = 4$.

**Test case 2:** The following roads with minimum total length can be constructed to connect Berland:
- A road with $L=2$ between city $1$ and city $3$, since ($A_1 \& A_3 \& 2) = 2$.
- A road with $L=4$ between city $2$ and city $3$, since ($A_2 \& A_3 \& 4) = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 4 4 4
```

**Output for this case**

```text
12
```



#### Test case 2

**Input for this case**

```text
3
2 4 6
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CNCTCT)

[Contest: Division 1](https://www.codechef.com/START66A/problems/CNCTCT)

[Contest: Division 2](https://www.codechef.com/START66B/problems/CNCTCT)

[Contest: Division 3](https://www.codechef.com/START66C/problems/CNCTCT)

[Contest: Division 4](https://www.codechef.com/START66D/problems/CNCTCT)

***Author:*** [Sai Panda](https://www.codechef.com/users/ereh)

***Testers:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2417

#
[](#prerequisites-3)PREREQUISITES:

[Kruskal’s algorithm](https://cp-algorithms.com/graph/mst_kruskal.html) to compute MST

#
[](#problem-4)PROBLEM:

Given N vertices where the i-th one has value A_i, you can draw an edge between u and v of length L if L is a submask of both A_u and A_v.

Find the minimum cost to connect all the cities, or claim it is impossible to do so.

#
[](#explanation-5)EXPLANATION:

For the moment, let us suppose we can actually connect all N vertices. Let’s make a couple of observations:

- The final graph is going to be a tree.

- Any edge L in the final graph will have its length be a power of 2, i.e, L = 2^k for some k \geq 0.

Proof

The first point should be obvious: if we have a cycle, remove some edge on it to obtain strictly lower cost while preserving connectivity.

The second point is also not hard to see: if some length contains more than one set bit, removing any set bit in it will still keep it a valid edge while reducing cost.

This immediately gives us a solution, albeit a slow one:

Consider the (multi)graph G on N vertices, where for each (u, v, k) there is an edge between u and v of length 2^k if u and v *both* have the k-th bit set.

Our answer is then nothing but the weight of the minimum spanning tree of this graph.

However, this graph can have upto 30N^2 edges, and computing them all is obviously impossible so we need to do better.

To optimize this, let’s look at how Kruskal’s MST algorithm would work on this graph:

- First, it’ll consider all edges with weight 2^0

- Then, it’ll consider all edges with weight 2^1

- Then, it’ll consider all edges with weight 2^2

\vdots

Here’s the nice thing: for a fixed k, the edges with weight 2^k have a rather special structure.

What?

Let x_1 \lt x_2 \lt \ldots \lt x_m be all the vertices with the k-th bit set.

Then, the edges with weight 2^k are exactly *all* pairs of these m vertices.

Now, suppose we find x_1, \ldots, x_m for a fixed k.

We don’t need to consider *all* pairs of these m vertices: we simply need to keep enough edges to make them all connected. The easiest way to do this is to only consider the edges (x_1, x_2), (x_2, x_3), \ldots, (x_{m-1}, x_m).

Notice that doing this immediately brings us down to \lt N edges per bit, for a total of \lt 30\cdot N edges in total.

This is small enough that we can simply run a MST algorithm on these edges directly and output the answer.

Note that if the final graph we obtain is not connected, the answer is -1 since there’s no way to connect it.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log {10^9}) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define pb push_back
#define ff first
#define ss second
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define endl "\n"

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (auto &x : a)
            cin >> x;
        int ans = 0;
        for (int k = 0; k < 30; ++k) {
            vector<int> na;
            int tt = 0, cnt = 0;
            for (auto &x : a) {
                if (x & (1ll << k))
                    tt |= x, cnt++;
                else
                    na.pb(x);
            }
            if (cnt) {
                ans += (cnt - 1) * (1ll << k);
                na.pb(tt);
                swap(a, na);
            }
        }
        if (sz(a) > 1)
            cout << -1 << endl;
        else
            cout << ans << endl;
    }
    return 0;
}
``

Tester's code (C++)
``/**
 * the_hyp0cr1t3
 * 22.11.2022 20:41:56
**/
#ifdef W
    #include <k_II.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
#endif

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << "L: " << l << ", R: " << r << ", Value Found: " << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

struct DSU {
    int N, cnt;
    vector<int> data;
    DSU(int n): N(n), cnt(n), data(n, -1) {}

    int par(int x) {
        return data[x] < 0? x : data[x] = par(data[x]);
    }

    bool merge(int x, int y) {
        x = par(x), y = par(y);
        if(x == y) return false;
        if(-data[x] < -data[y]) swap(x, y);
        data[x] += data[y];
        data[y] = x;
        cnt--;
        return true;
    }

};

int main() {
#if __cplusplus > 201703L
    namespace R = ranges;
#endif
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    int64_t sumn = 0;

    int tests = readIntLn(1, 100'000);
    while(tests--) [&] {
        int n = readIntLn(1, 100'000);
        auto a = readVectorInt(n, 0, 1'000'000'000);
        sumn += n;

        DSU dsu(n);
        int64_t ans = 0;
        for(int j = 0; j < 31; j++) {
            int prv = -1;
            for(int i = 0; i < n; i++) {
                if(~a[i] >> j & 1) continue;
                if(~prv)
                    ans += (1LL << j) * dsu.merge(prv, i);
                prv = i;
            }
        }

        cout << (dsu.cnt > 1 ? -1 : ans) << '\n';
    }();

    assert(sumn <= 300'000);

    cerr << "sumn = " << sumn << '\n';

#ifndef W
    readEOF();
#endif

} // ~W
``

Editorialist's code (Python)
``class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    dsu = UnionFind(n)
    merges = 0
    for bit in range(30):
        prv = -1
        for i in range(n):
            if (~a[i] >> bit) & 1: continue
            if prv != -1 and dsu.find(i) != dsu.find(prv):
                ans += 1 << bit
                dsu.union(i, prv)
                merges += 1
            prv = i
    print(ans if merges == n-1 else -1)
``

</details>
