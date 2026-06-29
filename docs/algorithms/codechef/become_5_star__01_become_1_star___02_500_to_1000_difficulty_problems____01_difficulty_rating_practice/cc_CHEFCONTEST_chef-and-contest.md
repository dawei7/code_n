# Chef and Contest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCONTEST |
| Difficulty Rating | 872 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CHEFCONTEST](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CHEFCONTEST) |

---

## Problem Statement

Chef and Chefina are competing against each other in a programming contest. They were both able to solve all the problems in the contest, so the winner between them must be decided by time penalty. Chef solved all the problems in $X$ minutes and made $P$ wrong submissions, while Chefina solved all the problems in $Y$ minutes and made $Q$ wrong submissions. Who won the competition (or was it a draw)?

**Note:** The time penalty is calculated as follows:
- The base time penalty is the time at which the final problem was solved (so, $X$ for Chef and $Y$ for Chefina)
- Each wrong submission adds a penalty of $10$ minutes
- The winner is the person with less penalty time. If they both have the same penalty, it is considered a draw.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers — $X,Y,P$, and $Q$ respectively.

---

## Output Format

For each test case, output a single line containing one string — the name of the winner ("Chef" or "Chefina"), or "Draw" if the match was a draw. Print each string without the quotes.

Each character of the answer can be printed in either uppercase or lowercase, i.e, the strings "Chef", "chEf", "cHeF", etc. are treated as equivalent.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 100$
- $0 \leq P,Q \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
10 8 2 3
10 10 10 10
40 21 2 0
```

**Output**

```text
Chef
Draw
Chefina
```

**Explanation**

**Test Case $1$:**
- Chef solved the problems in $10$ minutes and made $2$ wrong submissions, thus his total penalty is $10 + 2 \cdot 10 = 30$ minutes.
- Chefina solved the problems in $8$ minutes and made $3$ wrong submissions, thus her total penalty is $8 + 3 \cdot 10 = 38$ minutes.

Chef took less time, so he is the winner.

**Test Case $2$:**
- Chef solved the problems in $10$ minutes and made $10$ wrong submissions, thus his total penalty is $10 + 10 \cdot 10 = 110$ minutes.
- Chefina solved the problems in $10$ minutes and made $3$ wrong submissions, thus her total penalty is $10 + 10 \cdot 10 = 110$ minutes.

Chef and Chefina took the same time, so the match is a draw.

**Test Case $3$:**
- Chef solved the problems in $40$ minutes and made $2$ wrong submissions, thus his total penalty is $40 + 2 \cdot 10 = 60$ minutes.
- Chefina solved the problems in $21$ minutes and made $0$ wrong submissions, thus her total penalty is $21 + 0 \cdot 10 = 21$ minutes.

Chefina took less time, so she is the winner.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 8 2 3
```

**Output for this case**

```text
Chef
```



#### Test case 2

**Input for this case**

```text
10 10 10 10
```

**Output for this case**

```text
Draw
```



#### Test case 3

**Input for this case**

```text
40 21 2 0
```

**Output for this case**

```text
Chefina
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFCONTEST)

[Contest: Division 1](https://www.codechef.com/START19A/problems/CHEFCONTEST)

[Contest: Division 2](https://www.codechef.com/START19B/problems/CHEFCONTEST)

[Contest: Division 3](https://www.codechef.com/START19C/problems/CHEFCONTEST)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/Utkarsh_25dec)

***Tester:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360) and [Lavish Gupta](https://www.codechef.com/users/lavish315)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef solved all the problems of a contest in X minutes with P wrong submissions, while Chefina took Y minutes and made Q wrong submissions. Each wrong submission adds 10 minutes to the total penalty. Who did better?

#
[](#explanation-5)EXPLANATION:

Chef and Chefina both solved every problem, so we simply need to compare their total penalty times to find out who did better. Each wrong submission adds 10 minutes to penalty time. So,

- Chef’s total penalty is X + 10\cdot P minutes

- Chefina’s total penalty is Y + 10\cdot Q minutes

Simply compute these two numbers and compare them to find out who won, or if it was a draw. In most languages, this is a direct application of `if` conditions, with pseudocode looking something like this:

``if x + 10*p < y + 10*q
    Chef wins
else if x + 10*p > y + 10*q:
    Chefina wins
else
    Draw
``

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution (C++)
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll MX=200000;
ll fac[MX], ifac[MX];

const ll mod = 998244353;

ll po(ll x, ll n ){
    ll ans=1;
     while(n>0){
        if(n&1) ans=(ans*x)%mod;
        x=(x*x)%mod;
        n/=2;
     }
     return ans;
}

void solve()
{

    int x,y,p,q;
    x = readIntSp(1,100);
    y = readIntSp(1,100);
    p = readIntSp(0,100);
    q = readIntLn(0,100);

    int t1 = x+10*p;
    int t2 = y+10*q;

    if(t1<t2) cout<<"CheF";
    else if(t1==t2) cout<<"dRaW";
    else cout<<"CheFiNA";

    cout<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Tester's Solution (C++)
``#include <bits/stdc++.h>
using namespace std;
#define ll long long

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

const int MAX_T = 1000;
const int MAX_N = 100;
const int MAX_SUM_N = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll z = 998244353;
ll dp[2500005] ;

void solve()
{
    int x = readIntSp(1 , MAX_N) ;
    int y = readIntSp(1 , MAX_N) ;
    int p = readIntSp(0 , MAX_N) ;
    int q = readIntLn(0 , MAX_N) ;

    int pen1 = x + 10*p ;
    int pen2 = y + 10*q ;

    if(pen1 < pen2)
    {
        cout << "cHeF" << endl ;
        return ;
    }
    if(pen1 != pen2)
    {
        cout << "cHefIna" << endl ;
    }
    else
        cout << "dRaw" << endl ;
    return ;

}

signed main()
{
    // fast;
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve() ;
    }

    assert(getchar() == -1);
    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    // cerr<<"Sum of lengths : " << sum_n << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution (Python)
``for _ in range(int(input())):
    x, y, p, q = map(int, input().split())
    if x + 10*p < y + 10*q:
        print('Chef')
    elif x + 10*p > y + 10*q:
        print('Chefina')
    else:
        print('Draw')
``

</details>
