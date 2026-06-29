# Dynamic Programming - String Distance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP32 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Dynamic Programming |
| Official Link | [PREP32](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_14/problems/PREP32) |

---

## Problem Statement

Given two strings $A$ and $B$ consisting of lowercase english characters. Find the **minimum** number of operations required to convert $A$ to $B$.

You have the following operations permitted on $A$,
- Insert a character
- Delete a character
- Replace a character

For example,
- $A =$ `codechef`, now if you insert `q` at position $5$ then $A = $ `codeqchef`.
- $A =$ `codechef`, now if you delete position $6$ then $A = $ `codecef`.
- $A =$ `codechef`, now if you replace position $5$ with `q` then $A = $ `codeqhef`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains string $A$.
- The second line of each test case contains string $B$.

---

## Output Format

For each test case, output on a new line the minimum number of operations required to convert $A$ to $B$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq |A|, |B| \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
codechef
fochf
aa
alq
ab
ab
```

**Output**

```text
4
2
0
```

**Explanation**

**Test case $1$**: $A =$ `codechef`. You can do following,
- Replace $A_1$ with `f`. So $A =$ `fodechef`.
- Delete $A_3$, $A_4$, $A_7$. So $A =$ `fochf`.

**Test case $2$**: $A =$ `aa`. You can do following,
- Replace $A_2$ with `q`. So $A =$ `aq`.
- Insert `l` at $A_2$. So $A =$ `alq`.

**Test case $3$**: Both strings same.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
codechef
fochf
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
aa
alq
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
ab
ab
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# DSA Interview Preparation: Edit Distance Problem Editorial

In this lesson, we address the **Edit Distance** problem. The goal is to convert one string $A$ into another string $B$ using three allowed operations: insertion, deletion, and replacement. We want to determine the minimum number of operations required. This classical dynamic programming problem helps in understanding how to decompose problems into subproblems and build solutions iteratively.

Below we discuss two correct approaches to solving the problem.

---

## Approach 1: Iterative Bottom-Up Dynamic Programming

### Overview

The most common solution uses a **Bottom-Up Dynamic Programming (DP)** approach. We define a DP table $dp[i][j]$ representing the minimum edit distance between the first $i$ characters of $A$ and the first $j$ characters of $B$. The transitions are:

- If $i = 0$, then $dp[0][j] = j$ (all insertions are required).
- If $j = 0$, then $dp[i][0] = i$ (all deletions are required).
- If $A[i-1] == B[j-1]$, then $dp[i][j] = dp[i-1][j-1]$ (no operation needed).
- Otherwise, $dp[i][j] = 1 + \min(dp[i-1][j],\; dp[i][j-1],\; dp[i-1][j-1])$ (delete, insert, or replace).

This solution runs in $O(m \times n)$ time, where $m$ and $n$ are the lengths of $A$ and $B$, respectively.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
#include

using namespace std;

int minOperationsDP(const string &A, const string &B) {
    int m = A.size(), n = B.size();
    vector> dp(m + 1, vector(n + 1, 0));

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0)
                dp[i][j] = j;
            else if (j == 0)
                dp[i][j] = i;
            else if (A[i - 1] == B[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = 1 + min({ dp[i - 1][j],    // Delete
                                     dp[i][j - 1],    // Insert
                                     dp[i - 1][j - 1] // Replace
                                   });
        }
    }
    return dp[m][n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;
        cout << minOperationsDP(A, B) << "\n";
    }

    return 0;
}
```

#### Python Code

```python
def min_operations_dp(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],   # Delete
                                   dp[i][j - 1],   # Insert
                                   dp[i - 1][j - 1]) # Replace
    return dp[m][n]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        print(min_operations_dp(A, B))
```

---

## Approach 2: Space-Optimized Dynamic Programming

### Overview

The iterative DP approach can be optimized in terms of space because each row of the DP table only depends on the previous row. By maintaining only two rows (or even a single row with careful updates), the space requirement is reduced from $O(m \times n)$ to $O(n)$, while the time complexity remains $O(m \times n)$.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
#include

using namespace std;

int minOperationsOptimized(const string &A, const string &B) {
    int m = A.size(), n = B.size();
    vector prev(n + 1, 0), curr(n + 1, 0);

    for (int j = 0; j <= n; j++) {
        prev[j] = j;
    }

    for (int i = 1; i <= m; i++) {
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (A[i - 1] == B[j - 1])
                curr[j] = prev[j - 1];
            else
                curr[j] = 1 + min({ prev[j],      // Delete
                                    curr[j - 1],  // Insert
                                    prev[j - 1] }); // Replace
        }
        prev = curr;
    }
    return prev[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;
        cout << minOperationsOptimized(A, B) << "\n";
    }
    return 0;
}
```

#### Python Code

```python
def min_operations_optimized(A, B):
    m, n = len(A), len(B)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] * (n + 1)
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j],      # Delete
                                  curr[j - 1],  # Insert
                                  prev[j - 1])  # Replace
        prev = curr
    return prev[n]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        print(min_operations_optimized(A, B))
```

---

## Final Thoughts

1. **Iterative Bottom-Up DP:**
   This is the classical solution that builds a DP table step by step. It clearly demonstrates how each state depends on previously computed values. Its straightforward formulation makes it a great teaching tool for dynamic programming.

2. **Space-Optimized DP:**
   This approach refines the basic DP method by minimizing space usage. By noting that only the previous row is needed to compute the current row, we reduce the space complexity to $O(n)$ while keeping the same time complexity. This is particularly beneficial when handling large inputs.

Both methods provide strong foundations in dynamic programming that can be applied to a variety of problems.

Happy Coding!

</details>
