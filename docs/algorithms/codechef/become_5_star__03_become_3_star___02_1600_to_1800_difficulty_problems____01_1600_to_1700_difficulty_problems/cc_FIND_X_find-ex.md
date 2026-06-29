# Find eX

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIND_X |
| Difficulty Rating | 1651 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [FIND_X](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/FIND_X) |

---

## Problem Statement

Chef has $4$ positive integers $A$, $B$, $C$, and $D$ such that $A$ $\%$ $B=C$ $\%$ $D$.

Find the **smallest positive** integer $X$ such that $(A+X)$ $\%$ $B=(C+X)$ $\%$ $D$ holds.

It is guaranteed that such $X$ always exists.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $A$, $B$, $C$, and $D$.

---

## Output Format

For each test case, print a single line containing one integer — $X$, the smallest integer satisfying the conditions.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B, C, D \leq 10^9$
- $A$ $\%$ $B = C$ $\%$ $D$

---

## Examples

**Example 1**

**Input**

```text
3
4 7 4 8
5 1 8 2
3 2 4 3
```

**Output**

```text
1
2
5
```

**Explanation**

**Test case $1$:** The smallest $X$ satisfying the equation is $1$, as $(4+1)$ $\%$ $7=(4+1)$ $\%$ $8 = 5$.

**Test case $2$:** The smallest $X$ satisfying the equation is $2$, as $(5+2)$ $\%$ $1=(8+2)$ $\%$ $2 = 0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 7 4 8
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5 1 8 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3 2 4 3
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIND_X)

[Contest: Division 1](https://www.codechef.com/START82A/problems/FIND_X)

[Contest: Division 2](https://www.codechef.com/START82B/problems/FIND_X)

[Contest: Division 3](https://www.codechef.com/START82C/problems/FIND_X)

[Contest: Division 4](https://www.codechef.com/START82D/problems/FIND_X)

***Author:*** [shubham_grg](https://www.codechef.com/users/shubham_grg)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1651

#
[](#prerequisites-3)PREREQUISITES:

Basic math

#
[](#problem-4)PROBLEM:

Given integers A, B, C, D such that A\bmod B = C\bmod D, find the smallest positive integer X such that (A+X)\bmod B = (C+X)\bmod D

#
[](#explanation-5)EXPLANATION:

tl;dr

The answer is either 1 or \text{lcm}(B, D) - (A\bmod C).

First, notice that the actual values of A and C don’t matter: only their remainders when divided by B and D, respectively.

So, let’s replace A with (A\bmod B) and C with (C\bmod D). In particular, this ensures that A\lt B, C\lt D, and A = C.

Now, note that a lot of the time we can just choose X = 1.

In fact, as long as A+1 \lt B and C+1 \lt D, we can choose X = 1 (since A = C, A+1 = C+1 and both these values don’t exceed their respective modulos).

X = 1 also works when *both* A+1 = B and C+1 = D hold, since both values become 0 in that case.

So, we only need to solve for the case when X = 1 *doesn’t* work, i.e, exactly one of A = B-1 or C = D-1 holds.

Let’s do a bit of math.

Consider an integer X for which equality holds.

We have (A+X)\bmod B = (C+X)\bmod D.

Writing out this in terms of remainders, there exist three integers p, q, r such that

- A+X = pB + r

-
C+X = qD + r

Note that r is common.

It’s clearly optimal to choose r = 0 (if it was anything higher, X - 1 would work too so X wouldn’t be minimal).

This gives us A+X = pB and C+X = qD.

However, notice that we have A = C (from our replacement in the very first step), so this means A+X = pB = qD.

In particular, A+X must be a multiple of both B and D.

The smallest such integer is, by definition, \text{lcm}(B, D).

So, we can choose X+A = \text{lcm}(B, D), which gives us X = \text{lcm}(B, D) - A as our answer.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\log\min(B,D)) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main() {
	// your code goes here

	int t; cin>>t;
	assert(t<=1e5);
	while(t--)
	{
	    ll A, B, C, D; cin>>A>>B>>C>>D;

	    assert(A>0 && A<=1e9);
	    assert(B>0 && B<=1e9);
	    assert(C>0 && C<=1e9);
	    assert(D>0 && D<=1e9);
	    assert(A%B==C%D);

	    A%=B, C%=D;

	    if((A+1)%B==(C+1)%D) cout<<"1\n";
	    else
	    {
	        ll ans=B*D/__gcd(B, D)-A;
	        cout<<ans<<"\n";
	    }
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

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
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

pair<long long, long long> inv_gcd(long long a, long long b) {
    a = a % b;
    if (a == 0) {
        return {b, 0};
    }
    long long s = b, t = a;
    long long m0 = 0, m1 = 1;
    while (t) {
        long long u = s / t;
        s -= t * u;
        m0 -= m1 * u;
        auto tmp = s;
        s = t;
        t = tmp;
        tmp = m0;
        m0 = m1;
        m1 = tmp;
    }
    if (m0 < 0) {
        m0 += b / s;
    }
    return {s, m0};
}

pair<long long, long long> crt(vector<long long> r, vector<long long> m) {
    int n = (int) r.size();
    long long r0 = 0, m0 = 1;
    for (int i = 0; i < n; i++) {
        long long r1 = r[i] % m[i], m1 = m[i];
        if (m0 < m1) {
            swap(r0, r1);
            swap(m0, m1);
        }
        if (m0 % m1 == 0) {
            if (r0 % m1 != r1) {
                return {0, 0};
            }
            continue;
        }
        long long g, im;
        tie(g, im) = inv_gcd(m0, m1);
        long long u = (m1 / g);
        if ((r1 - r0) % g) {
            return {0, 0};
        }
        long long x = (r1 - r0) / g % u * im % u;
        r0 += x * m0;
        m0 *= u;
        if (r0 < 0) {
            r0 += m0;
        }
    }
    return {r0, m0};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    while (tt--) {
        long long a = in.readLong(1, 1e9);
        in.readSpace();
        long long b = in.readLong(1, 1e9);
        in.readSpace();
        long long c = in.readLong(1, 1e9);
        in.readSpace();
        long long d = in.readLong(1, 1e9);
        in.readEoln();
        a %= b;
        c %= d;
        assert(a == c);
        if ((a + 1) % b == (c + 1) % d) {
            cout << 1 << '\n';
            continue;
        }
        a = (b - a) % b;
        c = (d - c) % d;
        auto p = crt({a, c}, {b, d});
        if (!p.first) {
            p.first += p.second;
        }
        cout << p.first << '\n';
    }
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``import math
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if (a+1)%b == (c+1)%d: print(1)
    else: print(b*d//math.gcd(b, d) - a%b)
``

</details>
