# Distinct Neighbours 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISTINCTNEIG |
| Difficulty Rating | 1997 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [DISTINCTNEIG](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/DISTINCTNEIG) |

---

## Problem Statement

You are given an array $A$ of length $2\cdot N$.

You also have an **empty** array $B$. You are asked to do the following operation exactly $N$ times.

- Choose two **distinct** indices $x$ and $y$ $(1\le x,y \le |A|)$;
- Append $(A_x - A_y)$ to the end of array $B$;
- Delete the $x^{th}$ and $y^{th}$ elements from $A$ and concatenate remaining elements without changing the order.

Find whether there exists a set of operations to get array $B$ such that $B_i \neq B_{(i+1)}$ $(1 \leq i \lt N)$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$.
    - The second line of each test case contains $2\cdot N$ space-separated integers $A_1,A_2,\ldots,A_{2\cdot N}$ representing the array $A$.

---

## Output Format

For each test case, print on a new line the answer: `YES` if it is possible to obtain valid $B$, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES, `yes`, `yEs` will all be treated as identical.

---

## Constraints

- $1 \leq T \leq 10^3$
- $2 \leq N \leq 10^3$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^3$.

---

## Examples

**Example 1**

**Input**

```text
3
2
1 1 1 1
3
1 1 2 2 3 3
2
1 1 2 2
```

**Output**

```text
NO
YES
YES
```

**Explanation**

**Test case $1$:** No matter how we perform the operations, $B=[0,0]$.

**Test case $2$:**
- In first operation, we can take $x=2$ and $y=3$. Now we append $A_x-A_y=1-2=-1$ at the back of $B$, and delete $A_2$ and $A_3$ from $A$. Now $A=[1,2,3,3]$.
- In second operation, we can take $x=2$ and $y=1$; append $A_x - A_y = 2-1 = 1$ at the back of $B$ and delete $A_2$ and $A_1$. Thus, $A = [3, 3]$ and $B = [-1, 1]$.
- In the third operation, we take $x=1$ and $y=2$; append $A_x - A_y = 3-3 = 0$ at the back of $B$ and delete $A_1$ and $A_2$. Thus, $A = []$ and $B = [-1, 1,0]$.

Thus, finally $B=[-1,1,0]$. There are no two consecutive elements in $B$ that are equal.

**Test case $3$:**
- In first operation, we can take $x=2$ and $y=3$. Now we append $A_x-A_y=1-2=-1$ at the back of $B$, and delete $A_2$ and $A_3$ from $A$. Now $A=[1,2]$.
- In second operation, we can take $x=2$ and $y=1$; append $A_x - A_y = 2-1 = 1$ at the back of $B$ and delete $A_2$ and $A_1$. Thus, $A = []$ and $B = [-1, 1]$.

Thus, finally $B=[-1,1]$. There are no two consecutive elements in $B$ that are equal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 1 1 1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
3
1 1 2 2 3 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2
1 1 2 2
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

[Practice](https://www.codechef.com/problems/DISTINCTNEIG)

[Contest: Division 1](https://www.codechef.com/START64A/problems/DISTINCTNEIG)

[Contest: Division 2](https://www.codechef.com/START64B/problems/DISTINCTNEIG)

[Contest: Division 3](https://www.codechef.com/START64C/problems/DISTINCTNEIG)

[Contest: Division 4](https://www.codechef.com/START64D/problems/DISTINCTNEIG)

***Author:*** [Satyam](https://www.codechef.com/users/satyam_343)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1997

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You are given an array A of length 2N. Let B be an empty array. Repeat the following N times:

- Pick two elements x and y of A. Delete them from A and append x-y to B.

Is it possible to perform moves so that B_i \neq B_{i+1} for each 1 \leq i \lt N?

#
[](#explanation-5)EXPLANATION:

Suppose we perform moves on A in some order to end up with B. Let’s analyze the array we get.

- If B_i \neq B_{i+1} for any i, of course we’re happy.

- Otherwise, B_i = B_{i+1} for some index. There are two cases here:

- If B_i \neq 0, we can actually fix this error. Note that B_i = x - y for some x and y from A. Instead, we could’ve just chosen B_i = y - x instead: now B_i and B_{i+1} have different signs, so they obviously can’t be equal.

- If B_i = 0, once again we have two cases:

- Suppose B_i = x - x and B_{i+1} = y - y, where x \neq y. Then, we can replace them with x-y and y-x instead, which fixes the problem.

- However, if B_i = B_{i+1} = x - x, there’s nothing we can do.

This should give us the intuition that if there are too many occurrences of the same integer x in A, we’ll always end up with some adjacent pair in B that’s both x - x, which can’t be fixed.

But, how many is too many?

Let’s fix an integer x, and say it occurs k times in A. Then,

- If k \leq N, there exists a way to create B such that we never create zeros of the form x - x, since we can always pair an x with a non-x.

- Otherwise, there will always be some pairs of the form x - x.

- There are 2N - k non-x elements, allowing us to create at most 2N - k pairs of x with something else.

- This leaves a minimum of k - (2N - k) = 2k - 2N instances of x, which means B will contain at least k-N zeros of the form x-x.

- For these zeros to not adjacent in B, their number cannot exceed half the length of B (which is N). That is, k-N \leq \left\lceil \frac{N}{2}\right\rceil must hold (\left\lceil \ \ \right\rceil denotes the [ceiling](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) function).

Now notice that if this condition holds for some k, it will also hold for any lower k. So, it’s enough to check this for the largest value of k. That is,

- Let k be the largest number of occurrences of some element in A.

- Then, the answer is “Yes” if and only if k - N \leq \left\lceil \frac{N}{2}\right\rceil

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
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
    vector<ll> freq(n+5,0);
    ll till=n+(n+1)/2;
    for(ll i=1;i<=2*n;i++){
        ll x; cin>>x;
        freq[x]++;
    }
    sort(all(freq));
    if(freq.back()>till){
        cout<<"NO\n";
    }
    else{
        cout<<"YES\n";
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
    a = list(map(int, input().split()))
    mx = max(a.count(x) for x in a)
    print('Yes' if (mx - n) <= (n+1)//2 else 'No')
``

</details>
