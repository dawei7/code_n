# Minimum number of Flips

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINFLIPS |
| Difficulty Rating | 781 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MINFLIPS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINFLIPS) |

---

## Problem Statement

Chef has an array $A$ of length $N$ consisting of $1$ and $-1$ only.

In one operation, Chef can choose any index $i$ $(1\le i \le N)$ and multiply the element $A_i$ by $-1$.

Find the **minimum** number of operations required to make the sum of the array equal to $0$. Output `-1` if the sum of the array cannot be made $0$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case consists of a single integer $N$ denoting the length of the array.
- Second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the minimum number of operations to make the sum of the array equal to $0$. Output `-1` if it is not possible to make the sum equal to $0$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $A_i = 1$ or $A_i = -1$

---

## Examples

**Example 1**

**Input**

```text
4
4
1 1 1 1
5
1 -1 1 -1 1
6
1 -1 -1 1 1 1
2
1 -1
```

**Output**

```text
2
-1
1
0
```

**Explanation**

**Test case $1$:** The minimum number of operations required is $2$. In the first operation, change $A_3$ from $1$ to $-1$. Similarly, in the second operation, change $A_4$ from $1$ to $-1$. Thus, the sum of the final array is $1+1-1-1=0$.

**Test case $2$:** It can be proven that the sum of the array cannot be made equal to zero by making any number of operations.

**Test case $3$:** We can change $A_1$ from $1$ to $-1$ in one operation. Thus, the sum of the array becomes $-1-1-1+1+1+1=0$.

**Test case $4$:** The sum of the array is already zero. Thus we do not need to make any operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
1 -1 1 -1 1
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
6
1 -1 -1 1 1 1
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
2
1 -1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START42A/problems/MINFLIPS)

[Contest Division 2](https://www.codechef.com/START42B/problems/MINFLIPS)

[Contest Division 3](https://www.codechef.com/START42C/problems/MINFLIPS)

[Contest Division 4](https://www.codechef.com/START42D/problems/MINFLIPS)

Setter: [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [ Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

781

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has an array of length N consisting of 1 and ?1 only.

In one operation Chef can choose any index and multiply it by ?1.

What is the minimum number of operations required to make sum of the array equal to 0. Output ?1 if the sum of the array cannot be made 0.

#
[](#explanation-5)EXPLANATION:

In the final array the count of -1 and 1 has to be equal to make the sum equal to 0. Hence if N is odd, it is not possible to make the sum 0. Otherwise take the count of 1 and -1 and whichever is greater, decrease its count to \frac{N}{2} by using the operation defined above.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
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
void solve()
{
    int N=readInt(2,1000,'\n');
    int A[N+1]={0};
    int sum=0;
    for(int i=1;i<=N;i++)
    {
        if(i==N)
            A[i]=readInt(-1,1,'\n');
        else
            A[i]=readInt(-1,1,' ');
        assert(A[i]!=0);
        sum+=A[i];
    }
    if(N%2==1)
    {
        cout<<-1<<'\n';
        return;
    }
    sum=abs(sum);
    cout<<(sum/2)<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,100,'\n');
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
    int n;
    cin >> n;
    int cnt1 = 0;
    vll v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        cnt1 += (v[i] == 1);
    }
    if (n & 1)
        cout << -1 << '\n';
    else if (cnt1 >= n / 2)
        cout << cnt1 - n / 2 << '\n';
    else
        cout << n / 2 - cnt1 << '\n';

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
