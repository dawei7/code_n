# Sasta Shark Tank

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SST |
| Difficulty Rating | 592 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SST) |

---

## Problem Statement

Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in return).

He was offered deals from two investors. The first investor offers  $A$ dollars for $10$% of his company and the second investor offers $B$ dollars for $20$% of his company. Devendra will accept the offer from the investor whose valuation of the company is more. Determine which offer will Devendra accept or if both the offers are equally good.

For example, if the first investor offers $300$ dollars for $10$% of the company, then the first investor's valuation of the company is $3000$ dollars since $10$% of $3000 = 300$. If the second investor offers $500$ dollars for $20$% of the company, then the second investor's valuation of the company is $2500$ dollars since $20$% of $2500 = 500$.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $A$ and $B$ - the amount offered by first investor for $10$% of Devendra's company and the amount offered by second investor for $20$% of Devendra's company respectively.

---

## Output Format

For each test case, Output `FIRST` if Devendra should accept the first investor's deal, output `SECOND` if he should accept the second investor's deal, otherwise output `ANY` if both deals are equally good.

You may print each character of the strings in uppercase or lowercase (for example, the strings "FiRst", "First", "FIRST", and "FIrst" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $100 \leq A,B \leq 10000$
- $A$ and $B$ are multiples of $100$

---

## Examples

**Example 1**

**Input**

```text
3
100 200
200 100
200 500
```

**Output**

```text
ANY
FIRST
SECOND
```

**Explanation**

**Test case 1:** First investor's valuation of Devendra's company was $1000$ since $10$% of $1000 = 100$ which is the amount he offered for $10$% of the company.

Second investor's valuation of Devendra's company was also $1000$ since $20$% of $1000 = 200$ which is the amount he offered for $20$% of the company.

Therefore he can accept any of the deal.

**Test case 2:** First investor offered a better deal as he valued Devendra's company at $2000$ dollars (since $10$% of $2000 = 200$) compared to the second investor who valued Devendra's company at $500$ dollars (since $20$% of $500 = 100$).

**Test case 3:** Second investor offered a better deal as he valued Devendra's company at $2500$ dollars compared to the first investor who valued Devendra's company $2000$ dollars.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 200
```

**Output for this case**

```text
ANY
```



#### Test case 2

**Input for this case**

```text
200 100
```

**Output for this case**

```text
FIRST
```



#### Test case 3

**Input for this case**

```text
200 500
```

**Output for this case**

```text
SECOND
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/APRIL222A/problems/SST)

[Contest Division 2](https://www.codechef.com/APRIL222B/problems/SST)

[Contest Division 3](https://www.codechef.com/APRIL222C/problems/SST)

[Contest Division 4](https://www.codechef.com/APRIL222D/problems/SST)

Setter: [Devendra Singh](https://www.codechef.com/users/devendra7700)

Tester: [Aryan](https://www.codechef.com/users/aryanc403), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

592

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in return).

He was offered deals from two investors. The first investor offers  A dollars for 10% of his company and the second investor offers B dollars for 20% of his company. Devendra will accept the offer from the investor whose valuation of the company is more. Determine which offer will Devendra accept or if both the offers are equally good.

For example, if the first investor offers 300 dollars for 10% of the company, then the first investor’s valuation of the company is 3000 dollars since 10% of 3000 = 300. If the second investor offers 500 dollars for 20% of the company, then the second investor’s valuation of the company is 2500 dollars since 20% of 2500 = 500.

#
[](#explanation-5)EXPLANATION:

The first investor offers A dollars for 10% of the company, then the first investor’s valuation of the company is (100/10)\cdot A= 10\cdot A dollars. The second investor offers B dollars for 20% of the company, then the second investor’s valuation of the company is (100/20)\cdot B= 5\cdot B dollars. We just need to compare these two valuations of the company by the investors and if first investor’s valuation is higher, then he should accept the offer from the first investor else if the second investor’s valuation is higher, he should accept the offer from the second investor else both offers are equally good and he can choose any of them.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

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
T=readIntLn(1,1e2);
while(T--)
{

    const lli A=readIntSp(1e2,1e4);
    const lli B=readIntLn(1e2,1e4);
    assert(A%100==0&&B%100==0);
    if(2*A==B){
        cout<<"aNy"<<endl;
        continue;
    }
    if(2*A>B){
        cout<<"fIrSt"<<endl;
        continue;
    }
    cout<<"sEcOnD"<<endl;
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
    ll a=readIntSp(100,10000);
    ll b=readIntLn(100,10000);
    assert((a%100)==0);
    assert((b%100)==0);
    a=2*a-b;
    if(a==0){
        cout<<"AnY\n";
    }
    else if(a>0){
        cout<<"fiRsT\n";
    }
    else{
        cout<<"sEcOnD\n";
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
    ll test_cases=readIntLn(1,100);
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
int a,b;
cin>>a>>b;
if(2*a>b)
cout<<"FIRST\n";
else if(2*a<b)
cout<<"SECOND\n";
else
cout<<"ANY\n";
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
