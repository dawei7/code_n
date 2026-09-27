# Guided Example: Exam Room

We trace the step-by-step interval partitioning, boundary versus interior distance calculations, tie-breaking heuristics, dynamic interval splitting and merging, and closest-student distance maximization on representative exam room operations:

- **Input:**
  $$
  n = 10, \quad \text{operations} = [[\text{"seat"}], [\text{"seat"}], [\text{"seat"}], [\text{"seat"}], [\text{"leave"}, 4], [\text{"seat"}]]
  $$
- **Required output:** `[0, 9, 4, 2, null, 5]`
  - Classroom configuration & seating protocol:
    - There are $n = 10$ seats in a single line, indexed from $0$ to $9$.
    - When a student enters via `seat()`, they must sit in the seat that **maximizes the distance to the closest person**.
    - If there are multiple such seats with equal maximal distance, the student sits in the seat with the **lowest index**.
    - When a student leaves via `leave(p)`, seat $p$ becomes empty, merging adjacent unoccupied spaces.
    - Virtual boundary coordinates:
      - Left wall: $-1$ (unoccupied boundary before seat $0$).
      - Right wall: $n = 10$ (unoccupied boundary after seat $n - 1 = 9$).
    - An empty segment between two occupied seats $l$ and $r$ is denoted by the interval $(l, r)$.
- **Interval Distance Invariants:**
  - **Left Edge Interval ($l = -1$):**
    - The seat chosen is always seat $0$.
    - Distance to the nearest person (who is at seat $r$) is $r - 0 = r$.
    - In interval formula: $r - l - 1 = r - (-1) - 1 = r$.
  - **Right Edge Interval ($r = n$):**
    - The seat chosen is always seat $n - 1$.
    - Distance to the nearest person (who is at seat $l$) is $(n - 1) - l$.
    - In interval formula: $r - l - 1 = n - l - 1$.
  - **Interior Interval (both $l \ge 0$ and $r < n$):**
    - The best seat is the exact integer midpoint:
      $$
      p = \lfloor \frac{l + r}{2} \rfloor
      $$
    - The distance to both neighbors is:
      $$
      d = \lfloor \frac{r - l}{2} \rfloor
      $$
  - **Priority Ordering:**
    - Order intervals by descending effective distance $d$.
    - For ties in distance $d$, break ties by ascending seat coordinate $p$.

---

## 1. Instance & Teaching Goal

Given an exam room of $n = 10$ seats, students enter and leave dynamically.
Each arriving student must maximize their minimum distance to existing students, breaking ties with the smallest index.

```text
Seats: 0 1 2 3 4 5 6 7 8 9
Op 1: seat()   -> sits at 0 (distance to boundary: 9)
Op 2: seat()   -> sits at 9 (distance to 0: 9)
Op 3: seat()   -> sits at 4 (midpoint of [0, 9], distance: 4)
Op 4: seat()   -> sits at 2 (midpoint of [0, 4], distance: 2; ties with 6, chooses 2)
Op 5: leave(4) -> seat 4 vacated, merging intervals (2, 4) and (4, 9) into (2, 9)
Op 6: seat()   -> sits at 5 (midpoint of [2, 9], distance: 3)
```

The objective is to trace each insertion and deletion across priority-ordered intervals, showing why each chosen seat is globally optimal under the distance metric.

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Metric Formulation:
For any open interval $(l, r)$ representing empty seats strictly between $l$ and $r$:
$$
\text{dist}(l, r) = \begin{cases}
r & \text{if } l = -1 \\
(n - 1) - l & \text{if } r = n \\
\lfloor \frac{r - l}{2} \rfloor & \text{if } 0 \le l < r < n
\end{cases}
$$

### 2. Candidate Placement Seat:
$$
\text{seat\_pos}(l, r) = \begin{cases}
0 & \text{if } l = -1 \\
n - 1 & \text{if } r = n \\
\lfloor \frac{l + r}{2} \rfloor & \text{if } 0 \le l < r < n
\end{cases}
$$

