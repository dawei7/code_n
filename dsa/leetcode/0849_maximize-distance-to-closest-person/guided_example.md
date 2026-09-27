# Guided Example: Maximize Distance to Closest Person

We trace the step-by-step 1D occupancy array traversal, three-regime seat placement analysis (leading edge, trailing edge, interior gap), midpoint distance derivation ($\lfloor \frac{i - last}{2} \rfloor$), boundary span distance derivation ($first$ and $n - 1 - last$), and global maximum closest distance selection on representative seating charts:

- **Input:**
  $$
  seats = [1, 0, 0, 0, 1, 0, 1]
  $$
- **Required output:** `2`
  - Seat placement optimization rules:
    - An array of $n$ seats consists of occupied seats (`1`) and empty seats (`0`).
    - At least one seat is occupied, and at least one seat is empty.
    - Alex wants to choose an empty seat to maximize his distance to the **closest** person.
    - Objective: Return the maximum possible minimum distance to any occupied seat:
      $$
      \max_{k, \, seats[k] = 0} \min_{j, \, seats[j] = 1} |k - j|
      $$
    - For $seats = [1, 0, 0, 0, 1, 0, 1]$ ($n = 7$):
      - Occupied seats are at indices: **0**, **4**, and **6**.
      - Empty seats available:
        - Seat 1: closest person at 0 $\implies$ distance 1.
        - Seat 2: closest persons at 0 and 4 $\implies$ distance 2.
        - Seat 3: closest person at 4 $\implies$ distance 1.
        - Seat 5: closest persons at 4 and 6 $\implies$ distance 1.
      - Maximizing the distance gives seat 2 with distance **`2`**.
- **Three-Regime Partition Invariant:**
  - **The Three Geometrical Cases:**
    - Any empty seat chosen by Alex falls into one of three distinct structural regimes:
      1. **Leading Edge Run (Left End):**
         - If Alex sits at index 0, the closest person to his right is at index $first$.
         - Distance achieved:
           $$
           dist_{\text{left}} = first
           $$
      2. **Trailing Edge Run (Right End):**
         - If Alex sits at index $n - 1$, the closest person to his left is at index $last$.
         - Distance achieved:
           $$
           dist_{\text{right}} = n - 1 - last
           $$
      3. **Interior Gaps (Between Two Occupied Seats):**
         - For two adjacent occupied seats at indices $last$ and $i$, the gap length is $d = i - last$.
         - The optimal seat is the integer midpoint:
           $$
           dist_{\text{interior}} = \left\lfloor \frac{i - last}{2} \right\rfloor
           $$
  - **Global Maximum Selection:**
    - The optimal distance across the entire row is the maximum across all three regimes:
      $$
      ans = \max\left( first, \; n - 1 - last, \; \left\lfloor \frac{d_{\max}}{2} \right\rfloor \right)
      $$
- **Step-by-Step Worked Execution Trace on $seats = [1, 0, 0, 0, 1, 0, 1]$ ($n = 7$):**
  - Initialize tracking: $first = \text{None}, last = \text{None}, d_{\max} = 0$.
  - **Index 0 ($seats[0] = 1$):**
    - First occupied seat encountered: $first \leftarrow 0$.
    - Update last seen: $last \leftarrow 0$.
  - **Indices 1, 2, 3 ($seats = 0$):**
    - Empty seats; continue scan.
  - **Index 4 ($seats[4] = 1$):**
    - Interior gap between previous occupied seat ($last = 0$) and current ($i = 4$):
      $$
      \Delta = 4 - 0 = \mathbf{4}
      $$
    - Update max interior gap: $d_{\max} \leftarrow \max(0, 4) = \mathbf{4}$.
    - Update last seen: $last \leftarrow 4$.
  - **Index 5 ($seats[5] = 0$):**
    - Empty seat; continue scan.
  - **Index 6 ($seats[6] = 1$):**
    - Interior gap between $last = 4$ and $i = 6$:
      $$
      \Delta = 6 - 4 = \mathbf{2}
      $$
    - Update max interior gap: $d_{\max} \leftarrow \max(4, 2) = \mathbf{4}$.
    - Update last seen: $last \leftarrow 6$.
  - **Scan Complete: Evaluate the Three Regimes:**
    - Leading edge distance:
      $$
      dist_{\text{left}} = first = \mathbf{0}
      $$
    - Trailing edge distance:
      $$
      dist_{\text{right}} = n - 1 - last = 7 - 1 - 6 = \mathbf{0}
      $$
    - Maximum interior midpoint distance:
      $$
      dist_{\text{interior}} = \left\lfloor \frac{d_{\max}}{2} \right\rfloor = \left\lfloor \frac{4}{2} \right\rfloor = \mathbf{2}
      $$
    - Global maximum distance:
      $$
      ans = \max(0, \; 0, \; 2) = \mathbf{2}
      $$
- **Trailing Run Domination Trace ($seats = [1, 0, 0, 0], n = 4$):**
  - $first = 0, last = 0, d_{\max} = 0$.
  - Leading distance: $0$. Interior distance: $0$.
  - Trailing distance: $n - 1 - last = 4 - 1 - 0 = \mathbf{3}$ (Alex sits at index 3).
  - $ans = \max(0, 3, 0) = \mathbf{3}$.
