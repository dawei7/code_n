# Sum of Goodness

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEQGOODNESS |
| Difficulty Rating | 2167 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SEQGOODNESS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SEQGOODNESS) |

---

## Problem Statement

You are given an array $A = A_1, A_2, \ldots, A_N$ of size $N$.

Consider a subsequence $S = S_1, S_2, \ldots, S_M$ of $A$. Let us define the *Goodness* of subsequence $S$ as follows:

 - Sort the subsequence $S$ in non-decreasing order.
 - Then, the *Goodness* of subsequence $S$ is the number of indices such that $S_i = i,$ where
  $(1 \le i \le |S|).$

For example, suppose $A = [ 10, 3, 2, 5, 11, 3, 1, 12 ]$, and the subsequence is $S = [ 3, 2, 5, 3, 1 ]$. After sorting, $S = [ 1, 2, 3, 3, 5 ]$, and so the *Goodness*  of $S$ is $4$.

Consider all the $2^N - 1$ possible non-empty subsequences of array $A$, and find the sum of all their *Goodness*.

Since the answer can be large, output the answer modulo $10^9 + 7.$

**Note:** A sequence $S$ is a *subsequence* of array $A$ if $S$ can be obtained from $A$ by deletion of several (possibly, zero) elements. For example, $[3,1]$ is a subsequence of $[3,2,1]$ and $[4,3,1]$, but not a subsequence of $[1,3,3,7]$ and $[3,10,4]$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers, $A_1, A_2, A_3,..., A_N.$

---

## Output Format

For each test case, output the answer modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N $ for each $1 \leq i \leq N$.
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
2
1 2
5
3 2 5 5 3
4
1 1 2 1
6
6 4 5 2 3 1
```

**Output**

```text
3
5
17
63
```

**Explanation**

**Testcase 1:** The given array is $[1, 2]$. There are 3 possible non-empty subsequences:
- $[1]$. The *Goodness* of this subsequence is $1$, since $S_1 = 1$.
- $[2]$. The *Goodness* of this subsequence is $0$.
- $[1, 2]$. The *Goodness* of this subsequence is $2$, since $S_1 = 1$ and $S_2 = 2$.

Thus the total sum is $1 + 0 + 2 = 3$, which is the answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
3 2 5 5 3
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
4
1 1 2 1
```

**Output for this case**

```text
17
```



#### Test case 4

**Input for this case**

```text
6
6 4 5 2 3 1
```

**Output for this case**

