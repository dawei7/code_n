# Maximum power of two

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAX2POW |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MAX2POW](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/MAX2POW) |

---

## Problem Statement

Given an array $A$ ($1$-indexed) of positive integers size $N$ and $Q$ queries. Each query will be in the form $l$ $r$ $x$ which means multiply all the elements in array $A$ from index $l$ to $r$ (inclusive) by $x$. Output the maximum power of $2$ in the final array $A$.

---

## Input Format

- The first line of input contains $2$ integers $N$ - size of array $A$ and $Q$ - number of queries
- The second line contains $N$ space-separated integers $A_1, A_2,……, A_N$
- Each of the next $Q$ lines contains three space-separated integers $l$ $r$ $x$ denoting the query.

---

## Output Format

Output a single line containing one integer - Maximum power of $2$ in the final array.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $ 1 \leq l \leq r \leq N $
- $ 2 \leq x \leq 10^9 $
- $ 1 \leq A_i \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
5 4
1 2 3 4 5
1 1 3
2 3 4
3 3 6
1 5 2
```

**Output**

```text
4
```

**Explanation**

Query 1 : Multiply numbers from index 1 to 1 by 3
Resulting array : 3 2 3 4 5

Query 2 : Multiply numbers from index 2 to 3 by 4
Resulting array : 3 8 12 4 5

Query 3 : Multiply numbers from index 3 to 3 by 6
Resulting array : 3 8 72 4 5

Query 4 : Multiply numbers from index 1 to 5 by 2
Resulting array : 6 16 144 8 10

So, highest power of $2$ in the array is $4$ as $144$ has prime factorisation as $2^4 \cdot 3^2$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we study a problem in which we are given an array $A$ of size $N$ and $Q$ queries. Each query specifies a range $[l, r]$ and a multiplier $x$. For every query, we multiply all elements in the range by $x$. Our goal is to determine the maximum exponent of $2$ – that is, the maximum power $p$ such that $2^p$ divides some element of the final array.

The key observation here is that we only care about the power of $2$ in each number. If we denote by $f(i)$ the exponent of $2$ in $A_i$, then each multiplication query (multiplying by $x$) adds $p = \text{count}(x)$ (where $\text{count}(x)$ is the number of times $2$ divides $x$) to the factor of $2$ in every element within the range. Thus, after applying all queries, the final exponent for index $i$ becomes:

$$
f(i) = \text{initialPower}[i] + \sum_{\text{query affecting }i} p.
$$

We now discuss three approaches to solve this problem.

---

## Approach 1: Difference Array

### Explanation

Instead of updating the exponent for each element directly per query (which would be too slow for large $N$ and $Q$), we use a difference array technique. The idea is to maintain an auxiliary array `diff` where, for each query $(l, r, x)$ (with $p = \text{count}(x)$), we perform:

- `diff[l] += p`
- `diff[r+1] -= p`

After processing all queries, we convert the difference array into prefix sums. The value at index $i$ in the prefix sum represents the total increment (from all queries) to be added to the initial exponent at index $i$. Finally, we add this total increment to the precomputed exponent of $2$ for $A_i$ (which is obtained by repeatedly dividing $A_i$ by $2$) and then take the maximum over all indices.

This approach runs in $O(N + Q)$ time.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

// Function to count the power of 2 in x
int countTwo(long long x) {
    int cnt = 0;
    while(x % 2 == 0) {
        cnt++;
        x /= 2;
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector initialPower(N + 1, 0);

    // Calculate initial power of 2 for each element (1-indexed)
    for (int i = 1; i <= N; i++){
        long long x;
        cin >> x;
        initialPower[i] = countTwo(x);
    }

    // Difference array for range updates
    vector diff(N + 2, 0);
    while(Q--){
        int l, r;
        long long x;
        cin >> l >> r >> x;
        int p = countTwo(x);
        diff[l] += p;
        diff[r + 1] -= p;
    }

    int maxPower = 0, add = 0;
    for (int i = 1; i <= N; i++){
        add += diff[i];
        maxPower = max(maxPower, initialPower[i] + add);
    }

    cout << maxPower << "\n";
    return 0;
}
```

