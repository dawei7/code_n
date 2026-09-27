# Guided Example: Heaters

We trace the step-by-step monotonic radius predicate formulation ($check(r)$), binary search over the answer space ($[0, 10^9]$), two-pointer linear greedy interval coverage ($[heaters[j] - r, heaters[j] + r]$), and minimum warm radius derivation on representative 1D coordinates:

- **Input:**
  - House positions: $houses = [1, 2, 3]$
  - Heater positions: $heaters = [2]$
- **Required output:** `1`
  - Step 1: Sort both arrays:
    - Sorted houses: $[1, 2, 3]$ ($m = 3$)
    - Sorted heaters: $[2]$ ($n = 1$)
  - Step 2: Binary search on heating radius $r \in [0, 10^9]$:
    - Search space: $[0, 10^9]$
    - **Test radius $r = 0$:**
      - Heater covers $[2 - 0, 2 + 0] = [2, 2]$
      - House $1 < 2$ is uncovered $\implies check(0) = \text{False}$
    - **Test radius $r = 1$:**
      - Heater covers $[2 - 1, 2 + 1] = [1, 3]$
      - House 1: $1 \in [1, 3]$ (Covered!)
      - House 2: $2 \in [1, 3]$ (Covered!)
      - House 3: $3 \in [1, 3]$ (Covered!)
      - All houses covered $\implies check(1) = \text{True}$
    - Minimal radius satisfying the condition is $r = \mathbf{1}$.
- **Two Heaters Instance:** $houses = [1, 2, 3, 4], heaters = [1, 4]$
  - Radius $r = 1$:
    - Heater 1 covers $[1 - 1, 1 + 1] = [0, 2]$ (Houses 1 and 2)
    - Heater 4 covers $[4 - 1, 4 + 1] = [3, 5]$ (Houses 3 and 4)
    - Combined coverage: $[0, 2] \cup [3, 5]$, covering all 4 houses $\implies r = \mathbf{1}$
- **Single House and Heater at Same Spot:** $houses = [1], heaters = [1] \implies r = \mathbf{0}$
- **Extreme Distance Instance:** $houses = [1], heaters = [10^9] \implies r = 10^9 - 1$

