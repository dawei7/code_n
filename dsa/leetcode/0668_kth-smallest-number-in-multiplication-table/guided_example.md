# Guided Example: Kth Smallest Number in Multiplication Table

We trace the step-by-step binary search over the value domain ($x \in [1, m \cdot n]$), row-wise integer division rank counting ($cnt = \sum \min(\lfloor mid / i \rfloor, n)$), monotonic cumulative frequency mapping, boundary contraction ($cnt \ge k \implies right = mid$), and $k$-th order statistic isolation on representative multiplication table grids:

- **Input:** $m = 3, \quad n = 3, \quad k = 5$
- **Required output:** `3`
  - Multiplication table structure ($1$-indexed):
    $$
    M = \begin{bmatrix}
    1 \times 1 & 1 \times 2 & 1 \times 3 \\
    2 \times 1 & 2 \times 2 & 2 \times 3 \\
    3 \times 1 & 3 \times 2 & 3 \times 3
    \end{bmatrix} = \begin{bmatrix}
    1 & 2 & 3 \\
    2 & 4 & 6 \\
    3 & 6 & 9
    \end{bmatrix}
    $$
  - Flattened sorted multiset:
    $$
    [1, \; 2, \; 2, \; 3, \; \mathbf{3}, \; 4, \; 6, \; 6, \; 9]
    $$
  - Objective: Find the $k$-th element ($k = 5$), which is **$3$**.
- **Binary Search on the Solution & Row-wise Counting Invariant:**
  - **The Counting Predicate ($cnt(x)$):**
    - Instead of generating and sorting all $m \cdot n$ elements, we pose the decision question:
      *How many numbers in the multiplication table are less than or equal to candidate value $x$?*
    - In row $i$, the elements are the arithmetic progression:
      $$
      i \times 1, \; i \times 2, \; i \times 3, \dots, i \times n
      $$
    - An element $i \cdot j$ is $\le x$ if and only if $j \le \lfloor x / i \rfloor$.
    - Because each row contains at most $n$ entries, the number of valid entries in row $i$ is capped at $n$:
      $$
      count_i(x) = \min\left( \left\lfloor \frac{x}{i} \right\rfloor, \; n \right)
      $$
    - Summing across all $m$ rows gives the exact count in $\mathcal{O}(m)$ time:
      $$
      cnt(x) = \sum_{i=1}^m \min\left( \left\lfloor \frac{x}{i} \right\rfloor, \; n \right)
      $$
  - **Monotonicity & Bisection:**
    - As $x$ increases, $cnt(x)$ is non-decreasing.
    - If $cnt(x) \ge k$:
      - There are at least $k$ elements $\le x$. The $k$-th smallest could be $x$ or something smaller:
        $$
        right \leftarrow mid
        $$
    - If $cnt(x) < k$:
      - Strictly fewer than $k$ elements are $\le x$. The $k$-th smallest must be strictly greater than $x$:
        $$
        left \leftarrow mid + 1
        $$
