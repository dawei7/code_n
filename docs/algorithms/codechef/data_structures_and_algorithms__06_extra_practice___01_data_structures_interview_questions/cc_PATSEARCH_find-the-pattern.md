# Find the Pattern

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PATSEARCH |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [PATSEARCH](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/PATSEARCH) |

---

## Problem Statement

You are given two strings $S$ and $P$ both consisting of lowercase letters of the English alphabet. Find if the string $P$ occurs as a substring in the string $S$.

A substring is a contiguous sequence of characters within a string.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single string $S$.

- The second line of each test case contains a single string $P$.

---

## Output Format

- For each test case, print a single line containing one integer. That integer should be $1$ if the string $P$ occurs as a substring in the string $S$ and $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |P| \leq |S| \leq 2 \cdot 10^5$
- the characters in $S$ and $P$ are lowercase letters of the English alphabet
- the sum of $|S|$ over all test cases does not exceed $4 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
abcabdabe
abc
xxxaaaxax
xaaax
befdsedfg
dedf
```

**Output**

```text
1
1
0
```

**Explanation**

**Example case 1:** The first three characters in $S$ form a substring that is equal to $P$.

**Example case 2:** The string $P$ occurs as a substring in $S$ from position $3$ to position $7$.

**Example case 3:** The string $P$ does not occur as a substring in $S$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcabdabe
abc
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
xxxaaaxax
xaaax
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
befdsedfg
dedf
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Substring Search Problem

In this lesson, we address one of the most fundamental problems in string processing: determining whether the pattern string $\{P\}$ occurs as a contiguous substring in the main string $\{S\}$.

A **substring** is a contiguous sequence of characters within a string. Our objective is to check if $\{P\}$ exists in $\{S\}$. In doing so, we will discuss efficient approaches that utilize advanced algorithms to solve this problem, namely the **Knuth-Morris-Pratt (KMP) Algorithm** and the **Rabin-Karp Algorithm with Rolling Hash**.

---

## Approach 1: Knuth-Morris-Pratt (KMP) Algorithm

### Explanation
The KMP algorithm is an efficient solution that preprocesses the pattern $\{P\}$ to generate an **LPS (Longest Prefix Suffix)** array. The LPS array allows us to avoid redundant comparisons by "remembering" where the next valid match could begin if a mismatch occurs. This results in an overall time complexity of
$$ O(n + m), $$
where $n=|S|$ and $m=|P|$.

### Code Implementation

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

vector computeLPS(const string &pattern) {
    int m = pattern.size();
    vector lps(m, 0);
    int len = 0;
    int i = 1;
    while(i < m){
        if(pattern[i] == pattern[len]){
            len++;
            lps[i] = len;
            i++;
        } else {
            if(len != 0){
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

bool kmpSearch(const string &text, const string &pattern) {
    int n = text.size(), m = pattern.size();
    vector lps = computeLPS(pattern);
    int i = 0, j = 0;
    while(i < n){
        if(text[i] == pattern[j]){
            i++;
            j++;
        }
        if(j == m){
            return true;
        }
        else if(i < n && text[i] != pattern[j]){
            if(j != 0){
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while(T--){
        string S, P;
        cin >> S >> P;
        cout << (kmpSearch(S, P) ? 1 : 0) << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

import sys
def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        s = data[index]
        index += 1
        p = data[index]
        index += 1
        results.append("1" if kmp_search(s, p) else "0")
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

---

## Approach 2: Rabin-Karp Algorithm with Rolling Hash

### Explanation
Rabin-Karp is a probabilistic algorithm that leverages a **rolling hash** technique. It computes a hash value for the pattern $\{P\}$ and then for every substring in $\{S\}$ of the same length. If the hash values match, the algorithm performs a direct comparison to confirm the match, thereby mitigating false positives due to hash collisions.

The hash function used is:
$$ h = \left(\sum_{i=0}^{m-1} \text{value}(P[i]) \times d^{(m-i-1)}\right) \mod q, $$
where $d$ is the base (e.g., 256 for ASCII characters) and $q$ is a prime number used as the modulus. While the average-case performance is
$$ O(n + m), $$
in the worst-case it can degrade to
$$ O(n \cdot m). $$

### Code Implementation

#### C++ Code:
```cpp
#include
#include
using namespace std;

typedef long long ll;
const ll d = 256;
const ll q = 101;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while(T--){
        string S, P;
        cin >> S >> P;
        int n = S.size(), m = P.size();
        if(m > n){
            cout << 0 << "\n";
            continue;
        }
        ll hpattern = 0, htext = 0, h = 1;
        for (int i = 0; i < m - 1; i++){
            h = (h * d) % q;
        }
        for (int i = 0; i < m; i++){
            hpattern = (d * hpattern + P[i]) % q;
            htext = (d * htext + S[i]) % q;
        }
        bool found = false;
        for (int i = 0; i <= n - m; i++){
            if(hpattern == htext){
                int j;
                for(j = 0; j < m; j++){
                    if(S[i+j] != P[j])
                        break;
                }
                if(j == m){
                    found = true;
                    break;
                }
            }
            if(i < n - m){
                htext = (d * (htext - S[i] * h) + S[i + m]) % q;
                if(htext < 0)
                    htext += q;
            }
        }
        cout << (found ? 1 : 0) << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return False
    d = 256
    q = 101
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    hpattern = 0
    htext = 0
    for i in range(m):
        hpattern = (d * hpattern + ord(pattern[i])) % q
        htext = (d * htext + ord(text[i])) % q
    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                return True
        if i < n - m:
            htext = (d * (htext - ord(text[i]) * h) + ord(text[i + m])) % q
            if htext < 0:
                htext += q
    return False

import sys
def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        s = data[index]
        index += 1
        p = data[index]
        index += 1
        results.append("1" if rabin_karp(s, p) else "0")
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

---

## Conclusion
The two approaches to solving the substring search problem offer their own trade-offs:
- **KMP Algorithm:** Provides linear-time performance and is efficient for worst-case scenarios.
- **Rabin-Karp Algorithm:** Utilizes a rolling hash for an average-case linear-time solution, though it has a potential worst-case drawback.

Choose the approach that best meets your needs and the input constraints at hand.

</details>
