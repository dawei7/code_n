# Attack on Kingdom

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KNGATK |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [KNGATK](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/KNGATK) |

---

## Problem Statement

Nightking wants to attack the kingdom and he really likes cold days. However, he
doesn’t want to attack the kingdom on the coldest day, because it is obvious.

Instead, he will attack the second coldest day.
Given an array $A$ of $N$ **distinct** integers where $A_i$ represents the temperature forecast of the $i$-th day, You need to find the temperature of the day of the attack.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the number of days
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the temperature forecast of the $i$-th day.

---

## Output Format

For each test case, output in a single line - the answer to the $i$-th test case.

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
3
2
1 2
3
7 4 9
5
45 76 91 21 9
```

**Output**

```text
2
7
21
```

**Explanation**

- **Test Case $1$**: There are only $2$ days, so the night king will attack the day with a higher temperature.
- **Test Case $3$**: Out of the $5$ possible days, Night King will attack the day with the 2nd lowest temperature, therefore $21$ will be the answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
7 4 9
```

**Output for this case**

```text
7
```



#### Test case 3

**Input for this case**

```text
5
45 76 91 21 9
```

**Output for this case**

```text
21
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Finding the Second Coldest Day: A Detailed Editorial

In this lesson, we focus on solving the problem of finding the temperature on the second coldest day. We are given an array $A$ of $N$ **distinct** integers where each $A_i$ represents the forecasted temperature of day $i$. Our goal is to determine the second smallest element in the array.

Since the temperatures in the array are distinct, there is no ambiguity in identifying the second smallest element. Let’s explore three different approaches to solve this problem and analyze their efficiency.

---

## Approaches to the Problem

### 1. Sorting Approach

**Idea:**
In the sorting approach, we first sort the array. Once sorted in non-decreasing order, the second element (index $1$, if we use $0$-indexing) will be the second smallest element.

**Complexity:**
The sorting operation takes $$O(N \log N)$$ time, which is sufficient given the constraints.

**Explanation:**
- **Step 1:** Sort the array $A$.
- **Step 2:** The element at index $1$ is the second smallest element.

This approach is straightforward and easy to implement, making it a good option for beginners.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }
        // Sort the array
        sort(A.begin(), A.end());
        // The second smallest element is the second element in the sorted array
        cout << A[1] << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    # Sort the array
    A.sort()
    # The second smallest element is at index 1
    print(A[1])
```

---

### 2. Single-Pass Approach

**Idea:**
Use a single iteration over the array while maintaining two variables $min_1$ and $min_2$ which store the smallest and the second smallest elements, respectively.

**Methodology:**
- Initialize $$min\_1$$ and $$min\_2$$ to a very high value (use infinity or the maximum possible integer).
- For each element in the array:
  - If the element is less than $$min\_1$$, update $$min\_2$$ to $$min\_1$$ and then set $$min\_1$$ to the element.
  - Otherwise, if the element is less than $$min\_2$$, update $$min\_2$$.

**Complexity:**
This approach runs in $$O(N)$$ time, making it more efficient than sorting for this particular task.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }
        int min1 = numeric_limits::max();
        int min2 = numeric_limits::max();
        for (int i = 0; i < N; i++) {
            int num = A[i];
            if (num < min1) {
                min2 = min1;
                min1 = num;
            } else if (num < min2) {
                min2 = num;
            }
        }
        cout << min2 << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
import math
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    min1 = math.inf
    min2 = math.inf
    for num in A:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    print(min2)
```

---

### 3. Heap Approach

**Idea:**
This method uses a min-heap (or priority queue) to easily extract the smallest elements. By converting the array into a min-heap, we can remove the smallest element and then read the next element from the heap as the second smallest.

**Methodology:**
- **Step 1:** Convert the array into a min-heap.
- **Step 2:** Pop the smallest element from the heap.
- **Step 3:** The element now at the top of the min-heap is the second smallest element.

**Complexity:**
Building the min-heap takes $$O(N)$$ time, and each pop operation takes $$O(\log N)$$, making this approach efficient for the given input size.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        priority_queue, greater> minHeap;
        for (int i = 0; i < N; ++i) {
            int temp;
            cin >> temp;
            minHeap.push(temp);
        }
        // Pop the smallest element (coldest day)
        minHeap.pop();
        // Now, the top element is the second coldest day
        cout << minHeap.top() << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
import heapq
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    heapq.heapify(A)  # Convert list to a min-heap
    # Pop the smallest element
    heapq.heappop(A)
    # Next element is the second smallest
    print(heapq.heappop(A))
```

---

## Summary

We explored three effective approaches to determine the second coldest day:

- **Sorting Approach:** Sort the array and pick the element at index $1$.
  - **Time Complexity:** $$O(N \log N)$$
- **Single-Pass Approach:** Traverse the array once to find the smallest and second smallest element.
  - **Time Complexity:** $$O(N)$$
- **Heap Approach:** Use a min-heap to extract the two smallest elements.
  - **Time Complexity:** $$O(N)$$ (for heapify) plus $$O(\log N)$$ per extraction

For beginners, the sorting approach is intuitive and easy to implement. The single-pass approach is optimal in time complexity, while the heap approach offers an alternative method using data structures.

Choose the approach that best fits your understanding and the problem constraints.

Happy coding!

</details>
