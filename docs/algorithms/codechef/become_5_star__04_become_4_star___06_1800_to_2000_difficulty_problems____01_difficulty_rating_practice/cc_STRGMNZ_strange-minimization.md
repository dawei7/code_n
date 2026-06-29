# Strange Minimization

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRGMNZ |
| Difficulty Rating | 1928 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [STRGMNZ](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/STRGMNZ) |

---

## Problem Statement

You are given an integer $N$. Find another integer $X (X > N)$ such that the following conditions are satisfied :

1. $X$ is not a multiple of $N$.
2. The value  $|gcd(N,X)-lcm(N,X)|$ is as small as possible.

If there are multiple answers for $X$, print any.

For reference, $gcd(u, v)$ is the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) between $u$ and $v$, while $lcm(u, v)$ refers to the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple).

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.

---

## Output Format

For each testcase, print any suitable $X$ satisfying the above two conditions for the given $N$.

---

## Constraints

- $1 \le T \le 1000$
- $2 \le N \le 10^{12}$.
- Sum of $N$ over all testcases won't exceed $5*10^{12}$.

---

## Examples

**Example 1**

**Input**

```text
2
3
4
```

**Output**

```text
4
6
```

**Explanation**

1.In first case , $GCD(3,4)$ =$1$ and $LCM(3,4)$= $12$ , $|1-12|$= $11$. $11$ is the smallest value we can get by choosing $X$ as 4.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/STRGMNZ)

