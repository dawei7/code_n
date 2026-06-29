# Divide The String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DTS |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Two pointers |
| Official Link | [DTS](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_11/problems/DTS) |

---

## Problem Statement

You are given an integer $N$ and a string $S$, whose length is $N$. Your task is to split the string $S$ into $k$ consecutive substrings of the same length, so that the splitting is magical, while maximizing the $k$.

We call a splitting magical if all of the substrings are anagrams of each other. We say that two string $A$ and $B$ are anagrams of each other if we can rearrange the characters of the string $A$ so that it becomes equal to string $B$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, an integer $N$ and a string $S$.

---

## Output Format

For each testcase, output in a single line maximal possible value of $k$. It can be showed that the answer always exists.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
3
6 abbaab
4 aaaa
6 abcdef
```

**Output**

```text
3
4
1
```

**Explanation**

In the first test case, it is optimal to split the string into $ab$, $ba$ and $ab$ since they are all anagrams of (for example) $ab$.

In the second test case, it is optimal to split the string into $a$, $a$, $a$, $a$.

In the third test case, the string cannot be split into more than one component, which is the string itself $abcdef$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 abbaab
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 aaaa
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
6 abcdef
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore a problem where we are given an integer $N$ and a string $S$ of length $N$. Our goal is to split $S$ into $k$ consecutive substrings (each of length $N/k$) such that every substring is an anagram of the others—and among all possibilities, we must maximize $k$. In simpler terms, every substring must have the same multiset of characters.

A key observation to solve this problem is that if we denote the frequency of a letter by $f$, then for the split to be magical the frequency $f$ must be evenly distributed among the $k$ substrings. That is, $k$ must divide $f$. Since the string is composed of several characters, for every letter with frequency $f_i$, we must have:
$$
f_i \equiv 0 \pmod{k}
$$
A very powerful and elegant conclusion from this observation is that the maximum possible $k$ that satisfies the condition for all characters is simply the greatest common divisor (GCD) of all the nonzero frequencies. This forms the basis of our first approach.

Below, we describe three approaches to tackle the problem:

---

### **Approach 1: GCD of Frequencies**

**Idea:**
Count the frequency of each character in the string $S$. Since a valid split into $k$ substrings requires that each letter’s frequency is divisible by $k$, the maximum possible $k$ is the greatest common divisor (GCD) of all the character frequencies.

**Explanation:**
- Compute the frequency of each of the 26 lowercase English letters.
- Initialize $g = 0$. For every nonzero frequency $f$, update $g = \text{gcd}(g, f)$.
- The final value of $g$ is our answer.

**Time Complexity:**
This method runs in $O(N + 26)$ per test case, which is efficient given the problem constraints.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

int gcd(int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        string S;
        cin >> N >> S;

        vector freq(26, 0);
        for (char c : S) {
            freq[c - 'a']++;
        }

        int g = 0;
        for (int f : freq) {
            if (f > 0) {
                g = gcd(g, f);
            }
        }

        cout << g << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
import sys
import math

input_data = sys.stdin.read().strip().split()
if not input_data:
    exit()
T = int(input_data[0])
index = 1
results = []

for _ in range(T):
    N = int(input_data[index]); index += 1
    S = input_data[index]; index += 1

    freq = [0] * 26
    for c in S:
        freq[ord(c) - ord('a')] += 1

    g = 0
    for f in freq:
        if f > 0:
            g = math.gcd(g, f)

    results.append(str(g))

sys.stdout.write("\n".join(results))
```

---

### **Approach 2: Divisor Checking (Candidate Verification)**

**Idea:**
Instead of computing the GCD directly, we can iterate over all possible values of $k$ that divide $N$ (since $k$ must split the string evenly) and check if $k$ divides every character frequency.

**Explanation:**
- Loop over candidate values of $k$ from $N$ down to $1$.
- For each candidate, first check that $k$ divides $N$.
- Then, for every letter, verify that its frequency is divisible by $k$.
- The first (largest) candidate that meets these criteria is the answer.

