# Guided Example: Line Reflection

We trace the step-by-step horizontal coordinate bound derivation ($\min_x, \max_x$), integer reflection sum computation ($s = \min_x + \max_x$), hash set existence probing (`point_set`), and symmetric partner validation ($(s - x, y) \in point\_set$) on representative 2D point sets:

- **Input:** `points = [[1, 1], [-1, 1]]`
- **Required output:** `true`
  - Horizontal bounds: $\min_x = -1, \max_x = 1$
  - Doubled symmetry axis coordinate: $s = \min_x + \max_x = -1 + 1 = 0$ (axis of reflection $x = 0$)
  - Partner verification:
    - Point $(1, 1)$: reflected point $(0 - 1, 1) = (-1, 1) \in point\_set$ (Valid)
    - Point $(-1, 1)$: reflected point $(0 - (-1), 1) = (1, 1) \in point\_set$ (Valid)
  - All points have valid symmetric counterparts $\implies \text{true}$
- **Asymmetric Vertical Height Counterexample:** `points = [[1, 1], [-1, -1]]`
  - Bounds: $\min_x = -1, \max_x = 1 \implies s = 0$
  - Reflection of $(1, 1)$ requires partner $(-1, 1)$, but existing point is $(-1, -1) \implies \text{false}$
- **Self-Reflecting Axis Points:** A point on the reflection axis $(x_0, y)$ has $s - x_0 = x_0$, reflecting to itself

This instance demonstrates geometric reflection invariants, mathematically proves why extreme horizontal coordinates uniquely constrain the vertical symmetry axis, eliminates floating-point division using integer doubling, and achieves $O(N)$ linear time and $O(N)$ space complexity.

---

## 1. Instance & Teaching Goal

Given $N$ points on a 2D plane:
$$
points = [[1, 1], \; [-1, 1]]
$$
Determine whether there exists a vertical line $x = c$ parallel to the y-axis such that reflecting all points across $x = c$ maps the set of points onto itself:

```text
Visual Coordinate Plane:
y = 1 :  (-1, 1) -------- [x = 0] -------- (1, 1)
               <-- dist = 1 -->|<-- dist = 1 -->

Both points mirror symmetrically across x = 0.
Symmetry Output: true
```

### The Uniqueness of the Reflection Axis
If a valid line $x = c$ exists:
- The point with the minimum horizontal coordinate $\min_x$ must reflect to the point with the maximum coordinate $\max_x$.
- The distance from $\min_x$ to $c$ must equal the distance from $c$ to $\max_x$:
  $$
  c - \min_x = \max_x - c \implies 2c = \min_x + \max_x
  $$
- Therefore, the candidate axis is **uniquely fixed**: $c = \frac{\min_x + \max_x}{2}$.
- Rather than dividing by 2 (which introduces floating-point fractions like $c = 1.5$), we define $s = \min_x + \max_x$. The reflected x-coordinate of any point $x$ is:
  $$
  x' = 2c - x = s - x
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Extrema and Set Construction
In a single linear pass over `points`:
- Compute global horizontal extrema:
  $$
  \min_x = \min_{(x, y) \in points} x, \quad \max_x = \max_{(x, y) \in points} x
  $$
- Insert all coordinate pairs $(x, y)$ as tuples into a hash set `point_set`.
- Define reflection sum: $s = \min_x + \max_x$.

### 2. Universal Symmetry Predicate
A set is vertically symmetric about $x = s/2$ if and only if:
$$
\forall (x, y) \in points, \quad (s - x, \; y) \in point\_set
$$

> **Invariant.** If any point $(x, y)$ lacks its counterpart $(s - x, y)$ in `point_set`, no line parallel to the y-axis can reflect the set onto itself.

---

## 3. Step-by-Step Worked Execution

We trace `points = [[1, 1], [-1, 1]]`:

---

