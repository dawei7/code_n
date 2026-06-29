# Dispute Resolving

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PAL_STRING |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [PAL_STRING](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/PAL_STRING) |

---

## Problem Statement

You and Arup were arguing for who is a better problem solver, to resolve the matter you two came to Aman and decided that his decision will be considered final. Aman gave you both a string $S$ of length $N$, and asked you both to find the length of the longest substring $X$ of the array such that the $reverse(X) = X$. Arup failed to solve the task, can you solve the task?

---

## Input Format

- The first line contains an integer $T$ , representing $T$ test cases.

- First line of each test case contains an integer $N$ , representing the size of string $S$.

- Second line of each test case contains the string $S$ of size $N$.

---

## Output Format

- For each test case, print a single integer representing the length of the longest substring X.

---

## Constraints

- $1 \le T \le 100$

- $1 \le N \le 1000$

- $S$ contains only lowercase english letters.

- Sum of $N$ over all test cases does not exceed $10^4$

---

## Examples

**Example 1**

**Input**

```text
3
3
aba
4 
abcd
6
abbacc
```

**Output**

```text
3
1
4
```

**Explanation**

In the first test case, string $aba$ of length $3$ remains the same even after its reversed.

In the second test case, string $b$ of length $1$ remains the same even after its reversed. Other strings of length $1$ are also present which even after getting reversed remains the same.

In the first test case, string $abba$ of length $4$ remains the same even after its reversed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
aba
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
abcd
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
6
abbacc
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Longest Palindromic Substring Problem – Editorial

In this lesson, we explore the problem of finding the longest palindromic substring in a given string. A **palindrome** is a string that reads the same forwards and backwards. Given a string $S$ of length $N$, our task is to determine the length of the longest substring $X$ such that
$$
reverse(X) = X.
$$

We will discuss three important approaches to solve this problem:

## Approach 1: Dynamic Programming (DP)

### Explanation

The dynamic programming approach involves creating a two-dimensional boolean table, $$dp[i][j],$$ where each entry indicates whether the substring $$S[i \ldots j]$$ is a palindrome. The process is as follows:

1. **Base Case:** Every single character is a palindrome. Hence, for all indices $$i$$, set
   $$
   dp[i][i] = \text{true}.
   $$

2. **Substrings of Length 2:** For every pair of adjacent characters, if $$S[i] = S[i+1]$$ then mark $$dp[i][i+1] = \text{true}$$ and update the maximum palindrome length.

3. **Substrings of Length 3 or More:** For each substring $$S[i \ldots j]$$ (with length $$\geq 3$$), check if the first and last characters are the same (i.e. $$S[i] = S[j]$$) and the substring $$S[i+1 \ldots j-1]$$ is a palindrome (i.e. $$dp[i+1][j-1] = \text{true}$$). If both conditions satisfy, then $$S[i \ldots j]$$ is a palindrome.

The time complexity is approximately $$O(N^2)$$ and the space complexity is also $$O(N^2)$$.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

