# Dynamic Programming - Longest Valid Parentheses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP33 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Dynamic Programming |
| Official Link | [PREP33](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_14/problems/PREP33) |

---

## Problem Statement

You are given a string $S$ consisting of only $($ and $)$.

Find the length of the **longest** substring of $S$ which is a *valid parentheses* string.

Note:
- A substring of a string is obtained by deleting some (possibly zero) characters from the beginning and some (possibly zero) characters from the end.
- A *valid parentheses* string is defined as:
    - Empty string is valid.
    - If $P$ is valid, $(P)$ is also valid.
    - If $P$ and $Q$ are valid, $PQ$ is also valid.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case consists of a string $S$, consisting of $($ and $)$ only.

---

## Output Format

For each test case, output on a new line, the length of the **longest** substring of $S$ which is a *valid parentheses* string.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq |S| \leq 10^5$
- $S$ contains $($ and $)$ only.
- The sum of $|S|$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
(()
)
)(())()
)((
```

**Output**

```text
2
0
6
0
```

**Explanation**

**Test case $1$:** The longest valid parentheses substring is $()$ having length $2$.

**Test case $2$:** There is no valid parentheses substring in the string.

**Test case $3$:** The longest valid parentheses substring is $(())()$ having length $6$.

**Test case $4$:** There is no valid parentheses substring in the string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
(()
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
)
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
)(())()
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
)((
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial - Longest Valid Parentheses

In this lesson, we explore the problem of finding the length of the longest valid parentheses substring in a given string $S$. This problem requires identifying continuous segments of the string that form valid pairs of parentheses (i.e., each opening bracket has a corresponding closing bracket in the proper order). We will discuss three different approaches that are common in interviews: the **Stack Based Approach**, the **Dynamic Programming Approach**, and the **Two-Pass (Two Pointers) Approach**. Each approach has distinct trade-offs and strengths, and understanding them will deepen your problem-solving skills.

---

## Approach 1: Stack Based Approach

### Explanation:
The stack-based approach uses a stack to keep track of indices where unmatched parentheses occur. We start by initializing the stack with $-1$, which serves as the base for computing valid substring lengths. As we scan the string:
- When we encounter an opening bracket `(`, we push its index onto the stack.
- When we encounter a closing bracket `)`, we pop an element from the stack.
  - If the stack becomes empty, it means the current closing bracket does not have a matching opening bracket, so we push its index to serve as a new base.
  - Otherwise, the current valid substring’s length is determined by subtracting the new top of the stack from the current index.

This approach runs in $O(n)$ time and uses $O(n)$ space in the worst-case scenario.

### Code Implementation:

#### C++ Code:
```cpp
#include
#include
#include
#include
using namespace std;

int longestValidParentheses(string s) {
    int n = s.length();
    int maxLen = 0;
    stack stk;
    stk.push(-1);  // Base for the first valid substring

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stk.push(i);
        } else {
            stk.pop();
            if (stk.empty()) {
                stk.push(i);  // Set new base
            } else {
                maxLen = max(maxLen, i - stk.top());
            }
        }
    }

    return maxLen;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        string S;
        cin >> S;
        cout << longestValidParentheses(S) << endl;
    }

    return 0;
}
```

#### Python Code:
```python
def longestValidParentheses(s: str) -> int:
    max_len = 0
    stack = [-1]  # Base for the first valid substring

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # Set new base
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input().strip()
        print(longestValidParentheses(s))
