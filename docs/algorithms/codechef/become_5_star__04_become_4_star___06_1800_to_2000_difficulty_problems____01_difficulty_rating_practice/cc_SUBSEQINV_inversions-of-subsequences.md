# Inversions of subsequences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSEQINV |
| Difficulty Rating | 1943 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [SUBSEQINV](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/SUBSEQINV) |

---

## Problem Statement

Chef has a permutation $P$ of length $N$.

Chef wants to find the number of **non-empty** [subsequences](https://en.wikipedia.org/wiki/Subsequence) of $P$ which have the same number of *inversions* as $P$.
Since the answer can be large, output it modulo $998244353$.

Note:
- A permutation of length $N$ contains all integers from $1$ to $N$ exactly once.
- The number of *inversions* in an array $X$ is the number of pairs $(i, j)$ such that $1 \le i \lt j \le N$ and $X_i \gt X_j$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$.
    - The next line contains $N$ space-separated integers denoting the permutation $P$.

---

## Output Format

For each test case, output the number of non-empty subsequences of $P$ which have same number of inversions as $P$, modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases do not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 4 5
6
3 1 2 4 6 5
```

**Output**

```text
31
2
```

**Explanation**

**Test case $1$:** There are no inversions in the given permutation. All $2^5 - 1 = 31$ subsequences of the given permutation have $0$ inversions.

**Test case $2$:** The number of inversions in the given permutation is $3$. The subsequences with $3$ inversions are $[3, 1, 2, 4, 6, 5]$ and $[3, 1, 2, 6, 5]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
31
```



#### Test case 2

**Input for this case**

```text
6
3 1 2 4 6 5
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUBSEQINV)

[Contest: Division 1](https://www.codechef.com/START87A/problems/SUBSEQINV)

[Contest: Division 2](https://www.codechef.com/START87B/problems/SUBSEQINV)

[Contest: Division 3](https://www.codechef.com/START87C/problems/SUBSEQINV)

[Contest: Division 4](https://www.codechef.com/START87D/problems/SUBSEQINV)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1943

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics

#
[](#problem-4)PROBLEM:

Given a permutation P of length N, find the number of non-empty subsequences of P that have the same number of inversions as it.

#
[](#explanation-5)EXPLANATION:

For a subsequence S of P, let inv(S) denote its inversion count.

It should be clear that for any subsequence S, inv(S) \leq inv(P) must hold.

So, let’s try to figure out when inv(S) \lt inv(P) holds.

Consider some inversion (i, j) in P, i.e, i \lt j and P_i \gt P_j.

If a subsequence S doesn’t contain *both* i and j, then this inversion won’t be counted in inv(S), and hence inv(S) \lt inv(P) will hold.

Turning this around, for inv(S) = inv(P) to be true, S should contain *every* index that’s involved with at least one inversion.

It’s not hard to see that this condition is both necessary and sufficient, i.e, inv(S) = inv(P) if and only if S contains every index that’s part of an inversion.

So, our task shifts to computing what these positions are.

An index i is part of an inversion iff:

- There exists an index j \lt i such that P_j \gt P_i; or

- There exists an index j\gt i such that P_i \gt P_j

That means that index i is *not* part of any inversion iff P_i \gt P_j for every j\lt i, *and* P_i \lt P_j for every j \gt i.

In other words, P_i = \max(P_1, P_2, \ldots, P_i) and P_i = \min(P_i, P_{i+1}, \ldots, P_N).

By precomputing prefix maximums and suffix minimums, this can be checked for each index in \mathcal{O}(1).

Now, we know exactly which indices *must* be included in any valid subsequence S.

Each of the other indices may be included or not; they don’t affect the inversion count.

So, if there are k ‘free’ indices, the number of subsequences is 2^k.

Note that there’s a single edge-case here: if k = N, then the answer is 2^k - 1 instead, since the empty sequence will be counted in 2^k and we don’t want that.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``//Utkarsh.25dec
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 998244353
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
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
int sumN = 0;
void solve()
{
    int N = readInt(1,100000,'\n');
    sumN+=N;
    assert(sumN<=500000);
    int A[N+1];
    set <int> s;
    for(int i=1;i<=N;i++)
    {
        if(i==N)
            A[i] = readInt(1, N, '\n');
        else
            A[i] = readInt(1, N, ' ');
        s.insert(A[i]);
    }
    assert(s.size() == N);
    int prefMax[N+10];
    int suffMin[N+10];
    prefMax[0] = 0;
    suffMin[N+1] = N+1;
    for(int i=1;i<=N;i++)
        prefMax[i] = max(prefMax[i-1],A[i]);
    for(int i=N;i>=1;i--)
        suffMin[i] = min(suffMin[i+1],A[i]);
    int necessary = 0;
    for(int i=1;i<=N;i++)
    {
        if(A[i]<prefMax[i-1] || A[i]>suffMin[i+1])
            necessary++;
    }
    ll ans = power(2, N-necessary);
    if(necessary == 0)
        ans = (ans + mod - 1)%mod;
    cout<<ans<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
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

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
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

template <long long mod>
struct modular {
    long long value;
    modular(long long x = 0) {
        value = x % mod;
        if (value < 0) value += mod;
    }
    modular& operator+=(const modular& other) {
        if ((value += other.value) >= mod) value -= mod;
        return *this;
    }
    modular& operator-=(const modular& other) {
        if ((value -= other.value) < 0) value += mod;
        return *this;
    }
    modular& operator*=(const modular& other) {
        value = value * other.value % mod;
        return *this;
    }
    modular& operator/=(const modular& other) {
        long long a = 0, b = 1, c = other.value, m = mod;
        while (c != 0) {
            long long t = m / c;
            m -= t * c;
            swap(c, m);
            a -= t * b;
            swap(a, b);
        }
        a %= mod;
        if (a < 0) a += mod;
        value = value * a % mod;
        return *this;
    }
    friend modular operator+(const modular& lhs, const modular& rhs) { return modular(lhs) += rhs; }
    friend modular operator-(const modular& lhs, const modular& rhs) { return modular(lhs) -= rhs; }
    friend modular operator*(const modular& lhs, const modular& rhs) { return modular(lhs) *= rhs; }
    friend modular operator/(const modular& lhs, const modular& rhs) { return modular(lhs) /= rhs; }
    modular& operator++() { return *this += 1; }
    modular& operator--() { return *this -= 1; }
    modular operator++(int) {
        modular res(*this);
        *this += 1;
        return res;
    }
    modular operator--(int) {
        modular res(*this);
        *this -= 1;
        return res;
    }
    modular operator-() const { return modular(-value); }
    bool operator==(const modular& rhs) const { return value == rhs.value; }
    bool operator!=(const modular& rhs) const { return value != rhs.value; }
    bool operator<(const modular& rhs) const { return value < rhs.value; }
};
template <long long mod>
string to_string(const modular<mod>& x) {
    return to_string(x.value);
}
template <long long mod>
ostream& operator<<(ostream& stream, const modular<mod>& x) {
    return stream << x.value;
}
template <long long mod>
istream& operator>>(istream& stream, modular<mod>& x) {
    stream >> x.value;
    x.value %= mod;
    if (x.value < 0) x.value += mod;
    return stream;
}

constexpr long long mod = 998244353;
using mint = modular<mod>;

mint power(mint a, long long n) {
    mint res = 1;
    while (n > 0) {
        if (n & 1) {
            res *= a;
        }
        a *= a;
        n >>= 1;
    }
    return res;
}

vector<mint> fact(1, 1);
vector<mint> finv(1, 1);

mint C(int n, int k) {
    if (n < k || k < 0) {
        return mint(0);
    }
    while ((int) fact.size() < n + 1) {
        fact.emplace_back(fact.back() * (int) fact.size());
        finv.emplace_back(mint(1) / fact.back());
    }
    return fact[n] * finv[k] * finv[n - k];
}

int main() {
    input_checker in;
    int tt = in.readInt(1, 1000);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(2, 1e5);
        in.readEoln();
        sn += n;
        auto a = in.readInts(n, 1, n);
        in.readEoln();
        mint ans = 1;
        set<int> st;
        st.emplace(0);
        for (int i = 0; i < n; i++) {
            if (a[i] == i + 1 && *st.rbegin() == i) {
                ans += ans;
            }
            st.emplace(a[i]);
        }
        assert((int) st.size() == n + 1);
        if (is_sorted(a.begin(), a.end())) {
            ans--;
        }
        cout << ans << '\n';
    }
    assert(sn <= 5e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``mod = 998244353
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    prefmax, sufmin = [0]*n, [0]*n
    mx, mn = 0, n+1
    for i in range(n):
        mx = max(mx, p[i])
        if mx == p[i]: prefmax[i] = 1
        mn = min(mn, p[n-1-i])
        if mn == p[n-1-i]: sufmin[n-1-i] = 1
    ct = 0
    for i in range(n): ct += prefmax[i] * sufmin[i]
    ans = pow(2, ct, mod)
    if ct == n: ans -= 1
    print(ans)
``

</details>