int longestPalindromeSubstring(const string &s) {
    int n = s.size();
    vector> dp(n, vector(n, false));
    int maxLen = 1;

    // Every single character is a palindrome.
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    // Check for substrings of length 2.
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            maxLen = 2;
        }
    }

    // Check for substrings of length 3 or more.
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                maxLen = len;
            }
        }
    }
    return maxLen;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << longestPalindromeSubstring(S) << endl;
    }
    return 0;
}
```

#### Python Code
```python
def longest_palindrome_substring(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_len = 1

    # Every single character is a palindrome.
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2

    # Check for substrings of length 3 or more.
    for l in range(3, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_len = l

    return max_len

T = int(input())
for _ in range(T):
    N = int(input())
    s = input().strip()
    print(longest_palindrome_substring(s))
```

---

## Approach 2: Expand Around Center

### Explanation

The "Expand Around Center" approach is based on the insight that every palindrome mirrors around its center. For each character in the string (considered as a center), you try to expand in both directions as long as the characters match. Note that palindromes can have a center at a single character (odd length) or between two characters (even length).

The method involves:
- Iterating over each index.
- Expanding around the center for both odd and even cases.
- Updating the maximum length when a longer palindrome is found.

This method requires constant extra space, $$O(1),$$ while the time complexity remains $$O(N^2)$$.

### Code Implementation

#### C++ Code
```cpp
#include
#include
using namespace std;

int longestPalindrome(const string &s) {
    int n = s.size();
    if (n == 0) return 0;
    int maxLen = 1;

    auto expandAroundCenter = [&](int left, int right) {
        while (left >= 0 && right < n && s[left] == s[right]) {
            int len = right - left + 1;
            if (len > maxLen)
                maxLen = len;
            left--;
            right++;
        }
    };

    for (int i = 0; i < n; i++) {
        expandAroundCenter(i, i);     // Odd length palindromes.
        expandAroundCenter(i, i + 1); // Even length palindromes.
    }

    return maxLen;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << longestPalindrome(S) << endl;
    }
    return 0;
}
```

#### Python Code
```python
def longest_palindrome(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    max_len = 1

    def expand(left: int, right: int):
        nonlocal max_len
        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)     # Odd length palindrome.
        expand(i, i + 1) # Even length palindrome.

    return max_len

T = int(input())
for _ in range(T):
    N = int(input())
    s = input().strip()
    print(longest_palindrome(s))
```

---

## Approach 3: Manacher’s Algorithm

### Explanation

Manacher’s Algorithm is an advanced technique that finds the longest palindromic substring in $$O(N)$$ time. The key idea is to transform the string to avoid differentiating between odd and even lengths by inserting a separator (for example, `#`) between every two characters (and adding sentinels at the beginning and end). This creates a new string in which every palindrome has an odd length.

We then use an auxiliary array $$p$$ to record the length of the palindrome (in terms of the number of characters that can be expanded from the center) at each position. The algorithm maintains a center and a right boundary to efficiently mirror previously calculated results and update the palindrome lengths.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

int longestPalindromeManacher(const string &s) {
    int n = s.size();
    if (n == 0) return 0;

    // Transform s into t with boundaries.
    string t = "^";
    for (int i = 0; i < n; i++) {
        t += "#" + s.substr(i, 1);
    }
    t += "#$";

    int m = t.size();
    vector p(m, 0);
    int center = 0, right = 0;

    for (int i = 1; i < m - 1; i++) {
        int mirror = 2 * center - i;
        if (i < right)
            p[i] = min(right - i, p[mirror]);

        while (t[i + 1 + p[i]] == t[i - 1 - p[i]])
            p[i]++;

        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }
    }

    int maxLen = 0;
    for (int i = 1; i < m - 1; i++) {
        if (p[i] > maxLen)
            maxLen = p[i];
    }
    return maxLen;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << longestPalindromeManacher(S) << endl;
    }
    return 0;
}
```

#### Python Code
```python
def longest_palindrome_manacher(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    # Transform the string s into t with separators and sentinels.
    t = "^"
    for char in s:
        t += "#" + char
    t += "#$"

    m = len(t)
    p = [0] * m
    center = 0
    right = 0

    for i in range(1, m - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_len = max(p)
    return max_len

T = int(input())
for _ in range(T):
    N = int(input())
    s = input().strip()
    print(longest_palindrome_manacher(s))
```

---

## Conclusion

Each approach offers its own tradeoffs:
- **Dynamic Programming** is intuitive and easier to implement but uses $$O(N^2)$$ space.
- **Expand Around Center** reduces space usage to $$O(1)$$, though both it and the DP approach have $$O(N^2)$$ time complexity.
- **Manacher’s Algorithm** provides a more optimal runtime of $$O(N)$$, making it ideal for larger inputs, though it is more complex.

By understanding these approaches, you gain valuable insights into different algorithmic strategies for handling string-based problems. Happy coding and best of luck with your DSA interviews!

</details>
