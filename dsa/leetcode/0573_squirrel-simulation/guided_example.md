# Guided Example: Squirrel Simulation

We trace the step-by-step tree round-trip baseline summation ($S = \sum 2 \cdot d(\text{tree}, nut_i)$), first-nut initial leg substitution ($d(\text{squirrel}, nut_k) + d(\text{tree}, nut_k)$), net delta minimization ($S - a + b$), Manhattan metric evaluation ($|r_1 - r_2| + |c_1 - c_2|$), and optimal first-target selection on representative grid scenarios:

- **Input:**
  - Grid: $height = 5, \; width = 7$
  - Tree location: $tree = [2, 2]$
  - Squirrel location: $squirrel = [4, 4]$
  - Nut locations: $nuts = [[3, 0], [2, 5]]$
- **Required output:** `12`
  - Movement rules:
    - Distance between any two points $(r_1, c_1)$ and $(r_2, c_2)$ is Manhattan distance $|r_1 - r_2| + |c_1 - c_2|$.
    - The squirrel can carry at most **one nut at a time**.
    - Every nut must ultimately be delivered to the tree.
    - Starting point: Squirrel starts at $(4, 4)$.
- **Round-Trip Baseline & First-Nut Delta Principle:**
  - For any nut collected after the squirrel is already at the tree, collecting that nut requires a complete **round trip**:
    $$
    \text{Round-trip}(nut_i) = d(tree, nut_i) + d(nut_i, tree) = 2 \cdot d(tree, nut_i)
    $$
  - If the squirrel had started at the tree, the total distance for all nuts would be:
    $$
    S = \sum_{i} 2 \cdot d(tree, nut_i)
    $$
  - However, the squirrel starts at $squirrel \ne tree$.
  - Whichever nut $k$ the squirrel visits **first**, the path for that nut changes:
    - Instead of traveling $tree \to nut_k \to tree$ (distance $2 \cdot d(tree, nut_k)$),
    - The squirrel travels $squirrel \to nut_k \to tree$ (distance $d(squirrel, nut_k) + d(tree, nut_k)$).
  - All subsequent nuts are gathered via standard round-trips from the tree.
  - Therefore, choosing nut $k$ as the first target replaces one leg $d(tree, nut_k)$ with $d(squirrel, nut_k)$:
    $$
    \text{Total Distance}(k) = S - d(tree, nut_k) + d(squirrel, nut_k)
    $$
  - To minimize total travel, we simply evaluate this formula for each candidate first nut $k$ and take the minimum!
- **Detailed Step-by-Step Execution Trace:**
  - **Step 1: Compute Distances to Tree:**
    - **Nut 0 at $(3, 0)$:**
      $$
      a_0 = d(tree, nut_0) = |3 - 2| + |0 - 2| = 1 + 2 = \mathbf{3}
      $$
    - **Nut 1 at $(2, 5)$:**
      $$
      a_1 = d(tree, nut_1) = |2 - 2| + |5 - 2| = 0 + 3 = \mathbf{3}
      $$
  - **Step 2: Compute Baseline Total Round-Trip Sum $S$:**
    $$
    S = 2 \cdot (a_0 + a_1) = 2 \cdot (3 + 3) = 2 \cdot 6 = \mathbf{12}
    $$
  - **Step 3: Compute Distances from Squirrel to Each Nut:**
    - Squirrel is at $(4, 4)$.
    - **Nut 0 at $(3, 0)$:**
      $$
      b_0 = d(squirrel, nut_0) = |3 - 4| + |0 - 4| = 1 + 4 = \mathbf{5}
      $$
    - **Nut 1 at $(2, 5)$:**
      $$
      b_1 = d(squirrel, nut_1) = |2 - 4| + |5 - 4| = 2 + 1 = \mathbf{3}
      $$
  - **Step 4: Evaluate Candidate First Nut Choices:**
    - **Option A: Visit Nut 0 First ($k = 0$):**
      - Squirrel walks to Nut 0 ($5$), delivers to tree ($3$), then does round trip for Nut 1 ($2 \times 3 = 6$):
      - Formula:
        $$
        \text{Dist}_0 = S - a_0 + b_0 = 12 - 3 + 5 = \mathbf{14}
        $$
    - **Option B: Visit Nut 1 First ($k = 1$):**
      - Squirrel walks to Nut 1 ($3$), delivers to tree ($3$), then does round trip for Nut 0 ($2 \times 3 = 6$):
      - Formula:
        $$
        \text{Dist}_1 = S - a_1 + b_1 = 12 - 3 + 3 = \mathbf{12}
        $$
  - **Step 5: Select Minimum Total Distance:**
    $$
    ans = \min(14, 12) = \mathbf{12}
    $$
- **High Squirrel Distance Savings Example:**
  - If a nut is located right next to the squirrel ($b = 1$) but far from the tree ($a = 10$), picking that nut first saves $a - b = 10 - 1 = 9$ units of travel compared to baseline $S$!
- **Single Nut Instance ($nuts = [[1, 1]]$):**
  - $S = 2a$. Total = $2a - a + b = a + b = d(squirrel, nut) + d(nut, tree)$.

