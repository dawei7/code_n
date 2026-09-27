# Guided Example: Couples Holding Hands

We trace the step-by-step couple index mapping ($x \gg 1$), couch seat pairing ($row[2i], row[2i+1]$), permutation cycle graph construction, Disjoint Set Union (Union-Find) component clustering, cycle decomposition swap cost theorem ($k - 1$ swaps for component of size $k$), and global minimum swap calculation ($N - C$) on representative seating arrangements:

- **Input:** $row = [0, 2, 1, 3]$
- **Required output:** `1`
  - Seating & couple specifications:
    - There are $2N$ people sitting in $2N$ seats. Total number of couples is $N = \text{length} / 2$.
    - Couple definitions:
      - Couple 0: persons $(0, 1)$
      - Couple 1: persons $(2, 3)$
      - $\dots$
      - Couple $k$: persons $(2k, 2k + 1)$
      - Any person $x$ belongs to couple ID:
        $$
        \text{couple}(x) = \lfloor x / 2 \rfloor = x \gg 1
        $$
    - The seats are grouped into adjacent pairs (couches): $(0, 1), (2, 3), \dots, (2i, 2i + 1)$.
    - A couple is successfully holding hands if both partners occupy the same adjacent seat pair $(2i, 2i + 1)$.
    - Single swap: Choose any two people anywhere on the row and swap their seats.
    - Objective: Find the **minimum number of swaps** to seat every couple side-by-side.
    - For $[0, 2, 1, 3]$:
      - Couch 0 (seats 0, 1): occupied by person 0 (Couple 0) and person 2 (Couple 1).
      - Couch 1 (seats 2, 3): occupied by person 1 (Couple 0) and person 3 (Couple 1).
      - Person 2 and Person 1 are misplaced.
      - Swap person 2 and person 1:
        $$
        [0, \mathbf{2}, \mathbf{1}, 3] \implies [0, \mathbf{1}, \mathbf{2}, 3]
        $$
      - Now Couch 0 has $(0, 1)$ (Couple 0) and Couch 1 has $(2, 3)$ (Couple 1).
      - Minimum swaps: **1**.
- **Cycle Decomposition & Union-Find Component Invariant:**
  - **The Couple Graph Representation:**
    - Consider an undirected graph with $N$ vertices representing the $N$ couples.
    - Each couch $i$ hosts two people: person $row[2i]$ and person $row[2i + 1]$.
    - Add an undirected edge between their respective couple IDs:
      $$
      u = row[2i] \gg 1, \quad v = row[2i + 1] \gg 1
      $$
    - If $u == v$, the couple is already sitting together (a self-loop).
    - If $u \ne v$, an edge connects couple $u$ and couple $v$.
  - **The $k - 1$ Swaps Theorem:**
    - Any connected component of $k$ couples represents an entangled permutation cycle.
    - A single swap between two people from different couples in the same component can always place at least one couple together while reducing the component size to $k - 1$.
    - Therefore, resolving an entangled component of size $k$ requires **strictly $k - 1$ swaps**.
  - **Global Formula ($N - C$):**
    - Let $C$ be the total number of connected components in the couple graph:
      $$
      \text{Total Swaps} = \sum_{j=1}^C (k_j - 1) = \sum_{j=1}^C k_j - \sum_{j=1}^C 1 = N - C
      $$
    - Computing the minimum swaps is equivalent to finding the number of connected components $C$ using Disjoint Set Union (Union-Find)!
- **Step-by-Step Worked Execution Trace on $row = [0, 2, 1, 3]$:**
  - Total people: $4 \implies$ total couples: $N = 4 / 2 = \mathbf{2}$.
  - Couples: Couple 0, Couple 1.
  - **Phase 0: Initialize Union-Find Forest:**
    - Parent array for 2 couples:
      $$
      p = [0, \; 1] \quad (C = 2 \text{ independent components})
      $$
  - **Phase 1: Process Couch 0 (Seats 0 and 1):**
    - Occupants: person $row[0] = 0$, person $row[1] = 2$.
    - Map to couples:
      $$
      a = 0 \gg 1 = \mathbf{0}
      $$
      $$
      b = 2 \gg 1 = \mathbf{1}
      $$
    - Union couple 0 and couple 1:
      $$
      find(0) = 0, \quad find(1) = 1 \implies p[0] \leftarrow 1
      $$
    - Couples 0 and 1 are now unified into a single connected component!
  - **Phase 2: Process Couch 1 (Seats 2 and 3):**
    - Occupants: person $row[2] = 1$, person $row[3] = 3$.
    - Map to couples:
      $$
      a = 1 \gg 1 = \mathbf{0}
      $$
      $$
      b = 3 \gg 1 = \mathbf{1}
      $$
    - Union couple 0 and couple 1:
      $$
      find(0) = 1, \quad find(1) = 1 \implies \mathbf{Already\ in\ Same\ Component!}
      $$
  - **Phase 3: Count Connected Components ($C$):**
    - Roots of the DSU forest:
      - Node 0: $p[0] = 1$ (child of 1)
      - Node 1: $p[1] = 1$ (root of component $\{0, 1\}$)
    - Total roots / components:
      $$
      C = \mathbf{1}
      $$
  - **Phase 4: Compute Minimum Swaps:**
    $$
    ans = N - C = 2 - 1 = \mathbf{1}
    $$
