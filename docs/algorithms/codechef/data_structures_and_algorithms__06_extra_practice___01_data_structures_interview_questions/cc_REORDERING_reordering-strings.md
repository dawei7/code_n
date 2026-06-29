# Reordering Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REORDERING |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [REORDERING](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/REORDERING) |

---

## Problem Statement

You are given a string $S$ of length $26$ consisting of each character from $(a-z)$ once. The importance of character $S_i \gt S_j$ , if $i \lt j$ .
You are given an array $A$ of strings of size $N$ . You need to reorder the array $A$ of strings so that the string with the higher priority occurs **before** the strings with the lower priority.
The priority of string is defined by the following rules :
A string $X$ has higher priority than string $Y$ if :
- The first position where string $X$ and $Y$ differs (let that position be $i$) , the importance of character $X_i \gt Y_i$
- String $X$ is a prefix of string $Y$.

---

## Input Format

- The first line contains an integer $T$ , representing $T$ test cases.

- First line of each test case contains the string $S$

- Second line of each test case contains an integer $N$ , representing the size of Array $A$.

- Next $i^{th}$ of the next $N$ lines of each test case contains the $i^{th}$ string of array $A$.

---

## Output Format

- For each test case, print $N$ lines containing a string in each line such that the string printed before the current string has greater priority than the string printed after.

---

## Constraints

- $1 \le T \le 10$

- $1 \le N \le 50000$

- $1 \le |A_i| \le 10$

- Strings of array $A$ contains only lower-case english letters.

- Sum of $|A_i|$ over all test cases doesn't exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
abcdefghijklmnopqrstuvwxyz
3
aaa
aa
abc
cdefghijklabmnopqrstuvwxyz
3
cdef
cjkl
abm
```

**Output**

```text
aa
aaa
abc
cdef
cjkl
abm
```

**Explanation**

In the first test case since string $S$ is in real alphabetical order. So, the real lexicographical order is printed.

In the second test case since **c** has higher importance than **a** and **d** has higher importance than **j** ,so the resulting order is $``cdef"$,$``cjkl"$,$``abm"$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson we will discuss how to sort a list of strings according to a custom “importance” order. In our problem, we are given a string
$$ S $$
of length 26 that defines the importance for each character of the English alphabet. In particular, if character
$$ S_i $$
occurs before
$$ S_j $$
in string $$ S $$ (i.e. if $$ i < j $$) then
$$ S_i $$
has higher importance than
$$ S_j $$
(in other words, a higher “rank”). We are then given an array of strings
$$ \mathcal{A} $$
and our task is to reorder this array so that the string with the highest priority appears first. The priority is defined as follows:

1. For two strings $$ X $$ and $$ Y $$, let $$ i $$ be the first index where they differ. Then, if
   $$ importance(X_i) > importance(Y_i) $$,
   string $$ X $$ has higher priority.
2. If there is no differing index (i.e. one string is a prefix of the other), the shorter string (the prefix) is considered to have higher priority.

Below, we discuss two common approaches.

---

### Approach 1: Custom Comparator Sorting

In this method we explicitly define a comparator function that iterates character by character over two strings. At the first index where the strings differ, we compare their importance values. If one string is a prefix of the other (i.e. no difference is found in the common length), the shorter string is given priority.

**Why It Works:**
Assume you are comparing two strings $$ X $$ and $$ Y $$. Let
$$ i $$
be the first index where
$$ X_i \neq Y_i $$. We then check:
$$ importance(X_i) > importance(Y_i). $$
If true, then $$ X $$ should come before $$ Y $$. Furthermore, if $$ X $$ is a prefix of $$ Y $$, then by definition $$ X $$ has higher priority.

**Time Complexity:**
Since we compare at most the length of the strings and sort using, say, a standard sorting algorithm, the running time is
$$ O(N \log N \cdot L), $$
where $$ N $$ is the number of strings and $$ L $$ is the maximum string length.

**C++ Code (Approach 1):**
Below is the C++ implementation using a custom comparator.

```cpp
#include
#include
#include
#include
using namespace std;

unordered_map importance;

bool compare(const string &a, const string &b) {
    int len = min(a.length(), b.length());
    for (int i = 0; i < len; i++) {
        if (a[i] != b[i]) {
            return importance[a[i]] > importance[b[i]];
        }
    }
    return a.length() < b.length(); // If prefix, the shorter string is higher priority.
}

