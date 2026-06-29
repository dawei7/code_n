# Chairs Requirement

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHAIRS_ |
| Difficulty Rating | 305 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CHAIRS_](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHAIRS_) |

---

## Problem Statement

Chef's coding class is very famous in Chefland.

This year $X$ students joined his class and each student will require one chair to sit on. Chef already has $Y$ chairs in his class. Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ — the number of students in the class and the number of chairs Chef already has.

---

## Output Format

For each test case, output the minimum number of extra chairs Chef must buy so that every student gets one chair.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
20 14
41 41
35 0
50 100
```

**Output**

```text
6
0
35
0
```

**Explanation**

- **Test case 1:** There are $20$ students in the class and Chef has $14$ chairs already. Therefore Chef must buy $6$ more chairs.
- **Test case 2:** There are $41$ students in the class and Chef already has exactly $41$ chairs. Therefore Chef does not need to buy any more chairs.
- **Test case 3:** There are $35$ students in the class and Chef has no chairs initially. Therefore Chef must buy $35$ chairs.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20 14
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
41 41
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
35 0
```

**Output for this case**

```text
35
```



#### Test case 4

**Input for this case**

```text
50 100
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE221A/problems/CHAIRS_)

[Contest Division 2](https://www.codechef.com/JUNE221B/problems/CHAIRS_)

[Contest Division 3](https://www.codechef.com/JUNE221C/problems/CHAIRS_)

[Contest Division 4](https://www.codechef.com/JUNE221D/problems/CHAIRS_)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

305

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s coding class is very famous in Chefland.

This year X students joined his class and each student will require one chair to sit on. Chef already has Y chairs in his class. Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.

#
[](#explanation-5)EXPLANATION:

There are 2 possibilities:

-
X \leq Y, this means that Chef has sufficient chairs to accommodate all the X students, so the answer is 0.

-
X > Y, this means that Chef has insufficient chairs and needs at least X - Y additional chairs, so the answer is X - Y.

We can combine both these possibilities using Max function. The required answer is Max(X - Y, 0).

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
    int x = readIntSp(0, 100);
    int y = readIntLn(0, 100);
    cout << max(0LL, x - y) << endl;
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

int main(){
    int T;
    cin >> T;
    while(T--){
    	int x,y;
    	cin >> x >> y;
    	cout << max(x-y,0) << endl;
    }
	return 0;
}
``

</details>
