# Palindrome In Making

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEPAL3 |
| Difficulty Rating | 2322 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAKEPAL3](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAKEPAL3) |

---

## Problem Statement

JJ has an array $A$ of length $N$. He can perform the following operation on $A$:
- Select any $L$, $R$ ($1 \le L \le R \le N$) and for each $i$ such that $L \le i \le R$, set $A_i := A_i + 1$.

JJ wants to make $A$ palindromic. Find the **minimum** number of moves to do so.

Note: An array is called a palindrome if it reads the same backwards and forwards, for e.g. $[1, 3, 3, 1]$ and $[6, 2, 6]$ are palindromic.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the minimum number of moves to make $A$ palindromic.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
6
2 6 4 3 4 1
2
1 10
3
1 10 1
```

**Output**

```text
2
9
0
```

**Explanation**

**Test Case 1**: We can perform the following operations:
- $[2, 6, \underline{4, 3, 4, 1}] \xrightarrow{L = 3, R = 6} [2, 6, 5, 4, 5, 2]$
- $[2, 6, 5, \underline{4, 5}, 2] \xrightarrow{L = 4, R = 5} [2, 6, 5, 5, 6, 2]$

**Test Case 2:** We perform the operation on $(L = 1, R = 1)$ $9$ times after which array becomes $[10, 10]$.

**Test Case 3:** $A$ is already a palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
2 6 4 3 4 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
1 10
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
3
1 10 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAKEPAL3)

[Contest: Division 1](https://www.codechef.com/START66A/problems/MAKEPAL3)

[Contest: Division 2](https://www.codechef.com/START66B/problems/MAKEPAL3)

[Contest: Division 3](https://www.codechef.com/START66C/problems/MAKEPAL3)

[Contest: Division 4](https://www.codechef.com/START66D/problems/MAKEPAL3)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2322

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

Given an array A, in one move you can pick any 1 \leq L \leq R \leq N and add 1 to all A_i such that L \leq i \leq R.

Find the minimum number of moves to make A a palindrome.

#
[](#explanation-5)EXPLANATION:

We want to make A a palindrome, so let’s look at corresponding pairs in A, i.e, pairs of indices (i, N+1-i). If A_i \leq A_{N+1-i}, then A_i needs to be increased to reach A_{N+1-i}.

So, let’s consider a new array B of length N, where

-
B_i = A_{N+1-i} - A_i,  if A_i \leq A_{N+1-i}

-
B_i = 0 otherwise.

B_i is the *least* number of operations that need to cover index i so that A can be made a palindrome.

In fact, we can always perform operations in such a way that exactly B_i of them touch index i, and it’s not hard to see that this is optimal.

Now, all that remains is to minimize the number of operations we perform. That can be done greedily, as follows:

- Let’s iterate i from 1 to N.

- When i = 1, perform B_1 operations on index 1

- When i = 2,

- If B_2 \leq B_1, we can extend B_2 of the operations performed on index 1 to also cover this index, for no extra cost.

- if B_2 \gt B_1, then we need B2 - B_1 *extra* operations starting at index 2.

- Note that the above two cases can be combined to say that we perform \max(0, B_2 - B_1) operations starting at index 2.

- Now notice that this applies to any index i where 2 \leq i \leq N, i.e, we need \max(0, B_i - B_{i-1}) operations starting at this index.

So, the final answer is simply

\sum_{i=2}^N \max(0, B_i - B_{i-1})

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
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

int sign(int x)
{
    return x >= 0 ? 1 : -1;
}

void solve()
{
    int n = readIntLn(1, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e9);
    vector<int> d(n / 2);
    for(int i = 0; i < n / 2; i++)
        d[i] = a[i] - a[n - 1 - i];
    int ans = 0;
    for(int l = 0; l < sz(d);)
    {
        int r = l;
        while(r < sz(d) and sign(d[l]) == sign(d[r]))
            r++;
        ans += abs(d[l]);
        for(int i = l + 1; i < r; i++)
            ans += max(0LL, abs(d[i]) - abs(d[i - 1]));
        l = r;
    }
    cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1e5);
    for(int tc = 1; tc <= T; tc++)
    {
        solve();
    }
    readEOF();
    assert(sumN <= 3e5);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur = ans = 0
    for i in range(n):
        need = max(0, a[n-1-i] - a[i])
        ans += max(0, need - cur)
        cur = need
    print(ans)
``

</details>
