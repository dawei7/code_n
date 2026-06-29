# Elections in Chefland

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ELECTIONS |
| Difficulty Rating | 1034 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ELECTIONS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ELECTIONS) |

---

## Problem Statement

There are $101$ citizens in Chefland. It is election time in Chefland and $3$ parties, $A, B$, and $C$ are contesting the elections. Party $A$ receives $X_A$ votes, party $B$ receives $X_B$ votes, and party $C$ receives $X_C$ votes.

The constitution of Chefland requires a particular party to receive a clear majority to form the government. A party is said to have a clear majority if it receives **strictly** greater than $50$ votes.

If any party has a clear majority, print the winning party (`A`, `B` or `C`). Otherwise, print `NOTA`.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains $3$ space-separated integers — $X_A$, $X_B$, and $X_C$.

---

## Output Format

For each test case, if any party has a clear majority, print the winning party (`A`, `B` or `C`). Otherwise, print `NOTA`.

You can print each letter of the string in any case (upper or lower) (for instance, strings `Nota`, `nOtA` and `notA` will be considered identical).

---

## Constraints

- $1 \leq T \leq 500$
- $0 \leq X_A, X_B, X_C \leq 101$
- $X_A + X_B + X_C = 101$

---

## Examples

**Example 1**

**Input**

```text
3
80 19 2
20 55 26
50 1 50
```

**Output**

```text
A
B
NOTA
```

**Explanation**

**Test Case $1$:** Party $A$ has received $80$ votes, which is strictly greater than $50$.

**Test Case $2$:** Party $B$ has received $55$ votes, which is strictly greater than $50$.

**Test Case $3$:** None of the parties have received strictly more than $50$ votes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
80 19 2
```

**Output for this case**

```text
A
```



#### Test case 2

**Input for this case**

```text
20 55 26
```

**Output for this case**

```text
B
```



#### Test case 3

**Input for this case**

```text
50 1 50
```

**Output for this case**

```text
NOTA
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START22A/problems/ELECTIONS)

[Contest Division 2](https://www.codechef.com/START22B/problems/ELECTIONS)

[Contest Division 3](https://www.codechef.com/START22C/problems/ELECTIONS)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are 101 citizens in Chefland. It is election time in Chefland and 3 parties, A, B, and C are contesting the elections. Party A receives X_A votes, party B receives X_B votes, and party C receives X_C votes.

The constitution of Chefland requires a particular party to receive a clear majority to form the government. A party is said to have a clear majority if it receives **strictly** greater than 50 votes.

If any party has a clear majority, print the winning party (`A`, `B` or `C`). Otherwise, print `NOTA`.

#
[](#explanation-5)EXPLANATION:

The aim of the problem is to test the ability of converting the problem statement into an error-free running code. Note the following observation:

- There can be at max 1 party which have a clear majority. More than 1 party cannot have clear majority.

So we can check if X_A > 50 using if condition.

If Yes, the answer is A.

If No, then check for B, and then C if required.

If none of X_A, X_B, X_C are **strictly** greater than 50, then the answer is `NOTA`.

Tip for beginners

Avoid using nested *if-else conditions*. Try to use simple *if conditions* to solve the problem.

Corner Test Case
``1
50 49 2
``

The answer should be `NOTA`. The key-point is, we need X_i > 50, and not X_i \geq 50.

#
[](#time-complexity-6)TIME COMPLEXITY:

Each Test-Case will require checking constant number of conditions. Therefore it will take O(1) time for each test case.

#
[](#solution-7)SOLUTION:

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
T=readIntLn(1,500);
const lli sumVotes = 101;
while(T--)
{
    const lli A=readIntSp(0,sumVotes);
    const lli B=readIntSp(0,sumVotes-A);
    const lli C=sumVotes-A-B;
    readIntLn(C,C);
    if(2*A>sumVotes){
        cout<<"a"<<endl;
        continue;
    }
    if(2*B>sumVotes){
        cout<<"b"<<endl;
        continue;
    }
    if(2*C>sumVotes){
        cout<<"c"<<endl;
        continue;
    }
    cout<<"NoTa"<<endl;
}   aryanc403();
    readEOF();
    return 0;
}

``

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std ;

int main()
{
    int t ;
    cin >> t ;
    while(t--)
    {
        int a , b , c ;
        cin >> a >> b >> c ;

        if(a > 50)
        {
            cout << "A\n" ;
            continue ;
        }

        if(b > 50)
        {
            cout << "B\n" ;
            continue ;
        }

        if(c > 50)
        {
            cout << "C\n" ;
            continue ;
        }

        cout << "NOTA\n" ;
    }

    return 0;
}
``

</details>
