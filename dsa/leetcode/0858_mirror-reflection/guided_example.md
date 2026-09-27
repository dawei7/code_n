# Guided Example: Mirror Reflection

We trace the step-by-step optical ray unfolding onto an infinite planar lattice, least common multiple ($\text{lcm}$) corner intersection derivation, parity analysis of vertical and horizontal reflections, and receptor identification on representative square rooms:

- **Input:**
  $$
  p = 2, \quad q = 1
  $$
- **Required output:** `2`
  - Geometry of the room:
    - A square room with side length $p = 2$.
    - Mirrors on all 4 walls.
    - Receptors at three corners:
      - Receptor $0$: Southeast corner $(p, 0) = (2, 0)$.
      - Receptor $1$: Northeast corner $(p, p) = (2, 2)$.
      - Receptor $2$: Northwest corner $(0, p) = (0, 2)$.
      - Southwest corner $(0, 0)$ is the laser emitter.
    - Laser ray starts at $(0, 0)$ and first strikes the east wall at $(p, q) = (2, 1)$.
    - Upon striking a mirror wall, it reflects specularly (angle of incidence equals angle of reflection).
    - Objective: Determine which receptor ($0, 1$, or $2$) the ray hits first.
- **The Optical Reflection Principle (Grid Unfolding):**
  - Instead of reflecting the ray inside a single $p \times p$ box, we **unfold the room into an infinite periodic 2D grid** of $p \times p$ squares!
  - In the unfolded grid, the laser travels in a **straight line** with constant slope:
    $$
    \text{slope} = \frac{\Delta y}{\Delta x} = \frac{q}{p}
    $$
  - The ray hits a corner of the original room whenever the straight line passes through a grid vertex $(x, y) = (m \cdot p, n \cdot p)$, where $m$ and $n$ are positive integers.
  - Since $y = \frac{q}{p} x$, setting $x = m \cdot p$ gives $y = m \cdot q$.
  - For $y$ to be an exact multiple of $p$, say $n \cdot p$, we require:
    $$
    m \cdot q = n \cdot p = \text{lcm}(p, q)
    $$
  - Dividing both $p$ and $q$ by their greatest common divisor $g = \gcd(p, q)$:
    $$
    p' = \frac{p}{g}, \quad q' = \frac{q}{g}
    $$
    Then $m = p'$ (number of rooms traversed horizontally) and $n = q'$ (number of rooms traversed vertically).

---

## 1. Instance & Teaching Goal

Given $p = 2$ and $q = 1$, trace the laser trajectory until it hits a corner receptor.

```text
Unfolded Plane (p = 2, q = 1):
Vertical (y):
 2 |  [2]       [1]       [2]
 1 |       \   /   \     /
 0 |  (0,0)  \     / \  /
   +-----------------------
       0       2       4 (x)

Straight ray from (0, 0) to (4, 2):
  At x = 2: y = 1 (East wall hit, reflects westward in real room)
  At x = 4: y = 2 (Reaches grid vertex (2*p, 1*p))
  
Parity:
  Horizontal: 4 / 2 = 2 boxes (Even -> Left/West wall)
  Vertical:   2 / 2 = 1 box   (Odd  -> Top/North wall)
  West + North = Receptor 2!
```

The teaching goal is to demonstrate the powerful geometric transformation from internal polygonal reflections to linear lattice path intersections.

---

## 2. Conceptual Foundation & Invariants

### 1. Parity Mapping Theorem:
Because reflections alternate the orientation of the room:
- **Horizontal Axis ($x = m \cdot p$):**
  $$
  m \pmod 2 = \begin{cases}
  1 & \text{Ray is on the East wall } (x = p) \\
  0 & \text{Ray is on the West wall } (x = 0)
  \end{cases}
  $$
- **Vertical Axis ($y = n \cdot p$):**
  $$
  n \pmod 2 = \begin{cases}
  1 & \text{Ray is on the North ceiling } (y = p) \\
  0 & \text{Ray is on the South floor } (y = 0)
  \end{cases}
  $$