void solve() {
    string S;
    cin >> S;
    for (int i = 0; i < 26; i++) {
        importance[S[i]] = 25 - i;
    }
    int N;
    cin >> N;
    vector A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end(), compare);
    for (const string &s : A) {
        cout << s << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

**Python Code (Approach 1):**
In Python, we can use the `cmp_to_key` method from the `functools` module to write a custom comparator.

```python
import sys
from functools import cmp_to_key

def solve():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    index = 1
    result = []

    for _ in range(t):
        S = input_data[index].strip()
        index += 1
        # Create the importance mapping: higher value means higher priority.
        priority = {c: 25 - i for i, c in enumerate(S)}

        n = int(input_data[index].strip())
        index += 1
        words = []
        for _ in range(n):
            words.append(input_data[index].strip())
            index += 1

        def cmp(x, y):
            # Compare character by character
            min_len = min(len(x), len(y))
            for i in range(min_len):
                if x[i] != y[i]:
                    # Higher importance should come first.
                    return -1 if priority[x[i]] > priority[y[i]] else 1
            # If one string is a prefix of the other, the shorter string comes first.
            return -1 if len(x) < len(y) else (1 if len(x) > len(y) else 0)

        words.sort(key=cmp_to_key(cmp))
        result.extend(words)
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    solve()
```

---

### Approach 2: Key Transformation (Tuple Key Sorting)

Instead of comparing strings character by character during sorting, we can precompute a key for each string. We transform each string into a fixed-length tuple where each element is the negative of the importance value of the corresponding character. The reason for taking the negative is that a higher importance value should make the key “smaller” (since the sort is in ascending order) so that it comes first.

**Key Transformation Details:**
- For a string $$ s $$, we compute:
  $$ key(s) = \Bigl( -importance(s_0),\,-importance(s_1), \dots, -importance(s_{|s|-1}) \Bigr) $$
- Since strings can have variable lengths, we pad the key to a fixed length $$ L $$ (the maximum string length among all inputs) with a value less than any possible digit. Here we use $$ -26 $$ because every letter gives a value in the range $$ [-25, 0] $$.

This transformation makes sure that if string $$ X $$ is a prefix of string $$ Y $$, then at the first index where $$ X $$ has been padded (and $$ Y $$ has an actual value), $$ X $$ gets a smaller tuple value and hence is ordered before $$ Y $$.

**Time Complexity:**
Precomputing keys takes
$$ O(N \cdot L) $$
time and then sorting takes
$$ O(N \log N) $$
with comparisons on tuples of length $$ L $$.

**C++ Code (Approach 2):**
Here we first determine the maximum length $$ L $$, then transform every string into its corresponding key (a vector of integers), and finally sort based on the key.

```cpp
#include
#include
#include
#include
#include
using namespace std;

struct StringWithKey {
    string s;
    vector key;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        string S;
        cin >> S;
        unordered_map priority;
        for (int i = 0; i < 26; i++) {
            priority[S[i]] = 25 - i;
        }
        int N;
        cin >> N;
        vector arr(N);
        int maxLength = 0;
        for (int i = 0; i < N; i++) {
            cin >> arr[i].s;
            if(arr[i].s.size() > maxLength)
                maxLength = arr[i].s.size();
        }
        // Transform each string into a key.
        for (int i = 0; i < N; i++) {
            arr[i].key.resize(maxLength);
            int len = arr[i].s.size();
            for (int j = 0; j < len; j++) {
                // Use negative of priority to have higher importance be "smaller"
                arr[i].key[j] = -priority[arr[i].s[j]];
            }
            // Pad with -26 (which is less than -25) to ensure prefix ordering.
            for (int j = len; j < maxLength; j++) {
                arr[i].key[j] = -26;
            }
        }
        // Sort based on the transformed key.
        sort(arr.begin(), arr.end(), [](const StringWithKey &a, const StringWithKey &b) {
            return a.key < b.key;
        });
        for (auto &item : arr) {
            cout << item.s << "\n";
        }
    }
    return 0;
}
```

**Python Code (Approach 2):**
In Python the key transformation is particularly concise using tuple comprehensions. We compute the key for each string and sort based on that.

```python
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    line = 1
    res = []

    for _ in range(t):
        S = input_data[line].strip()
        line += 1
        # Map each character to its priority (higher integer means higher importance)
        priority = {c: 25 - i for i, c in enumerate(S)}

        n = int(input_data[line].strip())
        line += 1
        words = []
        for _ in range(n):
            words.append(input_data[line].strip())
            line += 1
        # Determine the maximum length of the strings.
        L = max(len(word) for word in words)

        # Transform each string into a key tuple.
        def transform(word):
            # Negative priority values ensures that a higher original priority gives a smaller key value.
            key = tuple(-priority[c] for c in word)
            # Pad with -26 (which is less than any -priority value) so that prefixes come first.
            return key + (-26,) * (L - len(word))

        words.sort(key=transform)
        res.extend(words)
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    solve()
```

---

### Summary

We explored two effective methods:

1. **Custom Comparator Sorting:** Here we define a function that directly compares two strings based on the custom importance mapping. This method is very natural and directly follows the problem statement.

2. **Key Transformation Sorting:** In this approach we precompute a key for each string by converting it into a fixed-length tuple after mapping each character. Padding ensures that the prefix condition is met. This approach leverages the built-in sorting mechanisms with tuple comparison.

Both methods run efficiently given the constraints and help solidify the concepts of custom sorting, handling prefixes, and using key transformations. Understanding these techniques will strengthen your ability to handle string sorting problems in data structures and algorithms interviews.

</details>
