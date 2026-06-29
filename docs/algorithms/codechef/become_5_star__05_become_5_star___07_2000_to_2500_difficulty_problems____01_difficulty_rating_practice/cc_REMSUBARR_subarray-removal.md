# Subarray Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMSUBARR |
| Difficulty Rating | 2007 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [REMSUBARR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/REMSUBARR) |

---

## Problem Statement

Chef has a *permutation* $A$ of length $N$. Chef can perform the following operation on $A$: $\\$
**1)** Select $L$ and $R$ such that $(1 \le L \le R \le N)$ and $(R - L + 1 \lt N)$ $\\$
**2)** Remove the subarray $A_{L \ldots R}$ from $A$. (The remaining parts of $A$ are concatenated)

The score of this operation $ = $ length of the subarray removed $ = R - L + 1$

For e.g., if $A = [3, 1, 4, 6, 5, 2]$, and Chef selects $L = 3, R = 5$, then the score of this operation $ = 3$ and $A$ becomes $[3, 1, 2]$.

Chef wants to perform this operation **exactly once** such that, after the operation, $A$ still remains a permutation. What is the maximum score that Chef can achieve in doing so?

As a reminder, a permutation of length $M$ is an array where every integer from $1$ to $M$ occurs exactly once.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the permutation $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the permutation $A$.

---

## Output Format

For each test case, output the maximum score that Chef can achieve after applying the operation exactly once such that $A$ still remains a permutation.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \le N \le 10^5$
- $A$ is a permutation
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3
2 1 3
7
1 2 3 4 5 6 7
6
3 1 4 6 5 2
```

**Output**

```text
1
6
3
```

**Explanation**

**Test Case 1:** Chef can remove subarray $A_{3 \ldots 3}$ after which $A$ becomes $[2, 1]$ which is still a permutation.

**Test Case 2:** Chef can remove subarray $A_{2 \ldots 7}$ after which $A$ becomes $[1]$ which is still a permutation.

**Test Case 3:** Chef can remove subarray $A_{3 \ldots 5}$ after which $A$ becomes $[3, 1, 2]$ which is still a permutation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 1 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
7
1 2 3 4 5 6 7
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
6
3 1 4 6 5 2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REMSUBARR)

[Contest: Division 1](https://www.codechef.com/START89A/problems/REMSUBARR)

[Contest: Division 2](https://www.codechef.com/START89B/problems/REMSUBARR)

[Contest: Division 3](https://www.codechef.com/START89C/problems/REMSUBARR)

[Contest: Division 4](https://www.codechef.com/START89D/problems/REMSUBARR)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2007

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You’re given a permutation P of \{1, 2, \ldots, N\}.

Chef can choose a subarray [L, R] of length strictly less than N and delete it. The *score* of this operation is the length of the subarray.

Find the maximum score of an operation such that the remaining elements still form a permutation.

#
[](#explanation-5)EXPLANATION:

Suppose Chef deletes subarray [L, R] and the remaining elements form a permutation of \{1, 2, \ldots, K\}.

Then, note that the length of the subarray [L, R] must be exactly N-K, since it must contain the elements K+1, K+2, \ldots, N (in some order) — that’s the only way for the remaining parts to form a permutation.

We want to *maximize* N-K, which means we want to *minimize* K.

That is, we want to find the smallest integer K such that elements K+1, K+2, \ldots, N appear as a contiguous subarray in the permutation.

This gives us a rather straightforward \mathcal{O}(N^2) solution (which is too slow to get AC, but serves as a good starting point):

- Iterate K from 1 to N

- For a fixed K, mark all the positions that contain integers \geq K+1, then check if they form a contiguous subarray.

Now, we’d like to speed up the second part of this algorithm.

Let’s define an array \text{pos}, such that \text{pos}_x = i if and only if P_i = x.

That is, \text{pos} denotes the positions of the elements in P.

Then, for a fixed K, we’re interested in \text{pos}_{K+1}, \text{pos}_{K+2}, \ldots, \text{pos}_{N}.

In particular,

- Let L_K = \min(\text{pos}_{K+1}, \text{pos}_{K+2}, \ldots, \text{pos}_{N}) and R_K = \max(\text{pos}_{K+1}, \text{pos}_{K+2}, \ldots, \text{pos}_{N}).

- Then, [L_K, R_K] is the *unique smallest* subarray that contains all the elements \geq K+1.

- All we need to do is check whether the length of this subarray is exactly N-K, i.e, if R_K-L_K+1 =  N-K.

Note that L_K and R_K are respectively suffix minimums/maximums of the \text{pos} array.

The \text{pos} array itself can be computed in \mathcal{O}(N), after which computing its suffix minima/maxima is trivial.

After this, each K is processed in \mathcal{O}(1) time, giving us a solution in \mathcal{O}(N) overall.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
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

const long long INF = 1e18;

const int N = 1e6 + 5;

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
    int n = readIntLn(2, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, n);
    assert(set<int>(a.begin(), a.end()).size() == n);
    vector<int> idx(n + 1);
    for(int i = 0; i < n; i++)
        idx[a[i]] = i;
    int L = N + 1, R = 0, ans = 0;
    for(int i = n; i > 1; i--)
    {
        L = min(L, idx[i]);
        R = max(R, idx[i]);
        if(R - L + 1 == n - i + 1)
            ans = R - L + 1;
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
        // cout << "Case #" << tc << ": ";
        solve();
    }
    readEOF();
    assert(sumN <= 5e5);
    cerr << sumN << endl;
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pos = [0]*(n+1)
	for i in range(n): pos[a[i]] = i
	L, R = n, -1
	ans = 0
	for x in reversed(range(2, n+1)):
		L = min(L, pos[x])
		R = max(R, pos[x])
		if R-L+1 == n-x+1: ans = n-x+1
	print(ans)
``

</details>
