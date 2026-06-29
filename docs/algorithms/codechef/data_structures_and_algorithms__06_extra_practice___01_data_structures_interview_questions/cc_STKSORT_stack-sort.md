# Stack Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STKSORT |
| Difficulty Rating | 1400 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STKSORT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/STKSORT) |

---

## Problem Statement

You have an array $A$ of integers of size $N$, an array $B$ ( initially empty ) and a stack $S$ ( initially empty ). You are allowed to do the following operations :

- Take the first element of array $A$ and push it into $S$ and remove it from $A$.
- Take the top element from stack $S$, append it to the end of array $B$ and remove it from $S$.

You have to tell if it possible to move all the elements of array $A$ to array $B$ using the above operations such that finally the array $B$ is sorted in ascending order.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains a single integer $N$.
- Second line of each testcase contains $N$ **distinct** integers : $A_1, A_2 . . . A_N$.

---

## Output Format

For each testcase, if it possible to move all the elements of array $A$ to array $B$ using the above operations such that finally, the array $B$ is sorted in ascending order, print "YES" (without quotes), else print "NO" (without quotes).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- $A_i = A_j$ if and only if $i = j$

It is guaranteed that the sum of values of $N$ over all the test cases doesn't exceed $2*10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
4
1 2 4 3
4
1 3 4 2
```

**Output**

```text
YES
NO
```

**Explanation**

**Test-case 1:**
Consider the following sequence of operations
- Remove $1$ from $A$ and push it into $S$.
- Remove $1$ from $S$ and append it to $B$.
- Remove $2$ from $A$ and push it into $S$.
- Remove $2$ from $S$ and append it to $B$.
- Remove $4$ from $A$ and push it into $S$.
- Remove $3$ from $A$ and push it to $S$.
- Remove $3$ from $S$ and append it to $B$.
- Remove $4$ from $S$ and append it to $B$.

By following above sequence of operations you end up with $B = [1, 2, 3, 4]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 4 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
1 3 4 2
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore a classic problem in stack-sorting. Given an array $A$ of distinct integers (a permutation of $1$ to $N$), we must decide whether it is possible to transfer all elements from $A$ to an initially empty array $B$ using a stack $S$, such that $B$ becomes sorted in ascending order. The only allowed operations are:
- Remove the first element from $A$ and push it into $S$.
- Pop the top element of $S$ and append it to $B$.

A permutation that can be sorted using these operations is called **stack-sortable**.

Below, we discuss two different approaches to solve this problem:

---

### **Approach 1: Stack Simulation with Next Expected Number**

**Idea:**
We simulate the allowed operations while keeping track of the next number expected in sorted order. Initialize a variable `next_num` to $1$ (since the sorted order is $1,2,\dots,N$). For each element in $A$:
- **If** it equals `next_num`, we simulate an immediate move to $B$ by simply incrementing `next_num`.
- **Else** we push the element onto stack $S$.

Before processing each new element from $A$, we pop from $S$ if its top equals `next_num` (since these can safely be moved to $B$).

The simulation fails if at any point the current element is greater than the element at the top of the stack. This condition prevents us from later retrieving smaller elements (because a stack operates in LIFO order) and ultimately getting the sorted sequence in $B$.

**Complexity:**
Time complexity is $O(N)$ because each element is pushed and popped at most once.

**Code Implementation:**

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

bool canSort(vector& A) {
    int N = A.size();
    stack S;
    int next_num = 1;

    for (int i = 0; i < N; i++) {
        // Move elements from S to B (simulate by incrementing next_num)
        while (!S.empty() && S.top() == next_num) {
            S.pop();
            next_num++;
        }

        if (A[i] == next_num) {
            // Directly move A[i] to B
            next_num++;
        } else if (!S.empty() && A[i] > S.top()) {
            // It is impossible to get a sorted order.
            return false;
        } else {
            // Push A[i] to the stack
            S.push(A[i]);
        }
    }

    // Final clearing: move remaining elements if they are in order.
    while (!S.empty() && S.top() == next_num) {
        S.pop();
        next_num++;
    }

    return S.empty();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << (canSort(A) ? "YES" : "NO") << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def can_sort(A):
    stack = []
    next_num = 1

    for number in A:
        # Pop from stack if possible
        while stack and stack[-1] == next_num:
            stack.pop()
            next_num += 1

        if number == next_num:
            next_num += 1
        elif stack and number > stack[-1]:
            return False
        else:
            stack.append(number)

    # Final clearing: pop any remaining elements in order
    while stack and stack[-1] == next_num:
        stack.pop()
        next_num += 1

    return not stack

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print("YES" if can_sort(A) else "NO")
```

---

### **Approach 2: Checking for the 231-Pattern (Monotonic Stack Approach)**

**Idea:**
A well-known result in combinatorics states that a permutation is stack-sortable if and only if it avoids the **231-pattern**. In other words, if there exist indices $i < j < k$ such that $A[k] < A[i] < A[j]$, then the permutation is not stack-sortable.

A practical way to check this pattern is by using a monotonic stack while maintaining a variable `last` (which represents the last popped element). The algorithm works as follows:
- Initialize `last` to a very small value (for our constraints, we can use $0$ because all array values are at least $1$).
- Iterate over each element in $A$. For the current element, pop elements from the stack while the top element is less than the current element and update `last` with the popped value.
- If at any point, the current element is less than `last`, then $A$ contains the forbidden pattern and hence is not stack-sortable.
- Otherwise, push the current element onto the stack.

**Complexity:**
This method also runs in $O(N)$ time, making it efficient for the given constraints.

**Code Implementation:**

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

bool isStackSortable(vector& A) {
    int n = A.size();
    int last = 0; // Using 0 as the initial value (lower than any element in A)
    stack s;

    for (int i = 0; i < n; i++) {
        // Pop smaller elements and update 'last'
        while (!s.empty() && s.top() < A[i]) {
            last = s.top();
            s.pop();
        }
        // If current element is less than the last popped element, it violates the order.
        if (A[i] < last)
            return false;
        s.push(A[i]);
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << (isStackSortable(A) ? "YES" : "NO") << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def is_stack_sortable(A):
    last = 0  # Starting with 0 as all elements are >= 1
    stack = []

    for num in A:
        # Pop from the stack as long as its top element is less than 'num'
        while stack and stack[-1] < num:
            last = stack.pop()
        # If the current number is smaller than 'last', the 231 pattern exists.
        if num < last:
            return False
        stack.append(num)

    return True

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print("YES" if is_stack_sortable(A) else "NO")
```

---

### **Summary**

- **Approach 1** simulates the process using a stack and a `next_num` variable.
- **Approach 2** leverages the result from combinatorics that a permutation is stack-sortable if it avoids the 231-pattern.

Both approaches run in $O(N)$ time and are efficient for handling large input sizes. For real interview scenarios (with constraints up to $10^5$ elements), either of these methods is recommended.

Happy coding and good luck with your DSA interviews!

</details>