- **Already Paired Couples Trace ($row = [3, 2, 0, 1]$):**
  - Couch 0: $(3, 2) \implies$ both belong to Couple 1 ($a = 1, b = 1$). Self-loop.
  - Couch 1: $(0, 1) \implies$ both belong to Couple 0 ($a = 0, b = 0$). Self-loop.
  - No cross-couple edges exist $\implies C = 2$ disjoint components.
  - Swaps: $N - C = 2 - 2 = \mathbf{0}$.
- **3-Couple Circular Entanglement Trace ($[0, 2, 3, 4, 5, 1]$):**
  - Couch 0: Coup 0 & Coup 1.
  - Couch 1: Coup 1 & Coup 2.
  - Couch 2: Coup 2 & Coup 0.
  - All 3 couples form a single 3-cycle component ($C = 1$).
  - Swaps: $N - C = 3 - 1 = \mathbf{2}$.

This instance demonstrates permutation cycle graph decomposition and Disjoint Set Union component counting, mathematically proves why each swap reduces the cycle deficit by at most 1, and derives $O(N \alpha(N))$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $2N$ people sitting in $2N$ seats:
Couples are $(0, 1), (2, 3), \dots$. Couches are $(2i, 2i + 1)$.
Find the **minimum swaps** so every couple sits together.

```text
row = [ 0, 2, 1, 3 ]
N = 2 couples: Couple 0 = (0, 1), Couple 1 = (2, 3)

Couch 0 has person 0 (Couple 0) and person 2 (Couple 1) -> Edge (0, 1)
Couch 1 has person 1 (Couple 0) and person 3 (Couple 1) -> Edge (0, 1)

Both couples form 1 tangled component of size 2.
Swaps needed = size - 1 = 2 - 1 = 1 swap!

Result: 1
```

### The Invariant of the Component Formula $N - C$
- If $k$ couples are tangled together in a connected component, it takes exactly $k - 1$ swaps to resolve them.
- Summing over all $C$ connected components gives:
  $$\text{Total Swaps} = \sum (k_i - 1) = N - C$$
- Union-Find counts the components $C$ in nearly linear time.

---

## 2. Conceptual Foundation & Invariants

### 1. Couple Projection:
$$
couple(x) = x \gg 1
$$

### 2. Graph Construction & Component Counting:
For couch $i \in [0, N - 1]$:
$$
uf.union(row[2i] \gg 1, \; row[2i + 1] \gg 1)
$$
$$
ans = N - C = N - \sum_{i=0}^{N-1} [find(i) == i]
$$

> **Permutation Cycle Transposition Invariant.** In the symmetric group $S_N$, any permutation $\sigma$ factoring into $C$ disjoint cycles requires a minimum of $N - C$ transpositions to reduce to the identity permutation.

---

## 3. Step-by-Step Worked Execution

We trace $row = [0, 2, 1, 3]$:

---

### Step 1: Initialize
- $N = 2$ couples. $p = [0, 1]$.

---

### Step 2: Union Couches
- Couch 0: people $0, 2 \implies$ couple $0, 1 \implies union(0, 1) \implies p = [1, 1]$.
- Couch 1: people $1, 3 \implies$ couple $0, 1 \implies$ already connected.

---

### Step 3: Count Components
- Only root is 1 $\implies C = 1$.

---

### Step 4: Output
- $ans = N - C = 2 - 1 = \mathbf{1}$.

---

## 4. Complete Execution Trace

| Couch $i$ | Seat Occupants $(row[2i], row[2i+1])$ | Couple IDs $(a, b)$ | DSU Action Taken | DSU Roots Count $C$ |
|:---:|:---:|:---:|:---:|:---:|
| Initial | — | — | — | $2$ |
| $0$ | $(0, 2)$ | $(0, 1)$ | $union(0, 1)$ | $1$ |
| $1$ | $(1, 3)$ | $(0, 1)$ | Already unified | $1$ |
| **Final** | — | — | **$N - C = 2 - 1$** | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Already Sorted ($[0, 1, 2, 3]$):** Each couple sits together $\implies C = N \implies N - N = 0$ swaps.
- **Reverse Paired ($[1, 0, 3, 2]$):** $(1, 0)$ is couple 0, $(3, 2)$ is couple 1 $\implies 0$ swaps (order within the couch does not matter).
- **All Coups Tangled in Single Large Loop:** $C = 1 \implies N - 1$ swaps.
- **Minimal Case ($N = 1$):** 2 people $\implies 0$ swaps.

---

## 6. Traps & Common Anti-Patterns

- **Simulating Swaps Greedily:** Finding partners and simulating array swaps works in $O(N^2)$ but requires modifying the array and managing partner index tables. DSU calculates the exact optimal swaps purely via component connectivity in $O(N \alpha(N))$.
- **Pair Identification Off-By-One:** Person $x$ belongs to couple $x // 2$, **not** $x \% 2$. Bit shift $x \gg 1$ correctly groups $(0, 1) \to 0, (2, 3) \to 1$.
- **Treating Individual People as Nodes:** The graph nodes must be **couples** ($N$ nodes), not individual people ($2N$ nodes).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ couches, each doing one union operation: $\mathcal{O}(N \alpha(N))$.
  - Counting components takes $\mathcal{O}(N)$ find operations.
  - Total Time: strictly $\mathcal{O}(N \alpha(N))$ where $N \le 30$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the DSU parent array.
