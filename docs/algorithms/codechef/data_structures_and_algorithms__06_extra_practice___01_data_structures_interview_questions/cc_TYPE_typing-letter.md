# Typing Letter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TYPE |
| Difficulty Rating | 1250 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [TYPE](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/TYPE) |

---

## Problem Statement

You have to type an email to send to your friend. The email can be represented as a string $T$ (which does not contain spaces). To complete your task you can perform **any one** of the following actions in one move:

- Append a character at the end of the string.
- Append a duplicate of the current string.

Find the **minimum** number of moves required to type the email.

---

## Input Format

- First-line will contain $T$ - the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the size of the string.
- The second line of every test case contains a string $T$ of size $N$.

---

## Output Format

For each testcase, output in a single line - the answer to the $i$-th test case.

---

## Constraints

- $1 \leq T \leq 150$
- $1 \leq N \leq 2 \cdot 10^3, \sum N \leq 5\cdot10^3$
- The string contains only lowercase english letters

---

## Examples

**Example 1**

**Input**

```text
3
6
oooobj
1
q
5
qqqqr
```

**Output**

```text
5
1
4
```

**Explanation**

- **Test Case $1$**: We can type the email in the following manner:

o -> oo -> oooo -> oooob -> oooobj

So total of $5$ moves are required.

- **Test Case $2$**: We need to type a single character, so $1$ move is required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
oooobj
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
1
q
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5
qqqqr
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we learn how to build the email string using two allowed moves:
1. **Append a character at the end of the string.**
2. **Append a duplicate of the current string.**

The goal is to achieve the target string using a minimum number of moves. In our discussion, we present **two approaches** to solve this problem.

---

## Approach 1: Dynamic Programming (Iterative DP)

We define an array $\texttt{dp}[0 \ldots n]$, where $\texttt{dp}[i]$ represents the minimum number of moves required to build the first $i$ characters of the email. The recurrence is:

$$
\texttt{dp}[i] = \texttt{dp}[i-1] + 1
$$

because you can always form the $i^\text{th}$ character by appending it individually. In addition, if the first $j$ characters (i.e. the prefix) match the subsequent substring of length $i-j$, then we can form the string of length $i$ by first forming the prefix in $\texttt{dp}[j]$ moves and then using a duplicate move (which doubles the current string). Note that a duplication move is valid only when the substring lengths match; that is, when $i - j = j$ or equivalently $i = 2j$. The transition becomes:

$$
\texttt{dp}[i] = \min\Big(\texttt{dp}[i], \texttt{dp}[j] + 1\Big)
$$

for any $j$ such that $\texttt{T}[0:j] = \texttt{T}[j:i]$ holds. This iterative DP method has a time complexity of approximately $O(n^2)$ which is acceptable under the given constraints.

### C++ Implementation

```cpp
#include
#include
#include
#include
using namespace std;

int minMoves(const string &T) {
    int n = T.length();
    vector dp(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + 1; // Append one character.
        // Check if duplication is possible.
        for (int j = i - 1; j > 0; j--) {
            if (T.substr(0, j) == T.substr(j, i - j)) {
                dp[i] = min(dp[i], dp[j] + 1);
                break; // Once found, further checks are unnecessary.
            }
        }
    }
    return dp[n];
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string email;
        cin >> email;
        cout << minMoves(email) << endl;
    }
    return 0;
}
```

### Python Implementation

```python
def min_moves(email):
    n = len(email)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1  # Append one character.
        # Check for a valid duplication move.
        for j in range(i - 1, 0, -1):
            if email[:j] == email[j:i]:
                dp[i] = min(dp[i], dp[j] + 1)
                break
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    email = input().strip()
    print(min_moves(email))
```

---

## Approach 2: Recursive DFS with Memoization

A recursive approach can also be used to solve this problem. We define a recursive function $\texttt{dfs}(i)$ that returns the minimum moves required to form the substring $\texttt{T}[0:i]$. At every state $i$, we have two options:

1. **Append a character:** This takes one move, and we move to state $i+1$.
2. **Duplicate the current string:** If $i > 0$, and the condition $\texttt{T}[0:i] = \texttt{T}[i:2i]$ holds (ensuring the move is valid), we can move to state $2i$ in one move.

We cache the results in a memoization table to avoid recomputation.

### C++ Implementation

```cpp
#include
#include
#include
#include
using namespace std;

int n;
string s;
vector memo;

int dfs(int i) {
    if(i == n) return 0;
    if(memo[i] != -1) return memo[i];
    // Option 1: Append one character.
    int res = 1 + dfs(i + 1);
    // Option 2: Duplicate the current string if valid.
    if(i > 0 && 2 * i <= n && s.substr(0, i) == s.substr(i, i)) {
        res = min(res, 1 + dfs(2 * i));
    }
    memo[i] = res;
    return res;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        cin >> n >> s;
        memo.assign(n, -1);
        cout << dfs(0) << endl;
    }
    return 0;
}
```

### Python Implementation

```python
import sys
sys.setrecursionlimit(10000)

def dfs(i, n, s, memo):
    if i == n:
        return 0
    if memo[i] != -1:
        return memo[i]
    # Option 1: Append a character.
    res = 1 + dfs(i + 1, n, s, memo)
    # Option 2: Duplicate if valid.
    if i > 0 and 2 * i <= n and s[:i] == s[i:2*i]:
        res = min(res, 1 + dfs(2 * i, n, s, memo))
    memo[i] = res
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    memo = [-1] * (n + 1)
    print(dfs(0, n, s, memo))
```

---

## Summary

- **Dynamic Programming (Iterative):** We use an array $\texttt{dp}$ to store the minimum moves for each prefix. This method is easy to understand and implement.
- **Recursive DFS with Memoization:** This approach builds the answer recursively by exploring both options (append and duplicate) at every step while caching intermediate results.

Each approach correctly computes the minimum moves required to form the target string using the allowed operations. For beginners, the DP approach is the most straightforward, while the recursive method demonstrates another useful technique—memoization in DFS.

</details>
