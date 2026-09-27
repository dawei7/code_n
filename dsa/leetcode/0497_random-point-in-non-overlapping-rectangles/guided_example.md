# Guided Example: Random Point in Non-overlapping Rectangles

We trace the step-by-step discrete lattice point counting ($A = (x_2 - x_1 + 1)(y_2 - y_1 + 1)$), cumulative weight prefix array construction ($s[i]$), binary search rectangle selection (`bisect_left(s, v)`), and uniform 2D integer coordinate sampling on representative non-overlapping rectangle layouts:

- **Input:**
  - $rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]$
- **Required outcome:** Every integer point in the covered space picked with exact equal probability $\frac{1}{T}$.
- **Discrete area and prefix sum construction:**
  - **Rectangle 0 ($[-2, -2, -1, -1]$):**
    - Horizontal integer span: $x \in [-2, -1] \implies x_2 - x_1 + 1 = -1 - (-2) + 1 = 2$
    - Vertical integer span: $y \in [-2, -1] \implies y_2 - y_1 + 1 = -1 - (-2) + 1 = 2$
    - Lattice points contained:
      $$
      A_0 = 2 \times 2 = \mathbf{4} \text{ points}
      $$
      (Points: $\{(-2, -2), (-2, -1), (-1, -2), (-1, -1)\}$)
    - Prefix sum: $s[0] = 4$
  - **Rectangle 1 ($[1, 0, 3, 0]$):**
    - Horizontal span: $x \in [1, 3] \implies 3 - 1 + 1 = 3$
    - Vertical span: $y \in [0, 0] \implies 0 - 0 + 1 = 1$
    - Lattice points contained:
      $$
      A_1 = 3 \times 1 = \mathbf{3} \text{ points}
      $$
      (Points: $\{(1, 0), (2, 0), (3, 0)\}$)
    - Prefix sum: $s[1] = s[0] + A_1 = 4 + 3 = \mathbf{7}$
  - Total integer points across all rectangles: $T = s[1] = \mathbf{7}$
  - Prefix array:
    $$
    s = [4, \; 7]
    $$
- **Sampling Trace (`pick()`):**
  - **Draw 1 (Random token $v = 3 \in [1, 7]$):**
    - Binary search $v = 3$ in $s = [4, 7]$:
      - $3 \le s[0] (4) \implies$ Selected rectangle is $idx = 0$!
    - Sample point inside Rectangle 0:
      - Pick $x \in [-2, -1]$ uniformly: e.g. $-2$
      - Pick $y \in [-2, -1]$ uniformly: e.g. $-1$
      - Output point: $\mathbf{(-2, -1)}$
  - **Draw 2 (Random token $v = 6 \in [1, 7]$):**
    - Binary search $v = 6$ in $s = [4, 7]$:
      - $6 > s[0] (4)$ and $6 \le s[1] (7) \implies$ Selected rectangle is $idx = 1$!
    - Sample point inside Rectangle 1:
      - Pick $x \in [1, 3]$ uniformly: e.g. $2$
      - Pick $y \in [0, 0]$ uniformly: $0$
      - Output point: $\mathbf{(2, 0)}$
  - Probability for any individual point:
    $$
    P(\text{Point } p) = P(\text{Rect } k) \times \frac{1}{A_k} = \frac{A_k}{T} \times \frac{1}{A_k} = \frac{1}{T} = \frac{1}{7}
    $$
    Every lattice point has exact uniform probability $\frac{1}{7}$!
- **Single Point Rectangle ($[1, 1, 1, 1]$):** Area is $1 \times 1 = 1 \implies$ Always returns $(1, 1)$.

This instance demonstrates discrete 2D spatial sampling with area-weighted selection, mathematically proves why proportional prefix sampling guarantees uniform point densities across unequal rectangles, and derives $O(N)$ initialization, $O(\log N)$ pick runtime, and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of non-overlapping axis-aligned rectangles $rects$:
Pick a random **integer point** $(x, y)$ inside the union of all rectangles.
Every integer point must have an **equal probability** of being chosen.

```text
Rectangle 0: [-2, -2, -1, -1] -> 2x2 = 4 integer points
Rectangle 1: [ 1,  0,  3,  0] -> 3x1 = 3 integer points
Total Integer Points across room: 4 + 3 = 7 points

Weighted Prefix Sum Array:
  Rect 0 claims tokens [1, 2, 3, 4]  (Weight 4/7)
  Rect 1 claims tokens [5, 6, 7]     (Weight 3/7)

Binary search on random token in [1, 7] chooses rectangle fairly!
```

### The Discrete Lattice vs Continuous Area Difference
In discrete integer sampling:
- The number of points along interval $[x_1, x_2]$ is $(x_2 - x_1 + 1)$, **not** $(x_2 - x_1)$!
- A degenerate line segment like $[1, 0, 3, 0]$ has continuous area 0, but contains **3 discrete integer points**: $(1, 0), (2, 0), (3, 0)$.
- The number of integer points in rectangle $[x_1, y_1, x_2, y_2]$ is:
  $$
  A_i = (x_2 - x_1 + 1) \times (y_2 - y_1 + 1)
  $$
- The probability of picking rectangle $i$ must be strictly proportional to $A_i$.

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative Discrete Area Array:
Let $N = |rects|$:
Compute prefix sum array $s$:
$$
s[i] = \sum_{j=0}^i (x_{2, j} - x_{1, j} + 1)(y_{2, j} - y_{1, j} + 1)
$$
- $s[i]$ is the cumulative number of lattice points contained in rectangles $0 \dots i$.
- The total number of points in the system is $T = s[N - 1]$.

