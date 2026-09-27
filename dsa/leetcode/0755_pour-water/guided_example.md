# Guided Example: Pour Water

We trace the step-by-step fluid gravity simulation on 1D elevation profiles, left-priority descent scanning ($d = -1$), non-increasing terrain traversal ($heights[i+d] \le heights[i]$), closest-to-$k$ lowest basin settling ($j = i + d$ on strict drop), right-side fallback scanning ($d = +1$), stationary drop elevation ($heights[k] \leftarrow heights[k] + 1$), and cumulative terrain reshaping across successive droplets:

- **Input:**
  - Initial terrain: $heights = [2, 1, 1, 2, 1, 2, 2]$
  - Water volume: $volume = 4$
  - Pour index: $k = 3$
- **Required output:**
  $$
  [2, 2, 2, 3, 2, 2, 2]
  $$
  - Fluid dynamics rules for each droplet:
    1. A droplet is released at index $k$.
    2. **Leftward Flow First ($d = -1$):**
       - The droplet can flow left as long as the terrain does not rise ($heights[i - 1] \le heights[i]$).
       - If it encounters a strictly lower level ($heights[i - 1] < heights[i]$), it continues downhill.
       - If multiple adjacent positions share the lowest elevation, the droplet settles at the position **closest to $k$**.
       - If a valid drop point $j \ne k$ is found on the left, the droplet settles there ($heights[j] \leftarrow heights[j] + 1$).
    3. **Rightward Flow Fallback ($d = +1$):**
       - If the droplet cannot find a strictly lower elevation to the left, it attempts to flow right under the same physical rules ($heights[i + 1] \le heights[i]$).
       - If a lower point $j \ne k$ is found on the right, it settles at the lowest point closest to $k$.
    4. **Stationary Pool:**
       - If neither direction provides a strictly lower settling position, the droplet rests at its initial drop point:
         $$
         heights[k] \leftarrow heights[k] + 1
         $$
- **Monotonic Descent & Basin Settling Invariant:**
  - **Left-Preference Invariant:**
    - The physics simulation strictly prioritizes leftward drainage over rightward drainage.
    - Even if a deeper valley exists on the right, any strictly lower basin on the left absorbs the droplet first!
  - **Lowest Point Closest to $k$:**
    - When scanning downhill:
      - As long as the next cell is strictly lower ($heights[i + d] < heights[i]$), update candidate index $j \leftarrow i + d$.
      - If the next cell is at the same elevation ($heights[i + d] == heights[i]$), the droplet can traverse across the flat plain, but candidate $j$ is **not** updated to the further cell.
      - If the terrain rises later without going lower, $j$ remains anchored at the first (closest to $k$) cell of that plateau!
