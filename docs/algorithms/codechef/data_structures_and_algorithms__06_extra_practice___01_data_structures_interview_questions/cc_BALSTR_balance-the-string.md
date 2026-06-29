# Balance the String 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BALSTR |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [BALSTR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/BALSTR) |

---

## Problem Statement

Alice has been asked to balance a string $S$ given to her.
The string contains of only ‘(‘ and ‘)’. A string $S$ is said to be balanced if-
- Open brackets must be closed by the corresponding closing bracket.
- Open brackets must be closed in the correct order.

Find the minimum number of ‘(‘ or ‘)’ she would have to add anywhere to balance out the string.

---

## Input Format

- First line will contain $T$, the number of test cases.
- For every test case, next line will contain 1 integer $N$ ,size of the string
 And its next line has the string $S$.

---

## Output Format

For each test case, the minimum number of parentheses Alice can add to balance the string $S$. separated by a new line or a space.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \le |S| \le 10^6$

---

## Examples

**Example 1**

**Input**

```text
1
2
()
```

**Output**

```text
0
```

**Explanation**

The string is already balanced.

**Example 2**

**Input**

```text
1
8
)(())(()
```

**Output**

```text
2
```

**Explanation**

To make it balanced, the minimum amount of brackets to be added are 2.
The string becomes ***(***)(())(()***)***

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Balancing Parentheses: An Editorial

In this lesson, we explore different ways to solve the problem of balancing a string of parentheses. Given a string $S$ containing only the characters `(` and `)`, our challenge is to determine the minimum number of parentheses that must be added (at any position) in order to make the string balanced. A balanced string satisfies the following:
- Every opening parenthesis $($ must have a corresponding closing parenthesis $)$.
- The parentheses must be closed in the correct order.

For example, the string `)(())(()` requires 2 additional parentheses to become balanced.

Below, we discuss **three approaches** to solve the problem, along with complete C++ and Python implementations.

---

## Approaches to the Problem

### Approach 1: Stack-Based Method

**Idea:**
We use a stack to keep track of the unmatched opening parentheses. When we encounter an opening parenthesis $($, we push it onto the stack. When we encounter a closing parenthesis $)$, we check:
- If the stack is not empty, the top of the stack is an opening parenthesis and can be paired. We pop the stack.
- If the stack is empty, it means there is no matching $($, so we count this closing parenthesis as unmatched.

After processing the entire string, the number of unmatched opening parentheses is the size of the stack. The final answer is the sum of unmatched closing parentheses (tracked by a counter) and the size of the stack.

**Time Complexity:**
$$ O(n) $$

**Space Complexity:**
$$ O(n) $$ in the worst case.

---

### Approach 2: Simple Counting Method

**Idea:**
Instead of using a stack, we can simply use two counters:
- A variable `balance` to record the current number of unclosed opening parentheses.
- A variable `insertions` to record the number of extra closing parentheses needed when the count goes negative.

For each character in the string:
- If the character is $($, we increase `balance`.
- If the character is $)$ and `balance` is positive, we reduce `balance`.
- If the character is $)$ and `balance` is zero, it means there is no matching opening parenthesis so we increment `insertions`.

At the end, any remaining `balance` indicates unmatched opening parentheses. The answer is:
$$ \text{insertions} + \text{balance} $$

**Time Complexity:**
$$ O(n) $$

**Space Complexity:**
$$ O(1) $$

---

### Approach 3: Bidirectional Scan (Two-Pass Approach)

**Idea:**
This method involves two passes over the string:

1. **Left-to-Right Pass:**
   - We count the extra closing parentheses required.
   - Initialize `balance` to $0$. For every character, if it is $($, increment `balance`; if it is $)$ and there is no corresponding $($ (i.e. `balance` is $0$), increment a counter `extraClosing`.

2. **Right-to-Left Pass:**
   - We count extra opening parentheses by performing a similar scan in reverse.
   - Initialize a counter `revBalance` to $0$. For every character (iterating from end to start), if it is $)$, increment `revBalance`; if it is $($ and `revBalance` is zero, it means there is no matching $)$, so increment a counter `extraOpening`.

