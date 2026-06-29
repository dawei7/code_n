# Make Them Alike

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALIKE_THEM |
| Difficulty Rating | 2245 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ALIKE_THEM](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ALIKE_THEM) |

---

## Problem Statement

You are given a permutation $P$ of length $N$, an array $A$ of size $N$, and an integer $M$.

Initially, $0 \le A_i \le M$. Consider an array $A'$ obtained from $A$ by replacing all **zeros** in $A$ with **positive** integers **less than or equal to** $M$.

The array $A'$ will then be transformed as follows, in $N$ steps:
- In the $i^{th}$ step, we set $A'_i = A'_{P_i}$.

The initial array $A'$ is said to be *beautiful*, if, after the transformation of $N$ steps, all elements of array $A'$ are **equal**.

Find the number of such *beautiful* arrays $A'$ which can be formed by changing the zeros in array $A$ to any value $\leq M$. Since this number can be huge, print this number modulo $10^9+7$.

Note that a permutation of length $N$ contains of all elements from $1$ to $N$ exactly once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$, the size of the array and the maximum value it can have.
    - The second line of each test case consists of $N$ space-separated integers $P_1, P_2, \ldots, P_N$, the permutation $P$.
    - The third line of each test case consists of $N$ space-separated integers $A_1, A_2, \ldots, A_N$, the initial array $A$.

---

## Output Format

For each test case, output on a new line, the number of such *beautiful* arrays $A'$ which can be formed by changing the zeros in array $A$ to any value $\leq M$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq M \leq 10^9$
- $0 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4 3
2 1 4 3
0 2 0 2
3 2
3 1 2
0 0 0
8 54
8 1 2 4 3 6 7 5
0 0 0 0 0 0 0 0
```

**Output**

```text
9
8
459165024
```

**Explanation**

**Test case $1$:** The given permutation is $[2,1,4,3]$. One of the possible beautiful arrays is: $A' = [1,2,3,2]$. This is obtained by replacing the first $0$ with $1$ and the second $0$ with $3$ in the array $A$.
For the transformation:
- In the first step, $A'_1$ is replaced with $A'_{P_1} = A'_2$, that is $2$. The array becomes $[2,2,3,2]$.
- In the second step, $A'_2$ is replaced with $A'_{P_2} = A'_1$, that is $2$. The array becomes $[2,2,3,2]$.
- In the third step, $A'_3$ is replaced with $A'_{P_3} = A'_4$, that is $2$. The array becomes $[2,2,2,2]$.
- In the fourth step, $A'_4$ is replaced with $A'_{P_4} = A'_3$, that is $2$. The array becomes $[2,2,2,2]$.

Thus, after the transformation, all elements of the array are equal. The other beautiful arrays for this test case are: $[1,2,1,2], [1,2,2,2], [2,2,1,2], [2,2,2,2], [2,2,3,2], [3,2,1,2], [3,2,2,2], [3,2,3,2]$.

There are $9$ beautiful arrays in total.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3
2 1 4 3
0 2 0 2
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
3 2
3 1 2
0 0 0
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
8 54
8 1 2 4 3 6 7 5
0 0 0 0 0 0 0 0
```

**Output for this case**