[Contest: Division 3 ](https://www.codechef.com/LTIME102A/problems/STRGMNZ)

[Contest: Division 2 ](https://www.codechef.com/LTIME102A/problems/STRGMNZ)

[Contest: Division 1 ](https://www.codechef.com/LTIME102A/problems/STRGMNZ)

*Author:* [S.Manuj Nanthan ](https://www.codechef.com/users/munch_01)

*Tester :* [ Aryan Choudhary ](https://www.codechef.com/users/aryanc403)

*Editorialist:* [Mradul Bhatnagar ](https://www.codechef.com/users/mradul_adm)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

Maths, Observation

#
[](#problem-4)PROBLEM:

You are given an integer N. Find another integer X(X>N) such that the following conditions are satisfied :

-
X is not a multiple of NN.

- The value |gcd(N,X)?lcm(N,X)| is as small as possible.

If there are multiple answers for X, print any.

#
[](#explanation-5)EXPLANATION:

Let g = gcd(N, X) and let Y = \dfrac{X}{g}.

Now, |gcd(N, X) - lcm(N, X)| = |g - \dfrac{NX}{g}| = |g - NY|

Since X > N and X is not multiple of N, we have g < N.

So g < NY and hence |gcd(N, X) - lcm(N, X)| = |g - \dfrac{NX}{g}| = |g - NY| = NY - g

Now gcd(N, X) = g implies gcd(\dfrac{N}{g}, Y) = 1. Since X > N, we have Y > \dfrac{N}{g}.

So, Y \ge \dfrac{N}{g} + 1. But gcd(\dfrac{N}{g}, \dfrac{NX}{g} + 1) = 1. So, the minimum occurs at Y = \dfrac{N}{g} + 1.

So for fixed g = gcd(N, X), the minimum is equal to N(\dfrac{N}{g} + 1) - g = \dfrac{N^2}{g} - g + 1

The function \dfrac{N^2}{g} - g + 1 is decreasing function over g. So choose g as big as possible.

Let p be the smallest prime factor N, then choose g = \dfrac{N}{p} (largest factor of N)

And the answer will be equal to X = gY = g(\dfrac{N}{g} + 1) = N + g = N + N/p.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(\sqrt{N}) per test case

#
[](#solutions-7)SOLUTIONS:

Author's Solution
``#from itertools import *
#from math import *
#from bisect import *
#from collections import *
#from random import *
#from decimal import *
#from heapq import *
#from itertools import *            #Life is hard!
import sys
input=sys.stdin.readline
def inp():
    return int(input())
def st():
    return input().rstrip('\n')
def lis():
    return list(map(int,input().split()))
def ma():
    return map(int,input().split())
t=inp()
while(t):
    t-=1
    n=inp()
    fl=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            fl=i
            break
    if(fl==0):
        print(n+1)
    else:
        xx=(fl+1)*(n//fl)
        print(xx)
``

Tester's Solution
``/* in the name of Anton */

/*
  Compete against Yourself.
  Author - Aryan (@aryanc403)
  Atcoder library - https://atcoder.github.io/ac-library/production/document_en/
*/

#ifdef ARYANC403
    #include <header.h>
#else
    #pragma GCC optimize ("Ofast")
    #pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
    //#pragma GCC optimize ("-ffloat-store")
    #include<bits/stdc++.h>
    #define dbg(args...) 42;
#endif

// y_combinator from @neal template https://codeforces.com/contest/1553/submission/123849801
// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0200r0.html
template<class Fun> class y_combinator_result {
    Fun fun_;
public:
    template<class T> explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args> decltype(auto) operator()(Args &&...args) { return fun_(std::ref(*this), std::forward<Args>(args)...); }
};
template<class Fun> decltype(auto) y_combinator(Fun &&fun) { return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun)); }

using namespace std;
#define fo(i,n)   for(i=0;i<(n);++i)
#define repA(i,j,n)   for(i=(j);i<=(n);++i)
#define repD(i,j,n)   for(i=(j);i>=(n);--i)
#define all(x) begin(x), end(x)
#define sz(x) ((lli)(x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"

typedef long long int lli;
typedef long double mytype;
typedef pair<lli,lli> ii;
typedef vector<ii> vii;
typedef vector<lli> vi;

const auto start_time = std::chrono::high_resolution_clock::now();
void aryanc403()
{
#ifdef ARYANC403
auto end_time = std::chrono::high_resolution_clock::now();
std::chrono::duration<double> diff = end_time-start_time;
    cerr<<"Time Taken : "<<diff.count()<<"\n";
#endif
}

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

vi readVectorInt(int n,lli l,lli r){
    vi a(n);
    for(int i=0;i<n-1;++i)
        a[i]=readIntSp(l,r);
    a[n-1]=readIntLn(l,r);
    return a;
}

// #include<atcoder/dsu>
// vector<vi> readTree(const int n){
//     vector<vi> e(n);
//     atcoder::dsu d(n);
//     for(lli i=1;i<n;++i){
//         const lli u=readIntSp(1,n)-1;
//         const lli v=readIntLn(1,n)-1;
//         e[u].pb(v);
//         e[v].pb(u);
//         d.merge(u,v);
//     }
//     assert(d.size(0)==n);
//     return e;
// }

const lli INF = 0xFFFFFFFFFFFFFFFL;

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

class CMP
{public:
bool operator()(ii a , ii b) //For min priority_queue .
{    return ! ( a.X < b.X || ( a.X==b.X && a.Y <= b.Y ));   }};

void add( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt==m.end())         m.insert({x,cnt});
    else                    jt->Y+=cnt;
}

void del( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt->Y<=cnt)            m.erase(jt);
    else                      jt->Y-=cnt;
}

bool cmp(const ii &a,const ii &b)
{
    return a.X<b.X||(a.X==b.X&&a.Y<b.Y);
}

const lli mod = 1000000007L;
// const lli maxN = 1000000007L;

    lli T,n,i,j,k,in,cnt,l,r,u,v,x,y;
    lli m;
    string s;
    vi a;
    //priority_queue < ii , vector < ii > , CMP > pq;// min priority_queue .

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
const auto solve=[&](lli n)->lli{
    if(n==1)
        return -1;
    for(lli i=2;i*i<=n;++i){
        if(n%i)
            continue;
        return (i+1)*(n/i);
    }
    return (n+1);
};
T=readIntLn(1,1e3);
lli sumN = 5e12,maxN=1e12;
while(T--)
{

    const lli n=readIntLn(2,min(maxN,sumN));
    sumN-=n;
    cout<<solve(n)<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

</details>
