# Chef gives Party

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PARTY2 |
| Difficulty Rating | 363 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PARTY2](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARTY2) |

---

## Problem Statement

Chef wants to give a burger party to all his $N$ friends i.e. he wants to buy **one** burger for each of his friends.

The cost of each burger is $X$ rupees while Chef has a total of $K$ rupees.

Determine whether he has enough money to buy a burger for each of his friends or not.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains the three integers $N$, $X$, and $K$ - the number of Chef's friends, the cost of each burger, and the total money Chef has, respectively.

---

## Output Format

For each test case, output `YES` if the Chef can give a party to all his $N$ friends. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \le T \le 1000$
- $1 \le N, X \le 100$
- $1 \le K \le 10000$

---

## Examples

**Example 1**

**Input**

```text
4
5 10 70
5 10 40
10 40 400
14 14 150
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

- **Test case $1$:** Chef has $5$ friends. The cost of buying a burger for each of them will be $10 \times 5 = 50$ while Chef has $70$ rupees. Therefore, he can buy a burger for all of them.

- **Test case $2$:** Chef has $5$ friends. The cost of buying a burger for each of them will be $10 \times 5 = 50$ while Chef has $40$ rupees. Therefore, he can **not** buy a burger for all of them.

- **Test case $3$:** Chef has $10$ friends. The cost of buying a burger for each of them will be $40 \times 10 = 400$ and Chef has $400$ rupees. Therefore, he can buy a burger for all of them.

- **Test case $4$:** Chef has $14$ friends. The cost of buying a burger for each of them will be $14 \times 14 = 196$ while Chef has $150$ rupees. Therefore, he can **not** buy a burger for all of them.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 10 70
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 10 40
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
10 40 400
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
14 14 150
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

[Contest Division 1](https://www.codechef.com/START38A/problems/PARTY2)

[Contest Division 2](https://www.codechef.com/START38B/problems/PARTY2)

[Contest Division 3](https://www.codechef.com/START38C/problems/PARTY2)

[Contest Division 4](https://www.codechef.com/START38D/problems/PARTY2)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

363

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of them. The cost of each burger is X rupees while Chef has a total of K rupees.

Determine if he has enough money to buy a burger for each of his friends or not?

#
[](#explanation-5)EXPLANATION:

Total numbers of burgers to be bought is N and each burger costs Rs. X. The total cost to buy N burgers is N\cdot X. Therefore if N\cdot X\leq K the answer is `Yes` otherwise `No`

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

void solve()
{
    int n = readIntSp(1, 100);
    int x = readIntSp(1, 100);
    int k = readIntLn(1, 10000);
    if(n * x <= k)
        cout << "YES\n";
    else
        cout << "NO\n";
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
    int n,x,k;
    cin>>n>>x>>k;
    if(n*x>k)
    cout<<"NO\n";
    else
    cout<<"YES\n";
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
