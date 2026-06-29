# Potato to Gold

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SIMPLEARRAY |
| Difficulty Rating | 2326 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SIMPLEARRAY](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SIMPLEARRAY) |

---

## Problem Statement

You are given an array $A$ of $N$ integers and an integer $K$. Find the number of (**possibly empty**) [subsequences](https://en.wikipedia.org/wiki/Subsequence) of $A$ such that no two elements in the subsequence have a sum that is divisible by $K$.

Two subsequences are considered distinct if they are made up of different indices. For example, $A = [1, 2, 1, 2]$ contains $[1, 2]$ as a subsequence three times, and all $3$ must be counted separately in the answer.

More formally,
- Let $S = \{x_1, x_2, \ldots, x_m\}$ be a (possibly empty) set such that $1 \leq x_1 \lt x_2 \lt \ldots \lt x_m \leq N$.
- $S$ is said to be *good* if $A_{x_i} + A_{x_j}$ is not divisible by $K$ for any $1 \leq i \lt j \leq m$. In particular, any subsequence of size $\leq 1$ is *good*.
- Your task is to count the number of *good* sets.

Since the answer can be very large, print it modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space separated integers, $N$ and $K$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$

---

## Output Format

For each test case, output on a new line number of subsequences satisfying the condition, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ and $K$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
3 4
4 5 7
5 4
1 2 3 4 5
5 3
1 2 3 4 5
```

**Output**

```text
6
20
14
```

**Explanation**

**Test case $1$:** Here, $K = 4$. There are $8$ subsequences of the array, and they are considered as follows:
- $[]$: the empty subsequence. It satisfies the condition.
- $[4], [5], [7]$: size $1$ subsequences, all are good.
- $[4, 5]$: good, because $4+5 = 9$ is not a multiple of $4$
- $[4, 7]$: good, because $4+7 = 11$ is not a multiple of $4$
- $[5, 7]$: not good, because $5+7=12$ is a multiple of $4$.
- $[4, 5, 7]$: not good, again because it contains $5$ and $7$.

So, $6$ of the subsequences are good.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4
4 5 7
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
5 4
1 2 3 4 5
```

**Output for this case**

```text
20
```



#### Test case 3

**Input for this case**

```text
5 3
1 2 3 4 5
```

**Output for this case**

```text
14
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SIMPLEARRAY)

[Contest: Division 1](https://www.codechef.com/START65A/problems/SIMPLEARRAY)

[Contest: Division 2](https://www.codechef.com/START65B/problems/SIMPLEARRAY)

[Contest: Division 3](https://www.codechef.com/START65C/problems/SIMPLEARRAY)

[Contest: Division 4](https://www.codechef.com/START65D/problems/SIMPLEARRAY)

***Author:*** [Sahil Tiwari](https://www.codechef.com/users/still_me)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2326

#
[](#prerequisites-3)PREREQUISITES:

Frequency arrays, Basic combinatorics

#
[](#problem-4)PROBLEM:

You are given an array A and an integer K. Count the number of subsequences that don’t contain any pair whose sum is divisible by K.

#
[](#explanation-5)EXPLANATION:

First, notice that the condition "A_i + A_j is divisible by K" can be written as A_i + A_j \equiv 0 \pmod K.

In particular, we can work with all the array elements modulo K so that they’re all between 0 and K-1.

Now, consider what happens when we have x+y \equiv 0 \pmod K when both x and y are less than K. There are three possibilities:

- First, we can have x = y = 0

- Second, if K is even we can have x = y = K/2

- Finally, if neither of the above hold, we must have y = K-x; and in particular x \neq y.

Let’s leave the first two cases alone for now, and look at the third.

For convenience, let x \lt K-x.

Note that for each x, any good subsequence can have *either* some occurrences of x, *or* some occurrences of K-x: never both.

In particular, we can take as many x-s as we like, or as many (K-x)-s as we like, without affecting any other sums (since K-(K-x) = x). Essentially, we ‘pair up’ x with K-x, and then different pairs are completely independent.

So, the choices of which of the x's or (K-x)'s we take are completely independent across different x.

This means that any subsequence can be constructed as follows:

- Choose a subset of 1's *or* a subset of K-1's

- Then, choose a subset of 2's *or* a subset of (K-2)'s

- Then, choose a subset of 3's *or* a subset of (K-3)'s

\vdots

Thus, the total number of subsequences can be found by multiplying the number of choices for different x.

This brings us to the questions: how many choices are there for a fixed x?

Answer

Let freq(x) be the number of occurrences of x in the array.

Note that we can choose any subset of the x's, or any subset of the (K-x)'s.

The first one gives us 2^{freq(x)} choices, while the second gives us 2^{freq(K-x)} choices.

The empty set is counted in both, so we need to subtract 1 to avoid overcounting.

This brings the total to 2^{freq(x)} + 2^{freq(K-x)} - 1.

The number of subsequences is thus just the product of (2^{freq(x)} + 2^{freq(K-x)} - 1) across all x such that x \lt K-x.

The only exceptions here are x = 0 and (if K is even) x = K/2, which shouldn’t be included in the above product because they behave slightly differently. Do you see how to deal with them?

Answer

x = 0 and x = K/2 follow a simple rule: there can’t be more than one of each in the subsequence.

So, we have 1+freq(0) choices for 0 (choose none of them, or choose exactly one), and similarly 1 + freq(K/2) choices for K/2.

Multiply these quantities to the previous value to obtain the final answer.

Notice that the value for a given x requires us to compute a power of 2 modulo something.

There are several ways to do this: the simplest is to just precompute the value of 2^x\pmod {MOD} for every 0 \leq x \leq 5\cdot 10^5 before processing any test cases, after which these can be used in \mathcal{O}(1).

Alternately, you can use [binary exponentiation](https://cp-algorithms.com/algebra/binary-exp.html).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N + K) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#define int long long int
using namespace std;

#define mod 1000000007

int power(int a , int b) {
	if(b == 0)
		return 1;
	int res = power(a , b>>1);
	if(b & 1)
		return (res * res % mod) * a % mod;
	return res * res % mod;
}

signed main() {

	int t;
	cin>>t;
	while(t--) {
		int n , k;
		cin>>n>>k;
		vector<int> a(k);
		for(int i=0;i<n;i++) {
			int x;
			cin>>x;
			a[x % k]++;
		}
		// for(auto &i: a)
		// 	cout<<i<<" ";
		// cout<<endl;
		int ans = 1;
		// cout<<power(2 , 2)<<endl;
		for(int i=1;i<(k+1)/2;i++) {
			int c = (power(2 , a[i]) + power(2 , a[k-i]) - 1);
			ans = ans * c % mod;
		}
		if(k % 2 == 0) {
			ans = ans * (a[k/2] + 1) % mod;
		}
		ans = ans * (a[0]+1) % mod;
		cout<<ans<<endl;
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

const long long mod = (int) 1e9 + 7;

struct mint {
    long long value;

    mint(long long x = 0) {
        value = x % mod;
        if (value < 0) value += mod;
    }

    mint &operator+=(const mint &other) {
        if ((value += other.value) >= mod) value -= mod;
        return *this;
    }

    mint &operator-=(const mint &other) {
        if ((value -= other.value) < 0) value += mod;
        return *this;
    }

    mint &operator*=(const mint &other) {
        value = value * other.value % mod;
        return *this;
    }

    mint &operator/=(const mint &other) {
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

    friend mint operator+(const mint &lhs, const mint &rhs) { return mint(lhs) += rhs; }

    friend mint operator-(const mint &lhs, const mint &rhs) { return mint(lhs) -= rhs; }

    friend mint operator*(const mint &lhs, const mint &rhs) { return mint(lhs) *= rhs; }

    friend mint operator/(const mint &lhs, const mint &rhs) { return mint(lhs) /= rhs; }

    mint &operator++() { return *this += 1; }

    mint &operator--() { return *this -= 1; }

    mint operator++(int) {
        mint result(*this);
        *this += 1;
        return result;
    }

    mint operator--(int) {
        mint result(*this);
        *this -= 1;
        return result;
    }

    mint operator-() const { return mint(-value); }

    bool operator==(const mint &rhs) const { return value == rhs.value; }

    bool operator!=(const mint &rhs) const { return value != rhs.value; }

    bool operator<(const mint &rhs) const { return value < rhs.value; }
};

string to_string(const mint &x) {
    return to_string(x.value);
}

ostream &operator<<(ostream &stream, const mint &x) {
    return stream << x.value;
}

istream &operator>>(istream &stream, mint &x) {
    stream >> x.value;
    x.value %= mod;
    if (x.value < 0) x.value += mod;
    return stream;
}

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
        finv.emplace_back(1 / fact.back());
    }
    return fact[n] * finv[k] * finv[n - k];
}

int main() {
    input_checker in;
    int tt = in.readInt(1, 1e4);
    in.readEoln();
    int sn = 0, sk = 0;
    int mn = 2e9, mx = -1;
    while (tt--) {
        int n = in.readInt(1, 1e5);
        in.readSpace();
        int k = in.readInt(1, 5e5);
        in.readEoln();
        sn += n;
        sk += k;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            a[i] = in.readInt(1, 1e9);
            mn = min(mn, a[i]);
            mx = max(mx, a[i]);
            a[i] %= k;
            (i == n - 1 ? in.readEoln() : in.readSpace());
        }
        vector<int> c(k);
        for (int i = 0; i < n; i++) {
            c[a[i]]++;
        }
        mint ans = c[0] + 1;
        for (int i = 1; i < k; i++) {
            int j = k - i;
            if (i == j) {
                ans *= c[i] + 1;
            } else if (i < j) {
                ans *= power(2, c[i]) + power(2, c[j]) - 1;
            }
        }
        cout << ans << '\n';
    }
    assert(sn <= 1e6);
    assert(sk <= 1e6);
    cerr << sn + sk << " " << mn << " " << mx << endl;
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = [0]*k
    for x in a:
        freq[x%k] += 1
    ans = 1
    for i in range(k):
        if i == 0 or 2*i == k:
            ans *= 1 + freq[i]
        else:
            if i > k-i: break
            ans *= pow(2, freq[i], mod) + pow(2, freq[k-i], mod) - 1
        ans %= mod
    print(ans%mod)
``

</details>