- **Step-by-Step Worked Execution Trace on the 4 Droplets:**
  - Initial array: $heights = [2, 1, 1, 2, 1, 2, 2]$ with pour source at $k = 3$ ($heights[3] = 2$).
  - **Droplet 1 ($v = 1$):**
    - Drop at $k = 3$ ($height = 2$).
    - Scan Left ($d = -1$):
      - Step to index 2: $heights[2] = 1 < heights[3] = 2 \implies$ strictly lower! Candidate $j \leftarrow 2$.
      - Step to index 1: $heights[1] = 1 \le heights[2] = 1 \implies$ plateau. $j$ remains $2$.
      - Step to index 0: $heights[0] = 2 > heights[1] = 1 \implies$ terrain rises! Scan terminates.
    - Settle point: $j = 2 \ne 3$.
    - Settles at index 2:
      $$
      heights[2] \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Terrain after Droplet 1:
      $$
      heights = [2, \; \mathbf{1}, \; \mathbf{2}, \; 2, \; 1, \; 2, \; 2]
      $$
  - **Droplet 2 ($v = 2$):**
    - Drop at $k = 3$ ($height = 2$).
    - Scan Left ($d = -1$):
      - Step to index 2: $heights[2] = 2 \le heights[3] = 2$ (plateau, $j$ still 3).
      - Step to index 1: $heights[1] = 1 < heights[2] = 2 \implies$ strictly lower! Candidate $j \leftarrow 1$.
      - Step to index 0: $heights[0] = 2 > heights[1] = 1 \implies$ rises (blocked).
    - Settle point: $j = 1 \ne 3$.
    - Settles at index 1:
      $$
      heights[1] \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Terrain after Droplet 2:
      $$
      heights = [2, \; \mathbf{2}, \; 2, \; 2, \; 1, \; 2, \; 2]
      $$
  - **Droplet 3 ($v = 3$):**
    - Drop at $k = 3$ ($height = 2$).
    - Scan Left ($d = -1$):
      - Indices 2, 1, 0 all have height 2.
      - No cell is strictly less than 2. Left scan yields $j = 3$ (fails).
    - Scan Right ($d = +1$):
      - Step to index 4: $heights[4] = 1 < heights[3] = 2 \implies$ strictly lower! Candidate $j \leftarrow 4$.
      - Step to index 5: $heights[5] = 2 > heights[4] = 1 \implies$ rises (blocked).
    - Settle point: $j = 4 \ne 3$.
    - Settles at index 4:
      $$
      heights[4] \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Terrain after Droplet 3:
      $$
      heights = [2, \; 2, \; 2, \; 2, \; \mathbf{2}, \; 2, \; 2]
      $$
  - **Droplet 4 ($v = 4$):**
    - Drop at $k = 3$ ($height = 2$).
    - Scan Left: All cells to left have height 2. No lower point ($j = 3$).
    - Scan Right: All cells to right have height 2. No lower point ($j = 3$).
    - Neither direction flows downhill!
    - Settles directly at drop point $k = 3$:
      $$
      heights[3] \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Terrain after Droplet 4:
      $$
      heights = [2, \; 2, \; 2, \; \mathbf{3}, \; 2, \; 2, \; 2]
      $$
  - **Final Elevation Profile:**
    $$
    ans = [2, \; 2, \; 2, \; 3, \; 2, \; 2, \; 2]
    $$
- **One-Sided Descent Trace ($heights = [1, 2, 3, 4], volume = 2, k = 3$):**
  - Continuous downhill slope to the left: $4 \to 3 \to 2 \to 1$.
  - First droplet rolls all the way to index 0 $\implies [2, 2, 3, 4]$.
  - Second droplet rolls to index 0 (tied with index 1, settles at closest) $\implies [2, 3, 3, 4]$ or fills bottom.

