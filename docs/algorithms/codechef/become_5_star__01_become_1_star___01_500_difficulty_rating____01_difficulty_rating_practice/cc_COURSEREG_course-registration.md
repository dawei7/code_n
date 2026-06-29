# Course Registration

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COURSEREG |
| Difficulty Rating | 470 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [COURSEREG](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COURSEREG) |

---

## Problem Statement

There is a group of $N$ friends who wish to enroll in a course together. The course has a maximum capacity of $M$ students that can register for it. If there are $K$ other students who have already enrolled in the course, determine if it will still be possible for all the $N$ friends to do so or not.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- Each test case consists of a single line containing three integers $N$, $M$ and $K$ - the size of the friend group, the capacity of the course and the number of students already registered for the course.

---

## Output Format

For each test case, output `Yes` if it will be possible for all the $N$ friends to register for the course. Otherwise output `No`.

You may print each character of `Yes` and `No` in uppercase or lowercase (for example, `yes`, `yEs`, `YES` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq M \leq 100$
- $0 \leq K \leq M$

---

## Examples

**Example 1**

**Input**

```text
3
2 50 27
5 40 38
100 100 0
```

**Output**

```text
Yes
No
Yes
```

**Explanation**

**Test Case 1:** The $2$ friends can enroll in the course as it has enough seats to accommodate them and the $27$ other students at the same time.

**Test Case 2:** The course does not have enough seats to accommodate the $5$ friends and the $38$ other students at the same time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 50 27
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
5 40 38
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
100 100 0
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START32A/problems/COURSEREG)

[Contest Division 2](https://www.codechef.com/START32B/problems/COURSEREG)

[Contest Division 3](https://www.codechef.com/START32C/problems/COURSEREG)

[Contest Division 4](https://www.codechef.com/START32D/problems/COURSEREG)

**Setter:** [ Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

**Tester:** [Ashley Khoo](https://www.codechef.com/users/errorgorn), [ Nishant Shah](https://www.codechef.com/users/nishant_adm)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a group of N friends who wish to enroll in a course together. The course has a maximum capacity of M students that can register for it. If there are K other students who have already enrolled in the course, determine if it will still be possible for all the N friends to do so or not.

#
[](#explanation-5)EXPLANATION:

We are given that the course has a maximum capacity of M students. K students have already enrolled in the course; therefore , atmost M-K students can enroll in the course now. Since N friends wish to enroll in the course together, following 2 cases are possible :

-
N \leq M-K; it will be possible for all the N friends to enroll in the course together, therefore the output will be **YES**.

-
N \gt M-K; it will not be possible for all the N friends to enroll in the course together, therefore the output will be **NO**.

Examples

-

N = 5, M = 10,  K = 5; Since 5 \leq 10 - 5, it is possible for all the 5 friends to enroll in the course together, therefore the output will be **YES**.

-

N = 10, M = 15, k = 10; Since 10 \gt 15-10, it is not possible for all the 10 friends to enroll in the course together, therefore the output will be **NO**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;

/*
---------Input Checker(ref : https://pastebin.com/Vk8tczPu )-----------
*/

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true)
    {
        char g = getchar();
        if (g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if (cnt == 0)
            {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd)
        {
            if (is_neg)
            {
                x = -x;
            }

            if (!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
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
    while (true)
    {
        char g = getchar();
        assert(g != -1);
        if (g == endd)
        {
            break;
        }
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r)
{
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r)
{
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r)
{
    return readString(l, r, '\n');
}
string readStringSp(int l, int r)
{
    return readString(l, r, ' ');
}

/*
-------------Main code starts here------------------------
*/

// Note here all the constants from constraints
const int MAX_T = 1000;
const int MAX_N = 100;

void solve()
{
    int n, m, k;
    n = readIntSp(1, MAX_N);
    m = readIntSp(n, MAX_N);
    k = readIntLn(0, m);

    if (n + k <= m)
    {
        cout << " \n YEs   \n\n";
    }
    else
    {
        cout << "   \n   \n  nO  \n\n   \n";
    }
}

signed main()
{
    int t;
    t = readIntLn(1, MAX_T);

    for (int i = 1; i <= t; i++)
    {
        solve();
    }

    // Make sure there are no extra characters at the end of input
    assert(getchar() == -1);
    cerr << "SUCCESS\n";

    // Some important parameters which can help identify weakness in testdata
    cerr << "Tests : " << t << '\n';
}
``

Editorialist's Solution
``/*prakhar_87*/
#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int n, m, k;
    cin >> n >> m >> k;
    if (n <= m - k) cout << "YES\n";
    else cout << "NO\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
