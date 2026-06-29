# Swap the numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SWAPNUM31 |
| Difficulty Rating | 1869 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [SWAPNUM31](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/SWAPNUM31) |

---

## Problem Statement

You're given an array $A = [A_1, A_2, \ldots, A_N]$ containing $N$ integers.
You also have an integer $K$.

You can perform the following operation on this array:
- Choose indices $i$ and $j$ such that $|i - j| \geq K$, and swap $A_i$ and $A_j$.
That is, you can swap the values of two indices that are at a distance of at least $K$ from each other.

Find the lexicographically **smallest** array that can be reached, if you perform the above operation several (possibly, zero) times.

**Note:** For two arrays $X$ and $Y$ of the same length, $X$ is said to be lexicographically smaller than $Y$ if there exists an index $i$ ($1 \leq i \leq N$) such that:
- $X_1 = Y_1, X_2 = Y_2, \ldots, X_{i-1} = Y_{i-1}$; and
- $X_i \lt Y_i$

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$.
    - The next line contains $N$ space-separated numbers, the values $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print on a new line $N$ space-separated integers — the lexicographically smallest array possible after applying the above operation several times.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, K \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all tests won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
3 2
3 2 1
4 3
3 2 4 1
```

**Output**

```text
1 2 3
1 2 4 3
```

**Explanation**

**Test case $1$:** Initially, we have $A = [3, 2, 1]$.
Choose $i = 1$ and $j = 3$, which is valid because $|1-3| = 2 \geq K = 2$.
Swapping $A_1$ and $A_3$, we have the array $[1, 2, 3]$, which is the best we can do.

**Test case $2$:** $A = [3, 2, 4, 1]$ and $K = 3$ here.
The only possible swap is $i = 1$ and $j = 4$; the other two elements can't be moved.
Performing this swap gives us $A = [1, 2, 4, 3]$, which is the best we can do.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
3 2 1
```

**Output for this case**

```text
1 2 3
```



#### Test case 2

**Input for this case**

```text
4 3
3 2 4 1
```

**Output for this case**

```text
1 2 4 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SWAPNUM31)

[Contest: Division 1](https://www.codechef.com/START96A/problems/SWAPNUM31)

[Contest: Division 2](https://www.codechef.com/START96B/problems/SWAPNUM31)

[Contest: Division 3](https://www.codechef.com/START96C/problems/SWAPNUM31)

[Contest: Division 4](https://www.codechef.com/START96D/problems/SWAPNUM31)

***Author:*** [fellas](https://www.codechef.com/users/fellas)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1869

# [](#prerequisites-3)PREREQUISITES:

Sorting

# [](#problem-4)PROBLEM:

You have an array A and an integer K.

In one move, you can pick indices i, j such that |i-j| \geq K, and swap A_i and A_j.

What’s the lexicographically smallest array you can arrive at?

# [](#explanation-5)EXPLANATION:

Let’s call an index i *swappable* if there exists another index j such that |i-j| \geq K.

For each i = 1, 2, \ldots, N, let’s first find if it’s swappable or not.

It’s easy to see that an index is swappable if and only if i \geq K+1, or i+K \leq N (i.e, it can either be swapped with something to its left, or something to its right).

Now, any index that’s *not* swappable has its value fixed: that A_i can’t move anywhere after all.

On the other hand, any two swappable indices can always be made to swap values!

Proof

Let i and j be two swappable indices, with i \lt j.

If |i-j| \geq K, we can directly swap their values; so let’s look at the |i-j|\lt K case.

Since i is swappable, there are two possibilities:

- Suppose there exists an index x \lt i such that |i-x|\geq K, i.e, i can be swapped left.

Then, j can also be swapped left with x.

So, perform the sequence swap(i, x) \to swap(x, j) \to swap(i, x), and A_i and A_j have swapped positions without affecting anything else.

- Otherwise, there exists an index x \gt i such that |i-x| \geq K.

In particular, we can choose x = N.

- If |j-N| \geq K, then once again i and j can be swapped via index N, as we did above.

- Otherwise, |j-N|\lt K. But, since j is swappable, that means there must exist an index to the left of j that it can swap with.

We can always choose 1 to be this index - and in particular, 1 and N can be swapped with each other.

- Perform the sequence of swaps: swap(i, N) \to swap(j, 1) \to swap(1, N) \to swap(i, N) \to swap(1, j), and we’re done.

Given that we can rearrange the values of swappable indices as we like, to obtain the lexicographically minimum array it’s obviously best to sort them.

So, the solution is as follows:

- First, find all swappable indices. Suppose there are k of them: i_1, i_2, \ldots, i_k.

- Sort the values at these indices alone, and place them in i_1, i_2, \ldots, i_k in order.

- Leave the other positions untouched.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>
using namespace std;
using namespace __gnu_pbds;
#define ll long long
#define int long long
#define endl "\n"
#define fi first
#define se second
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define fr(a,b,c) for(int a=b; a<c; a++)
#define frr(a,b,c) for(int a=b;a>=c;a--)
#define pb push_back
#define pii pair<int,int>
#define R(a) ll a; cin >> a;
#define RS(a) string  a; cin >> a;
typedef tree<long long,null_type,greater_equal<long long>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef tree<long long,null_type,less<long long>,rb_tree_tag,tree_order_statistics_node_update> ordered_set1;
#define RA(a, n) ll a[(n) + 1] = {}; fr(i, 1, (n)+1) {cin >> a[i];}
#define RM(a, n, m) int a[n + 1][m + 1] = {}; fr(i, 1, n+1) {fr(j, 1, m+1) cin >> a[i][j];}
#define reset(X) memset(X, 0, sizeof(X))
using vi=vector<int>;

void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]"<<endl;}
template <typename T, typename... V>
void print(T t, V... v) {_print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define deb(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define deb(x...)
#endif
#define all(x) (x).begin(),(x).end()
const int inf = 1e18;
const int mod=998244353;
unsigned int power(int x, unsigned int y, int p)
{
    int res = 1;
    x = x % p;
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % p;
        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}
int modInverse(int n, int p)
{
    return power(n, p-2, p);
}

void solve () {
    int n, k;
    cin >> n >> k;
    int a[n+1];
    for( int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    vector<int>v;
    vector<bool>can_swap(n+1);
    for(int i = 1; i <= n; i++) {
        if(i + k <= n) {
            can_swap[i] = 1;
            can_swap[i+k] = 1;
        }

    }
    for(int i = 1; i <= n; i++) {
        if(can_swap[i]) {
            v.push_back(a[i]);
        }
    }
    sort(v.begin(), v.end());
    int pos = 0;
    for(int i = 1; i <= n; i++) {
        if(can_swap[i]) {
            a[i] = v[pos];
            pos += 1;
        }
    }

    for(int i = 1; i <= n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

 signed main()
    {
        fastio;
    #ifndef ONLINE_JUDGE
        if(fopen("input9.txt", "r"))
        {
            freopen("input9.txt", "r", stdin);
            freopen("output9.txt", "w", stdout);
        }
    #endif
        int t=1;
        cin>>t;
        //precompute();
        for(int i = 1; i<=t; i++)
        {
            solve();
        }
    }
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    moved = []
    unmoved = []
    for i in range(n):
        if i+k <= n-1 or i >= k: moved.append(a[i])
        else: unmoved.append(a[i])
    moved.sort()
    if not unmoved: print(*moved)
    else:
        k = len(moved)
        ans = moved[:k//2] + unmoved + moved[k//2:]
        print(*ans)
``

</details>
