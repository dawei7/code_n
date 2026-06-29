# Subsequence-Numbers Divisible by 7

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUB7NUM |
| Difficulty Rating | 1943 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [SUB7NUM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/SUB7NUM) |

---

## Problem Statement

Kulyash has given you an array $A$ of size $N$.

He defines the *subsequence-number* of a **non-empty** [subsequence](https://en.wikipedia.org/wiki/Subsequence)
$S$ of array $A$ as the number formed by the **concatenation** of all the elements of the subsequence $S$.

Find the count of non-empty subsequences of $A$ having their *subsequence-numbers* **divisible** by $7$. Since the answer can be huge, output it modulo $10^9 + 7$.

For example: Consider $A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$. A subsequence $S$ of $A$ is $[2, 5, 7, 10]$. The *subsequence-number* of this subsequence is $25710$.

---

## Input Format

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains one integer $N$, the size of the array.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of the array $A$.

---

## Output Format

For each test case, output in a single line the number of subsequences with *subsequence-number* divisible by $7$ modulo $1000000007$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 3\cdot 10^5$
- $1 \leq A_i \leq 3\cdot 10^5$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
4
1 2 3 4
2
7 7
```

**Output**

```text
0
1
3
```

**Explanation**

**Test case $1$:** Only $3$ subsequences are possible for the given array. These are $[1]$, $[1, 2]$, and $[2]$. The *subsequence-numbers* are $1$, $12$, and $2$ respectively. None of the *subsequence-numbers* are divisible by $7$, so the answer is $0$.

**Test case $2$:** $[1, 4]$ is the only subsequence having its *subsequence-number* $14$ which is divisible by $7$. So, the answer is $1$.

**Test case $3$:** All the non-empty subsequences $[7]$, $[7]$, and $[7, 7]$ have their *subsequence-numbers* $7, 7,$ and $77$ divisible by $7$. So, the answer is $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2
7 7
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

[Contest Division 1](https://www.codechef.com/MAY222A/problems/SUB7NUM)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/SUB7NUM)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/SUB7NUM)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/SUB7NUM)

Setter: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1943

#
[](#prerequisites-3)PREREQUISITES:

Dynamic programming

#
[](#problem-4)PROBLEM:

Kulyash has given you an array A of size N.

He defines the *subsequence-number* of a **non-empty** [subsequence](https://en.wikipedia.org/wiki/Subsequence)

S of array A as the number formed by the **concatenation** of all the elements of the subsequence S.

Find the count of non-empty subsequences of A having their *subsequence-numbers* **divisible** by 7. Since the answer can be huge, output it modulo 10^9 + 7.

For example: Consider A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. A subsequence S of A is [2, 5, 7, 10]. The *subsequence-number* of this subsequence is 25710.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Let dp[i][j] represent the number of subsequences in the prefix P_i of the array A which leave a remainder j when there subsequence-number is divided by 7.

Let D be the number of digits in the i^{th} element.

Initialize dp[0][0]=1 and rest as 0 (the empty subsequence, this will be subtracted from the answer later).

The dp transition is : for each j from 0 to 6

dp[i][j*10^{D} + A_i] = dp[i-1][j] + dp[i-1][j*10^{D}+A_i]

The answer is dp[N][0]-1

#
[](#explanation-6)EXPLANATION:

For each value of remainder, rem = 0\: to\: 6, let us calculate the number of subsequences in the prefix P_i (first i elements of the array A) which leave a remainder rem when their subsequence-number is divided by 7 . The subsequences till a particular index i leaving remainder rem include the subsequences calculated for prefix P_{i-1} for the same remainder rem.

Let D be the number of digits in the i^{th} element. Let the number of subsequences in P_{i-1} which leave a remainder R when their subsequence-number is divided by 7 be X, Then the remainder when the subsequence-number formed by combining the i^{th} element with an earlier subsequence from these X subsequences is divided by 7 is (R*10^D+A_i) %7.  Hence, we need to add X to the number of subsequences in P_i which leave a remainder (R*10^D+A_i)%7 when their subsequence-number is divided by 7.

This problem has both optimal substructure property and overlapping subproblems. These kind of problems can be solved using dynamic programming.

Let dp[i][j] represent the number of subsequences in the prefix P_i of the array A which leave a remainder j when there subsequence-number is divided by 7.

Initialize dp[0][0]=1 and rest as 0 (the empty subsequence, this will be subtracted from the answer later).

The dp transition is : for each j from 0 to 6

dp[i][j*10^{D} + A_i] = dp[i-1][j] + dp[i-1][j*10^{D}+A_i]

The answer is dp[N][0]-1

#
[](#time-complexity-7)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-8)SOLUTION:

Setter's solution
``#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
using namespace std;
int main(){
    ll T;
    cin >> T;
    while(T--){
        ll n;
        cin >> n;
        vector<ll>v(n);
        for(ll i=0;i<n;i++)cin >> v[i];
        vector<vector<ll>>dp(n,vector<ll>(7,0));
        vector<ll>mul(n,1);
        for(ll i=0;i<n;i++){
            ll x=v[i];
            while(x){
                mul[i]*=10;
                x/=10;
            }
        }
        dp[0][v[0]%7]=1;
        for(ll i=1;i<n;i++){
            for(ll k=0;k<7;k++)dp[i][k]=dp[i-1][k];
            for(ll k=0;k<7;k++)dp[i][(mul[i]*k+v[i])%7]=(dp[i][(mul[i]*k+v[i])%7]+dp[i-1][k])%MOD;
            dp[i][v[i]%7]=(dp[i][v[i]%7]+1)%MOD;
        }
        cout << dp[n-1][0] << endl;
    }
    return 0;
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
int dig(int n)
{
    int cnt = 0;
    while (n)
    {
        cnt++;
        n /= 10;
    }
    return cnt;
}
void sol(void)
{
    int n;
    cin >> n;
    vll v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    ll dp[n + 1][7], ans = 0;
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 0; i < n; i++)
    {
        int digits = dig(v[i]), tenpower = pow(10, digits);
        for (int j = 0; j < 7; j++)
        {
            dp[i + 1][(j * tenpower + v[i]) % 7] = dp[i][j] + dp[i][(j * tenpower + v[i]) % 7];
            dp[i + 1][j] %= mod;
        }
    }
    cout << (dp[n][0] - 1 + 2 * mod) % mod << '\n';
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
