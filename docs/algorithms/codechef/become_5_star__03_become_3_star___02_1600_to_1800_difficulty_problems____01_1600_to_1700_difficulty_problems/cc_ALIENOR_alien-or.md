# ALIEN-OR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALIENOR |
| Difficulty Rating | 1639 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ALIENOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ALIENOR) |

---

## Problem Statement

You are given:
- positive integers $N$ and $K$ $(K \le N)$.
- an array $A$ of size $N$, where each element of the array is a **binary** string of length $K$;

For each $1\le j\lt 2^K$, your task is to find whether there exists a set of indices $\{i_1, i_2, \ldots, i_m\}$ $(1\le i_j, m \le N)$ such that:
- The decimal value of $(A_{i_1}$ $|$ $A_{i_2}$ $|$ $A_{i_3}$ $|$ $\ldots$ $|$ $A_{i_m})$ equals $j$, where $|$ denotes [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#:~:text=A%20bitwise%20OR%20is%20a) operation.

Print `YES` if a set of indices satisfying the given condition exists for **all** $1\le j\lt 2^K$. Otherwise, print `NO`.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases.
- The first line of each test case contains two integers $N$ and $K$.
- The $i$-th of the next $N$ lines contains the binary string $A_i$.

---

## Output Format

For each test case, print `YES` if a set of indices satisfying the given condition exists for **all** $1\le j\lt 2^K$. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 50$
- $1 \leq N \leq 100$
- $1 \leq K \leq N$
- $|A_i| = K$
- $A_i \in \{0, 1\}$
- The sum of $N$ over all test cases won't exceed $500$.

---

## Examples

**Example 1**

**Input**

```text
3
2 2
01
10
4 3
000
010
011
100
6 3
000
001
010
011
100
101
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:**
- $j = 1$ : The set of indices $\{1\}$ satisfies the condition as decimal value of $A_1 = 1 = j$.
- $j = 2$ : The set of indices $\{2\}$ satisfies the condition as decimal value of $A_2 = 2 = j$.
- $j = 3$ : The set of indices $\{1, 2\}$ satisfies the condition as decimal value of $(A_1$ $|$ $A_2) = 3 = j$.

**Test case $2$:** The set of indices for $j = 2, 3, 4, 6, 7$ are $\{2\}, \{3\}, \{4\}, \{2,4\},$ and $\{3, 4\}$ respectively.
However, there doesn't exist any set of indices for $j=1$ and $j=5$. Hence output is `NO`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
01
10
4 3
000
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
010
011
100
6 3
000
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
001
010
011
100
101
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALIENOR)

[Contest: Division 1](https://www.codechef.com/START132A/problems/ALIENOR)

[Contest: Division 2](https://www.codechef.com/START132B/problems/ALIENOR)

[Contest: Division 3](https://www.codechef.com/START132C/problems/ALIENOR)

[Contest: Division 4](https://www.codechef.com/START132D/problems/ALIENOR)

***Author:*** [akash_chauhan0](https://www.codechef.com/users/akash_chauhan0)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given N binary strings, each of length K, denoting the binary representations of a set of integers.

Let A_i denote the i'th integer.

For each x from 0 to 2^{K-1}, does x appear as the bitwise OR of some subset of the A_i?

# [](#explanation-5)EXPLANATION:

We’re interested in the integers from 1 to 2^{K-1}, which equivalently is all integers with at most K digits in binary.

Notice that 2^K can be extremely large, so it’s not really possible to check every subset.

Instead, observe that if we have a subset S_1 whose bitwise OR is x, and a subset S_2 whose bitwise OR is y, then the subset S_1\cup S_2 has a bitwise OR of (x\mid y).

Why?

The bitwise OR of a set of strings S is, quite simply, the string that contains a 1 at any position that *at least* one string from S contains a 1 in.

So,

- x contains information about all the set positions of S_1.

- y contains information about all the set positions of S_2.

- x\mid y contains information about all the set positions of S_1 *or* S_2, which is just S_1 \cup S_2.

In simpler words, we can build “big” bitwise ORs using “small” ones.

So, intuitively, if we have enough “small” values, we’ll be able to get every value by taking unions like this to get larger ones.

The question is, what exactly is ‘small’ here?

To answer that, think of the “building blocks” of bitwise OR: the numbers which cannot be obtained as the bitwise OR of any other numbers.

These are exactly those numbers that have **exactly one** bit set in their binary representation, i.e, numbers of the form `00...010...00`.

For example, if K = 4, you’re looking at `0001, 0010, 0100, 1000`.

If any one of these is absent, it clearly cannot ever be obtained as a bitwise OR of *other* binary strings.

On the other hand, if they’re all present, we can use the subset union method mentioned above to get *any* bitwise OR, just by taking the ones corresponding to the set bits.

So, quite simply, we only need to check if every possible string with exactly one bit set is present among the ones we have.

That is, for each i from 1 to K, the string that’s filled with 0's except at position i, should be present in our set.

There are K such strings, and for each of them, you can check each of the N strings we have for its existence - the constraints are small enough that this brute-force check will be fast enough.

There are faster implementations, but they aren’t needed to get AC.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(NK^2) or \mathcal{O}(NK) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

bool canBeImpressed(vector<string> S, int K)
{
    // to mark up each of i belongs to [0,K-1]
    // iff there exists a binary string '1' followed by 'i' zeroes
    map<int, int> pow;

    // CONCEPT - 2^n (in Decimal) =  1 followed by 'n' zeroes (in Binary)
    for (string bin : S)
    {
        // if it's of the form 2^i, then it must only consists of one '1'
        if (count(bin.begin(), bin.end(), '1') == 1)
        {
            // simple math to extract position of '1' from LHS(Unit Place)
            int i = (bin.size() - bin.find('1') - 1);
            pow[i]++;
        }
    }

    for (int i = 0; i < K; i++)
    {
        // if any of i missing, then it can't possible to form subsets for every j belongs [0,2^k-1]
        // because 2^i can't be represent using any subsequence of diff powers of 2's
        if (pow.find(i) == pow.end())
            return false;
    }
    return true;
}

int main()
{
    // INUITION ::
    // Since we 're required to form subsets for j belongs to [0,2^k-1]
    // We must require k binary string : {2^0,2^1,2^2,..,2^(k-1)}
    // as they can't be formed using Bitwise OR any other subsets
    // Now, if we observe closely we don't require any more binary strings because
    // We can form every binary string using subset combination of these k binary
    // strings such that  Bitwise OR = [0,2^k-1]
    int T;
    cin >> T;
    while (T--)
    {
        int N, K;
        cin >> N >> K;
        vector<string> S(N);
        for (int i = 0; i < N; i++)
            cin >> S[i];

        if (canBeImpressed(S, K))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

void Solve()
{
    int n, k; cin >> n >> k;

    vector <bool> found(k, false);
    for (int i = 0; i < n; i++){
        string str; cin >> str;

        int cnt = 0;
        for (auto x : str) cnt += x == '1';

        if (cnt == 1){
            int pos = -1;
            for (int j = 0; j < k; j++) if (str[j] == '1') pos = j;

            found[pos] = true;
        }
    }

    for (auto x : found) if (!x){
        cout << "No\n";
        return;
    }
    cout << "Yes\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    strs = []
    for i in range(n):
        strs.append(input().strip())
    have = 0
    for i in range(k):
        for s in strs:
            if s.count('1') == 1 and s[i] == '1':
                have += 1
                break
    print('Yes' if have == k else 'No')
``

</details>
