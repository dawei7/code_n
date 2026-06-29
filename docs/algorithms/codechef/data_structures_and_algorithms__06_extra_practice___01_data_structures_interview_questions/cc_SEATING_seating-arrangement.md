# Seating Arrangement

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEATING |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SEATING](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/SEATING) |

---

## Problem Statement

You are given an array $A$ of size $N$ containing integers representing that the seats are located at $(A_i,0)$ coordinate. You have to allocate $1$ seat each for $Arup$, $Aman$ and $Rahul$ such that the sum of time required for each of them to meet the other two (i.e. the sum of time required for $Arup$ to meet $Aman$, $Arup$ to meet $Rahul$, $Rahul$ to meet $Aman$, $Rahul$ to meet $Arup$, $Aman$ to meet $Arup$, $Aman$ to meet $Rahul$ ) is maximum, given that you can walk at a speed of $1$ unit distance per unit time in any direction. Print the sum of time required for each of them to meet the other two.

---

## Input Format

- The first line contains an integer $T$ , representing $T$ test cases.

- First line of each test case contains an integer $N$ , representing the size of array $A$.

- Second line of each test case contains $N$ integers , representing array $A$.

---

## Output Format

- For each test case , print a single integer representing the sum of time required for each of them to meet the other two .

---

## Constraints

- $1 \le T \le 100$

- $3 \le N \le 100000$

- $-10^9 \le A_i \le 10^9$

- Sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
3
-5 0 5
4 
-1 -3 2 4
5
-100000 0 100000 -1000000 1000000
```

**Output**

```text
40
28
8000000
```

**Explanation**

In the first test case $Arup$, $Aman$ and $Rahul$ are seated at coordinates $\{(-5,0),(0,0),(5,0)\}$ seats respectively.

In the second test case one of the possible seating arrangements for $Arup$, $Aman$ and $Rahul$ can be $\{(2,0),(-3,0),(4,0)\}$ respectively.

In the third test case one of the possible seating arrangements for $Arup$, $Aman$ and $Rahul$ can be $\{(-1000000,0),(1000000,0),(0,0)\}$ respectively.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
-5 0 5
```

**Output for this case**

```text
40
```



#### Test case 2

**Input for this case**

```text
4
-1 -3 2 4
```

**Output for this case**

```text
28
```



#### Test case 3

**Input for this case**

```text
5
-100000 0 100000 -1000000 1000000
```

**Output for this case**

```text
8000000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given an array $A$ of size $N$, where each element represents the $x$-coordinate of a seat (with the $y$-coordinate being zero). Our goal is to allocate three seats (one for each person: Arup, Aman, and Rahul) such that the sum of the pairwise meeting times is maximized. Since they can walk at a speed of $1$ unit per unit time, the meeting time is exactly the distance between the seats. Note that the meeting time between two persons is counted twice (once for each direction).

The key insight is the following: if we denote the chosen seat coordinates as $a$, $b$, and $c$ (with $a \le b \le c$), then the distances between them are:
$$
|b - a|,\quad |c - b|,\quad |c - a|
$$
The total time (summing each pair twice) is:
$$
2\bigl((b-a) + (c-b) + (c-a)\bigr)
$$
Notice that:
$$
(b - a) + (c - b) + (c - a) = 2(c - a)
$$
Therefore, the total time becomes:
$$
2 \times 2(c - a) = 4(c - a)
$$
Thus, to maximize the meeting time, we should allocate the seats at the extreme positions (i.e. the smallest and largest coordinates) and pick any seat in between (or even one of the extremes again if duplicates exist). In other words, if $A_{\text{min}}$ is the minimum value and $A_{\text{max}}$ is the maximum value in the array, then the answer is:
$$
4 \times (A_{\text{max}} - A_{\text{min}})
$$

Below, we discuss three approaches to solve the problem along with code implementations in both C++ and Python.

---

### **Approach 1: Sorting the Array**

**Idea:**

1. **Sort** the array $A$.
2. The first element will be $A_{\text{min}}$, and the last element will be $A_{\text{max}}$.
3. Calculate the answer as:
   $$
   4 \times (A_{\text{max}} - A_{\text{min}})
   $$

Both C++ and Python implementations are provided below.

**C++ Implementation:**
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
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        sort(A.begin(), A.end());
        long long answer = (long long)(A[N - 1] - A[0]) * 4;
        cout << answer << endl;
    }
    return 0;
}
```

**Python Implementation:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    answer = (A[-1] - A[0]) * 4
    print(answer)
```

---

### **Approach 2: Single-Pass Iteration for Minimum and Maximum**

**Idea:**

1. Iterate through the array without sorting.
2. Keep track of the minimum value $A_{\text{min}}$ and the maximum value $A_{\text{max}}$.
3. Compute the answer using:
   $$
   4 \times (A_{\text{max}} - A_{\text{min}})
   $$

This approach runs in $\mathcal{O}(N)$ time and is efficient for large arrays.

**C++ Implementation:**
```cpp
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        int first;
        cin >> first;
        int minVal = first, maxVal = first;
        for (int i = 1; i < N; i++) {
            int x;
            cin >> x;
            if (x < minVal) minVal = x;
            if (x > maxVal) maxVal = x;
        }
        long long answer = (long long)(maxVal - minVal) * 4;
        cout << answer << endl;
    }
    return 0;
}
```

**Python Implementation:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    min_val = A[0]
    max_val = A[0]
    for x in A:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    answer = (max_val - min_val) * 4
    print(answer)
```

---

### **Approach 3: Using Built-in Functions**

**Idea:**

1. Use built-in functions to directly obtain the minimum and maximum values from the array.
2. In C++, utilize `std::minmax_element`.
3. In Python, use `min()` and `max()`.

This approach simplifies the code and leverages language features.

**C++ Implementation:**
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
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        auto result = minmax_element(A.begin(), A.end());
        long long answer = (long long)(*result.second - *result.first) * 4;
        cout << answer << endl;
    }
    return 0;
}
```

**Python Implementation:**
```python
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    answer = (max(A) - min(A)) * 4
    print(answer)
```

---

### **Summary**

- **Approach 1 (Sorting):** Sort the array and pick the extremes. This approach runs in $\mathcal{O}(N \log N)$ time.
- **Approach 2 (Single-Pass Iteration):** Directly iterate to find the minimum and maximum values in $\mathcal{O}(N)$ time.
- **Approach 3 (Built-in Functions):** Leverage built-in functions (or library routines) to get the extremes, resulting in concise and clear code.

All approaches ultimately compute the final result as:
$$
\text{Answer} = 4 \times (A_{\text{max}} - A_{\text{min}})
$$
which maximizes the total meeting time when the three seats are allocated.

</details>
