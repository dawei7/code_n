# Previous smaller element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP60 |
| Difficulty Rating | 1200 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [PREP60](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/PREP60) |

---

## Problem Statement

You are given an array $A$ of size $N$.

We define the *previous smaller element* of an element $A_i$ as the element $A_j$ such that $A_j \lt A_i$ and $j$ is **maximum** possible.

Find the *previous smaller element* for every element $A_i$ in the array. Output $-1$ for the elements which have no *previous smaller element*.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer - $N$.
    - The next line contains $N$ space-separated integers - the array $A$.

---

## Output Format

For each test case, output on a new line, $N$ space-separated integers denoting the *previous smaller element* of the $i^{th}$ element of the array. Output $-1$ for the elements which have no *previous smaller element*.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\times 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5
4 5 2 10 8
3
3 2 1
4
1 2 3 4
```

**Output**

```text
-1 4 -1 2 2 
-1 -1 -1 
-1 1 2 3
```

**Explanation**

**Test case $1$:** Given $A$ as $[4, 5, 2, 10, 8]$.
- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: The element at $i=1$ is smaller than that at $i=2$ and is at the nearest left. Hence $A_1=4$ is the output.
- $i=3$: No element to the left which is smaller than $A_3=2$. Hence $-1$ is the output.
- $i=4$: The element at $i=3$ is smaller than that at $i=4$ and is at the nearest left. Hence $A_3=2$ is the output.
- $i=5$: The element at $i=3$ is smaller than that at $i=5$ and is at the nearest left. Hence $A_3=2$ is the output.

**Test case $2$:** Given $A$ as $[3, 2, 1]$.
- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: No element to the left which is smaller than $2$. Hence $-1$ is the output.
- $i=3$: No element to the left which is smaller than $1$. Hence $-1$ is the output.

**Test case $3$:** Given $A$ as $[1, 2, 3, 4]$.
- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: The element at $i=1$ is smaller than that at $i=2$ and is at the nearest left. Hence $A_1=1$ is the output.
- $i=3$: The element at $i=2$ is smaller than that at $i=3$ and is at the nearest left.. Hence $A_2=2$ is the output.
- $i=4$: The element at $i=3$ is smaller than that at $i=4$ and is at the nearest left.. Hence $A_3=3$ is the output.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
4 5 2 10 8
```

**Output for this case**

```text
-1 4 -1 2 2
```



#### Test case 2

**Input for this case**

```text
3
3 2 1
```

**Output for this case**

```text
-1 -1 -1
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
-1 1 2 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss the problem of finding the *previous smaller element* for every element in an array. Given an array $A$ of size $N$, for every element $A_i$, we need to find the nearest element to its left that is strictly smaller. If there is no such element for $A_i$, we output $-1$.

There are multiple approaches that one might consider:

---

### Approach 1: Brute Force

**Idea:**
For each element $A_i$, scan all the elements to the left, i.e. from $A_{i-1}$ to $A_1$ to find the closest element that is smaller than $A_i$.

**Methodology:**
1. For each index $i$ from $0$ to $N-1$:
   - Initialize the answer as $-1$.
   - Loop backward from index $i-1$ until $0$.
   - If we find an element $A_j$ such that $A_j < A_i$, then store it as the result for $A_i$ and break out of the loop.
2. Time complexity is $$ O(n^2) $$ in the worst-case scenario (particularly for arrays that are sorted in non-decreasing order).

**Code Implementations:**

*C++ Code:*

```cpp
#include
#include
using namespace std;

void solveBruteForce() {
    int n;
    cin >> n;
    vector arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++) {
        int prevSmaller = -1;
        for (int j = i - 1; j >= 0; j--) {
            if (arr[j] < arr[i]) {
                prevSmaller = arr[j];
                break;
            }
        }
        cout << prevSmaller << " ";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--) {
        solveBruteForce();
    }
    return 0;
}
```

*Python Code:*

```python
def solve_brute_force():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = []
    for i in range(n):
        prev_smaller = -1
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                prev_smaller = arr[j]
                break
        result.append(prev_smaller)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        solve_brute_force()
```

---

### Approach 2: Monotonic Stack

**Idea:**
We improve on the brute force method by using a **monotonic stack**. The idea is to maintain a stack that keeps indices of an increasing sequence of elements. For each element:
- We pop elements from the stack until the top element of the stack is smaller than the current element.
- If the stack is not empty after this, the element at the top is the previous smaller element.
- Then we push the current element's index onto the stack.

**Methodology:**
1. Initialize an empty stack.
2. For each index $i$ from $0$ to $N-1$:
   - While the stack is not empty and $A[\text{stack.top()}] \ge A_i$, pop the stack.
   - If the stack is not empty, then $A[\text{stack.top()}]$ is the previous smaller element for $A_i$, otherwise output $-1$.
   - Push the index $i$ into the stack.
3. This algorithm runs in $$ O(n) $$ time since every element is pushed and popped at most once.

**Code Implementations:**

*C++ Code:*

```cpp
#include
#include
#include
using namespace std;

void solveMonotonicStack() {
    int n;
    cin >> n;
    vector arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector result(n, -1);
    stack st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && arr[st.top()] >= arr[i]) {
            st.pop();
        }
        if (!st.empty()) {
            result[i] = arr[st.top()];
        }
        st.push(i);
    }

    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--) {
        solveMonotonicStack();
    }
    return 0;
}
```

*Python Code:*

```python
def solve_monotonic_stack():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        solve_monotonic_stack()
```

---

### Discussion and Conclusions

- **Brute Force Approach:**
  This approach is straightforward and easy to understand. However, due to its $$ O(n^2) $$ time complexity, it may not be optimal for large arrays. It is useful to understand basic iteration and checking techniques.

- **Monotonic Stack Approach:**
  This is the optimal solution for this problem. The use of a stack allows us to obtain the previous smaller element for each array element in nearly $$ O(n) $$ time. This method is efficient and widely applicable in similar problems involving "next" or "previous" greater or smaller elements.

**Intuition:**
The monotonic stack effectively keeps track of candidates that could potentially be the previous smaller element. By maintaining a structure where elements are stored in an increasing order, we can quickly discard elements that are too large to be of any use for the current element. This optimizes the search compared to the brute force method.

By understanding both these approaches, you not only learn how to implement a solution for this particular problem but also gain insight into how stacks can be used to solve similar problems in data structures and algorithms.

Happy coding and best of luck with your interview preparations!

</details>
