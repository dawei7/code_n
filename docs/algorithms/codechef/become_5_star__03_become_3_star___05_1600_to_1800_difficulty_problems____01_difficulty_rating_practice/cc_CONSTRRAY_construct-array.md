# Construct Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONSTRRAY |
| Difficulty Rating | 1624 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CONSTRRAY](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CONSTRRAY) |

---

## Problem Statement

You are given a positive integer $N$.

Consider an array $A$ of length $N$. Let $P_i$ denote the sum of the first $i$ elements of $A$ and $S_i$ denote the sum of the last $i$ elements of $A$.

You need to construct the array $A$ of size $N$ such that all of the following conditions are met:
- $-10^9 \leq A_i \leq 10^9$, for all $(1\le i \le N)$
- $P_i \gt S_i$ if $i$ is odd, for each $(1 \leq i \lt N)$
- $P_i \lt S_i$ if $i$ is even, for each $(1 \leq i \lt N)$

If there are multiple solutions, you can print any of them.
If there is no such array, print $-1$ instead.

---

## Input Format

- Each test contains multiple test cases. The first line contains the number of test cases $T$.
- The only line of each test case contains a single integer $N$, where $N$ is the length of the required array.

---

## Output Format

For each test case, if a **valid** array exists, print $N$ space-separated integers $A_1, A_2, \ldots, A_N$ satisfying all the given conditions.

If there are multiple solutions, you can print any of them.
If there is no such array, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 10^3$
- $2 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
3
4
```

**Output**

```text
343 -343
-1
0 -5 343 -100
```

**Explanation**

**Test case $1$:** All elements are in the given range for the array $A = [343, -343]$.
- For $i = 1$: Since $i$ is odd, $P_1 = 343$ is greater than $S_1 = -343$.

**Test case $2$:** It can be proved that no array of length $3$ exists satisfying all conditions.

**Test case $3$:** All elements are in the given range for the array $A = [0, -5, 343, -100]$.
- For $i = 1$: Since $i$ is odd, $P_1 = 0$ is greater than $S_1 = -100$.
- For $i = 2$: Since $i$ is even, $P_2 = 0 + (-5) = -5$ is less than $S_2 = 343 + (-100) = 243$.
- For $i = 3$: Since $i$ is odd, $P_3 = 0 + (-5) + 343 = 338$ is greater than $S_3 = (-5)+343 +(-100) = 238$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
343 -343
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
0 -5 343 -100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CONSTRRAY)

[Contest: Division 1](https://www.codechef.com/START76A/problems/CONSTRRAY)

[Contest: Division 2](https://www.codechef.com/START76B/problems/CONSTRRAY)

[Contest: Division 3](https://www.codechef.com/START76C/problems/CONSTRRAY)

[Contest: Division 4](https://www.codechef.com/START76D/problems/CONSTRRAY)

***Author:*** [nirkhut](https://www.codechef.com/users/nirkhut)

***Preparer***: [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Construct an array of length N such that for each 1 \leq i \lt N,

- If i is odd, P(i) \gt S(i)

- If i is even, P(i) \lt S(i)

P(i) denotes the sum of the first i elements of A, S(i) denotes the sum of the last i elements of A.

#
[](#explanation-5)EXPLANATION:

Looking at what the inequalities given to us mean in terms of the values of A, we see that:

- A_1 \gt A_N

- A_1 + A_2 \lt A_N + A_{N-1}

-
A_1 + A_2 + A_3 \gt A_N + A_{N-1} + A_{N-2}

\vdots

Intuitively, for the inequalities to reverse we see A_2 should be “much smaller” than A_{N-1}; A_3 should be “much larger” than A_{N-2}; and so on.

In general,

- If i is odd, A_i should be much larger than A_{N+1-i}

- If i is even, A_i should be much smaller than A_{N+1-i}

In particular, A_i can never equal $A_{N+1-i} for any 1 \leq i \leq N.

Notice that this immediately tells us that when N is odd, no such array can exist: we would require the middle element to not equal itself, which is obviously impossible.

Now let’s deal with the case when N is even.

One easy way to deal with the “much larger/much smaller” conditions is to make one of the elements positive and the other negative. Setting one of them to x and the other to -x for an appropriately chosen x will give us what we want.

Let’s try to build A in this fashion.

- First, set A_1 = 1 and A_N = -1. This ensures A_1 \gt A_N.

- Now, if we set A_2 = -2 and A_{N-2} = 2, we get P(2) = -1 and S(2) = 1, satisfying the inequality.

- Once again, it’s easy to see that setting A_3 = 2 and A_{N-2} = -2 gives us P(3) = 1 and S(3) = -1, as necessary.

\vdots

In general, alternating between 2 and -2 (except for the first and last elements) will give us what we want:

- If i is even

- P(i) = 1 + (-2) + 2 + (-2) + \ldots + (-2) = -1

- S(i) = -1 + 2 + (-2) + 2 + \ldots + 2 = 1

- If i is odd

- P(i) = 1 + (-2) + 2 + (-2) + \ldots + 2 = 1

- S(i) = -1 + 2 + (-2) + 2 + \ldots + (-2) = -1

This satisfies all the inequalities we have, and so is a valid array.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Preparer's code (C++)
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
const ll MAX=500500;
void solve(){
    ll n; cin>>n;
    if(n&1){
        cout<<"-1\n";
    }
    else{
        if(n==4){
            cout<<"0 5 343 -100\n";
            return;
        }
        cout<<"1";
        ll use=-2;
        for(ll i=2;i<n;i++){
            cout<<" "<<use;
            use*=-1;
        }
        cout<<" -1\n";
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
    n = int(input())
    if n%2 == 0: print( *([-1] + [2, -2]*(n//2 - 1) + [1]) )
    else: print(-1)
``

</details>
