# Sum of Smaller Elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMLSUM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SMLSUM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/SMLSUM) |

---

## Problem Statement

You are given two sequences $A_1, A_2, \ldots, A_N$ and $B_1, B_2, \ldots, B_N$.

You need to answer $Q$ queries. In each query you are given an integer $X$ and you need find the sum of all elements $B_i$ of the sequence $B$ for which it holds that $A_i \leq X$.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains two-space separated integers $N$ and $Q$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

- The fourth line contains $Q$ space-separated integers $X_1, X_2, \ldots, X_Q$.

---

## Output Format

- For each test case, print a single line containing $Q$ space-separated integers. The $j$-th integer in the line should be the sum of all elements $B_i$ of the sequence $B$ for which it holds that $A_i \leq X_j$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,Q \leq 10^5$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$
- the sum of $Q$ over all test cases does not exceed $2 \cdot 10^{5}$
- $1 \leq A_i,B_i,X_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
1
5 5
6 2 8 1 4
9 9 8 9 1
1 2 3 9 5
```

**Output**

```text
9 18 18 36 19
```

**Explanation**

**Example case 1:** In the first query, only $A_4 = 1 \leq 1$ so the answer is $B_4=9$. In the second query, $A_4 \leq 2$ and $A_2 \leq 2$ so the answer is $B_4+B_2=18$. In the third query, only elements on positions $2$ and $4$ are appropriate, so the answer is $18$ again. In the fourth query, all the elements are smaller than or equal to $9$, so the answer is $B_1+B_2+B_3+B_4+B_5=36$. In the fifth query, $A_2 \leq 5$, $A_4 \leq 5$ and $A_5 \leq 5$ so the answer is $B_2+B_4+B_5=19$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Solving the "Sum of B for A ≤ X" Problem

In this editorial, we discuss three reliable approaches to solve the task where you are given two sequences $A$ and $B$, and for each query with an integer $X$, you must compute the sum of all $B_i$ such that $A_i \leq X$. We will explore the following methods:

1. **Sorting and Prefix Sum with Binary Search:**
   This intuitive approach involves pairing the elements from sequences $A$ and $B$, sorting these pairs by the $A$ values, and building a prefix sum array on the $B$ values. For each query, a binary search (upper bound) is used to determine the number of elements with $A_i \leq X$, and the prefix sum up to that index gives the answer.

2. **Fenwick Tree (Binary Indexed Tree):**
   Here, we perform coordinate compression on the $A$ array because the values can be as large as $10^9$, then build a Fenwick Tree by updating it with the corresponding $B$ values at the compressed indices. Each query is then answered by performing a prefix sum query in the tree. This method is especially useful when there are updates or multiple dynamic queries, although it fits well here.

3. **Offline Query Processing with Two-Pointers:**
   In this method, we process all queries offline. Both the array of pairs $(A_i, B_i)$ and the queries are sorted. By iterating with two pointers, we add $B_i$ values to an accumulator as long as the condition $A_i \leq X$ is met for each query. This approach eliminates the need for repetitive binary searches.

Below are the detailed code implementations in both C++ and Python for each approach.

---

## Approach 1: Sorting and Prefix Sum with Binary Search

### C++ Implementation
```cpp
#include
#include
#include
using namespace std;

struct Item {
    int a, b;
    Item(int a, int b) : a(a), b(b) {}
};

bool itemCompare(const Item& i1, const Item& i2) {
    return i1.a < i2.a;
}

void solve() {
    int N, Q;
    cin >> N >> Q;

    vector items;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        items.emplace_back(a, 0);
    }

    for (int i = 0; i < N; i++) {
        cin >> items[i].b;
    }

    sort(items.begin(), items.end(), itemCompare);

    vector prefixSum(N + 1, 0);
    for (int i = 0; i < N; i++) {
        prefixSum[i + 1] = prefixSum[i] + items[i].b;
    }

    for (int i = 0; i < Q; i++) {
        int X;
        cin >> X;
        auto it = upper_bound(items.begin(), items.end(), Item(X, 0), itemCompare);
        int index = distance(items.begin(), it);
        cout << prefixSum[index] << " ";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) solve();
    return 0;
}
```

### Python Implementation
```python
import bisect
import sys
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    items = list(zip(A, B))
    items.sort(key=lambda x: x[0])

    prefix_sum = [0]
    for a, b in items:
        prefix_sum.append(prefix_sum[-1] + b)

    queries = list(map(int, input().split()))
    for X in queries:
        index = bisect.bisect_right(items, (X, float('inf')))
        sys.stdout.write(str(prefix_sum[index]) + " ")
    sys.stdout.write("\n")

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        solve()
```

---

## Approach 2: Fenwick Tree (Binary Indexed Tree)

### C++ Implementation
```cpp
#include
#include
#include
using namespace std;

