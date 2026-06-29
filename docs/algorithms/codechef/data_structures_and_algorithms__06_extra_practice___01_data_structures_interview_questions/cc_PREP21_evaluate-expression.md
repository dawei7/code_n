# Evaluate Expression

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP21 |
| Difficulty Rating | 1200 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [PREP21](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/PREP21) |

---

## Problem Statement

You are given a string $S$ consisting of $N$ characters. Each character is either a digit from $0$ to $9$ or an operator out of `+`, `-`, and `*`.

Consider the string to be in [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation#) consisting of **digits** (from $1$ to $9$) as the operands and `+`, `-`, or `*` as the operators and evaluate the expression.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number of characters in the string.
    - The next line consists of $N$ characters, where the $i^{th}$ character is either a digit from $0$ to $9$ or an operator out of `+`, `-`, and `*`. Consider the string to be in reverse polish notation.

---

## Output Format

For each test case, output on a new line, an integer denoting the evaluated expression.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
73-
7
04*3*0-
3
27*
7
703*-9-
```

**Output**

```text
4
0
14
-2
```

**Explanation**

**Test case $1$:** The postfix expression corresponds to $7-3$ which is equal to $4$.

**Test case $2$:** The postfix expression corresponds to $((0\times 4)\times 3) - 0)$ which is equal to $0$.

**Test case $3$:** The postfix expression corresponds to $2\times 7$ which is equal to $14$.

**Test case $4$:** The postfix expression corresponds to $(7 - (0\times 3)) - 9)$ which is equal to $-2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
73-
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
7
04*3*0-
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3
27*
```

**Output for this case**

```text
14
```



#### Test case 4

**Input for this case**

```text
7
703*-9-
```

**Output for this case**

```text
-2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to evaluate a Reverse Polish Notation (RPN) expression. An RPN expression is one where every operator follows all of its operands. For example, the RPN expression for $7-3$ is represented as “73-”. We will explore two important approaches to solving this problem.

---

## Approach 1: Iterative Stack Evaluation

The iterative approach is the most common method for evaluating an RPN expression. The idea is to use a stack to keep track of the operands. As you scan the string from left to right:

- **If the current character is a digit:**
  Convert it to its numeric value and push it onto the stack.

- **If the current character is an operator:**
  Pop the top two numbers from the stack (say, $a$ and $b$ in that order). Then, apply the operator to get the result of $a\,op\,b$. Finally, push the result back onto the stack.

At the end of the traversal, the stack will contain exactly one element, which is the result of the evaluated expression.

**Time Complexity:**
The algorithm works in $\mathcal{O}(N)$ where $N$ is the number of characters. Each character is processed only once.

Below are the implementations in C++ and Python:

### C++ Implementation

```cpp
#include
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string s;
        cin >> s;
        stack st;
        for (char ch : s) {
            if (isdigit(ch)) {
                st.push(ch - '0');
            } else {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                if (ch == '+')
                    st.push(a + b);
                else if (ch == '-')
                    st.push(a - b);
                else if (ch == '*')
                    st.push(a * b);
            }
        }
        cout << st.top() << "\n";
    }
    return 0;
}
```

### Python Implementation

```python
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    s = input().strip()
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
    print(stack[-1])
```

---

## Approach 2: Recursive Evaluation by Converting to Prefix Expression

Another interesting method to evaluate an RPN expression is to take advantage of recursion by converting the RPN expression to a prefix expression. **Why Reverse?**
When you reverse an RPN expression, the order turns into a prefix expression. Consider the RPN expression “73-”, which represents $7-3$. Reversing it gives “-37”. In a prefix expression, the operator comes first and is followed by its operands. However, note that after reversing the string, when you process an operator, you must **first evaluate the right operand and then the left operand**. This ensures that when you combine them, the operation is executed in the correct order (i.e. you compute $7-3$, not $3-7$).

**Algorithm Outline:**
- Reverse the input string to get a prefix-like expression.
- Use a recursive function that:
  - Reads the next token.
  - If the token is a digit, returns its numeric value.
  - If the token is an operator, recursively evaluates the next token(s) in order to determine the right operand first and then the left operand. Finally, it applies the operator in the order: left operator right.

This approach also runs in $\mathcal{O}(N)$ time but requires recursion. It is important to note that for very deep expressions, the recursion depth might be an issue; however, within the given constraints, this method works well.

Below are the implementations in C++ and Python:

### C++ Implementation

```cpp
#include
#include
#include
#include
using namespace std;

int idx; // global index for recursive traversal

int evalPrefix(const string &s) {
    char token = s[idx++];
    if (isdigit(token)) {
        return token - '0';
    }
    // For an operator, first evaluate the right operand and then the left operand.
    int right = evalPrefix(s);
    int left = evalPrefix(s);
    if (token == '+') return left + right;
    if (token == '-') return left - right;
    if (token == '*') return left * right;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string s;
        cin >> s;
        // Reverse the string to convert the RPN to a prefix expression.
        reverse(s.begin(), s.end());
        idx = 0;
        cout << evalPrefix(s) << "\n";
    }
    return 0;
}
```

### Python Implementation

```python
import sys
sys.setrecursionlimit(10**6)

def eval_prefix(s, idx):
    token = s[idx[0]]
    idx[0] += 1
    if token.isdigit():
        return int(token)
    # For an operator, first evaluate the right operand then the left operand.
    right = eval_prefix(s, idx)
    left = eval_prefix(s, idx)
    if token == '+':
        return left + right
    elif token == '-':
        return left - right
    elif token == '*':
        return left * right

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    # Reverse the string to get a prefix expression.
    s = s[::-1]
    idx = [0]
    print(eval_prefix(s, idx))
```

---

Both these approaches efficiently evaluate an RPN expression, and each has its own advantages:
- **Iterative Stack Evaluation (Approach 1)** is straightforward and widely used.
- **Recursive Evaluation via Reversed Prefix Conversion (Approach 2)** offers a recursive perspective that underlines the connection between different notations in mathematical expressions.

By understanding these methods, you will be better prepared to tackle a variety of problems in DSA interviews. Remember that the iterative approach is generally recommended for its simplicity and low overhead, whereas the recursive method provides valuable insight into alternative evaluation strategies.

</details>
