# Prime Factor Division

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIMEFACDIV |
| Difficulty Rating | 2016 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [PRIMEFACDIV](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/PRIMEFACDIV) |

---

## Problem Statement

*Mario has reached Bowser's Castle and is inches away from rescuing Princess Peach. He has to answer the following problem at the gate to be allowed to enter. Can you help him?*

Let $S(M)$ denote the set of all [prime](https://en.wikipedia.org/wiki/Prime_number) [factors](https://en.wikipedia.org/wiki/Divisor) of $M$.
Given two positive integers $A$ and $B$, determine whether $A$ is divisible by all elements in $S(B)$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, $A$ and $B$, as mentioned in the statement.

---

## Output Format

For each test case, print `YES` if $A$ is divisible by all elements in $S(B)$ and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
21 63
72 72
25 20
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case $1$:** The set of all prime factors of $B = 63$ is given by $S(B) = \{3, 7\}$. Also, $A = 21$ is divisible by all elements in $S(B)$.

**Test case $2$:** The set of all prime factors of $B = 72$ is given by $S(B) = \{2, 3\}$. Also, $A = 72$ is divisible by all elements in $S(B)$.

**Test case $3$:** The set of all prime factors of $B = 20$ is given by $S(B) = \{2, 5\}$. Here, $A = 25$ is not divisible by $2$ in $S(B)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
21 63
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
72 72
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
25 20
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PRIMEFACDIV)

[Contest: Division 1](https://www.codechef.com/START64A/problems/PRIMEFACDIV)

[Contest: Division 2](https://www.codechef.com/START64B/problems/PRIMEFACDIV)

[Contest: Division 3](https://www.codechef.com/START64C/problems/PRIMEFACDIV)

[Contest: Division 4](https://www.codechef.com/START64D/problems/PRIMEFACDIV)

***Author:*** [Vishesh Saraswat](https://www.codechef.com/users/vishesh_s)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2016

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with prime factorization

#
[](#problem-4)PROBLEM:

Given two integers A and B, does every prime dividing B also divide A?

#
[](#explanation-5)EXPLANATION:

The obvious solution is to attempt to prime-factorize B and then check if each prime factor divides A.

Unfortunately, both the number of test cases and the numbers themselves are too large: even a fast prime-factorization algorithm likely isn’t going to be fast enough, so we need to be a bit smarter.

There’s a couple of different ways to approach this task, though for the most part they rely on looking at the prime factorizations of A and B and drawing some conclusions from that.

Method 1 (GCD)

Consider a prime p that divides B. Suppose it also divides A.

Then, p definitely divides \gcd(A, B).

In particular, since \gcd(A, B) is a factor of B, the answer to the initial question is “Yes” if and only if B and \gcd(A, B) have the same set of primes dividing them.

So, we essentially reduce our problem to this: given two integers x and y, where y is a factor of x, do they have the same set of prime factors dividing them?

- If x = 1, then y = 1 and the answer is obviously “Yes”.

- If x \gt 1 but y = 1, the answer is obviously “No”.

- Otherwise, we have x, y \gt 1. Since y \mid x, let’s look at z = x/y.

- Consider some prime p that divides x.

- If x and y have the same power of p, then z doesn’t contain p at all.

- Otherwise, z does contain some power of p. So, p divides y if and only if p divides \gcd(z, y).

In other words, in the case when x, y \gt 1, they have the same prime factors if and only if z and \gcd(z, y) have the same prime factors!

This gives us a pretty simply algorithm:

- Initially, x = B and y = \gcd(A, B).

- While x \gt 1 and y \gt 1, replace x and y with x/y and \gcd(y, x/y).

- In the end, if x = 1 the answer is “Yes” and otherwise the answer is “No”.

The while loop runs only \mathcal{O}(\log B) times, since at each step the larger number is at least halved. This is fast enough for our purposes.

Method 2 (Exponentiation)

A rather interesting solution is to simply compute A^{60} \bmod B and check whether this is 0 or not.

Computing A^{60} \bmod B can be done quickly with exponentiation, however if you’re using C++ or Java you’ll need to use 128-bit integers or something like [this](https://github.com/kth-competitive-programming/kactl/blob/main/content/number-theory/ModMulLL.h), since otherwise the multiplications will overflow even `long long`.

Why does this work?

The idea behind this solution is simple: if p is a prime that divides B, then p divides A if and only if p divides A^{60}.

This follows from the fact that the largest power of a prime that fits within 10^{18} is 59 (since 2^{60} \gt 10^{18}).

The prime factorization of A^{60} has every prime to a power of at least 60, which is strictly larger than the power of anything in B. So, every prime in B divides A^{60} if and only if then B itself divides A^{60}, so we simply check that instead.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\log B) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include "bits/stdc++.h"
using namespace std;
/*
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using ordered_set = tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>;
*/

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define sz(x) (int)(x).size()

using ll = long long;
#define int ll
const int mod = 1e9+7;

void solve(int tc) {
    int a, b;
    cin >> a >> b;
    int g = gcd(a, b);
    int gg = gcd(g, b);
    while (b % gg == 0 and gg != 1) {
        b /= gg;
        gg = gcd(gg, b);
    }
    cout << (b == 1 ? "YES\n" : "NO\n");
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);
    int tc = 1;
    cin >> tc;
    for (int i = 1; i <= tc; ++i) solve(i);
    return 0;
}

``

Tester's code (C++)
``#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast,unroll-loops")
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
const ll MOD=1e9+7;
const ll MAX=1000100;
void solve(){
    ll a,b; cin>>a>>b;
    ll g=__gcd(a,b);
    while(b!=1){
        ll x=__gcd(g,b);
        if(x==1){
            cout<<"NO\n";
            return;
        }
        b/=x;
    }
    cout<<"YES\n";
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
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b = map(int, input().split())
    print('Yes' if pow(a, 60, b) == 0 else 'No')
``

</details>
