# Sum of Cube 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMOFCUBE |
| Difficulty Rating | 2259 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SUMOFCUBE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SUMOFCUBE) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ positive integers.

Find $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j)$, where $F(i,j)=\sum_{k=i}^{j} A_k$.

Since the value might be quite large, print it modulo $998244353$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

---

## Output Format

For each test case, output on a new line, the answer, modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
1 1
3
1 2 1
5
8 5 6 2 3
```

**Output**

```text
10
128
42621
```

**Explanation**

**Test case $1$:** $F(1, 1) = 1, F(1, 2) = 1+1=2, F(2, 2) = 1$.

Thus, $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j) = 1^3 + 2^3 + 1^3 = 10$.

**Test case $2$:** $F(1, 1) = 1, F(1, 2) = 1+2=3, F(1, 3) = 1+2+1 =4, F(2, 2) = 2, F(2, 3) = 2+1=3, F(3, 3) = 1$.

Thus, $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j) = 1^3 + 3^3 + 4^3+2^3+3^3+1^3 = 128$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
3
1 2 1
```

**Output for this case**

```text
128
```



#### Test case 3

**Input for this case**

```text
5
8 5 6 2 3
```

**Output for this case**

```text
42621
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUMOFCUBE)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/SUMOFCUBE)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/SUMOFCUBE)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/SUMOFCUBE)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/SUMOFCUBE)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2259

#
[](#prerequisites-3)PREREQUISITES:

[Prefix sums](https://usaco.guide/silver/prefix-sums?lang=cpp)

#
[](#problem-4)PROBLEM:

Given an array A, compute

\sum_{i=1}^N \sum_{j=i}^N \left( \sum_{k=i}^j A_k\right)^3

#
[](#explanation-5)EXPLANATION:

Most problems that have to do with some operation on subarray sums are often made simpler by thinking about them in terms of prefix sums, and this one is no different.

Let P_i = A_1 + A_2 + \ldots + A_i for i \geq 1, with P_0 = 0.

Writing our expression in terms of these prefix sums gives us

\sum_{i=1}^N \sum_{j=i}^N (P_j - P_{i-1})^3 = \sum_{i=1}^N \sum_{j=i}^N (P_j^3 - P_{i-1}^3 - 3P_j^2P_{i-1} + 3P_jP_{i-1}^2)

Suppose we fix the value of j. Let’s look at what we compute as i varies, for each term above:

-
P_j^3 is added once for each i \leq j, adding a total of j \cdot P_j^3 to the final answer

-
-P_{i-1}^3 is added once for each i \leq j. This simply corresponds to the (j-1)-th prefix sum of the array [-P_1^3, -P_2^3, \ldots, -P_N^3]

- This is essentially another prefix sum array, so just precompute this array in \mathcal{O}(N) after computing P.

- The sum of -3P_j^2P_{i-1} across all i \leq j is simply -3P_j^2 \cdot x, where x = P_1 + P_2 + \ldots + P_{j-1} is yet another prefix sum.

- The sum of 3P_jP_{i-1}^2 across all i \leq j is, yet again, 3P_j multiplied by the (j-1)-th prefix sum of [P_1^2, P_2^2, \ldots, P_N^2].

Notice that if all the required prefix sums are precomputed, then we can process a fixed j in \mathcal{O}(1) time, thus solving the problem in \mathcal{O}(N) in total by simply iterating across j.

This problem is somewhat overflow-prone because of all the cubing and squaring of large numbers, so make sure to look out for that and keep all the values within the modulo.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
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
const ll MAX=2002;
ll pw(ll x,ll ex){
    ll now=1;
    while(ex--){
        now=(now*x)%MOD;
    }
    return now;
}
void solve(){
    ll n; cin>>n;
    vector<ll> pref(n+5,0);
    for(ll i=1;i<=n;i++){
        ll x; cin>>x;
        pref[i]=(pref[i-1]+x)%MOD;
    }
    vector<ll> dp(4,0);
    dp[0]=1;
    ll ans=0;
    vector<ll> coef(5,1);
    coef[0]=-1;
    coef[1]=3;
    coef[2]=-3;
    for(ll i=1;i<=n;i++){
        for(ll j=0;j<=3;j++){
            ll cur=coef[j]*pw(pref[i],j)*dp[3-j];
            ans=(ans+coef[j]*pw(pref[i],j)*dp[3-j])%MOD;
        }
        for(ll j=0;j<=3;j++){
            dp[j]=(dp[j]+pw(pref[i],j))%MOD;
        }
    }
    ans=(ans+MOD)%MOD;
    cout<<ans<<nline;
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
``mod = 998244353

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ans = pref = 0
	psum = psum2 = psum3 = 0
	for i in range(n):
		pref += a[i]

		ans += (i+1)*(pref ** 3)
		ans -= psum3
		ans -= 3*(pref ** 2)*psum
		ans += 3*pref*psum2
		ans %= mod

		psum += pref
		psum2 += pref ** 2
		psum3 += pref ** 3
	print(ans)
``

</details>
