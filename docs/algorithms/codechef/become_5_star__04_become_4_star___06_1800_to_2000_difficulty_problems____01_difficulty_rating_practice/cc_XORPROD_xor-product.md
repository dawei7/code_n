# XOR Product

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORPROD |
| Difficulty Rating | 1845 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [XORPROD](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/XORPROD) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

He can modify this array by applying a special operation **any** number of times. In one operation, he can:
- Select two indices $i$ and $j$ $(1\le i \lt j \le |A|)$.
- Append $A_i \oplus A_j$ to the end of the array, where $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)
- Remove $A_i$ and $A_j$ from the array.

Chef wants to **maximize** the product of all the elements of the array after applying these operations.

Help Chef determine the **maximum product** he can achieve by applying this operation any (possibly zero) number of times. As this number can be large, print it modulo $998244353$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in the array.
    - The second line consists of $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the elements of the array initially.

---

## Output Format

For each test case, output the maximum product he can achieve modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 5\cdot 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 2 1 2
2
3 3
2
2 1
```

**Output**

```text
9
9
3
```

**Explanation**

**Test case $1$:** Chef can make the following operations:
- Operation $1$: Choose $i = 1$ and $j = 2$, append $A_1\oplus A_2 = 1\oplus 2 = 3$ to the end of the array and remove elements $A_1$ and $A_2$. Thus, the array becomes $[1, 2, 3]$.
- Operation $2$: Choose $i = 1$ and $j = 2$, append $A_1\oplus A_2 = 1\oplus 2 = 3$ to the end of the array and remove elements $A_1$ and $A_2$. Thus, the array becomes $[3, 3]$.

The product of all elements of the array is $3\times 3 = 9$. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.

**Test case $2$:** The product of all elements of the array is $3\times 3 = 9$. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.
Thus, Chef does not need to perform any operations.

**Test case $3$:** Chef can make the following operation:
- Operation $1$: Choose $i = 1$ and $j = 2$, append $A_1\oplus A_2 = 1\oplus 2 = 3$ to the end of the array and remove elements $A_1$ and $A_2$. Thus, the array becomes $[3]$.

The product of all elements is $3$. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
2
3 3
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
2
2 1
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

[Practice](https://www.codechef.com/problems/XORPROD)

[Contest: Division 1](https://www.codechef.com/START68A/problems/XORPROD)

[Contest: Division 2](https://www.codechef.com/START68B/problems/XORPROD)

[Contest: Division 3](https://www.codechef.com/START68C/problems/XORPROD)

[Contest: Division 4](https://www.codechef.com/START68D/problems/XORPROD)

***Author:*** [tejas10p](https://www.codechef.com/users/tejas10p)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1845

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

Given an array A, in one move you can choose x, y \in A, delete them, and add x\oplus y to A.

Maximize the product of A.

#
[](#explanation-5)EXPLANATION:

A little analysis of how the operation affects the product of all the elements should tell you that it’s almost never optimal to replace two elements.

In fact, it’s optimal to replace x and y with x\oplus y *if and only if* x = 1 and y is even.

Why?

This can be seen somewhat intuitively by looking at just two elements.

Let x \leq y, and we want to decide whether to operate on x and y or not.

First, note that we have x\oplus y \lt 2y, which should both be obvious to see by looking at the bits independently.

Now,

- If we don’t operate on x and y, we contribute xy to the product.

- If we do operate on them, we contribute x\oplus y \lt 2y to the product.

In particular, if xy \geq 2y, i.e, x \geq 2, then it’s always better to *not* perform the operation.

This forces x = 1.

Now we have to decide which y give us 1\oplus y \gt 1\cdot y = y. Note that:

- If y is even, 1\oplus y = y+1

- If y is odd, 1\oplus y = y-1

This tells us that x = 1 and y being even is the *only* optimal case to perform an operation on two elements.

It’s somewhat reasonable to expect this to hold when we need to perform more than one move, but a lot less obvious why: after all, the order of moves matters, and maybe we want to perform one ‘bad’ move to be able to get to a ‘good’ one later.

It so happens that this is never the case. A slightly more detailed proof is attached below if you’re interested.

More detailed proof

Let B = [B_1, B_2, \ldots, B_k] be the final array, after we have performed some operations.

Note that B_i = A_{i_1} \oplus A_{i_2} \oplus \ldots A_{i_r} for some indices i_1, \ldots, i_r.

Let’s call each A_{i_j} a *component* of B_i.

Suppose there exists a B_i such that it has at least two components that are \geq 2. W.l.o.g let A_{i_1} \geq 2.

Then, we can instead perform operations so that we end up with B_i \oplus A_{i_1} and A_{i_1} instead of just B_i; and this gives us a strictly higher product.

So, an optimal solution will never have such a B_i.

Now suppose some B_i has \geq 2 components that are 1.

Then, we can remove two ones from this component (which doesn’t change its xor) and keep those ones as two more separate components: this doesn’t affect the product.

So, there exists an optimal solution in which each B_i has at most one 1, and at most one value \geq 2.

Now consider B_i = 1 \oplus y where y \geq 2.

As we noted above, if y is odd it’s better to have y and 1 separately.

So, an optimal solution can only have B_i that are either single elements, or 1 \oplus y for even y.

This completes the proof.

With this information in hand, let’s now get to actually solving the problem.

We can simply simulate the process: as long as we have at least one 1 and one even number remaining, perform an operation on them.

All that remains is to decide which even number to operate on at each step. This is simple: choose the smallest remaining even number.

Why?

Note that we’re choosing x =1 and even y, which means we’re removing 1\cdot y from the product and multiplying it by y+1 instead. So, our product is multiplied by \frac{y+1}{y}.

\frac{y+1}{y} is larger the smaller y is, so it’s optimal to choose the smallest y we can (while ensuring it’s even).

Implementing this is fairly straightforward: count the number of 1's in the sequence, then sort the even numbers and keep choosing the smallest one of them to operate on while there are remaining 1's.

Note that operating on an even number turns it into an odd number so the list doesn’t need to be updated.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#define mod 998244353
using namespace std;

int main() {
    //freopen("inp4.in", "r", stdin);
    //freopen("out4.out", "w", stdout);
    int t;
    cin >> t;
    assert(t > 0 && t < 50000);
    while(t--) {
        int n;
        cin >> n;
        assert(n > 0 && n <= 100000);
        long long int a[n];
        int ones = 0;
        priority_queue<long long int> pq;
        long long int ans = 1;
        for(int i = 0; i < n; i++) {
            cin >> a[i];
            assert(a[i] > 0 && a[i] <= 1000000000);
            if(a[i]&1) {
                if(a[i] == 1) ones++;
                ans *= a[i];
                ans %= mod;
            } else pq.push(-a[i]);
        }
        while(ones && !pq.empty()) {
            int top = -pq.top();
            pq.pop();
            ones--;
            ans *= (top + 1);
            ans %= mod;
        }
        while(!pq.empty()) {
            ans *= (-pq.top());
            pq.pop();
            ans %= mod;
        }
        cout << ans << "\n";
    }
}
``

Tester's code (C++)
``#include <bits/stdc++.h>

using namespace std;

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

template<long long mod>
struct modular {
    long long value;

    modular(long long x = 0) {
        value = x % mod;
        if (value < 0) value += mod;
    }

    modular &operator+=(const modular &other) {
        if ((value += other.value) >= mod) value -= mod;
        return *this;
    }

    modular &operator-=(const modular &other) {
        if ((value -= other.value) < 0) value += mod;
        return *this;
    }

    modular &operator*=(const modular &other) {
        value = value * other.value % mod;
        return *this;
    }

    modular &operator/=(const modular &other) {
        long long a = 0, b = 1, c = other.value, m = mod;
        while (c != 0) {
            long long t = m / c;
            m -= t * c;
            swap(c, m);
            a -= t * b;
            swap(a, b);
        }
        a %= mod;
        if (a < 0) a += mod;
        value = value * a % mod;
        return *this;
    }

    friend modular operator+(const modular &lhs, const modular &rhs) { return modular(lhs) += rhs; }

    friend modular operator-(const modular &lhs, const modular &rhs) { return modular(lhs) -= rhs; }

    friend modular operator*(const modular &lhs, const modular &rhs) { return modular(lhs) *= rhs; }

    friend modular operator/(const modular &lhs, const modular &rhs) { return modular(lhs) /= rhs; }

    modular &operator++() { return *this += 1; }

    modular &operator--() { return *this -= 1; }

    modular operator++(int) {
        modular res(*this);
        *this += 1;
        return res;
    }

    modular operator--(int) {
        modular res(*this);
        *this -= 1;
        return res;
    }

    modular operator-() const { return modular(-value); }

    bool operator==(const modular &rhs) const { return value == rhs.value; }

    bool operator!=(const modular &rhs) const { return value != rhs.value; }

    bool operator<(const modular &rhs) const { return value < rhs.value; }
};

template<long long mod>
string to_string(const modular<mod> &x) {
    return to_string(x.value);
}

template<long long mod>
ostream &operator<<(ostream &stream, const modular<mod> &x) {
    return stream << x.value;
}

template<long long mod>
istream &operator>>(istream &stream, modular<mod> &x) {
    stream >> x.value;
    x.value %= mod;
    if (x.value < 0) x.value += mod;
    return stream;
}

constexpr long long mod = 998244353;
using mint = modular<mod>;

mint power(mint a, long long n) {
    mint res = 1;
    while (n > 0) {
        if (n & 1) {
            res *= a;
        }
        a *= a;
        n >>= 1;
    }
    return res;
}

vector<mint> fact(1, 1);
vector<mint> finv(1, 1);

mint C(int n, int k) {
    if (n < k || k < 0) {
        return mint(0);
    }
    while ((int) fact.size() < n + 1) {
        fact.emplace_back(fact.back() * (int) fact.size());
        finv.emplace_back(mint(1) / fact.back());
    }
    return fact[n] * finv[k] * finv[n - k];
}

int main() {
    input_checker in;
    int tt = in.readInt(1, 5e4);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(2, 1e5);
        in.readEoln();
        sn += n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            a[i] = in.readInt(1, 1e9);
            (i == n - 1 ? in.readEoln() : in.readSpace());
        }
        vector<vector<int>> b(2);
        int c = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == 1) {
                c++;
            } else {
                b[a[i] % 2].emplace_back(a[i]);
            }
        }
        sort(b[0].begin(), b[0].end());
        for (int i = 0; i < min(c, (int) b[0].size()); i++) {
            b[0][i]++;
        }
        mint ans = 1;
        for (int i = 0; i < 2; i++) {
            for (int j: b[i]) {
                ans *= j;
            }
        }
        cout << ans << '\n';
    }
    cerr << sn << endl;
    assert(sn <= 3e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``mod = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    evens, odds = sorted([x for x in a if x%2 == 0]), sorted([x for x in a if x%2 == 1])
    p = q = 0
    while p < len(odds) and q < len(evens):
        if odds[p] != 1: break
        evens[q] += 1
        p += 1
        q += 1
    ans = 1
    for i in range(p, len(odds)): ans = (ans * odds[i])%mod
    for x in evens: ans = (ans * x)%mod
    print(ans)
``

</details>
