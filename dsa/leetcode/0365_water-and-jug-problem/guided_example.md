# Guided Example: Water and Jug Problem

We trace the step-by-step state space graph exploration (`dfs(i, j)`), the six discrete jug operations (Fill, Empty, Pour), cycle avoidance via visited set (`vis`), and Bézout's identity / $\gcd(x, y)$ divisibility on representative water jug instances:

- **Input:** $x = 3, \quad y = 5, \quad z = 4$
- **Required output:** `true`
  - Capable measuring sequence:
    1. Start: $(0, 0)$ (Both jugs empty)
    2. Fill jug 2: $(0, 5)$
    3. Pour jug 2 into jug 1: amount $a = \min(5, 3 - 0) = 3 \implies (3, 2)$
    4. Empty jug 1: $(0, 2)$
    5. Pour jug 2 into jug 1: $(2, 0)$
    6. Fill jug 2: $(2, 5)$
    7. Pour jug 2 into jug 1: amount $b = \min(5, 3 - 2) = 1 \implies (3, \mathbf{4})$
  - Second jug contains exactly $4$ liters ($j == 4$) $\implies \text{true}$!
  - Mathematical confirmation via Bézout's Identity:
    - $\gcd(3, 5) = 1$
    - $4 \le 3 + 5 = 8$
    - $4 \pmod{\gcd(3, 5)} = 4 \pmod 1 = 0 \implies$ Provably solvable!
- **Target Exceeds Total Capacity:** $x = 2, y = 6, z = 10 \implies z > x + y \implies \text{false}$
- **Non-Divisible Target Counterexample:** $x = 2, y = 6, z = 5 \implies \gcd(2, 6) = 2$, but $5 \pmod 2 \ne 0 \implies \text{false}$

This instance demonstrates state space search on implicitly defined transition graphs, connects graph reachability to number-theoretic linear Diophantine equations ($a x + b y = z$), and analyzes state complexity bounded by the jug perimeters.

---

## 1. Instance & Teaching Goal

Given two jugs of capacities $x = 3$ and $y = 5$, and an infinite water supply:
Determine whether it is possible to measure exactly $z = 4$ liters in total across the two jugs:
Available atomic operations:
1. **Fill** either jug completely to capacity ($x$ or $y$).
2. **Empty** either jug completely to $0$.
3. **Pour** water from one jug into the other until either the donor jug is empty or the receiving jug is full.

```text
Capacities: Jug 1 = 3L, Jug 2 = 5L. Target = 4L.

Step-by-Step Pouring Strategy:
(0, 0) -> Fill Jug 2     -> (0, 5)
(0, 5) -> Pour J2 to J1  -> (3, 2)
(3, 2) -> Empty Jug 1    -> (0, 2)
(0, 2) -> Pour J2 to J1  -> (2, 0)
(2, 0) -> Fill Jug 2     -> (2, 5)
(2, 5) -> Pour J2 to J1  -> (3, 4)  <-- JUG 2 HOLDS EXACTLY 4 LITERS!

Target 4L Successfully Measured!
```

---

## 2. Conceptual Foundation & Invariants

### 1. State Representation $(i, j)$
A state is a 2-tuple $(i, j)$ where:
- $i \in [0, x]$: Water currently in jug 1.
- $j \in [0, y]$: Water currently in jug 2.
- Terminal Success Condition:
  $$
  i == z \quad \lor \quad j == z \quad \lor \quad i + j == z
  $$

### 2. The 6 Directed Graph Transitions from $(i, j)$:
1. `Fill Jug 1`: $(x, j)$
2. `Fill Jug 2`: $(i, y)$
3. `Empty Jug 1`: $(0, j)$
4. `Empty Jug 2`: $(i, 0)$
5. `Pour J1 -> J2`: Amount $a = \min(i, y - j) \implies (i - a, j + a)$
6. `Pour J2 -> J1`: Amount $b = \min(j, x - i) \implies (i + b, j - b)$

### 3. Cycle Detection
Because water can be repeatedly filled and emptied, the transition graph contains cycles (e.g. $(0, 0) \to (3, 0) \to (0, 0)$).
A hash set `vis` records visited states $(i, j)$. If $(i, j) \in vis$, backtrack immediately with `False`.

### 4. Mathematical Ground Truth (Bézout's Lemma)
Any reachable amount of water is a linear combination:
$$
a \cdot x + b \cdot y = z \quad (a, b \in \mathbb{Z})
$$
A solution exists if and only if:
1. $z \le x + y$
2. $z \pmod{\gcd(x, y)} == 0$

> **Invariant.** All reachable states $(i, j)$ have the property that $i, j,$ and $i + j$ are integer multiples of $\gcd(x, y)$.

---

## 3. Step-by-Step Worked Execution

We trace the DFS execution for $x = 3, y = 5, z = 4$:
Root call: `dfs(0, 0)`.

---

### Step 1: Initial State $(0, 0)$
- Mark `(0, 0)` in `vis`.
- Target check: $0 \ne 4, 0 + 0 \ne 4$.
- Branch to `dfs(0, 5)` (Fill Jug 2).

---

### Step 2: State $(0, 5)$
- Mark `(0, 5)` in `vis`.
- Target check: $0 \ne 4, 5 \ne 4, 5 \ne 4$.
- Evaluate pour from Jug 2 to Jug 1:
  $$
  b = \min(j, \; x - i) = \min(5, \; 3 - 0) = \mathbf{3}
  $$
  New state: $(0 + 3, \; 5 - 3) = \mathbf{(3, 2)}$.