```text
63
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SEQGOODNESS)

[Contest: Division 1](https://www.codechef.com/START90A/problems/SEQGOODNESS)

[Contest: Division 2](https://www.codechef.com/START90B/problems/SEQGOODNESS)

[Contest: Division 3](https://www.codechef.com/START90C/problems/SEQGOODNESS)

[Contest: Division 4](https://www.codechef.com/START90D/problems/SEQGOODNESS)

***Author:*** [prince_patel_8](https://www.codechef.com/users/prince_patel_8)

***Tester:*** [udhav2003](https://www.codechef.com/users/udhav2003)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2167

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics and computing [binomial coefficients](https://cp-algorithms.com/combinatorics/binomial-coefficients.html#binomial-coefficient-for-small-n), sorting

#
[](#problem-4)PROBLEM:

The *goodness* of a sequence S is defined as follows:

- Sort S in increasing order;

- Then, its goodness is the number of indices i such that S_i = i.

Given an array A, find the sum of goodness across all its subsequences.

#
[](#explanation-5)EXPLANATION:

First, let’s try to solve this problem for when all the elements of A are **distinct**.

For this, we can use the technique of looking at *contribution*.

That is, instead of finding the sum of goodness across all sequences, we’ll find for each element the number of sequences it contributes to the goodness of.

Since all the elements are distinct, this is not too hard.

Let’s consider an element x in A, we want to count the number of subsequences of A such that S_x = x.

For this:

- There should be exactly x-1 elements less than x, to be placed at indices 1, 2, \ldots, x-1.

- There can be any number of elements \gt x, since they don’t affect the position of x in the sorted subsequence.

This then turns into a rather simply counting problem:

- If there are L elements less than x in A, we can choose x-1 of them in \binom{L}{x-1} ways.

- If there are R elements greater than x in A, we can choose any subset of them freely in 2^R ways.

- Multiplying them together, we get \binom{L}{x-1} \cdot 2^R ways.

Finding L and R isn’t very hard.

Let’s sort the array A, then if A_i = x in this sorted array we have L = i-1 and R = N-i.

So, after sorting, we can solve the problem in \mathcal{O}(N): for each index i, add \binom{i-1}{A_i-1} \cdot 2^{N-i} to the answer.

Computing binomial coefficients quickly can be done by precomputing factorials, for example as described [here](https://cp-algorithms.com/combinatorics/binomial-coefficients.html#binomial-coefficient-for-small-n).

Now, what happens if the elements aren’t necessarily distinct?

In fact, the exact same solution works!

That is, the answer is simply

\sum_{i=1}^N \binom{i-1}{A_i-1}\cdot 2^{N-i}

after A is sorted.

Proof

When elements aren’t distinct, the only real issue that we face is that which element is placed at which position in sorted order isn’t uniquely determined; which might throw off our contribution counting.

For example, the subsequence [1, 1] should be counted against exactly one of the ones; not both of them.

One way to resolve this ambiguity is to uniquely define an order among equal elements as well.

For example, if we have k ones in A, we can label them [1_1, 1_2, 1_3, \ldots, 1_k], and we can say that if 1_i and 1_j are both chosen in a subsequence (where i \lt j), then 1_i will be placed before 1_j in sorted order.

This immediately resolves the ambiguity, since if S_i = i for some subsequence, it will contribute only towards one *specific* i (depending on the labels of the i's chosen for this subsequence).

Now, note that because we have a uniquely defined order among all the elements, they’re all essentially distinct!

So, our initial solution, where we treated elements as distinct, works here too.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>

using namespace std;

#define int long long int

const int N = 2e5 + 10;
vector<int> fact(N);
vector<int> inv(N);
const int mod = (int)1e9 + 7;

int power(int x, int y, int p){
    int res = 1;
    x = x % p;
    if (x == 0)
        return 0;
    while (y > 0){
        if (y & 1)
            res = (res * x) % p;
        y = y >> 1;
        x = (x * x) % p;
    }
    return res;
}
void inti() {
    fact[0] = 1;
    for (int i = 1; i < N; i++){
        fact[i] = (fact[i - 1] % mod * i % mod) % mod;
    }
    for (int i = 0; i < N; i++){
        inv[i] = power(fact[i], mod - 2, mod);
    }
}
int nCr(int n, int r){
    return (fact[n] % mod * inv[n - r] % mod * inv[r] % mod) % mod;
}

int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  inti();
  cin >> tt;
  assert(tt <= 100000);
  int sum = 0;
  while(tt--) {
    int n;
    cin >> n;
    sum += n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) {
      cin >> a[i];
      assert(a[i] <= n);
    }
    int ans = 0;
    sort(a.begin(), a.end());
    for(int i = 0; i < n; i++) {
      if(a[i] <= i + 1) {
        int right = power(2, n - i - 1, mod);
        int left = nCr(i, a[i] - 1);
        ans += (left * right) % mod;
        ans %= mod;
      }
    }
    assert(ans < mod);
    cout << ans << '\n';
  }
  assert(sum <= 200000);
}
``

Tester's code (C++)
``#pragma GCC optimisation("O3")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimize("Ofast,unroll-loops")
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define NUM1 1000000007LL
#define all(a) a.begin(), a.end()
#define beg(a) a.begin(), a.begin()
#define sq(a) ((a)*(a))
#define NUM2 998244353LL
#define MOD NUM1
#define LMOD 1000000006LL
#define fi first
#define se second
typedef long double ld;
const ll MAX = 100010;
const ll MAX2 = MAX;
const ll large = 1e18;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

//public free to use template by bqi343 on github
struct mi {
 	int v; explicit operator int() const { return v; }
	mi():v(0) {}
	mi(ll _v):v(int(_v%MOD)) { v += (v<0)*MOD; }
};
mi& operator+=(mi& a, mi b) {
	if ((a.v += b.v) >= MOD) a.v -= MOD;
	return a; }
mi& operator-=(mi& a, mi b) {
	if ((a.v -= b.v) < 0) a.v += MOD;
	return a; }
mi operator+(mi a, mi b) { return a += b; }
mi operator-(mi a, mi b) { return a -= b; }
mi operator*(mi a, mi b) { return mi((ll)a.v*b.v); }
mi& operator*=(mi& a, mi b) { return a = a*b; }
mi pow(mi a, ll p) { assert(p >= 0); // won't work for negative p
	return p==0?1:pow(a*a,p/2)*(p&1?a:1); }
mi inv(mi a) { assert(a.v != 0); return pow(a,MOD-2); }
mi operator/(mi a, mi b) { return a*inv(b); }
bool operator==(mi a, mi b) { return a.v == b.v; }
bool operator==(mi a, int b){ return a.v == b;}
ostream& operator<<(ostream& os, const mi& val)
{
    os << (int) val;
    return os;
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector<mi> fact(MAX);
    fact[0] = 1;
    for(int i = 1; i < MAX; i++) fact[i] = i*fact[i - 1];
    vector<mi> invfact(MAX);
    invfact.back() = inv(fact.back());
    for(int i = MAX - 2; i >= 0; i--) invfact[i] = (i + 1)*invfact[i + 1];
    auto ncr = [&](int n, int r){
        if(n < r || r < 0) return mi(0);
        return fact[n]*invfact[r]*invfact[n - r];
    };
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> a(n);
        for(auto& x: a) cin >> x;
        sort(all(a));
        mi val = 0;
        for(int i = 0; i < n; i++){
            val += ncr(i, a[i] - 1)*pow(mi(2), n - i - 1);
        }
        cout << val << '\n';
    }
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
MX = 100005
fac = [1]
invfac = [1]
for i in range(1, MX):
	fac.append(i * fac[i-1] % mod)
	invfac.append(pow(fac[-1], mod-2, mod))
def C(n, r):
	if n < r or r < 0: return 0
	return fac[n] * invfac[r] % mod * invfac[n-r] % mod

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        # choose a[i]-1 elements from the left, and anything from the right
        rt = pow(2, n-i-1, mod)
        lt = C(i, a[i]-1)
        ans += lt * rt % mod
    print(ans % mod)
``

</details>
