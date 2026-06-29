# Backtracking - Palindrome Partitioning

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP43 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Backtracking |
| Official Link | [PREP43](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_16/problems/PREP43) |

---

## Problem Statement

You are given a string $S$ consisting of lowercase english characters. Partition $S$ such that every substring of the partition is a palindrome. Find all possible **unique palindrome** partitioning of $S$.

Note:
- A substring of a string is obtained by deleting some (possibly zero) characters from the beginning and some (possibly zero) characters from the end.
- A palindrome is a string that reads the same backward as forward.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case consists of a string $S$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique palindrome partitioning:
- The first line contains a single integer $M$.
- The next $M$ lines contains space-separated substring of $S$.

Note:
- The partitions must be printed in lexicographically increasing order.
We say that partition $X$ is lexicographically smaller than $Y$ if either $X$ is a prefix of $Y$ or there exists an index $i$ such that for all $j\lt i$, $X_j = Y_j$ and $X_i\lt Y_i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq |S| \leq 15$

---

## Examples

**Example 1**

**Input**

```text
3
aab
a
aaa
```

**Output**

```text
2
a a b 
aa b 
1
a 
4
a a a 
a aa 
aa a 
aaa
```

**Explanation**

**Test case $1$:** All possible **unique palindrome** partitioning of $S$ will be $[a, a, b]$, $[aa, b]$.

**Test case $2$:** All possible **unique palindrome** partitioning of $S$ will be $[a]$.

**Test case $3$:** All possible **unique palindrome** partitioning of $S$ will be $[a, a, a, a]$, $[a, aa]$, $[aa, a]$, $[aaa]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Unique Palindrome Partitioning

In this lesson, we explore different approaches to generate all **unique palindrome partitionings** of a given string. A partition is valid if every substring in it is a palindrome. We will discuss three distinct methods:

---

## Approach 1: Backtracking with On-the-Fly Palindrome Check

### Overview
This approach uses recursion (backtracking) to partition the string. For every possible substring $S[i \ldots j]$ starting at index $i$, we check if it is a palindrome by comparing characters from the ends to the center. If it is, we include it in the current partition and recursively process the remainder of the string. When the entire string is partitioned (i.e. $i = |S|$), we add the current partition to the list of solutions.

### Key Points
- **Recursion:** We explore all possible ways to break the string.
- **Palindrome Check:** For each substring, we check if it reads the same forwards and backwards.
- **Lexicographical Order:** Once we generate all partitions, we sort them according to lexicographical order.
- **Deduplication:** We remove duplicate partitions (if any) to ensure uniqueness.

### C++ Code

```cpp
#include
#include
#include
#include
using namespace std;

bool isPalindrome(const string &s, int start, int end) {
    while (start < end) {
        if (s[start] != s[end])
            return false;
        start++;
        end--;
    }
    return true;
}

void backtrack(string &s, int start, vector ¤t, vector> &result) {
    if (start == s.size()) {
        result.push_back(current);
        return;
    }
    for (int end = start; end < s.size(); end++) {
        if (isPalindrome(s, start, end)) {
            current.push_back(s.substr(start, end - start + 1));
            backtrack(s, end + 1, current, result);
            current.pop_back();
        }
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        vector> partitions;
        vector current;
        backtrack(S, 0, current, partitions);
        sort(partitions.begin(), partitions.end());
        partitions.erase(unique(partitions.begin(), partitions.end()), partitions.end());
        cout << partitions.size() << endl;
        for (const auto &partition : partitions) {
            for (const auto &substr : partition) {
                cout << substr << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Code

```python
def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start, end = start + 1, end - 1
    return True

def backtrack(s, start, current, result):
    if start == len(s):
        result.append(current.copy())
        return
    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            current.append(s[start:end+1])
            backtrack(s, end+1, current, result)
            current.pop()

def partition(s):
    result = []
    backtrack(s, 0, [], result)
    return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input().strip()
        partitions = partition(S)
        # Convert each partition to tuple for deduplication and then sort lexicographically
        partitions = sorted(set(tuple(p) for p in partitions))
        print(len(partitions))
        for part in partitions:
            print(" ".join(part))
```

---

## Approach 2: Backtracking with DP Precomputation

### Overview
In this approach, we optimize the repeated palindrome checks by precomputing a two-dimensional DP table $dp[i][j]$ that tells us whether the substring $S[i \ldots j]$ is a palindrome. We first calculate the DP table with a time complexity of $O(n^2)$ and then use it in a similar backtracking strategy.

### Key Points
- **DP Table Precomputation:** Compute $dp[i][j] = true$ if $S[i \ldots j]$ is a palindrome.
- **Faster Checks:** Once precomputed, verifying if a substring is a palindrome is constant time.
- **Backtracking:** Use the precomputed table during recursion to reduce overhead.

### C++ Code

```cpp
#include
#include
#include
#include
using namespace std;

void computePalindromeDP(const string &s, vector> &dp) {
    int n = s.size();
    dp.assign(n, vector(n, false));
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            if (s[i] == s[j])
                dp[i][j] = (j - i == 1) ? true : dp[i + 1][j - 1];
        }
    }
}

