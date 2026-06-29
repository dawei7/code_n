# Even-Max

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVNMX |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [EVNMX](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/EVNMX) |

---

## Problem Statement

Given an array $A$ of $N$ integers and an integer $k$, Help us find the first even number in every subarray of $A$ of length $k$.

---

## Input Format

First Line would have the number $N$ , $k$ signifying the amount of numbers and length of the subarray separated by a space.
The second Line contains $N$ numbers separated by a space.

---

## Output Format

Output the cost of the bunch , if there is no even number output $-1$

---

## Constraints

- $1 \leq k  \leq N \leq 10^5$
- $1 \leq number[i] \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4 2
12 32 43 23
```

**Output**

```text
12 32 -1
```

**Explanation**

In the first window of 2 numbers [12,32] , the first even number is 12 , similarly in the second window,[32,43] , 32 is the first even number, and in the third window, [43,23], there is no even number

**Example 2**

**Input**

```text
3 2
1 5 2
```

**Output**

```text
-1 2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore how to solve the problem of finding the first even number in every subarray (or window) of size $k$ from a given array $A$. We will discuss two different approaches to understand the trade-offs in complexity and clarity. Each approach is explained in detail with both C++ and Python implementations.

---

### Approach 1: Brute Force

**Idea:**
For each subarray (window) of length $k$, iterate over the window elements from left to right. Check each element, and if it is even, output that number and break out of the loop. If no even number is found in the window, output $-1$.

**Explanation:**
1. Iterate over all windows. There are $N-k+1$ windows if $N$ is the array size.
2. For each window, scan through its $k$ elements.
3. **Time complexity:** In the worst-case scenario, every window may require scanning $k$ elements, giving a complexity of $$O((N-k+1) \times k).$$
   This approach is straightforward but can be inefficient for large values of $N$ and $k$.

**C++ Code for Brute Force:**
```cpp
#include
#include
using namespace std;

vector firstEvenBruteForce(const vector& arr, int k) {
    int n = arr.size();
    vector result;
    for (int i = 0; i <= n - k; i++) {
        int firstEven = -1;
        for (int j = i; j < i + k; j++) {
            if (arr[j] % 2 == 0) {
                firstEven = arr[j];
                break;
            }
        }
        result.push_back(firstEven);
    }
    return result;
}

int main() {
    int N, k;
    cin >> N >> k;
    vector arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector result = firstEvenBruteForce(arr, k);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```

**Python Code for Brute Force:**
```python
def first_even_brute_force(arr, k):
    n = len(arr)
    result = []
    for i in range(n - k + 1):
        first_even = -1
        for j in range(i, i + k):
            if arr[j] % 2 == 0:
                first_even = arr[j]
                break
        result.append(first_even)
    return result

if __name__ == "__main__":
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = first_even_brute_force(arr, k)
    print(" ".join(map(str, result)))
```

---

### Approach 2: Sliding Window with Queue

**Idea:**
We can optimize the process by using a queue that stores the indices of even numbers in the array. As we slide the window:
- Add indices of even numbers to the queue.
- Remove indices that fall out of the current window.
- The front of the queue will always correspond to the first even number in the window.

**Explanation:**
1. Traverse the array once, maintaining a queue (or similar data structure) to store indices of even numbers.
2. For index $i$, if $A[i]$ is even, add $i$ to the queue.
3. When you have traversed at least $k-1$ indices (i.e., the current window is complete), check if the front index of the queue is still within the window boundaries. If not, remove it.
4. If the queue is not empty, its front element is the first even in the window; otherwise, output $-1$.
5. This implementation processes each element efficiently, leading to an overall time complexity of $$O(N).$$

**C++ Code for Sliding Window with Queue:**
```cpp
#include
#include
#include
using namespace std;

vector firstEvenSlidingWindow(const vector& arr, int k) {
    int n = arr.size();
    vector result;
    queue evenIndices;

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            evenIndices.push(i);
        }

        if (i >= k - 1) {
            // Remove indices that are out of the current window
            while (!evenIndices.empty() && evenIndices.front() <= i - k) {
                evenIndices.pop();
            }

            if (evenIndices.empty()) {
                result.push_back(-1);
            } else {
                result.push_back(arr[evenIndices.front()]);
            }
        }
    }
    return result;
}

int main() {
    int N, k;
    cin >> N >> k;
    vector arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector result = firstEvenSlidingWindow(arr, k);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```

**Python Code for Sliding Window with Queue:**
```python
from collections import deque

def first_even_sliding_window(arr, k):
    n = len(arr)
    result = []
    even_indices = deque()

    for i in range(n):
        # If the number is even, add its index to the deque
        if arr[i] % 2 == 0:
            even_indices.append(i)

        # Check if we have a complete window
        if i >= k - 1:
            # Remove indices that are out of the current window
            while even_indices and even_indices[0] <= i - k:
                even_indices.popleft()

            if even_indices:
                result.append(arr[even_indices[0]])
            else:
                result.append(-1)

    return result

if __name__ == "__main__":
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = first_even_sliding_window(arr, k)
    print(" ".join(map(str, result)))
```

---

### Summary

- **Brute Force** is simple to understand but inefficient with a worst-case time complexity of $$O((N-k+1) \times k).$$
- **Sliding Window with Queue** optimizes the solution by processing each element efficiently, leading to an overall time complexity of $$O(N).$$

Each approach has been explained along with code samples in C++ and Python to help you understand the problem’s various solutions. As a beginner, you should start with understanding the brute-force method and then move on to the more efficient sliding window technique.

Happy Coding!

</details>
