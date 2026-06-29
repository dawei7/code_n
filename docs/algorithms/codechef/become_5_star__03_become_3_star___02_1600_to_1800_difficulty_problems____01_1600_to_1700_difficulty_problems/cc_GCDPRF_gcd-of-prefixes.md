# GCD of Prefixes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDPRF |
| Difficulty Rating | 1617 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [GCDPRF](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/GCDPRF) |

---

## Problem Statement

Sasuke and Itachi are playing a game. Sasuke first creates an array $A$ containing $N$ positive integers $A_1, A_2, \dots, A_N$. He then creates a new array $B$ of length $N$ such that $B_i = \gcd(A_1, A_2, ..., A_i)$ for each $1 \leq i \leq N$. Now, Sasuke gives array $B$ to Itachi and asks him to find any array $A$ (with $1\leq A_i\leq 10^9$) such that the given process applied to $A$ will produce $B$. Can you help Itachi solve this problem?

Here, $\gcd$ stands for [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $B_1, B_2, \dots, B_N$

---

## Output Format

For each test case, print a single line containing $N$ space-separated integers denoting the array $A$ you constructed. If no such array $A$ exists, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- It is guaranteed that sum of $N$ over all test cases doesn't exceed $5 \times 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
4 2
2
1 3
```

**Output**

```text
4 26
-1
```

**Explanation**

**Test Case 1:** One possible answer is $[4, 26]$ because $B$ can be generated as follows: $B = [\gcd(4), \gcd(4, 26)] = [4, 2]$.

**Test Case 2:** It can be shown that no array $A$ exists which can produce the given $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
4 2
```

**Output for this case**

```text
4 26
```



#### Test case 2

**Input for this case**

```text
2
1 3
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START17A/problems/GCDPRF)

[Contest Division 2](https://www.codechef.com/START17B/problems/GCDPRF)

[Contest Division 3](https://www.codechef.com/START17C/problems/GCDPRF)

[Practice](https://www.codechef.com/problems/GCDPRF)

**Setter:** [Deep Raval](https://www.codechef.com/users/deep2905)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Basic Math

#
[](#problem-4)PROBLEM

Sasuke and Itachi are playing a game. Sasuke first creates an array A containing N positive integers A_1, A_2, \dots, A_N. He then creates a new array B of length N such that B_i = \gcd(A_1, A_2, ..., A_i) for each 1 \leq i \leq N. Now, Sasuke gives array B to Itachi and asks him to find any array A (with 1\leq A_i\leq 10^9) such that the given process applied to A will produce B. Can you help Itachi solve this problem?

Here, \gcd stands for [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

#
[](#quick-explanation-5)QUICK EXPLANATION

If the given array B is a valid candidate for A, then print B. Otherwise, no such A exists.

#
[](#explanation-6)EXPLANATION

###
[](#checking-if-some-a-exists-7)Checking if some A exists

We know that B_i = gcd(A_1, A_2, ..., A_i) and B_{i+1} = gcd(A_1, A_2, ..., A_i, A_{i+1}) = gcd(gcd(A_1, A_2, ..., A_i), A_{i+1}) = gcd(B_i, A_{i+1})

This way, we can write B_{i+1} = gcd(B_i, A_{i+1}).

What just happened?

gcd(x, y, z) = gcd(gcd(x, y), z) = gcd(x, gcd(y, z)) holds for all valid x, y, z. So we decided to compute gcd of first i terms, and then take gcd with A_{i+1}. Since gcd of first i terms is B_i, we can write B_{i+1} = gcd(B_i, A_{i+1})

The implication of this is that B_{i+1} must be a factor of B_i, Since gcd of two numbers is divisor of both numbers. Hence, condition B_{i+1} divides B_i should hold for all 1 \leq i \lt N.

So if the given array has any such i where B_{i+1} doesn’t divide B_i, no such A can exist.

###
[](#finding-a-8)Finding A

The given array B is a valid candidate for A. We’d end up with something like  B_{i+1} = gcd(B_{i}, A_{i+1}), but we have A_{i+1} = B_{i+1}. Since B_{i+1} divide B_i, gcd(B_i, B_{i+1}) = B_{i+1}

So the given array B satisfies our condition and can be printed as array A.

#
[](#time-complexity-9)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-10)SOLUTIONS

Setter's Solution
``/**
 * Author : RDP
 * There are no two words in the English language more harmful than "good job".
 * 1729 ;)
**/
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

/********** Definations, Macros and Debug Stuff  **********/
void debug_out() { cerr << '\n'; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T)
{
    cerr << " " << to_string(H);
    debug_out(T...);
}

#define endl '\n'
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]: ", debug_out(__VA_ARGS__)
#define FAST_IO                  \
    ios::sync_with_stdio(false); \
    std::cin.tie(NULL);          \
    std::cout.tie(NULL);
#define all(x) (x).begin(), (x).end()
const long double EPS = 5e-8;
#define PI 3.1415926535897932384626433832795
const ll MOD = 1000000007;
/**********************************************************/
/**************** Frequently used functions ***************/
template <typename T>
inline void print_vector(const vector<T> &a)
{
    for (auto &x : a)
        cout << x << ' ';
    cout << endl;
}
inline ll binary_pow(ll a, ll b)
{
    ll res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
inline ll mod_pow(ll x, ll y, ll m = MOD)
{
    ll res = 1;
    x = x % m;
    if (x == 0)
        return 0;
    while (y > 0)
    {
        if (y & 1)
            res = (res * x) % m;
        y = y >> 1;
        x = (x * x) % m;
    }
    return res;
}
inline ll mod_add(ll a, ll b, ll m = MOD)
{
    a = a % m;
    b = b % m;
    return (((a + b) % m) + m) % m;
}
inline ll mod_mul(ll a, ll b, ll m = MOD)
{
    a = a % m;
    b = b % m;
    return (((a * b) % m) + m) % m;
}
inline ll mod_sub(ll a, ll b, ll m = MOD)
{
    a = a % m;
    b = b % m;
    return (((a - b) % m) + m) % m;
}
inline ll mminvprime(ll a, ll b)
{
    return mod_pow(a, b - 2, b);
}
inline ll mod_div(ll a, ll b, ll m = MOD)
{
    a = a % m;
    b = b % m;
    return (mod_mul(a, mminvprime(b, m), m) + m) % m;
}
inline ll ceilf(ll x, ll y)
{
    return x % y == 0 ? x / y : x / y + 1;
}
// Use this for randomizing things
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
/**********************************************************/

void test_case()
{
    int n;
    cin >> n;
    vector<ll> a(n);
    for (auto &x : a)
        cin >> x;
    ll cur_gcd = a[0];
    for (int i = 1; i < n; i++)
    {
        cur_gcd = __gcd(cur_gcd, a[i]);
        if (cur_gcd != a[i])
        {
            cout << -1 << endl;
            return;
        }
    }
    print_vector(a);
}

int main()
{
    FAST_IO
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        test_case();
    }
    return 0;
}
/*
Some things to remember when you're stuck:
    1. Check for edge cases.
    2. Stay Calm.
    3. Don't be stupid (search for silly mistakes).
    4. Read problem again. Approach solution from different point of view.
    5. In case of modulo, check for negative result (add MOD).

Some common C++ pit falls:
    1. Don't use inbuilt ceil.
    2. Never take inputs as double unless it is necessary.
    3. Don't pass INT in accumulate.
*/
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
lli sumN = 5e5;
while(T--)
{

    const int n=readIntLn(1,min(sumN,100000LL));
    sumN-=n;
    const auto a=readVectorInt(n,1,1e9);
    bool fl=true;
    for(int i=1;i<n;++i){
        if(__gcd(a[i],a[i-1])!=a[i]){
            fl=false;
            break;
        }
    }
    if(!fl){
        cout<<-1<<endl;
        continue;
    }
    for(auto x:a)
        cout<<x<<" ";
    cout<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class GCDPRF{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int[] B = new int[N];
        for(int i = 0; i< N; i++)B[i] = ni();
        boolean yes = true;
        for(int i = 1; i< N; i++)yes &= B[i-1]%B[i] == 0;
        if(yes){
            for(int x:B)p(x+" ");pn("");
        }else pn(-1);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new GCDPRF().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
