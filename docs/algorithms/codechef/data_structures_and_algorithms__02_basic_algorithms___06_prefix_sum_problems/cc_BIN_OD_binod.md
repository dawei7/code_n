# Binod

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BIN_OD |
| Difficulty Rating | 1776 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [BIN_OD](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/BIN_OD) |

---

## Problem Statement

*A Binod is a person who is very good with bitwise operations. Help Alice solve the following problem and become a Binod.*

You are given an array $A$ of $N$ elements. Process $Q$ queries on this array, of the following form:
- Each query contains $5$ integers $k, L_1, R_1, L_2, R_2$. It is guaranteed that $L_1 \leq R_1 \lt L_2 \leq R_2$.
- The answer to a query is the number of pairs $(i, j)$ such that:
    - $L_1 \leq i \leq R_1$ and $L_2 \leq j \leq R_2$
    - $A_i \oplus A_j$ has its $k$-th bit set. Here $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

**Note:** An integer $x$ is said to have its $k$-th bit set if the (unique) binary representation of $x$ contains $2^k$. For example, $5 = 101_2 = 2^0 + 2^2$ has its zeroth and second bits set but not the first, while $16 = 10000_2 = 2^4$ has only its fourth bit set.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the number of elements in array and number of queries, respectively.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
    - The next $Q$ lines describe queries. The $i$-th of these $Q$ lines contains $5$ space-separated integers $k, L_1, R_1, L_2, R_2$ — the parameters described in the statement.

---

## Output Format

For each test case, output $Q$ lines.The $i$-th of these lines should be the answer to the $i$-th query.

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq Q \leq 5\cdot 10^5$
- $0 \leq A_i \lt 2^{60}$
- $1 \leq L_1 \leq R_1 \lt L_2 \leq R_2 \leq N$.
- $0 \leq k \lt 60$
- The sum of $N$ and $Q$ over all test cases won't exceed $10^5$ and $5\cdot 10^5$ respectively.

---

## Examples

**Example 1**

**Input**

```text
2
5 2
1 2 4 3 2
1 1 3 5 5
2 1 2 3 5
6 2
3 5 6 13 12 20
1 1 4 5 6
3 2 3 4 6
```

**Output**

```text
2
2
4
4
```

**Explanation**

**Test case $1$:** The array is $A = [1, 2, 4, 3, 2]$.
- Query $1$: the ranges are $[1, 3]$ and $[5, 5]$, and $k = 1$. There are three pairs of $(i, j)$: $(1, 5), (2, 5), (3, 5)$.
    - $A_1 \oplus A_5 = 1 \oplus 2 = 3 = 11_2$ has its first bit set
    - $A_2 \oplus A_5 = 2 \oplus 2 = 0 = 0_2$ doesn't have its first bit set
    - $A_3 \oplus A_5 = 4 \oplus 2 = 6 = 110_2$ has its first bit set
    - So, the answer is $2$.
- Query $2$: the ranges are $[1, 2]$ and $[3, 5]$, and now $k = 2$. This time, there are $6$ pairs of indices. Of them, it can be verified that $(1, 3)$ and $(2, 3)$ are the ones that satisfy the given condition.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BIN_OD)

