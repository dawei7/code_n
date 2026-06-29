# Chef and Asteroids

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROIDS |
| Difficulty Rating | 1997 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [ROIDS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/ROIDS) |

---

## Problem Statement

Chef enjoys playing `Among Us` with the other Chefs in the kitchen. However, he struggles with the asteroids task.

The task consists of $N$ asteroids where the coordinates of the $i^{th}$ asteroid are $(X_i, Y_i)$.
In one second, each non-destroyed asteroid moves to the **left** by $1$ unit.
Formally, if an asteroid's current position is $(X, Y)$, then, after $1$ second, it moves to the position $(X − 1, Y)$.
Note that, an asteroid can move to a negative $X$ coordinate after some time.

The *optimal strategy* to play the game is to choose a non-destroyed asteroid having **minimum** $X$ coordinate, and destroy it.
If multiple asteroids have minimum $X$ coordinate, any one of them can be destroyed first.

However, Chef likes to take his chances. Each second, he chooses a non-destroyed asteroid, **uniformly at random** and destroys it.

Find the probability that Chef's strategy of randomly destroying the asteroids is same as the *optimal strategy*.

The probability can be written in the form of $\frac{P}{Q}$ such that $Q$ is not divisible by $1000000007$. Output the value of $P \cdot Q^{-1}$ mod $1000000007$.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of asteroids.
- The next $N$ lines describe the asteroids. The $i^{th}$ of these $N$ lines contain two space-separated integers $X_i$ and $Y_i$, denoting the initial position of the $i^{th}$ asteroid.

---

## Output Format

Print a single integer, the probability $\frac{P}{Q}$ in the form $P \cdot Q^{-1}$ mod $1000000007$.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq X_i, Y_i \leq 10^5$
- It is guaranteed that no $2$ asteroids have the same initial position.

---

## Examples

**Example 1**

**Input**

```text
6
1 2
3 1
3 4
3 7
4 6
4 2
```

**Output**

```text
616666671
```

**Explanation**

There are $6$ asteroids in total. The initial positions of the asteroids are:

![](https://s3.amazonaws.com/codechef_shared/download/Images/START88/Asetroids.png)

The probability equals $\dfrac{1}{60}$, which is equivalent to $616666671$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ROIDS)