This instance demonstrates physical discrete fluid simulation and greedy valley filling, mathematically proves why prioritized direction and tied-level proximity uniquely determine equilibrium states, and derives $O(V \cdot N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given terrain heights $heights$, water $volume$, and pour point $k$:
Each droplet falls at $k$:
1. Tries to flow **left** to the lowest point $\le$ current level (closest to $k$ on ties).
2. If left has no lower point, tries to flow **right**.
3. If neither side has a lower point, stays at $k$.
Return final terrain heights.

```text
heights = [ 2, 1, 1, 2, 1, 2, 2 ], volume = 4, k = 3

Droplet 1: rolls left to index 2 (height 1) -> becomes [ 2, 1, 2, 2, 1, 2, 2 ]
Droplet 2: rolls left to index 1 (height 1) -> becomes [ 2, 2, 2, 2, 1, 2, 2 ]
Droplet 3: left is full (all 2s), rolls right to index 4 (height 1) -> [ 2, 2, 2, 2, 2, 2, 2 ]
Droplet 4: both sides flat at 2, rests at k = 3 -> [ 2, 2, 2, 3, 2, 2, 2 ]

Result: [ 2, 2, 2, 3, 2, 2, 2 ]
```

### The Invariant of Directional Priority & Flat Settling
- Scanning left first enforces left-side priority.
- Traversing while $heights[i+d] \le heights[i]$ allows crossing flat plateaus, but updating $j \leftarrow i + d$ ONLY on strict drops ($<$) ensures the droplet settles at the lowest point **closest to $k$**.

---

## 2. Conceptual Foundation & Invariants

### 1. Directional Scan Logic:
For $d \in \{-1, +1\}$:
$$
\text{while } 0 \le i + d < n \ \land \ heights[i + d] \le heights[i]:
$$
$$
\quad \text{if } heights[i + d] < heights[i] \implies j \leftarrow i + d
$$
$$
\quad i \leftarrow i + d
$$

### 2. Settling Rule:
$$
\text{If } j \ne k \implies heights[j] \leftarrow heights[j] + 1 \quad \text{else } heights[k] \leftarrow heights[k] + 1
$$

> **Potential Energy Minimization Invariant.** Each discrete droplet transition is a gradient descent on the potential function $U(x) = heights[x]$ subject to barrier admissibility $\Delta h \le 0$, with directional bias $\vec{d}_{left} \succ \vec{d}_{right}$ breaking energetic degeneracy.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Droplet 1
- Rolls left: $heights[2] = 1 < 2 \implies$ settles at index 2.
- $heights = [2, 1, 2, 2, 1, 2, 2]$.

---

### Step 2: Droplet 2
- Rolls left: passes 2, settles at index 1 ($height = 1$).
- $heights = [2, 2, 2, 2, 1, 2, 2]$.

---

### Step 3: Droplet 3
- Left is flat at 2.
- Rolls right: settles at index 4 ($height = 1$).
- $heights = [2, 2, 2, 2, 2, 2, 2]$.

---

### Step 4: Droplet 4
- Left and right are both flat at 2.
- Stays at $k = 3$.
- $heights = [2, 2, 2, \mathbf{3}, 2, 2, 2]$.

---

### Step 5: Output
$$
[2, 2, 2, 3, 2, 2, 2]
$$

---

## 4. Complete Execution Trace

| Droplet | Pour Index $k$ | Left Scan Result $j$ | Right Scan Result $j$ | Settling Location | Terrain State After Drop |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $3$ | $2$ (height 1) | — | Index $2$ | `[2, 1, 2, 2, 1, 2, 2]` |
| $2$ | $3$ | $1$ (height 1) | — | Index $1$ | `[2, 2, 2, 2, 1, 2, 2]` |
| $3$ | $3$ | $3$ (no drop) | $4$ (height 1) | Index $4$ | `[2, 2, 2, 2, 2, 2, 2]` |
| **$4$** | **$3$** | **$3$ (no drop)** | **$3$ (no drop)** | **Index $3$** | **`[2, 2, 2, 3, 2, 2, 2]`** |

---

## 5. Boundary Cases & Failure Modes

- **Volume 0:** Returns $heights$ unmodified.
- **Pour at Edges ($k = 0$ or $k = n - 1$):** Out-of-bounds guards prevent indexing errors; only one direction is scanned.
- **Deep Flat Valley ($[3, 1, 1, 1, 3]$ with $k = 4$):** Droplet enters from right, settles at index 3 (the closest of the three 1s to $k$).
- **V-Shaped Valley:** Fills the bottom element directly.

---

## 6. Traps & Common Anti-Patterns

- **Settling at Furthest Point on Plateau:** If terrain is $[3, 1, 1, 1, 3]$ with $k = 0$, settling at index 3 violates the rule to pick the lowest point **closest to $k$** (which is index 1).
- **Checking Right Before Left:** Problem explicitly mandates trying left first. Right is checked only if left has no lower point.
- **Climbing Over Higher Terrain:** Water cannot flow uphill ($heights[i + d] > heights[i]$); scan must terminate upon encountering any increase.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - For each of the $V$ droplets, we scan at most $N$ elements to the left and $N$ elements to the right: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(V \cdot N)$ where $V \le 100, N \le 100 \implies \le 10^4$ operations. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the input array modified in place.
