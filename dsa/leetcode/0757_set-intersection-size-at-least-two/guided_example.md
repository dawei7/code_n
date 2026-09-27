# Guided Example: Set Intersection Size At Least Two

We trace the step-by-step end-ascending start-descending interval sorting ($(b, -a)$), greedy right-edge coordinate placement, two-point state tracking ($s, e$), three-way overlap case analysis (zero, one, or two existing points), containing set size minimization, and point selection on representative interval collections:

- **Input:** $intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]$
- **Required output:** `3`
  - Containing set criteria:
    - You must construct an integer set $S$ such that **every interval** $[a, b] \in intervals$ contains **at least two integers** from $S$:
      $$
      \forall [a, b] \in intervals: \quad |S \cap [a, b]| \ge 2
      $$
    - Objective: Find the **minimum possible cardinality** $|S|$.
    - For the input:
      - We can choose set $S = \{2, 3, 5\}$ of size 3:
        - $[1, 3] \cap S = \{2, 3\}$ (size 2 $\ge 2$).
        - $[1, 4] \cap S = \{2, 3\}$ (size 2 $\ge 2$).
        - $[2, 5] \cap S = \{2, 3, 5\}$ (size 3 $\ge 2$).
        - $[3, 5] \cap S = \{3, 5\}$ (size 2 $\ge 2$).
      - Every interval contains at least two points from $S$.
      - No set of size 2 can cover all intervals.
      - Minimum size is **3**.
- **Greedy End-Alignment & 2-Point Tracking Invariant:**
  - **The Canonical Sort Key:**
    - Sort intervals by:
      $$
      \text{key} = (end_i, \; -start_i)
      $$
      - Primary Sort ($end \uparrow$): Intervals that end earliest must be satisfied first to prevent missing their deadlines.
      - Secondary Sort ($start \downarrow$): If two intervals end at the same $end$, the shorter interval (larger $start$) is strictly more restrictive; processing it first ensures its chosen points automatically satisfy the longer interval!
  - **The Two Latest Points Invariant ($s, e$ with $s < e$):**
    - As we scan left to right, we maintain the two largest numbers added to $S$ so far:
      - $e$: The largest point in $S$.
      - $s$: The second-largest point in $S$.
  - **The 3 Mutually Exclusive Cases for Interval $[a, b]$:**
    1. **Case 1 (Two Points Already Covered, $a \le s$):**
       - Both $s$ and $e$ lie within $[a, b]$ (since $a \le s < e \le b$).
       - Interval already contains $\ge 2$ points from $S$.
       - Do nothing: $ans$ unchanged, proceed.
    2. **Case 2 (Zero Points Covered, $a > e$):**
       - Neither $s$ nor $e$ lies inside $[a, b]$ ($e < a$).
       - We must add 2 brand new points to $S$.
       - To maximize their utility for future intervals, greedily choose the **two rightmost possible integers** in $[a, b]$:
         $$
         s \leftarrow b - 1, \quad e \leftarrow b
         $$
       - Increment: $ans \leftarrow ans + 2$.
    3. **Case 3 (Exactly One Point Covered, $s < a \le e$):**
       - Point $e$ is inside $[a, b]$, but $s$ is outside ($s < a$).
       - We need exactly 1 additional point.
       - Greedily choose the **rightmost point** $b$:
         $$
         s \leftarrow e, \quad e \leftarrow b
         $$
       - Increment: $ans \leftarrow ans + 1$.
