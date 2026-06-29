# Dominant Army

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DOMINANT |
| Difficulty Rating | 488 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DOMINANT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOMINANT) |

---

## Problem Statement

In the medieval age, there were $3$ kingdoms $A$, $B$, and $C$. The army of these kingdom had $N_A$, $N_B$, and $N_C$ soldiers respectively.

You are given that an army with $X$ soldiers can defeat an army with $Y$ soldiers only if $X \gt Y$.

An army is said to be **dominant** if it can defeat both the other armies **combined**. For example, kingdom $C$'s army will be dominant only if $N_C > N_A + N_B$.

Determine whether any of the armies is **dominant** or not.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $N_A$, $N_B$, and $N_C$ - the number of warriors in the armies of kingdoms $A$, $B$, and $C$ respectively.

---

## Output Format

For each test case, output `YES` if any of the armies is dominant. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N_A, N_B, N_C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
15 5 6
12 13 16
1 1 100
10 10 20
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** The kingdom $A$'s army is dominant since $15 > 5 + 6$.

**Test case $2$:** We can observe that none of the armies is dominant.

**Test case $3$:** The kingdom $C$'s army is dominant since $100 > 1 + 1$.

**Test case $4$:** We can observe that none of the armies is dominant. Note that the kingdom $C$'s army is not dominant since $20 \le 10 + 10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15 5 6
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
12 13 16
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
1 1 100
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
10 10 20
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START38A/problems/DOMINANT)

[Contest Division 2](https://www.codechef.com/START38B/problems/DOMINANT)

[Contest Division 3](https://www.codechef.com/START38C/problems/DOMINANT)

[Contest Division 4](https://www.codechef.com/START38D/problems/DOMINANT)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

488

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In the medieval age, there were 3 kingdoms A, B and C whose army had N_A, N_B and N_C soldiers respectively. An army with X soldiers can defeat an army with Y soldiers if X \gt Y.

An army is said to be **dominant** if it can defeat both the other armies combined. For example, kingdom C's army will be dominant if N_C \gt N_A + N_B.

Determine if any of the armies is **dominant** or not.

#
[](#explanation-5)EXPLANATION:

Kingdom A's army will be dominant if N_A \gt N_B + N_C, Kingdom B's army will be dominant if N_B \gt N_A + N_C  and Kingdom C's army will be dominant if N_C \gt N_A + N_B. If any of the above mentioned condition is true the answer is `Yes` else `No`.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

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

int y = 0, n = 0;

void solve()
{
    array<int, 3> a;
    a[0] = readIntSp(1, 100);
    a[1] = readIntSp(1, 100);
    a[2] = readIntLn(1, 100);
    sort(a.begin(), a.end());
    if(a[2] > a[0] + a[1])
        cout << "YES\n", y++;
    else
        cout << "NO\n", n++;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1000);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    cerr << "YES: " << y << " | NO: " << n << endl;
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int na, nb, nc;
    cin >> na >> nb >> nc;
    if (na > nb + nc || nb > na + nc || nc > na + nb)
        cout << "YES\n";
    else
        cout << "NO\n";
    return;
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
