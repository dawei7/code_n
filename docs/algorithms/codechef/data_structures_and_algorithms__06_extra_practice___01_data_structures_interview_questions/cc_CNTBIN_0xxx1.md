# 0xxx1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTBIN |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [CNTBIN](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/CNTBIN) |

---

## Problem Statement

You are given a binary string $S$ of size $N$. A string is called **good** if
- The first character of the string is $0$.
- The last character of the string is $1$.

Count the number of sub-strings in $S$ which are **good**. Since the answer might be a large number, print it modulo $10^{9} + 7$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains a single string $S$.

---

## Output Format

For each testcase, print the count of good sub-strings modulo $10^{9} + 7$.

---

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 10^5$
- Each character of string $S$ is either $0$ or $1$.

---

## Examples

**Example 1**

**Input**

```text
2
5
10010
6
010010
```

**Output**

```text
2
4
```

**Explanation**

**Test case 1**:
Following substrings are good :
- 10**01**0
- 1**001**0

**Test case 2**:
Following substrings are good :
- **01**0010
- 010**01**0
- 01**001**0
- **01001**0

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
10010
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6
010010
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Counting Good Substrings

In this lesson, we explore a problem that asks us to count the number of **good substrings** in a given binary string $S$. A substring is considered good if its first character is $0$ and its last character is $1$. Our goal is to compute the number of such substrings efficiently modulo $10^9+7$.

Recall that a substring is defined by its start index $i$ and end index $j$ (with $i < j$). Therefore, for a substring to be good:
- The character at index $i$ must be $0$.
- The character at index $j$ must be $1$.

This observation leads to the insight that if we know, for a given index $i$ where $S[i] = 0$, how many $1$’s lie at positions greater than $i$, we can accumulate the answer by summing up these counts. In mathematical terms:
$$
\text{count} = \sum_{i : S[i] = 0} \text{ones\_after}(i)
$$
where $\text{ones\_after}(i)$ is the number of $1$’s in $S[i+1\,..\,N-1]$.

Below, we discuss two correct approaches to solve this problem.

---

## Approach 2: Two-Pass Method Using Suffix Count

### Idea:
- Construct a suffix array `suffix_ones` where `suffix_ones[i]` holds the number of $1$’s from index $i$ to the end of the string.
- For each index $i$ with $S[i] = 0$, the number of valid substrings starting at $i$ is exactly `suffix_ones[i+1]`.

### Steps:
1. Initialize `suffix_ones[n-1]` based on the last character:
   $$
   \text{suffix\_ones}[n-1] = \begin{cases} 1 & \text{if } S[n-1]=='1', \\ 0 & \text{otherwise} \end{cases}
   $$
2. For each index from $n-2$ downto $0$, update:
   $$
   \text{suffix\_ones}[i] = \text{suffix\_ones}[i+1] + \begin{cases} 1 & \text{if } S[i]=='1', \\ 0 & \text{otherwise} \end{cases}
   $$
3. Loop from index $0$ to $n-2$ and for each position where $S[i]$ is $0$, add `suffix_ones[i+1]` to the answer.

### Complexity:
- **Time Complexity:** $O(N)$.

### Code Implementation:

#### C++:
```cpp
#include
#include
#include
using namespace std;
const int MOD = 1e9 + 7;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        string s;
        cin >> n >> s;

        vector suffix_ones(n, 0);
        suffix_ones[n-1] = (s[n-1] == '1');

        for (int i = n - 2; i >= 0; i--) {
            suffix_ones[i] = suffix_ones[i + 1] + (s[i] == '1');
        }

        long long ans = 0;
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == '0') {
                ans = (ans + suffix_ones[i + 1]) % MOD;
            }
        }

        cout << ans << "\n";
    }
    return 0;
}
```

#### Python:
```python
MOD = 10**9 + 7
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    suffix_ones = [0] * n
    suffix_ones[n-1] = 1 if s[n-1] == '1' else 0

    for i in range(n - 2, -1, -1):
        suffix_ones[i] = suffix_ones[i + 1] + (1 if s[i] == '1' else 0)

    ans = 0
    for i in range(n - 1):
        if s[i] == '0':
            ans = (ans + suffix_ones[i + 1]) % MOD

    print(ans)
```

---

## Approach 3: Optimized Single-Pass Method

### Idea:
- Traverse the string from right to left.
- Use a counter `ones_count` to track the number of $1$’s encountered.
- When a $0$ is found, add the current value of `ones_count` to the answer.

### Rationale:
This approach works because every $0$ can form a valid substring with all the $1$’s encountered so far (which lie to its right). This method reduces extra space usage by avoiding an additional array.

### Complexity:
- **Time Complexity:** $O(N)$.
- **Space Complexity:** $O(1)$ (aside from input storage).

### Code Implementation:

#### C++:
```cpp
#include
#include
using namespace std;
const int MOD = 1e9 + 7;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        string s;
        cin >> n >> s;
        long long ones_count = 0, ans = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '1') {
                ones_count++;
            } else if (s[i] == '0') {
                ans = (ans + ones_count) % MOD;
            }
        }

        cout << ans << "\n";
    }
    return 0;
}
```

#### Python:
```python
MOD = 10**9 + 7
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ones_count = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            ones_count += 1
        elif s[i] == '0':
            ans = (ans + ones_count) % MOD

    print(ans)
```

---

## Conclusion

Both the **two-pass suffix array method** and the **optimized single-pass method** leverage the observation that each $0$ can pair with every subsequent $1$ to form a good substring. While the two-pass method uses extra space to store suffix counts, the single-pass method achieves the same result using constant space and is thus more space-efficient.

Understanding these approaches deepens our grasp of algorithmic optimization, enabling us to choose the most efficient strategy based on the problem constraints.

</details>