void backtrackDP(const string &s, int start, vector ¤t, vector> &result, vector> &dp) {
    if (start == s.size()) {
        result.push_back(current);
        return;
    }
    for (int end = start; end < s.size(); end++) {
        if (dp[start][end]) {
            current.push_back(s.substr(start, end - start + 1));
            backtrackDP(s, end + 1, current, result, dp);
            current.pop_back();
        }
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        vector> dp;
        computePalindromeDP(S, dp);
        vector> partitions;
        vector current;
        backtrackDP(S, 0, current, partitions, dp);
        sort(partitions.begin(), partitions.end());
        partitions.erase(unique(partitions.begin(), partitions.end()), partitions.end());
        cout << partitions.size() << endl;
        for (const auto &partition : partitions) {
            for (const auto &substr : partition) {
                cout << substr << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Code

```python
def compute_palindrome_dp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = True if j - i == 1 else dp[i + 1][j - 1]
    return dp

def backtrack_dp(s, start, current, result, dp):
    if start == len(s):
        result.append(current.copy())
        return
    for end in range(start, len(s)):
        if dp[start][end]:
            current.append(s[start:end+1])
            backtrack_dp(s, end+1, current, result, dp)
            current.pop()

def partition_dp(s):
    dp = compute_palindrome_dp(s)
    result = []
    backtrack_dp(s, 0, [], result, dp)
    return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input().strip()
        partitions = partition_dp(S)
        partitions = sorted(set(tuple(p) for p in partitions))
        print(len(partitions))
        for part in partitions:
            print(" ".join(part))
```

---

## Approach 3: Iterative Bitmask Approach

### Overview
This approach uses an iterative method that leverages bitmasking. For a string of length $n$, there are $2^{n-1}$ ways to partition it (each of the $n-1$ gaps can either be a cut or not). For each bitmask, we form the corresponding partition and then check if every substring in that partition is a palindrome. If so, we add it to our result set.

### Key Points
- **Bitmasking:** Each bit represents a potential cut position.
- **Iterative Generation:** Loop through all $2^{n-1}$ possible partitions.
- **Validation:** For every generated partition, verify that each substring is a palindrome.
- **Uniqueness and Sorting:** Use a set to avoid duplicates, then sort for lexicographical order.

### C++ Code

```cpp
#include
#include
#include
#include
#include
using namespace std;

bool checkPartition(const string &s, const vector &cuts) {
    int start = 0;
    for (int cut : cuts) {
        string sub = s.substr(start, cut - start + 1);
        string rev = sub;
        reverse(rev.begin(), rev.end());
        if (sub != rev)
            return false;
        start = cut + 1;
    }
    string sub = s.substr(start);
    string rev = sub;
    reverse(rev.begin(), rev.end());
    return sub == rev;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        int n = S.size();
        set> partitions_set;
        int total = 1 << (n - 1);
        for (int mask = 0; mask < total; mask++) {
            vector partition;
            int start = 0;
            bool valid = true;
            for (int i = 0; i < n - 1; i++) {
                if (mask & (1 << i)) {
                    string sub = S.substr(start, i - start + 1);
                    string rev = sub;
                    reverse(rev.begin(), rev.end());
                    if (sub != rev) {
                        valid = false;
                        break;
                    }
                    partition.push_back(sub);
                    start = i + 1;
                }
            }
            if (!valid)
                continue;
            string sub = S.substr(start);
            string rev = sub;
            reverse(rev.begin(), rev.end());
            if (sub != rev)
                continue;
            partition.push_back(sub);
            partitions_set.insert(partition);
        }
        vector> partitions(partitions_set.begin(), partitions_set.end());
        sort(partitions.begin(), partitions.end());
        cout << partitions.size() << endl;
        for (const auto &part : partitions) {
            for (const auto &str : part) {
                cout << str << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
```

### Python Code

```python
def is_palindrome(sub):
    return sub == sub[::-1]

def partition_bitmask(s):
    n = len(s)
    result = set()
    total = 1 << (n - 1)
    for mask in range(total):
        partition = []
        start = 0
        valid = True
        for i in range(n - 1):
            if mask & (1 << i):
                substring = s[start:i+1]
                if not is_palindrome(substring):
                    valid = False
                    break
                partition.append(substring)
                start = i + 1
        if not valid:
            continue
        substring = s[start:]
        if not is_palindrome(substring):
            continue
        partition.append(substring)
        result.add(tuple(partition))
    return sorted(result)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input().strip()
        partitions = partition_bitmask(S)
        print(len(partitions))
        for part in partitions:
            print(" ".join(part))
```

---

## Conclusion

Each of these approaches has its benefits:

- **Approach 1:** Simple to implement; checks palindromes on the fly.
- **Approach 2:** Optimizes repeated palindrome checks using dynamic programming.
- **Approach 3:** Provides an alternative iterative solution using bitmasking to generate all possible splits.

Even though the string length is small ($|S| \leq 15$), understanding these methods provides valuable insight into recursive backtracking, dynamic programming, and bitmasking techniques. Experiment with these approaches to gain a deeper understanding of handling recursive partitioning problems.

</details>
