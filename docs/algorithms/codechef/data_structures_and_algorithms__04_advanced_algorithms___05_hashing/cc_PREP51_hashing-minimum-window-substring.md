# Hashing - Minimum Window Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP51 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Hashing |
| Official Link | [PREP51](https://www.codechef.com/learn/course/hashing/HASH04/problems/PREP51) |

---

## Problem Statement

You are given a string $S$ of length $N$ and a string $T$ of length $M$ consisting of lowercase english characters.

Find the **shortest** substring of $S$ which contains all characters present in $T$ (in any order including duplicates). If there are multiple such substring, return the first occurring **shortest** substring.

If there is no substring in $S$ that contains all characters of $T$, print $-1$ instead.

Note that a substring is obtained by deleting some (possible zero) characters from the beginning and some (possibly zero) characters from the end of the string.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the lengths of strings $S$ and $T$ respectively.
    - The second line of each test case contains a string with $N$ lowercase english alphabets — the string $S$.
    - The third line of each test case contains a string with $M$ lowercase english alphabets — the string $T$.

---

## Output Format

For each test case, output on a new line, the **shortest** substring of $S$ which contains all characters present in $T$ (in any order including duplicates). If there is no substring in $S$ that contains all characters of $T$, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, M \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
- The sum of $M$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
8 4
baccaccb
acbc
3 2
bac
ac
1 1
c
a
```

**Output**

```text
bacc
ac
-1
```

**Explanation**

**Test case $1$:** The substring $S[1:4] = bacc$ and $S[5:8] = accb$ both will be the smallest substring in $S$ contains all characters of the string $T$ but $S[1:4] = bacc$ occurs first.

**Test case $2$:** The substring $S[2:3] = ac$ will be shortest substring that contains all characters in $T$.

**Test case $3$:** No substring present in $S$ that contains all characters in $T$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8 4
baccaccb
acbc
```

**Output for this case**

```text
bacc
```



#### Test case 2

**Input for this case**

```text
3 2
bac
ac
```

**Output for this case**

```text
ac
```



#### Test case 3

**Input for this case**

```text
1 1
c
a
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Minimum Window Substring Problem Editorial

In this lesson, we explore the Minimum Window Substring problem. We are given two strings $S$ and $T$, and our goal is to find the shortest substring in $S$ that contains all characters from $T$ (including duplicates). If no such substring exists, we return $-1$. This problem is classic in interviews and helps develop skills in efficient string manipulation using the sliding window technique.

---

## Approaches to the Problem

Below are two efficient approaches to solve this problem:

---

### 1. Sliding Window Approach

#### **Idea:**

This approach uses the two-pointer (sliding window) technique to efficiently expand and contract a window over string $S$ so that it contains all the characters from $T$.

- **Methodology:**
  - **Expand Window:** Use a `right` pointer to add characters into the current window until it satisfies the condition of having all characters from $T$.
  - **Shrink Window:** Once the window is valid, move the `left` pointer to contract the window and update the smallest valid window found.
  - **Frequency Counts:** Use a hash map (or dictionary) to track the frequency of characters in $T$ and the current window.

- **Time Complexity:**
  $$O(N)$$ in most cases, making it suitable for large inputs.

#### **Code Implementation:**

**C++:**
```cpp
#include
#include
#include
#include
using namespace std;

string slidingWindowMinWindow(const string &S, const string &T) {
    unordered_map targetCount, windowCount;
    for(char c : T) targetCount[c]++;

    int left = 0, count = 0;
    int minLen = INT_MAX, start = 0;

    for (int right = 0; right < S.size(); right++) {
        if (targetCount[S[right]] > 0) {
            windowCount[S[right]]++;
            if (windowCount[S[right]] <= targetCount[S[right]])
                count++;
        }

        while (count == T.size()) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                start = left;
            }
            if (targetCount[S[left]] > 0) {
                windowCount[S[left]]--;
                if (windowCount[S[left]] < targetCount[S[left]])
                    count--;
            }
            left++;
        }
    }
    return (minLen == INT_MAX ? "-1" : S.substr(start, minLen));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;
    while(testCases--){
        int N, M;
        cin >> N >> M;
        string S, T;
        cin >> S >> T;
        cout << slidingWindowMinWindow(S, T) << "\n";
    }
    return 0;
}
```

**Python:**
```python
def sliding_window_min_window(S, T):
    from collections import defaultdict

    targetCount = defaultdict(int)
    for c in T:
        targetCount[c] += 1

    windowCount = defaultdict(int)
    left = 0
    count = 0
    min_len = float('inf')
    start = 0

    for right, c in enumerate(S):
        if c in targetCount:
            windowCount[c] += 1
            if windowCount[c] <= targetCount[c]:
                count += 1

        while count == len(T):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            if S[left] in targetCount:
                windowCount[S[left]] -= 1
                if windowCount[S[left]] < targetCount[S[left]]:
                    count -= 1
            left += 1

    return S[start:start + min_len] if min_len != float('inf') else "-1"

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        N, M = map(int, input().split())
        S = input().strip()
        T = input().strip()
        print(sliding_window_min_window(S, T))
