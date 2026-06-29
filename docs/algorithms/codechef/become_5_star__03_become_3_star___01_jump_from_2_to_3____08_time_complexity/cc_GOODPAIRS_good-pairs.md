# Good Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GOODPAIRS |
| Difficulty Rating | 1469 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [GOODPAIRS](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/GOODPAIRS) |

---

## Problem Statement

You are given arrays $A$ and $B$ of length $N$ each. Determine the number of *good* pairs.

A pair $(i,j)$ $(1\le i,j \le N)$ is said to be *good* if **all** of the following conditions are satisfied:
- $i \lt j;$
- $A_i = B_j;$
- $A_j = B_i;$

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.

Description of each test case:
- First line contains an integer $N$ - denoting the length of the arrays.
- Second line contains $N$ space-separated integers $A_1, A_2, \dots A_N$ - denoting the array $A$.
- Third line contains $N$ space-separated integers $B_1, B_2, \dots B_N$ - denoting the array $B$.

---

## Output Format

For each test case, output the number of *good* pairs.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
1 2 3
3 2 1
4
1 2 3 4
5 6 6 7
3
10 10 10
10 10 10
4
4 8 1 1
8 4 1 1
```

**Output**

```text
1
0
3
2
```

**Explanation**

**Test Case $1$:** The only *good* pair $(i,j)$ is $(1,3)$. Here,
- $1 \lt 3$
- $A_1 = 1$ and $B_3 = 1$. Thus, $A_1 = B_3$.
- $A_3 = 3$ and $B_1 = 3$. Thus, $A_3 = B_1$.

**Test Case $2$:** There are no *good* pairs.

**Test Case $3$:** There are $3$ good pairs $(i,j)$. These are $(1,2), (1,3),$ and $(2,3)$.

**Test Case $4$:** There are $2$ good pairs $(i,j)$. These are $(1,2)$ and $(3,4)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
3 2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
1 2 3 4
5 6 6 7
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3
10 10 10
10 10 10
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
4
4 8 1 1
8 4 1 1
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

[Contest Division 1](https://www.codechef.com/START38A/problems/GOODPAIRS)

[Contest Division 2](https://www.codechef.com/START38B/problems/GOODPAIRS)

[Contest Division 3](https://www.codechef.com/START38C/problems/GOODPAIRS)

[Contest Division 4](https://www.codechef.com/START38D/problems/GOODPAIRS)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1469

#
[](#prerequisites-3)PREREQUISITES:

[Map data structure](https://en.cppreference.com/w/cpp/container/map)

#
[](#problem-4)PROBLEM:

You are given 2 arrays A and B of length N each. Determine the number of good pairs.

A pair (i,j) is said to be good if:

- i \lt j

- A_i = B_j

- A_j = B_i

#
[](#explanation-5)EXPLANATION:

Iterate over the arrays A and B from j=1 to N and keep count of the pair formed by (A_j,B_j). Let us now count the number of indices i for each index j (i<j) such that (i,j) form a good pair.

If (i,j) form a good pair then :

A_j=B_i and B_j=A_i;

This means the pair (A_i,B_i) is same as the pair (B_j,A_j);

Thus for each j add count of the pair (B_j,A_j)  to the answer and increase the count of (A_j,B_j) by 1

#
[](#time-complexity-6)TIME COMPLEXITY:

O(Nlog(N)) for each test case.

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
    int n=readInt(1,100000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    int A[n+1]={0}, B[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i<n)
            c=readInt(1,1000000000,' ');
        else
            c=readInt(1,1000000000,'\n');
        A[i]=c;
    }
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i<n)
            c=readInt(1,1000000000,' ');
        else
            c=readInt(1,1000000000,'\n');
        B[i]=c;
    }
    map <pair<ll,ll>,ll> cnt;
    ll ans=0;
    for(int i=1;i<=n;i++)
        cnt[mp(A[i],B[i])]++;
    for(int i=1;i<=n;i++)
    {
        cnt[mp(A[i],B[i])]--;
        ans+=cnt[mp(B[i],A[i])];
    }
    cout<<ans<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int T=readInt(1,1000,'\n');
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];
    map<pll, ll> cnt;
    ll ans = 0;
    for (int i = 0; i < n; i++)
    {
        pll p = {b[i], a[i]};
        ans += cnt[p];
        p = {p.S, p.F};
        cnt[p]++;
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
