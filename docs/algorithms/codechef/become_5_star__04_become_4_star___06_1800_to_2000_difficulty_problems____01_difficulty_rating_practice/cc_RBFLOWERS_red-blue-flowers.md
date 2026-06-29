# Red Blue Flowers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RBFLOWERS |
| Difficulty Rating | 1936 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [RBFLOWERS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/RBFLOWERS) |

---

## Problem Statement

Chef has a garden containing $N$ cells. The $i$-th cell has $R_i$ red flowers and $B_i$ blue flowers. Chef can collect only one type of flowers (either red or blue) from each cell.

Let $X$ denote the total number of red flowers Chef collects and $Y$ denote the total number of blue flowers Chef collects. Chef wants to **maximize** the value of $\mathrm{min}(X, Y)$. Can you help Chef?

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the number of cells in Chef's garden.
- The second line of each test case contains $N$ space-separated integers $R_1, R_2, \dots, R_N$ denoting the number of red flowers in each cell.
- The third line of each test case contains $N$ space-separated integers $B_1, B_2, \dots, B_N$ denoting the number of blue flowers in each cell.

---

## Output Format

For each test case, output the maximum value of $\mathrm{min}(X, Y)$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq R_i, B_i \leq 200$
- The sum of $N$ over all test cases does not exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
3
1
101
3
2
1 200
199 1
4
1 2 3 10
3 1 3 5
```

**Output**

```text
0
199
7
```

**Explanation**

**Test case 1:**
If Chef collects $101$ red flowers from the cell, Chef will have a total of $101$ red flowers $(X = 101)$ and $0$ blue flowers $(Y = 0)$.

If Chef collects the $3$ blue flowers from the cell, Chef will have a total of $0$ red flowers $(X = 0)$ and $3$ blue flowers $(Y = 3)$.

Either way, $\mathrm{min}(X, Y) = 0$, the answer is $0$.

**Test case 2:** Chef collects the $199$ blue flowers from the first cell and the $200$ red flowers from the second cell, so $\mathrm{min}(X, Y) = 199$, which is maximum.

**Test case 3:** Chef collects blue cells from the first three cells $(Y = 3 + 1 + 3)$ and red flowers from the fourth cell $(X = 10)$, so $\mathrm{min}(X, Y) = 7$, which is maximum.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
101
3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
1 200
199 1
```

**Output for this case**

```text
199
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 10
3 1 3 5
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RBFLOWERS)

[Contest: Division 1](https://www.codechef.com/START61A/problems/RBFLOWERS)

[Contest: Division 2](https://www.codechef.com/START61B/problems/RBFLOWERS)

[Contest: Division 3](https://www.codechef.com/START61C/problems/RBFLOWERS)

[Contest: Division 4](https://www.codechef.com/START61D/problems/RBFLOWERS)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Knapsack-style dynamic programming

#
[](#problem-4)PROBLEM:

You have two arrays R and B, both of length N. At each index, you can choose either R_i or B_i. Let X denote the sum of all chosen R_i and Y denote the sum of all chosen B_i. Maximize \min(X, Y).

#
[](#explanation-5)EXPLANATION:

The limits on N and the values are small, so a natural knapsack-style dynamic programming solution should strike you, something along the following lines:

Let f(i, x, y) be a boolean function, where f(i, x, y) is true if and only if you can make choices among the first i elements such that the sum of reds is exactly x and the sum of blues is exactly y.

Transitions are extremely easy: f(i, x, y) = f(i-1, x - R_i, y) \vee f(i-1, x, y - B_i) (\vee denotes logical OR), and memoization naturally makes transitions \mathcal{O}(1).

The final answer is the maximum value of \min(x, y) across all (x, y) such that f(N, x, y) is true.

While this is correct, it is also too slow. x and y can be as large as 200\times N, so we have 200^2 \times N^3 states in our dp, which is way too much.

Note that the constraints do allow a solution in \mathcal{O}(200 \times N^2), i.e, kicking out one state of our dp.

We can achieve that by a relatively common trick: turn the removed state into the value of the dp!

Consider a function f(i, x) which denotes the maximum sum of blues from the first i elements, given that the sum of reds is x.

Transitions for this function are as follows:

- If we choose R_i, the sum of blues is f(i-1, x - R_i)

- Otherwise, the sum of blues is f(i-1, x) + B_i

- So, f(i, x) = \max(f(i-1, x) + B_i, f(i-1, x-R_i))

Once again, by memoizing f(i, x) values, transitions are \mathcal{O}(1), so both our time and space complexity are fine.

The final answer is the maximum of \min(x, f(N, x)) across all 0 \leq x \leq 200\cdot N.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\cdot S) per test case, where S = 200\times N.

#
[](#code-7)CODE:

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << "L: " << l << ", R: " << r << ", Value Found: " << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int main() {
	int t;
	t = readIntLn(1, 100);
	int smn = 0;
	while(t--) {
	    int n;
	    n = readIntLn(1, 100);
	    smn += n;
	    assert(smn <= 100);
	    int r[n], b[n];
	    for(int i = 0; i < n - 1; i++) r[i] = readIntSp(1, 200);
	    r[n - 1] = readIntLn(1, 200);
	    for(int i = 0; i < n - 1; i++) b[i] = readIntSp(1, 200);
	    b[n - 1] = readIntLn(1, 200);
	    int dp[n][n*200 + 1];
	    memset(dp, -1, sizeof(dp));
	    dp[0][0] = b[0];
	    dp[0][r[0]] = 0;
	    for(int i = 0; i < n - 1; i++) {
	        for(int j = 0; j <= n*200 - r[i + 1]; j++)
	            dp[i + 1][j + r[i + 1]] = dp[i][j];
	        for(int j = 0; j <= n*200; j++)
	        if(dp[i][j] > -1)
	            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + b[i + 1]);
	    }
	    int ans = 0;
	    for(int j = 0; j <= n*200; j++) ans = max(ans, min(j, dp[n - 1][j]));
	    cout << ans << "\n";
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	r = list(map(int, input().split()))
	b = list(map(int, input().split()))
	maxS = 20004
	dp = [-1]*maxS
	dp[0] = 0
	for i in range(n):
		R, B = r[i], b[i]
		for x in reversed(range(maxS)):
			val = -1
			if dp[x] != -1:
				val = dp[x] + B
			if x-R >= 0 and dp[x-R] != -1:
				val = max(val, dp[x-R])
			dp[x] = val
	ans = 0
	for i in range(maxS):
		if dp[i] == -1: continue
		ans = max(ans, min(i, dp[i]))
	print(ans)
``

</details>