[Contest: Division 1](https://www.codechef.com/START65A/problems/BIN_OD)

[Contest: Division 2](https://www.codechef.com/START65B/problems/BIN_OD)

[Contest: Division 3](https://www.codechef.com/START65C/problems/BIN_OD)

[Contest: Division 4](https://www.codechef.com/START65D/problems/BIN_OD)

***Author:*** [Sahil Tiwari](https://www.codechef.com/users/still_me)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1776

#
[](#prerequisites-3)PREREQUISITES:

[Prefix sums](https://usaco.guide/silver/prefix-sums?lang=cpp)

#
[](#problem-4)PROBLEM:

You are given an array A and A queries on it. For each query, you are given two subarrays and an integer k.

Find the number of pairs of elements, one from the first subarray and one from the second, such that their bitwise xor has the k-th bit set.

#
[](#explanation-5)EXPLANATION:

Let’s look at answering a single query (k, L_1, R_1, L_2, R_2) first: speeding it up to answer multiple queries can come later.

Suppose A_i \oplus A_j has its k-th bit set. This is only possible when:

-
A_i has its k-th bit set and A_j doesn’t; or

-
A_j has its k-th bit set and A_i doesn’t

In particular, if take some A_i from [L_1, R_1] with its k-th bit set, we can pair it with *any* A_j from [L_2, R_2] whose k-th bit is unset.

Similarly, if take some A_i from [L_1, R_1] with its k-th bit unset, we can pair it with *any* A_j from [L_2, R_2] whose k-th bit is set.

This gives us a rather simple solution:

- Let S_1 be the number of elements in subarray [L_1, R_1] that have the k-th bit set

- Let U_1 be the number of elements in subarray [L_1, R_1] that have the k-th bit unset

- Let S_2 be the number of elements in subarray [L_2, R_2] that have the k-th bit set

- Let U_2 be the number of elements in subarray [L_2, R_2] that have the k-th bit unset

Then, the answer to this query is simply S_1\cdot U_2 + S_2\cdot U_1.

Computing S_1, S_2, U_1, U_2 is easy to do by looping across the subarrays, but that’s not fast enough to answer multiple queries: we need something a bit faster.

###
[](#using-prefix-sums-6)Using prefix sums

Notice that, if k is fixed, we can treat each element of the array as being either 0 or 1 depending on whether it has the k-th bit set or not.

Then, the above variables simplify quite nicely:

-
S_1 and S_2 are the number of ones in their respective ranges, or more specifically, just the sums of those ranges.

-
U_1 and U_2 are the number of zeros in their respective ranges. Knowing S_1, S_2, and the lengths of the ranges is enough to compute these values (since S_1 + U_1 = R_1-L_1 + 1 and S_2 + U_2 = R_2+L_2-1).

Computing range sums quickly is a well-known application of prefix sums.

We need to maintain separate prefix sums for each k, but there are only 60 possible values of k anyway so this is not an issue.

That is, for each 0 \leq k \lt 60, let pref_{k, i} denote the number of elements in [1, i] that have the k-th bit set.

Then,

- S_1 = pref_{k, R_1} - pref_{k, L_1-1}

- S_2 = pref_{k, R_2} - pref_{k, L_2-1}

-
U_1 and U_2 can be computed as noted above.

This allows us to answer each query in \mathcal{O}(1) time.

#
[](#time-complexity-7)TIME COMPLEXITY

\mathcal{O}(60\cdot N + Q) per test case.

#
[](#code-8)CODE:

Setter's code (C++)
``//	Code by Sahil Tiwari (still_me)

#include<bits/stdc++.h>
#define still_me main
#define endl "\n"
#define int long long int
#define all(a) (a).begin() , (a).end()
#define print(a) for(auto TEMPORARY: a) cout<<TEMPORARY<<" ";cout<<endl;
#define tt int TESTCASE;cin>>TESTCASE;while(TESTCASE--)
#define arrin(a,n) for(int INPUT=0;INPUT<n;INPUT++)cin>>a[INPUT]

using namespace std;
const int mod = 1e9+7;
const int inf = 1e18;

void solve() {
    int n , q;
    cin>>n>>q;
    vector<int> a(n);
    arrin(a , n);
    vector<vector<int>> b(n+1 , vector<int>(61));
    for(int i=0;i<n;i++) {
        for(int j=0;j<61;j++) {
            if(a[i] & (1ll << j))
                b[i+1][j]++;
            b[i+1][j] += b[i][j];
        }
    }
    while(q--) {
        int k , l , r , x , y;
        cin>>k>>l>>r>>x>>y;
        int o1 = b[r][k] - b[l-1][k];
        int o2 = b[y][k] - b[x-1][k];
        int z1 = r-l+1 - o1;
        int z2 = y-x+1 - o2;
        cout<<(o1*z2 + o2*z1)<<endl;
    }

}

signed still_me()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

    tt{
        solve();
    }
    return 0;
}
``

Tester's code (C++)
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
#define mod 1000000007
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
int sumN=0,sumQ=0;
void solve()
{
    int n=readInt(1,100000,' ');
    sumN+=n;
    int q=readInt(1,500000,'\n');
    sumQ+=q;
    assert(sumN<=100000);
    assert(sumQ<=500000);
    int sum[n+1][65];
    memset(sum,0,sizeof(sum));
    long long A[n+1];
    memset(A,0,sizeof(A));
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(0,1LL<<60,'\n');
        else
            A[i]=readInt(0,1LL<<60,' ');
        for(int j=0;j<60;j++)
        {
            sum[i][j]=sum[i-1][j];
            if((A[i]&(1LL<<j))!=0)
                sum[i][j]++;
        }
    }
    while(q--)
    {
        int k=readInt(0,59,' ');
        int l1=readInt(1,n,' ');
        int r1=readInt(l1,n,' ');
        int l2=readInt(r1+1,n,' ');
        int r2=readInt(l2,n,'\n');
        long long left1s=sum[r1][k]-sum[l1-1][k];
        long long left0s=(r1-l1+1)-left1s;
        long long right1s=sum[r2][k]-sum[l2-1][k];
        long long right0s=(r2-l2+1)-right1s;
        cout<<(left1s*right0s)+(left0s*right1s)<<'\n';
    }
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,50000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    pref = [[0 for i in range(60)] for _ in range(n+1)]
    for i in range(n):
        for k in range(60):
            pref[i+1][k] = pref[i][k] + ((a[i] >> k) & 1)
    for i in range(q):
        k, l1, r1, l2, r2 = map(int, input().split())
        on1, on2 = pref[r1][k] - pref[l1-1][k], pref[r2][k] - pref[l2-1][k]
        off1, off2 = r1-l1+1 - on1, r2-l2+1 - on2
        print(on1*off2 + on2*off1)
``

</details>
