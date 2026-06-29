# Merging Binary Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MERGEBS |
| Difficulty Rating | 2318 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MERGEBS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MERGEBS) |

---

## Problem Statement

You have two binary strings $A$ and $B$, both of length $N$. You have to merge both the binary strings to form a new binary string $C$ of length $2 \cdot N$. The relative order of characters in the original binary strings $A$ and $B$ should not change in the binary string $C$.

For example, if $A = {\color{blue}01011}$ and $B = {\color{red}10100}$, one possible way to merge them to form $C$ is: $C = {\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{red}1}{\color{blue}0}{\color{blue}1}{\color{blue}1}{\color{red}0}{\color{red}0}$.

**Minimize** the number of inversions in the merged binary string $C$.

As a reminder, a pair of indices $(i, j)$ is an inversion for binary string $C$ if and only if $1 \leq i \lt j \leq |C|$, $C_i = 1$ and $C_j = 0$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$ — the length of the binary strings $A$ and $B$.
- The second line of each test case contains the binary string $A$.
- The third line of each test case contains the binary string $B$.

---

## Output Format

For each test case, output a single line containing the **minimum** number of inversions in the merged binary string $C$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2000$.
- $|A| = |B| = N$
- $A$ and $B$ are binary strings, i.e, contain only $0$ and $1$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1010
0101
5
10010
11001
5
00001
11110
```

**Output**

```text
6
12
4
```

**Explanation**

**Test Case $1$:** $A = {\color{blue}1010}$ and $B = {\color{red}0101}$. One optimal $C$ is ${\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$. The $6$ inversions in this $C$ are $\{(2, 3), (2, 5), (2, 7), (4, 5), (4, 7), (6, 7)\}$.

**Test Case $2$:** $A = {\color{blue}10010}$ and $B = {\color{red}11001}$. One optimal $C$ is ${\color{blue}1}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}0}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$.

**Test Case $3$:** $A = {\color{blue}00001}$ and $B = {\color{red}11110}$. One optimal $C$ is ${\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}0}{\color{blue}1}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1010
0101
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
5
10010
11001
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
5
00001
11110
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START22A/problems/MERGEBS)

[Contest Division 2](https://www.codechef.com/START22B/problems/MERGEBS)

[Contest Division 3](https://www.codechef.com/START22C/problems/MERGEBS)

Setter: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy-Medium

#
[](#prerequisites-3)PREREQUISITES:

Dynamic Programming, Inversions

#
[](#problem-4)PROBLEM:

You have two binary strings A and B, both of length N. You have to merge both the binary strings to form a new binary string C of length 2 \cdot N. The relative order of characters in the original binary strings A and B should not change in the binary string C.

For example, if A = {\color{blue}01011} and B = {\color{red}10100}, one possible way to merge them to form C is: C = {\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{red}1}{\color{blue}0}{\color{blue}1}{\color{blue}1}{\color{red}0}{\color{red}0}.

**Minimize** the number of inversions in the merged binary string C.

As a reminder, a pair of indices (i, j) is an inversion for binary string C if and only if 1 \leq i \lt j \leq |C|, C_i = 1 and C_j = 0.

#
[](#quick-explanation-5)QUICK EXPLANATION:

We will use the above notation of pair of indices (i, j) to denote inversions.

-

Suppose you have already merged the substrings A[1 ...  i]  and B[1...j]. So the next two characters that you need to consider are A[i+1] and B[j+1]. Which character will you take next out of these two?

-

Let A[i+1] be 1, and we choose to take this character as the next character to merge. The **new inversions** that will be created in  the future because of this step will be

\# 0's  in A[i+1  ...  N]  + \# 0's  in B[j+1  ...  N].

-

In other words, for these many indices j' in future, (i', j') will be an inversion pair, where i' = i+j+1, and j'> i'.

The same argument holds for B[j+1].

-

Let A[i+1] be 0, and we choose to take this character as the next character to merge. There will be no **new inversions** that will be created in  the future because of this step (because C_{i'} should be 1 for new inversions to be created in future that starts at this index).

-

By above explanation, we can have a dp[i][j] which denotes the number of inversions when A[i...N] and B[j...N] are merged. Note that it is little different than the above explanation, just to be consistent with how standard DPs like LCS are defined. We Calculate dp[i][j] in terms of dp[i+1][j], dp[i][j+1] and number of 0's in suffix of A and B.

#
[](#explanation-6)EXPLANATION:

Such types of problems are usually based on Greedy or Dynamic Programming approaches.

We can start our analysis by considering the following situation. Let say we have already merged the substrings A[1 ...  i]  and B[1...j]. So the next two characters that we need to consider are A[i+1] and B[j+1]. The question is, which character should we choose?

Some greedy thinking can tell you that if either of one of A[i+1] or B[j+1] is 0, then we can take this character as our next character, as it will not increase the inversion count in future. However, if we have both A[i+1] and B[j+1] as 1, then we are stuck. Which 1 to take?

There can be some more greedy things that you can think of at this point, like maybe continue choosing those 1's which will lead to a 0 faster? But you will soon realize that all these greedy algorithms will fail.

This motivates us to think in the direction of Dynamic Programming. What happens when we choose, let say A[i+1]?

There are two main observations after this merge:

- The **new inversions** that will be created in  the future because of this step will be

\# 0's  in A[i+1  ...  N]  + \# 0's  in B[j+1  ...  N].

- We now have A[i+2] and B[j+1] as our next two characters, and we essentially have the same problem again, with the reduced strings A[i+2 ... N] and B[j+1 ... N]!!

Same thing holds for B[j+1].

If A[i+1] is 0, and we merge A[i+1], then we do not create any **new inversion**.

The above explanation suggests us to have a 2-dimensional DP, say dp[i][j].

Let cnt_a[i] stores the number of 0's in $ in A[i...N], and cnt_b[i] stores the number of 0's in $ in B[i...N].

Let dp[i][j] denote the number of inversions when A[i...N] and B[j...N] are merged.

Then we will have the following transitions:

If A[i] is 0, and we merge this character, then dp[i][j] = dp[i+1][j].

If A[i] is 1, and we merge this character, then dp[i][j] = dp[i+1][j] + cnt_a[i] + cnt_b[j].

Similarly for B[j], and we take the minimum value of dp[i][j] over all these 4 cases.

#
[](#time-complexity-7)TIME COMPLEXITY:

Calculating the arrays cnt_a and cnt_b will take O(N) time.

Calculating dp[i][j] will take O(1) time, provided that required dp values are calculates and stored.

So, the overall time complexity will be O(N^2)

#
[](#solution-8)SOLUTION:

Setter's Solution
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const double EPS = 1e-9;
const long long INF = 1e18;

const int N = 1e6+5;

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int32_t main()
{
    IOS;
    int T = readIntLn(1, 1000);
    int sumN = 0;
    while(T--)
    {
        int n = readIntLn(1, 1000);
        int m = n;
        sumN += n;
        string s = readStringLn(n, n);
        string t = readStringLn(n, n);
        s = '#' + s, t = '#' + t;
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INF));
        vector<int> ps(n + 1) , pt(m + 1);
        for(int i = 1; i <= n; i++)
            ps[i] = ps[i-1] + (s[i] == '1');
        for(int i = 1; i <= m; i++)
            pt[i] = pt[i-1] + (t[i] == '1');
        dp[0][0] = 0;
        for(int i = 1; i <= n; i++)
        {
            dp[i][0] = dp[i-1][0];
            if(s[i] == '0')
                dp[i][0] += ps[i-1];
        }
        for(int j = 1; j <= m; j++)
        {
            dp[0][j] = dp[0][j-1];
            if(t[j] == '0')
                dp[0][j] += pt[j-1];
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= m; j++)
            {
                if(s[i] == '0')
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + ps[i-1] + pt[j]);
                else
                    dp[i][j] = min(dp[i][j], dp[i-1][j]);

                if(t[j] == '0')
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + ps[i] + pt[j-1]);
                else
                    dp[i][j] = min(dp[i][j], dp[i][j-1]);
            }
        }
        cout << dp[n][m] << endl;
    }
    assert(sumN <= 2000);
    readEOF();
    return 0;
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
auto isBinaryString=[&](const string s)->bool{
    for(auto x:s){
        if(x!='0'&&x!='1')
            return false;
    }
    return true;
};

lli sumN = 2e3;
T=readIntLn(1,1e3);
while(T--)
{

    const lli n=readIntLn(1,min(1000LL,sumN));
    sumN-=n;
    const string s=readStringLn(n,n);
    const string t=readStringLn(n,n);
    assert(isBinaryString(s));
    assert(isBinaryString(t));
    vi a(n+1),b(n+1);
    for(int i=0;i<n;++i){
        a[i+1]=a[i]+s[i]-'0';
        b[i+1]=b[i]+t[i]-'0';
    }
    vector<vi> dp(n+1,vi(n+1,-1));
    const lli ans=y_combinator([&](const auto &self,lli i,lli j)->lli{
        if(i<0||j<0)
            return INF;
        lli &ans=dp[i][j];
        if(ans!=-1)
            return ans;
        if(i==0&&j==0)
            return ans=0;
        ans=INF;
        const lli c=a[i]+b[j];
        if(s[i-1]=='0')
            ans=min(ans,c+self(i-1,j));
        else
            ans=min(ans,self(i-1,j));

        if(t[j-1]=='0')
            ans=min(ans,c+self(i,j-1));
        else
            ans=min(ans,self(i,j-1));

        return ans;
    })(n,n);
    cout<<ans<<endl;
}   aryanc403();
    readEOF();
    return 0;
}

``

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std ;
const int inf = 1000000000 ;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t ;
    cin >> t ;
    while(t--)
    {
        int n;
        cin >> n ;

        string a , b ;
        cin >> a >> b ;

        vector<int> cnt_a(n+1) , cnt_b(n+1) ;

        for(int i = n-1 ; i >= 0 ; i--)
        {
            cnt_a[i] = cnt_a[i+1] + (a[i] == '0') ;
            cnt_b[i] = cnt_b[i+1] + (b[i] == '0') ;
        }

        int dp[n+1][n+1] ;
        for(int i = 0 ; i <= n ; i++)
            for(int j = 0 ; j <= n ; j++)
                dp[i][j] = inf ;

        dp[n][n] = 0 ;

        for(int i = n ; i >= 0 ; i--)
        {
            for(int j = n ; j >= 0 ; j--)
            {
                if(i < n)
                {
                    if(a[i] == '0')
                        dp[i][j] = min(dp[i][j] , dp[i+1][j]) ;
                    else
                        dp[i][j] = min(dp[i][j] , dp[i+1][j] + cnt_a[i] + cnt_b[j]) ;
                }

                if(j < n)
                {
                    if(b[j] == '0')
                        dp[i][j] = min(dp[i][j] , dp[i][j+1]) ;
                    else
                        dp[i][j] = min(dp[i][j] , dp[i][j+1] + cnt_a[i] + cnt_b[j]) ;
                }
            }
        }

        cout << dp[0][0] << endl ;
    }

    return 0;
}
``

</details>
