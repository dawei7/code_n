# Minimum Operation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINIMUMOP |
| Difficulty Rating | 2170 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MINIMUMOP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MINIMUMOP) |

---

## Problem Statement

You are given positive integers $N$ and $M$ $(M \geq 2)$.
You are also given an array $A$ of size $N$, such that $2 \leq A_i \leq M$.

In one operation on the array, you can:
- Select an integer $X$ $(2 \leq X \leq M)$ and change $A_i$ to $\gcd(A_i,X)$ for **all** $1 \leq i \leq N$.
Note that $\gcd$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

Your task is to make all the elements of $A$ **equal**.
Find the **minimum** number of operations required to do so and also print the selected integer $X$ for each operation.
If there are multiple ways to do so, you may print any.

It can be proven that it is always possible to make all the elements of $A$ equal in finite number of operations.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two integers $N$ and $M$ — the length of the array $A$ and maximum value of $X$ allowed.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$,  representing the array $A$.

---

## Output Format

For each test case, in the first line, print an integer $Z$, denoting the number of operations required.

In case $Z\gt 0$, print another line with $Z$ space-separated integers where the $i^{th}$ integer represents the selected integer $X$ selected in the $i^{th}$ operation in **order**.

If there are multiple ways to do so, you may print any.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $2 \leq M \leq 10^6$
- $2 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.
- Note that sum of $M$ over all test case isn't bounded.

---

## Examples

**Example 1**

**Input**

```text
2
3 343
343 343 343
5 100
4 8 12 16 20
```

**Output**

```text
0
1
4
```

**Explanation**

**Test case $1$:** Since all elements of the array are already equal, we require $0$ operations.

**Test case $2$:** We require only one operation:
- Select $X = 4$: Thus, the array becomes $[\gcd(4, 4), \gcd(4, 8), \gcd(4, 12), \gcd(4, 16), \gcd(4, 20)] = [4, 4, 4, 4, 4]$, where all elements are equal.

Note that this is the minimum number of operations required.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINIMUMOP)