```text
459165024
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALIKE_THEM)

[Contest: Division 1](https://www.codechef.com/START82A/problems/ALIKE_THEM)

[Contest: Division 2](https://www.codechef.com/START82B/problems/ALIKE_THEM)

[Contest: Division 3](https://www.codechef.com/START82C/problems/ALIKE_THEM)

[Contest: Division 4](https://www.codechef.com/START82D/problems/ALIKE_THEM)

***Authors:*** [shubham_grg](https://www.codechef.com/users/shubham_grg)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

[Functional graphs](https://usaco.guide/silver/func-graphs?lang=cpp)

#
[](#problem-4)PROBLEM:

You have an array A with N elements from 0 to M, and a permutation P of length N.

For each i such that A_i = 0, you must replace it with some integer from 1 to M.

An array is beautiful if the following holds:

- For each i from 1 to N in order, replace A_i with A_{P_i}.

- If this eventually results in all the elements of A becoming equal, A is said to be beautiful.

Count the number of ways of replacing zeros such that the resulting array is beautiful.

#
[](#explanation-5)EXPLANATION:

Let A be the initial array, and B be the array obtained by performing the given operation on A once.

Then, for each 1 \leq i \leq N, there’s a unique position \text{pos}_i such that B_i = A_{\text{pos}_i}

That is, the value ending up at position i has to come from some unique position, which depends only on what P is.

This is useful information to have, so let’s see how we can compute it.

In particular, we can see that:

- If P_i \geq i, then \text{pos}_i = P_i, since position i just directly receives the value at position P_i

- If P_i \lt i, then \text{pos}_i = \text{pos}_{P_i}, because P_i receives its value from somewhere, then i receives this value from position P_i; so their sources are the same.

In this way, computing \text{pos}_i can be done in \mathcal{O}(N) for all i.

Now, let’s attempt to use this information.

Consider a directed graph on N vertices, containing the N edges i \to \text{pos}_i for each i.

Note that each vertex has exactly one outedge, so this is a [functional graph](https://usaco.guide/silver/func-graphs?lang=cpp).

In particular, we know what a functional graph looks like: several disjoint cycles, with trees hanging off of some vertices of the cycles (each tree is directed towards its corresponding cycle).

Analyzing this information, we can see the following:

- If a vertex is on a cycle, it will remain on that cycle forever. In particular, each step simply shuffles the values on a cycle within the vertices on it.

- In particular, values on a cycle never disappear. So, if there are at least two distinct non-zero values on cycles, the answer is immediately 0.

- If there is a non-zero element on a cycle, all zeros on cycles must be set to this value; so they are uniquely determined.

- If all the elements on cycles are zeros, then there are M choices for what to choose for them.

- If a vertex is not on a cycle, it will eventually receive a value from a cycle; so its initial value doesn’t matter at all.

- If there are x indices such that A_i = 0 that are not on a cycle, they thus contribute M^x to the answer.

Together, this gives us a simple formula for the answer:

- If there are two distinct non-zero elements on cycles, the answer is 0.

- Otherwise, let there be x indices not lying on cycles such that A_i = 0 for these indices.

- If any cycle contains a non-zero element, the answer is M^x.

- Otherwise, the answer is M^{x+1}.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

const int MOD=1e9+7;

#define ll long long int

int solve(int n, int m, vector<int>p, vector<int>a)
{
	bool fetch[n+1]{};
	int curr=0, c=0, x=0;
	for(int i=1; i<=n; i++) if(p[i]>=i) fetch[p[i]]=true, x++;

	bool zero=false;
	for(int i=1; i<=n; i++)
	{
	    if(fetch[i] && a[i]==0) zero=true;
		if(fetch[i] && a[i])
		{
			if(curr && (curr^a[i])) return 0;
			curr=a[i];
		}
		if(!fetch[i] && a[i]) c++;
	}

	int exp=n-x+1-c;
	if(curr) exp--;

	ll ans=1;
	while(exp--) ans=(ans*m)%MOD;

	if(curr>m && zero)
	{
        return 0;
	}
	return ans;
}

int main()
{

	int t; cin>>t;

	assert(t<=1e5);
	int total_n=0;

	while(t--)
	{
		int n, m; cin>>n>>m;
		total_n+=n;
		assert(n>=1 && n<=2e5);
		assert(m>=1 && m<=1e9);

		vector<int>p(n+1), a(n+1);

		for(int i=1; i<=n; i++) cin>>p[i];
		for(int i=1; i<=n; i++) cin>>a[i];

		bool visi[n+1]{};
		for(int i=1; i<=n; i++)
		{
		    visi[p[i]]=true;
		}

		for(int i=1; i<=n; i++)
		{
		    assert(a[i]>=0 && a[i]<=1e9);
		    assert(p[i]);
		}

		cout<<solve(n, m, p, a)<<endl;
	}
	assert(total_n<=2e5);

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

struct dsu {
    vector<int> p;
    vector<int> sz;
    int n;

    dsu(int _n) : n(_n) {
        p = vector<int>(n);
        iota(p.begin(), p.end(), 0);
        sz = vector<int>(n, 1);
    }

    inline int get(int x) {
        if (p[x] == x) {
            return x;
        } else {
            return p[x] = get(p[x]);
        }
    }

    inline bool unite(int x, int y) {
        x = get(x);
        y = get(y);
        if (x == y) {
            return false;
        }
        p[x] = y;
        sz[y] += sz[x];
        return true;
    }

    inline bool same(int x, int y) {
        return (get(x) == get(y));
    }

    inline int size(int x) {
        return sz[get(x)];
    }

    inline bool root(int x) {
        return (x == get(x));
    }
};

template <long long mod>
struct modular {
    long long value;
    modular(long long x = 0) {
        value = x % mod;
        if (value < 0) value += mod;
    }
    modular& operator+=(const modular& other) {
        if ((value += other.value) >= mod) value -= mod;
        return *this;
    }
    modular& operator-=(const modular& other) {
        if ((value -= other.value) < 0) value += mod;
        return *this;
    }
    modular& operator*=(const modular& other) {
        value = value * other.value % mod;
        return *this;
    }
    modular& operator/=(const modular& other) {
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
    friend modular operator+(const modular& lhs, const modular& rhs) { return modular(lhs) += rhs; }
    friend modular operator-(const modular& lhs, const modular& rhs) { return modular(lhs) -= rhs; }
    friend modular operator*(const modular& lhs, const modular& rhs) { return modular(lhs) *= rhs; }
    friend modular operator/(const modular& lhs, const modular& rhs) { return modular(lhs) /= rhs; }
    modular& operator++() { return *this += 1; }
    modular& operator--() { return *this -= 1; }
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
    bool operator==(const modular& rhs) const { return value == rhs.value; }
    bool operator!=(const modular& rhs) const { return value != rhs.value; }
    bool operator<(const modular& rhs) const { return value < rhs.value; }
};
template <long long mod>
string to_string(const modular<mod>& x) {
    return to_string(x.value);
}
template <long long mod>
ostream& operator<<(ostream& stream, const modular<mod>& x) {
    return stream << x.value;
}
template <long long mod>
istream& operator>>(istream& stream, modular<mod>& x) {
    stream >> x.value;
    x.value %= mod;
    if (x.value < 0) x.value += mod;
    return stream;
}

constexpr long long mod = (int) 1e9 + 7;
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        in.readSpace();
        int m = in.readInt(1, 1e9);
        in.readEoln();
        sn += n;
        vector<int> p = in.readInts(n, 1, n);
        in.readEoln();
        vector<int> a = in.readInts(n, 0, m);
        in.readEoln();
        for (int i = 0; i < n; i++) {
            p[i]--;
        }
        dsu uf(n);
        for (int i = 0; i < n; i++) {
            uf.unite(i, p[i]);
        }
        int free = (int) (count(a.begin(), a.end(), 0));
        int of = free;
        int z = -1;
        for (int i = 0; i < n; i++) {
            if (!uf.root(i)) {
                continue;
            }
            vector<int> t;
            t.emplace_back(i);
            while (true) {
                int x = p[t.back()];
                t.emplace_back(x);
                if (x == t[0]) {
                    break;
                }
            }
            for (int j = 0; j < (int) t.size() - 1; j++) {
                if (t[j] <= t[j + 1]) {
                    if (a[t[j + 1]] == 0) {
                        free--;
                    } else {
                        if (z == -1) {
                            z = a[t[j + 1]];
                        } else if (z != a[t[j + 1]]) {
                            free = -1;
                            break;
                        }
                    }
                }
            }
            if (free == -1) {
                break;
            }
        }
        if (free == -1) {
            cout << 0 << '\n';
        } else {
            if (z == -1 && free < of) {
                free++;
            }
            cout << power(m, free) << '\n';
        }
    }
    assert(sn <= 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
	n, m = map(int, input().split())
	p = [0] + list(map(int, input().split()))
	a = [0] + list(map(int, input().split()))

	indeg, outedge = [0]*(n+1), [0]*(n+1)
	ans = 1

	for i in range(1, n+1):
		if p[i] >= i: outedge[i] = p[i]
		else: outedge[i] = outedge[p[i]]
		indeg[outedge[i]] += 1

	queue = []
	for i in range(1, n+1):
		if indeg[i] == 0: queue.append(i)

	for u in queue:
		if a[u] == 0: ans = (ans * m) % mod
		indeg[outedge[u]] -= 1
		if indeg[outedge[u]] == 0: queue.append(outedge[u])

	cyclevals = set()
	for u in range(1, n+1):
		if indeg[u] == 0: continue
		cyclevals.add(a[u])

	if len(cyclevals) > 2: ans = 0
	elif len(cyclevals) == 2:
		if 0 not in cyclevals: ans = 0
	else:
		if 0 in cyclevals: ans = (ans * m) % mod
	print(ans)
``

</details>
