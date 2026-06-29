# Split and Maximize

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPLITMAX |
| Difficulty Rating | 1313 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SPLITMAX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SPLITMAX) |

---

## Problem Statement

Let $f$ be a function, such that, for an array $A$ of size $M$, $f(A)$ is defined as

$f(A) = \sum_{i=1}^{M}\sum_{j=1, j \ne i}^{j=M} (A_i\cdot A_j)$

You are given an array $C$ of size $N$. In one operation on the array, you can:
- Choose an index $i$ $(1\le i \le |C|)$
- Select two **positive integers** $X$ and $Y$ such that $X+Y = C_i$
- **Remove** the element $C_i$ from the array $C$
- **Insert** the elements $X$ and $Y$ to the array $C$

Find the **maximum** value of $f(C)$ that can be obtained using **any** (possibly zero) number of given operations. Since this value can be huge, output the answer modulo $998244353$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, denoting the size of the array.
    - The next line contains $N$ space-separated integers $C_1, C_2, \ldots, C_N$, the elements of the array $C$.

---

## Output Format

For each test case, output on a new line, the **maximum** value of $f(C)$ that can be obtained using **any** (possibly zero) number of given operations. Since this value can be huge, output the answer modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq C_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
1 2
2
1 3
```

**Output**

```text
6
12
```

**Explanation**

**Test case $1$:** Using one operation, we choose $i = 2$, set $X = 1$ and $Y = 1$, remove $2$ from the array, and insert $X$ and $Y$. Thus, the final array is $C = [1, 1, 1]$.
Here, $f(C) = (A_1\cdot A_2) + (A_1\cdot A_3) + (A_2\cdot A_1) + (A_2\cdot A_3) + (A_3\cdot A_1) + (A_3\cdot A_2) = 1+1+1+1+1+1 = 6$.

**Test case $2$:**
- Operation $1$: We choose $i = 2$, set $X = 1$ and $Y = 2$, remove $3$ from the array, and insert $X$ and $Y$. Thus, the final array is $C = [1, 1, 2]$.
- Operation $2$: We choose $i = 3$, set $X = 1$ and $Y = 1$, remove $3$ from the array, and insert $X$ and $Y$. Thus, the final array is $C = [1, 1, 1, 1]$.

Here, $f(C) = 12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
2
1 3
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPLITMAX)

[Contest: Division 1](https://www.codechef.com/NOV221A/problems/SPLITMAX)

[Contest: Division 2](https://www.codechef.com/NOV221B/problems/SPLITMAX)

[Contest: Division 3](https://www.codechef.com/NOV221C/problems/SPLITMAX)

[Contest: Division 4](https://www.codechef.com/NOV221D/problems/SPLITMAX)

***Author:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1313

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

We define the value of an array A to be

\sum_{i=1}^N \sum_{\substack{j = 1 \\ j \neq i}}^N (A_i \cdot A_j)

You have an array C. In one move, you can split some C_i into two smaller positive elements that sum to it. What’s the maximum possible value you can attain?

#
[](#explanation-5)EXPLANATION:

Let S = A_1 + A_2 + \ldots + A_N.

The formula for value specifically excludes the product of an element with itself. When we rewrite it a bit to add that part back in,

\sum_{i=1}^N \sum_{\substack{j = 1 \\ j \neq i}}^N (A_i \cdot A_j) = \sum_{i=1}^N \sum_{\substack{j = 1}}^N (A_i \cdot A_j) - \sum_{i=1}^N A_i^2 \\
= \sum_{i=1}^N A_i \left ( \sum_{j=1}^N A_j\right ) - \sum_{i=1}^N A_i^2= \sum_{i=1}^N A_i \cdot S - \sum_{i=1}^N A_i^2\\
= S^2 - \sum_{i=1}^N A_i^2

Notice that the first part of this formula, S^2, is a constant. Further, S does not change when we perform an operation, since an element is split into two with the same sum.

So, maximizing the value of the array is equivalent to minimizing the value of \sum_{i=1}^N A_i^2.

This is obviously achieved when each A_i = 1. When this happens, the length of the array will be exactly S, and so \sum_{i=1}^N A_i^2 = \sum_{i=1}^S 1^2 = S.

The final answer is hence simply S^2 - S.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define all(ds) ds.begin(), ds.end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef vector< long long > vi;
typedef pair<long long, long long> ii;
typedef priority_queue <ll> pq;
#define o_set tree<ll, null_type,less<ll>, rb_tree_tag,tree_order_statistics_node_update>

const ll mod = 998244353;
const ll INF = (ll)1e18;
const ll MAXN = 1000006;

ll po(ll x, ll n){
    ll ans=1;
    while(n>0){ if(n&1) ans=(ans*x)%mod; x=(x*x)%mod; n/=2;}
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T=1;
    cin >> T;
    while(T--){

        ll sum = 0;
        ll x;
        int n;
        cin>>n;

        rep(i,n){
            cin>>x;
            sum+=x;
        }

        sum%=mod;

        cout<<(sum*sum-sum)%mod<<el;
    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
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
int sumN=0;
void solve()
{
    int n=readInt(1,200000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    int A[n+1];
    memset(A,0,sizeof(A));
    ll sum=0;
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(1,1000000000,'\n');
        else
            A[i]=readInt(1,1000000000,' ');
        sum+=A[i];
    }
    sum%=mod;
    ll ans=(sum*sum)+(mod-sum);
    ans%=mod;
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
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python)
``mod = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print((sum(a) * sum(a) - sum(a))%mod)
``

</details>
