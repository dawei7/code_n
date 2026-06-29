# Crazy Bishops on Chessboard

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CRZBISHOP |
| Difficulty Rating | 1351 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CRZBISHOP](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CRZBISHOP) |

---

## Problem Statement

Chef has a matrix of size $N\times N$.
There are $N$ [bishops](https://en.wikipedia.org/wiki/Bishop_(chess)) placed on the matrix, in a zig-zag fashion, at the cells $(1, 1), (2, 2), (1, 3), (2, 4), (1, 5), \dots,$ and so on.

For example, for $N = 4$, the matrix looks like:

Your task is to determine the **minimum** number of moves required to reach a position where each cell $(i, i)$ contains exactly one bishop for all $1\le i \le N$.

For the above mentioned case of $N = 4$, the final position should be:

Note:
- Bishops can only move diagonally. In one move, you can place exactly one bishop from its initial cell to any other cell lying on either of its diagonals.
- Bishops cannot move outside the matrix.
- No cell can contain more than one bishop at a time.
- A bishop cannot jump over another bishop.

---

## Input Format

- The first line of input will contain a single integer $T$ - the number of test cases.
- Each test case consists of a single integer $N$ - the size of the matrix.

---

## Output Format

For each test case, output a single integer, the **minimum** number of moves required to reach a position where each cell $(i, i)$ contains exactly one bishop for all $1\le i \le N$.

---

## Constraints

- $1 \leq T \leq 10^{4}$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
1
4
2
6
```

**Output**

```text
0
3
0
6
```

**Explanation**

**Test case $1$:** The bishop is already in its final position. Thus, no moves are required.

**Test case $2$:** We require a minimum of $3$ moves to reach the final position:
- Move bishop from $(2,2)$ to $(4, 4)$.
- Move bishop from $(1,3)$ to $(2, 2)$.
- Move bishop from $(2,4)$ to $(3, 3)$.

**Test case $3$:** The bishops are already in their final position. Thus, no moves are required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
2
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
6
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CRZBISHOP)

[Contest: Division 1](https://www.codechef.com/START85A/problems/CRZBISHOP)

[Contest: Division 2](https://www.codechef.com/START85B/problems/CRZBISHOP)

[Contest: Division 3](https://www.codechef.com/START85C/problems/CRZBISHOP)

[Contest: Division 4](https://www.codechef.com/START85D/problems/CRZBISHOP)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1351

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

There’s an N\times N chessboard with N bishops on it.

Initially, the bishops are at positions (1, 1), (2, 2), (1, 3), (2, 4), (1, 5), \ldots

You want their final positions to be (1, 1), (2, 2), (3, 3), (4, 4), \ldots

What’s the minimum number of moves needed to achieve this?

#
[](#explanation-5)EXPLANATION:

If N \leq 2, the answer is 0 because the first 2 bishops are already in positions.

For N \gt 2, working out a few small cases on paper might give you the following strategy:

- For each bishop that’s initially on (2, x), use one move to bring it to the required diagonal.

- Then, for each bishop that’s initially on (1, x), use two moves to bring it to the required diagonal.

This strategy would take a + 2\cdot b moves, where a = \left\lfloor \frac{N}{2} \right\rfloor - 1 is the number of bishops initially on the second row (that need to be moved), and b = \left\lceil \frac{N}{2} \right\rceil - 1 is the number of bishops initially on the first row (that need to be moved).

In fact, this is optimal!

Proof

For N \leq 2,, the fact that 0 moves are required is obvious.

For N \gt 2, note that each bishop has a unique cell on the main diagonal that they can reach in one move.

In particular, the bishops on (2, 2k) and (1, 2k+1) share the same main diagonal cell for any k \geq 1.

So, each of these bishops need at least one move, and at least one of them needs another; because if they both used one move they’d end up in the same cell, which is not allowed.

This gives us a lower bound on the number of moves needed, and it’s easy to see that our strategy attains this lower bound and is hence optimal.

It’s not hard (but also not necessary) to further simplify this into a formula based on N:

-

If N = 1, the answer is 0.

-

If N is odd, the answer is \displaystyle\frac{3N-5}{2}

-

If N is even, the answer is \displaystyle\frac{3N-6}{2}

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``/* DK....DAIICT */

#include <bits/stdc++.h>
using namespace std;

#define FAST                      \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0)

long long pow_s(long long a, long long b)
{
    long long res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}

long long pow_m(long long a, long long b, long long m)
{
    a %= m;
    long long res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
// string s = bitset<8>(n).to_string();    int to binary string
long long gcd(long long a, long long b)
{
    while (b)
    {
        a %= b;
        swap(a, b);
    }
    return a;
}
long long lcm(long long a, long long b)
{
    return a / gcd(a, b) * b;
}

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;

const ll MOD = 1e9 + 7;

void solve()
{
    ll n;
    cin >> n;
    if (n == 1)
    {
        cout << "0" << endl;
        return;
    }
    if (n & 1)
        cout << (3 * n - 5) / 2 << endl;
    else
        cout << (3 * n - 6) / 2 << endl;
}

int32_t main()
{
    FAST;
    ll t;
    cin >> t;
    while (t--)
    {
        solve();
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

int main() {
    input_checker in;
    int tt = in.readInt(1, 10000);
    in.readEoln();
    while (tt--) {
        long long n = in.readInt(1, 1e9);
        in.readEoln();
        long long ans = 0;
        while (n > 2) {
            if (n == 3) {
                ans += 2;
                n--;
            } else if (n == 4) {
                ans += 1;
                n--;
            } else {
                long long k = (n - 2) / 2;
                ans += 3 * k;
                n -= 2 * k;
            }
        }
        cout << ans << '\n';
    }
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    top, bottom = n//2, (n+1)//2
    print(max(0, top-1 + 2*(bottom-1)))
``

</details>
