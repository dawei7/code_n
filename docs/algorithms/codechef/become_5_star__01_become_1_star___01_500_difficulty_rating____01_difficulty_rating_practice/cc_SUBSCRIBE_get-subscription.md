# Get Subscription

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSCRIBE |
| Difficulty Rating | 315 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SUBSCRIBE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUBSCRIBE) |

---

## Problem Statement

Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly $X$ minutes.

The meeting platform supports a meeting of maximum $30$ minutes without subscription and a meeting of unlimited duration with subscription.

Determine whether Chef needs to take a subscription or not for setting up the meet.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single integer $X$ - denoting the duration of the lecture.

---

## Output Format

For each test case, print in a single line, `YES` if Chef needs to take the subscription, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
50
3
30
80
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test Case $1$:** Without subscription, the platform allows only $30$ minutes of duration. Since Chef needs to conduct a lecture of $50$ minutes, he needs to buy the subscription.

**Test Case $2$:** Without subscription, the platform allows $30$ minutes of duration. Since Chef needs to conduct a lecture of $3$ minutes only, he does not need to buy the subscription.

**Test Case $3$:** Without subscription, the platform allows $30$ minutes of duration. Since Chef needs to conduct a lecture of $30$ minutes only, he does not need to buy the subscription.

**Test Case $4$:** Without subscription, the platform allows only $30$ minutes of duration. Since Chef needs to conduct a lecture of $80$ minutes, he needs to buy the subscription.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
50
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
30
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
80
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START38A/problems/SUBSCRIBE)

[Contest Division 2](https://www.codechef.com/START38B/problems/SUBSCRIBE)

[Contest Division 3](https://www.codechef.com/START38C/problems/SUBSCRIBE)

[Contest Division 4](https://www.codechef.com/START38D/problems/SUBSCRIBE)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

315

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to conduct a lecture for which he needs to set up a meeting of exactly X minutes but the platform supports only 30 minutes without subscription and unlimited with subscription.

Determine if Chef needs to take subscription or not for conducting the lecture.

#
[](#explanation-5)EXPLANATION:

If the meeting lasts for more than 30 minutes then chef needs to buy a subscription as the platform allows free meetings upto 30 minutes only. If the meeting is going to last for less than or equal to 30 minutes then chef does not need to buy a subscription.

This means if X\leq30  the answer is `no` otherwise the answer is `yes`

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
    int X = readInt(1,100,'\n');
    if(X<=30)
        cout<<"NO\n";
    else
        cout<<"YES\n";
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int x;
    cin >> x;
    if (x <= 30)
        cout << "NO\n";
    else
        cout << "YES\n";
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