- **Step-by-Step Worked Execution Trace on $m = 3, n = 3, k = 5$:**
  - Search range:
    $$
    left = 1, \quad right = m \times n = 3 \times 3 = 9
    $$
  - **Iteration 1 ($left = 1, \; right = 9$):**
    - Midpoint:
      $$
      mid = \lfloor (1 + 9) / 2 \rfloor = \mathbf{5}
      $$
    - Count elements $\le 5$:
      - Row 1 ($i = 1$): $\min(\lfloor 5/1 \rfloor, 3) = \min(5, 3) = \mathbf{3}$ (Values: $1, 2, 3$)
      - Row 2 ($i = 2$): $\min(\lfloor 5/2 \rfloor, 3) = \min(2, 3) = \mathbf{2}$ (Values: $2, 4$)
      - Row 3 ($i = 3$): $\min(\lfloor 5/3 \rfloor, 3) = \min(1, 3) = \mathbf{1}$ (Values: $3$)
    - Total count:
      $$
      cnt(5) = 3 + 2 + 1 = \mathbf{6}
      $$
    - Compare with $k = 5$:
      $$
      cnt = 6 \ge 5 \implies \mathbf{Feasible}
      $$
    - Contract right boundary:
      $$
      right \leftarrow mid = \mathbf{5}
      $$
  - **Iteration 2 ($left = 1, \; right = 5$):**
    - Midpoint:
      $$
      mid = \lfloor (1 + 5) / 2 \rfloor = \mathbf{3}
      $$
    - Count elements $\le 3$:
      - Row 1 ($i = 1$): $\min(\lfloor 3/1 \rfloor, 3) = \min(3, 3) = \mathbf{3}$ (Values: $1, 2, 3$)
      - Row 2 ($i = 2$): $\min(\lfloor 3/2 \rfloor, 3) = \min(1, 3) = \mathbf{1}$ (Values: $2$)
      - Row 3 ($i = 3$): $\min(\lfloor 3/3 \rfloor, 3) = \min(1, 3) = \mathbf{1}$ (Values: $3$)
    - Total count:
      $$
      cnt(3) = 3 + 1 + 1 = \mathbf{5}
      $$
    - Compare with $k = 5$:
      $$
      cnt = 5 \ge 5 \implies \mathbf{Feasible}
      $$
    - Contract right boundary:
      $$
      right \leftarrow mid = \mathbf{3}
      $$
  - **Iteration 3 ($left = 1, \; right = 3$):**
    - Midpoint:
      $$
      mid = \lfloor (1 + 3) / 2 \rfloor = \mathbf{2}
      $$
    - Count elements $\le 2$:
      - Row 1 ($i = 1$): $\min(\lfloor 2/1 \rfloor, 3) = \mathbf{2}$ (Values: $1, 2$)
      - Row 2 ($i = 2$): $\min(\lfloor 2/2 \rfloor, 3) = \mathbf{1}$ (Values: $2$)
      - Row 3 ($i = 3$): $\min(\lfloor 2/3 \rfloor, 3) = \mathbf{0}$
    - Total count:
      $$
      cnt(2) = 2 + 1 + 0 = \mathbf{3}
      $$
    - Compare with $k = 5$:
      $$
      cnt = 3 < 5 \implies \mathbf{Too\ Small!}
      $$
    - Advance left boundary:
      $$
      left \leftarrow mid + 1 = 2 + 1 = \mathbf{3}
      $$
  - **Termination:**
    - Now $left = 3$ and $right = 3$ ($left == right$).
    - Search terminates with answer:
      $$
      ans = left = \mathbf{3}
      $$
- **Largest Entry ($m = 2, n = 3, k = 6$):**
  - Table: $[1, 2, 3]$ and $[2, 4, 6]$.
  - $k = 6$ (total elements) $\implies$ maximum entry is $6$.
- **Duplicates Across Ranks:**
  - If multiple copies of a number exist (e.g. value 3 appears twice at ranks 4 and 5), the smallest integer $x$ with $cnt(x) \ge 5$ is precisely 3.

This instance demonstrates range bisection on implicit matrices and rank projection, mathematically proves why divisor counting over product semigroups maps monotonically to empirical cumulative distributions, and derives $O(m \log(mn))$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ multiplication table and rank $k$:
Find the **$k$-th smallest number** in the table.

```text
Table (3 x 3):
  Row 1:  1  2  3
  Row 2:  2  4  6
  Row 3:  3  6  9

Sorted: [ 1, 2, 2, 3, 3, 4, 6, 6, 9 ]
k = 5 -> 5th element is 3.
```

### The Invariant of Row-Wise Divisor Counting
- In row $i$, the number of multiples $\le x$ is:
  $$
  count = \min\left(\lfloor x / i \rfloor, \; n\right)
  $$
- This counts how many elements in the entire table are $\le x$ in strictly $O(m)$ time without generating the grid.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cumulative Count Function:
$$
cnt(x) = \sum_{i=1}^m \min\left(\lfloor x / i \rfloor, \; n\right)
$$

