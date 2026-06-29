# Chef and Chocolates

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCHOCO |
| Difficulty Rating | 492 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CHEFCHOCO](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFCHOCO) |

---

## Problem Statement

Chef wants to gift $C$ chocolates to Botswal on his birthday. However, he has only $X$ chocolates with him.
The cost of $1$ chocolate is $Y$ rupees.

Find the **minimum** money in rupees Chef needs to spend so that he can gift $C$ chocolates to Botswal.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $C, X,$ and $Y$.

---

## Output Format

For each test case, output in a single line answer, the **minimum** money in rupees Chef needs to spend.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq C \leq 100$
- $0 \leq X \leq C$
- $1 \leq Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
7 5 5
10 1 1
```

**Output**

```text
10
9
```

**Explanation**

**Test Case $1$:** Chef has to gift a total of $7$ chocolates out of which he has $5$ chocolates. Thus, Chef needs to buy $2$ more chocolates, which costs him $10$ rupees.

**Test Case $2$:** Chef has to gift a total of $10$ chocolates out of which he has $1$ chocolate. Thus, Chef needs to buy $9$ more chocolates, which costs him $9$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 5 5
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
10 1 1
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START30A/problems/CHEFCHOCO)

[Contest Division 2](https://www.codechef.com/START30B/problems/CHEFCHOCO)

[Contest Division 3](https://www.codechef.com/START30C/problems/CHEFCHOCO)

[Contest Division 4](https://www.codechef.com/START30D/problems/CHEFCHOCO)

**Setter:** [Abhishek Aman](https://www.codechef.com/users/pertifiedcobra)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403), [ Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to gift C chocolates but has only X chocolates with him. The cost of 1 chocolate is Y rupees.

Find the minimum money in rupees Chef needs to spend so that he is able to gift C chocolates.

#
[](#explanation-5)EXPLANATION:

Initially there are X chocolates and chef needs to gift C chocolates. Since X \leq C,  Chef needs C-X more chocolates.

We know that 1 chocolate costs Y rupees. Therefore C-X chocolates will cost (C-X)\cdot Y  rupees

Example

C = 10, X = 4, Y = 5;

Initially Chef has 4 chocolates. We need 6 more so that Chef can gift total 10 chocolates. Cost of 1 chocolate is 5 rupees. Therefore cost of 6 chocolates is , 5 \cdot 6 = 30  rupees

Chef needs minimum 30 rupees to gift 10 chocolates

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

signed main(){
    int t;cin>>t;
    while(t--){
	    int C,X,Y;cin>>C>>X>>Y;
	    int diff=C-X;
	    int ans=diff*Y;
	    cout<<ans<<"\n";
    }
}
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
T=readIntLn(1,1e2);
while(T--)
{

    const lli c=readIntSp(0,1e2);
    const lli x=readIntSp(0,c);
    const lli y=readIntLn(1,1e2);
    cout<<y*(c-x)<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int c, x, y;
    cin >> c >> x >> y;
    int left = c - x;
    int cost = left * y;
    cout << cost << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
