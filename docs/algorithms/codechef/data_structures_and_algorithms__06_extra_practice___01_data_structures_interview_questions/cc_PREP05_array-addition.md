# Array - Addition

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP05 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PREP05](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/PREP05) |

---

## Problem Statement

You are given an array $A$ of $N$ integers. You need to output the **maximum possible sum** of any contiguous subarray of $A$ containing **non-negative** numbers only.

Note: A contiguous subarray is obtained by deletion of several (possibly zero) elements from the beginning of the array and several (possibly zero) elements from the end of the array. If there is no sub-array containing only non-negative numbers, then print $0$.

Note: The answer may be larger than $32$ bits.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains $N$ — the length of array $A$.
    - The second line of each test case contains $N$ space-separated integers - the elements of array $A$.

---

## Output Format

For each test case, output on a new line the maximum possible sum of any contiguous subarray of $A$ containing non-negative numbers only.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5
1 2 3 4 5
5
10 -1 -2 -3 10
5
10 0 8 -6 10
2
-5 -10
```

**Output**

```text
15
10
18
0
```

**Explanation**

**Test case $1$**: The sub-array $[1, 2, 3, 4, 5]$ gives us the sum $15$.

**Test case $2$**: The sub-array $[10]$ gives us the sum $10$.

**Test case $3$**: The sub-array $[10, 0, 8]$ gives us the sum $18$.

**Test case $4$**: There is no sub-array containing non-negative numbers only.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
5
10 -1 -2 -3 10
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
5
10 0 8 -6 10
```

**Output for this case**

```text
18
```



#### Test case 4

**Input for this case**

```text
2
-5 -10
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Editorial: Maximum Sum Non-Negative Subarray

In this lesson, we will solve the problem of finding the maximum possible sum of any contiguous subarray that contains **non-negative** numbers only. This problem is a great exercise for understanding how to iterate through arrays and manage subarrays efficiently.

In our discussion, we will cover three distinct approaches:

---

### Approach 1: Single Pass Iteration

In this approach, we traverse the array once and maintain two variables:
- $ {\textbf{currentSum}} $ represents the sum of contiguous non-negative numbers encountered so far.
- $ {\textbf{maxSum}} $ stores the maximum sum encountered.

For each element $ {x} $ in the array:
- If $ {x} $ is non-negative, we add it to $ {\textbf{currentSum}} $ and update $ {\textbf{maxSum}} $ if needed.
- If $ {x} $ is negative, we reset $ {\textbf{currentSum}} $ to $ {0} $.

This approach runs in $ {O(N)} $ time complexity, making it very efficient.

#### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

long long maxSumNonNegativeSubarray(vector& A) {
    long long maxSum = 0, currentSum = 0;
    for (int num : A) {
        if(num >= 0) {
            currentSum += num;
            maxSum = max(maxSum, currentSum);
        } else {
            currentSum = 0;
        }
    }
    return maxSum;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << maxSumNonNegativeSubarray(A) << "\n";
    }
    return 0;
}
```

#### Python Implementation

```python
def max_sum_non_negative_subarray(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        if num >= 0:
            current_sum += num
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = 0
    return max_sum

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_non_negative_subarray(arr))
```

---

### Approach 2: Iterative Segmentation on Negative Encounter

This approach is conceptually similar to Approach 1 but handles segments more explicitly:
- As we iterate over the array, we add non-negative numbers to $ {\textbf{currentSum}} $.
- When a negative number is encountered, we update $ {\textbf{maxSum}} $ using the current segment sum and then reset $ {\textbf{currentSum}} $.

At the end of the iteration, we ensure to update $ {\textbf{maxSum}} $ one last time if the final segment is non-negative.

#### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

long long maxSumUsingSegmentation(vector& A) {
    long long maxSum = 0, currentSum = 0;
    for (int num : A) {
        if(num >= 0) {
            currentSum += num;
        } else {
            maxSum = max(maxSum, currentSum);
            currentSum = 0;
        }
    }
    maxSum = max(maxSum, currentSum);
    return maxSum;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << maxSumUsingSegmentation(A) << "\n";
    }
    return 0;
}
```

#### Python Implementation

```python
def max_sum_segmentation(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        if num >= 0:
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    max_sum = max(max_sum, current_sum)
    return max_sum

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_segmentation(arr))
```

---

### Approach 3: Building Segments

In this approach, we explicitly build segments of contiguous non-negative numbers, store their sums, and then select the maximum:
- Iterate over the entire array and add non-negative numbers to a temporary sum.
- Upon encountering a negative number, append the temporary sum to a list of segments and reset the sum.
- Finally, compute the maximum segment sum.

This method may use extra space to store the segments but makes the segmentation process clear.

#### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

long long maxSumByBuildingSegments(vector& A) {
    vector segments;
    long long currentSum = 0;
    for (int num : A) {
        if(num >= 0) {
            currentSum += num;
        } else {
            segments.push_back(currentSum);
            currentSum = 0;
        }
    }
    segments.push_back(currentSum);
    long long maxSum = 0;
    for (long long seg : segments) {
        maxSum = max(maxSum, seg);
    }
    return maxSum;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        cout << maxSumByBuildingSegments(A) << "\n";
    }
    return 0;
}
```

#### Python Implementation

```python
def max_sum_by_building_segments(arr):
    segments = []
    current_sum = 0
    for num in arr:
        if num >= 0:
            current_sum += num
        else:
            segments.append(current_sum)
            current_sum = 0
    segments.append(current_sum)
    return max(segments) if segments else 0

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_by_building_segments(arr))
```

---

All three approaches efficiently solve the problem in $O(N)$ time per test case. Depending on your preference, you can choose the method which best aligns with your thinking style. The first approach provides an immediate update method, the second emphasizes understanding segment boundaries, and the third explicitly constructs segments from which the maximum can be derived.

Happy coding and good luck with your DSA interviews!

</details>
