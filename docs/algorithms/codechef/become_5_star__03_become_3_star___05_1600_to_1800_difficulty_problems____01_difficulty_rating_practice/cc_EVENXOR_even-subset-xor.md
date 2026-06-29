# Even Subset Xor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVENXOR |
| Difficulty Rating | 1714 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [EVENXOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/EVENXOR) |

---

## Problem Statement

A number $X$ is called *bad* if its binary representation contains odd number of $1$ bits. For example, $X = 13 = (1101)_2$ is bad while $X = 3 = (11)_2$ is not bad.

Chef calls an array $A$ of length $N$ **special** if the following conditions hold:
- For each $1 \le i \le N$, $0 \le A_i \lt 2^{20}$
- All the elements of $A$ are **distinct**
- There does not exist any non-empty [subset](https://en.wikipedia.org/wiki/Subset) of $A$ such that the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of the subset is bad.

For example,
- $A = [2, 3, 4]$ is not **special** because the XOR of the subset $[2, 3]$ is $2 \oplus 3 = 1$, which is *bad*. ($\oplus$ denotes the bitwise XOR operation)
- $A = [3, 3]$ is not special because its elements are not distinct.
- $A = [3, 5]$ is special because it satisfies all the conditions.

Chef challenges you to construct **any** special array of length $N$. Can you complete Chef's challenge?

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$ — the length of the special array to be constructed.

---

## Output Format

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of the special array of length $N$ you constructed.

**Note:** It can be proved that a special array of length $N$ always exists under the given constraints.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $0 \leq A_i \lt 2^{20}$

---

## Examples

**Example 1**

**Input**

```text
2
1
2
```

**Output**

```text
6
3 5
```

**Explanation**

**Test Case $1$:** There is only one non-empty subset of the given array, namely $[6]$. The XOR of this subset is $6 = (110)_2$, which is not bad.

**Test Case $2$:** The given array has three non-empty subsets, namely $[3], [5]$, and $[3, 5]$.
- $[3]$ has XOR $3 = (11)_2$, which is not bad.
- $[5]$ has XOR $5 = (101)_2$, which is not bad.
- $[3, 5]$ has XOR $6 = (110)_2$, which is not bad.

None of the subsets have bad XOR, and the elements are distinct. Hence, the array is special.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
3 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START22A/problems/EVENXOR)