### 2. Receptor Classification Table:
Since $\gcd(p', q') = 1$, $p'$ and $q'$ cannot both be even:

| Horizontal $p' \pmod 2$ | Vertical $q' \pmod 2$ | Effective Position $(x, y)$ | Corresponding Receptor |
|:---:|:---:|:---:|:---:|
| $1$ (Odd) | $1$ (Odd) | $(p, p)$ [Northeast] | **`1`** |
| $1$ (Odd) | $0$ (Even) | $(p, 0)$ [Southeast] | **`0`** |
| $0$ (Even) | $1$ (Odd) | $(0, p)$ [Northwest] | **`2`** |

---

## 3. Step-by-Step Worked Execution

We trace $p = 2, q = 1$:

---

### Step 1: Compute Greatest Common Divisor
$$
g = \gcd(p, q) = \gcd(2, 1) = 1
$$

---

### Step 2: Reduce Coordinates to Coprime Ratio
$$
p' = \frac{p}{g} = \frac{2}{1} = 2
$$
$$
q' = \frac{q}{g} = \frac{1}{1} = 1
$$
- The laser traverses $p' = 2$ rooms horizontally and $q' = 1$ room vertically to reach the first grid vertex.
- Total distance in $x$: $2 \times 2 = 4$.
- Total distance in $y$: $2 \times 1 = 2$.
- The straight-line target is point $(4, 2)$.

---

### Step 3: Evaluate Parities
- Horizontal parity:
  $$
  p' \pmod 2 = 2 \pmod 2 = \mathbf{0} \quad (\text{Even} \implies \text{West Wall})
  $$
- Vertical parity:
  $$
  q' \pmod 2 = 1 \pmod 2 = \mathbf{1} \quad (\text{Odd} \implies \text{North Ceiling})
  $$

---

### Step 4: Map to Corner Receptor
- Coordinate combination: $(\text{West}, \text{North}) = (0, p)$.
- The receptor at $(0, p)$ is **Receptor 2**.
- **Output:** **`2`**.

---

## 4. Complete Execution Trace

| Ray Segment | Start $(x_0, y_0)$ | Traveled $(\Delta x, \Delta y)$ | Unfolded End $(x, y)$ | Wall Struck | Folded Room Coordinate | Receptor Hit? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(0, 0)$ | $(2, 1)$ | $(2, 1)$ | East Wall | $(2, 1)$ | No (Interior of wall) |
| **$2$** | $(2, 1)$ | $(2, 1)$ | $(4, 2)$ | West / North Corner | $(0, 2)$ | **`Yes -> Receptor 2`** |

---

## 5. Boundary Cases & Failure Modes

- **$p = q$ (e.g. $p=2, q=2$):** $\gcd(2, 2) = 2 \implies p'=1, q'=1$. Ray directly strikes Receptor $1$ on the first shot.
- **$q = 0$:** By problem constraints $1 \le q \le p$, so $q \ne 0$.
- **Odd $p$, Even $q$ (e.g. $p = 3, q = 2$):** $g = 1 \implies p' = 3 \equiv 1 \pmod 2, q' = 2 \equiv 0 \pmod 2$. East wall + South floor $\implies$ Receptor $0$.

---

## 6. Traps & Common Anti-Patterns

- **Step-by-Step Ray Tracing Simulation:** Simulating each wall reflection with floating-point coordinates accumulates precision error and causes TLE when $p$ and $q$ are large ($10^5$).
- **Confusing Horizontal vs Vertical Box Counts:** $p'$ (derived from $p$) corresponds to the horizontal traversal count, while $q'$ corresponds to the vertical traversal count. Reversing their roles swaps receptors $0$ and $2$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Greatest common divisor computation using Euclidean algorithm: $\mathcal{O}(\log(\min(p, q)))$.
  - Parity bit checks: $\mathcal{O}(1)$.
  - Total Time: $\mathcal{O}(\log(\min(p, q)))$, finishing in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using fixed scalar registers.
