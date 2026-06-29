# Chef Product

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFPRODUCT |
| Difficulty Rating | 1658 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHEFPRODUCT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHEFPRODUCT) |

---

## Problem Statement

Chef has a special interest in studying sets of integers.

Given an integer $N$, he defines a *good-set* as a set of **distinct non-negative** integers, such that:
- The sum of the integers in the set is equal to $N$.
- The product of each non-empty subset of the set is **odd**.

Determine the number of **distinct sizes** of *good-set* that can be formed.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one integer $N$.

---

## Output Format

For each test case, output on a new line, the number of **distinct sizes** of *good-set* that can be formed.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
2
4
18
```

**Output**

```text
1
2
```

**Explanation**

**Test case $1$**: The only **good-set** is $\{1, 3\}$.

**Test case $2$**: The **good-sets** are $\{1,17\}$, $\{3,15\}$, $\{5,13\}$, $\{7,11\}$ and $\{1, 3, 5, 9\}$. Thus, there are four sets of size $2$ and one set of size $4$, giving $2$ distinct sizes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
18
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFPRODUCT)

[Contest: Division 1](https://www.codechef.com/START116A/problems/CHEFPRODUCT)

[Contest: Division 2](https://www.codechef.com/START116B/problems/CHEFPRODUCT)

[Contest: Division 3](https://www.codechef.com/START116C/problems/CHEFPRODUCT)

[Contest: Division 4](https://www.codechef.com/START116D/problems/CHEFPRODUCT)

***Author:*** [souradeep1999](https://www.codechef.com/users/souradeep1999)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Binary search

# [](#problem-4)PROBLEM:

You’re given an integer N.

Find the number of distinct sizes of *good sets*, where S is a good set of integers if:

- S consists of distinct positive integers whose sum is N; and

- Every non-empty subset of S has odd product.

# [](#explanation-5)EXPLANATION:

First, note that the second condition forces every element of a good set to be odd (by considering subsets of size 1), and the product of odd numbers remains odd so we’re free to choose any odd numbers we like.

So, what we really want to do is count the number of integers K such that **exactly** K distinct positive odd integers sum up to N.

Let’s fix some K and check if this is possible.

The smallest sum we can get is the sum of the K smallest odd numbers, i.e, 1 + 3 + 5 + \ldots + (2K-1), which equals K^2.

So, K^2 \leq N should hold.

Now, if K^2 \lt N, we need to increase some of these odd numbers to reach N.

However, notice that no matter how we increase things, since they’re all odd, the *parity* of the sum won’t change (i.e the sum will be odd if K is odd and even otherwise).

In particular, if N and K have different parities (one is even and the other is odd), it’s not possible to ever reach a sum of N.

On the other hand, if N and K have the same parity, it’s always possible: just make the last number 2K-1 + (N - K^2), and the overall sum becomes N.

Note that 2K-1 + (N-K^2) is itself an odd number, because (N-K^2) is even in this case.

All-in-all, K distinct positive odd numbers can sum to N if and only if:

- K^2 \leq N; and

- K and N have the same parity.

So,

- If N is even, we want to count the number of even numbers that are \leq \sqrt{N}.

- If N is odd, we want to count the number of odd numbers that are \leq \sqrt{N}

This can be done in \mathcal{O}(\log N) using binary search, or you can use your language’s library which likely has a `sqrt` function.

### [](#a-note-on-precision-6)A Note on Precision

If you use your language’s inbuilt `sqrt` function, there’s a chance you may receive the WA verdict even with a “correct” algorithm — this is because of precision errors.

For instance, in `C++`, using `sqrt` will give you a wrong answer when

N = (2^{29}-1)^2 - 2=288230375077969919

This is because the square root of N is just slightly below 2^{29}-1, and so must be rounded down to 2^{29}-2; but a lack of precision causes it to round towards 2^{29}-1 instead.

There are a couple of ways to fix this:

- Use binary search to compute the square root, as mentioned above. This avoids working with floating-point values entirely.

- Alternately, you can manually ‘fix’ the imprecise values since they won’t be far off from the actual values.

For example, if you have `int s = sqrt(N);`, the actual value you want is either `s-1, s, ` or `s+1`.

So, just check the three of those to see which of their squares is \leq N.

- In C++ in particular, the `sqrtl` function is more precise than plain `sqrt`.

# [](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(\log N) per testcase.

# [](#code-8)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define int long long int
#define ordered_set tree<int, nuint_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
mt19937 rng(std::chrono::duration_cast<std::chrono::nanoseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count());
#define mp make_pair
#define pb push_back
#define F first
#define S second
const int N=100005;
#define M 1000000007
#define BINF 1e16
#define init(arr,val) memset(arr,val,sizeof(arr))
#define MAXN 10000005
#define deb(xx) cout << #xx << " " << xx << "\n";
const int LG = 22;

int getSqrt(int x) {
    int lo = 0, hi = 1e9, c = 0;
    while(lo <= hi) {
        int mid = (lo + hi) / 2;
        if((mid * mid) <= x) {
            c = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return c;
}

void solve() {

    int n;
    cin >> n;

    int x = getSqrt(n);
    if(n % 2 != x % 2) {
        x = x - 1;
    }

    int c = (x + 1) / 2;

    cout << c << endl;

}

#undef int
int main() {
#define int long long int
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("optput.txt", "w", stdout);
#endif

    int T;
    cin >> T;

    for(int tc = 1; tc <= T; tc++){
        // cout << "Case #" << tc << ": ";
        solve();
    }

return 0;

}
``

Editorialist's code (Python)
``def isqrt(x):
    lo, hi = 0, 10**9
    while lo < hi:
        mid = (lo + hi + 1)//2
        if mid*mid <= x: lo = mid
        else: hi = mid - 1
    return lo

for _ in range(int(input())):
    n = int(input())
    mx = isqrt(n)
    if n%2 == 0: print(mx//2)
    else: print((mx+1)//2)
``

</details>
