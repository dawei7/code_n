# Valid Parenthesis

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP59 |
| Difficulty Rating | 1100 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [PREP59](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/PREP59) |

---

## Problem Statement

If you are new to stacks and queues, or want a refresher on them, start with our [Learn Stacks and Queues course](https://www.codechef.com/learn/course/stacks-and-queues)

----

Give string a $S$ consisting of only $($ and $)$. Find whether $S$ is a valid parenthesis string.

Note: A **valid parentheses** string is defined as:
- Empty string is valid.
- If $P$ is valid, $(P)$ is also valid.
- If $P$ and $Q$ are valid, $PQ$ is also valid.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing string $S$.

---

## Output Format

For each test case, output $1$ if the given string is a valid parenthesis, or output $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 10^5$
- The sum of $|S|$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
()(())
(()()
))((
```

**Output**

```text
1
0
0
```

**Explanation**

**Test case $1$**: $()(())$ will be valid parenthesis.

**Test case $2$**: $(()()$ will not be valid parenthesis.

**Test case $3$**: $))(($ will not be valid parenthesis.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
()(())
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
(()()
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
))((
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Valid Parentheses String Validation

In this lesson, we explain how to verify whether a string composed entirely of `$($` and `$)$` is a valid parenthesis string. A string is considered valid if:
- The empty string is valid.
- If a string $P$ is valid, then the string `($P$)` is also valid.
- If both $P$ and $Q$ are valid, then their concatenation $PQ$ is valid.

We will cover **two key approaches** to solve this problem. Each approach has a clear methodology, and we explain both with sample implementations in C++ and Python.

---

## Approach 1: Using a Stack Data Structure

### Explanation

A stack is a natural choice to solve problems where the order of operations follows a Last-In-First-Out (LIFO) sequence. In this approach, we:

1. **Initialize an empty stack.**
2. **Traverse each character of the input string:**
   - If the character is `$($`, **push** it onto the stack.
   - If the character is `$)$`, then:
     - Check if the stack is empty. If it is, then the string is invalid (there's no matching `$($`).
     - If the stack is not empty, **pop** the top element.
3. **After processing the entire string:**
   - The string is valid if and only if the stack is empty (every `$($` has a matching `$)$`).

This method has a time complexity of $O(n)$ and uses additional space proportional to the nesting depth of the parentheses.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
using namespace std;

bool isValidParenthesis(const string &s) {
    stack st;
    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else if (c == ')') {
            if (st.empty()) {
                return false;
            }
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        cout << (isValidParenthesis(S) ? 1 : 0) << endl;
    }
    return 0;
}
```

#### Python Code

```python
def isValidParenthesis(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        S = input().strip()
        print(1 if isValidParenthesis(S) else 0)
```

---

## Approach 2: Using a Balance Counter

### Explanation

This approach avoids the overhead of a stack by using a single counter variable to record the balance between opening and closing parentheses.

1. **Initialize a counter (`balance`) to 0.**
2. **Traverse the string character by character:**
   - For each `$($`, increment the counter.
   - For each `$)$`, decrement the counter.
3. **At any point during the traversal:**
   - If the counter becomes negative, it indicates that a closing parenthesis has no matching opening parenthesis, so the string is immediately invalid.
4. **After the traversal:**
   - The string is valid only if the counter is 0 (indicating all `$($` have matching `$)$`).

This approach also operates in $O(n)$ time but uses only constant extra space.

### Code Implementation

#### C++ Code

```cpp
#include
#include
using namespace std;

bool isValidParenthesis(const string &s) {
    int balance = 0;
    for (char c : s) {
        if (c == '(') {
            balance++;
        } else if (c == ')') {
            balance--;
            if (balance < 0) {
                return false;
            }
        }
    }
    return balance == 0;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        cout << (isValidParenthesis(S) ? 1 : 0) << endl;
    }
    return 0;
}
```

#### Python Code

```python
def isValidParenthesis(s: str) -> bool:
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        S = input().strip()
        print(1 if isValidParenthesis(S) else 0)
```

---

## Summary

Both approaches efficiently validate the parenthesis string in linear time, $O(n)$.

- The **stack approach** is intuitive as it directly simulates the matching process, which is especially helpful for beginners.
- The **balance counter approach** minimizes space usage by eliminating the need for an explicit stack.

Choose the approach that best suits your understanding or the specific requirements of your application. Understanding both strategies provides a solid foundation for dealing with similar problems in data structures and algorithms.

</details>
