# Palindrome by Splitting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPLITPAL |
| Difficulty Rating | 1540 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [SPLITPAL](https://www.codechef.com/learn/course/stacks-and-queues/DEQUE/problems/SPLITPAL) |

---

## Problem Statement

JJ has an array $A$ initially of length $N$. He can perform the following operation on $A$:

**1)** Pick any index $i$ $(1 \le i \le |A|)$ such that $A_i \gt 1$ $\\$
**2)** Select any two integers $X$ and $Y$ such that $X + Y = A_i$ and $X, Y \ge 1$ $\\$
**3)** Replace $A_i$ with $X$ and $Y$

Note that the length of the array increases by $1$ after each operation.

For example, if $A = [4, 6, 7, 2]$, he can select $i = 1$ and select $X = 1, Y = 3$ (since $X + Y = A_1$). After the operation array becomes: $[\underline{4}, 6, 7, 2] \rightarrow [\underline{1}, \underline{3}, 6, 7, 2]$.

JJ wants to make $A$ palindromic. Find the minimum number of operations to do so.

It is guaranteed that $A$ can be converted to a palindromic array by using the above operation.

Note: An array is called a palindrome if it reads the same backwards and forwards, for e.g. $[1, 3, 3, 1]$ and $[6, 2, 6]$ are palindromic.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the minimum number of operations to make $A$ palindromic.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \le A_i \le 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
3 7 6 4
5
1 4 5 4 1
5
1 2 3 4 5
```

**Output**

```text
2
0
4
```

**Explanation**

**Test Case 1:** We can perform the following operations:
- $[3, \underline{7}, 6, 4] \xrightarrow{i = 2, X = 1, Y = 6} [3, \underline{1}, \underline{6}, 6, 4]$
- $[3, 1, 6, 6, \underline{4}] \xrightarrow{i = 5, X = 1, Y = 3} [3, 1, 6, 6, \underline{1}, \underline{3}]$

**Test Case 2:** $A$ is already palindromic.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 7 6 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
1 4 5 4 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPLITPAL)

[Contest: Division 1](https://www.codechef.com/START66A/problems/SPLITPAL)

[Contest: Division 2](https://www.codechef.com/START66B/problems/SPLITPAL)

[Contest: Division 3](https://www.codechef.com/START66C/problems/SPLITPAL)

[Contest: Division 4](https://www.codechef.com/START66D/problems/SPLITPAL)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1540

#
[](#prerequisites-3)PREREQUISITES:

Two pointers or deques

#
[](#problem-4)PROBLEM:

Given an array A, in one move you can pick any A_i and split it into X and Y such that X+Y=A_i.

Find the minimum number of moves to make A a palindrome.

#
[](#explanation-5)EXPLANATION:

Let’s look at the two end elements, i.e, A_1 and A_N.

If A_1 = A_N, we can ignore them and continue on with the rest of the array: we now deal with N-2 elements.

Otherwise, suppose A_1 \lt A_N. Note that we have to perform at least one move on A_N to make the endpoints equal.

So, let’s perform this move: split A_N into (A_N - A_1) and A_1.

Now the endpoints of the array are equal, so we can continue on with the rest of the array. However, notice that we added the new element A_N - A_1 to the array, which we also need to take care of. So, we deal with N-1 elements now.

The A_1 \gt A_N case can be handled similarly: we just need to insert A_1 - A_N at the start of the array instead.

In either case, the array length decreases by at least 1, so the process will be done at most N times before we end. If we can simulate this algorithm fast enough, we are done.

Implementing this by deleting from arrays/vectors/etc will lead to a solution in \mathcal{O}(N^2) because it’s simply not possible to easily insert/delete elements at the beginning.

However, there are a couple of ways to overcome this:

- Perhaps the simplest way is to just use a data structure that *does* allow for quick insertion/deletion at both ends: a deque.

- With a deque, implementation becomes extremely easy: while there is more than one element, compare the front and back elements, then insert the appropriate new element to either the front or back.

- It’s also possible to implement this using two pointers (which really just simulates a deque on an array anyway):

- Start with L = 1, R = N.

- At each step, compare A_L and A_R.

- Deleting elements can be simulated by increasing L/decreasing R

- Adding a new element at the front/back can be done by decreasing L/increasing R and then setting A_L or A_R appropriately.

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
    int n = readIntLn(1, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e5);
    int L = 0, R = n - 1, ans = 0;
    while(L < R)
    {
        if(a[L] == a[R])
            L++, R--;
        else if(a[L] < a[R])
            a[R] -= a[L], L++, ans++;
        else
            a[L] -= a[R], R--, ans++;
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
    assert(sumN <= 2e5);
    return 0;
}
``

Editorialist's code (C++, deque)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	while (t--) {
	    int n; cin >> n;
	    deque<int> dq;
	    for (int i = 0; i < n; ++i) {
	        int x; cin >> x;
	        dq.push_back(x);
	    }
	    int ans = 0;
	    while (dq.size() > 1) {
	        int x = dq.front(), y = dq.back();
	        dq.pop_front(); dq.pop_back();
	        if (x == y) continue;
	        ++ans;
	        if (x < y) dq.push_back(y-x);
	        else dq.push_front(x-y);
	    }
	    cout << ans << '\n';
	}
	return 0;
}
``

Editorialist's code (Python, 2-pointers)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    L, R = 0, n-1
    ans = 0
    while L < R:
        if a[L] == a[R]:
            L += 1
            R -= 1
        elif a[L] < a[R]:
            a[R] -= a[L]
            L += 1
            ans += 1
        else:
            a[L] -= a[R]
            R -= 1
            ans += 1
    print(ans)
``

</details>