struct Fenwick {
    int n;
    vector tree;
    Fenwick(int n): n(n), tree(n+1, 0) {}

    void update(int i, long long delta) {
        while(i <= n) {
            tree[i] += delta;
            i += i & -i;
        }
    }

    long long query(int i) {
        long long sum = 0;
        while(i > 0) {
            sum += tree[i];
            i -= i & -i;
        }
        return sum;
    }
};

void solve() {
    int N, Q;
    cin >> N >> Q;
    vector A(N), B(N), comp;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        comp.push_back(A[i]);
    }
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }

    sort(comp.begin(), comp.end());
    comp.erase(unique(comp.begin(), comp.end()), comp.end());

    Fenwick fenw(comp.size());
    for (int i = 0; i < N; i++) {
        int idx = lower_bound(comp.begin(), comp.end(), A[i]) - comp.begin() + 1;
        fenw.update(idx, B[i]);
    }

    for (int i = 0; i < Q; i++) {
        int X;
        cin >> X;
        int idx = upper_bound(comp.begin(), comp.end(), X) - comp.begin();
        cout << fenw.query(idx) << " ";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) solve();
    return 0;
}
```

### Python Implementation
```python
import sys
import bisect
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        return total

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    comp = sorted(set(A))
    coord = {v: i+1 for i, v in enumerate(comp)}

    fenw = FenwickTree(len(comp))
    for i in range(N):
        fenw.update(coord[A[i]], B[i])

    queries = list(map(int, input().split()))
    res = []
    for X in queries:
        idx = bisect.bisect_right(comp, X)
        res.append(fenw.query(idx))
    sys.stdout.write(" ".join(map(str, res)) + "\n")

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        solve()
```

---

## Approach 3: Offline Query Processing with Two-Pointers

### C++ Implementation
```cpp
#include
#include
#include
using namespace std;

void solve() {
    int N, Q;
    cin >> N >> Q;
    vector> items(N);
    for (int i = 0; i < N; i++) {
        cin >> items[i].first;
    }
    for (int i = 0; i < N; i++) {
        cin >> items[i].second;
    }

    vector> queries(Q);
    for (int i = 0; i < Q; i++) {
        int X;
        cin >> X;
        queries[i] = {X, i};
    }

    sort(items.begin(), items.end());
    sort(queries.begin(), queries.end());

    vector ans(Q, 0);
    long long curr_sum = 0;
    int j = 0;
    for (auto &q : queries) {
        int X = q.first;
        while(j < N && items[j].first <= X) {
            curr_sum += items[j].second;
            j++;
        }
        ans[q.second] = curr_sum;
    }

    for(auto &res : ans)
        cout << res << " ";
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) solve();
    return 0;
}
```

### Python Implementation
```python
import sys
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    items = list(zip(A, B))
    items.sort(key=lambda x: x[0])
    sorted_queries = sorted([(x, i) for i, x in enumerate(queries)])

    ans = [0] * Q
    curr_sum = 0
    j = 0
    for X, idx in sorted_queries:
        while j < N and items[j][0] <= X:
            curr_sum += items[j][1]
            j += 1
        ans[idx] = curr_sum
    sys.stdout.write(" ".join(map(str, ans)) + "\n")

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        solve()
```

---

## Final Remarks

All three approaches efficiently address the problem within the constraints provided.
- **Approach 1** is clear and utilizes sorting with prefix sums and binary search, making it easy to implement and understand.
- **Approach 2** introduces the Fenwick Tree data structure with coordinate compression, a useful tool for many range query problems.
- **Approach 3** processes the queries offline using a two-pointer technique which is both elegant and efficient.

Understanding these methods not only helps in solving this particular problem but also builds a foundation for solving various other query and range-sum problems in interviews.

Happy Coding!

</details>
