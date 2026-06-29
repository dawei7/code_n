# Difference Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP68 |
| Difficulty Rating | 1000 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [PREP68](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/PREP68) |

---

## Problem Statement

You are given an array $A$ of $N$ integers and an integer $B$. Your task is to determine whether there exists a pair of indices $(i, j)$ such that $1 \leq i < j \leq N$ and $|A[i] - A[j]| = B$.

---

## Function Declaration

### Function Name
$hasPairWithDifference$ – This function checks if there is any valid pair in the array with an absolute difference exactly equal to $B$.

### Parameters

* $A$ : A list/array of integers of length $N$, representing the input sequence.
* $N$ : An integer representing the number of elements in the array.
* $B$ : An integer representing the target absolute difference.

### Return Value

Returns an integer(or boolean): `1` (or `true`) if such a pair exists, and `0` (or `false`) otherwise.

---

### Constraints:
* $1 \leq T \leq 100$
* $1 \leq N \leq 10^5$
* $-10^9 \leq A[i] \leq 10^9$ for each $1 \leq i \leq N$
* $0 \leq B \leq 2 \cdot 10^9$
* The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically**

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $B$.
    - The next line contains $N$ space-separated integers representing array $A$.

---

## Output Format

For each test case, output on a new line $1$ if there exists a pair of indices $(i, j)$ $(1\le i \lt j \le N)$ such that $abs(A_i - A_j) = B$, or $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $-10^6 \leq B \leq 10^6$
- $-10^6 \leq A_i \leq 10^6$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
6 78
5 10 3 2 50 80
2 30
-10 20
4 5
1 2 3 4
```

**Output**

```text
1
1
0
```

**Explanation**

**Test case $1$:** Given $A$ as $[5, 10, 3, 2, 50, 80]$. Elements with difference $78$ are $A_6 = 80$ and $A_4 = 2$.

**Test case $2$:** Given $A$ as $[-10, 20]$. Elements with difference $30$ are $A_2 = 20$ and $A_1 = -10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 78
5 10 3 2 50 80
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 30
-10 20
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 5
1 2 3 4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# DSA Interview Preparation: Finding a Pair with a Given Absolute Difference

In this lesson, we explore the problem of detecting whether there exists a pair of indices in an array such that the absolute difference between the corresponding elements is equal to a given value $B$. In mathematical terms, we want to find indices $i$ and $j$ (with $1 \le i < j \le N$) such that:
$$
|A_i - A_j| = |B|
$$
We present two efficient approaches to solve this problem, allowing you to choose the most suitable method based on input size and efficiency requirements.

---

## Approach 1: Sorting and Two-Pointers

### Explanation

The **Sorting and Two-Pointers Approach** works as follows:

1. **Sort the Array:** Sorting the array allows us to methodically check differences in a structured order.
2. **Two-Pointers Technique:** Initialize two pointers `i` and `j` such that `i = 0` and `j = 1`.
   - Calculate the difference $A[j] - A[i]$ (this is non-negative since the array is sorted).
   - If the difference equals $B$, the required pair has been found.
   - If the difference is less than $B$, increment the right pointer (`j`) to increase the difference.
   - If the difference is greater than $B$, increment the left pointer (`i`) to decrease the difference.
   - Ensure that `i` is always less than `j` by adjusting pointers appropriately.

- **Time Complexity:** $O(N \log N)$ due to sorting, plus $O(N)$ for the two-pointer traversal.
- **Space Complexity:** $O(1)$ extra space, if sorting is done in place.

This approach efficiently handles moderate to large arrays, avoiding unnecessary comparisons.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, B;
        cin >> N >> B;
        B = abs(B);

        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        sort(A.begin(), A.end());
        int i = 0, j = 1;
        bool found = false;

        while (i < N && j < N) {
            if (i != j && (A[j] - A[i]) == B) {
                found = true;
                break;
            } else if ((A[j] - A[i]) < B) {
                j++;
            } else {
                i++;
            }
            if (i == j)
                j++;
        }

        cout << (found ? 1 : 0) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
T = int(input())
for _ in range(T):
    N, B = map(int, input().split())
    B = abs(B)
    A = list(map(int, input().split()))

    A.sort()
    i, j = 0, 1
    found = False

    while i < N and j < N:
        if i != j and (A[j] - A[i]) == B:
            found = True
            break
        elif (A[j] - A[i]) < B:
            j += 1
        else:
            i += 1
        if i == j:
            j += 1

    print(1 if found else 0)
```

---

## Approach 2: HashSet for Direct Lookup

### Explanation

The **HashSet Approach** leverages an unordered set (or hash set) to achieve an average time complexity of $O(N)$ per test case. The key idea is to iterate through the array and, for each element $a$, verify whether either $a + B$ or $a - B$ exists in the set. If either exists, the pair satisfying the condition has been found. If not, insert $a$ into the set and continue.

- **Time Complexity:** Average-case $O(N)$ due to constant-time lookups in the hash set.
- **Space Complexity:** $O(N)$ for storing elements.

This method is particularly efficient for large inputs thanks to its direct lookup strategy.

### Code Implementation

#### C++ Code
```cpp
#include
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
        int N, B;
        cin >> N >> B;
        B = abs(B);

        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        unordered_set seen;
        bool found = false;
        for (int num : A) {
            if (seen.count(num - B) || seen.count(num + B)) {
                found = true;
                break;
            }
            seen.insert(num);
        }

        cout << (found ? 1 : 0) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
T = int(input())
for _ in range(T):
    N, B = map(int, input().split())
    B = abs(B)
    A = list(map(int, input().split()))

    seen = set()
    found = False
    for num in A:
        if (num - B) in seen or (num + B) in seen:
            found = True
            break
        seen.add(num)

    print(1 if found else 0)
```

---

## Summary

- **Sorting and Two-Pointers Approach:** Provides an efficient solution with a time complexity of $O(N \log N)$ due to sorting, making it ideal for moderately large arrays.
- **HashSet Approach:** Offers an average-case $O(N)$ solution and is especially optimal for very large inputs due to the fast lookup times of hash sets.

These two approaches give you a range of efficient methods for finding a pair with a given absolute difference. Choose the approach that best fits the constraints and size of your input.

Happy coding and best of luck during your DSA interviews!

</details>
