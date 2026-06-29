# Adjacent Xors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADJXOR2 |
| Difficulty Rating | 1827 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ADJXOR2](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ADJXOR2) |

---

## Problem Statement

JJ has an array $A$ of length $N$ and an integer $X$. JJ can perform the following operation **at most once**:
- Select a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of $A$ and add $X$ to all the elements of that subsequence.

For example, if $A = [2, 1, 6, 3, 5]$ and $X = 7$, we can select the subsequence $[2, 3, 5]$ and add $X$ to all the elements. Now the array $A$ becomes $[2 + 7, 1, 6, 3 + 7, 5 + 7] = [9, 1, 6, 10, 12]$.

JJ wants to maximize the value of $\displaystyle \sum_{i = 2}^{N} (A_{i - 1} \oplus A_{i})$. Can you help him to do so?

Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

& & kya
&

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two space-separated integers $N$ and $X$ — the size of the array $A$ and the parameter $X$ mentioned in the statement.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the maximum value of $\displaystyle \sum_{i = 2}^{n} (A_{i - 1} \oplus A_{i})$ which can be obtained after applying the given operation **at most once**.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \le X \le 10^9$
- $1 \le A_i \le 10^9$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2 1
1 2
4 1
2 2 3 3
5 2
5 3 6 2 8
```

**Output**

```text
3
15
43
```

**Explanation**

**Test case $1$:** It is optimal to not perform the given operation. So the answer will equal $1 \oplus 2 = 3$.

**Test case $2$:** It is optimal to add $X = 1$ to the $2^{nd}$ and the $3^{rd}$ element. So $A$ will become $[2, 3, 4, 3]$ and the answer will be $(2 \oplus 3) + (3 \oplus 4) + (4 \oplus 3) = 15$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
1 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 1
2 2 3 3
```

**Output for this case**

```text
15
```



#### Test case 3

**Input for this case**

```text
5 2
5 3 6 2 8
```

**Output for this case**

```text
43
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ADJXOR2)

[Contest: Division 1](https://www.codechef.com/START51A/problems/ADJXOR2)

[Contest: Division 2](https://www.codechef.com/START51B/problems/ADJXOR2)

[Contest: Division 3](https://www.codechef.com/START51C/problems/ADJXOR2)

[Contest: Division 4](https://www.codechef.com/START51D/problems/ADJXOR2)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Venkata Nikhil Medam](https://www.codechef.com/users/nikhil_medam)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1827

#
[](#prerequisites-3)PREREQUISITES:

Dynamic programming

#
[](#problem-4)PROBLEM:

JJ has an array A and an integer X. At most once, he can choose a subsequence of A and add X to all its elements.

What is the maximum possible value of \displaystyle \sum_{i=2}^N (A_i \oplus A_{i-1}) that he can obtain?

#
[](#explanation-5)EXPLANATION:

This task can be solved fairly easily with the help of dynamic programming.

Suppose we define a new array dp of length N, where dp_i is the maximum possible answer for the first i elements. Our aim is to compute dp_N.

Each element has two choices for it: it either remains A_i, or becomes A_i + X. This information can be encapsulated into the state for dynamic programming by simply holding two values for each index: dp_{i, 1} denotes the maximum answer for the first i elements if A_i isn’t changed, and dp_{i, 2} denotes the maximum answer for the first i elements if A_i is changed to A_i + X.

All that remains are the base cases and transitions.

- The base case is i = 1, where we have dp_{1, 1} = dp_{1, 2} = 0

- To compute dp_{i, 1}, we have 2 choices for the previous element: either it changed, or it did not.

- If it did not change, we get the value dp_{i-1, 1} + (A_i \oplus A_{i-1})

- If it did change, we get the value dp_{i-1, 2} + (A_i \oplus (A_{i-1} + X))

-
dp_{i, 1} is the maximum of these two values.

- Similarly, dp_{i, 2} is the maximum of dp_{i-1, 1} + ((A_i + X) \oplus A_{i-1}) and dp_{i-1, 2} + ((A_i + X) \oplus (A_{i-1} + X)).

These values can be computed iteratively, simply iterating i from 2 to N. The final answer is the maximum of dp_{N, 1} and dp_{N, 2}.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter (C++)
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const int mod = 998244353;

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

int sumN = 0;

void solve()
{
    int n = readIntSp(1, 1e5);
    int x = readIntLn(1, 1e9);
    vector<int> a = readVectorInt(n, 1, 1e9);
    sumN += n;
    vector<array<int, 2>> dp(n);
    for(int i = 1; i < n; i++)
    {
        dp[i][0] = max(dp[i - 1][0] + (a[i - 1] ^ a[i]), dp[i - 1][1] + ((a[i - 1] + x) ^ a[i]));
        dp[i][1] = max(dp[i - 1][0] + (a[i - 1] ^ (a[i] + x)), dp[i - 1][1] + ((a[i - 1] + x) ^ (a[i] + x)));
    }
    cout << max(dp[n - 1][0], dp[n - 1][1]) << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1e5);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    readEOF();
    assert(sumN <= 2e5);
    return 0;
}
``

Tester (nikhil_medam, C++)
``// Tester: Nikhil_Medam
#include <bits/stdc++.h>
#pragma GCC optimize ("-O3")
using namespace std;
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long
#define double long double
const int N = 1e5 + 5;

int t, n, x, a[N], dp[N][2];
int xorValue(int x, int y) {
    return x ^ y;
}
int32_t main() {
    cin >> t;
    while(t--) {
        cin >> n >> x;
        for(int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        for(int i = 2; i <= n; i++) {
            dp[i][0] = max(xorValue(a[i], a[i - 1]) + dp[i - 1][0], xorValue(a[i], a[i - 1] + x) + dp[i - 1][1]);
            dp[i][1] = max(xorValue(a[i] + x, a[i - 1]) + dp[i - 1][0], xorValue(a[i] + x, a[i - 1] + x) + dp[i - 1][1]);
        }
        cout << max(dp[n][0], dp[n][1]) << endl;
    }
	return 0;
}
``

Editorialist (Python)
``for _ in range(int(input())):
	n, x = map(int, input().split())
	a = list(map(int, input().split()))
	p, q = 0, 0
	for i in range(1, n):
		same = max(p + (a[i] ^ a[i-1]), q + (a[i] ^ (a[i-1] + x)))
		change = max(p + ((a[i]+x) ^ a[i-1]), q + ((a[i]+x) ^ (a[i-1] + x)))
		p, q = same, change
	print(max(p, q))
``

</details>
