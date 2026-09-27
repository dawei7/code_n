# Guided Example: Count of Smaller Numbers After Self

We trace the step-by-step coordinate compression mapping, reverse right-to-left array traversal, Binary Indexed Tree (Fenwick tree) frequency insertion, and logarithmic prefix count extraction on representative sequence instances:

- **Input:** $\text{nums} = [5, 2, 6, 1]$
- **Required output:** $[2, 1, 1, 0]$
  - For $5$: Elements to right are $[2, 6, 1]$; elements smaller than $5$ are $2$ and $1$ ($2$ smaller)
  - For $2$: Elements to right are $[6, 1]$; element smaller than $2$ is $1$ ($1$ smaller)
  - For $6$: Element to right is $[1]$; element smaller than $6$ is $1$ ($1$ smaller)
  - For $1$: No elements to right ($0$ smaller)
- **Duplicate Elements Instance:** $\text{nums} = [-1, -1] \implies [0, 0]$ (Strict inequality; equal elements do not count as smaller)
- **Monotonically Increasing Array:** $\text{nums} = [1, 2, 3, 4] \implies [0, 0, 0, 0]$
- **Monotonically Decreasing Array:** $\text{nums} = [4, 3, 2, 1] \implies [3, 2, 1, 0]$

This instance demonstrates dynamic order statistics via coordinate compression and Fenwick trees, proves why scanning right-to-left restricts the data structure to only previously processed rightward elements, contrasts $O(N \log N)$ Fenwick querying against naive $O(N^2)$ nested scanning, and analyzes $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array:
$$
\text{nums} = [5, 2, 6, 1] \quad (N = 4)
$$
For each index $i$, find the number of elements to its right that are strictly smaller than $\text{nums}[i]$:
$$
\text{counts}[i] = \sum_{j > i} [\text{nums}[j] < \text{nums}[i]]
$$

```text
Elements:   5     2     6     1
Rightward: [2,6,1] [6,1]  [1]  []
Smaller:   {2, 1}  {1}   {1}   {}
Counts:      2      1     1     0
```

### Why a Naive Double Loop Fails
- Comparing each index $i$ against all $j > i$ requires $\frac{N(N - 1)}{2}$ operations, which is $O(N^2)$. For $N = 10^5$, $N^2 = 10^{10}$, causing immediate Time Limit Exceeded.
- **The Reverse Traversal & Fenwick Tree Architecture:**
  - If we traverse the array **from right to left**, whenever we inspect element $\text{nums}[i]$, the data structure contains **only the elements that appear to its right**!
  - We query the number of active elements with value $< \text{nums}[i]$ in $O(\log N)$ time, then insert $\text{nums}[i]$ into the structure.

---

## 2. Conceptual Foundation & Invariants

### Step A: Coordinate Compression
The values in $\text{nums}$ can range from $-10^4$ to $10^4$.
To map arbitrary integers to compact 1-based ranks:
1. Extract unique sorted values: $\text{alls} = \text{sorted}(\text{set}(\text{nums}))$.
   For $[5, 2, 6, 1] \implies \text{alls} = [1, 2, 5, 6]$.
2. Map each value to its rank $x \in [1, M]$:
   $$
   m = \{1: 1, \; 2: 2, \; 5: 3, \; 6: 4\} \quad (M = 4)
   $$

### Step B: The Fenwick Tree Protocol
Initialize a Binary Indexed Tree of size $M$:
For each value $v$ encountered in reverse order ($\text{nums}[::-1]$):
1. Look up compressed rank: $x = m[v]$.
2. Insert $v$ into the tree by incrementing frequency at rank $x$:
   $$
   \text{tree.update}(x, 1)
   $$
3. Query the number of elements strictly smaller than $v$:
   Because $x$ is the rank of $v$, all values strictly smaller have ranks $\le x - 1$:
   $$
   \text{count} = \text{tree.query}(x - 1)
   $$
4. Append $\text{count}$ to `ans`.
5. Finally, reverse `ans` to restore original left-to-right order: $\text{return } ans[::-1]$.

> **Invariant.** When evaluating element $\text{nums}[i]$, the Fenwick tree holds the multiset of all elements in the suffix $\text{nums}[i+1 \dots N-1]$. $\text{tree.query}(x - 1)$ returns the exact count of suffix elements strictly smaller than $\text{nums}[i]$.

---

## 3. Step-by-Step Worked Execution

We trace the reverse pass on $\text{nums} = [5, 2, 6, 1]$:
Rank dictionary: $m = \{1: 1, 2: 2, 5: 3, 6: 4\}$.
Tree size $M = 4$. Initial tree `c = [0, 0, 0, 0, 0]`.

---

### Step 1: Process $v = 1$ (Index 3, Original Suffix: Empty)
- Rank: $x = m[1] = 1$.
- Insert rank 1: $\text{tree.update}(1, 1)$.
  - Updates node $1$ and ancestor nodes $2, 4$.
- Query count strictly smaller than 1:
  $$
  \text{count} = \text{tree.query}(x - 1) = \text{tree.query}(0) = \mathbf{0}
  $$
- Record: `ans = [0]`.

