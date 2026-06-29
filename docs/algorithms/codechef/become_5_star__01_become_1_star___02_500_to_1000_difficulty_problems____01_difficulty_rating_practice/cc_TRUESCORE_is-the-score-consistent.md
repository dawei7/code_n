# Is the Score Consistent

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRUESCORE |
| Difficulty Rating | 572 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [TRUESCORE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRUESCORE) |

---

## Problem Statement

Chef is watching a football match. The current score is $A:B$, that is, team $1$ has scored $A$ goals and team $2$ has scored $B$ goals. Chef wonders if it is possible for the score to become $C:D$ at a later point in the game (i.e. team $1$ has scored $C$ goals and team $2$ has scored $D$ goals). Can you help Chef by answering his question?

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $A$ and $B$ - the intial number of goals team $1$ and team $2$ have scored respectively.
- The second line of each test case contains two integers $C$ and $D$ - the final number of goals team $1$ and team $2$ must be able to score respectively.

---

## Output Format

For each testcase, output `POSSIBLE` if it is possible for the score to become $C:D$ at a later point in the game, `IMPOSSIBLE` otherwise.

You may print each character of `POSSIBLE` and `IMPOSSIBLE` in uppercase or lowercase (for example, `possible`, `pOSsiBLe`, `Possible` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A,B,C,D \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
1 5
3 5
3 4
2 6
2 2
2 2
```

**Output**

```text
POSSIBLE
IMPOSSIBLE
POSSIBLE
```

**Explanation**

**Test case 1:** The current score is $1:5$. If team $1$ scores $2$ more goals, the score will become $3:5$. Thus $3:5$ is a possible score.

**Test case 2:** The current score is $3:4$. It can be proven that no non-negative pair of integers $(x, y)$ exists such that if team $1$ scores $x$ more goals and team $2$ scores $y$ more goals the score becomes $2:6$ from $3:4$. Thus in this case $2:6$ is an impossible score.

**Test case 3:** The current score is already $2:2$. Hence it is a possible score.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
3 5
```

**Output for this case**

```text
POSSIBLE
```



#### Test case 2

**Input for this case**

```text
3 4
2 6
```

**Output for this case**

```text
IMPOSSIBLE
```



#### Test case 3

**Input for this case**

```text
2 2
2 2
```

**Output for this case**

```text
POSSIBLE
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START34A/problems/TRUESCORE)

[Contest Division 2](https://www.codechef.com/START34B/problems/TRUESCORE)

[Contest Division 3](https://www.codechef.com/START34C/problems/TRUESCORE)

[Contest Division 4](https://www.codechef.com/START34D/problems/TRUESCORE)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is watching a football match. The current score is A:B, that is, team 1 has scored A goals and team 2 has scored B goals. Chef wonders if it is possible for the score to become C:D at a later point in the game (i.e. team 1 has scored C goals and team 2 has scored D goals). Can you help Chef by answering his question?

#
[](#explanation-5)EXPLANATION:

In any match the score of any team cannot decrease with time. Therefore we just need to check whether the score of each team at a later point of time is greater or equal to the current score of that team.

Therefore if  C\geq A and D\geq B then the a score of C:D is possible after a score of A:B

otherwise it is impossible.

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
    int a=readInt(0,10,' ');
    int b=readInt(0,10,'\n');
    int c=readInt(0,10,' ');
    int d=readInt(0,10,'\n');
    if(a<=c && b<=d)
        cout<<"POSSIBLE\n";
    else
        cout<<"IMPOSSIBLE\n";
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

Tester-1's Solution(Python)
``for _ in range(int(input())):
	A, B = map(int, input().split())
	C, D = map(int, input().split())
	print('POSSIBLE' if A <= C and B <= D else 'IMPOSSIBLE')
``

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif

/*
------------------------Input Checker----------------------------------
*/

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

/*
------------------------Main code starts here----------------------------------
*/
int MAX=100000;
int check_bin(string s){
    for(auto it:s){
        if((it!='0')&&(it!='1')){
            return 0;
        }
    }
    return 1;
}
int sum_cases=0;
int last;
void solve(){
    int a=readIntSp(0,10); int b=readIntLn(0,10);
    int c=readIntSp(0,10); int d=readIntLn(0,10);
    if(min(c-a,d-b)>=0){
        cout<<"POSSIBLE\n";
    }
    else{
        cout<<"IMPOSSIBLE\n";
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    int test_cases=readIntLn(1,1000);
    last=test_cases;
    while(test_cases--){
        solve();
    }
    assert(getchar()==-1);
    return 0;
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(),_obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N=1e5+11,mod=1e9+7;
ll max(ll a,ll b) {return ((a>b)?a:b);}
ll min(ll a,ll b) {return ((a>b)?b:a);}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
int a,b,c,d;
cin>>a>>b>>c>>d;
if(a<=c && b<=d)
cout<<"POSSIBLE\n";
else
cout<<"IMPOSSIBLE\n";
return ;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int test=1;
    cin>>test;
    while(test--) sol();
}
``

</details>
