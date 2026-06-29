# Weird Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WEIRDSUBARR |
| Difficulty Rating | 1739 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [WEIRDSUBARR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/WEIRDSUBARR) |

---

## Problem Statement

An array $A$ is called *weird* if it can be sorted in non-decreasing order by applying the given operation any number of times:
- Select any index $i$ $(1 \le i \le |A|)$ and set $A_i := -A_i$.

For example: $A = [2, 1, 3]$ is *weird* since after applying the operation at $i = 1$, $A$ becomes $[-2, 1, 3]$ which is sorted.

JJ has a permutation $P$ of length $N$. He wants to find the number of subarrays of $P$ which are *weird*. Can you help him?

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the permutation $P$.
- The second line of each test case contains $N$ space-separated integers $P_1, P_2, \dots, P_N$ denoting the permutation $P$.

---

## Output Format

For each test case, output on a new line the number of *weird* subarrays of $P$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $P$ is a permutation.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
2 3 1
3
2 1 3
4
1 2 3 4
```

**Output**

```text
5
6
10
```

**Explanation**

**Test Case 1:** Weird subarrays of $P$ are: $[2], [3], [1], [2, 3], [3, 1]$.

**Test Case 2:** Weird subarrays of $P$ are: $[2], [1], [3], [2, 1], [1, 3], [2, 1, 3]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 3 1
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
3
2 1 3
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WEIRDSUBARR)

[Contest: Division 1](https://www.codechef.com/START61A/problems/WEIRDSUBARR)

[Contest: Division 2](https://www.codechef.com/START61B/problems/WEIRDSUBARR)

[Contest: Division 3](https://www.codechef.com/START61C/problems/WEIRDSUBARR)

[Contest: Division 4](https://www.codechef.com/START61D/problems/WEIRDSUBARR)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

(Optional) Dynamic programming

#
[](#problem-4)PROBLEM:

You have a permutation P of \{1, 2, \ldots, N\}. In one move, you can negate any of its elements.

A subarray is called *weird* if it can be sorted in ascending order by applying this move several times. Count the number of weird subarrays in P.

#
[](#explanation-5)EXPLANATION:

In tasks like this which require you to count objects satisfying a certain property, it’s useful to get a simpler criterion of that property.

Let’s look at a weird array A = [A_1, A_2, \ldots, A_k]. What does this tell us about the elements of A?

One obvious fact is that in the final array, all the negative elements *must* come before all the positive elements — otherwise, there’s no way for the final array to be sorted.

So, there is some index p such that A_1, A_2, \ldots, A_p are negated, and A_{p+1}, \ldots, A_k are not. Looking at each of those parts individually,

- We want -A_1 \lt -A_2 \lt \ldots \lt -A_p, i.e, A_1 \gt A_2 \gt \ldots \gt A_p

- We also want A_{p+1} \lt A_{p+2} \lt \ldots \lt A_k

In other words, A must look like a ‘valley’: first decreasing, then increasing (purely increasing/decreasing is also ok). It’s also obvious that any such array is *weird*, since it can be sorted by negating the first part.

So, we just need to count the number of valleys in P.  There are several ways to do this, a couple will be mentioned below:

- Let’s call an index i a *hill* if P_{i-1} \lt P_i \gt P_{i+1}. Note that a subarray is a valley if and only if it doesn’t contain a hill index along with both of its neighbors.

- Suppose we find all hill indices. Then, we can simply count the number of weird indices between each adjacent pair of them to obtain our answer.

- Counting the number of subarrays between two hills is simple combinatorics.

- You may refer to the setter’s code (below) for this approach.

- Another method is to directly count valleys.

- Suppose we fix the deepest point of the valley to be index i. Let’s count the number of valleys like this.

- The left of i should be some decreasing sequence, and the right should be increasing.

- Let left_i denote the longest decreasing sequence ending at i, and right_i denote the longest increasing sequence starting at i. These two can be found with dynamic programming in \mathcal{O}(N).

- Then, we add left_i \times right_i to the answer, to account for all choices of subarrays with i as the deepest point (also including purely increasing/decreasing subarrays)

- Adding up left_i \times right_i across all 1 \leq i \leq N gives us the answer

- You may refer to the editorialist’s code (below) for this approach.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

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
    vector<int> p = readVectorInt(n, 1, n);
    assert(set<int>(p.begin(), p.end()).size() == n);
    vector<int> hills{0};
    for(int i = 1; i + 1 < n; i++)
        if(p[i] > p[i - 1] and p[i] > p[i + 1])
            hills.push_back(i);
    hills.push_back(n - 1);
    int ans = 0;
    for(int i = 0; i + 1 < sz(hills); i++)
    {
        int len = hills[i + 1] - hills[i] + 1;
        ans += len * (len - 1) / 2;
    }
    ans += n;
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
    assert(sumN <= 2e5);
    readEOF();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    left, right = [1]*n, [1]*n
    for i in range(1, n):
        if p[i] < p[i-1]: left[i] += left[i-1]
        if p[n-1-i] < p[n-i]: right[n-1-i] += right[n-i]
    print(sum(left[i] * right[i] for i in range(n)))
``

</details>
