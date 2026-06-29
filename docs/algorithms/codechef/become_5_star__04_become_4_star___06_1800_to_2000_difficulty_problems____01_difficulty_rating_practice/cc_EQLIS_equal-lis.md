# Equal LIS

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQLIS |
| Difficulty Rating | 1848 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [EQLIS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/EQLIS) |

---

## Problem Statement

For a permutation $P$ of length $N$, we define $L(P)$ to be the length of the longest increasing subsequence in $P$. That is, $L(P)$ is the largest integer $K$ such that there exist indices $i_1 \lt i_2 \lt \ldots \lt i_K$ such that $P_{i_1} \lt P_{i_2} \lt \ldots \lt P_{i_K}$.

Define $P^R$ to be the permutation $(P_N, P_{N-1}, \ldots, P_1)$.

You are given a positive integer $N$. You need to output a permutation $P$ of length $N$ such that $L(P) = L(P^R)$, or say that none exist.

**Note:** $P$ is said to be a permutation of length $N$ if $P$ is a sequence of length $N$ consisting of $N$ **distinct** integers between $1$ and $N$. For example, $(3, 1, 2)$ is a permutation of length $3$, but $(1, 4, 2)$, $(2, 2, 3)$ and $(2, 1)$ are not.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing one integer $N$ — the length of the permutation to be constructed.

---

## Output Format

For each test case, output on a new line `"YES"` if there exists a valid permutation, and `"NO"` if there doesn't. If you outputted `"YES"`, on the next line, output a valid permutation $P$ as $N$ space-separated integers, the $i^{th}$ of which is $P_i$.

You can print each letter of the string in any case (upper or lower) (for instance, strings `YES`, `yEs`, and `yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 2 \cdot 10^5$
- The sum of $N$ across all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
2
3
```

**Output**

```text
NO
YES
1 3 2
```

**Explanation**

**Test Case $1$:** There are two permutations of length $2$ — $(1, 2)$ and $(2, 1)$. The length of the LIS of $(1, 2)$ is $2$ and the length of the LIS of $(2, 1)$ is $1$. Since these permutations are reverses of each other and have unequal LIS lengths, there is no valid permutation of length $2$.

**Test Case $2$:** The length of the LIS of $(1, 3, 2)$ is $2$, and the length of the LIS of its reverse, $(2, 3, 1)$, is also $2$. Therefore, this is a valid permutation of length $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START22A/problems/EQLIS)

