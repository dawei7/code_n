# Chandelier

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHANDWEIGHT |
| Difficulty Rating | 2368 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHANDWEIGHT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHANDWEIGHT) |

---

## Problem Statement

A linear chandelier is held up by $N$ supports. The $i^{th}$ support initially holds up a weight $W_i$, and will collapse if the weight on it is **more than or equal to** $A_i$. Note that initially, $W_i \lt A_i$ for all $1 \le i \le N$.

Whenever $W_i\ge A_i$ for some support, the following happens:

- The $i^{th}$ support is destroyed;
- Let $x$ and $y$ be uniformly random non-negative integers such that $x+y=W_i$.
Add $x$ to $W_{i-1}$ and add $y$ to $W_{i+1}$.

Note that:
- If either one of the neighbours do not exist, all the weight is added to the remaining neighbour.
- If both neighbours do not exist, the weight dissipates.

For all $1 \le i \le N$, find the **minimum** weight you need to add to $W_i$, so that there is a nonzero chance all supports end up destroyed.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- The first line of each test case contains $N$, the number of supports.
- The second line of each test case contains $N$ integers $W_1, W_2, \ldots, W_N$, denoting initial weight on  each support.
- The third line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$, denoting the minimum load at which a support destroys.

---

## Output Format

For each test, output $N$ space-separated integers. The $i^{th}$ of these should be the **minimum weight** you need to add to the $i^{th}$ chandelier, so that there is a nonzero chance that all supports end up destroyed.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 3\cdot 10^5$
- $1 \leq W_i \lt A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
1 1 1
2 2 2
1
1
1000000000
2
1 1234
2 5678
7
122 179 269 184 250 104 455
398 203 318 340 312 489 464
```

**Output**

```text
1 1 1
999999999
4443 4444
276 146 49 156 291 385 9
```

**Explanation**

**Test case $1$:** The following is possible if we add weight $1$ to support $2$:
- Support $2$ collapses, since $W_2=2\ge 2$. A weight $x=1$ gets added to $W_1$, and a weight $y=1$ gets added to $W_3$.
- Support $1$ collapses, since $W_1=2\ge 2$.
- Support $3$ collapses, since $W_3=2\ge 2$.

If we add zero weight, then nothing would happen and all supports would stay standing. So the answer for $i=2$ is $1$.

**Test case $2$:** We have to add $999999999$ weight to the only support to make it collapse.

**Test case $3$:** Note that we could add a weight of $1$ to support $1$ to make it collapse, but then, there would be no way to make the second support collapse. We can show that we have to add at least $4443$ weight to support $1$ to make it possible for both supports to end up destroyed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 1 1
2 2 2
```

**Output for this case**

```text
1 1 1
```



#### Test case 2

**Input for this case**

```text
1
1
1000000000
```

**Output for this case**

```text
999999999
```



#### Test case 3

**Input for this case**

```text
2
1 1234
2 5678
```

**Output for this case**

```text
4443 4444
```



#### Test case 4

**Input for this case**

```text
7
122 179 269 184 250 104 455
398 203 318 340 312 489 464
```

**Output for this case**