- **Leading Run Domination Trace ($seats = [0, 0, 0, 1], n = 4$):**
  - $first = 3, last = 3$.
  - Leading distance: $first = \mathbf{3}$ (Alex sits at index 0).
  - $ans = \max(3, 0, 0) = \mathbf{3}$.
- **Odd Gap Length Trace ($seats = [1, 0, 0, 1]$):**
  - $i - last = 3 - 0 = 3$.
  - Midpoint distance: $\lfloor 3 / 2 \rfloor = \mathbf{1}$ (sitting at 1 gives distance 1 to 0; sitting at 2 gives distance 1 to 3).

This instance demonstrates 1D Voronoi cell radius maximization on bounded integer intervals and piecewise boundary metric analysis, mathematically proves why interior maximum distance scales as half the gap length while boundary edges enjoy full run length, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given seat occupancies ($1$ = person, $0$ = empty):
Alex sits at an empty seat to **maximize his distance** to the closest person.
Find the maximum distance.

```text
seats = [ 1, 0, 0, 0, 1, 0, 1 ]

Occupied seats at: [ 0, 4, 6 ]

Options for Alex:
  Seat 1: dist to 0 = 1
  Seat 2: dist to 0 = 2, dist to 4 = 2 -> min dist = 2!
  Seat 3: dist to 4 = 1
  Seat 5: dist to 4 or 6 = 1

Best seat is 2 with distance 2.
Result: 2
```

### The Invariant of the Three Placement Regimes
- **Left end:** distance $= first$.
- **Right end:** distance $= n - 1 - last$.
- **Between two people:** distance $= \lfloor (i - last) / 2 \rfloor$.
- Answer is the maximum of these three possibilities.

---

## 2. Conceptual Foundation & Invariants

### 1. Voronoi Radius Formulas:
$$
R(k) = \begin{cases}
first & k = 0 \\
n - 1 - last & k = n - 1 \\
\lfloor \frac{d}{2} \rfloor & k = \text{midpoint of interior gap of length } d
\end{cases}
$$

### 2. Global Optimum:
$$
ans = \max \left( first, \; n - 1 - last, \; \left\lfloor \frac{\max(i - last)}{2} \right\rfloor \right)
$$

> **1D Voronoi Metric Invariant.** The maximum clearance problem on a compact 1D domain $[0, n - 1]$ with obstacle set $P \subset [0, n - 1]$ achieves its supremum either at the domain boundary $\partial \Omega$ (with clearance $\text{dist}(\partial \Omega, P)$) or at the circumcenter of two adjacent obstacles (with clearance $\lfloor |p_{k+1} - p_k| / 2 \rfloor$).

---

## 3. Step-by-Step Worked Execution

We trace $seats = [1, 0, 0, 0, 1, 0, 1]$:

---

### Step 1: Track Occupied Indices
- $first = 0$.
- Gap between 0 and 4: $4 - 0 = 4$.
- Gap between 4 and 6: $6 - 4 = 2$.
- $last = 6$.

---

### Step 2: Interior Distance
- $\lfloor 4 / 2 \rfloor = \mathbf{2}$.

---

### Step 3: Edge Distances
- Left: $first = 0$.
- Right: $7 - 1 - 6 = 0$.

---

### Step 4: Output
- $\max(0, 0, 2) = \mathbf{2}$.

---

## 4. Complete Execution Trace

| Seat Index $i$ | Seat Value | Event Triggered | Gap Measured ($i - last$) | Midpoint Clearance | Running Max $d$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $first \leftarrow 0, last \leftarrow 0$ | — | — | $0$ |
| $1 \dots 3$ | $0$ | Empty run | — | — | $0$ |
| $4$ | $1$ | Person at 4 | $4 - 0 = 4$ | $\lfloor 4 / 2 \rfloor = 2$ | **$4$** |
| $5$ | $0$ | Empty seat | — | — | $4$ |
| **$6$** | **$1$** | **Person at 6** | **$6 - 4 = 2$** | **$\lfloor 2 / 2 \rfloor = 1$** | **`4`** |
| **Final** | — | — | — | $\max(0, 0, \lfloor 4/2 \rfloor)$ | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Person Only at Beginning ($[1, 0, 0, 0]$):** Trailing run gives $n - 1 - 0 = 3$.
- **Person Only at End ($[0, 0, 0, 1]$):** Leading run gives $first = 3$.
- **No Interior Gaps ($[0, 1, 0]$):** Left gives 1, right gives 1 $\implies 1$.
- **Odd Gap Lengths ($[1, 0, 0, 1]$):** Gap is 3 $\implies \lfloor 3 / 2 \rfloor = 1$.

---

## 6. Traps & Common Anti-Patterns

- **Treating Edge Gaps as Halved:** At the ends of the row, Alex has a wall on one side, not another person. The distance is the FULL run length ($first$ or $n - 1 - last$), NOT divided by 2!
- **Scanning All Seats for Each Empty Seat ($O(N^2)$):** Checking distance to closest person naively for every seat is quadratic. Single-pass gap tracking solves in $O(N)$.
- **Integer Division vs Ceiling:** Interior distance must use integer floor division $\lfloor d / 2 \rfloor$, since Alex cannot sit at fractional seat coordinates.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass through array of length $N$: $\mathcal{O}(N)$.
  - Constant scalar comparisons per element: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 2 \times 10^4$. Completes in $< 0.5$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar indices `first`, `last`, and `d`).
