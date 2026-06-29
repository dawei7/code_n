# Range Assign, Number of Distinct Elements Minimize

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RANGEASSIGN |
| Difficulty Rating | 1648 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [RANGEASSIGN](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/RANGEASSIGN) |

---

## Problem Statement

You are given an array $A$ of $N$ **positive** integers.

In one operation, you can do the following:
- Choose integers $i$ and $j$ $(1 \le i < j \le N)$, such that $A_i = A_j$;
- For all $k$ $(i < k < j)$, change the value of $A_k$ to $A_i$.

Find out whether $A$ can have **at most $2$ distinct** values after using **any** (possibly zero) number of operations.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input:
    - The first line of each test case contains $N$ - the size of the array.
    - The next line contains $N$ integers, $A_1, A_2, A_3, \ldots, A_N$ - the elements of the array.

---

## Output Format

For each test case, print `YES` if $A$ can have **at most $2$ distinct** values after using **any** (possibly zero) number of operations and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5
5 9 5 5 5
3
1 2 3
4
1 2 1 3
4
1 2 3 1
```

**Output**

```text
YES
NO
YES
YES
```

**Explanation**

**Test case $1$:** The array $A$ already has $2$ distinct elements.

**Test case $2$:** It is impossible to make operations such that $A$ has $2$ distinct elements.

**Test case $3$:** We can make an operation as:
- Choose $i = 1$ and $j = 3$. Thus, we change $A_2$ to $A_1 = 1$.

The final array is $[1,1,1,3]$ which has two distinct elements.

**Test case $4$:** We can make an operation as:
- Choose $i = 1$ and $j = 4$. Thus, we change $A_2$ and $A_3$ to $A_1 = 1$.

The final array is $[1,1,1,1]$ which has one distinct element.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
5 9 5 5 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4
1 2 1 3
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4
1 2 3 1
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RANGEASSIGN)

[Contest: Division 1](https://www.codechef.com/START64A/problems/RANGEASSIGN)

[Contest: Division 2](https://www.codechef.com/START64B/problems/RANGEASSIGN)

[Contest: Division 3](https://www.codechef.com/START64C/problems/RANGEASSIGN)

[Contest: Division 4](https://www.codechef.com/START64D/problems/RANGEASSIGN)

***Author:*** [Ritul Kumar Singh](https://www.codechef.com/users/ritul_kr_singh)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1648

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have an array A. In one move you can choose two integers i \lt j such that A_i = A_j and set A_k = A_i for each i \lt k \lt j.

Can you perform operations such that A has at most two distinct elements in the end?

#
[](#explanation-5)EXPLANATION:

First, if A_1 = A_N, the answer is clearly “Yes”: just make the entire array equal.

Otherwise, notice that the operation cannot change A_1 or A_N, so our only hope is to have the two distinct elements in the array be these two.

So, the only reasonable moves to make are those starting at i = 1 or those ending at j = N.

This immediately means the answer is “Yes” if and only if there exists an index i such that A_i = A_1 and A_{i+1} = A_N.

This can be checked easily with a simple `for` loop.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int int64_t
#define sp << ' ' <<
#define nl << '\n'

signed main() {
	cin.tie(0)->sync_with_stdio(0);

	int T; cin >> T;
	while(T--) {
		int N; cin >> N;

		int A[N];
		for(int &i : A) cin >> i;

		bool ok = A[0] == A[N-1];

		for(int i = 1; i < N; ++i)
			if(A[i] == A[N-1] && A[i-1] == A[0]) ok = 1;

		cout << (ok ? "YES" : "NO") nl;
	}
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
    ll n; cin>>n;
    vector<ll> a(n+5);
    for(ll i=1;i<=n;i++){
        cin>>a[i];
    }
    if(a[1]==a[n]){
        cout<<"YES\n";
        return;
    }
    for(ll i=1;i<n;i++){
        if((a[i]==a[1]) and (a[i+1]==a[n])){
            cout<<"YES\n";
            return;
        }
    }
    cout<<"NO\n";
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
    a = list(map(int, input().split()))
    if a[0] == a[-1]:
        print('Yes')
    else:
        ans = 'No'
        for i in range(n-1):
            if a[i] == a[0] and a[i+1] == a[-1]:
                ans = 'Yes'
        print(ans)
``

</details>
