# Subscriptions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSCRIBE_ |
| Difficulty Rating | 504 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SUBSCRIBE_](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUBSCRIBE_) |

---

## Problem Statement

A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of $N$ friends in Chefland want to buy Chef-TV subscriptions. We know that $6$ people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is $X$ rupees.
Determine the minimum total cost that the group of $N$ friends will incur so that everyone in the group is able to use Chef-TV.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N$ and $X$ — the size of the group of friends and the cost of one subscription.

---

## Output Format

For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \le X \le 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1 100
12 250
16 135
```

**Output**

```text
100
500
405
```

**Explanation**

- **Test case 1:** There is only one person in the group. Therefore he will have to buy $1$ subscription. Therefore the total cost incurred is $100$.
- **Test case 2:** There are $12$ people in the group. Therefore they will have to buy $2$ subscriptions. Therefore the total cost incurred is $500$.
- **Test case 3:** There are $16$ people in the group. Therefore they will have to buy $3$ subscriptions. Therefore the total cost incurred is $405$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 100
```

**Output for this case**

```text
100
```



#### Test case 2

**Input for this case**

```text
12 250
```

**Output for this case**

```text
500
```



#### Test case 3

**Input for this case**

```text
16 135
```

**Output for this case**

```text
405
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE221A/problems/SUBSCRIBE_)

[Contest Division 2](https://www.codechef.com/JUNE221B/problems/SUBSCRIBE_)

[Contest Division 3](https://www.codechef.com/JUNE221C/problems/SUBSCRIBE_)

[Contest Division 4](https://www.codechef.com/JUNE221D/problems/SUBSCRIBE_)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

504

#
[](#prerequisites-3)PREREQUISITES:

Basic Math

#
[](#problem-4)PROBLEM:

A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of N friends in Chefland want to buy Chef-TV subscriptions for each of them. We know that 6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is X rupees.

Determine the total cost that the group of N friends will incur so that everyone in the group is able to use Chef-TV.

#
[](#explanation-5)EXPLANATION:

The N friends will form  \lfloor \frac{N}{6} \rfloor  sharing groups having 6 people in each sharing group. If N is not divisible by 6 then the remaining N (mod 6) people will form an additional sharing group having less than 6 people. In order words the N friends require  \lceil \frac{N}{6} \rceil  number of Chef-TV subscriptions. The total cost that the group of N friends will incur is  X.\lceil \frac{N}{6} \rceil.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``    #include <wtsh.h>
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
    int x = readIntLn(1, 1000);
    cout << (n + 5) / 6 * x << endl;
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
    readEOF();
    return 0;
}

``

Editorialist's Solution
``using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--){
	    int n,x;
	    cin >> n >> x;
	    int m=n/6;
	    if(n%6!=0)m++;
	    cout << m*x << endl;
	}
	return 0;
}
``

</details>
