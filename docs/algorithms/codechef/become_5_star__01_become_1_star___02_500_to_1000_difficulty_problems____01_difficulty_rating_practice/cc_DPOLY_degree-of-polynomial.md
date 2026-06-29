# Degree of Polynomial

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DPOLY |
| Difficulty Rating | 793 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [DPOLY](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DPOLY) |

---

## Problem Statement

In mathematics, the [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial) of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable $x$ with $N$ terms. The polynomial looks like $A_0\cdot x^0 + A_1\cdot x^1 + \ldots + A_{N-2}\cdot x^{N-2} + A_{N-1}\cdot x^{N-1}$ where $A_{i-1}$ denotes the coefficient of the $i^{th}$ term $x^{i-1}$ for all $(1\le i\le N)$.

Find the degree of the polynomial.

**Note:** It is guaranteed that there exists **at least** one term with non-zero coefficient.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains of a single integer $N$ - the number of terms in the polynomial.
- Second line of each test case contains of $N$ space-separated integers - the $i^{th}$ integer $A_{i-1}$ corresponds to the coefficient of $x^{i-1}$.

---

## Output Format

For each test case, output in a single line, the degree of the polynomial.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $-1000 \le A_i \le 1000$
- $A_i \ne 0$ for at least one $(0\le i \lt N)$.

---

## Examples

**Example 1**

**Input**

```text
4
1
5
2
-3 3
3
0 0 5
4
1 2 4 0
```

**Output**

```text
0
1
2
2
```

**Explanation**

**Test case $1$:** There is only one term $x^0$ with coefficient $5$. Thus, we are given a constant polynomial and the degree is $0$.

**Test case $2$:** The polynomial is $-3\cdot x^0 + 3\cdot x^1 = -3 + 3\cdot x$. Thus, the highest power of $x$ with non-zero coefficient is $1$.

**Test case $3$:** The polynomial is $0\cdot x^0 + 0\cdot x^1 + 5\cdot x^2= 0+0 + 5\cdot x^2$. Thus, the highest power of $x$ with non-zero coefficient is $2$.

**Test case $4$:** The polynomial is $1\cdot x^0 + 2\cdot x^1+ 4\cdot x^2 + 0\cdot x^3= 1 + 2\cdot x + 4\cdot x^2$. Thus, the highest power of $x$ with non-zero coefficient is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
5
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
-3 3
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
0 0 5
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
4
1 2 4 0
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

[Contest Division 1](https://www.codechef.com/MAY222A/problems/DPOLY)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/DPOLY)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/DPOLY)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/DPOLY)

Setter: [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

793

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In mathematics, the [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial) of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable x with N terms. The polynomial looks like A_0\cdot x^0 + A_1\cdot x^1 + \ldots + A_{N-2}\cdot x^{N-2} + A_{N-1}\cdot x^{N-1} where A_{i-1} denotes the coefficient of the i^{th} term x^{i-1} for all (1\le i\le N).

Find the degree of the polynomial.

**Note:** It is guaranteed that there exists **at least** one term with non-zero coefficient.

#
[](#explanation-5)EXPLANATION:

The answer to the above problem is the **largest** index i (0-based) in the array A which is non-zero.Let ans be the largest index with non-zero value. Keep on iterating on the array A from the beginning and if A_i!=0, set ans =i.

In the end output ans.

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
void solve()
{
    int n;
    n=readInt(1,1000,'\n');

    bool oneNonZero = false;
    int a[n];
    for(int i = 0; i<n-1; i++){
        int x = readInt(-1000,1000,' ');
        a[i] = x;
        if(x!=0) oneNonZero = true;
    }
    int x = readInt(-1000,1000,'\n');
    a[n-1] = x;
    if(x!=0) oneNonZero = true;

    assert(oneNonZero==true);

    for(int i = n-1;i>=0; i--){
        if(a[i]!=0){
            cout<<i<<endl;
            return;
        }
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
    vll v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    int ans = 0;
    for (int i = 0; i < n; i++)
        if (v[i])
            ans = i;
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