[Contest Division 2](https://www.codechef.com/START22B/problems/EVENXOR)

[Contest Division 3](https://www.codechef.com/START22C/problems/EVENXOR)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

[Bitwise Xor](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)

#
[](#problem-4)PROBLEM:

A number X is called *bad* if its binary representation contains odd number of 1 bits. For example, X = 13 = (1101)_2 is bad while X = 3 = (11)_2 is not bad.

Chef calls an array A of length N **special** if the following conditions hold:

- For each 1 \le i \le N, 0 \le A_i \lt 2^{20}

- All the elements of A are **distinct**

- There does not exist any non-empty [subset](https://en.wikipedia.org/wiki/Subset) of A such that the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of the subset is bad.

For example,

-
A = [2, 3, 4] is not **special** because the XOR of the subset [2, 3] is 2 \oplus 3 = 1, which is *bad*. (\oplus denotes the bitwise XOR operation)

-
A = [3, 3] is not special because its elements are not distinct.

-
A = [3, 5] is special because it satisfies all the conditions.

Chef challenges you to construct **any** special array of length N. Can you complete Chef’s challenge?

#
[](#hints-5)Hints:

A number X is called *bad* if its binary representation contains odd number of 1 bits.

Let the number X be called *good* if its binary representation contains even number of 1 bits.

Hint 1

When we take `XOR` of two bits, the total number of 1 bits either remains same, or decreases by 2.

Hint 2

When we take `XOR` of two numbers, the total number of 1 bits changes by even number.

Hint 3

When we take `XOR` of set numbers, the total number of 1 bits changes by even number.

Hint 4

Consider any set of *good* numbers. The `XOR` of the subset will also be a *good* number.

#
[](#explanation-6)EXPLANATION:

Let us use the defined terminology of *good* and *bad* elements.

Our aim is to construct a **special** array of length N. In other words, we want to create an array of length N containing **distinct** elements, such that there doesn’t exist any non-empty subset such that the bitwise XOR of the subset is bad.

**Approach 1**

Let us first analyze, what happens when we take XOR of two numbers.

Taking XOR of two 1-bit numbers

We have 4 possible cases:

- 0 \oplus 0  = 0

- 0 \oplus 1  = 1

- 1 \oplus 0  = 1

- 1 \oplus 1  = 0

An important point to note is, the total number of 1-bits remain same in the first 3 cases, and decreases by 2 in the last case.

Taking XOR of two numbers

We have seen that when we take XOR of two bits, the total number of 1-bits either remains same, or decreases by 2. In other words, the total number of 1-bits changes by even number.

When we take XOR of two K-bit numbers, we can consider the operation as taking XOR of two 1-bit numbers K times. And therefore, we can extend the above argument and say that the total number of 1-bits changes by even number.

Taking XOR of set of numbers

Let the set S = \{ S_1 , S_2 , \cdots , S_K\}.

The XOR of the set S is defined as (((S_1 \oplus S_2) \oplus S_3) \oplus \cdots \oplus S_K)

In other words, it is K-1 successive XORs. We can again extend the same argument as above, and say that when we take XOR of set of numbers, the total number of 1-bits changes by even number.

After making the above observations, let us shift our focus to the subsets.

Each individual element of the array is a valid subset. Let us focus on the subset \{A_i\}.

The XOR of this subset is A_i, and therefore A_i should have even number of 1-bits.

This holds for all i : 1 \leq i \leq N.

Once we have the above property in the array, by using the observation 3 (Taking XOR of set of numbers), we can claim that XOR of any subset is *good* because the total number of 1-bits in the subset is even (sum of even numbers is even), and after taking XOR, the number of 1-bits changes by even number. Hence, the resulting XOR has even number of set bits.

Finally, we need a  list of 1000 *good* numbers. To get the list of *good* numbers, we can start iterating from 0, and check if the number is *good* or not by counting number of set bits.

Can you prove that there are 2^{10} *good* numbers which are less than 2^{11}?

**Approach 2**

As we have seen in the first approach, each individual element of the array is a valid subset. Let us focus on the subset \{A_i\}. The XOR of this subset is A_i, and therefore A_i should have even number of 1-bits.

This holds for all i : 1 \leq i \leq N.

We also have to follow the constraint that A_i < 2^{20}. In other words, A_i can be a 20-bit number.

Let us divide these 20-bits in two halves, first 10-bits, and last 10-bits.

Now, consider the numbers where first half is exactly same as the second half. Let’s call such numbers as *special numbers*. So for example, `1000010000-1000010000` is a *special number*.

Total count of *special numbers*

Let us fill the first 10 bits. Total number of ways to fill them  = 2^{10} = 1024.

Now, we can replicate these first 10 bits in the last 10 bits.

Hence, total count of *special numbers* = 1024

Parity of number of set-bits in a *special number*

Because the first 10-bits are exactly replicated as the last 10-bits, we can claim that the number of set-bits will always be even.

XOR of two *special numbers*

Consider two *special numbers* A and B. Let A \oplus B = C.

Analyze first 10-bits and last 10-bits of C. They are exactly same!! (Why?)

And therefore, C is a *special number*, and has even number of set bits.

Note that any *special number* can be simply written as (i\cdot 2^{10} + i)  where 0 \leq i < 2^{10}.

The above three statements tells us that if each A_i is a **distinct** *special number*, all the three conditions are satisfied, and we have solved our problem!!

#
[](#time-complexity-7)TIME COMPLEXITY:

We can first create the list of 1000 good numbers by iterating from 0 till 2^{11}.

Then for each test case, we can print first N numbers from the list. Hence time complexity is O(N) per testcase.

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

const int N = 1e3 + 5;

vector<int> ans;

int32_t main()
{
    IOS;
    for(int i = 0; sz(ans) < N; i++)
    {
        if(__builtin_popcountll(i) % 2 == 0)
            ans.push_back(i);
    }
    int T; cin >> T;
    while(T--)
    {
        int n; cin >> n;
        for(int i = 0; i < n; i++)
            cout << ans[i] << " ";
        cout << endl;
    }
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
#define bcnt(x) (__builtin_popcount(x))
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
const lli maxN = 1e3;
vi a;
for(lli i=0;sz(a)<maxN;++i){
    if(bcnt(i)&1)
        continue;
    a.pb(i);
}
T=readIntLn(1,1e2);
while(T--)
{

    n=readIntLn(1,1e3);
    for(int i=0;i<n;++i)
        cout<<a[i]<<" \n"[i+1==n];
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
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t ;
    cin >> t ;

    int arr[1000] ;
    int ind = 0 , val = 0 ;

    while(ind < 1000)
    {
        int curr_set_bits = __builtin_popcount(val) ;

        if(curr_set_bits%2 == 0)
        {
            arr[ind] = val ;
            ind++ ;
        }
        val++ ;
    }

    while(t--)
    {
        int n ;
        cin >> n ;
        for(int i = 0 ; i < n ; i++)
        {
            cout << arr[i] << ' ';
        }
        cout << '\n' ;
    }

    return 0;
}
``

</details>
