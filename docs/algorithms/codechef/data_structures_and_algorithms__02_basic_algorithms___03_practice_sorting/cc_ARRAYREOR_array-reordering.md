# Array Reordering

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRAYREOR |
| Difficulty Rating | 1250 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [ARRAYREOR](https://www.codechef.com/practice/course/sorting/SORTINGPRO/problems/ARRAYREOR) |

---

## Problem Statement

You are given two arrays $A$ and $B$ of size $N$. Given a function $F$ such that. $F(i,j) = A_i  + B_j$
Reorder the arrays $A$ and $B$ such that $F(i,j) \geq F(j,i)$,  $1 \leq i \leq N, 1 \leq j \leq N, i \lt j$.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- Each test case will contain three lines of input.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains $N$ integers, $A_1, A_2 . . . A_N$.
- The third line of each test case contains $N$ integers, $B_1, B_2 . . . B_N$.

---

## Output Format

- In the first line of output, print the rearranged array $A$.
- In the first line of output, print the rearranged array $B$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases is less than or equal to $2*10^5$.

---

## Examples

**Example 1**

**Input**

```text
1
4
3 8 1 5
2 1 6 4
```

**Output**

```text
8 5 3 1 
1 2 4 6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will tackle a problem that asks us to reorder two arrays, $A$ and $B$, each of size $N$, so that for every pair of indices with $1 \leq i < j \leq N$, the following inequality holds:
$$
A_i + B_j \geq A_j + B_i.
$$

After a little algebra, we can rearrange the inequality as
$$
A_i - A_j \geq B_i - B_j.
$$

This form hints at a relationship between the elements of $A$ and $B$. In fact, one powerful result from combinatorial optimization — the rearrangement inequality — tells us that the sum
$$
\sum_{i=1}^N A_i \cdot B_{\sigma(i)}
$$
is maximized (or minimized) when one array is sorted in ascending order and the other in descending order. Although our problem is not directly about multiplying elements, this idea inspires us to look at ordering the arrays so that their relative differences favor the required inequality.

We will now discuss two effective approaches.

---

### **Approach 1: Greedy Sorting of Arrays**

**Idea:**
Sort array $A$ in **descending order** and array $B$ in **ascending order**. This guarantees that for every pair $i < j$, we have:
- $A_i \geq A_j$, and
- $B_i \leq B_j$.

When you add $A_i$ to $B_j$ versus $A_j$ to $B_i$, these orderings ensure that
$$
A_i + B_j \geq A_j + B_i,
$$
satisfying the problem’s condition.

**Explanation:**
Consider any two indices $i$ and $j$ with $i < j$. With $A$ sorted descending, $A_i \geq A_j$. Similarly, with $B$ sorted ascending, $B_i \leq B_j$. Therefore:
- The difference $A_i - A_j$ is non-negative.
- The difference $B_j - B_i$ is also non-negative.

Hence, the sum $A_i + B_j$ is at least as large as $A_j + B_i$, meeting the requirement. This approach is simple, efficient (with a time complexity of $O(N \log N)$), and is a direct application of the rearrangement principle.

**Implementation Code:**

Below are the implementations in both **C++** and **Python**.

**C++ Code:**
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
        vector A(N), B(N);

        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        for (int i = 0; i < N; i++) {
            cin >> B[i];
        }

        // Sort array A in descending order and array B in ascending order.
        sort(A.begin(), A.end(), greater());
        sort(B.begin(), B.end());

        for (int i = 0; i < N; i++) {
            cout << A[i] << " ";
        }
        cout << "\n";

        for (int i = 0; i < N; i++) {
            cout << B[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    t = int(next(it))
    results = []

    for _ in range(t):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(n)]

        # Sort A in descending order and B in ascending order.
        A.sort(reverse=True)
        B.sort()

        results.append(" ".join(map(str, A)))
        results.append(" ".join(map(str, B)))

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

---

### **Approach 2: Sorting by the Difference $(A_i - B_i)$**

**Idea:**
Notice that the inequality
$$
A_i + B_j \geq A_j + B_i
$$
can be rearranged to:
$$
A_i - B_i \geq A_j - B_j
$$
for every $i < j$. This suggests that if we compute the difference $D_i = A_i - B_i$ for each index and then sort the indices (or pair the respective $A$ and $B$ values) in **descending order of $D_i$**, the required property will be satisfied.

**Explanation:**
By forming pairs $\left( A_i, B_i \right)$ and sorting them such that the differences $D_i = A_i - B_i$ are in descending order, we ensure that:
$$
D_1 \geq D_2 \geq \cdots \geq D_N.
$$
For any two positions $i < j$, we then have
$$
A_i - B_i \geq A_j - B_j,
$$
which is equivalent to the condition
$$
A_i + B_j \geq A_j + B_i.
$$

**Implementation Code:**

Below are the implementations for this approach in both **C++** and **Python**.

**C++ Code:**
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

    while (T--) {
        int N;
        cin >> N;

        // Create a vector of pairs to store (A_i, B_i).
        vector> pairs(N);
        for (int i = 0; i < N; i++) {
            cin >> pairs[i].first;
        }
        for (int i = 0; i < N; i++) {
            cin >> pairs[i].second;
        }

        // Sort pairs by (A_i - B_i) in descending order.
        sort(pairs.begin(), pairs.end(), [](const pair& p1, const pair& p2) {
            return (p1.first - p1.second) > (p2.first - p2.second);
        });

        // Extract and print the rearranged A and B arrays.
        for (int i = 0; i < N; i++) {
            cout << pairs[i].first << " ";
        }
        cout << "\n";

        for (int i = 0; i < N; i++) {
            cout << pairs[i].second << " ";
        }
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    t = int(next(it))
    results = []

    for _ in range(t):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(n)]

        # Pair the elements from A and B.
        pairs = list(zip(A, B))

        # Sort pairs by (a - b) in descending order.
        pairs.sort(key=lambda x: x[0] - x[1], reverse=True)

        results.append(" ".join(str(pair[0]) for pair in pairs))
        results.append(" ".join(str(pair[1]) for pair in pairs))

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

---

### **Conclusion**

Both approaches satisfy the condition:
$$
A_i + B_j \geq A_j + B_i \quad \text{for all } 1 \leq i < j \leq N.
$$
- **Approach 1** uses straightforward, independent sorting of the arrays.
- **Approach 2** leverages the insight from the rearranged inequality by sorting based on the difference $(A_i - B_i)$.

Each method has a time complexity of $O(N \log N)$ due to sorting, ensuring that both are efficient within the given constraints. As a beginner, understanding these approaches not only helps in solving this problem but also builds a strong foundation in sorting techniques and the rearrangement inequality—a key concept in algorithm design.

Happy coding and best of luck with your DSA interviews!

</details>
