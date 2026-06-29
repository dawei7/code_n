# K Increment Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KPAL |
| Difficulty Rating | 2038 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [KPAL](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/KPAL) |

---

## Problem Statement

Chef has an array $A$ of size $N$ and an integer $K$. He can perform the following operation on $A$ any number of times:
- Select any $K$ distinct indices $i_1, i_2, \ldots, i_K$ and increment the array elements at these $K$ indices by $1$.
Formally, set $A_{i_j} := A_{i_j} + 1$ for all $1 \le j \le K$.

For example, if $A = [3, 2, 8, 4, 6]$ and we select the indices $2, 3, 5$, then $A$ becomes $[3, 2 + 1, 8 + 1, 4, 6 + 1]$ i.e. $[3, 3, 9, 4, 7]$.

Determine if Chef can make the array $A$ palindromic by applying the given operation **any** number of times.

Note: An array is called palindrome if it reads the same backwards and forwards, for e.g. $[4, 10, 10, 4]$ and $[7, 1, 7]$ are palindromic arrays.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $K$ — the size of the array $A$ and the parameter mentioned in the statement.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output `YES` if we can make $A$ palindromic by applying the given operation. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le K \le N \le 10^5$
- $1 \le A_i \le 10^6$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5 3
2 4 5 4 2
6 1
4 5 5 4 6 4
6 2
4 5 5 4 6 4
4 2
1 2 3 3
```

**Output**

```text
YES
YES
YES
NO
```

**Explanation**

**Test case $1$:** The given array $A$ is already palindromic.

**Test case $2$:** We can apply the following operations:
- Select index $[4]$: $A$ becomes $[4, 5, 5, 5, 6, 4]$
- Select index $[2]$: $A$ becomes $[4, 6, 5, 5, 6, 4]$

**Test case $3$:** We can apply the following operations:
- Select index $[2, 4]$: $A$ becomes $[4, 6, 5, 5, 6, 4]$

**Test case $4$:** It can be proven that $A$ can not be converted into a palindrome using the given operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
2 4 5 4 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
6 1
4 5 5 4 6 4
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
6 2
4 5 5 4 6 4
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4 2
1 2 3 3
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

[Practice](https://www.codechef.com/problems/KPAL)

[Contest: Division 1](https://www.codechef.com/START77A/problems/KPAL)

[Contest: Division 2](https://www.codechef.com/START77B/problems/KPAL)

[Contest: Division 3](https://www.codechef.com/START77C/problems/KPAL)

[Contest: Division 4](https://www.codechef.com/START77D/problems/KPAL)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You have an array A and an integer K.

In one move, you can choose **exactly** K elements of A and increase their values by 1.

Is is possible to make A a palindrome?

#
[](#explanation-5)EXPLANATION:

Let’s get a trivial edge-case out of the way first:

If K = N then we can only increase every element. In this case, if A isn’t already a palindrome it’s obviously impossible to turn it into one.

From now on, we’ll assume K \lt N.

Our objective now is to make A_i = A_{N+1-i} for every 1 \leq i \leq N.

In particular, if A_i \lt A_{N+1-i}, we need to increase it by (A_{N+1-i} - A_i).

After that’s achieved, A_i and A_{N+1-i} need to be increased by equal amounts, to preserve their equality.

When either N or K is odd, it can be seen that it’s always possible to make A a palindrome.

How?

First, say K is odd.

We have the following simple strategy:

- If A_i = A_{N+1-i} for every i, we’re done.

- Otherwise, pick an index i such that A_i \lt A_{N+1-i}

- Next, choose \frac{K-1}{2} pairs of opposite indices that don’t include N+1-i (which is always possible since K \lt N), for a total of K indices chosen.

- Perform the operation on these K indices, and continue.

Each move brings A_i closer to A_{N+1-i}, while not breaking the ‘palindrome-ness’ of all other indices.

It’s not hard to see that it’ll finish in finite time, at which point we’ll be done.

Next, say N is odd and K is even.

Once again we have a similar strategy:

- Pick an index i such that A_i \lt A_{N+1-i}

- Pick the middle index, which can be increased freely

- Finally, pick \frac{K-2}{2} pairs of opposite indices excluding N+1-i (once again, always possible since K \lt N) and perform the operation on these K.

This leaves us with the case when N is even, K is even, and K \lt N.

Note that:

- Since N is even, if the final array is a palindrome its sum will be even.

- Since K is even, each move increases the sum of the array by an even number.

Together, this tells us that if sum(A) is odd, it can never be turned into a palindrome.

What if sum(A) is even?

We can always make A into a palindrome!

Proof

This can be proved with a minor modification to our proofs odd K and N.

Consider the following process:

- If A_i = A_{N+1-i} for every i, we’re done.

- Otherwise, find an index i such that A_i \lt A_{N+1-i}.

- There are now two possible cases.

- If there exists *another* index j such that A_j \lt A_{N+1-j}, then pick j as well, then pick \frac{K-2}{2} opposite pairs not including these two and perform the operation on them.

- If no such j exists, then the sum of the array being even means that A_i+2 \leq A_{N+1-i}.

- So, pick an arbitrary index j (that is not N+1-i), and \frac{K-2}{2} more opposite pairs and perform the operation on them.

- Next, pick i, N+1-j, and then \frac{K-2}{2} more pairs to perform the operation.

- This way we’ve increased A_i by 2 while preserving ‘palindrome-ness’ of the other indices.

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
    int n = readIntSp(1, 1e5);
    int k = readIntLn(1, n);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e6);
    vector<int> b = a;
    reverse(b.begin(), b.end());
    if(a == b)
        cout << "YES\n";
    else
    {
        if(k == n)
            cout << "NO\n";
        else if(n % 2 == 1 or k % 2 == 1)
            cout << "YES\n";
        else
        {
            int sum = accumulate(a.begin(), a.end(), 0LL);
            if(sum % 2 == 0)
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }
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
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	if n == k:
		print('Yes' if a == a[::-1] else 'No')
		continue
	if n%2 == 1 or k%2 == 1:
		print('Yes')
		continue
	print('Yes' if sum(a)%2 == 0 else 'No')
``

</details>
