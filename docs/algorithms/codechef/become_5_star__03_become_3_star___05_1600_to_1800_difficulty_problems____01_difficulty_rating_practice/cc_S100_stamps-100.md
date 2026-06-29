# Stamps 100

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | S100 |
| Difficulty Rating | 1631 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [S100](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/S100) |

---

## Problem Statement

You are given a **binary** string $S$ of length $N$.

You can apply the following operation any (possibly zero) number of times:
- Select an integer $i\ \lparen 1 \leq i \leq N-2 \rparen$ and replace the substring $S_i S_{i+1} S_{i+2}$ with `100`.

Find the **lexicographically smallest** string after the operations.

Note: String $X$ is lexicographically smaller than string $Y$ if $X_i \lt Y_i$, where $i$ is the first index where $X$ and $Y$ differ.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of string $S$.
    - The second line of each test case contains a binary string $S$.

---

## Output Format

For each test case, output the **lexicographically smallest** string after the operations.

---

## Constraints

- $1 \leq T \leq 10^5$
- $3 \leq N \leq 3 \cdot 10^5$
- $|S| = N$
- Each character of $S$ is either `0` or `1`.
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
3
110
4
0001
```

**Output**

```text
100
0001
```

**Explanation**

**Test case $1$:** You can convert $S$ into `100`.
Since `100` is lexicographically smaller than `110`, output `100`.

**Test case $2$:** You should keep $S$ as it is without applying any operations, so output `0001`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
110
```

**Output for this case**

```text
100
```



#### Test case 2

**Input for this case**

```text
4
0001
```

**Output for this case**

```text
0001
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/S100)

[Contest: Division 1](https://www.codechef.com/START100A/problems/S100)

[Contest: Division 2](https://www.codechef.com/START100B/problems/S100)

[Contest: Division 3](https://www.codechef.com/START100C/problems/S100)

[Contest: Division 4](https://www.codechef.com/START100D/problems/S100)

***Author & Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1631

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given a string binary S. In one move, you can replace a substring of length 3 by `"100"`.

Find the lexicographically smallest string you can attain.

# [](#explanation-5)EXPLANATION:

Let k be the *first occurrence* of \texttt{1} in S, i.e, the smallest index such that S_k = \texttt{1} . If no ones exist in the string, let k = N+1 instead.

In particular, S_i = \texttt{0} for all 1 \leq i \lt k.

Note that it’s never optimal to perform an operation involving an index \lt k, because we would replace a prefix zero with a 1, and that isn’t optimal for lexicographical smallness.

So, we only perform replacement operations on substrings that start at indices \geq k.

Now, a simple analysis of this should tell you that:

- If k \gt N-2, then it’s not possible to even perform a move; so the optimal solution is to do nothing and just print S.

- If k \leq N-2, then we can perform replacement operations on some substrings.

Here, we can in fact make S_i = \texttt{0} for **every** i \gt k via the following process:

- Perform the replacement operation on substring S_iS_{i+1}S_{i+2} in **decreasing order** of i, starting from i = N-2 and going down to i = k.

It’s easy to see that:

- The first move sets S_N = S_{N-1} = \texttt{0}.

- The second move sets S_{N-2} = \texttt{0} without changing anything to its right.

- The second move sets S_{N-3} = \texttt{0} without changing anything to its right.

\vdots

In fact, in the second case we set *every* character of S to zero except S_k, and it’s easy to see why this is the lexicographically smallest string possible - making S_k zero using an operation would make some character to the *left* of S_k change from 0 to 1, and that’s not optimal.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int tt;
	cin >> tt;
    while (tt--) {
		int n;
		cin >> n;
        string s;
        cin >> s;
        int i = (int) (find(s.begin(), s.end(), '1') - s.begin());
        if (i <= n - 3) {
            for (int j = i + 1; j < n; j++) {
                s[j] = '0';
            }
        }
        cout << s << " \n";
    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(n-2):
        if s[i] == '1':
            s = s[:i] + '1' + '0'*(n-i-1)
            break
    print(s)
``

</details>
