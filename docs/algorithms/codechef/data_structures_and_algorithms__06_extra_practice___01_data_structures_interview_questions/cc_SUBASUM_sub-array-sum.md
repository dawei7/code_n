# Sub-array Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBASUM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [SUBASUM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/SUBASUM) |

---

## Problem Statement

Given an array $A$ of integers of length $N$. Find the sum of difference between maximum and minimum elements of all sub-arrays. Formally, find the value of the following expression :
$\sum\limits_{i=1}^{N}\sum\limits_{j=i}^{N} max(A_i, A_{i + 1} . . . A_j) - min(A_i, A_{i + 1} . . . A_j)$

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains a single integer $N$.
- Second line of each testcase contains of $N$ integers : $A_1, A_2 . . . A_N$.

---

## Output Format

For each testcase, output a single integer equal to the value of given expression.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$

It is guaranteed that the sum of values of $N$ over all the test cases doesn't exceed $2*10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
3
1 4 9
3
5 5 5
```

**Output**

```text
16
0
```

**Explanation**

**Test-case 1:**
Consider all the sub-arrays of given array
- [1]
- [1, 4]
- [1, 4, 9]
- [4]
- [4, 9]
- [9]

The desired value = $(1 - 1) + (4 - 1) + (9 - 1) + (4 - 4) + (9 - 4) + (9 - 9) = 16$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 4 9
```

**Output for this case**

```text
16
```



#### Test case 2

**Input for this case**

```text
3
5 5 5
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Sum of Differences in All Subarrays

In this lesson, we focus on an efficient approach to solve the problem of finding the sum of differences between the maximum and minimum elements for every subarray of a given array. We employ the **Monotonic Stack (Contribution Technique)**, which is both intuitive and efficient for large inputs.

---

## Monotonic Stack (Contribution Technique)

### Idea
Each element in the array can serve as the maximum or minimum in several subarrays. We calculate its contribution to the overall sum by counting the number of subarrays in which it appears as the unique maximum (and similarly, as the unique minimum). The final answer is calculated as:
$$
\text{result} = \sum_{i = 0}^{N-1} \Big( A[i] \times \text{count}_{\text{max}}(i) - A[i] \times \text{count}_{\text{min}}(i) \Big)
$$
where
$$
\text{count}_{\text{max}}(i) = (i - \text{prevGreater}[i]) \times (\text{nextGreater}[i] - i)
$$
with a similar formula for $\text{count}_{\text{min}}(i)$.

### Methodology
1. **Monotonic Stack Usage:**
   - Use a **monotonic decreasing stack** to compute the **Next Greater** and **Previous Greater** indices.
   - Use a **monotonic increasing stack** to compute the **Next Smaller** and **Previous Smaller** indices.
2. **Contribution Calculation:**
   - For each element, compute its contribution as a maximum and as a minimum using the formulas derived from its span of influence.
3. **Summing Contributions:**
   - Sum up the differences between the maximum and minimum contributions for all elements to obtain the final result.

**Complexity:**
This approach runs in $O(n)$ time per test case, making it highly efficient for large inputs.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

long long sumOfDifferences(vector& A) {
    int n = A.size();
    long long result = 0;

    vector nextSmaller(n, n), nextGreater(n, n), prevSmaller(n, -1), prevGreater(n, -1);
    stack s;

    // Next Smaller
    for (int i = 0; i < n; i++) {
        while (!s.empty() && A[s.top()] > A[i]) {
            nextSmaller[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }
    while (!s.empty()) s.pop();

    // Next Greater
    for (int i = 0; i < n; i++) {
        while (!s.empty() && A[s.top()] < A[i]) {
            nextGreater[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }
    while (!s.empty()) s.pop();

    // Previous Smaller
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && A[s.top()] >= A[i]) {
            prevSmaller[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }
    while (!s.empty()) s.pop();

    // Previous Greater
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && A[s.top()] <= A[i]) {
            prevGreater[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }

    for (int i = 0; i < n; i++) {
        long long contribMax = static_cast(A[i]) * (i - prevGreater[i]) * (nextGreater[i] - i);
        long long contribMin = static_cast(A[i]) * (i - prevSmaller[i]) * (nextSmaller[i] - i);
        result += contribMax - contribMin;
    }

    return result;
}

int main(){
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
        cout << sumOfDifferences(A) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
import sys
input = sys.stdin.readline

def sum_of_differences(A):
    n = len(A)
    res = 0
    next_smaller = [n] * n
    prev_smaller = [-1] * n
    next_greater = [n] * n
    prev_greater = [-1] * n
    stack = []

    # Next Smaller
    for i in range(n):
        while stack and A[stack[-1]] > A[i]:
            next_smaller[stack.pop()] = i
        stack.append(i)
    stack.clear()

    # Next Greater
    for i in range(n):
        while stack and A[stack[-1]] < A[i]:
            next_greater[stack.pop()] = i
        stack.append(i)
    stack.clear()

    # Previous Smaller
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            prev_smaller[stack.pop()] = i
        stack.append(i)
    stack.clear()

    # Previous Greater
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] <= A[i]:
            prev_greater[stack.pop()] = i
        stack.append(i)

    for i in range(n):
        count_max = (i - prev_greater[i]) * (next_greater[i] - i)
        count_min = (i - prev_smaller[i]) * (next_smaller[i] - i)
        res += A[i] * count_max - A[i] * count_min
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(sum_of_differences(arr))
```

---

## Conclusion

The **Monotonic Stack (Contribution Technique)** provides an elegant and efficient solution with a linear runtime, making it ideal for handling large inputs. By computing the contribution of each element as it serves as a maximum and a minimum across subarrays, we achieve an optimal solution.

Understanding and mastering this approach will equip you to efficiently tackle similar problems in algorithm design. Happy coding!

</details>
