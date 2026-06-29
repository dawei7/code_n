# Maximal Expression

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXIMALEXP |
| Difficulty Rating | 2127 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAXIMALEXP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAXIMALEXP) |

---

## Problem Statement

You are given two integers $N$ and $K$.

Let $F(X) = (X \bmod K)\times ((N-X)\bmod K)$, where $\bmod$ denotes the [modulo operator](https://en.wikipedia.org/wiki/Modulo).

Find an integer $X$ such that the value of $F(X)$ is the **maximum** over all $0\le X \le N$.
If there are multiple answers, you may print any.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two integers $N$ and $K$.

---

## Output Format

For each testcase, print a single integer $X$ $(0\leq X\leq N)$ such that the value of $F(X)$ is the maximum over all possible $X$ from $0$ to $N$.

If there are multiple answers, you may print any.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq N \leq 10^9$
- $1 \leq K \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
5 2
4 7
8 3
```

**Output**

```text
0
2
4
```

**Explanation**

**Test case $1$:** $F(X)=0$ for all $0\leq X\leq 5$.

**Test case $2$:**
- $F(0) = (0\bmod 7)\times(4\bmod 7) = 0$
- $F(1) = (1\bmod 7)\times(3\bmod 7) = 3$
- $F(2) = (2\bmod 7)\times(2\bmod 7) = 4$
- $F(3) = (3\bmod 7)\times(1\bmod 7) = 3$
- $F(4) = (4\bmod 7)\times(0\bmod 7) = 0$

So, $X=2$ is the only correct answer.

**Test case $3$:**
- $F(X) = 0$ for $X\in\{0,2,3,5,6,8\}$
- $F(X) = 1$ for $X\in\{1,4,7\}$

So, $1$, $4$ and $7$ are all correct answers.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 7
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8 3
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXIMALEXP)

[Contest: Division 1](https://www.codechef.com/START107A/problems/MAXIMALEXP)

[Contest: Division 2](https://www.codechef.com/START107B/problems/MAXIMALEXP)

[Contest: Division 3](https://www.codechef.com/START107C/problems/MAXIMALEXP)

[Contest: Division 4](https://www.codechef.com/START107D/problems/MAXIMALEXP)

***Author:*** [munch_01](https://www.codechef.com/users/munch_01)

***Preparer:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2127

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given N and K, define the function f(x) = (x\bmod K) \times ((N-x)\bmod K).

Find any 0 \leq x \leq N that maximizes f(x).

# [](#explanation-5)EXPLANATION:

N can be quite large, so of course trying every x is out of the question.

Instead, let’s attempt to reduce the number of x we need to check.

One way to build intuition for this is to look at the case when K \gt N, in which case x\bmod K = x and (N-x)\bmod K = (N-x) (since they’re both less than K already).

This results in f(x) = x\cdot (N-x), and it’s not hard to see that this function is maximized at x = \frac{N}{2} (or rather, the nearest integer to \frac{N}{2}).

For example, a quick way of seeing it is to observe that when x \lt N-x, we have x\cdot (N-x) \leq (x+1)\cdot (N-x-1), so it’s always better to bring x closer to N-x.

In fact, this idea applies to the case when K \leq N as well!

That is, the choice of x that maximizes f(x) will be such that x\bmod K and (N-x) \bmod K have a difference of at most 1.

We just need to figure out when this is possible at all, i.e, which x satisfy this condition.

It turns out there are only two cases:

- The first is x = \frac{N\bmod K}{2}

This is the direct generalization of what we had for the N\lt K case, where here we instead start at 0 and N\bmod K and keep moving them closer towards each other.

- The second is to just move in the other direction! That is, the point x = \frac{(N\bmod K) + K}{2}.

This is what we get by starting at N\bmod K and K (which is equivalent to 0 modulo K) and moving them closer to each other.

Note that to have this option, you do need to verify that x \leq N - it might not be the case if N is too small.

Now that you have (at most) two options for x, simply evaluate f(x) at both of them and choose the best one.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE

Tester's code (C++)
``// Input Checker
// Input verification
#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

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

	auto readIntVec(int n, int minv, int maxv) {
		assert(n >= 0);
		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readInt(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
		}
		return v;
	}

	auto readLongVec(int n, long long minv, long long maxv) {
		assert(n >= 0);
		vector<long long> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readLong(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
		}
		return v;
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

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	input_checker inp;

	int t = inp.readInt(1, 1e5); inp.readEoln();
	while (t--) {
		int n = inp.readInt(0, 1e9); inp.readSpace();
		int b = inp.readInt(1, 1e9); inp.readEoln();
		int ans=((n%b)/2);
		if(n>=b && n%b!=b-1)
		ans+=((b+1)/2);
		cout<<ans<<"\n";
	}
	inp.readEof();
}
``

Editorialist's code (Python)
``def f(x, n, k):
    return (x%k) * ((n-x)%k)

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = (n%k)//2
    what = (k+n%k)//2
    if what <= n and f(what, n, k) > f(ans, n, k): ans = what
    print(ans)
``

</details>
