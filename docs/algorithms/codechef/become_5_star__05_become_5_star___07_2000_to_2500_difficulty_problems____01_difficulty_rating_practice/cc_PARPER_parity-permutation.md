# Parity Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PARPER |
| Difficulty Rating | 2066 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [PARPER](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/PARPER) |

---

## Problem Statement

You are given an array $A$ of length $N$ containing **distinct** integers and an integer $K$ (either $0$ or $1$).

Your task is to find the total number of permutations of array $A$ such that for **all** pairs $(i, j)$
with $1 \leq i \lt j \leq N$, and $(i + j)$ being an **odd** number:
- $(A_i+A_j) \% 2$ $= K$

You should output the count of such permutations modulo $10^9+7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, as mentioned in statement.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line, the total number of permutations of array $A$ satisfying the conditions, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $0 \leq K \leq 1$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5 0
6 10 1 4 8
4 0
17 13 21 3
3 1
1 2 3
```

**Output**

```text
0
24
2
```

**Explanation**

**Test Case $1$:** There is no permutation that satisfies the required conditions.

**Test Case $2$:** All the permutations of the array satisfy the required conditions.

**Test Case $3$:** Two permutations satisfy the conditions. They are:
- $[1,2,3]$: The pairs under consideration are $(1, 2)$ and $(2, 3)$. Here $(A_1+A_2) \% 2 = 1 = K$. Similarly $(A_2+A_3) \% 2 = 1 = K$.
- $[3,2,1]$ The pairs under consideration are $(1, 2)$ and $(2, 3)$. Here $(A_1+A_2) \% 2 = 1 = K$. Similarly $(A_2+A_3) \% 2 = 1 = K$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 0
6 10 1 4 8
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 0
17 13 21 3
```

**Output for this case**

```text
24
```



#### Test case 3

**Input for this case**

