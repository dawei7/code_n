# Minimum Similar Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINSIM |
| Difficulty Rating | 1500 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [MINSIM](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/MINSIM) |

---

## Problem Statement

Given two strings $s$,$t$, Alice calls a string $t$ similar to string $s$ if all the characters(including duplicates) present in the string $t$ are present in string $s$.

Find the shortest substring of the string $s$ which is similar to $t$ to make Alice happy.
If there is no such substring, print “IMPOSSIBLE” without the quotes.

String $a$ is a substring of string $b$ if it is possible to choose several consecutive letters in $b$ in such a way that they form $a$.

---

## Input Format

- The first line will contain 2 integers $|S|,|T|$
- The second line contains the string $S$.
- The third line contains the string $T$.

---

## Output Format

Output the length of the shortest similar substring and the substring as well on different lines. If multiple answers are possible then output the earliest substring of the string $s$. If there is no such substring, print “IMPOSSIBLE” without the quotes.

---

## Constraints

- $1 \leq |S|,|T| \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
8 2
aabcbcde
ad
```

**Output**

```text
6
abcbcd
```

**Explanation**

Substrings {abcbcde,abcbcd} follow the similar substring condition out of which abcbcd is the shortest.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Finding the Shortest Similar Substring

In this lesson, we focus on an important problem frequently seen in DSA interviews: finding the shortest substring of a given string $s$ that is similar to a string $t$. Two strings are considered similar if the substring contains all the characters (with their respective counts) present in $t$. This is a variation of the classic "Minimum Window Substring" problem.

> **Note:** The brute force approach has been removed from this editorial due to inaccuracies in its solution codes. We now concentrate on the efficient sliding window techniques that are both correct and practical for larger inputs.

We will explore the following approaches:

- **Approach 2: Sliding Window with Hashmap**
- **Approach 3: Optimized Sliding Window Using Arrays**

---

## Approach 2: Sliding Window with Hashmap

**Concept:**
This approach uses a dynamic sliding window with two pointers (commonly called the left and right pointers) to maintain a window in which the current substring of $s$ contains all required characters of $t$.

**Steps:**
1. Create a hashmap for the character counts in $t$ (`freqT`) and another for the counts in the current window (`window`).
2. Expand the window by moving the right pointer until it satisfies the criteria (i.e. the window becomes “similar” to $t$).
3. Once the window is valid, slide the left pointer to reduce the window size as much as possible while preserving its validity.
4. Update the answer whenever a smaller valid window is found.

**Time Complexity:**
This method runs in $O(n)$ time, making it ideal for large inputs.

### C++ Implementation (Approach 2)
```cpp
#include
#include
#include
#include
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> s >> t;
    unordered_map freqT, window;
    for (char c : t) {
        freqT[c]++;
    }
    int required = freqT.size();
    int formed = 0, left = 0, right = 0;
    int bestLength = INT_MAX, bestLeft = 0;
    while (right < n) {
        char c = s[right];
        window[c]++;
        if (freqT.count(c) && window[c] == freqT[c])
            formed++;
        while (left <= right && formed == required) {
            if (right - left + 1 < bestLength) {
                bestLength = right - left + 1;
                bestLeft = left;
            }
            char d = s[left];
            window[d]--;
            if (freqT.count(d) && window[d] < freqT[d])
                formed--;
            left++;
        }
        right++;
    }
    if (bestLength == INT_MAX)
        cout << "IMPOSSIBLE" << endl;
    else {
        cout << bestLength << endl;
        cout << s.substr(bestLeft, bestLength) << endl;
    }
    return 0;
}
```

### Python Implementation (Approach 2)
```python
from collections import Counter
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = input().strip()
t = input().strip()
freqT = Counter(t)
window = {}
required = len(freqT)
formed = 0
l = 0
best_length = float('inf')
best_l = 0
for r in range(len(s)):
    c = s[r]
    window[c] = window.get(c, 0) + 1
    if c in freqT and window[c] == freqT[c]:
        formed += 1
    while l <= r and formed == required:
        if (r - l + 1) < best_length:
            best_length = r - l + 1
            best_l = l
        d = s[l]
        window[d] -= 1
        if d in freqT and window[d] < freqT[d]:
            formed -= 1
        l += 1
if best_length == float('inf'):
    print("IMPOSSIBLE")
else:
    print(best_length)
    print(s[best_l:best_l+best_length])
```

---

## Approach 3: Optimized Sliding Window Using Arrays

**Concept:**
When the character set is limited (for example, standard ASCII characters), fixed-size arrays can be used instead of hash maps to store character counts. This reduces the constant time overhead, making the algorithm even more efficient.

**Steps:**
1. Use two arrays (of size 128, assuming ASCII) to store counts for $t$ and the current window in $s$.
2. Determine the number of required characters from the frequency array of $t$.
3. Use the sliding window technique to expand and contract the window while comparing the frequency arrays efficiently.

**Time Complexity:**
The complexity remains $O(n)$, but the reduced overhead typically makes this approach faster in practice.

### C++ Implementation (Approach 3)
```cpp
#include
#include
#include
#include
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> s >> t;
    vector freqT(128, 0), window(128, 0);
    for (char c : t)
        freqT[c]++;
    int required = 0;
    for (int i = 0; i < 128; i++) {
        if (freqT[i] > 0)
            required++;
    }
    int formed = 0, left = 0, right = 0;
    int bestLength = INT_MAX, bestLeft = 0;
    while (right < n) {
        char c = s[right];
        window[c]++;
        if (freqT[c] != 0 && window[c] == freqT[c])
            formed++;
        while (left <= right && formed == required) {
            if (right - left + 1 < bestLength) {
                bestLength = right - left + 1;
                bestLeft = left;
            }
            char d = s[left];
            window[d]--;
            if (freqT[d] != 0 && window[d] < freqT[d])
                formed--;
            left++;
        }
        right++;
    }
    if (bestLength == INT_MAX)
        cout << "IMPOSSIBLE" << endl;
    else {
        cout << bestLength << endl;
        cout << s.substr(bestLeft, bestLength) << endl;
    }
    return 0;
}
```

### Python Implementation (Approach 3)
```python
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = input().strip()
t = input().strip()
freqT = [0] * 128
window = [0] * 128
for c in t:
    freqT[ord(c)] += 1
required = sum(1 for count in freqT if count > 0)
formed = 0
l = 0
best_length = float('inf')
best_l = 0
for r, c in enumerate(s):
    window[ord(c)] += 1
    if freqT[ord(c)] > 0 and window[ord(c)] == freqT[ord(c)]:
        formed += 1
    while l <= r and formed == required:
        if (r - l + 1) < best_length:
            best_length = r - l + 1
            best_l = l
        window[ord(s[l])] -= 1
        if freqT[ord(s[l])] > 0 and window[ord(s[l])] < freqT[ord(s[l])]:
            formed -= 1
        l += 1
if best_length == float('inf'):
    print("IMPOSSIBLE")
else:
    print(best_length)
    print(s[best_l: best_l + best_length])
```

---

## Summary

- **Sliding Window with Hashmap:**
  This approach efficiently finds the smallest window in $O(n)$ time by dynamically adjusting the window using two pointers and hashmaps for character frequency.

- **Optimized Sliding Window with Arrays:**
  When the character set is limited (such as ASCII), using fixed-size arrays for frequency counts can further reduce constant time overhead and improve performance.

Both approaches are effective solutions for finding the shortest similar substring and are well-suited for use in technical interviews and real-world applications.

Happy coding and best of luck with your DSA interview preparation!

</details>