#### Python Code
```python
def count_two(x):
    cnt = 0
    while x % 2 == 0:
        cnt += 1
        x //= 2
    return cnt

def main():
    import sys
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    N = int(next(it))
    Q = int(next(it))
    initialPower = [0] * (N + 1)

    for i in range(1, N + 1):
        x = int(next(it))
        initialPower[i] = count_two(x)

    diff = [0] * (N + 2)
    for _ in range(Q):
        l = int(next(it))
        r = int(next(it))
        x = int(next(it))
        p = count_two(x)
        diff[l] += p
        diff[r + 1] -= p

    maxPower = 0
    add = 0
    for i in range(1, N + 1):
        add += diff[i]
        maxPower = max(maxPower, initialPower[i] + add)
    print(maxPower)

if __name__ == '__main__':
    main()
```

---

## Approach 2: Fenwick Tree (Binary Indexed Tree)

### Explanation

A Fenwick tree (or Binary Indexed Tree, BIT) efficiently supports point queries and range updates. Here, we use the BIT to add the power increment $p$ for each query over the range $[l, r]$ by performing:
- `update(l, p)`
- `update(r + 1, -p)`

After processing all queries, a prefix sum query on the BIT at any index $i$ will give the total addition (from all the queries) that applies to $A_i$. We then add this value to the precomputed exponent of $2$ for that element and track the maximum.

This approach has similar time complexity to the difference array method, i.e. $O((N + Q)\log N)$ due to BIT operations.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

struct Fenwick {
    int n;
    vector tree;
    Fenwick(int n): n(n) {
        tree.assign(n + 1, 0);
    }
    void update(int i, int delta) {
        for (; i <= n; i += i & -i)
            tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i)
            sum += tree[i];
        return sum;
    }
};

