# Guided Example: Intervals Between Identical Elements

We trace the step-by-step execution of the optimal prefix-sum and delta-transition approach on a representative problem instance:

- **Input Array (`arr`):** `[2, 1, 3, 1, 2, 3, 3]`
- **Expected Output:** `[4, 2, 7, 2, 4, 4, 5]`

This instance demonstrates how elements with identical values form independent 1D coordinate groups, how prefix sums or telescopic delta shifts evaluate all pairwise index distances in linear time, and how individual group results are mapped back to their original array positions.

---

## 1. Problem Overview & Representative Instance

Given a 0-indexed array `arr` of length $n$, the interval between two indices $i$ and $j$ is defined as $|i - j|$. For each index $i$, we must compute the sum of intervals between $i$ and all indices $j$ such that $\text{arr}[j] = \text{arr}[i]$.

In our representative instance `arr = [2, 1, 3, 1, 2, 3, 3]`:
- Value $1$ occurs at indices $[1, 3]$.
- Value $2$ occurs at indices $[0, 4]$.
- Value $3$ occurs at indices $[2, 5, 6]$.

Calculating pairwise absolute differences independently for each index in naive fashion would take $\mathcal{O}(n^2)$ time in the worst case (when all elements are identical). By grouping occurrences and applying prefix sum decomposition, we compute all $n$ distance sums in strictly linear time.

---

## 2. Mathematical & Algorithmic Principles

### Equivalence Class Grouping
The problem partitions the index set $\{0, 1, \dots, n-1\}$ into disjoint equivalence classes defined by identical array values:

$$\mathcal{C}_v = \{ i \in \{0, \dots, n-1\} \mid \text{arr}[i] = v \}$$

Because distances only exist between elements sharing the same value, each equivalence class $\mathcal{C}_v$ is completely independent.
Let $\mathcal{C}_v = \{p_0, p_1, \dots, p_{m-1}\}$ be sorted in strictly ascending order: $p_0 < p_1 < \dots < p_{m-1}$.

### Telescopic Delta Transition
For a fixed index $p_k \in \mathcal{C}_v$ ($0 \le k < m$), the total distance sum $D_k$ is:

$$D_k = \sum_{j=0}^{m-1} |p_k - p_j| = \sum_{j=0}^{k-1} (p_k - p_j) + \sum_{j=k+1}^{m-1} (p_j - p_k)$$

At the leftmost occurrence $k = 0$, all other occurrences lie strictly to the right:

$$D_0 = \sum_{j=0}^{m-1} (p_j - p_0) = \left(\sum_{j=0}^{m-1} p_j\right) - m \cdot p_0$$

When advancing from occurrence $k - 1$ to occurrence $k$, the coordinate shifts rightward by $\Delta = p_k - p_{k-1} > 0$:
- For all $k$ occurrences to the left ($p_0, \dots, p_{k-1}$), the distance to the reference point increases by $\Delta$, contributing $+k \cdot \Delta$.
- For all $m - k$ occurrences at or to the right ($p_k, \dots, p_{m-1}$), the distance to the reference point decreases by $\Delta$, contributing $-(m - k) \cdot \Delta$.

Thus, the transition recurrence is:

$$D_k = D_{k-1} + k \cdot \Delta - (m - k) \cdot \Delta = D_{k-1} + (2k - m) \cdot \Delta$$

This single algebraic relation evaluates each subsequent distance sum in $\mathcal{O}(1)$ time.

| Metric | Definition | Role in Computation |
|---|---|---|
| $p_k$ | Sorted index of $k$-th occurrence of value $v$ | Physical location in `arr` |
| $m$ | Total count of occurrences $\lvert \mathcal{C}_v \rvert$ | Class cardinality |
| $\Delta$ | $p_k - p_{k-1}$ | Coordinate displacement between neighbors |
| Left Count ($k$) | Elements with index $< p_k$ | Number of elements whose distance expands by $\Delta$ |
| Right Count ($m - k$) | Elements with index $\ge p_k$ | Number of elements whose distance contracts by $\Delta$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Phase 1: Grouping Indices by Value
Scanning `arr = [2, 1, 3, 1, 2, 3, 3]` from left to right yields:
- Value $1$: indices $[1, 3]$ ($m = 2$)
- Value $2$: indices $[0, 4]$ ($m = 2$)
- Value $3$: indices $[2, 5, 6]$ ($m = 3$)

### Phase 2: Processing Group for Value $1$ ($p = [1, 3]$, $m = 2$)
- **Occurrence $k = 0$ at index $p_0 = 1$:**
  - Initial distance: $D_0 = (p_1 - p_0) = 3 - 1 = 2$.
  - Record: $\text{ans}[1] = 2$.
- **Occurrence $k = 1$ at index $p_1 = 3$:**
  - Displacement: $\Delta = 3 - 1 = 2$.
  - Left count: $k = 1$; Right count: $m - k = 2 - 1 = 1$.
  - Delta update: $D_1 = D_0 + (2 \times 1 - 2) \times 2 = 2 + 0 = 2$.
  - Record: $\text{ans}[3] = 2$.

### Phase 3: Processing Group for Value $2$ ($p = [0, 4]$, $m = 2$)
- **Occurrence $k = 0$ at index $p_0 = 0$:**
  - Initial distance: $D_0 = (p_1 - p_0) = 4 - 0 = 4$.
  - Record: $\text{ans}[0] = 4$.
