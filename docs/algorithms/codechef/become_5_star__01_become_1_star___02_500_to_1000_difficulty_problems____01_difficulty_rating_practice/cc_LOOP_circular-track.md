# Circular Track

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LOOP |
| Difficulty Rating | 838 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [LOOP](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/LOOP) |

---

## Problem Statement

There is a circular track of length $M$ consisting of $M$ checkpoints and $M$ **bidirectional** roads such that each road has a length of $1$ unit.

![](https://s3.amazonaws.com/codechef_shared/download/Images/START38/START38.png)

Chef is currently at checkpoint $A$ and wants to reach checkpoint $B$. Find the **minimum** length of the road he needs to travel.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A, B,$ and $M$ - the initial checkpoint, the final checkpoint, and the total number of checkpoints respectively.

---

## Output Format

For each test case, output the **minimum** length Chef needs to travel.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq M \leq 10^9$
- $1 \leq A, B \leq M$
- $A \neq B$

---

## Examples

**Example 1**

**Input**

```text
4
1 3 100
1 98 100
40 30 50
2 1 2
```

**Output**

```text
2
3
10
1
```

**Explanation**

**Test Case $1$:** Chef can go from $1$ to $3$ as: $1 \rightarrow 2$ and then $2 \rightarrow 3$. Thus, total length travelled is $2$ units.

**Test Case $2$:** Chef can go from $1$ to $98$ as: $98 \leftarrow 99 \leftarrow 100 \leftarrow 1$. Thus, minimum distance travelled is $3$ units.

**Test Case $3$:** Chef can go from $40$ to $30$ as: $30 \leftarrow 31 \leftarrow 32 \leftarrow \dots \leftarrow 39 \leftarrow 40$. Thus, minimum distance travelled is $10$ units.

**Test Case $4$:** Chef can go from $2$ to $1$ as: $1 \leftarrow 2$. Thus, minimum distance travelled is $1$ unit.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3 100
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1 98 100
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
40 30 50
```

**Output for this case**

```text
10
```



#### Test case 4

**Input for this case**

```text
2 1 2
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

[Contest Division 1](https://www.codechef.com/START38A/problems/LOOP)

[Contest Division 2](https://www.codechef.com/START38B/problems/LOOP)

[Contest Division 3](https://www.codechef.com/START38C/problems/LOOP)

[Contest Division 4](https://www.codechef.com/START38D/problems/LOOP)

Setter: [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

838

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a circular track of length M consisting of M checkpoints and M **bidirectional** roads such that each road has a length of 1 unit.

Chef is currently at checkpoint A and wants to reach checkpoint B. Find the **minimum** length of the road he needs to travel.

#
[](#explanation-5)EXPLANATION:

Let A\leq B (otherwise we can swap them). Chef has two choices now:

**First Choice:** Start moving in clockwise direction until he reaches B. Distance travelled = B-A

**Second Choice:** Start moving in anti-clockwise direction until he reaches B. Distance travelled = A+M-B

Thus the answer is min(B-A,A+M-B)

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
    ll a,b,m;
    a=readInt(1,1000000000,' ');
    b=readInt(1,1000000000,' ');
    m=readInt(2,1000000000,'\n');
    assert(a>=1 && a<=m);
    assert(b>=1 && b<=m);
    assert(a!=b);
    if(a>b)
        swap(a,b);
    ll d1=(b-a);
    ll d2=a+m-b;
    cout<<min(d1,d2)<<'\n';
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
    int a, b, m;
    cin >> a >> b >> m;
    if (a > b)
        swap(a, b);
    cout << min(b - a, m - b + a) << '\n';
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