```

---

## Approach 2: Dynamic Programming

### Explanation:
The dynamic programming approach leverages a DP array, where $dp[i]$ represents the length of the longest valid substring ending at index $i$. The state transitions are as follows:

- **Case 1:** If $s[i] = ')' $ and $s[i-1] = '(' $, then we have a pair `"()"`, so we set:
  $$ dp[i] = dp[i-2] + 2 $$
  (with an adjustment if $i < 2$).

- **Case 2:** If $s[i] = ')' $ and $s[i-1] = ')'$, then we check if the character preceding the valid substring ending at $i-1$ is an opening bracket. Formally, if $i - dp[i-1] - 1 \geq 0$ and $s[i - dp[i-1] - 1] = '('$, then:
  $$ dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2] $$

This method also operates in $O(n)$ time with $O(n)$ extra space. It illustrates how storing intermediate results can simplify the problem and reduce redundant checks.

### Code Implementation:

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int longestValidParentheses(string s) {
    int n = s.length();
    if(n == 0) return 0;
    vector dp(n, 0);
    int maxLen = 0;

    for (int i = 1; i < n; i++) {
        if(s[i] == ')') {
            if(s[i-1] == '(') {
                dp[i] = 2 + (i >= 2 ? dp[i-2] : 0);
            } else if(i - dp[i-1] - 1 >= 0 && s[i - dp[i-1] - 1] == '(') {
                dp[i] = dp[i-1] + 2 + ((i - dp[i-1] - 2) >= 0 ? dp[i - dp[i-1] - 2] : 0);
            }
            maxLen = max(maxLen, dp[i]);
        }
    }

    return maxLen;
}

int main() {
    int T;
    cin >> T;

    while(T--) {
        string S;
        cin >> S;
        cout << longestValidParentheses(S) << endl;
    }

    return 0;
}
```

#### Python Code:
```python
def longestValidParentheses(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    max_len = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = 2 + (dp[i - 2] if i >= 2 else 0)
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
            max_len = max(max_len, dp[i])

    return max_len

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input().strip()
        print(longestValidParentheses(s))
```

---

## Approach 3: Two-Pass (Two Pointers) Approach

### Explanation:
The two-pass approach improves space efficiency by using only counters:
1. **Left-to-Right Pass:**
   We use two counters, $open$ and $close$, initialized to zero. As we scan the string:
   - Increment $open$ when encountering `'('`.
   - Increment $close$ when encountering `')'`.
   - If $open$ equals $close$, we update our maximum length as $2 \times close$.
   - If $close > open$, we reset both counters, as further valid substrings must start after this point.

2. **Right-to-Left Pass:**
   To catch cases where there are excess opening brackets, we repeat the process traversing from right to left. This time, the counters are reset when $open > close$.

This method is efficient with $O(n)$ time complexity and constant $O(1)$ space.

### Code Implementation:

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int longestValidParentheses(string s) {
    int maxLen = 0, open = 0, close = 0;
    int n = s.length();

    // Left to right pass
    for (int i = 0; i < n; i++) {
        if (s[i] == '(')
            open++;
        else
            close++;

        if(open == close)
            maxLen = max(maxLen, 2 * close);
        else if(close > open)
            open = close = 0;
    }

    open = close = 0;
    // Right to left pass
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '(')
            open++;
        else
            close++;

        if(open == close)
            maxLen = max(maxLen, 2 * open);
        else if(open > close)
            open = close = 0;
    }

    return maxLen;
}

int main() {
    int T;
    cin >> T;

    while(T--) {
        string S;
        cin >> S;
        cout << longestValidParentheses(S) << endl;
    }

    return 0;
}
```

#### Python Code:
```python
def longestValidParentheses(s: str) -> int:
    max_len = 0
    open_count = close_count = 0
    n = len(s)

    # Left to right pass
    for char in s:
        if char == '(':
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            max_len = max(max_len, 2 * close_count)
        elif close_count > open_count:
            open_count = close_count = 0

    # Reset counters for right to left pass
    open_count = close_count = 0
    for char in s[::-1]:
        if char == '(':
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            max_len = max(max_len, 2 * open_count)
        elif open_count > close_count:
            open_count = close_count = 0

    return max_len

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input().strip()
        print(longestValidParentheses(s))
```

---

### Summary

- **Stack Based Approach:**
  Uses a stack to track unmatched indices and calculate lengths. It is intuitive and directly simulates the pairing process.

- **Dynamic Programming Approach:**
  Uses a DP array to build solutions based on smaller subproblems. This approach is beneficial for understanding how local relationships build up into a global solution.

- **Two-Pass (Two Pointers) Approach:**
  Leverages counter variables, scanning from both directions to capture all valid substrings with constant extra space.

By practicing all three approaches, you will be better equipped to tackle variations of the valid parentheses problem, a frequent topic in DSA interviews.

Happy coding and keep practicing!

</details>
