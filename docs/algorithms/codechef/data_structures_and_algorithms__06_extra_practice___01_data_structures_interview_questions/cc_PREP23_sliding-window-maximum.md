# Sliding Window Maximum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP23 |
| Difficulty Rating | 1600 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [PREP23](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/PREP23) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ integers and an integer $X$.

Find the **maximum** element in each subarray of size $X$.
Print $(N-X+1)$ space-separated integers where the $i^{th}$ integer denotes the maximum element of the $i^{th}$ subarray of size $X$ from left.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of elements in the array and the size of subarrays.
    - The next line contains $N$ space-separated integers, the elements of array $A$.

---

## Output Format

For each test case, output on a new line, the **maximum** element in each subarray of size $X$.
Print $(N-X+1)$ space-separated integers where the $i^{th}$ integer denotes the maximum element of the $i^{th}$ subarray of size $X$ from left.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4 2
1 2 3 4
4 3
4 3 2 1
3 1
9 7 10
```

**Output**

```text
2 3 4
4 3
9 7 10
```

**Explanation**

**Test case $1$:** For the array $A = [1, 2, 3, 4]$:
- The maximum element in the subarray $[1, 2]$ is $2$.
- The maximum element in the subarray $[2, 3]$ is $3$.
- The maximum element in the subarray $[3, 4]$ is $4$.

Note that the subarrays are traverses from left to right.

**Test case $2$:** For the array $A = [4, 3, 2, 1]$:
- The maximum element in the subarray $[4, 3, 2]$ is $4$.
- The maximum element in the subarray $[3, 2, 1]$ is $3$.

**Test case $3$:** For the array $A = [9, 7, 10]$:
- The maximum element in the subarray $[9]$ is $9$.
- The maximum element in the subarray $[7]$ is $7$.
- The maximum element in the subarray $[10]$ is $10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
1 2 3 4
```

**Output for this case**

```text
2 3 4
```



#### Test case 2

**Input for this case**

```text
4 3
4 3 2 1
```

**Output for this case**

```text
4 3
```



#### Test case 3

**Input for this case**

```text
3 1
9 7 10
```

**Output for this case**

```text
9 7 10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss the problem of finding the maximum element in each subarray (or window) of size $X$ in an array of $N$ integers. The window slides from the beginning of the array to the end, and for each position, we output the maximum value contained within that window. We will explore two distinct approaches to solve this problem:

---

## Approach 1: Priority Queue (Max Heap) Method

### Explanation
In this approach, we utilize a max heap (priority queue) to efficiently track the maximum element within the current window. For each element at index $i$, we push a pair consisting of the element value and its index. Once we have formed a complete window (when $i \geq X - 1$), we ensure that the element at the top of the heap belongs to a valid index within the current window. If the index at the top is out of the window’s range (i.e., less than $i - X + 1$), we pop it out. This method generally has a time complexity of
$$ O(N \log X), $$
which offers a good balance between simplicity and performance.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--){
        int N, X;
        cin >> N >> X;
        vector A(N);
        for (int i = 0; i < N; i++)
            cin >> A[i];

        priority_queue> pq;
        vector result;

        for (int i = 0; i < N; i++) {
            // Push the current element and its index
            pq.push({A[i], i});

            // Start outputting after we have a valid full window
            if (i >= X - 1) {
                // Remove elements that are not in the current window.
                while(pq.top().second <= i - X) {
                    pq.pop();
                }
                result.push_back(pq.top().first);
            }
        }

        for(auto val: result) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}
```

#### Python Code

```python
import heapq

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    heap = []  # will store (-value, index) to simulate max heap
    result = []

    for i in range(N):
        heapq.heappush(heap, (-A[i], i))

        if i >= X - 1:
            # Ensure the max element is within the current window.
            while heap[0][1] <= i - X:
                heapq.heappop(heap)
            result.append(-heap[0][0])

    print(" ".join(map(str, result)))
```

---

## Approach 2: Deque (Optimal) Method

### Explanation
This is the most optimal approach, achieving a time complexity of
$$ O(N). $$
We use a double-ended queue (deque) to maintain a list of indices, with the property that the values corresponding to these indices are in **decreasing** order. For each new element at index $i$:
1. **Remove Out-of-Window Elements:** If the index at the front of the deque is out of the current window (i.e., if it equals $i - X$), remove it.
2. **Maintain Monotonicity:** Remove indices from the back of the deque while the corresponding elements are less than the current element, because these values will never be the maximum for the current or any future window.
3. **Add Current Element:** Append the current index at the back of the deque.
4. **Record Maximum:** For every complete window (when $i \geq X - 1$), the element at the front of the deque is the maximum for that window.

### Code Implementation

#### C++ Code

```cpp
#include
#include
#include
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
       int N, X;
       cin >> N >> X;
       vector A(N);
       for (int i = 0; i < N; i++)
           cin >> A[i];

       deque dq;
       vector result;

       for (int i = 0; i < N; i++){
           // Remove indices out of the current window
           if (!dq.empty() && dq.front() == i - X) {
               dq.pop_front();
           }

           // Maintain the decreasing order
           while (!dq.empty() && A[dq.back()] < A[i]) {
               dq.pop_back();
           }

           dq.push_back(i);

           // Once the first window is formed, record the maximum
           if (i >= X - 1) {
               result.push_back(A[dq.front()]);
           }
       }

       for (auto val: result) {
           cout << val << " ";
       }
       cout << endl;
    }
    return 0;
}
```

#### Python Code

```python
from collections import deque

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    dq = deque()
    result = []

    for i in range(N):
        # Remove indices that are out of the current window
        if dq and dq[0] == i - X:
            dq.popleft()

        # Maintain elements in decreasing order in the deque
        while dq and A[dq[-1]] < A[i]:
            dq.pop()

        dq.append(i)

        # Once the window is full, record the maximum element
        if i >= X - 1:
            result.append(A[dq[0]])

    print(" ".join(map(str, result)))
```

---

## Summary

- **Priority Queue (Max Heap):** Offers a time complexity of $$ O(N \log X), $$ providing a good balance between simplicity and performance.
- **Deque (Optimal):** The best approach with a linear time complexity of $$ O(N), $$ making it optimal for large inputs.

Understanding these approaches will help you design efficient algorithms not only for this specific problem but also for a wide range of challenges in competitive programming and technical interviews.

</details>
