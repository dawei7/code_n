# Guided Example: K-th Smallest Prime Fraction

We trace the step-by-step rational fraction ordering ($arr[i] / arr[j]$ for $i < j$), multi-list monotonicity decomposition across fixed denominators ($j$), $N-1$ way priority queue min-heap seeding ($(arr[0]/arr[j], 0, j)$), greedy successive pop-and-advance transitions ($i \to i + 1$), boundary termination ($i + 1 < j$), and $k$-th rank extraction on representative sorted prime sequences:

- **Input:**
  $$
  arr = [1, 2, 3, 5], \quad k = 3
  $$
- **Required output:**
  $$
  [2, 5]
  $$
  - Fraction construction rules:
    - Array $arr$ is strictly sorted in ascending order.
    - Consider every pair of indices $(i, j)$ with $0 \le i < j < n$, forming the fraction:
      $$
      F(i, j) = \frac{arr[i]}{arr[j]}
      $$
    - Because $arr[i] < arr[j]$, every fraction satisfies $0 < F(i, j) < 1$.
    - Total fractions formed:
      $$
      \binom{n}{2} = \frac{4 \times 3}{2} = 6 \text{ fractions}
      $$
    - Enumerate and sort all 6 fractions:
      1. $1/5 = 0.200$
      2. $1/3 \approx 0.333$
      3. **$2/5 = 0.400$**
      4. $1/2 = 0.500$
      5. $3/5 = 0.600$
      6. $2/3 \approx 0.667$
    - The 3rd smallest fraction is **$2/5$** $\implies$ return $[2, 5]$.
- **Monotonic Column Lists & Min-Heap Invariant:**
  - **The Sorted Sub-List Decomposition:**
    - For any fixed denominator index $j \in [1, n - 1]$, as numerator index $i$ increases from $0$ to $j - 1$:
      $$
      \frac{arr[0]}{arr[j]} < \frac{arr[1]}{arr[j]} < \frac{arr[2]}{arr[j]} < \dots < \frac{arr[j - 1]}{arr[j]}
      $$
    - This partitions the $\binom{n}{2}$ fractions into $n - 1$ **independent sorted lists**, one for each denominator $arr[j]$!
  - **Multi-Way Merge Priority Queue:**
    - Instead of sorting all $\binom{n}{2}$ fractions ($O(N^2 \log N)$), maintain a min-heap containing the smallest currently available fraction from each of the $n - 1$ lists:
      $$
      h = \left\{ \left(\frac{arr[0]}{arr[j]}, \; 0, \; j\right) \;\middle|\; j \in [1, n - 1] \right\}
      $$
    - Size of the heap is at most $n - 1$.
  - **Pop-and-Advance Step:**
    - Pop the global minimum $(val, i, j)$ from the heap.
    - If the current list has a next element ($i + 1 < j$):
      - Push the successor: $(arr[i + 1] / arr[j], \; i + 1, \; j)$.
    - Repeating this $k - 1$ times discards the smallest $k - 1$ fractions.
    - The element remaining at the top of the heap is guaranteed to be the $k$-th smallest!
- **Step-by-Step Worked Execution Trace on $arr = [1, 2, 3, 5], k = 3$:**
  - Denominator indices:
    - List 1 ($j = 1$, denom 2): $[1/2]$
    - List 2 ($j = 2$, denom 3): $[1/3, \; 2/3]$
    - List 3 ($j = 3$, denom 5): $[1/5, \; 2/5, \; 3/5]$
  - **Phase 0: Seed Min-Heap with $i = 0$ for all $j \in [1, 3]$:**
    - From List 1: $1/2 = 0.500 \implies (0.500, 0, 1)$
    - From List 2: $1/3 \approx 0.333 \implies (0.333, 0, 2)$
    - From List 3: $1/5 = 0.200 \implies (0.200, 0, 3)$
    - Min-Heap status:
      $$
      h = [ (0.200, 0, 3), \; (0.333, 0, 2), \; (0.500, 0, 1) ]
      $$
  - **Step 1 (Extract 1st Smallest):**
    - Pop minimum: $(0.200, i = 0, j = 3)$, representing $1/5$.
    - Advance in List 3: $i + 1 = 1 < 3 \implies$ push $(arr[1] / arr[3], 1, 3) = (2/5, 1, 3)$:
      $$
      \text{Value } = 2 / 5 = \mathbf{0.400}
      $$
    - Heap updated:
      $$
      h = [ (0.333, 0, 2), \; (0.400, 1, 3), \; (0.500, 0, 1) ]
      $$
  - **Step 2 (Extract 2nd Smallest):**
    - Pop minimum: $(0.333, i = 0, j = 2)$, representing $1/3$.
    - Advance in List 2: $i + 1 = 1 < 2 \implies$ push $(arr[1] / arr[2], 1, 2) = (2/3, 1, 2)$:
      $$
      \text{Value } = 2 / 3 \approx \mathbf{0.667}
      $$
    - Heap updated:
      $$
      h = [ (\mathbf{0.400}, 1, 3), \; (0.500, 0, 1), \; (0.667, 1, 2) ]
      $$
  - **Step 3 (Extract 3rd Smallest = Target):**
    - The current top of the heap is:
      $$
      h[0] = (0.400, \; i = 1, \; j = 3)
      $$
    - Numerator: $arr[i] = arr[1] = \mathbf{2}$.
    - Denominator: $arr[j] = arr[3] = \mathbf{5}$.
    - Fraction:
      $$
      ans = [\mathbf{2}, \; \mathbf{5}]
      $$
