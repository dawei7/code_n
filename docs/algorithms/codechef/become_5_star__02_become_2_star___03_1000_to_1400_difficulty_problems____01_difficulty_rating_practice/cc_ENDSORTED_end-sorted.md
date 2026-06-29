# End Sorted

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ENDSORTED |
| Difficulty Rating | 1049 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ENDSORTED](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ENDSORTED) |

---

## Problem Statement

Chef considers a permutation $P$ of $\{1, 2, 3, \dots, N\}$ `End Sorted` if and only if $P_1 = 1$ and $P_N = N$.

Chef is given a permutation $P$.

In one operation Chef can choose any index $i \ (1 \leq i \leq N-1)$ and swap $P_i$ and $P_{i+1}$. Determine the minimum number of operations required by Chef to make the permutation $P$ `End Sorted`.

**Note:** An array $P$ is said to be a permutation of $\{1, 2, 3, \dots, N\}$ if $P$ contains each element of $\{1, 2, 3, \dots, N\}$ exactly once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, denoting the length of the permutation $P$.
    - The second line contains $N$ space-separated integers $P_1, P_2, P_3, \ldots, P_N$, denoting the permutation $P$.

---

## Output Format

For each test case, output minimum number of operations required by Chef to make the permutation $P$ `End Sorted`.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $P$ is a permutation of $\{1, 2, 3, \dots N\}$
- The sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 3 2 4
3
3 2 1
2
2 1
3
2 1 3
```

**Output**

```text
0
3
1
1
```

**Explanation**

**Test case $1$:** $P$ is already `End Sorted`.

**Test case $2$:** $P$ can be made `End Sorted` using $3$ operations as follows: $[3, 2, 1] \to [\textcolor{red}{2, 3}, 1] \to [2, \textcolor{red}{1, 3}] \to [\textcolor{red}{1, 2}, 3]$. It can be shown that achieving this in fewer than $3$ moves is impossible.

**Test case $3$:** $P$ can be made `End Sorted` using one operation, by swapping $1$ and $2$.

**Test case $4$:** $P$ can be made `End Sorted` using one operation, by swapping $1$ and $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 3 2 4
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
3 2 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
2
2 1
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
3
2 1 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START47A/problems/ENDSORTED)

[Contest Division 2](https://www.codechef.com/START47B/problems/ENDSORTED)

[Contest Division 3](https://www.codechef.com/START47C/problems/ENDSORTED)

[Contest Division 4](https://www.codechef.com/START47D/problems/ENDSORTED)

Setter:[Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [ Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav Sharma](https://www.codechef.com/users/inov_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1049

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef considers a permutation P of \{1, 2, 3, \dots, N\} `End Sorted` if and only if P_1 = 1 and P_N = N.

Chef is given a permutation P.

In one operation Chef can choose any index i \ (1 \leq i \leq N-1) and swap P_i and P_{i+1}. Determine the minimum number of operations required by Chef to make the permutation P `End Sorted`.

**Note:** An array P is said to be a permutation of \{1, 2, 3, \dots, N\} if P contains each element of \{1, 2, 3, \dots, N\} exactly once.

#
[](#explanation-5)EXPLANATION:

Let id_1 be the position of 1 in the permutation and id_N be the position of N in the permutation. We want 1 at position 1 and N at position N in the permutation. If id_1 is smaller  than id_N we will have to make at least id_1-1 swaps to get 1  at position 1 and N-id_N swaps to get N at position N in the permutation. But if id_1>id_n we will have to do id_1-1  swaps to get 1 at position 1 in the permutation. One of these swaps, swaps N and 1 hence id_N is increased by 1. Therefore the answer in this case is id_1-1+N-(id_N+1).

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
    int n=readInt(2,100000,'\n');
    sumN+=n;
    assert(sumN<=300000);
    int P[n+1]={0};
    int indx[n+1]={0};
    int mark[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        if(i!=n)
            P[i]=readInt(1,n,' ');
        else
            P[i]=readInt(1,n,'\n');
        indx[P[i]]=i;
        mark[P[i]]=1;
    }
    for(int i=1;i<=n;i++)
        assert(mark[i]==1);
    int a=indx[1];
    int b=indx[n];
    int ans=(a-1)+(n-b);
    if(a>b)
        ans--;
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
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n, id1, idn;
    cin >> n;
    vll p(n);
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
        if (p[i] == 1)
            id1 = i;
        else if (p[i] == n)
            idn = i;
    }
    if (id1 < idn)
        cout << id1 + n - 1 - idn << '\n';
    else
        cout << id1 + n - 1 - idn - 1 << '\n';

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
