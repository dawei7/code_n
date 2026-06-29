# Non-Divisor Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVCOL |
| Difficulty Rating | 1623 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [DIVCOL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/DIVCOL) |

---

## Problem Statement

You are given an integer $N$.
Your task is to find the **minimum** integer $C$ such that there exists an array $A$ of size $N$ satisfying:
- $1\le A_i \le C$;
- For distinct indices $x$ and $y$ where $x$ **divides** $y; \ A_x \neq A_y$.

You need to print the minimum value of $C$ as well as the array $A$. In case multiple arrays exist, you may print any one.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$.

---

## Output Format

For each test case, output two lines.
- The first line should contain a single integer $C$, the minimum integer for which array $A$ exists.
- The second line should contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the array $A$ satisfying given conditions.

In case multiple arrays satisfy the conditions, you may print any one.

---

## Constraints

- $1 \le T \le 10^3$
- $1 \le N \le 2 \cdot 10^5$
- The sum of $N$ does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
1
3
```

**Output**

```text
1
1
2
2 1 1
```

**Explanation**

**Test case $2$** : We needed to ensure:

- $A_1 \ne A_2$;
- $A_1 \ne A_3$

It can be verified that the given array $[2, 1, 1]$ does that with the minimum value of $C$ , i.e. $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIVCOL)

[Contest: Division 1](https://www.codechef.com/START143A/problems/DIVCOL)

[Contest: Division 2](https://www.codechef.com/START143B/problems/DIVCOL)

[Contest: Division 3](https://www.codechef.com/START143C/problems/DIVCOL)

[Contest: Division 4](https://www.codechef.com/START143D/problems/DIVCOL)

***Author:*** [everule1](https://www.codechef.com/users/everule1)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Color the integers from 1 to N in such a way that if x divides y, they have different colors.

Minimize the number of colors used.

# [](#explanation-5)EXPLANATION:

First, we find a lower bound on the answer.

Note that if we have a ‘chain’ of values x_1 \lt x_2 \lt \ldots \lt x_k such that x_i divides x_{i+1} for every 1 \leq i \lt k, then all these x_i must receive different colors, since for each pair of them, one of them will divide another.

The longest such chain is obtained via the powers of two, i.e, 1, 2, 4, 8, 16, \ldots

So, let k be the largest integer such that 2^k \leq N (specifically, k = \left \lfloor \log_2 N \right\rfloor ).

As per our initial observation, we definitely need *at least* k+1 colors to color all these powers of 2.

It turns out that this k+1 is also tight: it’s always possible to use exactly this many colors.

There are several different constructions possible, but here’s a rather simple one:

- Color 1 with the color 1.

- Color 2 and 3 with the color 2.

- Color 4, 5, 6, 7 with the color 3.

\vdots

More generally, color all the values from 2^i to 2^{i+1}-1 with the color i+1.

This clearly uses \left \lfloor \log_2 N \right\rfloor + 1 colors, which as we noted above is optimal.

Further, it’s also not hard to see that no two elements with the same color divide each other - after all, if x divides y and x\lt y, then y\geq 2x so x and y will definitely have different colors.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

void Solve()
{
    int n; cin >> n;

    vector <int> ans(n + 1, 1);
    for (int i = 2; i <= n; i++){
        if (ans[i] == 1){
            for (int j = i; j <= n; j += i){
                int copy = j;
                while (copy % i == 0){
                    copy /= i;
                    ans[j]++;
                }
            }
        }
    }

    int mx = *max_element(ans.begin(), ans.end());
    cout << mx << "\n";

    for (int i = 1; i <= n; i++){
        cout << ans[i] << " \n"[i == n];
    }
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Tester's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "../debug.h"
#else
#define dbg(...)
#endif

namespace mint_ns {
template<auto P>
struct Modular {
    using value_type = decltype(P);
    value_type value;

    Modular(long long k = 0) : value(norm(k)) {}

    friend Modular<P>& operator += (      Modular<P>& n, const Modular<P>& m) { n.value += m.value; if (n.value >= P) n.value -= P; return n; }
    friend Modular<P>  operator +  (const Modular<P>& n, const Modular<P>& m) { Modular<P> r = n; return r += m; }

    friend Modular<P>& operator -= (      Modular<P>& n, const Modular<P>& m) { n.value -= m.value; if (n.value < 0)  n.value += P; return n; }
    friend Modular<P>  operator -  (const Modular<P>& n, const Modular<P>& m) { Modular<P> r = n; return r -= m; }
    friend Modular<P>  operator -  (const Modular<P>& n)                      { return Modular<P>(-n.value); }

    friend Modular<P>& operator *= (      Modular<P>& n, const Modular<P>& m) { n.value = n.value * 1ll * m.value % P; return n; }
    friend Modular<P>  operator *  (const Modular<P>& n, const Modular<P>& m) { Modular<P> r = n; return r *= m; }

    friend Modular<P>& operator /= (      Modular<P>& n, const Modular<P>& m) { return n *= m.inv(); }
    friend Modular<P>  operator /  (const Modular<P>& n, const Modular<P>& m) { Modular<P> r = n; return r /= m; }

    Modular<P>& operator ++ (   ) { return *this += 1; }
    Modular<P>& operator -- (   ) { return *this -= 1; }
    Modular<P>  operator ++ (int) { Modular<P> r = *this; *this += 1; return r; }
    Modular<P>  operator -- (int) { Modular<P> r = *this; *this -= 1; return r; }

    friend bool operator == (const Modular<P>& n, const Modular<P>& m) { return n.value == m.value; }
    friend bool operator != (const Modular<P>& n, const Modular<P>& m) { return n.value != m.value; }

    explicit    operator       int() const { return value; }
    explicit    operator      bool() const { return value; }
    explicit    operator long long() const { return value; }

    constexpr static value_type mod()      { return     P; }

    value_type norm(long long k) {
        if (!(-P <= k && k < P)) k %= P;
        if (k < 0) k += P;
        return k;
    }

    Modular<P> inv() const {
        value_type a = value, b = P, x = 0, y = 1;
        while (a != 0) { value_type k = b / a; b -= k * a; x -= k * y; swap(a, b); swap(x, y); }
        return Modular<P>(x);
    }

    friend void __print(Modular<P> v) {
        cerr << v.value;
    }
};
template<auto P> Modular<P> pow(Modular<P> m, long long p) {
    Modular<P> r(1);
    while (p) {
        if (p & 1) r *= m;
        m *= m;
        p >>= 1;
    }
    return r;
}

template<auto P> ostream& operator << (ostream& o, const Modular<P>& m) { return o << m.value; }
template<auto P> istream& operator >> (istream& i,       Modular<P>& m) { long long k; i >> k; m.value = m.norm(k); return i; }
template<auto P> string   to_string(const Modular<P>& m) { return to_string(m.value); }

}
constexpr int mod = (int)1e9 + 7;
using mod_int = mint_ns::Modular<mod>;

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  const int NN = 2e5 + 2;
  vector<int> prime, P(NN, 1);
  for(int i = 2 ; i < NN ; ++i) if(P[i]) {
    prime.push_back(i);
    for(int j = 2 * i ; j < NN ; j += i)
      P[j] = 0;
  }
  auto __solve_testcase = [&](int test) {
    int N;  cin >> N;
    vector<int> color(N + 1); color[1] = 1;
    for(int k = 1 ; k <= N ; ++k) {
      for(int &j: prime) {
        if(j * k > N) break;
        color[j * k] = color[k] + 1;
      }
    }
    cout << *max_element(color.begin(), color.end()) << '\n';
    for(int i = 1 ; i <= N ; ++i)
      cout << color[i] << " \n"[i == N];
  };

  int NumTest = 1;
  cin >> NumTest;
  for(int testno = 1; testno <= NumTest ; ++testno) {
    __solve_testcase(testno);
  }

  return 0;
}

``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    print(len(bin(n)) - 2)
    for i in range(1, n+1): print(len(bin(i))-2)
``

</details>