[Contest Division 2](https://www.codechef.com/START22B/problems/EQLIS)

[Contest Division 3](https://www.codechef.com/START22C/problems/EQLIS)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

Tester: [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

[Longest Increasing Subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)

You do not need to know the algorithm of computing LIS, just a familiarity with the definition of LIS is sufficient.

#
[](#problem-4)PROBLEM:

For a permutation P of length N, we define L(P) to be the length of the longest increasing subsequence in P. That is, L(P) is the largest integer K such that there exist indices i_1 \lt i_2 \lt \ldots \lt i_K such that P_{i_1} \lt P_{i_2} \lt \ldots \lt P_{i_K}.

Define P^R to be the permutation (P_N, P_{N-1}, \ldots, P_1).

You are given a positive integer N. You need to output a permutation P of length N such that L(P) = L(P^R), or say that none exist.

**Note:** P is said to be a permutation of length N if P is a sequence of length N consisting of N **distinct** integers between 1 and N. For example, (3, 1, 2) is a permutation of length 3, but (1, 4, 2), (2, 2, 3) and (2, 1) are not.

#
[](#hints-5)HINTS:

- In constructive problems, it usually helps to try figuring out the answers for lower values of N using pen and paper. It usually leads to a good number of observations, and helps in constructing the answer for the larger N.

- In the constructive problems involving LIS, thinking in the following two directions can be sometimes useful: Constructing sequence which is first increasing and then decreasing (or vice-versa). Or breaking down the sequence in blocks, and choosing and arranging elements in block such that you can only take a single (or some fixed number of) element/s from each block.

Coming back to the problem, the following hints might be useful:

Hint 1

The answer is “NO” only for N= 2. For all other values of N, a valid permutation exists.

Hint 2

Try to find out the answer for N = 4, 5 on pen and paper.

Hint 3

For N = 4, the valid permutations are: \{2, 4, 1, 3\} and \{2 , 1 , 4 , 3\}

For N = 5, one of the valid permutations are: \{1, 2, 5, 4, 3\}

Hint 4

The answer for odd values of N is: First have an increasing sequence from 1 till \left \lfloor{\frac{N}{2}}\right \rfloor, and then have a decreasing sequence from N till \left \lceil{\frac{N}{2}}\right \rceil.

Hint 5

Try constructing answer for even values of N using the construction for odd values of N. There can be several possible solutions. One such solution is:

First have an increasing sequence from 2 till \frac{N}{2}, then have 1 and then have a decreasing sequence from N till \frac{N}{2} + 1.

So, for N = 6, the answer will be 2 , 3 , 1 , 6 , 5 , 4.

#
[](#explanation-6)EXPLANATION:

After trying to find the permutation for N = 5 while thinking in the general directions as mentioned in the Hints section, we can figure out that the answer for odd values of N (present in Hint 4).

There is actually no algorithm of finding out the construction, you just need to play a little bit with some random permutations, and keep using the observations made in the process.

**When N is even**

At first, it looks like the answer will be “NO” for even values of N. However, on trying all the possible permutations for N = 4, you will see that the following two permutations are valid: \{2, 4, 1, 3\} and \{2 , 1 , 4 , 3\}

You can try to expand the solution for N = 4 to higher values, and observe the pattern.

**An Incorrect way?**

After seeing the permutation \{2 , 1 , 4 , 3\}, and going by the general direction of breaking sequence in blocks, it initially looks motivating to break the sequence in blocks of 2 and try to proceed further. On further pursuing, you might see some patterns, but they seemed little complicated. Do let us all know in the comment box if you have got some pattern

**One possible way**

Because we have a solution for odd values, it looks motivating to get use the answer for N-1 and extend it to N.

One way to do this is to observe that we create Increasing Subsequences at the beginning of the permutation. If we insert 1 in the middle, it will not affect the LIS.

The same argument holds when we look at the reverse of the permutation. This motivates us to create answer for [2 \cdots N] using Hint 4, and then insert 1 in the middle. This leads to the following construction:

First have an increasing sequence from 2 till \frac{N}{2}, then have 1 and then have a decreasing sequence from N till \frac{N}{2} + 1.

#
[](#time-complexity-7)TIME COMPLEXITY:

For each Test-Case, it will take O(N) time.

#
[](#solution-8)SOLUTION:

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
T=readIntLn(1,1e3);
lli sumN = 2e5;
while(T--)
{

    n=readIntLn(1,sumN);
    sumN-=n;
    dbg(n);
    if(n==2){
        cout<<"NO"<<endl;
        continue;
    }
    cout<<"YES"<<endl;
    lli bk=1;
    while(bk*bk<n)
        bk++;
    vector<vi> b(bk);
    lli cnt=0;
    for(lli i=0;i<bk;++i){
        cnt++;
        b[i].pb(i*bk);
    }

    for(lli i=0;i<bk&&cnt<n;++i)
        for(lli j=1;j<bk&&cnt<n;++j){
            cnt++;
            b[i].pb(i*bk+j);
        }
    vi a;
    for(auto &v:b){
        sort(all(v));
        reverse(all(v));
        a.insert(a.end(),all(v));
    }
    vi c=a;
    sort(all(c));
    (c).erase(unique(all(c)),(c).end());
    for(auto x:a){
        x=lower_bound(all(c),x)-c.begin();
        cout<<x+1<<" ";
    }
    cout<<endl;
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
    while(t--)
    {
        int n;
        cin >> n ;

        if(n == 2)
        {
            cout << "NO\n" ;
            continue ;
        }

        cout << "YES\n" ;
        if(n%2 == 1)
        {
            int val = n/2 ;
            for(int i = 1 ; i <= val ; i++)
                cout << i << ' ' ;
            for(int i = n ; i > val ; i--)
                cout << i << ' ';
            cout << '\n' ;
        }
        else
        {
            int val = (n/2);

            for(int i = 2 ; i <= val ; i++)
                cout << i << ' ';
            cout << 1 << ' ';
            for(int i = n ; i > val ; i--)
                cout << i << ' ';
            cout << '\n' ;
        }
    }

    return 0;
}
``

</details>