- **Step-by-Step Worked Execution Trace on $intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]$:**
  - **Phase 0: Sort Intervals:**
    - Initial: `[[1, 3], [1, 4], [2, 5], [3, 5]]`.
    - Key $(end, -start)$:
      - `[1, 3]` $\to (3, -1)$
      - `[1, 4]` $\to (4, -1)$
      - `[3, 5]` $\to (5, -3)$
      - `[2, 5]` $\to (5, -2)$
    - Sorted sequence:
      $$
      \text{Sorted: } [[1, 3], \; [1, 4], \; [3, 5], \; [2, 5]]
      $$
  - **Phase 1: Initialize State:**
    $$
    s = -1, \quad e = -1, \quad ans = 0
    $$
  - **Interval 1: $[a, b] = [1, 3]$:**
    - Compare $a = 1$ with $e = -1$:
      $$
      a > e \iff 1 > -1 \quad \mathbf{(Case\ 2:\ Zero\ Points\ Inside)}
      $$
    - Add 2 points at the right edge:
      $$
      s \leftarrow b - 1 = 3 - 1 = \mathbf{2}
      $$
      $$
      e \leftarrow b = \mathbf{3}
      $$
    - Update answer: $ans \leftarrow 0 + 2 = \mathbf{2}$.
    - Active set: $S = \{2, 3\}$.
  - **Interval 2: $[a, b] = [1, 4]$:**
    - Compare $a = 1$ with $s = 2$:
      $$
      a \le s \iff 1 \le 2 \quad \mathbf{(Case\ 1:\ Two\ Points\ Already\ Inside!)}
      $$
    - Points $2 \in [1, 4]$ and $3 \in [1, 4]$. Already satisfied!
    - No points added: $ans = 2$, state $(s, e) = (2, 3)$ unchanged.
  - **Interval 3: $[a, b] = [3, 5]$:**
    - Compare $a = 3$ with $s = 2$ and $e = 3$:
      $$
      s < a \le e \iff 2 < 3 \le 3 \quad \mathbf{(Case\ 3:\ Exactly\ One\ Point\ Inside)}
      $$
    - Only point $3$ is inside $[3, 5]$. We need 1 more point.
    - Greedily pick rightmost point $b = 5$:
      $$
      s \leftarrow e = \mathbf{3}
      $$
      $$
      e \leftarrow b = \mathbf{5}
      $$
    - Update answer: $ans \leftarrow 2 + 1 = \mathbf{3}$.
    - Active set: $S = \{2, 3, 5\}$.
  - **Interval 4: $[a, b] = [2, 5]$:**
    - Compare $a = 2$ with $s = 3$:
      $$
      a \le s \iff 2 \le 3 \quad \mathbf{(Case\ 1:\ Two\ Points\ Already\ Inside!)}
      $$
    - Both $3 \in [2, 5]$ and $5 \in [2, 5]$. Already satisfied!
    - No points added.
  - **Phase 2: Final Cardinality:**
    $$
    ans = \mathbf{3}
    $$
- **Completely Disjoint Intervals Trace ($[[1, 2], [3, 4], [5, 6]]$):**
  - Each interval falls under Case 2 (zero overlap).
  - Adds 2 points per interval: $\{1, 2\}$, $\{3, 4\}$, $\{5, 6\}$.
  - Total size: $3 \times 2 = \mathbf{6}$.
- **Nested Short Interval Dominance ($[[1, 10], [5, 6]]$):**
  - Sorted order: `[5, 6]` comes before `[1, 10]`.
  - Points $\{5, 6\}$ chosen for `[5, 6]`.
  - Next interval `[1, 10]` sees $1 \le 5 \implies$ automatically satisfied!
  - Total size: **2**.

