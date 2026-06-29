# Remove Duplicates

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP69 |
| Difficulty Rating | 900 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [PREP69](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/PREP69) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$ sorted in **non-decreasing** order. Your task is to remove all the duplicates and find the sorted **increasing** array of distinct elements consisting of all distinct elements present in $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output two lines:
- The first line should contain a single integer $M$ - the size of the array.
- The second line should contain $M$ space-separated integers denoting the elements of the array.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
5 10
4
1 5 5 10
5
4 4 6 6 8
```

**Output**

```text
2
5 10 
3
1 5 10 
3
4 6 8
```

**Explanation**

**Test case $1$**: Distinct elements will be $5$, $10$. So the array will be $[5, 10]$.

**Test case $2$**: Distinct elements will be $1$, $5$, $10$. So the array will be $[1, 5, 10]$.

**Test case $3$**: Distinct elements will be $4$, $6$, $8$. So the array will be $[4, 6, 8]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Editorial: Removing Duplicates from a Sorted Array

In this lesson, we address the problem of removing duplicate values from a sorted array and outputting the distinct elements in increasing order. Since the given array is already sorted in non-decreasing order, the problem becomes simpler because all duplicate elements will appear consecutively.

---

### Approaches to the Problem

There are two primary approaches to solve this problem:

1. **Iterative Approach (Two-pointer technique):**
   Since the array is sorted, you can iterate through the array and simply compare each element with its previous element. If the current element is different from the previous one (or if it is the first element), then it is a distinct value and can be added to the output array.
   **Time Complexity:** $$O(N)$$
   **Space Complexity:** $$O(N)$$ (for storing distinct elements)

2. **Using Data Structures (Set):**
   Here, we use a set data structure to automatically filter out duplicate elements. In C++, a `std::set` maintains the elements in sorted order, while in Python, we convert the list to a set to remove duplicates and then sort the result.
   **Time Complexity:**
   - In C++: Insertion in a set takes $$O(\log N)$$ per element leading to $$O(N \log N)$$ in worst-case.
   - In Python: Converting to a set averages $$O(N)$$, but sorting afterwards requires $$O(N \log N)$$.
   **Space Complexity:** $$O(N)$$

---

### Detailed Explanations and Code Implementations

#### Approach 1: Iterative Approach (Two-pointer Technique)

**Explanation:**

- **Methodology:**
  Since the array is sorted, you can traverse the array from start to finish and compare each element with its immediate predecessor. If an element is different from the previous element, it is added to the result list of distinct elements.

- **Example:**
  Consider the array `[1, 5, 5, 10]`:
  - Start with the first element `1`, add it to the distinct list.
  - The next element is `5`, which is different from `1`, so add it.
  - The following element is another `5`, which is a duplicate, so skip it.
  - Finally, `10` is different from `5`, so add it.
  - The final list of distinct elements is `[1, 5, 10]`.

- **C++ Code Implementation:**

```cpp
#include
#include
using namespace std;

void solve() {
    int N;
    cin >> N;
    vector A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    vector distinct;
    // Since array is sorted, just compare with previous element
    for (int i = 0; i < N; i++) {
        if (i == 0 || A[i] != A[i - 1]) {
            distinct.push_back(A[i]);
        }
    }
    cout << distinct.size() << "\n";
    for (int num : distinct) {
        cout << num << " ";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

- **Python Code Implementation:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index+n]))
        index += n
        distinct = []
        for i in range(n):
            if i == 0 or arr[i] != arr[i - 1]:
                distinct.append(arr[i])
        results.append(str(len(distinct)))
        results.append(" ".join(map(str, distinct)))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
```

---

#### Approach 2: Using Data Structures (Set)

**Explanation:**

- **Methodology:**
  In this approach, we leverage the built-in properties of sets. A set automatically removes duplicate elements. In C++, we use `std::set` which also keeps the elements sorted, while in Python we convert the list to a set and then sort it to ensure the result is in increasing order.

- **Example:**
  Given the array `[4, 4, 6, 6, 8]`:
  - Inserting each element into a set results in `{4, 6, 8}`.
  - Converting this back to a list (or iterating through the set in C++) yields the sorted list `[4, 6, 8]`.

- **C++ Code Implementation:**

```cpp
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
        set distinct;
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            distinct.insert(x);
        }
        cout << distinct.size() << "\n";
        for (int num : distinct) {
            cout << num << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

- **Python Code Implementation:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index+n]))
        index += n
        # Using set to remove duplicates and then sort
        distinct = sorted(set(arr))
        results.append(str(len(distinct)))
        results.append(" ".join(map(str, distinct)))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
```

---

### Conclusion

Both approaches efficiently solve the problem of removing duplicates from a sorted array. The **Iterative Approach** is optimal with a time complexity of $$O(N)$$ and is easier to implement when the array is already sorted. The **Set-based Approach** provides a quick and clean solution using built-in data structures, though it might involve a slightly higher time complexity in certain cases due to sorting after de-duplication in Python or logarithmic insertion times in C++.

Choose the approach that best fits your programming style and the constraints of the problem at hand.

</details>
