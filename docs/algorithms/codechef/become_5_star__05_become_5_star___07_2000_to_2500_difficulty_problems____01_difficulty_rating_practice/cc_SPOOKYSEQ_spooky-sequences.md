# Spooky Sequences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPOOKYSEQ |
| Difficulty Rating | 2304 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SPOOKYSEQ](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SPOOKYSEQ) |

---

## Problem Statement

*“I am not a witch. I’m your wife.”
\- Valerie, The Princess Bride*

Once upon a time, in a distant land, a mischievous witch spied on a group of people who were enjoying their time together.

Enveloped by a dark desire, she resolved to put an end to their merry gatherings and kill all $N$ people.

There are $N$ people, and the witch knows that the $i$-th of them has a strength of $A_i$.
The witch also knows of $M$ friendships, each between two people.
Friendship is transitive, that is, if $X$ and $Y$ are friends and $Y$ and $Z$ are friends, then $X$ and $Z$ are also friends.

The witch wants to kill all these people in a particular sequence known as a *spooky sequence*.

A sequence $S$ is called a *spooky sequence* if it satisfies the following properties:
- $S$ contains $N$ **distinct** integers, each between $1$ and $N$.
That is, $S$ is a linear order of the $N$ people.
- For any $1 \leq i \lt j \leq N$, if $S_i$ and $S_j$ are **friends**, then $A_{S_i} \leq A_{S_j}$ should hold.
That is, for any two friends, one with *strictly* higher strength cannot appear earlier in the sequence than the other.

Find the total number of *spooky sequences*. The answer can be large, so print it modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of people and number of friendships, respectively.
    - The next $M$ lines describe the friendships. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a friendship between $u_i$ and $v_i$.
    - The last line contains $N$ space-separated integers $A_1, A_2,\ldots, A_N$ — the strengths of the people.

---

## Output Format

