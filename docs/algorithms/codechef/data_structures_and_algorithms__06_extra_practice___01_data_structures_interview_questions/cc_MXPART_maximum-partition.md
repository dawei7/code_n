# Maximum Partition

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXPART |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MXPART](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/MXPART) |

---

## Problem Statement

Chef will give you an array $A$ of length $N$ which is a **permutation**. You can split the given array into some number of partitions, individually sort each subarray and join them back together without changing their relative order. After concatenating them, the result should a the sorted array. Find the ***maximum***  number of partitions we can make.

**Note:** A permutation is an array consisting of $N$ **distinct** integers from $1$ to $N$ in **arbitrary** order.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the length of the array.
- The second line of each test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers of the array.

---

## Output Format

For each testcase, output in a single line - the maximum number of partitions possible.

---

## Constraints

- $1 \leq T \leq 1500$
- $1 \leq N \leq 2\cdot 10^5, \sum N \leq 5\cdot10^5$
- $1 \leq A_i \leq N$
- $A$ is a permutation.

---

## Examples

**Example 1**

**Input**

```text
3
6
3 2 1 4 5 6
3
1 2 3
8
5 8 7 3 6 1 2 4
```

**Output**

```text
4
3
1
```

**Explanation**

- **Test Case $1$**: We can partition the array as follows - $[3,2,1] [4] [5] [6] $, so we will have $4$ partitions.
- **Test Case $2$**: We can partition the array as follows - $[1] [2] [3] $, so we will have $3$ partitions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
3 2 1 4 5 6
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
8
5 8 7 3 6 1 2 4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Maximum Partitioning of a Permutation into Sorted Subarrays

In this lesson we study a problem where you are given an array $A$ of length $N$ which is a **permutation** of numbers from $1$ to $N$. You are allowed to split the array into several partitions. Then you are allowed to sort each partition individually. Finally, you must join the sorted partitions (without reordering them) so that the final concatenated array is completely sorted in increasing order. The goal is to maximize the number of such partitions.

For example, consider the array:
$$
A = [3, 2, 1, 4, 5, 6]
$$
One optimal way to partition is:
$$
[3,2,1] \quad [4] \quad [5] \quad [6]
$$
After sorting each partition, we obtain:
$$
[1,2,3] \quad [4] \quad [5] \quad [6]
$$
When concatenated, the result is $[1,2,3,4,5,6]$. Thus, the maximum number of partitions here is $4$.

Below we discuss two approaches to solve this problem.

---

## Approach 1: Greedy Running Maximum

### **Intuition**

Since the array is a permutation of $1$ to $N$, note that when you traverse the array from left to right, if at index $i$ the maximum element encountered so far equals $i+1$, then the subarray $A[0 \ldots i]$ must contain exactly the numbers $1$ to $i+1$. Sorting this subarray will yield the sorted segment $[1, 2, \dots, i+1]$. Hence, we can place a partition ending at index $i$. This greedy method is optimal because we try to make a partition at every possible place where the condition
$$
\text{max\_so\_far} = i+1
$$
is met.

### **Complexity**

- **Time Complexity:** $O(N)$ per test case.
- **Space Complexity:** $O(1)$ extra space (apart from input).

### **Code Implementation**

Below is the complete C++ and Python code using the greedy approach.

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        int partitions = 0;
        int max_so_far = 0;
        for (int i = 0; i < N; i++) {
            max_so_far = max(max_so_far, A[i]);
            // If the maximum so far equals the index+1, a valid partition is found.
            if (max_so_far == i + 1) {
                partitions++;
            }
        }

        cout << partitions << "\n";
    }

    return 0;
}
```

#### Python Code
```python
def max_partitions(A):
    partitions = 0
    max_so_far = 0
    for i, x in enumerate(A):
        max_so_far = max(max_so_far, x)
        # Checking if subarray [0...i] can form a valid partition.
        if max_so_far == i + 1:
            partitions += 1
    return partitions

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        A = list(map(int, input_data[index:index+n]))
        index += n
        results.append(max_partitions(A))
    print("\n".join(map(str, results)))
```

---

## Approach 2: Prefix Maximum and Suffix Minimum Arrays

### **Intuition**

Another way to observe valid partition boundaries is by checking if every element in the left partition is less than or equal to every element in the right partition. We can precompute two arrays:

- **Prefix Maximum ($\text{prefix}[i]$):** The maximum element from $A[0]$ to $A[i]$.
- **Suffix Minimum ($\text{suffix}[i]$):** The minimum element from $A[i]$ to $A[N-1]$.

A partition boundary between indices $i$ and $i+1$ is valid if:
$$
\text{prefix}[i] \leq \text{suffix}[i+1]
$$

Since the array is a permutation, this condition turns out to be equivalent to the check in Approach 1. Nevertheless, this method reinforces the idea and is particularly useful in problems where array elements are arbitrary.

### **Complexity**

- **Time Complexity:** $O(N)$ per test case.
- **Space Complexity:** $O(N)$ extra space for the auxiliary arrays.

### **Code Implementation**

Below is the C++ and Python code using the prefix and suffix arrays technique.

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++){
            cin >> A[i];
        }

        vector prefix_max(N), suffix_min(N);
        prefix_max[0] = A[0];
        for (int i = 1; i < N; i++){
            prefix_max[i] = max(prefix_max[i - 1], A[i]);
        }
        suffix_min[N - 1] = A[N - 1];
        for (int i = N - 2; i >= 0; i--){
            suffix_min[i] = min(suffix_min[i + 1], A[i]);
        }

        int partitions = 0;
        // For every boundary, check if the partitioning condition is met.
        for (int i = 0; i < N - 1; i++){
            if(prefix_max[i] <= suffix_min[i+1]) {
                partitions++;
            }
        }
        // Add the final partition.
        partitions++;
        cout << partitions << "\n";
    }
    return 0;
}
```

#### Python Code
```python
def max_partitions_prefix_suffix(A):
    n = len(A)
    prefix_max = [0] * n
    suffix_min = [0] * n
    prefix_max[0] = A[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], A[i])
    suffix_min[-1] = A[-1]
    for i in range(n-2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], A[i])

    partitions = 0
    for i in range(n-1):
        if prefix_max[i] <= suffix_min[i+1]:
            partitions += 1
    partitions += 1  # Account for the last partition
    return partitions

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        A = list(map(int, input_data[index:index+n]))
        index += n
        results.append(max_partitions_prefix_suffix(A))
    print("\n".join(map(str, results)))
```

---

## Summary

- **Approach 1 (Greedy Running Maximum)** is the most efficient and straightforward solution.
- **Approach 2 (Prefix Maximum and Suffix Minimum Arrays)** offers an alternative perspective which can be generalized to other partitioning problems.

Understanding these two approaches ensures you have a strong grasp of the problem's structure and the reasoning behind making a partition at each valid index.

Happy Coding!

</details>