This instance demonstrates baseline round-trip perturbation optimization, mathematically proves why varying only the first leg reduces a combinatorial routing problem to a linear scan, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D grid with a `tree`, a `squirrel`, and several `nuts`:
The squirrel carries at most one nut at a time and must bring each nut to the tree.
Find the **minimal total Manhattan distance** to collect all nuts.

```text
Grid Configuration:
  Tree at (2, 2)
  Squirrel at (4, 4)
  Nut 0 at (3, 0) -> dist to tree = 3, dist to squirrel = 5
  Nut 1 at (2, 5) -> dist to tree = 3, dist to squirrel = 3

Choice 1: Collect Nut 0 first -> Total distance = 14
Choice 2: Collect Nut 1 first -> Total distance = 12 (Optimal!)

Minimum Total Distance = 12
```

### The First-Nut Perturbation Principle
- Every nut except the very first one requires a full round trip: $tree \to nut \to tree$ (cost: $2 \cdot d(tree, nut)$).
- Only the **first nut** has a different initial leg: $squirrel \to nut$ instead of $tree \to nut$.
- Therefore, the problem reduces to:
  1. Compute the baseline sum of all round trips from the tree: $S = \sum 2 \cdot d(tree, nut_i)$.
  2. For each nut $k$, calculate the total distance if nut $k$ is visited first:
     $$
     \text{Total}_k = S - d(tree, nut_k) + d(squirrel, nut_k)
     $$
  3. Pick the minimum across all nuts in a single pass!

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Metric:
$$
d((r_1, c_1), (r_2, c_2)) = |r_1 - r_2| + |c_1 - c_2|
$$

### 2. Baseline Formulation:
$$
S = \sum_{i=1}^N 2 \cdot d(tree, nut_i)
$$

### 3. Substitution Formula:
For any candidate first nut $k$:
$$
\text{Cost}(k) = S - d(tree, nut_k) + d(squirrel, nut_k)
$$
Minimize $\text{Cost}(k)$ over all $k \in [0, N - 1]$.

> **Round-Trip Conservation Invariant.** Because the squirrel must end at the tree after each delivery, the sequence in which nuts $2, \dots, N$ are gathered does not affect the total distance; only the identity of the very first nut changes the travel sum.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Tree Round Trips
- Nut 0 at $(3, 0)$: $d(tree, nut_0) = |3 - 2| + |0 - 2| = 3$.
- Nut 1 at $(2, 5)$: $d(tree, nut_1) = |2 - 2| + |5 - 2| = 3$.
- Total baseline $S = 2 \times (3 + 3) = \mathbf{12}$.

---

### Step 2: Compute Squirrel Distances
- Nut 0: $d(squirrel, nut_0) = |3 - 4| + |0 - 4| = 5$.
- Nut 1: $d(squirrel, nut_1) = |2 - 4| + |5 - 4| = 3$.

---

### Step 3: Test Candidate First Nuts
- Nut 0 first:
  $$
  S - a_0 + b_0 = 12 - 3 + 5 = 14
  $$
- Nut 1 first:
  $$
  S - a_1 + b_1 = 12 - 3 + 3 = \mathbf{12}
  $$

---

### Step 4: Emit Minimum
$$
ans = \min(14, 12) = \mathbf{12}
$$

---

## 4. Complete Execution Trace

| Nut Index | Coordinates | Tree Dist $a$ | Squirrel Dist $b$ | Delta $b - a$ | Total Distance $S - a + b$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(3, 0)$ | $3$ | $5$ | $+2$ | $12 + 2 = 14$ |
| **$1$** | **$(2, 5)$** | **$3$** | **$3$** | **$0$** | **$12 + 0 = \mathbf{12}$** |
| **Result** | — | Baseline $S = 12$ | — | Best: Nut 1 | **`12`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Nut ($N = 1$):** Must be the first nut $\implies d(squirrel, nut) + d(nut, tree)$.
- **Squirrel Starts on Top of a Nut ($b = 0$):** Savings equal $a$ $\implies S - a$.
- **Squirrel Starts at the Tree ($squirrel == tree$):** $b == a$ for all nuts $\implies$ total distance equals baseline $S$.
- **All Nuts Far from Squirrel ($b > a$ for all nuts):** Evaluates normally; picks the nut that minimizes the penalty $b - a$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Route Ordering (Traveling Salesperson heuristic):** Trying to sort nuts by distance from previous nuts creates complex factorial paths. Since every nut returns to the tree, subsequent paths are independent round trips.
- **Picking the Nut Closest to the Squirrel:** The best first nut is NOT necessarily the one closest to the squirrel; it is the nut that maximizes the difference $d(tree, nut) - d(squirrel, nut)$ (i.e. saves the most relative to the tree).
- **Ignoring the Return Trip from the First Nut:** The first nut still requires a trip from $nut \to tree$. The formula $S - a + b$ preserves this return trip.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of nuts ($\le 5 \times 10^4$).
  - Computing baseline $S$ takes $O(N)$ operations.
  - Evaluating the formula for each nut takes $O(N)$ operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 5 \times 10^4$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space beyond input data.
