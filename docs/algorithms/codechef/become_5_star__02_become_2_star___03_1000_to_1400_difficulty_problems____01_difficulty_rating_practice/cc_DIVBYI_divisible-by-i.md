# Divisible by i 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVBYI |
| Difficulty Rating | 1184 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [DIVBYI](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DIVBYI) |

---

## Problem Statement

You are given an integer $N$.

Construct a permutation $P$ of length $N$ such that
- For all $i$ $(1 \leq i \leq N-1)$, $i$ divides $abs(P_{i+1}-P_i)$.

Recall that a permutation of length $N$ is an array where every integer from $1$ to $N$ occurs exactly once.

It can be proven that for the given constraints at least one such $P$ always exists.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follow.
- The only line of each test case contains an integer $N$ - the length of the array to be constructed.

---

## Output Format

For each test case, output a single line containing $N$ space-separated integers $P_1, P_2, \dots, P_N$, denoting the elements of the array $P$.

If there exist multiple such arrays, print any.

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $2 \leq N \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^5$.

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
1 2
2 1 3
```

**Explanation**

**Test case 1:** A possible array satisfying all the conditions is $[1, 2]$:
  - For $i=1$: $abs(A_2-A_1)=abs(2-1)=1$ is divisible by $1$.

**Test case 2:** A possible array satisfying all the conditions is $[2, 1, 3]$:
  - For $i=1$: $abs(A_2-A_1)=abs(1-2)=1$ is divisible by $1$.
  - For $i=2$: $abs(A_3-A_2)=abs(3-1)=2$ is divisible by $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
1 2
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
2 1 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE221A/problems/DIVBYI)

[Contest Division 2](https://www.codechef.com/JUNE221B/problems/DIVBYI)

[Contest Division 3](https://www.codechef.com/JUNE221C/problems/DIVBYI)

[Contest Division 4](https://www.codechef.com/JUNE221D/problems/DIVBYI)

Setter: [Satyam](https://www.codechef.com/users/satyam_343)

Tester: [Lavish Gupta](https://www.codechef.com/users/lavish_adm), [Abhinav sharma](https://www.codechef.com/users/inov_360),[ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1184

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an integer N.

Construct a permutation P of length N such that

- For all i (1 \leq i \leq N-1), i divides abs(P_{i+1}-P_i).

Recall that a permutation of length N is an array where every integer from 1 to N occurs exactly once.

It can be proven that for the given constraints at least one such P always exists.

#
[](#explanation-5)EXPLANATION:

Let us look at the maximum difference needed (and is possible) for any two adjacent values in the permutation. It is equal to N-1 (needed to be divisible by index i=N-1) and since P only consists of the values from 1 to N. It is possible only when the last two values are 1,N or N,1.

Let us take the case when the last two values are 1,N i.e P_N=N and P_{N-1}=1. Now for index N-2 we need the absolute difference of P_{N-2} and P_{N-1} to be divisible by  N-2 which is again the maximum possible difference that can be created from the remaining values (as N can’t be used anymore to create differences) which are 1 and N-2. Assign P_{N-2}=N-1. Now for index N-3 we need the absolute difference of P_{N-3} and P_{N-2} to be divisible by  N-3 which is again the maximum possible difference that can be created from the remaining values (as N and 1 can’t be used anymore to create differences) which are 2 and N-1. Therefore P_{N-3}=2. Using same analysis keep assigning the values till all values of the permutation are exhausted.

This sequence can be generated in linear time: Let R=N and L=1. Keep iterating from the index i=N to 1 assign P_i=R and P_{i-1}=L(if\: i-1\geq 1), Decrease R by 1 and increase L by 1. The resulting sequence is same as described above and it satisfies the condition needed in the problem. Similar analysis can be carried out for the sequence when P_N=1 and P_{N-1}=N.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
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
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define vvvl vector<vector<vector<ll>>>
#define all(v) v.begin(),v.end()
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
void _print(ll x){cerr<<x;}
void _print(string x){cerr<<x;}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<class T,class V> void _print(pair<T,V> p) {cerr<<"{"; _print(p.first);cerr<<","; _print(p.second);cerr<<"}";}
template<class T>void _print(vector<T> v) {cerr<<" [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T>void _print(set<T> v) {cerr<<" [ "; for (T i:v){_print(i); cerr<<" ";}cerr<<"]";}
template<class T>void _print(multiset<T> v) {cerr<< " [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T,class V>void _print(map<T, V> v) {cerr<<" [ "; for(auto i:v) {_print(i);cerr<<" ";} cerr<<"]";}
template<class T> using oset=tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template<class T> using muloset=tree<T, null_type, less_equal<T>, rb_tree_tag, tree_order_statistics_node_update>;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const ll MOD=1e9+7;
const ll MAX=500500;
void solve(){
    ll n; cin>>n;
    ll l=1,r=n;
    vector<ll> a(n+5,0);
    for(ll i=n;i>=1;i--){
        if((i&1)==(n&1)){
            a[i]=r--;
        }
        else{
            a[i]=l++;
        }
    }
    for(ll i=1;i<=n;i++){
        cout<<a[i]<<" \n"[i==n];
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
    cout<<fixed<<setprecision(15);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
  int n;
  cin >> n;
  int arr[n], l = 1, r = n;
  for (int i = n - 1; i >= 0; i -= 2)
  {
    arr[i] = l++;
    if (i - 1 >= 0)
      arr[i - 1] = r--;
  }
  for (int i = 0; i < n; i++)
    cout << arr[i] << ' ';
  cout << '\n';
  return;
}
int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL), cout.tie(NULL);
  int test = 1;
  cin >> test;
  while (test--)
    sol();
}

``

</details>