```text
276 146 49 156 291 385 9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHANDWEIGHT)

[Contest: Division 1](https://www.codechef.com/START103A/problems/CHANDWEIGHT)

[Contest: Division 2](https://www.codechef.com/START103B/problems/CHANDWEIGHT)

[Contest: Division 3](https://www.codechef.com/START103C/problems/CHANDWEIGHT)

[Contest: Division 4](https://www.codechef.com/START103D/problems/CHANDWEIGHT)

***Author:*** [bucketpotato](https://www.codechef.com/users/bucketpotato)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

A chandelier is held by N supports. The i-th of them initially supports weight W_i, and has limit A_i.

When W_i\geq A_i, the support is destroyed, and triggers further destruction by distributing its weight randomly to both sides.

For each 1 \leq i \leq N, find the minimum weight needed to be added to support i, so that *all* supports are destroyed.

# [](#explanation-5)EXPLANATION:

First, let’s rephrase the process a bit.

We want to find whether there’s a non-zero chance that all the supports are destroyed; where x and y are chosen uniformly randomly when a support fails.

The randomess can in fact be discarded entirely — we’re free to choose x and y as we wish; since we only want to know if a *single* way exists.

That is, we’re free to choose exactly how much of the weight falls to either side.

Suppose support i is destroyed.

It will distribute its weight to (i-1) and (i+1).

However, following that, the two sections are completely disjoint since one of their adjacent supports is already destroyed.

That is, (i-1) will give all its weight to (i-2), which will give all its weight to (i-3), and so on till 1 is reached; similarly on the other side all the weight is transferred along (i+1)\to (i+2)\to \ldots \to N.

In other words, destroying one support will independently trigger the destruction of a *prefix* and a *suffix* of supports; and we just need to make sure there’s enough weight to make them all fall.

Let \text{pref}[i] denote the minimum weight that needs to be added to support i, so that all the supports 1, 2, 3, \ldots, i are destroyed leftwards (that is, we pretend i+1 doesn’t exist).

Finding \text{pref}[i] is not too hard:

- Certainly, we must have \text{pref}[i] \geq A_i - W_i, since we need at least that much to destroy support i at all.

- Also, after i is destroyed, the prefix till i-1 must be destroyed next.

By definition, this needs an extra weight of at least \text{pref}[i-1]; meaning we need to add at least \text{pref}[i-1] - W_i to support i.

- So, we have \text{pref}[i] = \max(A_i, \text{pref}[i-1]) - W_i

Similarly, the weights required to destroy each suffix can be calculated, say as \text{suf}[i].

Now, for each i:

- We need to reach at least A_i to destroy it.

- After destruction, we need at least \text{pref}[i-1] to destroy the remaining prefix, and \text{suf}[i+1] to destroy the remaining suffix.

- In either case, we already have W_i.

So, the answer for i is just \max(A_i, \text{pref}[i-1] + \text{suf}[i+1]) - W_i

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include "bits/stdc++.h"

using namespace std;

#define ll long long

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t; cin >> t;
  while (t--) {

    int n; cin >> n;

    vector<ll> w(n + 1);
    vector<ll> a(n + 1);

    for (int i = 1; i <= n; i++) {
      cin >> w[i];
    }
    for (int i = 1; i <= n; i++) {
      cin >> a[i];
    }

    vector<ll> pf(n + 2), sf(n + 2);
    for (int i = 1; i <= n; i++) {

      // we need to add at least (a[i] - w[i]).
      // will a[i] on this support be enough to
      // destroy all the previous ones?
      ll rm = max(0ll, pf[i - 1] - a[i]);
      pf[i] = a[i] - w[i] + rm;

    }

    for (int i = n; i > 0; i--) {
      ll rm = max(0ll, sf[i + 1] - a[i]);
      sf[i] = a[i] - w[i] + rm;
    }

    for (int i = 1; i <= n; i++) {

      ll ans = max(a[i] - w[i], pf[i - 1] + sf[i + 1] - w[i]);
      cout << ans << " \n"[i == n];

    }

  }

}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

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

input_checker inp;
int sum_n = 0;
const int N = 3e5;

void Solve()
{
    int n = inp.readInt(1, N);
    sum_n += n;
    inp.readEoln();

    vector <int> w = inp.readInts(n, 1, (int)1e9);
    inp.readEoln();
    vector <int> a = inp.readInts(n, 1, (int)1e9);
    inp.readEoln();

    //p[i] = how much to add to break i'th prefix
    //p[i + 1] = a[i + 1] - w[i + 1] + max(0, p[i] - a[i]);

    vector <int> p(n + 1, 0), s(n + 1, 0);
    for (int i = 1; i <= n; i++){
        p[i] = a[i - 1] - w[i - 1] + max(0LL, p[i - 1] - a[i - 1]);
    }

    for (int i = n - 1; i >= 0; i--){
        s[i] = a[i] - w[i] + max(0LL, s[i + 1] - a[i]);
    }

    for (int i = 0; i < n; i++){
        int ans = p[i] + s[i + 1] - w[i];
        ans = max(ans, a[i] - w[i]);
        cout << ans << " \n"[i + 1 == n];
    }
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;

    t = inp.readInt(1, 10000);
    inp.readEoln();
    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }

    assert(sum_n <= N);
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pref, suf = [0]*n, [0]*n
    for i in range(n):
        pref[i] = a[i] - w[i]
        if i > 0:
            if a[i] < pref[i-1]: pref[i] += pref[i-1] - a[i]
    for i in reversed(range(n)):
        suf[i] = a[i] - w[i]
        if i+1 < n:
            if a[i] < suf[i+1]: suf[i] += suf[i+1] - a[i]
    ans = [0]*n
    for i in range(n):
        L, R = 0, 0
        if i > 0: L = pref[i-1]
        if i+1 < n: R = suf[i+1]
        ans[i] = max(L+R - w[i], a[i] - w[i])
    print(*ans)
``

</details>