```

---

### 2. Optimized Sliding Window with Filtered Characters

#### **Idea:**

This variant enhances the standard sliding window approach by filtering out characters from $S$ that are not present in $T$. By processing only the relevant characters, the algorithm can reduce unnecessary iterations and improve performance.

- **Methodology:**
  - **Filter $S$:** Generate a filtered list of pairs (index, character) containing only characters from $S$ that also exist in $T$.
  - **Two-Pointer Technique:** Apply the sliding window strategy on this filtered list to identify the minimum valid window.
  - **Frequency Counts:** Maintain frequency maps for characters in the window and the required counts from $T$.

- **Time Complexity:**
  $$O(N)$$ in the worst-case scenario, often faster in practice.

#### **Code Implementation:**

**C++:**
```cpp
#include
#include
#include
#include
#include
using namespace std;

string filteredSlidingWindow(const string &S, const string &T) {
    unordered_map targetCount;
    for (char c : T) {
        targetCount[c]++;
    }

    // Store only the characters in S that are also in T
    vector> filteredS;
    for (int i = 0; i < S.size(); i++) {
        if (targetCount.find(S[i]) != targetCount.end())
            filteredS.push_back({i, S[i]});
    }

    int left = 0, count = 0;
    int minLen = INT_MAX, start = 0;
    unordered_map windowCount;

    for (int right = 0; right < filteredS.size(); right++) {
        char c = filteredS[right].second;
        windowCount[c]++;
        if (windowCount[c] <= targetCount[c])
            count++;

        while (count == T.size()) {
            int windowStart = filteredS[left].first;
            int windowEnd = filteredS[right].first;
            if (windowEnd - windowStart + 1 < minLen) {
                minLen = windowEnd - windowStart + 1;
                start = windowStart;
            }
            char leftChar = filteredS[left].second;
            windowCount[leftChar]--;
            if (windowCount[leftChar] < targetCount[leftChar])
                count--;
            left++;
        }
    }
    return (minLen == INT_MAX ? "-1" : S.substr(start, minLen));
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;
    while(testCases--){
        int N, M;
        cin >> N >> M;
        string S, T;
        cin >> S >> T;
        cout << filteredSlidingWindow(S, T) << "\n";
    }
    return 0;
}
```

**Python:**
```python
def filtered_sliding_window(S, T):
    from collections import defaultdict
    targetCount = defaultdict(int)
    for c in T:
        targetCount[c] += 1

    # Filter S to include only the characters in T with their indices
    filtered_S = [(i, c) for i, c in enumerate(S) if c in targetCount]

    windowCount = defaultdict(int)
    left = 0
    count = 0
    min_len = float('inf')
    start = 0

    for right in range(len(filtered_S)):
        i, c = filtered_S[right]
        windowCount[c] += 1
        if windowCount[c] <= targetCount[c]:
            count += 1

        while count == len(T):
            window_start = filtered_S[left][0]
            window_end = filtered_S[right][0]
            if window_end - window_start + 1 < min_len:
                min_len = window_end - window_start + 1
                start = window_start
            left_c = filtered_S[left][1]
            windowCount[left_c] -= 1
            if windowCount[left_c] < targetCount[left_c]:
                count -= 1
            left += 1

    return S[start:start + min_len] if min_len != float('inf') else "-1"

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        N, M = map(int, input().split())
        S = input().strip()
        T = input().strip()
        print(filtered_sliding_window(S, T))
```

---

## Conclusion

- The **Sliding Window Approach** utilizes two pointers and hash maps to efficiently manage the window boundaries and character frequencies, providing an effective solution even for large inputs.
- The **Optimized Sliding Window** approach further refines this method by processing only the relevant characters in $S$, potentially reducing runtime in practice.

These methods provide robust strategies for solving the Minimum Window Substring problem, illustrating key techniques that are highly valuable in technical interviews.

</details>