This instance demonstrates greedy matroid intersection scheduling and boundary point packing, mathematically proves why right-edge coordinate selection maximizes future interval coverage under lexicographical end-point order, and derives $O(N \log N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of intervals:
Find the **minimum size of a set $S$** such that every interval contains **at least 2 integers** from $S$.

```text
intervals = [ [1, 3], [1, 4], [2, 5], [3, 5] ]

Sort by end ascending, start descending:
  [1, 3], [1, 4], [3, 5], [2, 5]

1. [1, 3]: no points yet -> pick {2, 3} (rightmost) -> ans = 2
2. [1, 4]: contains {2, 3} -> already has 2 points! -> ans = 2
3. [3, 5]: contains {3} (only 1 point) -> pick {5} -> ans = 3
4. [2, 5]: contains {3, 5} -> already has 2 points! -> ans = 3

Result: 3
```

### The Invariant of the Two-Endpoint Greedy Placement
- Sorting by $(end \uparrow, start \downarrow)$ guarantees we resolve the most restrictive intervals first.
- Tracking the two largest points in $S$ ($s < e$) tells us exactly how many points already fall inside the current $[a, b]$:
  - If $a \le s$: both $s, e$ are inside $\implies$ 0 needed.
  - If $s < a \le e$: only $e$ is inside $\implies$ 1 needed (pick $b$).
  - If $a > e$: neither is inside $\implies$ 2 needed (pick $b-1, b$).

---

## 2. Conceptual Foundation & Invariants

### 1. Canonical Lexicographical Ordering:
$$
\text{sort}(intervals, \; \text{key} = (b, -a))
$$

### 2. State Transition Cases:
For current $[a, b]$:
- If $a \le s \implies \text{continue}$
- If $a > e \implies ans \leftarrow ans + 2, \; s \leftarrow b - 1, \; e \leftarrow b$
- If $s < a \le e \implies ans \leftarrow ans + 1, \; s \leftarrow e, \; e \leftarrow b$

> **Greedy Stabbing Point Optimality.** In the hitting set problem on 1D interval families with cardinality constraint $k = 2$, placing stabbing points at the maximal admissible coordinates $b-1, b$ maximizes the measure of the future intersection cone $\bigcap_{j > i} [a_j, b_j]$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Sort
- $[1, 3], [1, 4], [3, 5], [2, 5]$.

---

### Step 2: $[1, 3]$
- $a = 1 > -1 \implies$ pick $s = 2, e = 3 \implies ans = 2$.

---

### Step 3: $[1, 4]$
- $a = 1 \le 2 \implies$ contains both $\implies$ skip.

---

### Step 4: $[3, 5]$
- $s = 2 < 3 \le 3 \implies$ contains 3, needs 1 point $\implies$ pick $s = 3, e = 5 \implies ans = 3$.

---

### Step 5: $[2, 5]$
- $a = 2 \le 3 \implies$ contains both $\implies$ skip.

---

### Step 6: Output
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Interval $[a, b]$ | Case Triggered | Points Already Inside | Points Added to $S$ | New State $(s, e)$ | Cumulative Size $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[1, 3]` | Case 2 ($a > e$) | None | $2, 3$ | $(2, 3)$ | **$2$** |
| `[1, 4]` | Case 1 ($a \le s$) | $2, 3$ | None | $(2, 3)$ | **$2$** |
| `[3, 5]` | Case 3 ($s < a \le e$) | $3$ | $5$ | $(3, 5)$ | **$3$** |
| `[2, 5]` | Case 1 ($a \le s$) | $3, 5$ | None | $(3, 5)$ | **$3$** |
| **Total** | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Interval ($[1, 5]$):** Pick $\{4, 5\} \implies$ returns 2.
- **Short Intervals of Length 2 ($[1, 2]$):** Interval length $2 - 1 + 1 = 2 \implies$ forces both integers $\{1, 2\}$ into $S$.
- **Completely Disjoint Intervals:** $N$ disjoint intervals require $2N$ distinct points.
- **Identical Intervals ($[1, 4], [1, 4]$):** First interval picks $\{3, 4\}$; second interval recognizes both and skips.

---

## 6. Traps & Common Anti-Patterns

- **Sorting Only by End Time:** If two intervals have the same $end$ (e.g. $[1, 5]$ and $[4, 5]$), sorting only by $end$ might process $[1, 5]$ first and pick $\{1, 2\}$, which completely misses $[4, 5]$! Secondary sort by $start$ descending ($-start$) guarantees $[4, 5]$ is processed first.
- **Picking Arbitrary Points Inside Interval:** Picking points near the beginning of $[a, b]$ fails to cover future intervals. Greedily picking the **rightmost** points ($b-1, b$) gives the maximal chance of overlapping with future intervals.
- **Tracking Full Set of Integers:** Maintaining a full hash set of all chosen points is unnecessary; only the **two most recently added points** $(s, e)$ need to be remembered.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ intervals: $\mathcal{O}(N \log N)$.
  - Single pass through sorted intervals: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$ where $N \le 3000$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the sorting space (only scalar pointers $s, e$).
