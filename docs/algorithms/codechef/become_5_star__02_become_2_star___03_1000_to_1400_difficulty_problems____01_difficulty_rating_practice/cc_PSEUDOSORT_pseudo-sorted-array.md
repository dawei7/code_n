# Pseudo Sorted Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PSEUDOSORT |
| Difficulty Rating | 1067 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PSEUDOSORT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PSEUDOSORT) |

---

## Problem Statement

An array $A$ of length $N$ is said to be *pseudo-sorted* if it can be made non-decreasing after performing the following operation **at most once**.
- Choose an $i$ such that $1 \le i \leq N-1$ and swap $A_i$ and $A_{i+1}$

Given an array $A$, determine if it is *pseudo-sorted* or not.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each testcase, output `YES` if the array $A$ is pseudo-sorted, `NO` otherwise.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases do not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
3 5 7 8 9
4
1 3 2 3
3
3 2 1
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case 1:** The array is already sorted in non-decreasing order.

**Test case 2:** We can choose $i = 2$ and swap $A_2$ and $A_3$. The resulting array will be $[1, 2, 3, 3]$, which is sorted in non-decreasing order.

**Test case 3:** It can be proven that the array cannot be sorted in non-decreasing order in at most one operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 5 7 8 9
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
1 3 2 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
3
3 2 1
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/APRIL222A/problems/PSEUDOSORT)

[Contest Division 2](https://www.codechef.com/APRIL222B/problems/PSEUDOSORT)

[Contest Division 3](https://www.codechef.com/APRIL222C/problems/PSEUDOSORT)

[Contest Division 4](https://www.codechef.com/APRIL222D/problems/PSEUDOSORT)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Aryan](https://www.codechef.com/users/aryanc403), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1067

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

An array A of length N is said to be *pseudo-sorted* if it can be made non-decreasing after performing the following operation **at most once**.

- Choose an i such that 1 \le i \leq N-1 and swap A_i and A_{i+1}

Given an array A, determine if it is *pseudo-sorted* or not.

#
[](#explanation-5)EXPLANATION:

In a non-decreasing array of length N there cannot be an index i such that 1 \le i \leq N-1  and  A_i>A_i+1. Therefore we keep on traversing the array from the beginning till the end and as soon as we find an index i such that A_i>A_{i+1} we swap A_i\: with\: A_{i+1} and end traversing the array.

If the array is now non-decreasing i.e. for every index i such that 1 \le i \leq N-1, we have A_i\leq A_{i+1} , the initial array A was pseudo-sorted otherwise not.

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
int sumN=0;
void solve()
{
    int n=readInt(2,100000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    vector <int> v;
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i==n)
            c=readInt(1,1000000000,'\n');
        else
            c=readInt(1,1000000000,' ');
        v.pb(c);
    }
    for(int i=1;i<n;i++)
    {
        if(v[i]<v[i-1])
        {
            swap(v[i],v[i-1]);
            break;
        }
    }
    for(int i=1;i<n;i++)
    {
        if(v[i]<v[i-1])
        {
            cout<<"NO\n";
            return;
        }
    }
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
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester-1's Solution
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

bool isBinaryString(const string s){
    for(auto x:s){
        if('0'<=x&&x<='1')
            continue;
        return false;
    }
    return true;
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
T=readIntLn(1,1e3);
lli sumN = 2e5;
while(T--)
{

    n=readIntLn(2,min(sumN,100000LL));
    sumN-=n;
    a=readVectorInt(n,1,1e9);
    auto b=a;
    sort(all(b));
    dbg(a,b);
    lli cnt=0;
    for(lli i=0;i<n;i++){
        if(a[i]==b[i])
            continue;
        cnt++;
        if(i+1==n||a[i+1]!=b[i]){
            cnt=INF;
            break;
        }
        swap(a[i],a[i+1]);
    }
    cout<<(cnt<2?"yEs":"nO")<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
#define ll long long
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

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
ll MAX=100000;
ll tes_sum=0;
vector<string> YS={"YES","yes","yES","YeS","yEs","YEs","Yes","yeS"};
vector<string> NO={"NO","no","No","nO"};
void solve(){
    ll n=readIntLn(2,MAX);
    tes_sum+=n;
    vector<ll> a;
    ll x;
    for(ll i=1;i<n;i++){
        x=readIntSp(1,1000000000);
        a.push_back(x);
    }
    x=readIntLn(1,1000000000);
    a.push_back(x);
    vector<ll> b=a;
    sort(b.begin(),b.end());
    ll prev=-MAX;
    for(ll i=0;i<n;i++){
        if(a[i]!=b[i]){
            if(prev==i-1){
                prev=n;
            }
            else if(prev==-MAX){
                prev=i;
            }
            else{
                cout<<NO[rng()%4]<<"\n";
                return;
            }
        }
    }
    cout<<YS[rng()%8]<<"\n";
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
    while(test_cases--){
        solve();
    }
    assert(getchar()==-1);
    assert(tes_sum<=200000);
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
int n;
cin>>n;
vll v(n);
bool canswap=true;
for(int i=0;i<n;i++)
{
  cin>>v[i];
  if(i && v[i]<v[i-1] && canswap)
  {
      canswap=false;
      swap(v[i],v[i-1]);
  }
}
bool issorted=true;
for(int i=1;i<n;i++)
{
    if(v[i]<v[i-1])
    issorted=false;
}
if(issorted)
cout<<"YES\n";
else
cout<<"NO\n";
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
