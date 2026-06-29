# Red Green Grids

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REDGREEN |
| Difficulty Rating | 2319 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [REDGREEN](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/REDGREEN) |

---

## Problem Statement

There is an empty grid (all cells are colored white) of $N$ rows and $M$ columns.

Chef can fill each cell with either `RED` or `GREEN` color.
Chef defines a *valid* path as a path of cells starting from $(1,1)$ and ending at $(N,M)$, where, Chef moves either `right` or `down` by $1$ cell each time.

For a particular grid, Chef defines the *score* of the grid as the number of *valid* paths containing **equal** number of `RED` and `GREEN` cells.

Find the **sum** of *scores* of all possible colored grids containing $N$ rows and $M$ columns.
Since the answer can be large, output it modulo $998244353$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $N$ and $M$ - denoting the dimensions of the grid.

---

## Output Format

For each test case, output the **sum** of *scores* of all possible colored grids containing $N$ rows and $M$ columns, modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, M \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1 1
1 2
2 3
```

**Output**

```text
0
2
72
```

**Explanation**

**Test case $1$:** There are $2$ possible coloured grids of size $1 \times 1$. In the first grid, the one and only cell is colored `RED`. In the second grid, the one and only cell is colored `GREEN`. Neither of the grids have a *valid* path with equal number of red and green cells. Thus, score of each grid is $0$.

**Test case $2$:** There are $4$ possible coloured grids of the given dimension:

For grids $1$ and $4$, the scores are $0$ as there are no valid paths with equal red and green cells. Grids $2$ and $3$ have score $1$ each. The valid path with equal red and green cells is $(1,1) \rightarrow (1,2)$ in both the grids.

Thus, the sum of scores of all possible coloured grids is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2 3
```

**Output for this case**

```text
72
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REDGREEN)

[Contest: Division 1](https://www.codechef.com/START60A/problems/REDGREEN)

[Contest: Division 2](https://www.codechef.com/START60B/problems/REDGREEN)

[Contest: Division 3](https://www.codechef.com/START60C/problems/REDGREEN)

[Contest: Division 4](https://www.codechef.com/START60D/problems/REDGREEN)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2319

#
[](#prerequisites-3)PREREQUISITES:

Combinatorics

#
[](#problem-4)PROBLEM:

You have an N\times M grid, each cell of which can be colored either red or green. The score of a colored grid is the number of right-down paths from (1, 1) to (N, M) such that the number of red cells equals the number of green cells on this path.

Find the sum of scores across possible colorings of the grid.

#
[](#explanation-5)EXPLANATION:

This task can be solved with a trick that’s rather common in counting problems, sometimes called the *contribution trick*.

Whenever you need to fix a configuration and count the number of objects in it that satisfy some property, you can often instead fix an object that satisfies that property and count how many configurations it appears in — the sum of both values is the same.

Let’s do the same thing here. We want to

- Fix a coloring of the grid

- Look at a right-down path from (1, 1) to (N, M)

- Count it if it has an equal number of red and green cells

Instead, we will

- Fix a right-down path from (1, 1) to (N, M)

- Color it in such a way that the number of red and green cells is equal

- Then, count the number of grids that contain this path

Summing this across all paths is the the final answer.

Now, let’s see how to compute this.

- First, we need to fix a path. There are \binom{N+M-2}{M-1} paths from (1, 1) to (N, M) — this is a well-known result.

- An easy proof is that you make exactly N+M-2 steps in total with M-1 of them being right and N-1 being down, so fixing the positions of the right steps fixes the path.

- Next, we need to color the path correctly.

- Let the length of the path be $L. Note that L = N + M - 1.

- If L is odd, there is no way to color the path correctly

- Otherwise, we simply fix the positions of the green cells in \binom{L}{L/2} ways, which then also fixes the red cells

- Finally, we want to know how many grids this path appears in. We’ve fixed the colors of cells on the path, but everything else is completely free and has two choices each (red or green).

- This gives us 2^{N\cdot M - L} grids that contain this path.

So, the final answer is simply

\binom{N+M-2}{M-1} \binom{L}{L/2} 2^{N\cdot M - L}

where L = N + M - 1. Note that the answer is 0 when L is odd.

The binomial coefficients can be precomputed in a 2000\times 2000 table using Pascal’s identity since we only need something like \binom{2000}{1000} at worst. Similarly, the powers of 2 upto 10^6 can be precomputed.

This allows each query to be answered in \mathcal{O}(1) time.

There are of course other ways to compute binomial coefficients (for example, the standard factorial + inverse factorial method) and powers of 2 (via binary exponentiation), if you want to do something else.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) or \mathcal{O}(\log {MOD}) per test case, depending on implementation.

#
[](#code-7)CODE:

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define maxn 10007
#define mod 998244353

long long int fact[maxn], ifact[maxn];

long long int mpow(long long int a, long long int b) {
    long long int res = 1;
    while(b) {
        if(b&1) res *= a, res %= mod;
        a *= a;
        a %= mod;
        b >>= 1;
    }
    return res;
}

void pre() {
    fact[0] = fact[1] = ifact[0] = ifact[1] = 1;
    for(int i = 2; i < maxn; i++) fact[i] = fact[i - 1]*i, fact[i] %= mod;
    for(int i = 2; i < maxn; i++) ifact[i] = ifact[i - 1]*mpow(i, mod - 2), ifact[i] %= mod;
}

long long int comb(long long int a, long long int b) {
    if(b == 0) return 1LL;
    long long int ans = fact[a];
    ans *= ifact[b];
    ans %= mod;
    ans *= ifact[a - b];
    ans %= mod;
    return ans;
}

int main() {
    pre();
    int t;
    cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;
        if((n + m - 1)&1) cout << "0\n";
        else {
            long long int paths = comb(n + m - 2, m - 1);
            paths *= ((fact[n + m - 1]*((ifact[(n + m - 1)/2]*ifact[(n + m - 1)/2])%mod))%mod);
            paths %= mod;
            paths *= mpow(2, n*m - (n + m - 1));
            paths %= mod;
            cout << paths << "\n";
        }
    }
    return 0;
}
``

Editorialist's code (Python)
``mod = 998244353
N = 2005
C = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    C[i][0] = 1
for i in range(1, N):
    for j in range(1, i+1):
        C[i][j] = (C[i-1][j] + C[i-1][j-1]) % mod

for _ in range(int(input())):
    n, m = map(int, input().split())
    len = n + m - 1
    ans = C[n+m-2][m-1] * C[len][len//2] * pow(2, n*m - len, mod)
    if len%2 == 1:
        ans = 0
    print(ans%mod)
``

</details>
