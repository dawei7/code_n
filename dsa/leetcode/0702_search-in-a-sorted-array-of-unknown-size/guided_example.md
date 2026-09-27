# Guided Example: Search in a Sorted Array of Unknown Size

We trace the step-by-step exponential galloping range expansion ($r \leftarrow 2r$), out-of-bounds sentinel absorption ($reader.get(k) = 2^{31}-1$), interval bounding ($[r/2, r]$), logarithmic binary search bisection, target equality verification ($reader.get(l) == target$), and missing element rejection ($-1$) on representative sorted stream queries:

- **Input:** $reader = [-1, 0, 3, 5, 9, 12], \quad target = 9$
- **Required output:** `4`
  - Array interface rules:
    - Elements are strictly sorted in ascending order.
    - The array length is unknown.
    - Calling `reader.get(k)` returns the element at index $k$.
    - If index $k$ exceeds the length of the array, `reader.get(k)` returns the sentinel value $2^{31} - 1 = 2147483647$.
    - Objective: Locate the index of $target = 9$ in logarithmic time $O(\log N)$. If $target$ is absent, return $-1$.
    - For the input array: $reader[4] = 9$. The target index is **4**.
- **Exponential Galloping & Binary Search Invariant:**
  - **The Two-Phase Architecture:**
    - Without knowing the array length, standard binary search cannot immediately set a right boundary.
    - **Phase 1: Exponential Galloping (Doubling Search):**
      - Start with probe $r = 1$.
      - As long as `reader.get(r) < target`, double the upper bound:
        $$
        r \leftarrow r \times 2
        $$
      - If $r$ lands beyond the array, `reader.get(r)` returns $2^{31} - 1$, which is $\ge target$ (since $target \le 10^4$).
      - Thus, galloping is guaranteed to terminate in at most $1 + \lceil \log_2(\text{target index}) \rceil$ steps.
    - **Phase 2: Confined Binary Search:**
      - The target is strictly enclosed in the finite interval:
        $$
        l = \lfloor r / 2 \rfloor, \quad \text{range: } [l, \; r]
        $$
      - Execute standard binary search over interval $[l, r]$.
      - Return $l$ if $reader.get(l) == target$, else $-1$.
- **Step-by-Step Worked Execution Trace on $reader = [-1, 0, 3, 5, 9, 12]$ for $target = 9$:**
  - **Phase 1: Exponential Galloping:**
    - Initial probe: $r = 1$.
    - **Probe $r = 1$:**
      - Call: $reader.get(1) = 0$.
      - Compare: $0 < 9 \implies \mathbf{Target\ is\ Further\ Right}$.
      - Double right bound:
        $$
        r \leftarrow 1 \times 2 = \mathbf{2}
        $$
    - **Probe $r = 2$:**
      - Call: $reader.get(2) = 3$.
      - Compare: $3 < 9 \implies \mathbf{Target\ is\ Further\ Right}$.
      - Double right bound:
        $$
        r \leftarrow 2 \times 2 = \mathbf{4}
        $$
    - **Probe $r = 4$:**
      - Call: $reader.get(4) = 9$.
      - Compare: $9 \ge target \implies \mathbf{Upper\ Bound\ Bracketed!}$
      - Galloping halts.
  - **Phase 2: Confined Binary Search:**
    - Lower boundary: $l = r \gg 1 = 4 \gg 1 = \mathbf{2}$.
    - Upper boundary: $r = \mathbf{4}$.
    - Search interval: $[l, r] = [2, 4]$.
    - **Iteration 1:**
      - Midpoint:
        $$
        mid = \lfloor (2 + 4) / 2 \rfloor = \mathbf{3}
        $$
      - Query: $reader.get(3) = 5$.
      - Compare: $5 < 9 \implies$ Target lies strictly to the right of 3.
      - Contract left boundary:
        $$
        l \leftarrow mid + 1 = 3 + 1 = \mathbf{4}
        $$
    - **Iteration 2:**
      - Pointers converge: $l = 4, \; r = 4 \implies l == r$.
      - Binary search loop terminates.
  - **Step 3: Verification:**
    - Query candidate index: $reader.get(l) = reader.get(4) = 9$.
    - $9 == target \implies \mathbf{Match\ Confirmed!}$
    - Return target index:
      $$
      ans = \mathbf{4}
      $$
- **Absent Element Trace ($reader = [-1, 0, 3, 5, 9, 12], target = 2$):**
  - Galloping:
    - $r = 1$: $get(1) = 0 < 2 \implies r \leftarrow 2$.
    - $r = 2$: $get(2) = 3 \ge 2 \implies$ Upper bound bracketed at $r = 2$.
  - Binary search in $[1, 2]$:
    - $mid = 1$: $get(1) = 0 < 2 \implies l \leftarrow 2$.
    - Convergence at $l = 2$.
  - Verification: $reader.get(2) = 3 \ne 2$.
  - Return **`-1`**.
- **Target at Index 0 ($target = -1$):**
  - Galloping starts at $r = 1$: $get(1) = 0 \ge -1$.
  - Range $[0, 1] \implies mid = 0$, matches immediately at index 0.

