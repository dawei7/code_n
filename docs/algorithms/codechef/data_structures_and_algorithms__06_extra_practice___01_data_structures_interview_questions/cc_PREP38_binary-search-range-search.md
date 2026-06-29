# Binary Search - Range Search

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP38 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [PREP38](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/PREP38) |

---

## Problem Statement

You are given an array $A$ of size $N$. The elements of the array are sorted in ascending order. You are also given $Q$ queries which are of two types as follows:
- $0$ $i$ $X$: Given integers $i$ and $X$, change the $i^{th}$ $(1\le i \le N)$ element $A_i$ to $X$. Note that the array remains **sorted** after each operation of this type.
- $1$ $Y$: Given an integer $Y$, find the starting and ending position ($1-$based indexing) of the element $Y$ in array $A$. If the element is not present, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the size of array $A$ and the number of queries, respectively.
    - The second line contains $N$ space-separated integers - the array $A$. Note that the array is sorted.
    - The next $Q$ line contains details of the queries.

---

## Output Format

For each test case, if the query is of type $1$, output the starting and ending position of element $Y$ in the array $A$ in a new line. If $Y$ is not present in array $A$, print $-1$.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N, Q \leq 10^5$
- $1 \leq A_i, X, Y \leq 3\cdot 10^6$
- The array $A$ remains sorted in ascending order at all times.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
- The sum of $Q$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3 3
1 4 4
1 4
0 3 7
1 4
4 4
1 2 3 4
0 3 4
0 2 4
0 1 4
1 4
5 2
1 1 1 5 5
1 1
1 4
```

**Output**

```text
2 3
2 2
1 4
1 3
-1
```

**Explanation**

**Test case $1$:** Given $A$ as $[1, 4, 4]$.
- Query $1$: Given type $1$ query and $Y=4$. The starting and ending position are $2$ and $3$.
- Query $2$: Given type $0$ query, $i = 3$ and $X = 7$. The array $A$ becomes $[1, 4, 7]$.
- Query $3$: Given type $1$ query and $Y=4$. The starting and ending position are $2$ and $2$.

**Test case $2$:** Given $A$ as $[1, 2, 3, 4]$.
- Query $1$: Given type $0$ query, $i = 3$ and $X = 4$. The array $A$ becomes $[1, 2, 4, 4]$.
- Query $2$: Given type $0$ query, $i = 2$ and $X = 4$. The array $A$ becomes $[1, 4, 4, 4]$.
- Query $3$: Given type $0$ query, $i = 1$ and $X = 4$. The array $A$ becomes $[4, 4, 4, 4]$.
- Query $4$: Given type $1$ query and $Y=4$. The starting and ending position are $1$ and $4$.

**Test case $3$:** Given $A$ as $[1, 1, 1, 5, 5]$.
- Query $1$: Given type $1$ query and $Y=1$. The starting and ending position are $1$ and $3$.
- Query $2$: Given type $1$ query and $Y=5$. The element is not present. Thus, we print $-1$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Processing Queries on a Sorted Array

In this problem, we have an array $A$ of size $N$ that is maintained in sorted order. We need to support two types of queries:

1. **Update Query (Type 0):**
   Change the $i^{th}$ element to $X$. Although this update might appear to disturb the order, the problem guarantees that after processing the update, the array remains sorted. To ensure this, we reposition the updated element to its correct location in the array.

2. **Range Query (Type 1):**
   Given an integer $Y$, determine the starting and ending (1-indexed) positions where $Y$ occurs in $A$. If $Y$ is not present, output $-1$. This can be efficiently achieved using binary search methods such as lower bound and upper bound.

Below, we discuss a correct and intuitive approach to solve this problem.

---

## Approach: Removal and Reinsertion Using Binary Search

### Idea

A straightforward solution is to **remove** the element at the specified index and then **reinsert** the updated value $X$ in its proper position using binary search. This guarantees that the array remains sorted after every update.

For the range query (Type 1), we use binary search (e.g. via `lower_bound`/`upper_bound` in C++ or the `bisect` module in Python) to quickly locate the first and last occurrences of $Y$.

### How It Works

- **Update Query (Type 0):**
  - Remove the element at index $i-1$.
  - Use binary search to determine where $X$ should be inserted in the remaining sorted array.
  - Insert $X$ at that position.

- **Range Query (Type 1):**
  - Use binary search to find the first position where $Y$ occurs.
  - Similarly, determine the last occurrence.
  - Convert these positions from 0-indexed to 1-indexed for the final output. If $Y$ is not found, output $-1$.

### Complexity and Relevance

- **Time Complexity:**
  - Binary search operations for range queries run in $O(\log N)$.
  - Updating an element by removal and reinsertion has a worst-case time complexity of $O(N)$ due to shifting elements during removal and insertion.

- **Relevance:**
  This approach is intuitive, easy to implement, and works well for maintaining a sorted array under the specified constraints.

### Code Implementations

Below is the C++ and Python code implementation for the removal and reinsertion approach.

#### C++ Code

```cpp
#include
#include
#include
using namespace std;

pair findStartEnd(const vector& arr, int target) {
    auto start = lower_bound(arr.begin(), arr.end(), target);
    if (start == arr.end() || *start != target) {
        return {-1, -1};
    }
    auto end = upper_bound(arr.begin(), arr.end(), target);
    return {int(start - arr.begin()) + 1, int(end - arr.begin())};
}

void solve() {
    int N, Q;
    cin >> N >> Q;
    vector A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    while (Q--) {
        int type;
        cin >> type;
        if (type == 0) {
            int i, X;
            cin >> i >> X;
            int pos = i - 1;
            // Remove the element at index pos.
            A.erase(A.begin() + pos);
            // Insert X in the correct sorted position.
            auto it = lower_bound(A.begin(), A.end(), X);
            A.insert(it, X);
        } else {
            int Y;
            cin >> Y;
            auto result = findStartEnd(A, Y);
            if (result.first == -1) {
                cout << -1 << "\n";
            } else {
                cout << result.first << " " << result.second << "\n";
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

#### Python Code

```python
import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output = []
    for _ in range(t):
        N = int(data[index]); index += 1
        Q = int(data[index]); index += 1
        A = list(map(int, data[index:index+N])); index += N
        for _ in range(Q):
            typ = int(data[index]); index += 1
            if typ == 0:
                i = int(data[index]); X = int(data[index + 1]); index += 2
                pos = i - 1
                # Remove the element at position pos.
                A.pop(pos)
                # Find the correct insertion index and insert X.
                insert_pos = bisect.bisect_left(A, X)
                A.insert(insert_pos, X)
            else:
                Y = int(data[index]); index += 1
                left_idx = bisect.bisect_left(A, Y)
                if left_idx == len(A) or A[left_idx] != Y:
                    output.append("-1")
                else:
                    right_idx = bisect.bisect_right(A, Y)
                    output.append(f"{left_idx + 1} {right_idx}")
        # End of test case.
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
```

---

## Advanced Considerations

For very large inputs or when the number of queries is huge, one might consider using advanced data structures such as balanced binary search trees (e.g., Red-Black trees) or Fenwick trees (Binary Indexed Trees) with order statistics. These structures can support both point updates and range queries in $O(\log N)$ time. However, for the current problem constraints, the removal and reinsertion approach is intuitive and sufficiently efficient.

---

In summary, we have explored an effective method to handle queries on a sorted array using the removal and reinsertion technique with binary search. This approach simplifies maintaining the sorted order while ensuring range queries are handled efficiently.

Happy coding and best of luck with your DSA interviews!

</details>