For each test case, output on a new line the number of *spooky sequences*, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq M \leq \min(2 \cdot 10^5,N\cdot(N-1)/2)$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- Each unordered pair $(u_i, v_i)$ appears at most once in a testcase.
- $1 \leq A_i \leq 10^9$
- The sum of $N$  over all test cases won't exceed $2 \cdot 10^5$.
- The sum of $M$  over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 5
1 2
2 3
3 4
4 2
3 1
10 12 15 20 15
5 2
2 3
4 5
6 4 4 3 1
```

**Output**

```text
5
60
```

**Explanation**

**Test case $1$:** Each pair among $\{1, 2, 3, 4\}$ are friends, while $5$ is not friends with anyone else. Taking into account the strength condition for the group of $4$, there are five spooky sequences:
$[5, 1, 2, 3, 4]$
$[1, 5, 2, 3, 4]$
$[1, 2, 5, 3, 4]$
$[1, 2, 3, 5, 4]$
$[1, 2, 3, 4, 5]$

**Test case $2$:** $2$ and $3$ are friends, $4$ and $5$ are friends, and $1$ is not a friend of anyone else.
So, in any ordering:
- $A_2 = A_3$, so the order of $2$ and $3$ doesn't matter (even though they are friends).
- $4$ should appear after $5$, since $A_4\gt A_5$.
- There are no further constraints.

It can be verified that there are $60$ sequences satisfying this.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPOOKYSEQ)

[Contest: Division 1](https://www.codechef.com/START105A/problems/SPOOKYSEQ)

[Contest: Division 2](https://www.codechef.com/START105B/problems/SPOOKYSEQ)

[Contest: Division 3](https://www.codechef.com/START105C/problems/SPOOKYSEQ)

[Contest: Division 4](https://www.codechef.com/START105D/problems/SPOOKYSEQ)

***Author:***  [varshil27](https://www.codechef.com/users/varshil27)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2304

# [](#prerequisites-3)PREREQUISITES:

DFS/BFS/DSU, combinatorics

# [](#problem-4)PROBLEM:

N people have M friendships among them. Each person also has a strength A_i.

Friendship is transitive.

Find the number of orders S of these people such that, for any two friends i and j such that A_i \lt A_j, i appears before j in S.

# [](#explanation-5)EXPLANATION:

The M friendships define an undirected graph among the N people.

Further, the friendship relation being transitive really just splits the people up based on their connected components: i and j are friends with each other *if and only if* they’re in the same connected component.

So, as a first step, find all connected components of the graph.

This can be done in a variety of ways: depth-first search, breadth-first search, or even a DSU.

Now, observe that:

- Two different components don’t interfere with each others’ orders at all.

- Within a single connected component, the people must be ordered by increasing strength.

However, for a fixed strength within this component, the people can be ordered in any way.

Let’s first find the number of arrangements for a single component.

This is not too hard: as noted above, the only choice we have at all is to move around people with the same strength.

So, if there are \text{ct}[x] people with frequency x in a given component, the number of ways to arrange them is (\text{ct}[x])!, the factorial of \text{ct}[x].

So, for a single component, the total number of arrangements is the product of (\text{ct}[x])! across all x that appear in the component.

If the component is known, this is quite easy to compute: build a frequency table of all the elements in the component, then directly find the product of the required factorials.

Next, we need to think about interactions between components.

Suppose there are k components, with sizes s_1, s_2, \ldots, s_k.

Suppose we’ve also fixed an order of elements for each of the components.

How many ways do we have to arrange them into an overall order?

Answer

Recall that there’s no interaction between components at all.

So, the only thing that matters is *which* positions are chosen by the different components.

Thinking of it differently, we have k types of balls, and s_i of the i-th type. We’d like to find the number of ways to arrange these balls in a line, where balls of the same type aren’t distinguished.

That number is just

\frac{N!}{s_1! s_2! \ldots s_k!}

One way of seeing this is as follows:

- There are \binom{N}{s_1} ways to choose which s_1 positions the first type occupies.

- There are \binom{N-s_1}{s_2} ways to chose the positions of the second type.

- There are \binom{N-s_1-s_2}{s_3} ways for the third type, and so on till \binom{s_k}{s_k} ways for the k-th type.

Multiplying out everything and cancelling out factorials from the numerator/denominator will give the above expression.

See also [this article](https://en.wikipedia.org/wiki/Multinomial_theorem), specifically the “Number of unique permutations of words” section.

Note that this problem involves division under modulo.

That cannot be done directly, and must instead be done using the concept of modular inverses.

You can learn about them [from this article](https://cp-algorithms.com/algebra/module-inverse.html).

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``//Code by Varshil Kavathiya

#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

/*
****************************************************************************************************
*/

#define ll          long long
#define ld          long double
#define vll         vector<long long>
#define mll         map<long long,long long>
#define umll        unordered_map<ll,ll,custom_hash>
#define ss          second
#define ff          first
#define bs          binary_search
#define lb          lower_bound
#define ub          upper_bound
#define all(x)      x.begin(), x.end()
#define rep(i,n)    for(ll i=0;i<n;++i)
#define rep1(i,n)   for(ll i=1;i<n;++i)
#define tt          for(ll TT = 1; TT <= tc ; TT++)
#define pb          push_back
#define ppb         pop_back
#define mkp         make_pair
#define sqrt        sqrtl
#define cntSetBits  __builtin_popcountll
#define Tzeros      __builtin_ctzll
#define Lzeros      __builtin_clzll
#define endl        '\n'
#define iendl       '\n', cout<<flush
#define fast        ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL);
#define timetaken cerr<<fixed<<setprecision(10); cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl
const ll INF =      8e18;
const ll mod =      1000000007;
ll tc =             1;
const ll N =        200005;
const int dx[4] = { -1, 1, 0, 0}; const int dy[4] = {0, 0, -1, 1};
inline ll power(ll x, unsigned ll y, ll p = LLONG_MAX) {ll res = 1; x = x % p; if (x == 0) {return 0;} while (y > 0) { if (y & 1) {res = (res * x) % p;} y = y >> 1; x = (x * x) % p;} return res;} // CALCULATING POWER IN LOG(Y) TIME COMPLEXITY
inline ll inversePrimeModular(ll a, ll p) {return power(a, p - 2, p);}
ll mod_add(ll a, ll b, ll mod) {a = a % mod; b = b % mod; return (((a + b) % mod) + mod) % mod;}
ll mod_mul(ll a, ll b, ll mod) {a = a % mod; b = b % mod; return (((a * b) % mod) + mod) % mod;}
ll mod_sub(ll a, ll b, ll mod) {a = a % mod; b = b % mod; return (((a - b) % mod) + mod) % mod;}
struct custom_hash {static uint64_t splitmix64(uint64_t x) {x += 0x9e3779b97f4a7c15; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9; x = (x ^ (x >> 27)) * 0x94d049bb133111eb; return x ^ (x >> 31);} size_t operator()(uint64_t x) const {static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count(); return splitmix64(x + FIXED_RANDOM);}};
ll gcd(ll a, ll b) {if (b > a) {return gcd(b, a);} if (b == 0) {return a;} return gcd(b, a % b);}
ll lcm(ll a, ll b) {return ((a / gcd(a, b)) * b);}
template<class T, class V>istream& operator>>(istream &in, pair<T, V> &a) {in >> a.ff >> a.ss; return in;}
template<class T>istream& operator>>(istream &in, vector<T> &a) {for (auto &i : a) {in >> i;} return in;}
template<class T, class V>ostream& operator<<(ostream &os, pair<T, V> &a) {os << a.ff << " " << a.ss; return os;}
template<class T>ostream& operator<<(ostream &os, vector<T> &a) {for (int i = 0 ; i < a.size() ; i++) {if (i != 0) {os << ' ';} os << a[i];} return os;}
#define ordered_set tree<ll, null_type,less<ll>, rb_tree_tag,tree_order_statistics_node_update>
// ifdef->hide & ifndef->show
#ifndef ONLINE_JUDGE
#include "debug.cpp"
#define dbg(x...) cerr << #x << ": "; __(x)
#else
#define dbg(x...)
#endif
/*
****************************************************************************************************
*/
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

            assert(!(cnt > 19 || ( cnt == 19 && fi > 1) ));
        } else if (g == endd) {
            if (is_neg) {
                x = -x;
            }

            if (!(l <= x && x <= r))
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
long long readIntSp(long long l, long long r) {
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
    return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
    return readString(l, r, ' ');
}
const ll fac_size = 500005;
vector<ll> fac(fac_size + 1);
vector<ll> inv(fac_size + 1);
void calcFact()
{
      fac[0] = 1;
      for (ll i = 1; i <= fac_size; i++)
      {
            fac[i] = mod_mul(fac[i - 1], i, mod);
      }

      inv[fac_size] = inversePrimeModular(fac[fac_size], mod);

      for (ll i = fac_size; i > 0; i--)
      {
            inv[i - 1] = mod_mul(inv[i], i, mod);
      }
}
void dfs(ll i,vector<ll>&vis,vector<ll>&store,vector<vector<ll>>&adj)
{
        vis[i] = 1;
        store.pb(i);

        for(auto &x:adj[i])
        {
            if(vis[x]==0)
            {
                dfs(x,vis,store,adj);
            }
        }
}
void solve()
{
    ll n = readInt(1, 2e5, ' ');
    ll m = readInt(0, 2e5, '\n');

    vector<vector<ll>> adj(n);
    vector<ll> store;
    rep(i,m)
    {
        ll a = readInt(1, 2e5, ' ');
        ll b = readInt(1, 2e5, '\n');
        a--;
        b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    vector<ll> s(n);
    rep(i,n)
    {
        if(i==n-1)
        {
            s[i] = readInt(1, 1e9, '\n');
        }
        else
        {
            s[i] = readInt(1, 1e9, ' ');
        }
    }
    vector<ll> vis(n);
    ll ans = fac[n];
    rep(i,n)
    {
        if(vis[i]==0)
        {
            dfs(i,vis,store,adj);
            ans *= inv[store.size()];
            ans %= mod;
            map<ll, ll> cnt;
            for(auto&x:store)
            {
                cnt[s[x]]++;
            }
            for(auto&x:cnt)
            {
                ans *= fac[x.ss];
                ans %= mod;
            }
            store.clear();
        }
    }
    cout<<ans<<endl;
}
/*
****************************************************************************************************
*/

int32_t main()
{
      fast;
      cout << setprecision(30);
      calcFact();
      tc = readInt(1,2e4,'\n');
      tt
      {
            // cout << "#Case: " << TT << endl;
            solve();
      }
      timetaken;
      return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

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
        return res;
    }

    string readString(int minl, int maxl, const string &pattern = "") {
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

    auto readInts(int n, int minv, int maxv) {
        assert(n >= 0);
        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readInt(minv, maxv);
            if (i+1 < n) readSpace();
        }
        return v;
    }

    auto readLongs(int n, long long minv, long long maxv) {
        assert(n >= 0);
        vector<long long> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readLong(minv, maxv);
            if (i+1 < n) readSpace();
        }
        return v;
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

const int facN = 1e6 + 5;
const int mod = 1e9 + 7; // 998244353
int ff[facN], iff[facN];
bool facinit = false;

int power(int x, int y){
    if (y == 0) return 1;

    int v = power(x, y / 2);
    v = 1LL * v * v % mod;

    if (y & 1) return 1LL * v * x % mod;
    else return v;
}

void factorialinit(){
    facinit = true;
    ff[0] = iff[0] = 1;

    for (int i = 1; i < facN; i++){
        ff[i] = 1LL * ff[i - 1] * i % mod;
    }

    iff[facN - 1] = power(ff[facN - 1], mod - 2);
    for (int i = facN - 2; i >= 1; i--){
        iff[i] = 1LL * iff[i + 1] * (i + 1) % mod;
    }
}

int C(int n, int r){
    if (!facinit) factorialinit();

    if (n == r) return 1;

    if (r < 0 || r > n) return 0;
    return 1LL * ff[n] * iff[r] % mod * iff[n - r] % mod;
}

int P(int n, int r){
    if (!facinit) factorialinit();

    assert(0 <= r && r <= n);
    return 1LL * ff[n] * iff[n - r] % mod;
}

int Solutions(int n, int r){
    //solutions to x1 + ... + xn = r
    //xi >= 0

    return C(n + r - 1, n - 1);
}

input_checker inp;
int sum_n = 0, sum_m = 0;

void Solve()
{
    int n = inp.readInt(1, (int)2e5); inp.readSpace();
    int m = inp.readInt(0, (int)2e5); inp.readEoln();

    assert(2 * m <= n * (n - 1));

    sum_n += n;
    sum_m += m;

    vector<vector<int>> adj(n);

    assert(sum_n <= (int)2e5);
    assert(sum_m <= (int)2e5);

    set <pair<int, int>> st;

    for (int i = 1; i <= m; i++){
        int u, v;
        u = inp.readInt(1, n);
        inp.readSpace();
        v = inp.readInt(1, n);
        inp.readEoln();

        assert(u != v);
        assert(st.find({u, v}) == st.end());
        st.insert({u, v});
        st.insert({v, u});

        u--;
        v--;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto a = inp.readInts(n, 1, (int)1e9);
    inp.readEoln();

    int ans = ff[n];

    vector <bool> vis(n, false);
    for (int i = 0; i < n; i++){
        if (!vis[i]){
            queue <int> q;
            q.push(i);
            vis[i] = true;
            vector <int> b;
            b.push_back(a[i]);

            while (!q.empty()){
                int u = q.front(); q.pop();

                for (int v : adj[u]) if (!vis[v]){
                    q.push(v);
                    vis[v] = true;
                    b.push_back(a[v]);
                }
            }

            map <int, int> mp;
            for (auto x : b) mp[x]++;

            for (auto [x, y] : mp){
                ans *= ff[y]; ans %= mod;
            }

            ans *= iff[(int)b.size()];
            ans %= mod;
        }
    }

    cout << ans << "\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    factorialinit();

    t = inp.readInt(1, (int)2e4);
    inp.readEoln();

    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }

    inp.readEof();

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

mod = 10**9 + 7
maxn = 2*10**5 + 5
fac = [1]*(maxn)
for i in range(2, maxn): fac[i] = fac[i-1] * i % mod
def C(n, r):
    if n < r or r < 0: return 0
    return fac[n] * pow(fac[r] * fac[n-r], mod-2, mod) % mod

for _ in range(int(input())):
    n, m = map(int, input().split())
    D = DisjointSetUnion(n)
    for i in range(m):
        u, v = map(int, input().split())
        D.union(u-1, v-1)
    a = list(map(int, input().split()))
    comps = [ [] for _ in range(n)]
    for i in range(n): comps[D.find(i)].append(a[i])
    rem = n
    ans = 1
    for i in range(n):
        freq = {}
        for x in comps[i]:
            if x not in freq: freq[x] = 0
            freq[x] += 1
        ans = ans * C(rem, len(comps[i])) % mod
        rem -= len(comps[i])
        for x in freq.values():
            ans = ans * fac[x] % mod
    print(ans)
``

</details>
