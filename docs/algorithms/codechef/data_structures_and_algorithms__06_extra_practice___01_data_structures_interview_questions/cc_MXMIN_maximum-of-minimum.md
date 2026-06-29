# Maximum of Minimum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXMIN |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [MXMIN](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/MXMIN) |

---

## Problem Statement

Given an array $A$ of integers of size $N$. For every window size from $1$ to $N$, you have to find the maximum value among the minimum(s) of that window size in the array.

For example if $A = [2,4,6]$ then

Windows of size $1$ are - $[2], [4], [6]$, and the minimum value in each window is $2,4,6$. Among these values, the maximum is $6$.

Similarly, windows of size $2$ are - $[2,4], [4,6]$, and the minimum value in each window is $2,4$. Among these values, the maximum is $4$.

Similarly, Windows of size $3$ are - $[2,4,6]$, the minimum value in each window is $2$. Among these values, the maximum is $2$.

So the answer for this array will be $[6,4,2]$.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the number of days
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the array.

---

## Output Format

For each test case, output in a single line $N$ integers- the $i$-th integer denotes the answer for the window of size $i$.

---

## Constraints

- $1 \leq T \leq 1500$
- $2 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
3
7 18 16
5
3 13 2 10 8
5
17 9 13 7 12
7
4 8 10 16 14 19 3
```

**Output**

```text
18 16 7 
13 8 2 2 2 
17 9 9 7 7 
19 14 14 10 8 4 3
```

**Explanation**

- **Test Case $2$**: Following are the windows with different sizes and their minimums

Windows of size $1 - [3],[13],[2],[10],[8]$ - minimum of windows - $3,13,2,10,8$ - maximum value  - $13$.

Windows of size $2 - [3,13], [13,2], [2,10], [10,8]$ - minimum of windows - $3,2,2,8$ - maximum value  - $8$.

Windows of size $3 - [3,13,2], [13,2,10], [2,10,8]$ - minimum of windows - $2,2,2$ - maximum value  - $2$.

Windows of size $4 - [3,13,2,10], [13,2,10,8]$ - minimum of windows - $2,2$ - maximum value  - $2$.

Windows of size $5 - [3,13,2,10,8]$ - minimum of windows - $2$ - maximum value  - $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
7 18 16
```

**Output for this case**

```text
18 16 7
```



#### Test case 2

**Input for this case**

```text
5
3 13 2 10 8
```

**Output for this case**

```text
13 8 2 2 2
```



#### Test case 3

**Input for this case**

```text
5
17 9 13 7 12
```

**Output for this case**

```text
17 9 9 7 7
```



#### Test case 4

**Input for this case**

```text
7
4 8 10 16 14 19 3
```

**Output for this case**

```text
19 14 14 10 8 4 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Maximum of Minimum for Every Window Size

In this lesson, we discuss an optimal approach to solve the “Maximum of Minimum for Every Window Size” problem. In this problem, you are given an array $A$ of size $N$. For every window size from $1$ to $N$, your task is to find the maximum among the minimum values of all windows of that size. The method described below is designed to achieve this efficiently.

---

## Optimal Stack-Based Method

**Idea:**
The optimal solution utilizes the concept of **next smaller** and **previous smaller** elements. This approach determines, for each element, the maximum window size in which it can serve as the minimum. Instead of iterating over all possible window sizes, we preprocess the array using stacks to figure out how far each element can extend as the minimum, which leads to an overall time complexity of $$ O(N) $$.

**Algorithm:**
- **Step 1:** For every index $i$, determine:
  - **Previous smaller element index ($L[i]$):** The index of the closest element to the left of $i$ with a value less than $A[i]$. If no such element exists, set $L[i] = -1$.
  - **Next smaller element index ($R[i]$):** The index of the closest element to the right of $i$ with a value less than $A[i]$. If no such element exists, set $R[i] = N$.
- **Step 2:** For every index $i$, compute the length of the window in which $A[i]$ is the minimum as:

  $$ \text{len} = R[i] - L[i] - 1 $$

- **Step 3:** Construct an array $$ \text{max\_of\_min} $$ where the value at index $len$ is the maximum value among all $A[i]$ that can serve as the minimum for a window of size $len$.
- **Step 4:** Traverse the $$ \text{max\_of\_min} $$ array in reverse to fill in any gaps, ensuring that for all smaller window sizes, the maximum value is at least as high as what was computed for larger windows.

**Time Complexity:**
This method runs in $$ O(N) $$ time due to its efficient use of stacks.

**C++ Code:**
```cpp
#include
#include
#include
#include
using namespace std;

vector solve(const vector& arr) {
    int n = arr.size();
    vector left(n), right(n);
    stack st;

    // Compute previous smaller elements
    for (int i = 0; i < n; i++) {
        while (!st.empty() && arr[st.top()] >= arr[i])
            st.pop();
        left[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }
    while (!st.empty())
        st.pop();

    // Compute next smaller elements
    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && arr[st.top()] >= arr[i])
            st.pop();
        right[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    vector max_of_min(n + 1, 0);
    // Fill in the maximum for each window length
    for (int i = 0; i < n; i++) {
        int len = right[i] - left[i] - 1;
        max_of_min[len] = max(max_of_min[len], arr[i]);
    }
    // Propagate the maximum to smaller window sizes
    for (int i = n - 1; i >= 1; i--) {
        max_of_min[i] = max(max_of_min[i], max_of_min[i + 1]);
    }
    return vector(max_of_min.begin() + 1, max_of_min.end());
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector arr(n);
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }
        vector result = solve(arr);
        for (int val : result)
            cout << val << " ";
        cout << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
def max_of_min(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    st = []

    # Previous smaller element
    for i in range(n):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        left[i] = st[-1] if st else -1
        st.append(i)

    st.clear()

    # Next smaller element
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        right[i] = st[-1] if st else n
        st.append(i)

    max_of_min_arr = [0] * (n + 1)
    for i in range(n):
        length = right[i] - left[i] - 1
        max_of_min_arr[length] = max(max_of_min_arr[length], arr[i])

    # Propagate maximum values to smaller window sizes
    for i in range(n - 1, 0, -1):
        max_of_min_arr[i] = max(max_of_min_arr[i], max_of_min_arr[i + 1])

    return max_of_min_arr[1:]

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = max_of_min(arr)
    print(" ".join(map(str, res)))
```

---

## Summary

The **Optimal Stack-Based Method** is the most efficient solution for the problem. By leveraging stacks to compute both the next and previous smaller elements for each array entry, we achieve an overall time complexity of $$ O(N) $$. This makes the approach highly scalable and suitable for large inputs.

Happy coding!

</details>
