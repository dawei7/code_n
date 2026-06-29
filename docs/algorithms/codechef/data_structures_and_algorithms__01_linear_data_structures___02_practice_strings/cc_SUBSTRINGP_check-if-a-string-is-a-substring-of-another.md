# Check if a string is a substring of another

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSTRINGP |
| Difficulty Rating | 1000 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [SUBSTRINGP](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/SUBSTRINGP) |

---

## Problem Statement

Given two strings, `S1` and `S2`, your task is to determine whether `S2` is a substring of `S1`. If `S2` is a substring of `S1`, print "YES". Otherwise, print "NO".

A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "aabcda", but "ac" is not a contiguous sequence in "aabcda".

---

## Input Format

- The first line contains a single integer `T`, the number of test cases.
- Each test case consists of two lines:
    - The first line contains the string `S1`.
    - The second line contains the string `S2`.

---

## Output Format

For each test case, print a single line containing either "YES" or "NO", depending on whether `S2` is a substring of `S1`.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S1|, |S2| \leq 1000$
- `S1` and `S2` contain only lowercase English letters.

---

## Examples

**Example 1**

**Input**

```text
4
hello
ell
codechef
chef
programming
debug
abcd
efgh
```

**Output**

```text
YES
YES
NO
NO
```

**Explanation**

- In the first test case, "ell" is a substring of "hello".
- In the second test case, "chef" is a substring of "codechef".
- In the third test case, "debug" is not a substring of "programming".
- In the fourth test case, "efgh" is not a substring of "abcd".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
hello
ell
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
codechef
chef
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
programming
debug
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
abcd
efgh
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites**:- None

**Problem** :- Given two strings, S1 and S2, your task is to determine whether S2 is a substring of S1.

**Explanation** :-

Iterate through each character of the first string, S1, and check whether the second string, S2, is a substring starting from that position.

Here’s a breakdown of the core logic:

The code loops through each character of S1.

At each position in S1, it checks if the substring of S1 starting from that position matches S2.

If the substring of S1 matches S2, it means that S2 is a substring of S1. In this case, it prints “YES” and exits the loop.

If no match is found after checking all possible starting positions, it means S2 is not a substring of S1. In this case, it prints “NO”.

**Solution :-**

**C++ Solution : -**

``#include <iostream>
#include <string>
using namespace std;

bool isSubstring(const string& S1, const string& S2) {
    int lenS1 = S1.length(), lenS2 = S2.length();
    for (int i = 0; i <= lenS1 - lenS2; i++) {
        bool found = true;
        for (int j = 0; j < lenS2; j++) {
            if (S1[i + j] != S2[j]) {
                found = false;
                break;
            }
        }
        if (found) return true;
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S1, S2;
        cin >> S1 >> S2;
        cout << (isSubstring(S1, S2) ? "YES" : "NO") << endl;
    }
    return 0;
}

``

</details>
