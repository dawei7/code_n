# Yet Another Palindrome Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRPAL |
| Difficulty Rating | 1594 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [ARRPAL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/ARRPAL) |

---

## Problem Statement

Chef has an array $A$ of size $N$. He can perform the following operation on $A$:
- Select an $i$ $(1 \le i \le N)$ and for all $1 \le j \le i$, set $A_j := A_j + 1$ (i.e. add $1$ to every element in the prefix of length $i$).

Chef wants to convert $A$ to a *palindrome* by using the above operation **minimum** number of times. Can you help Chef?
If it is not possible to convert $A$ to a *palindrome*, output $-1$.

Note: An array is called *palindrome* if it reads the same backwards and forwards, for e.g. $[1, 4, 1]$ and $[7, 3, 3, 7]$ are palindromic arrays.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the **minimum** number of operations required to convert $A$ to a palindromic array.

If it is not possible to do so, output $-1$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
4 2 2 4
5
5 4 3 2 1
4
1 2 3 4
```

**Output**

```text
0
-1
3
```

**Explanation**

**Test case $1$:** The given array is already a palindrome.

**Test case $2$:** It can be proven that it is not possible to convert $A$ to a palindromic array using the given operation.

**Test case $3$:** We can perform the following operations:
- Select $i = 1$, $[1, 2, 3, 4] \rightarrow [2, 2, 3, 4]$
- Select $i = 2$, $[2, 2, 3, 4] \rightarrow [3, 3, 3, 4]$
- Select $i = 1$, $[3, 3, 3, 4] \rightarrow [4, 3, 3, 4]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 2 2 4
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5
5 4 3 2 1
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 4
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

[Practice](https://www.codechef.com/problems/ARRPAL)

[Contest: Division 1](https://www.codechef.com/START60A/problems/ARRPAL)

[Contest: Division 2](https://www.codechef.com/START60B/problems/ARRPAL)

[Contest: Division 3](https://www.codechef.com/START60C/problems/ARRPAL)

[Contest: Division 4](https://www.codechef.com/START60D/problems/ARRPAL)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Tester:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1594

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You are given an array A. In one move, you can add 1 to any prefix of A. Find the minimum number of moves needed to make A a palindrome, or report that it is impossible to do so.

#
[](#explanation-5)EXPLANATION:

Consider a second array B, where B_i denotes the number of times 1 was added to A_i during our operations. That is, the i-th element of the final array is A_i + B_i.

It’s obvious that B is a decreasing array (B_i \geq B_{i-1} for every i \gt 1), and the number of operations performed is exactly B_1. Our aim is to minimize B_1.

The final array should be a palindrome. So, if we consider some index i (1 \leq i \leq N/2), we want

A_i + B_i = A_{N+1-i} + B_{N+1-i}

Now, note that performing a move on a prefix larger than N/2 is pointless and can always be replaced by a shorter move that achieves the same result (do you see how?).

So, we can assume B_i = 0 for i \gt N/2. In particular, our equation above for a fixed index  i changes to

A_i + B_i = A_{N+1-i}

Notice that this fixes the value of B_i, so we just need to check whether the B_i we obtain this way is a valid array or not.

Hence, the final solution is as follows:

- For each 1 \leq i \leq N/2, compute B_i = A_{N+1-i} - A_i.

- If B is not a decreasing array, or any element of B is \lt 0, then it is impossible to make A a palindrome and the answer is -1.

- Otherwise, the answer is simply B_1.

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

void solve()
{
    int n = readIntLn(1, 3e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e9);
    vector<int> d;
    for(int i = 0; i <= n / 2 - 1; i++)
        d.push_back(a[n - 1 - i] - a[i]);
    if(*min_element(d.begin(), d.end()) >= 0 and is_sorted(d.rbegin(), d.rend()))
        cout << d[0] << endl;
    else
        cout << -1 << endl;
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
    assert(sumN <= 3e5);
    readEOF();
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
	    int n;
	    cin >> n;
	    int a[n];
	    for(int i = 0; i < n; i++) cin >> a[i];
	    int b[n];
	    memset(b, 0, sizeof(b));
	    for(int i = 0; i < n/2; i++) b[i] = a[n - 1 - i] - a[i];
	    int bad = 0;
	    if(b[0] < 0) bad = 1;
	    for(int i = 1; i < n; i++)
	        if(b[i] > b[i - 1] || b[i] < 0) bad = 1;
	    if(bad) cout << "-1\n";
	    else cout << a[n - 1] - a[0] << "\n";
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in reversed(range(n//2)):
        a[i] += ans
        if a[i] > a[n-1-i]:
            ans = -1
            break
        ans += a[n-1-i] - a[i]
    print(ans)
``

</details>
