# Concat Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONCATSORT |
| Difficulty Rating | 1637 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CONCATSORT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CONCATSORT) |

---

## Problem Statement

JJ has an array $A$. He can perform the following operation on $A$:
- Divide $A$ into two subsequences $P$ and $Q$ such that each $A_i$ belongs to either $P$ or $Q$.
- Set $A := P\ \texttt{concat}\ Q$

Here $\texttt{concat}$ denotes the concatenation operation. For e.g. $[2, 1, 5] \texttt{ concat } [4, 3] = [2, 1, 5, 4, 3]$.

Is it possible to make $A$ sorted in non-decreasing order after applying the above operation **at most once**?

Note: An array $X$ is a subsequence of an array $Y$ if $X$ can be obtained by deletion of several (possibly, zero or all) elements from $Y$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output `YES` if it is possible to make the array $A$ sorted after applying the given operation **at most once**. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
6
4 5 6 1 2 3
5
1 3 5 2 4
5
5 10 7 11 9
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** We can select $P = [1, 2, 3]$ and $Q = [4, 5, 6]$. Therefore $A$ will become $[1, 2, 3, 4, 5, 6]$ which is sorted.

**Test case $2$:** It can be proven that it is not possible to sort $A$ by using the given operation at most once.

**Test case $3$:** We can select $P = [5, 7, 9]$ and $Q = [10, 11]$. Therefore $A$ will become $[5, 7, 9, 10, 11]$ which is sorted.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
4 5 6 1 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5
1 3 5 2 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5
5 10 7 11 9
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JULY222A/problems/CONCATSORT)

[Contest Division 2](https://www.codechef.com/JULY222B/problems/CONCATSORT)

[Contest Division 3](https://www.codechef.com/JULY222C/problems/CONCATSORT)

[Contest Division 4](https://www.codechef.com/JULY222D/problems/CONCATSORT)

Setter: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Testers: [Jatin Garg](https://www.codechef.com/users/rivalq), [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1637

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

JJ has an array A. He can perform the following operation on A:

- Divide A into two subsequences P and Q such that each A_i belongs to either P or Q.

- Set A := P\ \texttt{concat}\ Q

Here \texttt{concat} denotes the concatenation operation. For e.g. [2, 1, 5] \texttt{ concat } [4, 3] = [2, 1, 5, 4, 3].

Is it possible to make A sorted in non-decreasing order after applying the above operation **at most once**?

Note: An array X is a subsequence of an array Y if X can be obtained by deletion of several (possibly, zero or all) elements from Y.

#
[](#explanation-5)EXPLANATION:

Let array B represent an array with same elements as of A but sorted in non-decreasing order(Sorted version of array A).

**Observation 1:** Subsequence P is a prefix of array B. If it is possible to sort A in non-decreasing order using the above defined operations then array B=P **concat** Q. This means P is a prefix of array B and Q has to be a suffix of array B. This also means that P and Q are sorted in non-decreasing order.

**Claim**: It is always optimal to take the largest prefix of array B which is also a subsequence of A as P.

**Proof:** Let K be the length of the largest prefix of array B which is also a subsequence of A and  k be the length of subsequence P. Let the last element P has an index i in array A. Let’s say it is possible to obtain array B using this subsequence as P and remaining elements of array A as Q. Since k< K we must have an index j in array A such that A_j = B_{k+1}. B_{k+1} has to be the smallest (and equal to the first element) of subsequence Q and since Q is a sorted subsequence, array values at all indices of array A which are not included in P till (including) index j must be equal to B_{k+1}. We can remove index j(or one occurrence of A_j) from Q and append it to P, new P and new Q will still be sorted and it will still be possible to obtain array B from new P and new Q. Repeat the same procedure until k become equal to K.

Also it is not always possible to sort A by taking P with a length smaller than the optimal length(described above)

Example

Take A=[1,1,2,1]. B = [1,1,1,2]. Possible to sort it in non-decreasing order by taking P as [1,1,1] and Q as [2] but not possible to sort it in non-decreasing order by taking P as [1,1] and Q=[2,1] as Q is not sorted in non-decreasing order.

From these observations it is clear that we need to take P as the largest prefix of array B which is also a subsequence of A. Largest prefix of array B which is also a subsequence of A can easily be calculated by two pointers (or using Map data structure). Check whether the remaining elements (Q ) form a non-decreasing array. If they form a non-decreasing array output `YES` otherwise `NO`.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(Nlog(N)) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
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
                cerr << l << ' ' << r << ' ' << x << '\n';
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
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
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
    int n = readIntLn(2, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e9);
    vector<int> b = a, rem;
    sort(b.begin(), b.end());
    int cur = 0;
    for(int i = 0; i < n; i++)
    {
        if(a[i] == b[cur])
            cur++;
        else
            rem.push_back(a[i]);
    }
    if(is_sorted(rem.begin(), rem.end()))
        cout << "YES\n";
    else
        cout << "NO\n";
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
    assert(sumN <= 2e5);
    readEOF();
    return 0;
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
bool issorted(vll &v)
{
    for (int i = 1; i < v.size(); i++)
    {
        if (v[i] < v[i - 1])
            return false;
    }
    return true;
}
void sol(void)
{
    ll n, id = -1;
    cin >> n;
    vll v(n), p, q;
    map<ll, vll> mp;
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        mp[v[i]].pb(i);
    }
    if (issorted(v))
    {
        cout << "YES\n";
        return;
    }
    vector<bool> vis(n, false);
    bool flag = true;
    for (auto x : mp)
    {
        for (auto y : x.S)
            if (y < id)
            {
                flag = false;
            }
            else if (y > id)
            {
                vis[y] = true;
                id = y;
            }
        if (!flag)
            break;
    }
    for (int i = 0; i < n; i++)
        if (!vis[i])
            q.pb(v[i]);
    if (issorted(q))
        cout << "YES\n";
    else
        cout << "NO\n";
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    cin >> test;
    while (test--)
        sol();
}

``

</details>
