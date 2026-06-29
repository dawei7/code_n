# Expected Value

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXPVALUE |
| Difficulty Rating | 2177 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [EXPVALUE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/EXPVALUE) |

---

## Problem Statement

Stack has a positive integer $P(P > 1)$.
He starts a game where his initial score is $0$.

In the $i^{th}$ turn, with a probability of $\frac{1}{2}$, Stack adds $\frac{1}{P^{i-1}}$ to his score.

Stack stops after $N$ turns.

Let $S_i$ be his score after $i$ turns and $F(i)$ denote the [expected value](https://en.wikipedia.org/wiki/Expected_value) of $S_i^2$.

For each integer $i(1 \leq i \leq N)$, find the value of $F(i)$ modulo $998244353$.

---

## Input Format

The only line of input contains two space-separated positive integers $N$ and $P$, as mentioned in the statement.

---

## Output Format

Print $N$ space-separated integers. For each integer $i(1 \leq i \leq N)$, output the value of $F(i)$ modulo $998244353$.

Formally, let $M=998244353$. It can be shown that the answer can be expressed as an irreducible fraction $\frac{x}{y}$, where $x$ and $y$ are integers and $y \not \equiv 0 \pmod{M}$.
Output the integer equal to $x \cdot y^{-1} \bmod M $.
In other words, output such an integer $z$ that $0 \leq z < M$ and $z \cdot y \equiv x \pmod{M}$.
.

---

## Constraints

- $1 \leq N \leq 3 \cdot 10^5$
- $2 \leq P \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
2 2
```

**Output**

```text
499122177 124780545
```

**Explanation**

$S_1$ can be $0$ or $1$ with equal probability.
Thus $F(1)=\frac{0 \cdot 0}{2}+\frac{1 \cdot 1}{2} = \frac{1}{2}$.

$F(2)=\frac{7}{8}$.

**Example 2**

**Input**

```text
10 343
```

**Output**

```text
499122177 379526990 822885144 761122022 256959043 151932103 340445396 758502677 478338987 125853909
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXPVALUE)

