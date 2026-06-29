# Yet Another Constructive Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ORANDCON |
| Difficulty Rating | 1580 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [ORANDCON](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/ORANDCON) |

---

## Problem Statement

You are given a positive integer $X$ which is at most $10^8$.

Find three **distinct** non-negative integers $A, B, C$ that do not exceed $10^9$ and satisfy the following equation:

$$(A \mid B) \mathbin{\&} (B \mid C) \mathbin{\&} (C \mid A) = X$$

Here, $\mid $ denotes the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and $\mathbin{\&}$ denotes the [bitwise AND operator](https://en.wikipedia.org/wiki/Bitwise_operation#AND).

It can be shown that a solution always exists for inputs satisfying the given constraints. If there are multiple solutions, you may print **any** of them.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing one integer, $X$.

---

## Output Format

- For each test case, print on a new line three **different** space-separated integers $A, B, C$.
- Your output will be considered correct only if $A, B, C$ are distinct non-negative integers not exceeding $10^9$ that satisfy the equation given in the problem statement.
- If there are multiple solutions, you may print **any** of them.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10^8$
- $0 \leq A, B, C \leq 10^9$
- $A, B, C$ must be pairwise distinct

---

## Examples

**Example 1**

**Input**

```text
4
3
2
13
100000000
```

**Output**

```text
1 2 3
2 3 4
6 9 13
23570468 129811858 80835401
```

**Explanation**

**Test case $1$:** $(1 \mid 2) \mathbin{\&} (2 \mid 3) \mathbin{\&} (3 \mid 1) = 3 \mathbin{\&} 3 \mathbin{\&} 3 = 3$ and hence $A = 1, B = 2, C = 3$ is one valid solution when $X = 3$. However there are several other solutions.

For example, $A = 1, B = 6, C = 3$ is also valid and will also be considered correct.

**Test case $2$:** $(2 \mid 3) \mathbin{\&} (3 \mid 4) \mathbin{\&} (4 \mid 2) = (3 \mathbin{\&} 7) \mathbin{\&} 6 = 3 \mathbin{\&} 6 = 2$.

**Test case $3$:** $(6 \mid 9) \mathbin{\&} (9 \mid 13) \mathbin{\&} (13 \mid 6) = (15 \mathbin{\&} 13) \mathbin{\&} 15 = 13 \mathbin{\&} 15 = 13$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
1 2 3
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
2 3 4
```



#### Test case 3

**Input for this case**

```text
13
```

**Output for this case**

```text
6 9 13
```



#### Test case 4

**Input for this case**

```text
100000000
```

**Output for this case**

```text
23570468 129811858 80835401
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[https://www.codechef.com/START24C/problems/ORANDCON](https://www.codechef.com/START24C/problems/ORANDCON)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

Tester: [Aryan Chaudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Rishabh Gupta](https://www.codechef.com/users/rishabhdevil)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given a positive integer X which is at most 10^8.

Find three **distinct** non-negative integers A,B,CA,B,C that do not exceed 10^9 and satisfy the following equation:

 ( A | B )   \&  ( B | C )   \&     ( C | A) = X

Here, | denotes the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and & denotes the [bitwise AND operator](https://en.wikipedia.org/wiki/Bitwise_operation#AND).

It can be shown that a solution always exists for inputs satisfying the given constraints. If there are multiple solutions, you may print any of them.

#
[](#explanation-5)EXPLANATION:

Every set bit of X must be present in (A|B), (B|C) and (A|C) which also boils down to the fact that every set bit of X must be present in at least 2 of A,B and C.

So, we can make a construction as A = X = B, C= 0. To make A!=B we can add a larger power of 2 to A(say 2^{27}), making sure it does not get larger than 10^9.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

 Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
#define LL long long
LL seed = chrono::steady_clock::now().time_since_epoch().count();
mt19937_64 rng(seed);
#define rand(l, r) uniform_int_distribution<LL>(l, r)(rng)
clock_t start = clock();

#define getchar getchar_unlocked

namespace IO {
long long readInt(char endd) {
    long long ret = 0;
    char c = getchar();
    while (c != endd) {
        ret = (ret * 10) + c - '0';
        c = getchar();
    }
    return ret;
}
long long readInt(long long L, long long R, char endd) {
    long long ret = readInt(endd);
    assert(ret >= L && ret <= R);
    return ret;
}
long long readIntSp(long long L, long long R) {
    return readInt(L, R, ' ');
}
long long readIntLn(long long L, long long R) {
    return readInt(L, R, '\n');
}
string readString(int l, int r) {
    string ret = "";
    char c = getchar();
    while (c == '0' || c == '?' || c == '1') {
        ret += c;
        c = getchar();
    }
    assert((int)ret.size() >= l && (int)ret.size() <= r);
    return ret;
}
}
using namespace IO;

const int TMAX = 100;

void solve() {
    int x = readIntLn(1, (int)1e8);
    int pos = 0, ret[3] = {0};
    for (int j=26;j>=0;--j) {
        for (int k=0;k<3;++k) {
            ret[k] |= (((pos == k) ^ ((x >> j) & 1)) << j);
        }
        pos = (pos == 2 ? 0 : pos + 1);
    }
    cout << ret[0] << " " << ret[1] << " " << ret[2] << '\n';
    assert(((ret[0] | ret[1]) & (ret[1] | ret[2]) & (ret[2] | ret[0])) == x);
}

int main() {
    int T = readIntLn(1, TMAX);
    while (T--) {
        solve();
    }
    // assert(getchar() == EOF);
    cerr << fixed << setprecision(10);
    cerr << (clock() - start) / ((long double)CLOCKS_PER_SEC) << " secs\n";
    return 0;
}
``

 Editorialist''s Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define dd double
#define endl "\n"
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define fi first
#define se second
#define vll vector<ll>
#define pll pair<ll,ll>
#define fo(i,n) for(int i=0;i<n;i++)
#define fo1(i,n) for(int i=1;i<=n;i++)
ll mod=1000000007;
ll n,k,t,m,q,flag=0;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(a) -- no. of elements strictly less than a
// s.find_by_order(i) -- itertor to ith element (0 indexed)
ll min(ll a,ll b){if(a>b)return b;else return a;}
ll max(ll a,ll b){if(a>b)return a;else return b;}
ll gcd(ll a , ll b){ if(b > a) return gcd(b , a) ; if(b == 0) return a ; return gcd(b , a%b) ;}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifdef NOOBxCODER
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #else
    #define NOOBxCODER 0
    #endif
    cin>>t;
    //t=1;
    while(t--){
        int a;
        cin>>a;
        cout<<a<<" "<<a + (1<<27)<<" "<< 0<<endl;

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}

``

</details>