### 2. Weighted Selection via Binary Search:
To pick a point:
1. Generate uniform integer $v \in [1, T]$.
2. Find the unique index $idx$ such that:
   $$
   s[idx - 1] < v \le s[idx]
   $$
   via binary search `bisect_left(s, v)`.
3. Within rectangle $rects[idx] = [x_1, y_1, x_2, y_2]$, choose $x \sim [x_1, x_2]$ and $y \sim [y_1, y_2]$ uniformly at random.

> **Uniform Point Density Invariant.** Because rectangle $idx$ is chosen with probability $A_{idx} / T$, and each of its points is chosen with conditional probability $1 / A_{idx}$, the overall marginal probability of any point is $\frac{A_{idx}}{T} \times \frac{1}{A_{idx}} = \frac{1}{T}$.

---

## 3. Step-by-Step Worked Execution

We trace $rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]$:

---

### Step 1: Initialization Phase
1. **Rectangle 0 ($[-2, -2, -1, -1]$):**
   - Width: $-1 - (-2) + 1 = 2$.
   - Height: $-1 - (-2) + 1 = 2$.
   - Lattice points: $A_0 = 2 \times 2 = 4$.
   - $s[0] = 4$.
2. **Rectangle 1 ($[1, 0, 3, 0]$):**
   - Width: $3 - 1 + 1 = 3$.
   - Height: $0 - 0 + 1 = 1$.
   - Lattice points: $A_1 = 3 \times 1 = 3$.
   - $s[1] = s[0] + 3 = 4 + 3 = 7$.
- Total points: $T = 7$. Prefix sums: $s = [4, 7]$.

---

### Step 2: Sampling Call `pick()`
- Roll uniform integer $v \in [1, 7]$. Suppose $v = 5$.
- Binary search $v = 5$ in $s = [4, 7]$:
  - $s[0] = 4 < 5$.
  - $s[1] = 7 \ge 5$.
  - Binary search selects index $idx = 1$.
- Retrieve Rectangle 1: $[x_1, y_1, x_2, y_2] = [1, 0, 3, 0]$.
- Pick $x \in [1, 3]$ uniformly: suppose roll yields $x = 3$.
- Pick $y \in [0, 0]$ uniformly: yields $y = 0$.
- Emit point: **`(3, 0)`**.

---

## 4. Complete Execution Trace

| Random Token $v \in [1, 7]$ | Binary Search on $s = [4, 7]$ | Chosen Rectangle $idx$ | Rectangle Bounds | Point Sampled $(x, y)$ | Point Probability |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $1 \le 4$ | Rect 0 | $[-2, -2, -1, -1]$ | $(-2, -2)$ | $1/7$ |
| **$2$** | $2 \le 4$ | Rect 0 | $[-2, -2, -1, -1]$ | $(-2, -1)$ | $1/7$ |
| **$3$** | $3 \le 4$ | Rect 0 | $[-2, -2, -1, -1]$ | $(-1, -2)$ | $1/7$ |
| **$4$** | $4 \le 4$ | Rect 0 | $[-2, -2, -1, -1]$ | $(-1, -1)$ | $1/7$ |
| **$5$** | $5 > 4, 5 \le 7$ | Rect 1 | $[1, 0, 3, 0]$ | $(1, 0)$ | $1/7$ |
| **$6$** | $6 \le 7$ | Rect 1 | $[1, 0, 3, 0]$ | $(2, 0)$ | $1/7$ |
| **$7$** | $7 \le 7$ | Rect 1 | $[1, 0, 3, 0]$ | $(3, 0)$ | $1/7$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Rectangle ($N = 1$):** Prefix array has 1 element $\implies$ Always picks from Rect 0.
- **Single Point Rectangle ($[0, 0, 0, 0]$):** Span is $1 \times 1 = 1$, correctly contributing 1 point to $T$.
- **1D Line Segment Rectangles ($[0, 0, 10, 0]$):** Height is $0 - 0 + 1 = 1$. Total points $= 11 \times 1 = 11$.
- **Huge Rectangles ($10^8 \times 10^8$):** Prefix values can reach $10^{16}$, which fit comfortably inside 64-bit integers.

---

## 6. Traps & Common Anti-Patterns

- **Using Continuous Area ($(x_2 - x_1)(y_2 - y_1)$):** Calculating area without $+1$ assigns zero weight to flat 1D rectangles like $[1, 0, 3, 0]$, completely ignoring their points.
- **Picking Rectangle Uniformly ($idx = \text{random}(0, N-1)$):** Choosing rectangles uniformly instead of by area gives a tiny $1 \times 1$ rectangle the same probability as a massive $1000 \times 1000$ rectangle, destroying uniform point probability.
- **Linear Scan to Find Rectangle:** Using a linear loop to find where $v$ falls takes $O(N)$ per pick. Binary search `bisect_left` runs in strictly $O(\log N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: Iterating over $N$ rectangles to compute points and prefix sums takes $\mathcal{O}(N)$ time.
  - Each `pick()` call:
    - Random token generation: $O(1)$.
    - Binary search on prefix array of size $N$: $O(\log N)$.
    - Coordinate sampling: $O(1)$.
    - Total per pick: $\mathcal{O}(\log N)$. For $N = 100$, takes $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the prefix sum array $s$.