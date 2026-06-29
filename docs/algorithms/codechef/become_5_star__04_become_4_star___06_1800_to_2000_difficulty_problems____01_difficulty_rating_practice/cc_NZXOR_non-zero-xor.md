# Non Zero Xor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NZXOR |
| Difficulty Rating | 1975 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [NZXOR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/NZXOR) |

---

## Problem Statement

An array $A$ of size $N$ is called *good* if the following conditions hold:
- For every pair $(l, r)$ $(1 \le l \le r \le N)$, $A_l \oplus A_{l+1} \oplus ... \oplus A_{r} \ne 0$. (where $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).)

JJ has an array $A$ of size $N$. He wants to convert the array to a good array. To do so he can perform the following operation multiple times:
- Pick an index $i$ such that $(1 \le i \le N)$ and set $A_i := X$ where $0 \le X \lt 10^{10^{10}}$.

Find the **minimum** number of operations required to convert $A$ into a *good* array.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the **minimum** number of operations required to convert the array $A$ into a good array.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \lt 2^{30}$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5
1 2 3 4 4
3
0 0 0
6
2 3 5 7 11 13
```

**Output**

```text
2
3
0
```

**Explanation**

**Test Case 1:** We can set $A_2 = 4$ and $A_4 = 5$. Thereby $A$ will become $[1, 4, 3, 5, 4]$ which is *good*. We can prove that we can not make $A$ good in $\lt 2$ operations.

**Test Case 2:** We can set $A_1 = 1$, $A_2 = 10$ and $A_3 = 100$. Thereby $A$ will become $[1, 10, 100]$ which is *good*. We can prove that we can not make $A$ good in $\lt 3$ operations.

**Test Case 3:** The given array $A$ is already *good*.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
0 0 0
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
6
2 3 5 7 11 13
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

[Practice](https://www.codechef.com/problems/NZXOR)

[Contest: Division 1](https://www.codechef.com/START55A/problems/NZXOR)

[Contest: Division 2](https://www.codechef.com/START55B/problems/NZXOR)

[Contest: Division 3](https://www.codechef.com/START55C/problems/NZXOR)

[Contest: Division 4](https://www.codechef.com/START55D/problems/NZXOR)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1975

#
[](#prerequisites-3)PREREQUISITES:

Prefix sums

#
[](#problem-4)PROBLEM:

An array is said to be *good* if no subarray has a xor of 0.

Given an array A, in one move you can replace one of its elements with any non-negative integer. Find the minimum number of moves to make A good.

#
[](#explanation-5)EXPLANATION:

Let P_i = A_1 \oplus A_2 \oplus \ldots \oplus A_i denote the prefix xor of array A, with P_0 = 0.

Note that a subarray [L, R] can have a xor of zero if and only if P_R \oplus P_{L-1} = 0, i.e, P_R = P_{L-1}.

So, an array A is *good* if and only if all its prefix sums are distinct.

Now look at what our given operation does to the prefix sums: changing the element A_i changes exactly all the prefix sums P_i, P_{i+1}, \ldots, P_N.

In particular, suppose we set A_i \gets x. Let y = A_i \oplus x. Then, each P_j for j \geq i becomes (P_j \oplus y).

This allows us to ‘fix’ the array from left to right, as follows:

- Let S be the set of current prefix sums. Initially, S = \{0\}.

- Iterate i from 1 to N.

- If P_i is not in S, insert it to S and continue.

- if P_i is in S, we have no choice but to perform an operation. We might as well perform this operation on position i. By choosing a large enough value of x and setting A_i \gets x, we can ensure the following:

-
P_i is no longer in S

- For any j \geq i and k \lt i, it is impossible for P_j = P_k to ever happen.

- In other words, we can essentially just pretend we are starting from an entirely new array. The current set S is useless to us, so we can simply clear it.

- Note that S should now contain something denoting the ‘empty’ prefix (recall that we initially had S = \{0\} for this purpose). There are a couple of ways of achieving this:

- If the values of P_i were calculated in advance, insert P_{i-1} into S (the editorialist’s code does this).

- Otherwise, notice that the values of P_i can actually be calculated on-the-go. If this is how you to choose to implement it, simply reset the current prefix sum to 0 and insert 0 into S to simulate starting from a new array (the setter’s code does this).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or \mathcal{O}(N\log N) per test case, depending on implementation.

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
    int n = readIntLn(1, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 0, (1 << 30) - 1);
    set<int> prefxor{0};
    int ans = 0, cur = 0;
    for(int &x: a)
    {
        cur ^= x;
        if(prefxor.count(cur))
        {
            ans++;
            prefxor.clear();
            cur = 0;
            prefxor.insert(0);
        }
        else
        {
            prefxor.insert(cur);
        }
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
    assert(sumN <= 3e5);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	p = {0}
	ans = 0
	pref = 0
	for x in a:
		pref ^= x
		if pref in p:
			ans += 1
			pref = x
			p = {x}
		else:
			p.add(pref)
	print(ans)
``

</details>