[Contest: Division 1](https://www.codechef.com/START86A/problems/MINIMUMOP)

[Contest: Division 2](https://www.codechef.com/START86B/problems/MINIMUMOP)

[Contest: Division 3](https://www.codechef.com/START86C/problems/MINIMUMOP)

[Contest: Division 4](https://www.codechef.com/START86D/problems/MINIMUMOP)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2170

#
[](#prerequisites-3)PREREQUISITES:

Fast prime factorization, [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)

#
[](#problem-4)PROBLEM:

You have an array A of length N, such that 2\leq A_i \leq M.

In one move, you can select an integer X and set A_i \gets \gcd(A_i, X) for every i.

Find the minimum number of moves needed to make all the array elements equal.

#
[](#explanation-5)EXPLANATION:

If all the A_i are already equal, the answer is 0. We need to solve for the case when they aren’t.

Notice that choosing X = 2 sets every A_i to either 1 or 2.

Choosing X = 3 after this sets everything to 1, since \gcd(1, 3) = \gcd(2, 3) = 1.

So, it’s always possible to make everything equal within two moves. All we need to check is whether everything can be made equal in 1.

Suppose we are able to do this, and make all the array elements equal to Y in the end.

There are two possibilities here: either Y = 1, or Y \gt 1.

Y = 1

We want to choose 2 \leq X \leq M such that \gcd(A_i, X) = 1 for *every* A_i.

In particular, this means that X cannot share a prime factor with any of the A_i; if it did, then the corresponding gcd wouldn’t be 1.

So, suppose we have a list of all the prime factors of all the A_i, say L.

We need to check if there’s an X between 2 and M that doesn’t have a prime factor in L.

Notice that it’s enough to restrict ourselves to the case when X is prime.

So, we simply need to check whether there’s any prime in the range [2, M] that isn’t in L.

If the primes upto M are precomputed (using a sieve), this is easy to do (given that you have L in hand, of course).

Finally, we also need to discuss how to compute the list L quickly, i.e, how to prime-factorize all the A_i quickly.

The constraints are low enough that directly factorizing each number in \mathcal{O}(\sqrt {A_i}) is probably fast enough, but there’s a faster way using the fact that A_i \leq 5\cdot 10^5.

In the initial sieve we do to find prime numbers, also store one prime divisor of each number, let’s call it \text{prm}[x] for x.

Then, to prime factorize A_i:

-
\text{prm}[A_i] is one prime factor.

- The next prime factor can be found by dividing \text{prm}[A_i] out of A_i and again looking at the \text{prm} array, i.e, looking at \text{prm}\left[\frac{A_i}{\text{prm}[A_i]}\right].

- Repeat this while A_i \gt 1.

Each division (at least) halves A_i, so this will take \log{A_i} steps.

This allows us to obtain all the prime factors of the A_i in \mathcal{O}(N\log M) time.

Putting everything together, the solution for this case looks as follows:

- Quickly prime factorize all the A_i, either using the method outlined above or otherwise.

Let L be the list of all prime factors of all the A_i.

- Then, for each prime p from 2 to M:

- If p is present in L, continue on. This can be checked quickly using, say, binary search.

- If p is *not* present in L, then performing one operation with p is valid, and you can **break out immediately**.

Note that as long as you break out immediately, this is fast enough even though there’s no constraint on the sum of M across all tests.

This is because the list L contains at most N\log M elements. So,

- If a valid prime is found, it’ll certainly be within N\log M + 1 steps at most, each taking one binary search. This is not a problem.

- If no valid prime is found, then N\log M must exceed the number of primes from 1 to M, which is approximately \frac{M}{\log M} by the [prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).

This roughly gives us a lower bound on N, something like N \geq \frac{M}{\log ^2 M}.

Since the sum of N across all cases is bounded, we’re fine.

Y > 1

Suppose we’re able to choose an X such that \gcd(A_i, X) = Y for every i, and Y \gt 1.

Notice that Y must be a factor of both X and A_i — in fact, Y must be a factor of *every* A_i.

This means Y must be factor of \gcd(A_1, A_2, \ldots, A_N), by definition of \gcd.

In particular, if \gcd(A_1, \ldots, A_N) = 1, then such a Y cannot exist.

On the other hand, if \gcd(A_1, \ldots, A_N) \gt 1, then simply choosing X = \gcd(A_1, \ldots, A_N) will also give us Y = \gcd(A_1, \ldots, A_N) \gt 1, and we’ll be done!

Check both cases above to see if using one move is possible.

If both cases fail, then the answer is 2, using X = 2 and X = 3 as discussed above.

As an aside, the technique of prime-factorizing numbers using a sieve is fairly common, and even appeared in [GCD_QUERIES](https://www.codechef.com/START85A/problems/GCD_QUERIES) from last week.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log^2 M) per test case with a sieve upto 10^6 as precomputation.

#
[](#code-7)CODE:

Setter's code (C++)
``#pragma GCC optimization("O3")
#pragma GCC optimization("Ofast,unroll-loops")

#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
const ll INF_MUL=1e13;
const ll INF_ADD=1e18;
#define pb push_back
#define mp make_pair
#define nline "\n"
#define f first
#define s second
#define pll pair<ll,ll>
#define all(x) x.begin(),x.end()
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define vvvl vector<vector<vector<ll>>>
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
void _print(ll x){cerr<<x;}
void _print(int x){cerr<<x;}
void _print(char x){cerr<<x;}
void _print(string x){cerr<<x;}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<class T,class V> void _print(pair<T,V> p) {cerr<<"{"; _print(p.first);cerr<<","; _print(p.second);cerr<<"}";}
template<class T>void _print(vector<T> v) {cerr<<" [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T>void _print(set<T> v) {cerr<<" [ "; for (T i:v){_print(i); cerr<<" ";}cerr<<"]";}
template<class T>void _print(multiset<T> v) {cerr<< " [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T,class V>void _print(map<T, V> v) {cerr<<" [ "; for(auto i:v) {_print(i);cerr<<" ";} cerr<<"]";}
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef tree<pair<ll,ll>, null_type, less<pair<ll,ll>>, rb_tree_tag, tree_order_statistics_node_update> ordered_pset;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const ll MOD=1e9+7;
const ll MAX=1000500;
vector<ll> freq(MAX,0);
vector<ll> prime(MAX,1);
vector<vector<ll>> track(MAX);
void solve(){
    ll n,m; cin>>n>>m;
    vector<ll> a(n);
    for(auto &it:a){
        cin>>it;
    }
    sort(all(a));
    if(a[0]==a[n-1]){
        cout<<0<<nline;
        return;
    }
    for(auto it:a){
        for(auto i:track[it]){
            freq[i]++;
        }
    }
    auto init=[&](){
        for(auto it:a){
            for(auto i:track[it]){
                freq[i]=0;
            }
        }
    };
    for(ll i=2;i<=m;i++){
        if(!prime[i]){
            continue;
        }
        if(freq[i]==0 or freq[i]==n){
            init();
            cout<<1<<nline<<i<<nline;
            return;
        }
    }
    init();
    cout<<2<<nline<<2<<" "<<3<<nline;
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=1;
    cin>>test_cases;
    prime[1]=0;
    for(ll i=2;i<MAX;i++){
        if(!prime[i]){
            continue;
        }
        for(ll j=i+i;j<MAX;j+=i){
            prime[j]=0;
            track[j].push_back(i);
        }
        track[i].push_back(i);
    }
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Tester's code (C++)
``//clear adj and visited vector declared globally after each test case
//check for long long overflow
//Mod wale question mein last mein if dalo ie. Ans<0 then ans+=mod;
//Incase of close mle change language to c++17 or c++14
//Check ans for n=1
#pragma GCC target ("avx2")
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
// #define int long long
#define IOS std::ios::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);cout.precision(dbl::max_digits10);
#define pb push_back
#define mod 1000000007ll //998244353ll
#define lld long double
#define mii map<int, int>
#define pii pair<int, int>
#define ll long long
#define ff first
#define ss second
#define all(x) (x).begin(), (x).end()
#define rep(i,x,y) for(int i=x; i<y; i++)
#define fill(a,b) memset(a, b, sizeof(a))
#define vi vector<int>
#define setbits(x) __builtin_popcountll(x)
#define print2d(dp,n,m) for(int i=0;i<=n;i++){for(int j=0;j<=m;j++)cout<<dp[i][j]<<" ";cout<<"\n";}
typedef std::numeric_limits< double > dbl;
using namespace __gnu_pbds;
using namespace std;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;
//member functions :
//1. order_of_key(k) : number of elements strictly lesser than k
//2. find_by_order(k) : k-th element in the set
const long long N=1000005, INF=2000000000000000000;
const int inf=2e9 + 5;
lld pi=3.1415926535897932;
int lcm(int a, int b)
{
    int g=__gcd(a, b);
    return a/g*b;
}
int power(int a, int b, int p)
    {
        if(a==0)
        return 0;
        int res=1;
        a%=p;
        while(b>0)
        {
            if(b&1)
            res=(1ll*res*a)%p;
            b>>=1;
            a=(1ll*a*a)%p;
        }
        return res;
    }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int getRand(int l, int r)
{
    uniform_int_distribution<int> uid(l, r);
    return uid(rng);
}
vi pfact[N];
int co[N];
int32_t main()
{
    IOS;
    for(int i=2;i<N;i++)
    {
        if(pfact[i].size()==0)
        {
            for(int j=i;j<N;j+=i)
            pfact[j].pb(i);
        }
    }
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        cin>>n>>m;
        int a[n];
        rep(i,0,n)
        cin>>a[i];
        sort(a, a+n);
        if(a[0]==a[n-1])
        {
            cout<<0<<"\n";
            continue;
        }
        rep(i,0,n)
        {
            for(auto p:pfact[a[i]])
            co[p]++;
        }
        int f=0;
        rep(i,2,m+1)
        {
            if(pfact[i][0]!=i)
            continue;
            if(co[i]==0 || co[i]==n)
            {
                f=i;
                break;
            }
        }
        rep(i,0,n)
        {
            for(auto p:pfact[a[i]])
            co[p]=0;
        }
        if(f)
        cout<<1<<"\n"<<f<<'\n';
        else
        cout<<2<<"\n"<<m<<" "<<m-1<<"\n";
    }
}
``

Editorialist's code (Python)
``mx = 10**6 + 314
prm = [0]*mx
for i in range(2, mx):
    if prm[i] > 0: continue
    for j in range(i, mx, i): prm[j] = i

from math import gcd
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if min(a) == max(a):
        print(0)
        continue

    ans = -1
    g = a[0]
    primes = set()
    for x in a:
        g = gcd(x, g)
        while x > 1:
            primes.add(prm[x])
            x //= prm[x]
    if g > 1: ans = g

    for x in range(1, m+1):
        if prm[x] < x: continue
        if x not in primes:
            ans = x
            break

    if ans == -1: print(2, '\n', 2, ' ', 3, sep = '')
    else: print(1, '\n', ans, sep = '')
``

</details>
