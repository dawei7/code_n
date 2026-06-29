# Chef and Stock Prices 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CSTOCK |
| Difficulty Rating | 1069 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [CSTOCK](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CSTOCK) |

---

## Problem Statement

Chef wants to buy a stock whose price was $S$ rupees when the market opened. He will buy the stock if and only if its price is in the range $[A, B]$. The price of the stock has changed by $C\%$ by the time he was trying to buy the stock. Will he be able to buy the stock?

---

## Input Format

- First line of the input contains $T$, the number of testcases. Then the test cases follow.
- Each test case contains $4$ space-separated integers $S, A, B, C$ in a single line.

---

## Output Format

For each test case, if Chef buys the stock print `YES`, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq S \leq 10^6$
- $0 \leq A \leq B \leq 10^6$
- $-100 \leq C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
100 93 108 7
100 94 100 -7
183 152 172 -17
```

**Output**

```text
Yes
No
No
```

**Explanation**

- **Test Case $1$:** The price of the stock after gaining $7\%$ will become $107$, which is in Chef's range of $[93, 108]$. Hence, Chef will buy the stock.
- **Test Case $2$:** The price of the stock after falling $7\%$ will become $93$, which is not in Chef's range of $[94, 100]$. Hence, Chef will not buy the stock.
- **Test Case $3$:** The price of the stock after falling $17\%$ will become $151.89$, which is not in Chef's range of $[152, 172]$. Hence, Chef will not buy the stock.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 93 108 7
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
100 94 100 -7
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
183 152 172 -17
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CSTOCK)

[Contest: Division 1](https://www.codechef.com/LTIME102A/problems/CSTOCK)

[Contest: Division 2](https://www.codechef.com/LTIME102B/problems/CSTOCK)

[Contest: Division 3](https://www.codechef.com/LTIME102C/problems/CSTOCK)

**Author:** [ Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

**Tester:** [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Nandini Kapoor](https://www.codechef.com/users/costheta_z)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

Math

#
[](#problem-4)PROBLEM:

Chef wants to buy a stock whose price was S rupees when the market opened. He will buy the stock if and only if its price is in the range [A,B]. The price of the stock has changed by C% by the time he was trying to buy the stock. Will he be able to buy the stock?

#
[](#explanation-5)EXPLANATION:

We are told that the initial price of the stock, S increases by C%, implying that the price of the stock increases by C rupees for every 100 rupees worth of it. We need to figure out how much the price increases by, for every S rupees. This will give us the total increase in the original stock price.

On cross multiplying the above proportionality, we obtain

100\times x = S\times C

x = (S\times C) / 100

We’ve now established the final price of the stock -

S + (S\times C) / 100

Now we need to check whether this price lies between A and B (inclusive) or not, because we are given that Chef will buy the stock iff its price is in the range [A,B]. We print YES if the price lies between the given range, indicating that Chef can buy the stock, otherwise we print NO.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case.

#
[](#solutions-7)SOLUTIONS:

Setter
````

Tester
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
T=readIntLn(1,1000);
while(T--)
{
    const lli s=readIntSp(1,1e6);
    const lli a=readIntSp(0,1e6);
    const lli b=readIntSp(a,1e6);
    const lli c=readIntLn(-100,100);
    const lli price=s*(100+c);
    cout<<(100*a<=price&&price<=b*100?"yEs":"nO")<<endl;
}   aryanc403();
    readEOF();
    return 0;
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define _z ios_base::sync_with_stdio(false); cin.tie(NULL);
#define endl "\n"

//______________________________z_____________________________

void solve() {
    double s, a, b, c;
    cin >> s >> a >> b >> c;
    double price = s + (s*c) / 100;
    if(price <= b && price >= a) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int32_t main()
{
    _z;
    int t=1;
    cin>>t;
    while(t--) {
        solve();
    }
}

``

</details>
