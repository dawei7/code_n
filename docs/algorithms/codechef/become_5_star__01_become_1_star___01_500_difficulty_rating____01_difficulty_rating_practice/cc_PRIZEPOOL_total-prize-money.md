# Total Prize Money

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIZEPOOL |
| Difficulty Rating | 296 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PRIZEPOOL](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRIZEPOOL) |

---

## Problem Statement

In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

- Top $10$ participants receive rupees $X$ each.
- Participants with rank $11$ to $100$ (both inclusive) receive rupees $Y$ each.

Find the total prize money over all the contestants.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$ - the prize for top $10$ rankers and the prize for ranks $11$ to $100$ respectively.

---

## Output Format

For each test case, output the total prize money over all the contestants.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq Y \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
1000 100
1000 1000
80 1
400 30
```

**Output**

```text
19000
100000
890
6700
```

**Explanation**

**Test Case $1$:** Top $10$ participants receive rupees $1000$ and next $90$ participants receive rupees $100$ each. So, total prize money $= 10 \cdot 1000 + 90 \cdot 100 = 19000$.

**Test Case $2$:** Top $10$ participants receive rupees $1000$ and next $90$ participants receive rupees $1000$ each. So, total prize money $= 10 \cdot 1000 + 90 \cdot 1000 = 100000$.

**Test Case $3$:** Top $10$ participants receive rupees $80$ and next $90$ participants receive rupee $1$ each. So, total prize money $= 10 \cdot 80 + 90 \cdot 1 = 890$.

**Test Case $4$:** Top $10$ participants receive rupees $400$ and next $90$ participants receive rupees $30$ each. So, total prize money $= 10 \cdot 400 + 90 \cdot 30 = 6700$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1000 100
```

**Output for this case**

```text
19000
```



#### Test case 2

**Input for this case**

```text
1000 1000
```

**Output for this case**

```text
100000
```



#### Test case 3

**Input for this case**

```text
80 1
```

**Output for this case**

```text
890
```



#### Test case 4

**Input for this case**

```text
400 30
```

**Output for this case**

```text
6700
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MAY222A/problems/PRIZEPOOL)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/PRIZEPOOL)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/PRIZEPOOL)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/PRIZEPOOL)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

296

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

- Top 10 participants receive rupees X each.

- Participants with rank 11 to 100 (both inclusive) receive rupees Y each.

Find the total prize money over all the contestants.

#
[](#explanation-5)EXPLANATION:

The total prize money for top 10 participants  = 10 \cdot X

The total prize money for next 90 participants  = 90 \cdot Y

Total prize money over all contestants = 10\cdot X\: +\: 90\cdot Y

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

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
    int x,y;
    x=readInt(1,1000,' ');
    y=readInt(1,1000,'\n');
    assert(x>=y);
    cout<<10*x+90*y<<'\n';
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int x, y;
    cin >> x >> y;
    cout << 10 * x + 90 * y << '\n';
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