int countTwo(long long x) {
    int cnt = 0;
    while(x % 2 == 0) {
        cnt++;
        x /= 2;
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector initialPower(N + 1, 0);
    for (int i = 1; i <= N; i++){
        long long x;
        cin >> x;
        initialPower[i] = countTwo(x);
    }

    Fenwick bit(N);
    while(Q--){
        int l, r;
        long long x;
        cin >> l >> r >> x;
        int p = countTwo(x);
        // Perform range update using BIT
        bit.update(l, p);
        if(r + 1 <= N)
            bit.update(r + 1, -p);
    }

    int maxPower = 0;
    for (int i = 1; i <= N; i++){
        int add = bit.query(i);
        maxPower = max(maxPower, initialPower[i] + add);
    }

    cout << maxPower << "\n";
    return 0;
}
```

#### Python Code
```python
import sys

def count_two(x):
    cnt = 0
    while x % 2 == 0:
        cnt += 1
        x //= 2
    return cnt

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    initialPower = [0] * (N + 1)

    for i in range(1, N + 1):
        x = int(next(it))
        initialPower[i] = count_two(x)

    bit = Fenwick(N)
    for _ in range(Q):
        l = int(next(it))
        r = int(next(it))
        x = int(next(it))
        p = count_two(x)
        bit.update(l, p)
        if r + 1 <= N:
            bit.update(r + 1, -p)

    maxPower = 0
    for i in range(1, N + 1):
        add = bit.query(i)
        maxPower = max(maxPower, initialPower[i] + add)
    print(maxPower)

if __name__ == '__main__':
    main()
```

---

## Approach 3: Segment Tree with Lazy Propagation

### Explanation

A Segment Tree with lazy propagation provides another way to handle range updates efficiently. In this approach, we build a segment tree where each node represents an interval of the array. For a query $(l, r, x)$, we update the tree by adding $p = \text{count}(x)$ to the interval $[l, r]$. Lazy propagation ensures that these updates are applied only when necessary, which speeds up range updates. Finally, we perform a point query to combine the initial exponent for each element with its accumulated updation value.

Although this method is more complex and is an overkill for this particular problem (since the difference array is simpler), it is a valuable tool to learn for other problems involving range updates and queries.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

int countTwo(long long x) {
    int cnt = 0;
    while(x % 2 == 0) {
        cnt++;
        x /= 2;
    }
    return cnt;
}

void updateTree(vector &tree, vector &lazy, int node, int start, int end, int l, int r, int val) {
    if(lazy[node] != 0) {
        tree[node] += lazy[node];
        if(start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > r || end < l)
        return;
    if(start >= l && end <= r) {
        tree[node] += val;
        if(start != end) {
            lazy[node * 2] += val;
            lazy[node * 2 + 1] += val;
        }
        return;
    }
    int mid = (start + end) / 2;
    updateTree(tree, lazy, node * 2, start, mid, l, r, val);
    updateTree(tree, lazy, node * 2 + 1, mid + 1, end, l, r, val);
}

int queryTree(vector &tree, vector &lazy, int node, int start, int end, int idx) {
    if(lazy[node] != 0) {
        tree[node] += lazy[node];
        if(start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
    if(start == end)
        return tree[node];
    int mid = (start + end) / 2;
    if(idx <= mid)
        return queryTree(tree, lazy, node * 2, start, mid, idx);
    else
        return queryTree(tree, lazy, node * 2 + 1, mid + 1, end, idx);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector initialPower(N + 1, 0);
    for (int i = 1; i <= N; i++){
        long long x;
        cin >> x;
        initialPower[i] = countTwo(x);
    }

    int size = 4 * N;
    vector seg(size, 0), lazy(size, 0);

    for (int i = 0; i < Q; i++){
        int l, r;
        long long x;
        cin >> l >> r >> x;
        int p = countTwo(x);
        updateTree(seg, lazy, 1, 1, N, l, r, p);
    }

    int maxPower = 0;
    for (int i = 1; i <= N; i++){
        int add = queryTree(seg, lazy, 1, 1, N, i);
        maxPower = max(maxPower, initialPower[i] + add);
    }

    cout << maxPower << "\n";
    return 0;
}
```

#### Python Code
```python
import sys
sys.setrecursionlimit(200000)

def count_two(x):
    cnt = 0
    while x % 2 == 0:
        cnt += 1
        x //= 2
    return cnt

def update_tree(node, start, end, l, r, val, tree, lazy):
    if lazy[node] != 0:
        tree[node] += lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    if start > r or end < l:
        return
    if start >= l and end <= r:
        tree[node] += val
        if start != end:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return
    mid = (start + end) // 2
    update_tree(node * 2, start, mid, l, r, val, tree, lazy)
    update_tree(node * 2 + 1, mid + 1, end, l, r, val, tree, lazy)

def query_tree(node, start, end, index, tree, lazy):
    if lazy[node] != 0:
        tree[node] += lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    if start == end:
        return tree[node]
    mid = (start + end) // 2
    if index <= mid:
        return query_tree(node * 2, start, mid, index, tree, lazy)
    else:
        return query_tree(node * 2 + 1, mid + 1, end, index, tree, lazy)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    initialPower = [0] * (N + 1)
    for i in range(1, N + 1):
        x = int(next(it))
        initialPower[i] = count_two(x)

    size = 4 * (N + 1)
    tree = [0] * size
    lazy = [0] * size

    for _ in range(Q):
        l = int(next(it))
        r = int(next(it))
        x = int(next(it))
        p = count_two(x)
        update_tree(1, 1, N, l, r, p, tree, lazy)

    maxPower = 0
    for i in range(1, N + 1):
        add = query_tree(1, 1, N, i, tree, lazy)
        maxPower = max(maxPower, initialPower[i] + add)
    print(maxPower)

if __name__ == '__main__':
    main()
```

---

In conclusion, all three approaches efficiently compute the maximum power of $2$ among the final elements of the array. The **Difference Array** approach is simple and has an optimal time complexity of $O(N + Q)$. The **Fenwick Tree** and **Segment Tree** approaches offer additional tools to handle range updates and queries, which are useful for more advanced variations of similar problems.

</details>