[Contest: Division 1](https://www.codechef.com/START76A/problems/EXPVALUE)

[Contest: Division 2](https://www.codechef.com/START76B/problems/EXPVALUE)

[Contest: Division 3](https://www.codechef.com/START76C/problems/EXPVALUE)

[Contest: Division 4](https://www.codechef.com/START76D/problems/EXPVALUE)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Linearity of expectation

#
[](#problem-4)PROBLEM:

Given N and p, consider the following N-step process:

- Initialize your score S to 0.

- In the i-th step, with probability 50\%, add p^{1-i}  to S

Let S_i denote your score after i steps.

Find \mathrm{E}[S_i^2] for each 1 \leq i \leq N.

#
[](#explanation-5)EXPLANATION:

Let’s first solve this for a fixed k, i.e, compute \mathrm{E}[S_k^2].

We have the set \{1, p^{-1}, p^{-2}, \ldots, p^{1-k}\}. We choose a random subset of this set (each with probability 2^{-k} of being chosen), and we want to find the expected value of the square of the sum of this subset.

Suppose the subset we choose is \{x_1, x_2, \ldots, x_m\}.

The square of its sum is (x_1 + x_2 + \ldots + x_m)^2, which when expanded is

\sum_{i=1}^m x_i^2 + \sum_{i=1}^m \sum_{j=i+1}^m 2x_ix_j

Let’s call the first summation X and the second one Y.

That is, X = \sum_{i=1}^m x_i^2 and Y = \sum_{i=1}^m \sum_{j=i+1}^m 2x_ix_j.

By linearity of expectation, \mathrm{E}[S_k^2] = \mathrm{E}[X] + \mathrm{E}[Y], so let’s compute each one individually.

Computing E(X)

\mathrm{E}[X] is simply the expected sum of squares of the subset.

Once again, let’s use linearity of expectation: each element of the set has a 50\% chance to be in our subset, so the expected value of the sum of squares is

0.5 \cdot \left(1^2 + \left(p^{-1}\right)^2 + \left(p^{-2}\right)^2 + \ldots + \left(p^{1-k}\right)^2\right)

Notice that this is the sum of k terms of a geometric series, with first term 1 and common ratio p^{-2}.

This sum can thus be computed in \mathcal{O}(\log{MOD}) using the [sum of GP formula](https://brilliant.org/wiki/geometric-progressions/#sums-of-geometric-progressions).

Alternately, you can just maintain the sum of squares as you iterate k, each time increasing it by p^{2-2k}.

Computing E(Y)

For the third this this problem, let’s use linearity of expectation.

For each 0 \leq i\lt j \lt k, the product 2p^{-i}p^{-j} has a 25\% chance of occurring in our score (we need to pick both p^{-i} and p^{-j}, 50\% chance of each).

So, the required expected value is

0.25 \sum_{i=0}^{k-1} \sum_{j=i+1}^{k-1} 2p^{-i-j}

For a fixed i, notice that the inner summation is once again a geometric progression with first term p^{-2i-1} and common ratio p^{-1}, so it can be computed in \mathcal{O}(\log{MOD}) .

This already gives us a way to compute \mathrm{E}[Y] in \mathcal{O}(k\log{MOD}); however, doing this separately for each k is too slow.

One way to speed it up is to flip the order of summations, and look at \displaystyle \sum_{j=0}^{k-1} \sum_{i=0}^{j-1} 2p^{-i-j} instead.

Once again, for a fixed j the inner summation is a GP and can be computed quickly.

However, the nice thing about looking at it this way is that when moving from k to k+1, almost all the computations are the same!

In fact, we only need to add in the summation for one more value of j.

This allows us to move from k to k+1 in \mathcal{O}(\log{MOD}) time, since we compute only one sum of GP at each step; hence making the overall complexity \mathcal{O}(N\log {MOD}).

Even simpler, you can notice that this sum of products increases by p^{1-k} times the sum of all the powers before, so maintaining the sum so far allows this to be updated in \mathcal{O}(1) without dealing with geometric progressions.

There are also other ways to compute this part quickly: for example, the closed-form formula

\frac{ (p^{k-1} - 1) (p^{k}-1)p^{1 - 2(k-1)}}{(p+1)(p-1)^2}

Either way, \mathrm{E}[X] and \mathrm{E}[Y] can be computed in \mathcal{O}(\log{MOD}) for a fixed k, so do it separately for each k, add them up, and we’re done.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log {MOD}) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``//#pragma GCC target ("avx2")
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")

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
const ll MOD=998244353;
const ll MAX=200200;
ll binpow(ll a,ll b,ll MOD){
    ll ans=1;
    a%=MOD;
    while(b){
        if(b&1)
            ans=(ans*a)%MOD;
        b/=2;
        a=(a*a)%MOD;
    }
    return ans;
}
ll inverse(ll a,ll MOD){
    return binpow(a,MOD-2,MOD);
}
ll getv(ll p,ll n){
    ll num=binpow(p,n,MOD)-1+MOD;
    ll den=inverse(p+MOD-1,MOD);
    num=(num*den)%MOD;
    return num;
}
void solve(){
    ll n,p; cin>>n>>p;
    p=inverse(p,MOD);
    for(ll i=1;i<=n;i++){
        ll ans=(getv(p,i)*getv(p,i)+getv(p*p,i))%MOD;
        ans=(ans*inverse(4,MOD))%MOD;
        cout<<ans<<" \n"[i==n];
    }
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
    //cin>>test_cases;
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
#define int long long
using namespace std;
const int mod=998244353;

int power(int a, int b, int p) {
    if(a==0)
    return 0;
    int res=1;
    a%=p;
    while(b>0) {
        if(b&1)
        res=(1ll*res*a)%p;
        b>>=1;
        a=(1ll*a*a)%p;
    }
    return res;
}

int32_t main() {
    int n, p;
    cin>>n>>p;
    assert(n>=1 && n<=300000 && p>=2 && p<=100000);
    int exp_sq=0, exp_sum=0, exp_prod=0, inv2=power(2, mod-2, mod);
    for(int i=0;i<n;i++) {
        int cur=power(power(p, i, mod), mod-2, mod);
        exp_sq=(exp_sq + (cur*cur))%mod;
        exp_prod=(exp_prod + (cur*exp_sum))%mod;
        exp_sum=(exp_sum + cur)%mod;
        int ans=((exp_sq + exp_prod)*inv2)%mod;
        cout<<ans<<" ";
    }
}
``

Editorialist's code (Python)
``def pw(a, n, mod):
	n %= mod-1
	r = 1
	while n > 0:
		if n%2 == 1: r = (r * a)%mod
		a = (a * a)%mod
		n //= 2
	return r

mod = 998244353
def gp_sum(a, r, n):
	ret = (pw(r, n, mod) - 1) * pw(r-1, mod-2, mod)
	return (a * ret) % mod
def what(p, n):
	ret = pw(p, 1 - 2*n, mod) * (pw(p, n, mod) - 1) * (pw(p, n+1, mod) - 1)
	ret %= mod
	ret *= pw((p - 1)**2, mod-2, mod)
	ret *= pw(p+1, mod-2, mod)
	return ret%mod;

n, p = map(int, input().split())
half = (mod+1)//2
r = pow(p*p, mod-2, mod)
for i in range(1, n+1):
	x = gp_sum(1, r, i) * half
	y = what(p, i-1) * half
	print((x + y)%mod, end = ' ')
``

</details>
