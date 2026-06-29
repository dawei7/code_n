# Subarray Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBARRAYREM |
| Difficulty Rating | 1505 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [SUBARRAYREM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/SUBARRAYREM) |

---

## Problem Statement

Chef has a **binary** array $A$ of length $N$. In one operation, Chef does the following:

**1.** Select any $L$ and $R$ such that $(1 \le L \lt R \le |A|)$ $\\$
**2.** Add $A_L \oplus A_{L+1} \oplus \ldots \oplus A_R$ to his *score* (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)) $\\$
**3.** Remove the subarray $A_{L \dots R}$ from $A$

Determine the **maximum** score Chef can get after performing the above operation any number of times.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the maximum score Chef can get.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $A_i \in \{0, 1\}$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5
1 0 0 0 1
3
1 1 1
3
0 0 0
```

**Output**

```text
2
1
0
```

**Explanation**

**Test Case 1:** We can perform the following moves:
- $A = [1, 0, 0, 0, 1]$. Select $L = 1$ and $R = 3$ and remove subarray $[1, 0, 0]$. $A$ becomes $[0, 1]$.
- $A = [0, 1]$. Select $L = 1$ and $R = 2$ and remove subarray $[0, 1]$. $A$ becomes $[]$.

Total score $= 1 + 1 = 2$

**Test Case 2:** We can perform the following move:
- $A = [1, 1, 1]$. Select $L = 1$ and $R = 3$ and remove subarray $[1, 1, 1]$. $A$ becomes $[]$.

Total score $= 1$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 0 0 0 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
1 1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
0 0 0
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

[Practice](https://www.codechef.com/problems/SUBARRAYREM)

[Contest: Division 1](https://www.codechef.com/START61A/problems/SUBARRAYREM)

[Contest: Division 2](https://www.codechef.com/START61B/problems/SUBARRAYREM)

[Contest: Division 3](https://www.codechef.com/START61C/problems/SUBARRAYREM)

[Contest: Division 4](https://www.codechef.com/START61D/problems/SUBARRAYREM)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have a boolean array A. In one move, you can choose any subarray of A with length at least 2, add its bitwise XOR to your score, and delete this subarray from A.

Find the maximum possible score you can achieve.

#
[](#explanation-5)EXPLANATION:

Since the array is boolean, each move increases our score by either zero or one.

Note that making a move that increases our score by zero is pointless, so we really want to count the maximum number of 1 moves that we can make.

Let’s call a subarray with xor 1 a *good* subarray.

Further, it’s better to use shorter subarrays if possible, since that gives us more freedom in the future. The shortest possible good subarrays we can choose are [0, 1] and [1, 0], so let’s keep choosing these as long as its possible to do so.

Suppose we can’t choose any more subarrays of this kind. Then, every element of A must be the same, i.e, A consists of all 0's or all 1's.

- In the first case, all 0's, nothing more can be done, since any remaining subarray has xor 0.

- In the second case, we still have good subarrays: anything with odd length is good, i.e, [1, 1, 1], [1, 1, 1, 1, 1], \ldots

- Suppose the length of A is now K. Then, the best we can do is \lfloor \frac{K}{3} \rfloor subarrays, each of the form [1, 1, 1]. So, add this value to the answer.

This gives us the final solution:

- While the array contains both 0's and 1's, remove one 0 and one 1 from it, and increase the answer by 1

- When the array contains only a single type of character, if it’s 1 and there are K of them, add \lfloor \frac{K}{3} \rfloor to the answer.

This can be done in \mathcal{O}(1) by knowing the counts of 0's and 1's, although simulation in \mathcal{O}(N) will still pass.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++, formula)
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
    vector<int> a = readVectorInt(n, 0, 1);
    int cnt0 = count(a.begin(), a.end(), 0);
    int cnt1 = count(a.begin(), a.end(), 1);
    int take = min(cnt0, cnt1);
    int ans = take;
    cnt0 -= take, cnt1 -= take;
    ans += cnt1 / 3;
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

Editorialist's code (Python, simulation)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur = []
    ans = 0
    for x in a:
        if len(cur) == 0 or x == cur[-1]: cur.append(x)
        else:
            ans += 1
            cur.pop()
    if len(cur) > 0 and cur[0] == 1:
        ans += len(cur)//3
    print(ans)
``

</details>
