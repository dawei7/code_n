# Minimum Number of Pizzas

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINPIZZAS |
| Difficulty Rating | 1532 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [MINPIZZAS](https://www.codechef.com/practice/course/2to3stars/LP2TO301/problems/MINPIZZAS) |

---

## Problem Statement

Chef is throwing a party for his $N$ friends. There is a pizza store nearby and he wants to buy pizza for his friends. Each pizza has exactly $K$ slices. Chef's friends get sad if one gets more slices than the other. Also, Chef gets sad if there are some pizza slices left. More formally, suppose Chef buys $P$ pizzas, then everyone is happy if and only if there is a way to distribute $K \cdot P$ slices between $N$ friends.

You need to find the minimum number of pizzas Chef has to buy to share all the slices among his friends so that none of his friends gets sad. Note that Chef hates pizza and doesn't take any slices.

---

## Input Format

- First line of input contains $T$, the number of test cases. Then the test cases follow.
- Each test case contains two space-separated integers $N$ and $K$, where $N$ is the number of friends of chef and $K$ is the number of slices in a pizza.

---

## Output Format

For each test case, print the minimum number of pizzas chef has to buy to share among his friends so that none of his friends gets sad.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^5$
- $1 \leq N, K \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 3
4 2
```

**Output**

```text
1
2
2
```

**Explanation**

- **Test case $1$:** One pizza has $2$ slices. And there are $2$ friends. So chef can just buy one pizza and give one slice to one friend and another slice to another friend.
- **Test case $2$:** One pizza has $3$ slices. And there are $2$ friends. So chef can't share one pizza without being left out with a slice. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $3$ slices to one friend and $3$ to another. So the minimum number of pizzas chef needs to buy is equal to $2$.
- **Test case $3$:** One pizza has $2$ slices. And there are $4$ friends. So chef can't share one pizza among the $4$ friends. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $1$ slice to each of his friends. So the minimum number of pizzas chef needs to buy is equal to $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINPIZZAS)

[Contest: Division 1](https://www.codechef.com/LTIME102A/problems/MINPIZZAS)

[Contest: Division 2](https://www.codechef.com/LTIME102B/problems/MINPIZZAS)

[Contest: Division 3](https://www.codechef.com/LTIME102C/problems/MINPIZZAS)

**Author:** [ Jyothi Surya Prakash Bugatha](https://www.codechef.com/users/suryaprak_adm)

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

Chef is throwing a party for his N friends. There is a pizza store nearby and he wants to buy pizza for his friends. Each pizza has exactly K slices. Chef’s friends get sad if one gets more slices than the other. Also, chef gets sad if there are some pizza slices left. What’s the minimum number of pizzas chef has to buy to share all the slices among his friends so that none of his friends gets sad. Note that chef hates pizza and doesn’t take any slices.

#
[](#explanation-5)EXPLANATION:

Let the number of slices Chef ends up buying for the party be X. You need to have a number of slices that can be divided among N friends equally such that no extra slice remains. From this statement we can conclude that X must be divisible by N.

We can’t buy a fractional amount of pizza (i.e. buying half a pizza or only y slices off of a complete pizza, where y<K is impossible). Thus X/K denoting the number if pizzas must be an integer, implying X must also be divisible by K.

Thus the smallest number X that is divisible by both N and K gives us the minimum number of slices Chef needs to buy. This by definition is the LCM of N and K, therefore

X = lcm(N, K)

or,

X = (N/gcd(N, K))\times K

Since X is the number of slices Chef needs to buy, the corresponding number of pizzas will be X/K, which makes our final answer

X/K

= ((N/gcd(N, K))\times K)/K

= N/gcd(N, K)

We finally output this value.

#
[](#time-complexity-6)TIME COMPLEXITY:

 O(log(min(N, K)) per test case, as \_\_gcd in C++ uses [Euclidian method](https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm/) for calculation of GCD of 2 numbers, which has this complexity.

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
T=readIntLn(1,2e5);
while(T--)
{

    const int n=readIntSp(1,1e9),k=readIntLn(1,1e9);
    cout<<n/__gcd(n,k)<<endl;
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
    int n, k;
    cin >> n >> k;
    int lcm = n / __gcd(k, n);
    cout << lcm << endl;
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
