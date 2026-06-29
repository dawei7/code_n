# Make them Zero

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEZERO |
| Difficulty Rating | 1320 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [MAKEZERO](https://www.codechef.com/learn/course/bit-manipulation/BITM04/problems/MAKEZERO) |

---

## Problem Statement

You are given an array $A$ of length $N$.

You can perform the following operation on the array any number of times:

- Choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) $S$ of the array $A$ and a **positive** integer $X$ such that $X$ is a power of $2$ and subtract $X$ from all the elements of the subsequence $S$.

Find the **minimum** number of operations required to make all the elements of the array equal to $0$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ denoting the length of the array $A$.
- Second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - denoting the elements of array $A$.

---

## Output Format

For each test case, output in a single line, the **minimum** number of moves required to make all the elements of the array $A$ equal to $0$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases do not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
2 2 2
4
2 2 2 4
2
0 0
3
1 2 3
```

**Output**

```text
1
2
0
2
```

**Explanation**

**Test Case $1$:** Take the subsequence with indices $\{1,2,3\}$ and subtract $2^1 = 2$ from each element.

**Test Case $2$:** Take the subsequence with indices $\{1,2,3,4\}$ and subtract $2^1 = 2$ from each element. After this operation, the array becomes $[0,0,0,2]$. Now, take the subsequence with index $\{4\}$ and subtract $2^1 = 2$ from it.

**Test Case $3$:** All the elements are already $0$.

**Test Case $4$:** Take the subsequence with indices $\{2,3\}$ and subtract $2^1=2$ from it. Now, the array becomes $[1, 0, 1]$. Now, take the subsequence with indices $\{1, 3\}$ and subtract $2^0=1$ from it.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 2 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 2 2 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
0 0
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
3
1 2 3
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

[Contest Division 1](https://www.codechef.com/MAY222A/problems/MAKEZERO)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/MAKEZERO)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/MAKEZERO)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/MAKEZERO)

Setter: [Yash Gandhi](https://www.codechef.com/users/yash0119)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1320

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A of length N.

You can perform the following operation on the array any number of times:

- Choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) S of the array A and a **positive** integer X such that X is a power of 2 and subtract X from all the elements of the subsequence S.

Find the **minimum** number of operations required to make all the elements of the array equal to 0.

#
[](#explanation-5)EXPLANATION:

Any two operations have different values of X in the optimal strategy

Let us suppose the subsequences chosen in two operations having same value of X be S_1 and S_2. Select all the elements which are present in both the subsequences and put them in new\:S_2 and and apply the operation on them taking 2\cdot X and the elements which are present only in either S_1 or only in S_2 into new\: S_1 and apply the operation by taking X as the integer. Keep doing this until there are no two operations with same value of X.

This means for each bit i which is set to 1 in the binary representation of any element K of the array A , 2^i will be subtracted, from all the elements having i^{th} bit set to 1, exactly once.

Therefore the answer is the number of different bits which are set to 1 in any element of the array.

Let OrValue be the bitwise\:OR of all the elements of the array.

Then the answer =  countofsetbits(OrValue).

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
int MaxAi=1000000000;
void solve()
{
    int n=readInt(1,100000,'\n');
    int A[n+1]={0};
    for(int i=1;i<=n;i++)
    {
    	if(i==n)
    		A[i]=readInt(0,MaxAi,'\n');
    	else
    		A[i]=readInt(0,MaxAi,' ');
    }
    ll orval=0;
    for(int i=1;i<=n;i++)
    	orval|=A[i];
    cout<<(__builtin_popcount(orval))<<'\n';
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n, ans = 0;
    cin >> n;
    vll v(n);
    int bit[30] = {0};
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        for (int j = 0; j < 30; j++)
            if ((1 << j) & v[i])
                bit[j]++;
    }
    for (int j = 0; j < 30; j++)
        ans += (bit[j] > 0);
        cout<<ans<<'\n';
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
