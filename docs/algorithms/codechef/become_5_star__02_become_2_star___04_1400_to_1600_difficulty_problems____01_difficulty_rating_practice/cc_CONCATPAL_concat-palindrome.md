# Concat Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONCATPAL |
| Difficulty Rating | 1520 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CONCATPAL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CONCATPAL) |

---

## Problem Statement

Chef has two strings $A$ and $B$ of lengths $N$ and $M$ respectively.

Chef can rearrange both strings in any way he wants. Let the rearranged string of $A$ be $A'$ and the rearranged string of $B$ be $B'$.

Determine whether we can construct rearrangements $A'$ and $B'$ such that $(A' + B')$ is a palindrome.

Here $+$ denotes the concatenation operation. For e.g. ${abc} + {xyz} = {abcxyz}$.

Note: A string is called palindrome if it reads the same backwards and forwards, for e.g. $\texttt{noon}$ and $\texttt{level}$ are palindromic strings.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ — the length of the strings $A$ and $B$ respectively.
- The second line of each test case contains a string $A$ of length $N$ containing lowercase Latin letters only.
- The third line of each test case contains a string $B$ of length $M$ containing lowercase Latin letters only.

---

## Output Format

For each test case, output `YES` if we can rearrange $A$ and $B$ such that $(A' + B')$ becomes a palindrome. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, M \leq 2 \cdot 10^5$
- $A$ and $B$ consist of lowercase Latin letters only.
- The sum of $N + M$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5 2
abcdd
ac
3 3
abc
xyz
2 4
aa
aaaa
1 3
a
aax
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** We can rearrange $A$ to $A' = acdbd$ and $B$ to $B' = ca$. So $A' + B' = acdbdca$ which is palindromic.

**Test case $2$:** We can not rearrange $A$ and $B$ such that $A' + B'$ is palindromic.

**Test case $3$:** For $A' = aa$ and $B' = aaaa$, $A' + B' = aaaaaa$ is palindromic.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
abcdd
ac
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 3
abc
xyz
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 4
aa
aaaa
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
1 3
a
aax
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

[Practice](https://www.codechef.com/problems/CONCATPAL)

[Contest: Division 1](https://www.codechef.com/START77A/problems/CONCATPAL)

[Contest: Division 2](https://www.codechef.com/START77B/problems/CONCATPAL)

[Contest: Division 3](https://www.codechef.com/START77C/problems/CONCATPAL)

[Contest: Division 4](https://www.codechef.com/START77D/problems/CONCATPAL)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have two strings A and B, which you can rearrange as you wish to form A' and B'.

Is it possible to make A'+B' a palindrome?

#
[](#explanation-5)EXPLANATION:

Suppose N \leq M, i.e, A is the shorter string.

Now, suppose we’re able to obtain A' and B' such that A'+B' is a palindrome.

Since N \leq M, this means that:

- The last N characters of B' must exactly form A'.

- The remaining M - N characters of B' must form a palindrome among themselves.

Notice that this isn’t too hard to check:

- Let \text{freq}_A[c] denote the number of occurrences of c in A. Similarly define \text{freq}_B[c].

- The first condition then simply says that \text{freq}_A[c] \leq \text{freq}_B[c] for *every* character c from `'a'` to `'z'`.

- This can be checked quite easily by just building both frequency tables.

- The second condition requires us to check whether all the remaining characters can form a palindrome via rearrangement.

- This is a rather classical task, and has a simple solution: a list of characters can be rearranged to form a palindrome if and only if at most one of them occurs an odd number of times.

- Notice that this is also easy to check with the frequency tables we have: the number of c such that (\text{freq}_B[c] - \text{freq}_A[c]) is odd should be \leq 1.

The answer is affirmative if and only if both conditions above are satisfied.

If N \gt M just swap A and B and apply the above algorithm anyway.

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
    int n = readIntSp(1, 2e5);
    int m = readIntLn(1, 2e5);
    sumN += n + m;
    string a = readStringLn(n, n);
    string b = readStringLn(m, m);
    for(auto &x: a) assert(x >= 'a' and x <= 'z');
    for(auto &x: b) assert(x >= 'a' and x <= 'z');
    if(n > m)
        swap(a, b), swap(n, m);
    array<int, 26> a_cnt{}, b_cnt{};
    for(auto &x: a)
        a_cnt[x - 'a']++;
    for(auto &x: b)
        b_cnt[x - 'a']++;
    bool ok = true;
    int odd = 0;
    for(int i = 0; i < 26; i++)
    {
        if(b_cnt[i] < a_cnt[i])
            ok = false;
        odd += (b_cnt[i] - a_cnt[i]) % 2;
    }
    if(odd <= 1 and ok)
        cout << "YES\n";
    else
        cout << "NO\n";
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 2e5);
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
	n, m = map(int, input().split())
	freq = {}
	for c in input():
		add = (n >= m) - (n < m)
		if c in freq: freq[c] += add
		else: freq[c] = add
	for c in input():
		add = (m > n) - (m <= n)
		if c in freq: freq[c] += add
		else: freq[c] = add
	odd = 0
	for y in freq.values():
		odd += y%2
	print('YES' if odd <= 1 and min(freq.values()) >= 0 else 'NO')
``

</details>
