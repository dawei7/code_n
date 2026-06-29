# Subarrays with length

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBARRAYLEN |
| Difficulty Rating | 1691 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [SUBARRAYLEN](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/SUBARRAYLEN) |

---

## Problem Statement

You are given an array $A$ of length $N$.

Determine the count of subarrays of $A$ which contain their length as an element.

Formally, count the number of pairs $(L, R)$ $(1\le L\le R\le N)$ such that: $(R-L+1) \in \{A_L, A_{L+1}, \ldots, A_R\}$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ denoting the length of the array $A$.
- Second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - denoting the array $A$.

---

## Output Format

For each test case, output the count of subarrays containing their lengths.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq N$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 1
5
2 3 1 3 5
10
10 7 4 4 2 9 2 1 9 3
```

**Output**

```text
4
6
15
```

**Explanation**

**Test Case $1$:** There are $4$ subarrays $(i,j)$ containing their lengths. They are $(1,1), (1,2), (2,3),$ and $(3,3)$.

**Test Case $2$:** There are $6$ subarrays $(i,j)$ containing their lengths. They are $(1,2), (1,3), (1,5), (2, 4), (3,3),$ and $(3,5)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
5
2 3 1 3 5
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
10
10 7 4 4 2 9 2 1 9 3
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MAY222A/problems/SUBARRAYLEN)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/SUBARRAYLEN)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/SUBARRAYLEN)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/SUBARRAYLEN)

Setter: [ TheScrasse](https://www.codechef.com/users/thescrasse)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A of length N.

Determine the count of subarrays of A which contain their length as an element.

Formally, count the number of pairs (L, R) (1\le L\le R\le N) such that: (R-L+1) \in \{A_L, A_{L+1}, \ldots, A_R\}.

#
[](#explanation-5)EXPLANATION:

Let us iterate over the elements of array A and for each element A_i count the number of pairs (L, R) (1\le L\le i\le R\le N) such that: (R-L+1) = A_i. The number of subarrays of a particular length which contain the element A_i can be found using the following equations:

**Left limit** for the start of such subarrays = max( 1,\: i - A_i +1)

**Right limit** for start of such subarrays = min(i, N - A_i+1)

Therefore the number of such subarrays is equal to **Right limit-Left limit+1**. But this does not account for the overcounting of subarrays. Same subarray could be counted more than once for two same values of array A. For index i = 1\:\: to\:\: N , to avoid overcounting, we will not count the subarrays which have been counted before due to some index j such that A_j=A_i.

Let last_{A_i} represent the index of last occurrence of A_i (initially 0), then the new left limits and right limits are:

**left limit** = max(last_{A_i} + 1, i - A_i + 1),

**right limit** = min(i, N - A_i+1)

Therefore the number of such subarrays is equal to **Right limit-Left limit+1**.

Sum of such subarrays for each index i =\: 1\: to\: N is the answer to the problem

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
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
int sumN=0;
void solve()
{
    int n=readInt(1,200000,'\n');
    sumN+=n;
    assert(sumN<=500000);
    int A[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(1,n,'\n');
        else
            A[i]=readInt(1,n,' ');
        adj[A[i]].pb(i);
    }
    int prev[n+1]={0};
    ll ans=0;
    for(int i=1;i<=n;i++)
    {
        ll exceed=i+A[i]-1-n;
        exceed=max(exceed,(ll)0);
        ll total=i-prev[A[i]];
        total=min(total,(ll)A[i]);
        total-=exceed;
        total=max(total,(ll)0);
        ans+=total;
        prev[A[i]]=i;
    }
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
    //cin>>T;
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N = 2e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
int last[N];
void sol(void)
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        last[i] = -1;
    vll v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    ll ans = 0;
    for (int i = 0; i < n; i++)
    {
        ll l = max(last[v[i]] + 1, i - v[i] + 1), r = min(i, n - v[i]);
        last[v[i]] = i;
        if (r >= l)
            ans += (r - l + 1);
    }
    cout << ans << '\n';
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    cin >> test;
    while (test--)
        sol();
}
``

</details>