### 3. Dynamic Interval Split on `seat()`:
Choosing seat $p$ from interval $(l, r)$ destroys $(l, r)$ and introduces two smaller sub-intervals:
$$
(l, r) \longrightarrow (l, p) \quad \text{and} \quad (p, r)
$$

### 4. Dynamic Interval Fusion on `leave(p)`:
Vacating seat $p$ bounded by left occupied neighbor $l$ and right occupied neighbor $r$ destroys $(l, p)$ and $(p, r)$, merging them back into:
$$
(l, p) \cup (p, r) \longrightarrow (l, r)
$$

---

## 3. Step-by-Step Worked Execution

### Initial State:
- Room size $n = 10$.
- Single active interval covering all seats: $(-1, 10)$.

---

### Step 1: Operation `seat()`
- Only interval: $(-1, 10)$.
- Left boundary rule ($l = -1$):
  $$
  p = 0, \quad d = 10 - (-1) - 1 = 10 \quad (\text{virtual})
  $$
  Sitting at $0$ places the student at the boundary with maximal clearance.
- Interval $(-1, 10)$ splits into:
  - $(-1, 0)$ (empty left boundary, $0$ seats between $-1$ and $0$).
  - $(0, 10)$ with distance $(10 - 1) - 0 = 9$.
- **Return: `0`**.

---

### Step 2: Operation `seat()`
- Active intervals:
  - $(0, 10)$: right boundary rule ($r = 10$):
    $$
    p = n - 1 = 9, \quad d = 9 - 0 = 9
    $$
- Interval $(0, 10)$ splits into:
  - $(0, 9)$ (interior interval).
  - $(9, 10)$ (empty right boundary).
- **Return: `9`**.

---

### Step 3: Operation `seat()`
- Candidate interval: $(0, 9)$.
  - Interior rule:
    $$
    p = \lfloor \frac{0 + 9}{2} \rfloor = 4
    $$
    $$
    d = \lfloor \frac{9 - 0}{2} \rfloor = 4
    $$
- Distance from seat $4$ to nearest person: $\min(4 - 0, 9 - 4) = \min(4, 5) = 4$.
- Interval $(0, 9)$ splits into $(0, 4)$ and $(4, 9)$.
- **Return: `4`**.

---

### Step 4: Operation `seat()`
- Candidate intervals:
  - $(0, 4)$: interior midpoint $p = \lfloor (0 + 4)/2 \rfloor = 2$, distance $d = \lfloor (4 - 0)/2 \rfloor = 2$.
  - $(4, 9)$: interior midpoint $p = \lfloor (4 + 9)/2 \rfloor = 6$, distance $d = \lfloor (9 - 4)/2 \rfloor = 2$.
- Both intervals yield distance $d = 2$.
- **Tie-breaker:** Smallest seat index wins:
  $$
  2 < 6 \implies \text{Seat } 2 \text{ is chosen!}
  $$
- Interval $(0, 4)$ splits into $(0, 2)$ and $(2, 4)$.
- **Return: `2`**.

---

### Step 5: Operation `leave(4)`
- Seat $4$ is vacated.
- Left neighbor of $4$ is $2$, so left interval was $(2, 4)$.
- Right neighbor of $4$ is $9$, so right interval was $(4, 9)$.
- Deleting both intervals and fusing them yields:
  $$
  (2, 4) + (4, 9) \longrightarrow (2, 9)
  $$
- **Return: `null`**.

---

### Step 6: Operation `seat()`
- Candidate intervals:
  - $(0, 2)$: midpoint $p = 1$, distance $d = \lfloor (2 - 0)/2 \rfloor = 1$.
  - $(2, 9)$: midpoint $p = \lfloor (2 + 9)/2 \rfloor = 5$, distance $d = \lfloor (9 - 2)/2 \rfloor = 3$.