This instance demonstrates binary search on monotonic feasibility predicates (decision-to-optimization reduction), proves why sorting enables $O(M + N)$ greedy two-pointer verification, and derives $O((M + N) \log(\text{range}) + M \log M + N \log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given coordinates of houses and heaters along a horizontal line:
Every heater warms all houses within horizontal distance $r$ (i.e. interval $[heater - r, heater + r]$).
Find the **minimum radius $r$** such that all houses are covered by at least one heater.

```text
House Coordinates:   (1)      (2)      (3)
                      |        |        |
Heater at x = 2:               [H]
Coverage with r = 1: <------------------>
                      [1 ------------- 3]

Radius r = 1 covers houses 1, 2, and 3. Minimum Radius = 1.
```

### The Monotonicity of Radius Coverage
Notice the monotonicity property:
- If a radius $r$ is sufficient to warm all houses, any larger radius $r' > r$ will also warm all houses.
- If a radius $r$ leaves at least one house in the cold, any smaller radius $r'' < r$ will definitely fail as well.
- This creates a monotonic boolean step function:
  $$
  \text{False}, \; \text{False}, \; \dots, \; \text{False}, \; \mathbf{True}, \; \text{True}, \; \dots
  $$
- Therefore, the minimal radius can be found via **Binary Search on the Answer Space** using a linear validation predicate `check(r)`.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Coverage Verification (`check(r)`):
Given both $houses$ and $heaters$ sorted in ascending order:
- Let pointer $i$ track the current house, and pointer $j$ track the current heater.
- The heating range of heater $j$ is $[heaters[j] - r, \; heaters[j] + r]$.
- While $i < m$:
  - If $j == n$: No more heaters remain to the right, and house $i$ is not covered $\implies$ Return `False`.
  - If $houses[i] > heaters[j] + r$:
    Heater $j$ lies completely to the left of house $i$. Advance to the next heater: $j \leftarrow j + 1$.
  - If $houses[i] < heaters[j] - r$:
    House $i$ lies completely to the left of heater $j$. Since heaters are sorted, no subsequent heater can reach house $i$ either $\implies$ Return `False`.
  - Otherwise ($heaters[j] - r \le houses[i] \le heaters[j] + r$):
    House $i$ is covered! Advance to the next house: $i \leftarrow i + 1$.
- If all $m$ houses are covered, return `True`.

### 2. Binary Search Domain:
$$
left = 0, \quad right = 10^9
$$
- If `check(mid)` is True: $mid$ is feasible; try smaller radii by setting $right \leftarrow mid$.
- If `check(mid)` is False: $mid$ is too small; increase radius by setting $left \leftarrow mid + 1$.

> **Monotonic Invariant.** For any sorted coordinates, `check(r)` is non-decreasing over $r \in [0, 10^9]$, guaranteeing convergence to the unique minimal feasible radius.

---

## 3. Step-by-Step Worked Execution

We trace $houses = [1, 2, 3]$ and $heaters = [2]$:

---

### Step 1: Sorting Both Sequences
- $houses = [1, 2, 3]$ ($m = 3$).
- $heaters = [2]$ ($n = 1$).
- Binary search bounds: $left = 0, \; right = 10^9$.

---

### Step 2: Binary Search Iterations (Highlighting Critical Boundaries)

1. **Midpoint $mid = 1$:**
   - Execute $check(1)$ with $r = 1$:
     - Heater $j = 0$ ($heaters[0] = 2$):
       - Lower bound: $2 - 1 = 1$. Upper bound: $2 + 1 = 3$.
     - House $i = 0$ ($houses[0] = 1$):
       - $1 \in [1, 3]$ (**Covered**). Advance $i \leftarrow 1$.
     - House $i = 1$ ($houses[1] = 2$):
       - $2 \in [1, 3]$ (**Covered**). Advance $i \leftarrow 2$.
     - House $i = 2$ ($houses[2] = 3$):
       - $3 \in [1, 3]$ (**Covered**). Advance $i \leftarrow 3$.
     - All 3 houses covered $\implies check(1) = \mathbf{True}$.
   - Update upper bound: $right \leftarrow 1$.

2. **Midpoint $mid = 0$ ($left = 0, right = 1$):**
   - Execute $check(0)$ with $r = 0$:
     - Heater range: $[2, 2]$.
     - House $i = 0$ ($houses[0] = 1$):
       - Test: $houses[0] < heaters[0] - 0 \iff 1 < 2$.
       - House 1 lies to the left of the heater coverage.
       - Returns $\mathbf{False}$.
   - Update lower bound: $left \leftarrow 0 + 1 = \mathbf{1}$.

---

### Step 3: Termination
- Search bounds meet: $left == right == 1$.
- Minimal radius: **`1`**.

---

## 4. Complete Execution Trace

| House $houses[i]$ | Heater $heaters[j]$ | Tested Radius $r$ | Coverage Interval $[H-r, H+r]$ | In Range? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---|
| **$1$** | $2$ | $0$ | $[2, 2]$ | No ($1 < 2$) | $check(0) = \text{False}$ |
| **$1$** | $2$ | $1$ | $[1, 3]$ | **Yes** ($1 \in [1, 3]$) | Advance house to $2$ |
| **$2$** | $2$ | $1$ | $[1, 3]$ | **Yes** ($2 \in [1, 3]$) | Advance house to $3$ |
| **$3$** | $2$ | $1$ | $[1, 3]$ | **Yes** ($3 \in [1, 3]$) | Advance house (Done!) |
| **Conclusion** | — | — | — | — | **Minimal Radius: $1$** |

---

## 5. Boundary Cases & Failure Modes

- **Houses on Both Sides of Single Heater ($[1, 100], [50]$):**
  - Radius must reach both extremes: $\max(|1 - 50|, |100 - 50|) = \max(49, 50) = \mathbf{50}$.
- **Heaters Outside Houses ($houses = [5, 6, 7], heaters = [1, 10]$):**
  - Left heater covers $[5]$ if $r \ge 4$; right heater covers $[7]$ if $r \ge 3$. House 6 requires $\min(|6-1|, |10-6|) = 4$. Minimum radius is $\mathbf{4}$.
- **Every House Has Co-Located Heater ($houses = [1, 2], heaters = [1, 2]$):** Radius $r = \mathbf{0}$ covers all.

---

## 6. Traps & Common Anti-Patterns

- **Not Sorting the Input Arrays:** The two-pointer greedy verification assumes both arrays are sorted in ascending coordinate order. If unsorted, $houses[i] < heaters[j] - r$ falsely rejects houses that could be covered by earlier or later heaters.
- **Off-by-One in Pointer Advancing:** Advancing $j$ when $houses[i] < heaters[j] - r$ discards the only heater that could possibly reach house $i$, causing premature failure. Only advance $j$ when the heater is already behind the house ($houses[i] > heaters[j] + r$).
- **Quadratic Distance Matrix ($O(M \cdot N)$):** Calculating distances between every house and every heater takes quadratic time, causing TLE for $M, N = 2.5 \times 10^4$. Binary search with two pointers runs in $O((M + N) \log R)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $houses$ of size $M$ takes $O(M \log M)$ time.
  - Sorting $heaters$ of size $N$ takes $O(N \log N)$ time.
  - Binary search over $R = 10^9$ takes $\log_2(10^9) \approx 30$ iterations.
  - Each `check` pass traverses both arrays in $O(M + N)$ time.
  - Total Time: $\mathcal{O}(M \log M + N \log N + (M + N) \log(\text{range}))$. For $M, N \le 2.5 \times 10^4$, finishes in $< 35$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond sorting storage.
