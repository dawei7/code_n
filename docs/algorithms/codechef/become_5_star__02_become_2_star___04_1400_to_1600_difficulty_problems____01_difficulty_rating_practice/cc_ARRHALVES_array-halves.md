# Array Halves

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRHALVES |
| Difficulty Rating | 1407 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [ARRHALVES](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/ARRHALVES) |

---

## Problem Statement

Chef has a permutation $P$ of length $2 \cdot N$. He can perform the following operation on $P$:
- Select an index $i$ $(1 \le i \lt 2 \cdot N)$ and swap $P_i$ and $P_{i + 1}$.

Chef would call the permutation $P$ *good*, if the **maximum** element of the first half of $P$ is **less** than the **minimum** element of the second half of $P$.
Formally $\displaystyle \max_{(1 \le i \le N)} P_i \lt \min_{(N \lt i \le 2 \cdot N)} P_i$.

Find the **minimum** number of operations Chef needs to apply to make $P$ *good*.

**Note:** A permutation of length $N$ is an array where every integer from $1$ to $N$ occurs exactly once.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — half the size of the permutation $P$.
- The second line of each test case contains $2 \cdot N$ space-separated integers $P_1, P_2, \dots, P_{2 \cdot N}$ denoting the permutation $P$.

---

## Output Format

For each test case, output the minimum number of operations required to make $P$ *good*.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $P$ is a permutation of length $2 \cdot N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
3 2 1 4
3
1 2 3 4 5 6
3
6 5 4 3 2 1
```

**Output**

```text
2
0
9
```

**Explanation**

**Test case $1$:** We can perform the following operations:
- Apply operation at $i = 1$: $[3, 2, 1, 4] \rightarrow [2, 3, 1, 4]$
- Apply operation at $i = 2$: $[2, 3, 1, 4] \rightarrow [2, 1, 3, 4]$

**Test case $2$:** $P$ is already good.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 2 1 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
1 2 3 4 5 6
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3
6 5 4 3 2 1
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARRHALVES)

[Contest: Division 1](https://www.codechef.com/JAN231A/problems/ARRHALVES)

[Contest: Division 2](https://www.codechef.com/JAN231B/problems/ARRHALVES)

[Contest: Division 3](https://www.codechef.com/JAN231C/problems/ARRHALVES)

[Contest: Division 4](https://www.codechef.com/JAN231D/problems/ARRHALVES)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have a permutation of length 2N. In one move, you can swap two adjacent elements.

Find the minimum number of swaps to obtain an array such that the maximum of the first N elements is less than the minimum of the last N elements.

#
[](#explanation-5)EXPLANATION:

Since the maximum of the first N elements must be less than the minimum of the last N elements, this means *every one* of the first N elements is less than *every one* of the last N elements.

This can only happen when the first N elements are \{1, 2, 3, \ldots, N\} (in some order) and the last N elements are \{N+1, N+2, \ldots, 2N\} (again, in some order).

In terms of swaps, this means that the only time we need to swap A_i and A_{i+1} is when A_i \gt N but A_{i+1} \leq N.

Looking at it differently, suppose we know that A_i \leq N and there are m positions \{j_1, j_2, \ldots, j_m\} before i such that A_{j} \gt N.

Then, the element at position i needs at least m swaps to be made, since it needs to be swapped with each of these once.

It’s not hard to see that exactly m swaps will suffice, since there’s no need to perform any more.

So, it’s enough to compute for each i such that A_i \leq N, the number of elements greater than it that are \gt N. The final answer is the sum of all these values.

This can be done by looping across the array and maintaining a counter.

That is,

- Initialize a variable \text{count} = 0.

- Then, for each i from 1 to 2N,

- If A_i \leq N, add \text{count} to the answer

- Otherwise, add 1 to \text{count}.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const long long INF = 1e18;

const int N = 1e6 + 5;

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << "L: " << l << ", R: " << r << ", Value Found: " << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int sumN = 0;

void solve()
{
    int n = readIntLn(1, 1e5);
    sumN += n;
    n *= 2;
    vector<int> a = readVectorInt(n, 1, n);
    assert(sz(set<int>(a.begin(), a.end())) == n);
    vector<int> b(n);
    for(int i = 0; i < n; i++)
        b[i] = (a[i] > n / 2);
    int cnt1 = 0, ans = 0;
    for(int i = 0; i < n; i++)
    {
        if(b[i])
            cnt1++;
        else
            ans += cnt1;
    }
    cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1e5);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    readEOF();
    assert(sumN <= 2e5);
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
        return res;
    }

    string readString(int minl, int maxl, const string& pattern = "") {
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
        if (buffer[pos] != '\n') {
            cerr << int(buffer[pos]) << endl;
        }
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
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 1e5);
        sn += n;
        in.readEoln();
        vector<int> p(2 * n);
        for (int i = 0; i < 2 * n; i++) {
            p[i] = in.readInt(1, 2 * n);
            (i == 2 * n - 1 ? in.readEoln() : in.readSpace());
            p[i]--;
        }
        {
            auto q = p;
            sort(q.begin(), q.end());
            for (int i = 0; i < 2 * n; i++) {
                assert(q[i] == i);
            }
        }
        for (int i = 0; i < 2 * n; i++) {
            p[i] = (p[i] >= n);
        }
        long long ans = 0;
        long long sum = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (p[i]) {
                sum++;
            } else {
                ans += sum;
            }
        }
        cout << ans << '\n';
    }
    assert(sn <= 2e5);
    in.readEof();
    cerr << sn << endl;
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    left, right = 0, 0
    ans = 0
    for i in range(2*n):
        if p[i] > n and i < n:
            ans += n-1-i-left
            left += 1
        if p[i] <= n and i >= n:
            ans += i-n-right
            right += 1
    print(ans + left*right)
``

</details>