- Recurse into `dfs(3, 2)`.

---

### Step 3: State $(3, 2)$
- Mark `(3, 2)` in `vis`.
- Target check: $3 \ne 4, 2 \ne 4, 3 + 2 = 5 \ne 4$.
- Branch to `dfs(0, 2)` (Empty Jug 1).

---

### Step 4: State $(0, 2)$
- Mark `(0, 2)` in `vis`.
- Evaluate pour from Jug 2 to Jug 1:
  $$
  b = \min(2, \; 3 - 0) = \mathbf{2}
  $$
  New state: $(0 + 2, \; 2 - 2) = \mathbf{(2, 0)}$.
- Recurse into `dfs(2, 0)`.

---

### Step 5: State $(2, 0)$
- Mark `(2, 0)` in `vis`.
- Branch to `dfs(2, 5)` (Fill Jug 2).

---

### Step 6: State $(2, 5)$
- Mark `(2, 5)` in `vis`.
- Target check: $2 \ne 4, 5 \ne 4, 2 + 5 = 7 \ne 4$.
- Evaluate pour from Jug 2 to Jug 1:
  $$
  b = \min(j, \; x - i) = \min(5, \; 3 - 2) = \mathbf{1}
  $$
  New state:
  $$
  (2 + 1, \; 5 - 1) = \mathbf{(3, 4)}
  $$
- Recurse into `dfs(3, 4)`.

---

### Step 7: Target State $(3, 4)$ — Success!
- State entered: $i = 3, j = 4$.
- Evaluate goal predicate:
  $$
  j == z \iff 4 == 4 \implies \mathbf{\text{True}}
  $$
- Immediate success return propagates back up the call stack!
- Overall return: **`true`**.

---

## 4. Complete Execution Trace

```text
x = 3, y = 5, z = 4
DFS Search Tree Path:
(0, 0) -> Fill J2    -> (0, 5)
(0, 5) -> Pour J2->J1 -> (3, 2) (poured 3L)
(3, 2) -> Empty J1   -> (0, 2)
(0, 2) -> Pour J2->J1 -> (2, 0) (poured 2L)
(2, 0) -> Fill J2    -> (2, 5)
(2, 5) -> Pour J2->J1 -> (3, 4) (poured 1L)
At (3, 4): j == 4 == z -> TARGET ACHIEVED! -> Return True
```

| Step | State $(i, j)$ | Action Performed | Jug 1 (3L) Level | Jug 2 (5L) Level | Sum $i + j$ | Target $z = 4$ Matched? |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | $(0, 0)$ | Initial Setup | 0 | 0 | 0 | No |
| 2 | $(0, 5)$ | Fill Jug 2 | 0 | 5 | 5 | No |
| 3 | $(3, 2)$ | Pour Jug 2 $\to$ Jug 1 | 3 | 2 | 5 | No |
| 4 | $(0, 2)$ | Empty Jug 1 | 0 | 2 | 2 | No |
| 5 | $(2, 0)$ | Pour Jug 2 $\to$ Jug 1 | 2 | 0 | 2 | No |
| 6 | $(2, 5)$ | Fill Jug 2 | 2 | 5 | 7 | No |
| **7** | **$(3, 4)$** | **Pour Jug 2 $\to$ Jug 1** | **3** | **4** | **7** | **Yes ($j == 4$)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys valid physical pouring operations: water is neither created nor destroyed during a pour, and capacities $x$ and $y$ are never exceeded. If a state satisfies $i == z, j == z,$ or $i + j == z$, the volume $z$ is genuinely measurable in one or across both jugs.

**Completeness.** Graph search visits every reachable configuration in the $(x+1) \times (y+1)$ grid. Because at least one jug is always empty or full at any operational step, the reachable state space is restricted to the boundary perimeter of size $O(x + y)$. Exhaustive traversal guarantees finding the target if reachable.

---

## 6. Traps This Instance Exposes

- **Infinite Loops Without Visited Set:** Pouring back and forth between jugs produces closed cycles (e.g. $(3, 2) \to (0, 2) \to (3, 2)$). Storing visited tuples $(i, j)$ in `vis` is essential to prevent infinite recursion.
- **Total Capacity Exceeded:** If $z > x + y$, it is physically impossible to hold $z$ liters of water simultaneously. Checking $z \le x + y$ is an immediate necessary condition.
- **Python Recursion Limit on Large Inputs:** For large values like $x = 10^6, y = 10^6 + 1$, DFS can hit Python's maximum recursion limit. In production, mathematical evaluation $z \le x + y \land z \pmod{\gcd(x, y)} == 0$ evaluates in $O(\log(\min(x, y)))$ time and $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(x + y)$.
  - In any valid sequence of operations, at least one jug is either completely empty ($0$) or completely full ($x$ or $y$).
  - The number of reachable states lies along the 4 boundaries of the rectangle $[0, x] \times [0, y]$, bounded by $2(x + y)$.
  - Each state generates 6 transitions in $O(1)$ time, yielding $O(x + y)$ total operations.
- **Auxiliary Space Complexity:** $O(x + y)$ to store the visited set `vis` and recursion stack.