- **Occurrence $k = 1$ at index $p_1 = 4$:**
  - Displacement: $\Delta = 4 - 0 = 4$.
  - Delta update: $D_1 = D_0 + (2 \times 1 - 2) \times 4 = 4 + 0 = 4$.
  - Record: $\text{ans}[4] = 4$.

### Phase 4: Processing Group for Value $3$ ($p = [2, 5, 6]$, $m = 3$)
- **Occurrence $k = 0$ at index $p_0 = 2$:**
  - Initial distance: $D_0 = (5 - 2) + (6 - 2) = 3 + 4 = 7$.
  - Record: $\text{ans}[2] = 7$.
- **Occurrence $k = 1$ at index $p_1 = 5$:**
  - Displacement: $\Delta = 5 - 2 = 3$.
  - Left count: $k = 1$; Right count: $m - k = 3 - 1 = 2$.
  - Delta update: $D_1 = D_0 + (1 \times 3 - 2 \times 3) = 7 + (3 - 6) = 4$.
  - Record: $\text{ans}[5] = 4$.
- **Occurrence $k = 2$ at index $p_2 = 6$:**
  - Displacement: $\Delta = 6 - 5 = 1$.
  - Left count: $k = 2$; Right count: $m - k = 3 - 2 = 1$.
  - Delta update: $D_2 = D_1 + (2 \times 1 - 1 \times 1) = 4 + (2 - 1) = 5$.
  - Record: $\text{ans}[6] = 5$.

### Assembly of Result Array
Combining values at original indices:
- $\text{ans}[0] = 4$
- $\text{ans}[1] = 2$
- $\text{ans}[2] = 7$
- $\text{ans}[3] = 2$
- $\text{ans}[4] = 4$
- $\text{ans}[5] = 4$
- $\text{ans}[6] = 5$
Final vector: `[4, 2, 7, 2, 4, 4, 5]`.

---

## 4. Comprehensive State Trace

The table below traces the calculations across each equivalence class.

| Value $v$ | Occurrence Rank ($k$) | Array Index ($p_k$) | Step $\Delta$ | Left Term ($+k \Delta$) | Right Term ($-(m-k)\Delta$) | Distance Sum ($D_k$) | Written Target |
|---|---|---|---|---|---|---|---|
| $2$ | $0$ | $0$ | — | — | — | $4$ | $\text{ans}[0] = 4$ |
| $1$ | $0$ | $1$ | — | — | — | $2$ | $\text{ans}[1] = 2$ |
| $3$ | $0$ | $2$ | — | — | — | $7$ | $\text{ans}[2] = 7$ |
| $1$ | $1$ | $3$ | $2$ | $+2$ | $-2$ | $2$ | $\text{ans}[3] = 2$ |
| $2$ | $1$ | $4$ | $4$ | $+4$ | $-4$ | $4$ | $\text{ans}[4] = 4$ |
| $3$ | $1$ | $5$ | $3$ | $+3$ | $-6$ | $4$ | $\text{ans}[5] = 4$ |
| $3$ | $2$ | $6$ | $1$ | $+2$ | $-1$ | $5$ | $\text{ans}[6] = 5$ |

Every computed interval sum matches the required output.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Consider a sorted list of positions $p_0 < p_1 < \dots < p_{m-1}$. The function $f(x) = \sum_{j=0}^{m-1} |x - p_j|$ is piecewise linear and convex. On the open interval $(p_{k-1}, p_k)$, the derivative is constant: $f'(x) = k - (m - k) = 2k - m$. Integrating $f'(x)$ across the displacement $\Delta = p_k - p_{k-1}$ yields $\int_{p_{k-1}}^{p_k} f'(x) dx = (2k - m) \Delta$. Because $f$ is continuous everywhere on $\mathbb{R}$, $f(p_k) = f(p_{k-1}) + (2k - m)\Delta$ holds strictly. Initializing with $D_0 = \sum (p_j - p_0)$ and applying this differential step produces the mathematically exact absolute difference sum for each index.

**Completeness.** Every array index belongs to exactly one value group $\mathcal{C}_v$. Scanning the array populates indices in naturally sorted order, ensuring that no sorting overhead or positional inversion occurs. Every index is assigned its verified distance sum, ensuring complete coverage of the input array.

---

## 6. Edge Cases & Anti-Patterns

- **Singleton Values ($m = 1$):** When an element occurs only once, $D_0 = 0$. The single position receives $0$ immediately without performing delta transitions.
- **All Elements Identical ($m = n$):** All indices belong to a single group. The initial sum takes $\mathcal{O}(n)$ time, and each subsequent index takes $\mathcal{O}(1)$ time, computing the entire array in $\mathcal{O}(n)$ total time instead of $\mathcal{O}(n^2)$.
- **All Elements Distinct:** Each element forms a group of size $1$, yielding an output array filled with zeros in $\mathcal{O}(n)$ time.
- **Anti-Pattern — Nested Loop Comparison:** Iterating over the array and filtering all identical elements for each index results in $\mathcal{O}(n^2)$ time complexity, leading to Time Limit Exceeded on large arrays ($n = 10^5$).

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `arr`. Grouping indices takes one linear pass $\mathcal{O}(n)$. For each group of size $m_i$, computing $D_0$ and performing $m_i - 1$ transitions takes $\mathcal{O}(m_i)$ operations. Across all groups, $\sum m_i = n$, yielding overall linear time $\mathcal{O}(n)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(n)$ to store the hash map of grouped index lists and the output array of size $n$.
