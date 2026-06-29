# Maximum Sum Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXSUMPERM |
| Difficulty Rating | 1873 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MAXSUMPERM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MAXSUMPERM) |

---

## Problem Statement

You are given an array $A$ of size $N$. The array will be used to perform $Q$ queries, where each query is comprised of a pair of integers, denoted by $L_i$ and $R_i$.

Before the queries are executed, you are allowed to rearrange the elements in array $A$ as desired.

Next, an integer variable $X$ is initialized to 0. For each of the $i$-th queries, calculate the sum of elements from $A_{L_i}$ through $A_{R_i}$ inclusive (i.e. $A_{L_i} + A_{L_i + 1} + \cdots + A_{R_i}$), and add this sum to $X$.

The objective of this problem is to find an arrangement of array $A$ that maximizes the final value of $X$ after all $Q$ queries have been processed.

If there are multiple possible arrangements of $A$ which achieve this maximum value, you can output any.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the length of array and number of queries, respectively.
    - The next line contains $N$ space-separated integers denoting the elements of the array.
    - The next $Q$ lines describe the queries. The $i$-th of these $Q$ lines contains two space-separated integers $L_i$ and $R_i$, describing the range for the $i$-th query.

---

## Output Format

For each test case, output on a new line the maximum possible value of $X$. And in the next line, output the rearranged array $A$, which achieves that maximum possible value.

---

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq N \leq 200000$
- $1 \leq Q \leq 200000$
- $1 \leq A_i \leq 100000$
- $1 \leq L_i \leq R_i \leq N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$
- The sum of $Q$ over all test cases won't exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5 2
1 2 3 4 5
1 4
2 3
2 3
1 1
1 1
1 2
2 2
```

**Output**

```text
23
2 4 5 3 1 
4
1 1
```

**Explanation**

**Testcase 1:** The given array is $[1, 2, 3, 4, 5]$. Suppose we rearrange it as $[2, 4, 5, 3, 1]$.
- Initially, $X = 0$
- In the first query, we add $A_1 + A_2 + A_3 + A_4$ to $X$. So $X = 0 + 14 = 14$.
- In the second query, we add $A_2 + A_3$ to $X$. So $X = 14 + 9 = 23$.

This is the maximum possible value of $X$ that we can achieve after the $Q$ queries. And so, the output is $23$, and this rearranged array.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXSUMPERM)

[Contest: Division 1](https://www.codechef.com/START91A/problems/MAXSUMPERM)

[Contest: Division 2](https://www.codechef.com/START91B/problems/MAXSUMPERM)

[Contest: Division 3](https://www.codechef.com/START91C/problems/MAXSUMPERM)

[Contest: Division 4](https://www.codechef.com/START91D/problems/MAXSUMPERM)

***Author:*** [rishabh_0906](https://www.codechef.com/users/rishabh_0906)

***Preparer:*** [rivalq](https://www.codechef.com/users/rivalq)

***Tester and Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1873

#
[](#prerequisites-3)PREREQUISITES:

Prefix sums

#
[](#problem-4)PROBLEM:

There’s an array A, and Q queries on it. You also have an integer X, initially equal to 0.

The i-th query consists of two indices L_i and R_i.

For this query, you add A_{L_i} + A_{L_i + 1} + \ldots  + A_{R_i} to X.

You’re allowed to rearrange A as you like *before* any queries are performed.

What’s the maximum possible final value of X?

#
[](#explanation-5)EXPLANATION:

Suppose A was fixed. Let’s look at how X is computed from a different perspective.

For each query (L_i, R_i), let’s say we *select* all the indices from L_i to R_i.

Let C_i be the number of times index i is selected across all the queries.

Then, the final value of X is simply \sum_{i=1}^N C_i \cdot A_i, that is, the sum of A_i multiplied by the number of times index i was selected; across all i.

Notice that the C_i values are completely independent of ordering of A; and depend purely on the query indices.

All the C_i values can be computed in \mathcal{O}(N + Q) time.

How?

Let’s start with C_i = 0 for all i.

For each query (L_i, R_i), we want to add 1 to each C_j such that L_i \leq j \leq R_i.

Doing this in a bruteforce manner will take \mathcal{O}(N \cdot Q) time.

However, we can do better if we process queries *offline*.

In fact, processing many range-add updates like this offline is a standard trick, and can be done with the help of prefix sums/difference arrays.

The idea is as follows:

- Consider a new array D of length N, where D_i = C_i - C_{i-1} (treat C_0 = 0).

D is the *difference array* of C.

- Note that if we know the values of array D, then finding C is easy: we have D_1 + D_2 + \ldots + D_i = (C_1 - C_0) + (C_2 - C_1) + \ldots + (C_i - C_{i-1}) = C_i - C_0 = C_i.

So, C is simply the prefix sum of the D array!

- Now, look at how queries on C change D.

If we add 1 to the range from L to R of C, then:

-
D_L increases by 1, because D_L = C_L - C_{L-1} and the latter doesn’t change.

-
D_{L+1}, D_{L+2}, \ldots, D_R all don’t change, since we’re both adding 1 and subtracting 1 from them.

-
D_{R+1} decreases by 1.

So, each update on C only changes two values of D.

Maintaining this is therefore very easy: start with D filled with all zeros; and for each update (L, R), increment D_L by 1 and decrement D_{R+1} by 1.

Finally, obtain C as the prefix sum array of D.

Now, each query takes \mathcal{O}(1) work, and we compute prefix sums once at the end; for \mathcal{O}(N+Q) time in total.

Once the C_i values are known, we want to ‘match’ the values of A to them so that \sum C_i\cdot A_i is maximized.

This can be done greedily.

That is, match the highest C_i with the highest A_i, the second highest C_i with the second highest A_i, and so on.

The correctness of this follows from the [Rearrangement inequality](https://en.wikipedia.org/wiki/Rearrangement_inequality).

Implementing this is fairly straightforward: sort the C_i and A_i values in ascending order, then just match them.

To reconstruct the required array, all you need to do is keep a record of the indices of the C_i values after they’ve been sorted.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N + Q) per test case.

#
[](#code-7)CODE:

Preparer's code (C++)
``#include <bits/stdc++.h>
using namespace std;

const int M = 1e9 + 7;

int solve() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    sort(a.begin() + 1, a.end());
    vector<int> w(n + 2);

    while (q--) {
        int l, r;
        cin >> l >> r;
        w[l]++;
        w[r + 1]--;
    }

    for (int i = 1; i <= n; i++) w[i] += w[i - 1];
    vector<int> ord(n + 1, 0);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin() + 1, ord.end(), [&](int i, int j) {
        return w[i] < w[j];
    });
    long long ans = 0;
    auto b = a;

    for (int i = 1; i <= n; i++) {
        b[ord[i]] = a[i];
        ans += 1LL * w[ord[i]] * a[i];
    }
    cout << ans << "\n";
    for (int i = 1; i <= n; i++) {
        cout << b[i] << " ";
    }
    cout << "\n";
    return 0;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
``

Editorialist's code (Python)
``for test in range(int(input())):
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ct = [0]*(n+1)
    for _ in range(q):
        l, r = map(int, input().split())
        ct[l-1] += 1
        ct[r] -= 1
    for i in range(1, n): ct[i] += ct[i-1]
    indices = list(range(n))
    indices.sort(key = lambda i : ct[i])
    ans = [0]*n
    x = 0
    for i in range(n):
        ans[indices[i]] = a[i]
        x += ct[indices[i]] * a[i]
    print(x)
    print(*ans)
``

</details>
