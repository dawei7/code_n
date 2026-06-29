# Maximize 1s

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAX1S |
| Difficulty Rating | 2255 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAX1S](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAX1S) |

---

## Problem Statement

You are given a binary string $S$. You are allowed to perform the following operation **at most once**:
- Pick some [substring](https://en.wikipedia.org/wiki/Substring) of $S$
- Flip all the values in this substring, i.e, convert $0$ to $1$ and vice versa

For example, if $S = 1\underline{00101}011$, you can pick the underlined substring and flip it to obtain $S = 1\underline{11010}011$.

For the substring of $S$ consisting of all the positions from $L$ to $R$, we define a function $f(L, R)$ to be the number of $1$'s in this substring. For example, if $S = 100101011$, then $f(2, 5) = 1$ and $f(4, 9) = 4$ (the respective substrings are $0010$ and $101011$).

If you perform the given operation optimally, find the **maximum** possible value of
$$
\sum_{L=1}^N \sum_{R=L}^N f(L, R)
$$
that can be obtained. Note that the substring flip operation can be performed **at most once**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input, containing a binary string $S$.

---

## Output Format

For each test case, output on a new line the maximum possible value of $\sum_{L=1}^N \sum_{R=L}^N f(L, R)$ that can be obtained.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq |S| \leq 3\cdot 10^5$
- The sum of $|S|$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
111
000
00100
```

**Output**

```text
10
10
26
```

**Explanation**

**Test case $1$:** There is no need to apply the operation since everything is already a $1$. The answer is thus the sum of:
- $f(1, 1) = 1$
- $f(1, 2) = 2$
- $f(1, 3) = 3$
- $f(2, 2) = 1$
- $f(2, 3) = 2$
- $f(3, 3) = 1$

which is $10$.

**Test case $2$:** Flip the entire string to obtain $111$, whose answer has been computed above.

**Test case $3$:** Flip the entire string to obtain $11011$. The sum of $f(L, R)$ across all substrings is now $26$, which is the maximum possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
111
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
000
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
00100
```

**Output for this case**

```text
26
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAX1S)

[Contest: Division 1](https://www.codechef.com/START63A/problems/MAX1S)

[Contest: Division 2](https://www.codechef.com/START63B/problems/MAX1S)

[Contest: Division 3](https://www.codechef.com/START63C/problems/MAX1S)

[Contest: Division 4](https://www.codechef.com/START63D/problems/MAX1S)

***Author:*** [Arun Sharma](https://www.codechef.com/users/arunsharma_)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2255

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics, [Maximum subarray sum](https://cp-algorithms.com/others/maximum_average_segment.html)

#
[](#problem-4)PROBLEM:

You have a binary string S. At most once, you can pick a substring of S and flip all its characters.

If the substring is chosen optimally, what is the maximum value of the sum of the count of 1's of each substring, across all substrings?

#
[](#explanation-5)EXPLANATION:

Let’s first forget about the flipping operation and try to quickly compute the value for a given string. Obviously iterating over all substrings would take \mathcal{O}(N^2) time, which is too much.

The quantity we want to calculate is the count of 1's in each substring, summed across all substrings.

Let’s look at it from a slightly different perspective: how much does each 1 present in the string ‘contribute’ to the final answer?

Answer

Suppose S_i = 1. S_i then contributes +1 to the final answer exactly once for each subarray it is in.

A simple combinatorial argument tells us that the number of subarrays it is present in equals i\cdot (N-i+1): the left endpoint of the subarray has i choices (1, 2, 3, \ldots, i) and the right has N-i+1 choices (i, i+1, i+2, \ldots, N).

So, let’s define B_i = i\cdot(N-i+1). Then, the answer for S is simply the sum of B_i across all those positions i such that S_i = 1, which can easily be computed in \mathcal{O}(N).

Now let’s look at how flipping can change things:

- If S_i = 1, then flipping this position will *decrease* the answer by B_i (since it used to contribute to the sum, and won’t after the flip).

- If S_i = 0, then flipping this position will *increase* the answer by B_i.

Flipping a substring is then equivalent to adding/subtracting the relevant values of B_i, which is essentially just a subarray sum!

In fact, suppose we define another array C as follows:

-
C_i = +B_i if S_i = 0

-
C_i = -B_i if S_i = 1

Then, it’s easy to see that flipping the range [L, R] in S changes the answer by exactly the subarray sum of C from L to R.

Of course, we want this change to be as large as possible, since our aim is to maximize the answer. This means we want to find the maximum subarray sum of C, which can be done in \mathcal{O}(N) in a variety of ways.

Thus, the final solution is:

- Compute the B and C arrays as mentioned above.

- Using B, compute the answer for S without flips.

- Then, find the maximum subarray sum of C and add it to the answer.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

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
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        string s = in.readString(1, 3e5, "01");
        in.readEoln();
        int n = (int) s.size();
        sn += n;
        vector<long long> a(n);
        long long t = 0;
        for (int i = 0; i < n; i++) {
            long long c1 = (n - i) * 1LL * (i + 1);
            if (s[i] == '0') {
                a[i] = c1;
            } else {
                t += c1;
                a[i] = -c1;
            }
        }
        vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + a[i];
        }
        long long mn = 0;
        long long ans = t;
        for (int i = 0; i < n + 1; i++) {
            mn = min(mn, pref[i]);
            ans = max(ans, t + pref[i] - mn);
        }
        cout << ans << '\n';
    }
    assert(sn <= 3e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	s = input()
	ans = mx = cur = 0
	for i in range(len(s)):
		subarrays = (i+1) * (len(s)-i)
		if s[i] == '1':
			ans += subarrays
			subarrays *= -1
		cur += subarrays
		cur = max(cur, 0)
		mx = max(mx, cur)
	print(ans + mx)
``

</details>