---

### Step 2: Process $v = 6$ (Index 2, Original Suffix: $[1]$)
- Rank: $x = m[6] = 4$.
- Insert rank 4: $\text{tree.update}(4, 1)$.
  - Updates node $4$.
- Query count strictly smaller than 6:
  $$
  \text{count} = \text{tree.query}(x - 1) = \text{tree.query}(3)
  $$
  - Node values covering ranks $1..3$: only rank 1 has been inserted.
  - $\text{tree.query}(3) = \mathbf{1}$ (Element $1$).
- Record: `ans = [0, 1]`.

---

### Step 3: Process $v = 2$ (Index 1, Original Suffix: $[6, 1]$)
- Rank: $x = m[2] = 2$.
- Insert rank 2: $\text{tree.update}(2, 1)$.
  - Updates node $2$ and ancestor node $4$.
- Query count strictly smaller than 2:
  $$
  \text{count} = \text{tree.query}(x - 1) = \text{tree.query}(1)
  $$
  - Node values covering rank 1: element $1$ has frequency 1.
  - $\text{tree.query}(1) = \mathbf{1}$ (Element $1$).
- Record: `ans = [0, 1, 1]`.

---

### Step 4: Process $v = 5$ (Index 0, Original Suffix: $[2, 6, 1]$)
- Rank: $x = m[5] = 3$.
- Insert rank 3: $\text{tree.update}(3, 1)$.
  - Updates node $3$ and ancestor node $4$.
- Query count strictly smaller than 5:
  $$
  \text{count} = \text{tree.query}(x - 1) = \text{tree.query}(2)
  $$
  - Sum of frequencies at ranks $1$ and $2$: element $1$ (count 1) and element $2$ (count 1).
  - $\text{tree.query}(2) = 1 + 1 = \mathbf{2}$ (Elements $\{1, 2\}$).
- Record: `ans = [0, 1, 1, 2]`.

---

### Step 5: Reverse Collected Results
Reverse `ans`:
$$
\text{ans}[::-1] = \mathbf{[2, 1, 1, 0]}
$$

---

## 4. Complete Execution Trace

```text
nums = [5, 2, 6, 1]
ranks: {1: 1, 2: 2, 5: 3, 6: 4}

Reverse Scan:
1. v = 1 (rank 1): update(1, 1) -> query(0) = 0 -> ans = [0]
2. v = 6 (rank 4): update(4, 1) -> query(3) = 1 -> ans = [0, 1]
3. v = 2 (rank 2): update(2, 1) -> query(1) = 1 -> ans = [0, 1, 1]
4. v = 5 (rank 3): update(3, 1) -> query(2) = 2 -> ans = [0, 1, 1, 2]

Reversing ans: [2, 1, 1, 0]
```

| Traversal Order | Element $v$ | Original Index $i$ | Rank $x$ | Suffix Present in Tree | Query Bound $(x - 1)$ | Query Result | Recorded `ans` |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 1st | 1 | 3 | 1 | $\{1\}$ | 0 | **0** | `[0]` |
| 2nd | 6 | 2 | 4 | $\{1, 6\}$ | 3 | **1** | `[0, 1]` |
| 3rd | 2 | 1 | 2 | $\{1, 6, 2\}$ | 1 | **1** | `[0, 1, 1]` |
| 4th | 5 | 0 | 3 | $\{1, 6, 2, 5\}$ | 2 | **2** | `[0, 1, 1, 2]` |
| **End** | - | - | - | - | - | - | **Final: `[2, 1, 1, 0]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because the array is traversed from right to left, the tree contains only values from indices $j > i$. Querying $\text{tree.query}(x - 1)$ sums the frequencies of all ranks $\le x - 1$, which correspond to numbers strictly less than $\text{nums}[i]$. Thus, no elements to the left or equal/greater values are included.

**Completeness.** Every element in $\text{nums}$ is mapped to a valid rank in $[1, M]$. Since every element is processed and inserted, all $N$ suffix intervals are evaluated in reverse order. Reversing the output reconstructs the exact solution for the original array order.

---

## 6. Traps This Instance Exposes

- **Strict Inequality vs Non-Strict:** The query must evaluate $x - 1$, NOT $x$. Evaluating `query(x)` would include equal values, returning the count of elements $\le \text{nums}[i]$ instead of strictly $< \text{nums}[i]$.
- **Right-to-Left vs Left-to-Right:** Scanning left-to-right would require tracking which elements are to the right and deleting them, which is complicated. Reversing the input transforms the problem into standard online prefix accumulation.
- **Large Value Domains:** Values can be negative (e.g. $-10^4$). Direct array indexing fails on negative or sparse large numbers. Coordinate compression maps any range into a contiguous positive sequence $[1, M]$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$.
  - Coordinate compression: Sorting unique elements takes $O(N \log N)$.
  - Reverse traversal: $N$ iterations. In each iteration, `tree.update` and `tree.query` visit at most $\lceil \log_2 M \rceil \le \lceil \log_2 N \rceil$ tree nodes. Total tree operations cost $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the rank dictionary $m$ and the Fenwick tree array of size $M + 1 \le N + 1$.