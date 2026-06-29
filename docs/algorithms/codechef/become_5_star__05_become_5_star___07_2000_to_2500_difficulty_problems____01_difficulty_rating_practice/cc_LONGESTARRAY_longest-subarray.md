# Longest Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LONGESTARRAY |
| Difficulty Rating | 2267 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [LONGESTARRAY](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/LONGESTARRAY) |

---

## Problem Statement

You are given an array $A$ of length $N$.

Find the **maximum length** of any subarray of $A$, such that, the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of all the elements of the subarray is equal to the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the remaining elements of the array.

Report $-1$ if no such subarray exists.

Note:
- A subarray is formed by deleting some (possibly zero) elements from the beginning of the array and some (possibly zero) elements from the end of the array.
- The bitwise OR of an empty array is considered to be $0$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

---

## Output Format

For each test case, output on a new line, the **length** of **longest** subarray such that the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array, or output $-1$ if no such subarray exists.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \lt 2^{30}$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 4
3
1 3 2
4
2 3 4 7
```

**Output**

```text
-1
1
3
```

**Explanation**

**Test case $1$:** For no subarray of $A$, the bitwise OR of the elements of the subarray equals the bitwise OR of the remaining elements.

**Test case $2$:** Consider the subarray $[3]$ having length $1$. The bitwise OR of the subarray is $3$ and the bitwise OR of the remaining elements of the array is $1 | 2 = 3$. Thus, the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array.

**Test case $3$:** Consider the subarray $[2, 3, 4]$ having length $3$. The bitwise OR of the subarray is $2|3|4 = 7$ and the bitwise OR of the remaining elements of the array is $7$. Thus, the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 4
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
3
1 3 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
2 3 4 7
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LONGESTARRAY)

[Contest: Division 1](https://www.codechef.com/START69A/problems/LONGESTARRAY)

[Contest: Division 2](https://www.codechef.com/START69B/problems/LONGESTARRAY)

[Contest: Division 3](https://www.codechef.com/START69C/problems/LONGESTARRAY)

[Contest: Division 4](https://www.codechef.com/START69D/problems/LONGESTARRAY)

***Authors:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2267

#
[](#prerequisites-3)PREREQUISITES:

Prefix sums

#
[](#problem-4)PROBLEM:

You are given an array A. Find the largest possible value of r-l+1 such that A_l \mid A_{l+1} \mid \ldots \mid A_r = A_1 \mid A_2 \mid \ldots \mid A_{l-1} \mid A_{r+1} \mid \ldots \mid A_N.

Here, \mid denotes bitwise OR.

#
[](#explanation-5)EXPLANATION:

Let M = A_1 \mid \ldots \mid A_N be the bitwise OR of all the elements.

Let’s call subarray [l, r] *valid* if its bitwise OR equals the bitwise OR of the rest of the array.

Note that the bitwise OR of any valid subarray *must* be M.

Why?

Let the bitwise OR of the subarray be x. Then, the outside also has bitwise OR x, and together they make up the whole array.

So, x\mid x = M, but x\mid x = x so we have x = M.

To phrase this differently, a subarray is valid if and only if, for each bit b that occurs in M,

-
A[l, r] contains an element with the b-th bit set; **and**

-
A[1, l-1] \cup A[r+1, N] contains an element with the b-th bit set.

Let’s use this fact.

Suppose we fix a position l. Let’s try to find the largest r such that [l, r] is valid: if we can do this for every l, the answer is the maximum value of r-l+1 among them all.

Now that l is fixed, let’s look at a specific bit b that is present in M.

- If b is present somewhere in the subarray [1, l-1], then the ‘outside’ is good with respect to this bit.

- Otherwise, we need to ensure that b is present **after** r.

- In particular, if last_b is the last position that contains b, then we must have r \lt last_b.

Each b that is not present in the prefix gives us one such constraint on r. Apply all of them to obtain the maximum possible r we can get if we start at l.

Now, the outside is taken care of, so we need to check the inside.

That is, for each b, we need to check whether it appears in the range [l, r] or not.

Putting everything together, we require the following:

- Given l and b, check whether [0, l-1] contains b

- Given l, r, b, check whether [l, r] contains b

- Given b, find last_b, the last index at which b appears

The last array in the third part can be precomputed by iterating across the array and just looking at each bit.

The first and second parts can be solved with the help of prefix sums.

Let P(i, b) denote the number of times b appears in [1, i]. Note that if we knew every P(i, b), then:

- Checking whether b lies in [0, i-1] is the same as checking whether P(i-1, b) \gt 0

- Checking whether b lies in [l, r] is the same as checking whether P(r, b) - P(l-1, b) \gt 0

P(i, b) can be calculated as follows:

- If A_i contains the bit b, then P(i, b) = P(i-1, b) + 1

- Otherwise, P(i, b) = P(i-1, b)

This allows us to compute every P(i, b) in \mathcal{O}(30N) time, and with this the rest of the problem can also be solved in \mathcal{O}(30N) as described above.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(30\cdot N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``// #pragma GCC optimize("O3")
// #pragma GCC optimize("Ofast,unroll-loops")

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
const ll MAX=500500;
ll freq[35][MAX];
void solve(){
    ll n; cin>>n;
    vector<ll> till(35,n+1);
    vector<ll> a(n+5,0);
    ll total=0;
    for(ll i=0;i<30;i++){
        freq[i][0]=0;
    }
    for(ll i=1;i<=n;i++){
        ll x; cin>>x;
        a[i]=x;
        total|=x;
        for(ll j=0;j<30;j++){
            freq[j][i]=freq[j][i-1]+min(1LL,x&(1<<j));
            if(x&(1<<j)){
                till[j]=i;
            }
        }
    }
    ll ans=-1,cur=0;
    for(ll i=1;i<=n;i++){
        ll l=n+1;
        for(ll j=0;j<30;j++){
            if(!(total&(1<<j))){
                continue;
            }
            if(cur&(1<<j)){
                ;
            }
            else{
                l=min(l,till[j]);
            }
        }
        ll check=l>i;
        for(ll j=0;j<30;j++){
            if(!(total&(1<<j))){
                continue;
            }
            if(freq[j][i-1] >= freq[j][l-1]){
                check=0;
            }
        }
        if(check){
            ans=max(ans,l-i);
        }
        cur|=a[i];
    }
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
``import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	first, last = [-1]*31, [-1]*31
	ct = [[0 for _ in range(31)] for _ in range(n+1)]
	for i in range(n):
		for b in range(30):
			ct[i+1][b] = ct[i][b]
			if (a[i] >> b) & 1:
				last[b] = i
				ct[i+1][b] += 1
				if first[b] == -1: first[b] = i
	ans = -1
	for i in range(n):
		r = n-1
		for b in range(30):
			if first[b] < i: continue
			r = min(r, last[b]-1)
		if r < i: continue
		len = r-i+1
		for b in range(30):
			if first[b] == -1: continue
			have = ct[r+1][b] - ct[i][b]
			if have == 0: len = -1
		ans = max(ans, len)
	print(ans)
``

</details>