[Contest: Division 1](https://www.codechef.com/START88A/problems/ROIDS)

[Contest: Division 2](https://www.codechef.com/START88B/problems/ROIDS)

[Contest: Division 3](https://www.codechef.com/START88C/problems/ROIDS)

[Contest: Division 4](https://www.codechef.com/START88D/problems/ROIDS)

***Author:*** [beevo](https://www.codechef.com/users/beevo)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1997

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics

#
[](#problem-4)PROBLEM:

There are N asteroids in the 2-D plane, the i-th initially at (X_i, Y_i).

Each second, every asteroid moves one step left.

An optimal strategy to destroy the asteroids is to pick an asteroid with the smallest X-coordinate each second.

A random strategy is to pick a random asteroid each second.

Find the probability that a random strategy is optimal.

#
[](#explanation-5)EXPLANATION:

Let’s number the asteroids 1, 2, \ldots, N.

Then, any strategy of destroying the asteroids can be described by an arrangement of the numbers 1 to N, i.e, a *permutation* P of length N which tells us that the i-th asteroid destroyed was P_i.

The total number of strategies is thus N!, and a random strategy simply picks one out of these N! uniformly at random.

So, if there are K *optimal* strategies in total, the probability that a random strategy is optimal is exactly \frac{K}{N!}

This means all we need to do is compute K, the number of optimal strategies.

We can make the following observations:

- The y-coordinates of the asteroids don’t matter at all, they neither change nor affect which one is chosen. They can be entirely ignored.

This makes our problem essentially one-dimensional, we only care about the x-coordinates.

- All the asteroids move similarly, so their relative positions stay the same. That is, if asteroid i is initially to the left of asteroid j, then this relation will continue to hold no matter how much time passes.

In other words, we can ignore the passage of time entirely, which makes finding an optimal strategy obvious.

Let x_1, x_2, \ldots, x_k be the *distinct* x-coordinates that appear among the points, with x_1 \lt x_2 \lt \ldots \lt x_k.

Let c_i be the number of points whose x-coordinate is x_i.

Then, an optimal strategy must look as follows:

- First, pick all c_1 points whose x-coordinate is x_1. These c_1 points can be chosen in any order, for c_1! ways in total.

- Next, pick all c_2 points whose x-coordinate is x_2. These c_2 points can be chosen in any order, for c_2! ways in total.

\vdots

- Finally, pick all c_k points whose x-coordinate is x_k. These c_k points can be chosen in any order, for c_k! ways in total.

The number of optimal strategies is thus simply the product of all the above values, i.e, \displaystyle\prod_{i=1}^k c_i!

If factorials are precomputed, computing the above product becomes simple.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>

#define el '\n'

typedef long long ll;
typedef long double ld;

#define Beevo ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 1e5 + 5, M = 1e9 + 7;

int fact[N], freq[N];

int mul(int a, int b) {
    return 1LL * a * b % M;
}

void pre() {
    fact[0] = 1;

    for (int i = 1; i < N; i++)
        fact[i] = mul(fact[i - 1], i);
}

int modPow(int b, int p) {
    if (p == 0)
        return 1;

    int x = modPow(b, p / 2);

    return p % 2 == 0 ? mul(x, x) : mul(b, mul(x, x));
}

int modInvFer(int n) {
    return modPow(n, M - 2);
}

void testCase() {
    pre();

    int n;
    cin >> n;

    assert(n >= 1 && n <= 1e5);

    int x, y;
    for (int i = 0; i < n; i++)
        cin >> x >> y, freq[x]++, assert(min(x, y) >= 1 && max(x, y) <= 1e5);

    int ways = 1;
    for (int i = 0; i < N; i++)
        ways = mul(ways, fact[freq[i]]);

    cout << mul(ways, modInvFer(fact[n]));
}

signed main() {
    Beevo

    int t = 1;
//    cin >> t;

    while (t--)
        testCase();
}
``

Tester's code (C++)
``/*...................................................................*
 *............___..................___.....____...______......___....*
 *.../|....../...\........./|...../...\...|.............|..../...\...*
 *../.|...../.....\......./.|....|.....|..|.............|.../........*
 *....|....|.......|...../..|....|.....|..|............/...|.........*
 *....|....|.......|..../...|.....\___/...|___......../....|..___....*
 *....|....|.......|.../....|...../...\.......\....../.....|./...\...*
 *....|....|.......|../_____|__..|.....|.......|..../......|/.....\..*
 *....|.....\...../.........|....|.....|.......|.../........\...../..*
 *..__|__....\___/..........|.....\___/...\___/.../..........\___/...*
 *...................................................................*
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define MOD 1000000007

const int N = 100005;
int f[N],invf[N];

int power(int a,int b)
{
    if(b==0)
        return 1;
    else
    {
        int x=power(a,b/2);
        int y=(x*x)%MOD;
        if(b%2)
            y=(y*a)%MOD;
        return y;
    }
}

int inverse(int a)
{
    return power(a,MOD-2);
}

void precompute()
{
    f[0]=1;
    for(int i=1;i<N;i++)
        f[i]=(f[i-1]*i)%MOD;
    for(int i=0;i<N;i++)
        invf[i]=inverse(f[i]);
}

void solve(int tc)
{
    int n;
    cin >> n;
    map<int,int> c;
    for(int i=0;i<n;i++)
    {
        int x,y;
        cin >> x >> y;
        c[x]++;
    }
    int num = 1;
    for(auto z:c)
    {
        num = (num*f[z.second])%MOD;
    }
    int den = f[n];
    int ans = (num*inverse(den))%MOD;
    cout << ans << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    precompute();
    int tc=1;
    // cin >> tc;
    for(int ttc=1;ttc<=tc;ttc++)
        solve(ttc);
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
n = int(input())
a = []
good, total = 1, 1
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)

    total *= i+1
    total %= mod
a.sort()
a.append(-1)

ct = 0
fac = 1
for i in range(n+1):
    if a[i] == a[i-1]:
        ct += 1
        fac *= ct
        fac %= mod
    else:
        good *= fac
        good %= mod
        fac = ct = 1
print(good * pow(total, mod-2, mod) % mod)
``

</details>
