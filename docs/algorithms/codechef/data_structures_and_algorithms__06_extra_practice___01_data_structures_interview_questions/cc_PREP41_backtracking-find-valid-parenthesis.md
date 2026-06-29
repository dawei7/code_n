# Backtracking - Find Valid Parenthesis

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP41 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Backtracking |
| Official Link | [PREP41](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_16/problems/PREP41) |

---

## Problem Statement

Given $N$ pairs of parentheses. Find all **valid parentheses** string of length $2 \cdot N$.

Note: A **valid parentheses** string is defined as:
- Empty string is valid.
- If $P$ is valid, $(P)$ is also valid.
- If $P$ and $Q$ are valid, $PQ$ is also valid.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing integer $N$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of valid parentheses:
- The first line contains a single integer $M$.
- The next $M$ lines contain string of length $2 \cdot N$.

Note: The valid parentheses strings must be printed in **lexicographically increasing** order.
String $S$ is said to be lexicographically smaller than string $T$ if there exists a position $i$ where $S_i \lt T_i$ and $S_j = T_j$ for all $j \lt i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 11$

---

## Examples

**Example 1**

**Input**

```text
2
2
3
```

**Output**

```text
2
(())
()()
5
((()))
(()())
(())()
()(())
()()()
```

**Explanation**

**Test case $1$**: There will be $2$ valid parenthesis strings $(())$, $()()$.

**Test case $2$**: There will be $5$ valid parenthesis strings $((()))$, $(()())$, $(())()$, $()(())$, $()()()$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on Generating Valid Parentheses Strings

In this lesson, we focus on generating all valid parentheses strings of length $2 \cdot N$, given $N$ pairs of parentheses. Recall that a valid parentheses string must satisfy:
- The number of opening parentheses equals the number of closing parentheses.
- At any prefix of the string, the count of opening parentheses is not less than the count of closing parentheses.

In this editorial, we explore two different approaches to solve the problem along with detailed explanations and code implementations in both C++ and Python.

---

## Approach 1: Recursion Backtracking

**Idea:**
We perform a depth-first search (DFS) using recursion to build the valid string one character at a time. We maintain two parameters: the number of remaining opening parentheses (denoted as $open$) and the number of remaining closing parentheses (denoted as $close$). At each recursive call, we consider the following:
- If we have an available opening parenthesis ($open > 0$), we add `'('` and recursively build the rest.
- If we can add a closing parenthesis (only allowed when $close > open$ to maintain validity), we add `')'` and proceed recursively.
- When $open = 0$ and $close = 0$, a complete valid string is formed.

This approach efficiently generates only valid combinations and naturally produces a lexicographically ordered result if we always attempt `'('` before `')'`. Nonetheless, we perform an explicit sort to abide by the output requirement.

**Code Implementations:**

*C++ Code:*
```cpp
#include
#include
#include
#include
using namespace std;

void generateParentheses(int open, int close, string current, vector& result) {
    if (open == 0 && close == 0) {
        result.push_back(current);
        return;
    }

    if (open > 0) {
        generateParentheses(open - 1, close, current + '(', result);
    }

    if (close > open) {
        generateParentheses(open, close - 1, current + ')', result);
    }
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector result;
        generateParentheses(N, N, "", result);

        sort(result.begin(), result.end());

        cout << result.size() << "\n";
        for (const string &s : result) {
            cout << s << "\n";
        }
    }

    return 0;
}
```

*Python Code:*
```python
def generate_parentheses(open_count, close_count, current, result):
    if open_count == 0 and close_count == 0:
        result.append(current)
        return
    if open_count > 0:
        generate_parentheses(open_count - 1, close_count, current + "(", result)
    if close_count > open_count:
        generate_parentheses(open_count, close_count - 1, current + ")", result)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        result = []
        generate_parentheses(N, N, "", result)
        result.sort()
        print(len(result))
        for s in result:
            print(s)
```

---

## Approach 2: Iterative Generation Using Breadth-First Search (BFS)

**Idea:**
We iteratively build valid strings using a queue to simulate the process of breadth-first generation. Each state in the queue is represented by a tuple $(current\_string, open\_count, close\_count)$.
- **Initialization:** Start with an empty string and counts $(N, N)$.
- **Iteration:** For the current state:
  - If both counts are zero, the string is complete and valid.
  - If $open\_count > 0$, append `'('` and decrease the count.
  - If $close\_count > open\_count$, append `')'` and decrease the closing count.

This BFS ensures that we explore all possibilities level-by-level. We sort the obtained results to meet the lexicographically increasing order requirement.

**Code Implementations:**

*C++ Code:*
```cpp
#include
#include
#include
#include
#include
using namespace std;

struct State {
    string curr;
    int open;
    int close;
};

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector result;
        queue q;
        q.push({"", N, N});

        while (!q.empty()) {
            State st = q.front();
            q.pop();
            if (st.open == 0 && st.close == 0) {
                result.push_back(st.curr);
            } else {
                if (st.open > 0) {
                    q.push({st.curr + "(", st.open - 1, st.close});
                }
                if (st.close > st.open) {
                    q.push({st.curr + ")", st.open, st.close - 1});
                }
            }
        }

        sort(result.begin(), result.end());
        cout << result.size() << "\n";
        for (auto &s : result) {
            cout << s << "\n";
        }
    }
    return 0;
}
```

*Python Code:*
```python
from collections import deque

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        result = []
        # Each element: (current_string, open_count, close_count)
        queue = deque()
        queue.append(("", N, N))

        while queue:
            s, open_count, close_count = queue.popleft()
            if open_count == 0 and close_count == 0:
                result.append(s)
            else:
                if open_count > 0:
                    queue.append((s + "(", open_count - 1, close_count))
                if close_count > open_count:
                    queue.append((s + ")", open_count, close_count - 1))

        result.sort()
        print(len(result))
        for seq in result:
            print(seq)
```

---

## Summary

- **Approach 1 (Recursion Backtracking):**
  This is the most efficient and commonly used method due to its pruning of invalid sequences during construction.

- **Approach 2 (Iterative BFS):**
  This method uses a queue to build valid strings level by level and serves as a strong alternative to recursion.

Both approaches ensure that the generated strings are valid and are output in lexicographically increasing order. For most interview scenarios and practical applications, **Approach 1 (Recursion Backtracking)** is recommended due to its optimal performance and simplicity.

</details>