- **Single Available Fraction Trace ($arr = [1, 7], k = 1$):**
  - Only one pair possible: $(i = 0, j = 1) \implies 1/7$.
  - Heap has 1 element, 0 pops $\implies$ returns `[1, 7]`.
- **Largest Fraction Extraction ($k = \binom{n}{2}$):**
  - Continuous pops empty lower elements until only the largest element $(arr[n - 2] / arr[n - 1])$ remains.

This instance demonstrates $K$-way merge sort on partially ordered multisets and priority queue stream scheduling, mathematically proves why advancing list iterators maintains the upper-contour frontier of rational lattices, and derives $O(N + K \log N)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted array $arr$ of primes and 1:
Find the **$k$-th smallest fraction** $arr[i] / arr[j]$ with $i < j$.

```text
arr = [ 1, 2, 3, 5 ], k = 3

Fractions grouped by denominator:
  Denom 2: [ 1/2 ]
  Denom 3: [ 1/3, 2/3 ]
  Denom 5: [ 1/5, 2/5, 3/5 ]

Seed min-heap with smallest from each list:
  Heap: [ 1/5 (0.2), 1/3 (0.33), 1/2 (0.5) ]

Pop 1: 1/5 popped -> push 2/5 (0.4)
Pop 2: 1/3 popped -> push 2/3 (0.67)

Top of heap is 2/5!
Result: [ 2, 5 ]
```

### The Invariant of the $K$-Way List Merge
- For each denominator $arr[j]$, fractions are already sorted: $arr[0]/arr[j] < arr[1]/arr[j] < \dots$.
- Using a min-heap of size $N - 1$, we merge these $N - 1$ sorted lists.
- Discarding $k - 1$ smallest elements leaves the $k$-th smallest at the top of the heap.

---

## 2. Conceptual Foundation & Invariants

### 1. Monotonic List Partition:
$$
L_j = \left( \frac{arr[0]}{arr[j]}, \; \frac{arr[1]}{arr[j]}, \; \dots, \; \frac{arr[j - 1]}{arr[j]} \right) \quad \forall j \in [1, n - 1]
$$

### 2. Min-Heap Transition:
$$
(val, i, j) \leftarrow heappop(h)
$$
$$
\text{if } i + 1 < j \implies heappush\left(h, \; \left(\frac{arr[i + 1]}{arr[j]}, \; i + 1, \; j\right)\right)
$$

> **Poset Antichain Frontier Invariant.** The set of pairs $(i, j)$ forms a product poset ordered by coordinate domination $(i, -j) \le (i', -j')$. The min-heap dynamically traces the minimal antichain frontier of unvisited elements in $O(k \log N)$ time.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [1, 2, 3, 5], k = 3$:

---

### Step 1: Initial Heap
- $1/5 = 0.200$
- $1/3 \approx 0.333$
- $1/2 = 0.500$

---

### Step 2: Pop 1
- Pop $1/5 \implies$ push $2/5 = 0.400$.
- Heap: $1/3, 2/5, 1/2$.

---

### Step 3: Pop 2
- Pop $1/3 \implies$ push $2/3 \approx 0.667$.
- Heap: $2/5, 1/2, 2/3$.

---

### Step 4: Output
- Top is $2/5 \implies \mathbf{[2, 5]}$.

---

## 4. Complete Execution Trace

| Extraction Step | Popped Fraction | Decimal Value | Successor Added to Heap | New Heap Top |
|:---:|:---:|:---:|:---:|:---:|
| Initial | — | — | Seed all numerators $0$ | $1/5$ ($0.200$) |
| $1$ | $1/5$ | $0.200$ | $2/5$ ($0.400$) | $1/3$ ($0.333$) |
| $2$ | $1/3$ | $0.333$ | $2/3$ ($0.667$) | **$2/5$ ($0.400$)** |
| **Target ($k=3$)** | — | — | — | **`[2, 5]`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimal Length ($N = 2, k = 1$):** Exactly 1 fraction $arr[0] / arr[1] \implies$ returns $[arr[0], arr[1]]$.
- **Largest Fraction ($k = \binom{n}{2}$):** Heap empties predecessors; final fraction is $[arr[n-2], arr[n-1]]$.
- **List Depletion ($i + 1 == j$):** When numerator reaches $j - 1$, no more valid fractions exist for that denominator; nothing is pushed.
- **Large $N$:** Heap holds at most $N - 1$ elements; memory remains strictly $O(N)$.

---

## 6. Traps & Common Anti-Patterns

- **Generating and Sorting All $\binom{n}{2}$ Fractions ($O(N^2 \log N)$):** For $N = 1000$, $\binom{n}{2} \approx 5 \times 10^5$ fractions. Generating all pairs takes large memory and time. The $K$-way heap merge runs in $O(N + K \log N)$.
- **Floating Point Equality Issues:** Fractions are distinct because $arr$ contains 1 and primes. Floating-point `1 / y` values maintain strict sorting order.
- **Index Out of Bounds:** A fraction requires $i < j$. Advancing numerator $i + 1$ must check $i + 1 < j$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initializing heap of size $N - 1$: $\mathcal{O}(N)$.
  - $k - 1$ extract-min and insert operations: $\mathcal{O}(K \log N)$.
  - Total Time: strictly $\mathcal{O}(N + K \log N)$ where $N \le 1000, K \le \binom{N}{2}$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the min-heap.