**Time Complexity:**
This approach may check up to $N$ values in the worst case but benefits from the fact that $26$ checks per candidate are inexpensive. Even so, it is less efficient than the GCD approach but still acceptable under the given constraints.

**C++ Implementation:**
```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int N;
        string S;
        cin >> N >> S;

        vector freq(26, 0);
        for (char c : S) {
            freq[c - 'a']++;
        }

        int ans = 1;
        // Check candidates from N downwards
        for (int k = N; k >= 1; k--){
            if (N % k != 0)
                continue;
            bool valid = true;
            for (int f : freq) {
                if (f % k != 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                ans = k;
                break;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
import sys

input_data = sys.stdin.read().strip().split()
if not input_data:
    exit()
T = int(input_data[0])
index = 1
results = []

for _ in range(T):
    N = int(input_data[index]); index += 1
    S = input_data[index]; index += 1

    freq = [0] * 26
    for c in S:
        freq[ord(c) - ord('a')] += 1

    ans = 1
    for k in range(N, 0, -1):
        if N % k != 0:
            continue
        valid = True
        for f in freq:
            if f % k != 0:
                valid = False
                break
        if valid:
            ans = k
            break

    results.append(str(ans))

sys.stdout.write("\n".join(results))
```

---

### **Approach 3: Naïve Splitting and Anagram Checking**

**Idea:**
For each candidate $k$ (where $k$ divides $N$), split the string into $k$ equal parts and then check if all parts are anagrams of each other.

**Explanation:**
- Determine the candidate $k$ by ensuring $N \bmod k = 0$. Compute the length of each substring as $L = N/k$.
- Split $S$ into $k$ parts.
- For each substring, compute the frequency count (or use a counter).
- Compare the frequency counts of all substrings. If they are identical, the split is magical.
- Return the first (largest) valid $k$ found.

**Time Complexity:**
This approach involves extra overhead due to splitting and frequency computation on each substring, making it less efficient than the GCD method. However, it demonstrates a more “brute-force” check of the anagram property.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

bool areAnagrams(const vector& count1, const vector& count2) {
    for (int i = 0; i < 26; i++) {
        if (count1[i] != count2[i])
            return false;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int N;
        string S;
        cin >> N >> S;

        int ans = 1;
        // Try candidates from N downwards
        for (int k = N; k >= 1; k--){
            if (N % k != 0)
                continue;
            int len = N / k;
            vector> parts(k, vector(26, 0));
            bool valid = true;
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < len; j++) {
                    parts[i][S[i * len + j] - 'a']++;
                }
            }
            // Compare all parts with the first part
            for (int i = 1; i < k; i++) {
                if (!areAnagrams(parts[0], parts[i])) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                ans = k;
                break;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
import sys
from collections import Counter

input_data = sys.stdin.read().strip().split()
if not input_data:
    exit()
T = int(input_data[0])
index = 1
results = []

for _ in range(T):
    N = int(input_data[index]); index += 1
    S = input_data[index]; index += 1
    ans = 1
    # Test candidates from N downwards
    for k in range(N, 0, -1):
        if N % k != 0:
            continue
        length = N // k
        parts = [Counter(S[i * length:(i + 1) * length]) for i in range(k)]
        valid = True
        base = parts[0]
        for part in parts[1:]:
            if part != base:
                valid = False
                break
        if valid:
            ans = k
            break
    results.append(str(ans))

sys.stdout.write("\n".join(results))
```

---

### **Conclusion**

The most optimal solution leverages the GCD of the frequency counts to directly obtain the maximum $k$. While the brute-force and direct-splitting methods (Approaches 2 and 3) are conceptually simple and help in understanding the problem, **Approach 1 (GCD)** is both elegant and efficient.

By understanding these approaches, you can gain deeper insights into frequency distribution problems and methods to check divisibility and properties of numbers—key concepts in Data Structures and Algorithms interviews.

</details>