### Step 1: Compute Extrema and Populate Set
- Process point $(1, 1)$:
  - $\min_x = \min(\infty, 1) = 1$
  - $\max_x = \max(-\infty, 1) = 1$
  - Add $(1, 1)$ to `point_set`.
- Process point $(-1, 1)$:
  - $\min_x = \min(1, -1) = -1$
  - $\max_x = \max(1, -1) = 1$
  - Add $(-1, 1)$ to `point_set`.
- Hash set contents:
  $$
  point\_set = \{(1, 1), \; (-1, 1)\}
  $$

---

### Step 2: Determine Candidate Reflection Sum $s$
$$
s = \min_x + \max_x = -1 + 1 = \mathbf{0}
$$
The line of reflection is $x = s/2 = 0$.

---

### Step 3: Validate Reflections for All Points
1. **Point $(1, 1)$:**
   - Compute required reflection: $(s - x, \; y) = (0 - 1, \; 1) = \mathbf{(-1, 1)}$.
   - Probe `point_set`: Is $(-1, 1) \in point\_set$? **Yes!**
2. **Point $(-1, 1)$:**
   - Compute required reflection: $(s - x, \; y) = (0 - (-1), \; 1) = \mathbf{(1, 1)}$.
   - Probe `point_set`: Is $(1, 1) \in point\_set$? **Yes!**

---

### Step 4: Final Confirmation
Every point has passed the symmetry verification.
$$
\text{Result} = \mathbf{\text{true}}
$$

---

## 4. Complete Execution Trace

```text
Points: [[1, 1], [-1, 1]]
min_x = -1, max_x = 1 -> s = -1 + 1 = 0
point_set = {(1, 1), (-1, 1)}

Verification:
Point (1, 1)  -> required partner: (0 - 1, 1) = (-1, 1)  -> In set? True
Point (-1, 1) -> required partner: (0 - -1, 1) = (1, 1)  -> In set? True

all(...) evaluated to True -> return True
```

| Point Inspected $(x, y)$ | Reflection Formula $(s - x, y)$ | Partner Evaluated | In `point_set`? | Status |
|:---:|:---:|:---:|:---:|:---:|
| $(1, 1)$ | $(0 - 1, 1)$ | $(-1, 1)$ | Yes | Verified |
| $(-1, 1)$ | $(0 - (-1), 1)$ | $(1, 1)$ | Yes | Verified |
| **All Passed** | - | - | - | **`true` (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $L$ be a vertical line of reflection. For any finite set of points, reflection is a distance-preserving isometry. The extreme coordinates $\min_x$ and $\max_x$ must map to each other, which uniquely fixes the axis at $x = (\min_x + \max_x)/2$. If every point $(x, y)$ reflects to an existing point $(s - x, y)$, then the set is closed under reflection across $L$, proving reflection symmetry.

**Completeness.** Since the candidate axis is unique, if the set fails the reflection test for this axis, no other vertical line can be an axis of symmetry. Checking each point in $O(1)$ average time guarantees an exhaustive and complete verification.

---

## 6. Traps This Instance Exposes

- **Floating-Point Imprecision:** Using float division `c = (min_x + max_x) / 2` and checking `2 * c - x` can introduce floating-point inaccuracies for half-integers. Working purely with integer sum $s = \min_x + \max_x$ eliminates rounding errors entirely.
- **Vertical Coordinate Matching:** A common mistake is only verifying horizontal balance $\sum x_i$ without checking if the corresponding $y$ coordinate matches. Points must share the exact same $y$ height ($y' = y$).
- **Duplicate Points in Input:** If the input contains duplicate coordinates, `set(points)` deduplicates them cleanly. Under set-reflection semantics, repeating a point does not invalidate symmetry.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of points.
  - Finding $\min_x$, $\max_x$, and populating `point_set` takes $O(N)$ time.
  - Verifying the reflection of each point takes $N$ iterations with $O(1)$ average set lookup time.
  - Overall runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(U)$, where $U \le N$ is the number of unique points stored in `point_set`.