This instance demonstrates unbounded search via exponential galloping and two-phase interval bisection, mathematically proves why doubling search preserves $O(\log N)$ optimality on infinite semi-lines, and derives $O(\log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an `ArrayReader` with unknown length:
Find the index of $target$ in $O(\log N)$ time.
Out-of-bounds calls return $2^{31} - 1$.
If absent, return $-1$.

```text
reader = [ -1, 0, 3, 5, 9, 12 ], target = 9

Phase 1: Exponential Galloping
  r = 1: get(1) = 0 < 9  -> double r to 2
  r = 2: get(2) = 3 < 9  -> double r to 4
  r = 4: get(4) = 9 >= 9 -> BRACKETED!

Phase 2: Binary Search in [2, 4]
  mid = 3: get(3) = 5 < 9 -> l = 4
  l = 4, r = 4 -> converged!

Verification: get(4) == 9 -> return 4
```

### The Invariant of Galloping Range Bounding
- Any unknown positive index $T$ satisfies $2^{k-1} \le T \le 2^k$ for some integer $k$.
- Repeatedly doubling $r$ brackets $T$ in at most $\lceil \log_2 T \rceil$ probes.
- Once bracketed, binary search over $[r/2, r]$ finishes in $\log_2(r/2)$ steps.

---

## 2. Conceptual Foundation & Invariants

### 1. Phase 1: Exponential Galloping:
$$
r \leftarrow 1
$$
$$
\text{While } reader.get(r) < target: \quad r \leftarrow r \ll 1
$$

### 2. Phase 2: Binary Search:
$$
l \leftarrow r \gg 1
$$
$$
\text{While } l < r: \quad mid = (l + r) \gg 1
$$
$$
\text{If } reader.get(mid) \ge target \implies r \leftarrow mid \quad \text{else} \quad l \leftarrow mid + 1
$$

> **Galloping Search Bound Invariant.** For an unknown monotone function $f: \mathbb{N} \to \mathbb{R}$, repeated doubling identifies an interval $[2^{k-1}, 2^k]$ containing $x^* = \min \{x \mid f(x) \ge target\}$ in $2\lceil \log_2 x^* \rceil$ point evaluations.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Galloping
- $r = 1: get(1) = 0 < 9 \implies r \leftarrow 2$.
- $r = 2: get(2) = 3 < 9 \implies r \leftarrow 4$.
- $r = 4: get(4) = 9 \ge 9 \implies$ Stop.

---

### Step 2: Binary Search
- $l = 2, r = 4$.
- $mid = 3: get(3) = 5 < 9 \implies l \leftarrow 4$.
- Loop ends ($l = r = 4$).

---

### Step 3: Verification
- $reader.get(4) = 9 == target \implies$ Return **`4`**.

---

## 4. Complete Execution Trace

| Phase | Probe / Range | Evaluated Index | Value Returned | Condition Tested | Bound Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Gallop 1 | $r = 1$ | $1$ | $0$ | $0 < 9$ (True) | $r \leftarrow 2$ |
| Gallop 2 | $r = 2$ | $2$ | $3$ | $3 < 9$ (True) | $r \leftarrow 4$ |
| Gallop 3 | $r = 4$ | $4$ | $9$ | $9 \ge 9$ (Bracketed) | Confine to $[2, 4]$ |
| Binary 1 | $[2, 4]$ | $mid = 3$ | $5$ | $5 < 9$ | $l \leftarrow 4$ |
| **End** | **$l = 4$** | **$4$** | **$9$** | **$9 == 9$ (Match!)** | **Return `4`** |

---

## 5. Boundary Cases & Failure Modes

- **Target at Index 0:** $r = 1$ has $get(1) \ge target$, search in $[0, 1]$ finds 0 immediately.
- **Target Absent Between Elements:** Bounded interval converges to nearest greater element $\implies$ equality check fails $\implies -1$.
- **Target Exceeds All Elements:** Gallops until hitting $2^{31} - 1$, binary search confines to valid range, returns $-1$.
- **Single Element Array ($N = 1$):** Handles correctly via sentinel value $2^{31} - 1$.

---

## 6. Traps & Common Anti-Patterns

- **Linear Search ($O(N)$):** Scanning index by index violates the $O(\log N)$ time limit constraint.
- **Fixed Arbitrary Right Bound ($r = 10000$):** Hardcoding an arbitrary large right bound makes binary search slower when the target is at index 2. Exponential galloping scales adaptively with target position.
- **Treating Sentinel $2^{31}-1$ as an Error:** The problem specifies that $2^{31} - 1$ is returned on out-of-bounds; it acts as $+\infty$ to push binary search to the left.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Galloping takes $\lceil \log_2 T \rceil$ steps where $T$ is the target index.
  - Binary search takes $\lceil \log_2 T \rceil$ steps.
  - Total API calls: at most $2 \lceil \log_2 T \rceil \le 28$ calls.
  - Total Time: strictly logarithmic $\mathcal{O}(\log T)$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only integer pointers $l, r, mid$).