### 2. Binary Search Monotonicity:
- If $cnt(mid) \ge k \implies right = mid$
- If $cnt(mid) < k \implies left = mid + 1$
Search interval converges to the exact $k$-th smallest element.

> **Hyperbolic Lattice Counting Invariant.** The function $cnt(x) = \sum_{i=1}^m \min(\lfloor x/i \rfloor, n)$ represents the lattice point cardinality under the hyperbolic bound $i \cdot j \le x$ inside the rectangle $[1, m] \times [1, n]$, which is monotonically non-decreasing in $x$.

---

## 3. Step-by-Step Worked Execution

We trace $m = 3, n = 3, k = 5$:

---

### Step 1: Test $mid = 5$
- Row 1: $\min(5, 3) = 3$.
- Row 2: $\min(2, 3) = 2$.
- Row 3: $\min(1, 3) = 1$.
- $cnt = 3 + 2 + 1 = 6 \ge 5 \implies right \leftarrow 5$.

---

### Step 2: Test $mid = 3$
- Row 1: $\min(3, 3) = 3$.
- Row 2: $\min(1, 3) = 1$.
- Row 3: $\min(1, 3) = 1$.
- $cnt = 3 + 1 + 1 = 5 \ge 5 \implies right \leftarrow 3$.

---

### Step 3: Test $mid = 2$
- Row 1: $\min(2, 3) = 2$.
- Row 2: $\min(1, 3) = 1$.
- Row 3: $\min(0, 3) = 0$.
- $cnt = 3 < 5 \implies left \leftarrow 2 + 1 = 3$.

---

### Step 4: Output
- $left = right = \mathbf{3}$.

---

## 4. Complete Execution Trace

| Search Interval $[left, right]$ | Candidate $mid$ | Row Counts $(Row_1, Row_2, Row_3)$ | Total Count $cnt(mid)$ | $cnt \ge 5$? | Range Next |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[1, 9]$ | $5$ | $(3, 2, 1)$ | $6$ | Yes | $right \leftarrow 5$ |
| $[1, 5]$ | $3$ | $(3, 1, 1)$ | $5$ | Yes | $right \leftarrow 3$ |
| $[1, 3]$ | $2$ | $(2, 1, 0)$ | $3$ | No | $left \leftarrow 3$ |
| **Converged** | **`3`** | — | — | — | **Result: `3`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** Always returns 1.
- **$k = m \cdot n$:** Always returns $m \cdot n$.
- **$1 \times N$ Grid:** Equivalent to standard 1D array $1 \dots n \implies$ returns $k$.
- **Large Dimensions ($m = 3 \times 10^4, n = 3 \times 10^4$):** $m \cdot n = 9 \times 10^8$. Binary search takes $\log_2(9 \times 10^8) \approx 30$ steps; $30 \times 3 \times 10^4 \approx 9 \times 10^5$ operations, completing in $< 20$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Generating the Whole Matrix ($O(M \cdot N)$ Space & Time):** For $m = n = 3 \times 10^4$, creating an array of $9 \times 10^8$ numbers requires several gigabytes of memory and causes Out Of Memory / Time Limit Exceeded.
- **Using Min-Heap ($O(K \log M)$):** For $k = 5 \times 10^8$, a heap takes hundreds of millions of operations. Binary search on value space runs in strictly $\mathcal{O}(M \log(MN))$ time.
- **Forgetting Row Width Cap:** Failing to write $\min(\lfloor x/i \rfloor, n)$ allows $j$ to exceed $n$, overcounting elements beyond the table boundary.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Range size: $R = m \cdot n$.
  - Number of bisections: $\mathcal{O}(\log(m \cdot n))$.
  - In each bisection, loop runs $m$ iterations: $\mathcal{O}(m)$.
  - (Assuming $m \le n$; if $m > n$, swap $m$ and $n$ so loop runs $\min(m, n)$ times).
  - Total Time: $\mathcal{O}(\min(m, n) \log(m \cdot n))$. Completes in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.