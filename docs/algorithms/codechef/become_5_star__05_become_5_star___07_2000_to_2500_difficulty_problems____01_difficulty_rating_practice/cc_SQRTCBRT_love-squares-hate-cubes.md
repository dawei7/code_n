# Love Squares Hate Cubes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SQRTCBRT |
| Difficulty Rating | 2150 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SQRTCBRT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SQRTCBRT) |

---

## Problem Statement

Kulyash loves **perfect squares** and hates **perfect cubes**.
For any natural number $N$,
$F(N) = \texttt{number of perfect squares smaller than or equal to } N - \texttt{number of positive perfect cubes smaller than or equal to } N$.

Kulyash gives you an integer $X$ and asks you to find the minimum value of $N$, such that $F(N) \geq X$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input.
    - The first and only line of each test case contains an integer $X$.

---

## Output Format

For each test case, output on a new line, the minimum value of $N$ such that $F(N) \geq X$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1
3
3151
```

**Output**

```text
4
25
11397376
```

**Explanation**

**Test case $1$**: There are $2$ perfect squares from $1$ to $4$, and $1$ perfect cube from $1$ to $4$, so $F(4) = 2 - 1 = 1$, as required.

**Test case $2$**: There are $5$ perfect squares from $1$ to $25$, and $2$ perfect cubes from $1$ to $25$, so $F(25) = 5 - 2 = 3$, as required.

**Test case $3$**: There are $3376$ perfect squares from $1$ to $11397376$, and $225$ perfect cubes from $1$ to $11397376$, so $F(11397376) = 3376 - 225 = 3151$, as required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
25
```



#### Test case 3

**Input for this case**

```text
3151
```

**Output for this case**

```text
11397376
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SQRTCBRT)

[Contest: Division 1](https://www.codechef.com/START79A/problems/SQRTCBRT)

[Contest: Division 2](https://www.codechef.com/START79B/problems/SQRTCBRT)

[Contest: Division 3](https://www.codechef.com/START79C/problems/SQRTCBRT)

[Contest: Division 4](https://www.codechef.com/START79D/problems/SQRTCBRT)

***Author:*** [kulyash](https://www.codechef.com/users/kulyash)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Binary search

#
[](#problem-4)PROBLEM:

F(N) denotes the difference between the number of squares and the number of cubes from 1 to N.

Given X, find the smallest value of N such that F(N) \geq X.

#
[](#explanation-5)EXPLANATION:

Problems of the type "find the smallest N such that \ldots" are often solved with binary search.

Unfortunately, that requires the function to be monotonic, and F(N) here isn’t monotonic.

Analyzing how it changes, we can see that:

F(N) = \begin{cases}
F(N-1), & \text{ if } N \text{ is neither a square nor a cube} \\
F(N-1) + 1, & \text{ if } N \text{ is a square but not a cube} \\
F(N-1) - 1, & \text{ if } N \text{ is a cube but not a square} \\
F(N-1), & \text{ if } N \text{ is both a square and a cube}
\end{cases}

In particular, notice that F can only increase at a square number, so the final answer must be a square number.

Further, the fact that cubes are more ‘spread out’ than squares means that F is actually a monotonic function when evaluated on the squares!

That is, we consider the function g(N) = F(N^2) instead, which is increasing.

Proof

It’s enough to prove that there’s at most one cube lying between any two consecutive squares, since this is what makes F increasing on the squares.

So, suppose we have 1\leq x^2 \leq y^3 \leq (y+1)^3. We just need to prove (x+1)^2 \lt (y+1)^3.

This is not hard to do by simple algebraic manipulation.

Expand out (x+1)^2 and (y+1)^3, to obtain (x^2 + 2x + 1) and (y^3 + 3y + 3y^2 + 1).

Comparing their terms, we can see that:

- y^3 \geq x_2

- They both have a 1

-
3y^2 \geq 3x \gt 2x. This follows from the fact that x^2 \leq y^3 means that y^2 \geq x^{4/3} \geq x.

So we have the required inequality.

With this information in hand, the solution is simple: use binary search to find the smallest value of N such that g(N) \geq X; the final answer is then N^2.

This requires us to quickly evaluate g(N) = F(N^2).

Note that the number of squares that are \leq N^2 is simply N, so we just need to count the number of cubes that are \leq N^2.

There are several ways to do this: for example, use `std::cbrtl` or yet another binary search.

###
[](#regarding-precision-6)Regarding precision

You may have encountered precision errors when computing cube roots; luckily, one of the samples was specifically designed to catch several common implementations.

In particular, `cbrt` in C++ or something like `N ** (1 / 3)` in Python have precision issues.

There are several ways to get around this, some being problem dependent:

- If possible, the absolute best solution is to simply not deal with floating-point integers at all. In this problem, the number of cubes \leq N can be computed using a binary search across the integers, so this is the safest way.

-
`cbrtl` in C++ is precise enough to get AC in this task.

- The cube root can be manually adjusted once you compute it: if c is the value you compute as the cube root of N (after rounding) and (c+1)^3 \leq N, then increase c to c+1 instead.

- After computing the cube root, add a small value to it (like 10^{-10}) before rounding to an integer.

#
[](#time-complexity-7)TIME COMPLEXITY

\mathcal{O}(\log^2 X) per testcase.

#
[](#code-8)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() {
    vector<ll>cubes;
    for(ll i=1;i<=1010000;i++)cubes.push_back(i*i*i);
    ll T;
    cin >> T;
    while(T--){
        ll x;
        cin >> x;
        ll l=1;
        ll r=2e9;
        ll ans;
        while(l<=r){
            ll mid=(r+l)/2;
            ll temp=upper_bound(cubes.begin(),cubes.end(),mid*mid)-cubes.begin();
            ll curr=mid-temp;
            if(curr>=x){
                ans=mid*mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        cout << ans << endl;
    }
return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
            now++;
        }
        return now;
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        int nxt = nextDelimiter();
        string res;
        while (pos < nxt) {
            res += buffer[pos];
            pos++;
        }
        // cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string &pattern = "") {
        assert(minl <= maxl);
        string res = readOne();
        assert(minl <= (int) res.size());
        assert((int) res.size() <= maxl);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int minv, int maxv) {
        assert(minv <= maxv);
        int res = stoi(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    long long readLong(long long minv, long long maxv) {
        assert(minv <= maxv);
        long long res = stoll(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    while (tt--) {
        int x = in.readInt(1, 1e9);
        in.readEoln();
        long long low = 0, high = 2e9;
        while (high - low > 1) {
            long long mid = (high + low) >> 1;
            long long cnt = mid;
            long long t = cbrt(mid * mid);
            while ((t + 1) * (t + 1) * (t + 1) <= mid * mid) {
                t++;
            }
            while (t * t * t > mid * mid) {
                t--;
            }
            cnt -= t;
            if (cnt >= x) {
                high = mid;
            } else {
                low = mid;
            }
        }
        cout << high * high << '\n';
    }
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``from bisect import bisect_left
cubes = [i**3 for i in range(1, 1010000)]

for _ in range(int(input())):
	x = int(input())
	lo, hi = 1, 2 * 10**9
	def g(n): # f(n*n)
		return n - bisect_left(cubes, n*n + 1)
	while lo < hi:
		mid = (lo + hi)//2
		if g(mid) >= x: hi = mid
		else: lo = mid+1
	print(lo * lo)
``

</details>