The final answer becomes:
$$ \text{extraClosing} + \text{extraOpening} $$

**Time Complexity:**
$$ O(n) $$ (two passes over the string)

**Space Complexity:**
$$ O(1) $$

---

## Code Implementations

Below, you will find the code implementations in both **C++** and **Python** for each approach.

### Approach 1: Stack-Based Method

#### **C++ Code**
```cpp
#include
#include
#include
using namespace std;

int minParenthesesToAdd(const string& s) {
    stack st;
    int unmatchedClosing = 0;
    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else {
            if (!st.empty() && st.top() == '(') {
                st.pop();
            } else {
                unmatchedClosing++;  // Unmatched closing parenthesis
            }
        }
    }
    // st.size() gives the count of unmatched opening parentheses.
    return unmatchedClosing + st.size();
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << minParenthesesToAdd(S) << "\n";
    }
    return 0;
}
```

#### **Python Code**
```python
def min_parentheses_to_add(s: str) -> int:
    stack = []
    unmatched_closing = 0
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                unmatched_closing += 1
    return unmatched_closing + len(stack)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(min_parentheses_to_add(s))
```

---

### Approach 2: Simple Counting Method

#### **C++ Code**
```cpp
#include
#include
using namespace std;

int minParenthesesToAdd(const string& s) {
    int balance = 0, insertions = 0;
    for (char c : s) {
        if (c == '(') {
            balance++;
        } else {
            if (balance > 0)
                balance--;
            else
                insertions++;  // Extra closing parenthesis needed
        }
    }
    return insertions + balance;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << minParenthesesToAdd(S) << "\n";
    }
    return 0;
}
```

#### **Python Code**
```python
def min_parentheses_to_add(s: str) -> int:
    balance = 0
    insertions = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                insertions += 1
    return insertions + balance

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(min_parentheses_to_add(s))
```

---

### Approach 3: Bidirectional Scan (Two-Pass Approach)

#### **C++ Code**
```cpp
#include
#include
using namespace std;

int minParenthesesToAdd(const string& s) {
    int extraClosing = 0, balance = 0;
    // Left-to-right pass: Count extra closing parentheses needed
    for (char c : s) {
        if (c == '(')
            balance++;
        else {
            if (balance > 0)
                balance--;
            else
                extraClosing++;
        }
    }

    int extraOpening = 0, revBalance = 0;
    // Right-to-left pass: Count extra opening parentheses needed
    for (int i = s.size() - 1; i >= 0; i--) {
        char c = s[i];
        if (c == ')')
            revBalance++;
        else {
            if (revBalance > 0)
                revBalance--;
            else
                extraOpening++;
        }
    }

    return extraClosing + extraOpening;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;
        cout << minParenthesesToAdd(S) << "\n";
    }
    return 0;
}
```

#### **Python Code**
```python
def min_parentheses_to_add(s: str) -> int:
    extra_closing = 0
    balance = 0
    # Left-to-right pass for extra closing parentheses
    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                extra_closing += 1

    extra_opening = 0
    rev_balance = 0
    # Right-to-left pass for extra opening parentheses
    for char in reversed(s):
        if char == ')':
            rev_balance += 1
        else:
            if rev_balance > 0:
                rev_balance -= 1
            else:
                extra_opening += 1

    return extra_closing + extra_opening

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(min_parentheses_to_add(s))
```

---

## Conclusion

All three approaches solve the problem in linear time $O(n)$ and are acceptable given the constraints. The **Stack-Based Method (Approach 1)** is intuitive but may use extra space in the worst case. The **Simple Counting Method (Approach 2)** and the **Bidirectional Scan (Approach 3)** offer a space-efficient solution with constant extra space. Beginners are encouraged to understand each approach and choose the one that best suits their problem-solving style.

Happy coding and good luck with your DSA interviews!

</details>