- Comparing distances:
  $$
  d(2, 9) = 3 > d(0, 2) = 1
  $$
- Maximum distance is $3$, obtained at seat $5$.
- Interval $(2, 9)$ splits into $(2, 5)$ and $(5, 9)$.
- **Return: `5`**.

---

## 4. Complete Execution Trace

| Step | Operation | Active Intervals Considered | Chosen Interval | Evaluated Distance | Assigned Seat | Resulting Intervals |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| $1$ | `seat()` | $(-1, 10)$ | $(-1, 10)$ | $10$ | **`0`** | $(0, 10)$ |
| $2$ | `seat()` | $(0, 10)$ | $(0, 10)$ | $9$ | **`9`** | $(0, 9)$ |
| $3$ | `seat()` | $(0, 9)$ | $(0, 9)$ | $4$ | **`4`** | $(0, 4), (4, 9)$ |
| $4$ | `seat()` | $(0, 4) \to d=2, p=2$<br>$(4, 9) \to d=2, p=6$ | $(0, 4)$ | $2$ | **`2`** | $(0, 2), (2, 4), (4, 9)$ |
| $5$ | `leave(4)` | Neighbor map: $L=2, R=9$ | Remove $(2, 4), (4, 9)$ | — | **`null`** | $(0, 2), (2, 9)$ |
| $6$ | `seat()` | $(0, 2) \to d=1, p=1$<br>$(2, 9) \to d=3, p=5$ | $(2, 9)$ | $3$ | **`5`** | $(0, 2), (2, 5), (5, 9)$ |

---

## 5. Boundary Cases & Failure Modes

- **Seat 0 Priority:** When no one is seated, seat $0$ is taken. When seat $0$ is empty but other seats are taken, distance from $0$ to the first seated person is $first$, not $\lfloor first/2 \rfloor$.
- **Seat $n - 1$ Priority:** Distance from the last seated person to seat $n - 1$ is $(n - 1) - last$, not $\lfloor ((n - 1) - last)/2 \rfloor$.
- **Interior Midpoint Rounding:** Integer division $\lfloor (r - l)/2 \rfloor$ correctly reflects the closest neighbor distance for odd lengths (e.g. interval $(0, 4) \implies p = 2, d = 2$; interval $(0, 3) \implies p = 1, d = 1$).
- **Consecutive Occupied Seats:** When two adjacent seats are occupied (e.g. $(2, 3)$), distance is $\lfloor (3 - 2)/2 \rfloor = 0$, so no new student can be placed between them.

---

## 6. Traps & Common Anti-Patterns

- **Equal Distance Tie-Breaking:** Failing to break ties by smallest seat index violates the specification. For example, in Step 4, interval $(0, 4)$ yields seat $2$ and $(4, 9)$ yields seat $6$, both with distance $2$. Selecting $6$ instead of $2$ fails the tie-break requirement.
- **Linear Seat Scanning:** Scanning all seats from $0$ to $n - 1$ on each `seat()` takes $\mathcal{O}(N)$ time. When $N = 10^9$, linear iteration causes Time Limit Exceeded (TLE).
- **Orphaned Interval Links:** When a student leaves, failing to merge both the left and right intervals creates disconnected segments and incorrect subsequent distance calculations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `seat()`: Extracting the maximum-distance interval from a balanced self-balancing search tree or sorted list takes $\mathcal{O}(\log P)$ where $P \le N$ is the number of currently seated students.
  - `leave(p)`: Looking up the neighboring seats in hash tables and deleting/inserting intervals in the sorted structure takes $\mathcal{O}(\log P)$ time.
  - For $M$ operations: $\mathcal{O}(M \log P)$, easily supporting $N = 10^9$ with $M = 10^4$ operations.
- **Auxiliary Space Complexity:**
  - Storing active intervals and seat-to-neighbor mappings takes $\mathcal{O}(P)$ space, where $P$ is the number of seated students ($\le M$).