```text
3 1
1 2 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PARPER)

[Contest: Division 1](https://www.codechef.com/START102A/problems/PARPER)

[Contest: Division 2](https://www.codechef.com/START102B/problems/PARPER)

[Contest: Division 3](https://www.codechef.com/START102C/problems/PARPER)

[Contest: Division 4](https://www.codechef.com/START102D/problems/PARPER)

***Author:*** [ro27](https://www.codechef.com/users/ro27)

***Tester:*** [mridulahi](https://www.codechef.com/users/mridulahi)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2066

# [](#prerequisites-3)PREREQUISITES:

Basic combinatorics

# [](#problem-4)PROBLEM:

You’re given an array A containing distinct integers and an integer K.

Find the number of permutations of A such that (A_i + A_j) \equiv K \pmod{2} for all pairs (i, j) such that i+j is odd.

# [](#explanation-5)EXPLANATION:

First, note that (i+j) being odd means that one of i and j must be odd, and the other must be even.

Let’s look at K = 0 and K = 1 separately.

If K = 0, then we want (A_i + A_j) to be even for all valid pairs (i, j).

This means A_i and A_j should have the same parity.

So,

- Let’s fix the parity of A_1; either even or odd.

- Then, A_2, A_4, A_6 should all have the same parity as A_1, since their sum must be even.

- But then, A_3, A_5, A_7, \ldots must also all have the same parity as A_2 (and hence, as A_1).

- This means that *all* the elements of A must have the same parity.

- If this condition holds, then clearly the order of elements doesn’t matter all, and so the answer is N!

- Otherwise, no valid rearrangement exists, and the answer is 0.

Next, let’s look at K = 1.

In this case, (A_i + A_j) must be odd for every valid (i, j) pair. So,

- Once again, let’s fix the parity of A_1.

- Then, the parity of A_2, A_4, ,A_6, \ldots must be the *opposite* of the parity of A_1.

- Similarly, the parity of A_3, A_5, A_7, \ldots must the *same* as that of A_1.

- If this is satisfied, then once again the order of elements (within even and odd positions) doesn’t matter at all.

So, suppose we have E even elements and O odd elements. Then,

- If A_1 is to be even, then all of A_1, A_3, A_5, \ldots must be even: in particular, we want E = \left\lceil \frac{N}{2}\right\rceil.

This fixes O = \left\lfloor \frac{N}{2}\right\rfloor

If this condition holds, then the even and odd elements can be freely permuted within themselves; for a total of E!\cdot O! ways; otherwise there are 0 ways.

- You can do a similar analysis for when A_1 is odd, and once again you’ll see that there are either E!\cdot O! ways (when O = \left\lceil \frac{N}{2}\right\rceil) and 0 ways otherwise.

The sum of the answers of the two cases above gives us the final answer.

Factorials can be computed easily in \mathcal{O}(N) time.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

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
    int p = 1; while (b > 0) {if (b & 1)p = (p * a); a = (a * a)  ; b >>= 1;}
    return p;
}
int N = 1e5;
vector<int>mp(N);

void lessgoo()
{
    int n, k;
    cin >> n >> k;
    ra(arr, n);
    int even = 0, odd = 0;
    for (auto x : arr) {
        if (x % 2 == 0)even++;

    }
    odd = n - even;
    if (k == 0) {
        if (even == 0 || odd == 0) {
            cout << mp[n] % mod << endl;
        } else {
            cout << 0 << endl;
        }
    } else {
        if (abs(even - odd) <= 1) {
            int ans = mp[even] % mod;
            ans = (ans * mp[odd]) % mod;
            ans = ans % mod;
            if (even == odd)ans = (ans * 2) % mod;
            cout << ans % mod << endl;

        } else {
            cout << 0 << endl;
        }
    }

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
    int ans = 1;
    mp[0] = 1;
    for (int i = 1; i <= N; i++) {
        mp[i]=(i*mp[i-1])%mod;
        mp[i]%=mod;

    }

    for (int tcase = 1; tcase <= test; tcase++)
    {
        // cout << "Case #" << tcase << ": ";

        lessgoo();

    }
    return 0;
}
``

Tester's code (C++)
``//#pragma GCC optimize("O3")
//#pragma GCC optimize("Ofast")
//#pragma GCC optimize("unroll-loops")
//#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

struct custom_hash {
        static uint64_t splitmix64(uint64_t x) {
                // http://xorshift.di.unimi.it/splitmix64.c
                x += 0x9e3779b97f4a7c15;
                x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
                x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
                return x ^ (x >> 31);
        }

        size_t operator()(uint64_t x) const {
                static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
                return splitmix64(x + FIXED_RANDOM);
        }
};
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<typename T>
T rand(T a, T b){
    return uniform_int_distribution<T>(a, b)(rng);
}

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<pair<int,int>, null_type, less<pair<int,int>>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<int> vi;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define all(x) begin(x), end(x)
#define sz(x) static_cast<int>((x).size())
#define int long long

const ll mod = 1e9 + 7;
const ll INF = 1e18;

/* ----------------------------------------------------- GO DOWN ---------------------------------------------------------------------- */

int norm (int x) {
        if (x < 0) {
                x += mod;
        }
        if (x >= mod) {
                x -= mod;
        }
        return x;
}
template<class T>
T power(T a, int b) {
        T res = 1;
        for (; b; b /= 2, a *= a) {
                if (b % 2) {
                res *= a;
                }
        }
        return res;
}
struct Z {
        int x;
        Z(int x = 0) : x(norm(x)) {}
        int val() const {
                return x;
        }
        Z operator-() const {
                return Z(norm(mod - x));
        }
        Z inv() const {
                assert(x != 0);
                return power(*this, mod - 2);
        }
        Z &operator*=(const Z &rhs) {
                x = x * rhs.x % mod;
                return *this;
        }
        Z &operator+=(const Z &rhs) {
                x = norm(x + rhs.x);
                return *this;
        }
        Z &operator-=(const Z &rhs) {
                x = norm(x - rhs.x);
                return *this;
        }
        Z &operator/=(const Z &rhs) {
                return *this *= rhs.inv();
        }
        friend Z operator*(const Z &lhs, const Z &rhs) {
                Z res = lhs;
                res *= rhs;
                return res;
        }
        friend Z operator+(const Z &lhs, const Z &rhs) {
                Z res = lhs;
                res += rhs;
                return res;
        }
        friend Z operator-(const Z &lhs, const Z &rhs) {
                Z res = lhs;
                res -= rhs;
                return res;
        }
        friend Z operator/(const Z &lhs, const Z &rhs) {
                Z res = lhs;
                res /= rhs;
                return res;
        }
        friend std::istream &operator>>(std::istream &is, Z &a) {
                int v;
                is >> v;
                a = Z(v);
                return is;
        }
        friend std::ostream &operator<<(std::ostream &os, const Z &a) {
                return os << a.val();
        }
};

const int maxn = 1e5 + 1;
Z fact[maxn];
Z ifact[maxn];
Z C (int n, int r) {
        return fact[n] * ifact[r] * ifact[n - r];
}

signed main() {

        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        fact[0] = 1;
        for (int i = 1; i < maxn; i++) fact[i] = fact[i - 1] * i;
        ifact[maxn - 1] = Z(1) / fact[maxn - 1];
        for (int i = maxn - 2; i >= 0; i--) ifact[i] = ifact[i + 1] * (i + 1);

        int t;
        cin >> t;

        while (t--) {
                int n, k;
                cin >> n >> k;
                int a[n];
                int c[2] = {0};
                for (int i = 0; i < n; i++) {
                        cin >> a[i];
                        c[a[i] & 1]++;
                }
                if (k == 0) {
                        if (c[0] != 0 && c[1] != 0) cout << 0 << "\n";
                        else cout << fact[n] << "\n";
                }
                else {
                        if (abs(c[0] - c[1]) == 0) cout << Z(2) * fact[n / 2] * fact[n / 2] << "\n";
                        else if (abs(c[0] - c[1]) == 1) cout << fact[n / 2] * fact[(n + 1) / 2] << "\n";
                        else cout << 0 << "\n";
                }
        }

}
``

Editorialist's code (Python)
``mod = 10**9 + 7

def fac(n):
    res = 1
    for i in range(2, n+1): res = res * i % mod
    return res

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    odds, evens = 0, 0
    for x in a:
        odds += x%2
        evens += (x+1)%2

    if k == 1:
        if abs(evens - odds) > 1: print(0)
        else:
            ans = fac(evens) * fac(odds) % mod
            if n%2 == 0: ans = ans * 2 % mod
            print(ans)
    else:
        if evens == 0 or odds == 0: print(fac(n))
        else: print(0)
``

</details>
