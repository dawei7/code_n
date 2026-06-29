# K Odd Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADVITIYA5 |
| Difficulty Rating | 1614 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [ADVITIYA5](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/ADVITIYA5) |

---

## Problem Statement

Given integers $N$ and $K$, construct a permutation $P = [P_1, P_2, \ldots, P_N]$ of the integers $\{1,2,\ldots, N\}$ such that there are **exactly** $K$ indices $i$ ($1 \le i \lt N$) for which $(P_i + P_{i + 1})$ is odd.

It can be proved that the answer always exists under the constraint of $1 \le K \le N - 1$.
If multiple answers exist, any of them will be accepted.

**Note:** A permutation of $\{1, 2, \ldots, N\}$ is a sequence in which every integer from $1$ to $N$ appears *exactly once*.
For example, if $N = 4$, $[4, 2, 1, 3]$ and $[1, 2, 3, 4]$ are valid permutations, but $[1, 4, 2, 1]$ ($1$ is repeated) and $[1, 3, 5, 2]$ ($5$ is larger than $N=4$) are not.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases.
- The first and only line of each testcase contains two space-separated integers $N$ and $K$, denoting the length of permutation and the required number of indices $i$ such that $(P_i+ P_{i+1})$ is odd, respectively.

---

## Output Format

For each testcase, output on a new line $N$ space-separated integers $P_1, P_2, \ldots, P_N$ denoting the permutation you found.
Each integer from $1$ to $N$ should appear exactly once, and there should be exactly $K$ indices $i$ such that $(P_i + P_{i+1})$ is odd.

If multiple possible answers exist, any of them will be accepted.

---

## Constraints

- $1 \le T \le 10^3$
- $2 \le N \le 10^5$
- $1 \le K \le N - 1$
- The sum of $N$ across all testcases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2 1
4 2
```

**Output**

```text
2 1
4 3 1 2
```

**Explanation**

**Test case $1$:** We have $P = [2, 1]$. $i = 1$ is the only index where $P_i + P_{i + 1}$ is odd.
$P = [1, 2]$ is also a valid solution, and will be accepted.

**Test case $2$:** We have $P = [4, 3, 1, 2]$.
- $i = 1$ gives us $(P_1 + P_2) = 4+3 = 7$, which is odd.
- $i = 2$ gives us $(P_2 + P_3) = 3+1 = 4$, which is even.
- $i = 3$ gives us $(P_3 + P_4) = 1+2 = 3$, which is odd.

Exactly $K = 2$ indices satisfy the given criterion, as required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
2 1
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
4 3 1 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ADVITIYA5)

[Contest: Division 1](https://www.codechef.com/START119A/problems/ADVITIYA5)

[Contest: Division 2](https://www.codechef.com/START119B/problems/ADVITIYA5)

[Contest: Division 3](https://www.codechef.com/START119C/problems/ADVITIYA5)

[Contest: Division 4](https://www.codechef.com/START119D/problems/ADVITIYA5)

***Author:*** [mehul_g2874](https://www.codechef.com/users/mehul_g2874)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given N and K, construct a permutation of \{1, 2, \ldots, N\} such that exactly K adjacent pairs of elements have an odd sum.

# [](#explanation-5)EXPLANATION:

For P_i + P_{i+1} to be odd, the only thing that really matters is the *parity* of P_i and P_{i+1}, not their actual values.

In particular, this sum is odd if and only if one of the two numbers is even and the other is odd.

So, our task is really to construct a *binary string* S of length N such that:

- S contains exactly \left\lfloor\frac{N}{2} \right\rfloor zeros (the positions of the even elements in [1, N].

- Every other position contains 1 (the positions of the odd elements).

- There are exactly K adjacent pairs of characters that are not equal (and hence will have odd sum).

If we can find such a binary string, all that needs to be done is to place the even elements at 0's and odd elements at 1's, in some order.

There are likely several constructions now, here’s one.

Consider the binary string 1010\ldots 10 that consists of 10 repeated several times.

If it’s repeated y times, it’ll have 2y-1 adjacent pairs of unequal elements.

So, we can do the following:

- Find the largest y such that 2y-1 \leq K, and create y repeated occurrences of 10.

Now, we either have 2y-1 = K or 2y-1 = K-1 (since each extra copy of 10 adds two to the count).

- If 2y-1 = K, we don’t want to have any more adjacent equal elements.

So, place any remaining ones just before the last character, and any remaining zeros at the end of the string.

Essentially, we go from 1010\ldots 10 to 1010\ldots 10111\ldots 11000\ldots 00, i.e, the last 1 and 0 both get ‘extended’.

- If 2y-1 = K-1, we want one more index.

For this, simply place a 1 at the end of the string, then once again distribute the remaining zeros and ones as above.

We go from 1010\ldots 10 to 1010\ldots 101000\ldots 00111\ldots 11.

Now, just replace zeros with distinct even numbers and ones with distinct odd numbers to obtain the answer.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

void Solve()
{
    int n, k; cin >> n >> k;

    vector <int> odd, even;
    for (int i = 1; i <= n; i++){
        if (i & 1) odd.push_back(i);
        else even.push_back(i);
    }

    cout << odd.back() << " ";
    odd.pop_back();

    int done = 0;
    int mv = 1;
    while (done < k - 1){
        done++;
        mv ^= 1;
        if (mv == 1){
            cout << odd.back() << " ";
            odd.pop_back();
        } else {
            cout << even.back() << " ";
            even.pop_back();
        }
    }

    if (!mv) swap(odd, even);
    for (auto x : odd) cout << x << " ";
    for (auto x : even) cout << x << " ";
    cout << "\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Tester's code (C++)
``#ifndef LOCAL
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt,fma")
#endif

#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "../debug.h"
#else
#define dbg(...) "11-111"
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
        while (now < (int) buffer.size() && !isspace(buffer[now])) {
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

    auto readInts(int n, int minv, int maxv) {
        assert(n >= 0);
        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readInt(minv, maxv);
            if (i+1 < n) readSpace();
        }
        return v;
    }

    auto readLongs(int n, long long minv, long long maxv) {
        assert(n >= 0);
        vector<long long> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = readLong(minv, maxv);
            if (i+1 < n) readSpace();
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

int32_t main() {
    ios_base::sync_with_stdio(0);   cin.tie(0);

    input_checker input;

    int T = input.readInt(1, 1000);   input.readEoln();
    int NN = 0;
    while(T-- > 0) {
        int N = input.readInt(1, (int)1e5);     input.readSpace();
        int K = input.readInt(1, (int)N - 1);   input.readEoln();
        for(int i = 1 ; i <= K ; ++i)   cout << i << " ";
        for(int i = K + 2 ; i <= N ; i += 2)    cout << i << " ";
        for(int i = K + 1 ; i <= N ; i += 2)    cout << i << " ";
        cout << '\n';
    }

    input.readEof();

    return 0;
}

``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [1, 0] * (k//2)
    have = 2*(k//2) - 1
    if have == k-1:
        a += [0]*(n//2 - k//2)
        a += [1]*((n+1)//2 - k//2)
    else:
        a += [1]*((n+1)//2 - k//2)
        a += [0]*(n//2 - k//2)
    odd, even = 1, 2
    for i in range(n):
        if a[i] == 1:
            a[i] = odd
            odd += 2
        else:
            a[i] = even
            even += 2
    print(*a)
``

</details>
