# Squarified

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SQUAR |
| Difficulty Rating | 2470 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SQUAR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SQUAR) |

---

## Problem Statement

You are given an array $A$ of length $N$.
An array $B$ is considered *squarified*, if:
- The product of the elements in any even-length [subsequence](https://en.wikipedia.org/wiki/Subsequence) of $B$ is a [perfect square](https://en.wikipedia.org/wiki/Perfect_square), and;
- The product of the elements in any odd-length subsequence of $B$ is **not** a perfect square.

Your task is to find the length of the **longest subsequence** of $A$ which is *squarified*.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line, the length of the **longest subsequence** of $A$ which is `squarified`.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^7$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
7 18 8 10
5
27 8 12 16 12
2
9 1
```

**Output**

```text
2
3
0
```

**Explanation**

**Test Case $1$:** $[18,8]$ is the longest squarified subsequence of the array.
- Even length subsequence is $[18, 8]$. Here, $18\cdot 8 = 144 = 12^2$.
- Odd length subsequence are $[18]$ and $[8]$. None of these are perfect squares.

**Test Case $2$:** $[27,12,12]$ is the longest squarified subsequence of the array.
- Even length subsequences are $[27,12]$ and $[12,12]$ with products $324$ and $144$ respectively. Both of these are perfect squares.
- Odd length subsequences are $[27],[12],$ and $[27,12,12]$ with products $27,12$ and $3888$. None of these are perfect squares.

**Test Case $3$:** There is no squarified subsequence present, hence answer is 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
7 18 8 10
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
27 8 12 16 12
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
2
9 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SQUAR)

[Contest: Division 1](https://www.codechef.com/START103A/problems/SQUAR)

[Contest: Division 2](https://www.codechef.com/START103B/problems/SQUAR)

[Contest: Division 3](https://www.codechef.com/START103C/problems/SQUAR)

[Contest: Division 4](https://www.codechef.com/START103D/problems/SQUAR)

***Author:*** [ro27](https://www.codechef.com/users/ro27)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Fast prime factorization using the [sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)

# [](#problem-4)PROBLEM:

Given an array A, find the length of its longest subsequence B such that:

- The product of elements of each even-length subsequence of B is a perfect square; and

- The product of elements of each odd-length subsequence of B is *not* a perfect square.

# [](#explanation-5)EXPLANATION:

First, let’s analyze the structure of a valid sequence B.

- The odd-length condition tells us that every element of B should be not a perfect square.

- The even-length condition tells us that the product of every pair of elements of B should be a perfect square.

Further, these two conditions are enough to guarantee that the entire subsequence is valid, since:

- Any even-length subsequence can be broken up into several pairs of elements, each of whose product is a square — and clearly, the product of several perfect squares is also a perfect square.

- The product of a perfect square with a non-square can never be a square; so the odd condition is also satisfied.

So, let’s try to find the longest subsequence we can create that satisfies both conditions.

The first one is easy: we can’t have squares, so simply discard all squares from A and work with the remaining elements.

Now, we only have to deal with the second condition, i.e, each pair of elements should multiply to a perfect square.

Given two integers x and y, when is their product (x\cdot y) a perfect square?

Answer

Let’s look at the prime factorizations of x and y.

Suppose

x = p_1^{a_1}p_2^{a_2}\ldots p_k^{a_k} \\
y = p_1^{b_1}p_2^{b_2}\ldots p_k^{b_k}

where the p_i are the primes that occur in at least one of x and y (for convenience, we allow a_i and b_i to be 0 as well).

The prime factorization of their product is then

x\cdot y = p_1^{a_1 + b_1}p_2^{a_2 + b_2}\ldots p_k^{a_k + b_k}

For this to be a square, *every* exponent must be even; in other words, for each i, a_i and b_i should have the same parity.

Looking at it differently, this means that x and y should have the exact same set of prime factors with odd powers.

That is, if x_s denotes the product of prime factors of x that have an odd power, and y_s is the same for y, then we must have x_s = y_s.

Note that x_s and y_s are what is known as the [*squarefree*](https://en.wikipedia.org/wiki/Square-free_integer) parts of x and y.

We now have a pretty simple condition: x and y can be in the same subsequence if and only if their squarefree parts are equal.

So, *every* element of the subsequence must have the same squarefree part — it’s not hard to see that this condition is both necessary and sufficient.

This brings us to a rather straightforward solution: replace each element by its squarefree part, then count the maximum number of occurrences of some element of the array.

Finding the squarefree part of an integer requires knowing its prime factorization — this can be done quickly using a modified sieve of Eratosthenes:

- First, run a sieve and precompute one prime factor of every integer upto 10^7; call this \text{prm}[x].

- Then, to prime factorize x, repeat the following:

- If x = 1, stop.

- Otherwise, let p = \text{prm}[x]. Repeatedly divide p out of x while it’s possible; which also tells you the parity of its power.

- Multiply this prime to the squarefree part if necessary; then go back to the first step.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log M) per testcase with \mathcal{O}(M\log \log M) precomputation, where M = 10^7.

# [](#code-7)CODE:

Author's code (C++)
``#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

template<class T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
// order_of_key(a)  -> gives index of the element(number of elements smaller than a)
// find_by_order(a) -> gives the element at index a
#define accelerate ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int        long long int
#define ld         long double
#define mod1       998244353
#define endl       "\n"
#define ff         first
#define ss         second
#define all(x)     (x).begin(),(x).end()
#define ra(arr,n)  vector<int> arr(n);for(int in = 0; in < n; in++) {cin >> arr[in];}

const int mod = 1e9 + 7;
const int inf = 1e18;
int MOD(int x) {int a1 = (x % mod); if (a1 < 0) {a1 += mod;} return a1;}
int power( int a,  int b) {
    int p = 1; while (b > 0) {if (b & 1)p = (p % mod * a % mod) % mod; a = (a % mod * a) % mod  ; b >>= 1;}
    return p % mod;
}
const int MAXN = 1e7;
int spf[MAXN+5];

void sieve()
{
    spf[1] = 1;
    for (int i = 2; i < MAXN; i++)spf[i] = i;
    for (int i = 4; i < MAXN; i += 2)spf[i] = 2;
    for (int i = 3; i * i < MAXN; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j < MAXN; j += i)
                if (spf[j] == j)
                    spf[j] = i;
        }
    }
}
void lessgoo()
{
    int n;
    cin >> n;
    ra(arr, n);
    int ans = 0;
    map<int, int>k;
    for (int i = 0; i < n; i++) {
        int x = arr[i];
        int prod = 1;
        map<int, int>mp;
        while (x != 1) {
            int z = spf[x];
            x = x / z;
            mp[z]++;
            if (mp[z] % 2 != 0)prod = prod * z;
            else prod = prod / z;
        }

        k[prod]++;
        if (prod != 1)ans = max(ans, k[prod]);
    }
    cout << ans << endl;

}

signed main()
{
    accelerate;

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int test = 1;
    cin >> test;
    sieve();
    for (int tcase = 1; tcase <= test; tcase++)
    {
        // cout << "Case #" << tcase << ": ";

        lessgoo();

    }
    return 0;
}
``

Tester's code (C++)
``#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

template<class T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
// order_of_key(a)  -> gives index of the element(number of elements smaller than a)
// find_by_order(a) -> gives the element at index a
#define accelerate ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int        long long int
#define ld         long double
#define mod1       998244353
#define endl       "\n"
#define ff         first
#define ss         second
#define all(x)     (x).begin(),(x).end()
#define ra(arr,n)  vector<int> arr(n);for(int in = 0; in < n; in++) {cin >> arr[in];}

const int mod = 1e9 + 7;
const int inf = 1e18;
int MOD(int x) {int a1 = (x % mod); if (a1 < 0) {a1 += mod;} return a1;}
int power( int a,  int b) {
    int p = 1; while (b > 0) {if (b & 1)p = (p % mod * a % mod) % mod; a = (a % mod * a) % mod  ; b >>= 1;}
    return p % mod;
}
const int MAXN = 1e7;
int spf[MAXN];

void sieve()
{
    spf[1] = 1;
    for (int i = 2; i < MAXN; i++)spf[i] = i;
    for (int i = 4; i < MAXN; i += 2)spf[i] = 2;
    for (int i = 3; i * i < MAXN; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j < MAXN; j += i)
                if (spf[j] == j)
                    spf[j] = i;
        }
    }
}
void lessgoo()
{
    int n;
    cin >> n;
    ra(arr, n);
    int ans = 0;
    map<int, int>k;
    for (int i = 0; i < n; i++) {
        int x = arr[i];
        int prod = 1;
        map<int, int>mp;
        while (x != 1) {
            int z = spf[x];
            x = x / z;
            mp[z]++;
            if (mp[z] % 2 != 0)prod = prod * z;
            else prod = prod / z;
        }

        k[prod]++;
        if (prod != 1)ans = max(ans, k[prod]);
    }
    cout << ans << endl;

}

signed main()
{
    accelerate;

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int test = 1;
    cin >> test;
    sieve();
    for (int tcase = 1; tcase <= test; tcase++)
    {
        // cout << "Case #" << tcase << ": ";

        lessgoo();

    }
    return 0;
}
``

Editorialist's code (Python)
``MAXN = 10**7 + 10
prm = [i for i in range(MAXN)]
for i in range(2, MAXN):
    if i*i >= MAXN: break
    if prm[i] < i: continue
    for j in range(i*i, MAXN, i): prm[j] = i

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    freq[1] = 0
    for x in a:
        sqf = 1
        while x > 1:
            p, ct = prm[x], 0
            while x%p == 0:
                x //= p
                ct ^= 1
            if ct == 1: sqf *= p
        if sqf == 1: continue
        if sqf not in freq: freq[sqf] = 0
        freq[sqf] += 1
    print(max(freq.values()))
``

</details>
