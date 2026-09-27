# Guided Example: Image Overlap

We trace the step-by-step 2D lattice translation geometry, relative displacement vector calculation ($\vec{\Delta} = (i - h, j - k)$), sparse 1-pixel coordinate extraction, translation histogram aggregation ($cnt[\vec{\Delta}] \mathrel{+}= 1$), and maximum overlapping pixel count determination on representative binary image pairs:

- **Input:**
  $$
  img1 = \begin{bmatrix}
  1 & 1 & 0 \\
  0 & 1 & 0 \\
  0 & 1 & 0
  \end{bmatrix}, \quad
  img2 = \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 1 & 1 \\
  0 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Image translation rules:
    - We are given two $n \times n$ binary matrices $img1$ and $img2$.
    - We may translate (slide) one image horizontally and vertically by any integer offset $(\Delta r, \Delta c)$.
    - When an image slides, pixels that fall outside the $n \times n$ boundary are discarded, and uncovered regions are padded with zeros.
    - Two 1-pixels **overlap** if after translation, a 1 from $img1$ aligns at the exact same grid coordinate $(h, k)$ as a 1 in $img2$.
    - Objective: Find the maximum possible number of overlapping 1-pixels across all valid 2D translations.
    - For the input images:
      - 1-pixels in $img1$: $(0, 0), (0, 1), (1, 1), (2, 1)$ (4 pixels).
      - 1-pixels in $img2$: $(1, 1), (1, 2), (2, 2)$ (3 pixels).
      - If we slide $img1$ down by 1 row ($\Delta r = +1$) and right by 1 column ($\Delta c = +1$):
        - Coordinate $(0, 0) \to (1, 1)$ (matches $img2$)
        - Coordinate $(0, 1) \to (1, 2)$ (matches $img2$)
        - Coordinate $(1, 1) \to (2, 2)$ (matches $img2$)
        - Coordinate $(2, 1) \to (3, 2)$ (falls off grid)
      - Exactly **3 pixels** overlap simultaneously!
      - Maximum overlap possible: **`3`**.
- **Vector Cross-Correlation Invariant:**
  - **The Translation Alignment Condition:**
    - Suppose a 1-pixel at $(i, j) \in img1$ maps to a 1-pixel at $(h, k) \in img2$.
    - The required translation vector must satisfy:
      $$
      (i, j) + (\Delta r, \Delta c) = (h, k) \iff (\Delta r, \Delta c) = (h - i, k - j)
      $$
      *(Equivalently, the displacement difference $(i - h, j - k)$ is constant)*.
  - **Shared Displacement Equivalence:**
    - Two pairs of 1-pixels $(p_1, q_1)$ and $(p_2, q_2)$ will **overlap under the exact same translation** if and only if their displacement vectors are identical:
      $$
      p_1 - q_1 = p_2 - q_2
      $$
  - **Displacement Histogram Mapping:**
    - Rather than testing all $(2n - 1)^2$ possible translations and scanning the entire grid for each:
    - Directly compute the vector difference for every pair of 1-pixels:
      $$
      \vec{d} = (i - h, \; j - k)
      $$
    - Increment the count for vector $\vec{d}$ in a frequency hash map $cnt$:
      $$
      cnt[\vec{d}] \leftarrow cnt[\vec{d}] + 1
      $$
    - The value $cnt[\vec{d}]$ is precisely the number of 1-pixels that overlap when the images are shifted by that vector!
    - The maximum overlap is simply $\max(cnt.\text{values}() \cup \{0\})$.
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Image Pair:**
  - **Coordinates of 1-pixels in $img1$ ($P$):**
    $$
    P = [(0, 0), \; (0, 1), \; (1, 1), \; (2, 1)]
    $$
  - **Coordinates of 1-pixels in $img2$ ($Q$):**
    $$
    Q = [(1, 1), \; (1, 2), \; (2, 2)]
    $$
  - Initialize frequency map: $cnt = \{\}$.
  - **Pairwise Displacement Computation:**
    - **From $p = (0, 0)$:**
      - Against $(1, 1)$: $\vec{d} = (0 - 1, 0 - 1) = \mathbf{(-1, -1)} \implies cnt[(-1, -1)] \leftarrow 1$.
      - Against $(1, 2)$: $\vec{d} = (0 - 1, 0 - 2) = (-1, -2) \implies cnt[(-1, -2)] \leftarrow 1$.
      - Against $(2, 2)$: $\vec{d} = (0 - 2, 0 - 2) = (-2, -2) \implies cnt[(-2, -2)] \leftarrow 1$.
    - **From $p = (0, 1)$:**
      - Against $(1, 1)$: $\vec{d} = (0 - 1, 1 - 1) = (-1, 0) \implies cnt[(-1, 0)] \leftarrow 1$.
      - Against $(1, 2)$: $\vec{d} = (0 - 1, 1 - 2) = \mathbf{(-1, -1)} \implies cnt[(-1, -1)] \leftarrow \mathbf{2}$.
      - Against $(2, 2)$: $\vec{d} = (0 - 2, 1 - 2) = (-2, -1) \implies cnt[(-2, -1)] \leftarrow 1$.
    - **From $p = (1, 1)$:**
      - Against $(1, 1)$: $\vec{d} = (1 - 1, 1 - 1) = (0, 0) \implies cnt[(0, 0)] \leftarrow 1$.
      - Against $(1, 2)$: $\vec{d} = (1 - 1, 1 - 2) = (0, -1) \implies cnt[(0, -1)] \leftarrow 1$.
      - Against $(2, 2)$: $\vec{d} = (1 - 2, 1 - 2) = \mathbf{(-1, -1)} \implies cnt[(-1, -1)] \leftarrow \mathbf{3}$.
    - **From $p = (2, 1)$:**
      - Against $(1, 1)$: $\vec{d} = (2 - 1, 1 - 1) = (1, 0) \implies cnt[(1, 0)] \leftarrow 1$.
      - Against $(1, 2)$: $\vec{d} = (2 - 1, 1 - 2) = (1, -1) \implies cnt[(1, -1)] \leftarrow 1$.
      - Against $(2, 2)$: $\vec{d} = (2 - 2, 1 - 2) = (0, -1) \implies cnt[(0, -1)] \leftarrow 2$.
  - **Frequency Histogram Summary:**
    - Vector $\mathbf{(-1, -1)}$: frequency **$3$**.
    - Vector $(0, -1)$: frequency $2$.
    - All other vectors: frequency $1$.
  - **Maximum Count Extraction:**
    $$
    ans = \max(cnt.\text{values}()) = \mathbf{3}
    $$
- **Zero 1-Pixels in Image ($img1 = [[0]], img2 = [[0]]$):**
  - $cnt$ is empty $\implies$ returns $0$.
- **Identical Images Trace ($img1 = img2$):**
  - Zero translation $(0, 0)$ matches every 1-pixel with itself $\implies ans = \text{total 1s in } img1$.

This instance demonstrates 2D discrete cross-correlation on sparse point sets and Minkowski difference representation, mathematically proves why counting vector differences isolates the optimal translation orbit in sub-grid complexity, and derives $O(M_1 \cdot M_2)$ runtime where $M \le N^2$, bounded by $O(N^4)$, and $O(M_1 \cdot M_2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two $n \times n$ binary matrices $img1$ and $img2$:
Slide $img1$ in any direction by integer offsets.
Find the **maximum number of overlapping 1-pixels**.

```text
img1:                img2:
  1 1 0                0 0 0
  0 1 0                0 1 1
  0 1 0                0 0 1

Slide img1 down 1 and right 1:
  (0, 0) -> (1, 1) [matches img2!]
  (0, 1) -> (1, 2) [matches img2!]
  (1, 1) -> (2, 2) [matches img2!]

3 pixels overlap!
Result: 3
```

### The Invariant of Displacement Hashing
- Any 1-pixel at $(i, j)$ in $img1$ aligns with $(h, k)$ in $img2$ under displacement:
  $$
  \vec{\Delta} = (i - h, \; j - k)
  $$
- Pixels that share the same displacement vector overlap under that exact translation.
- Hash map counts occurrences of each displacement vector; the answer is the maximum count.

---

## 2. Conceptual Foundation & Invariants

### 1. Minkowski Difference Representation:
$$
\text{Overlap}(\vec{v}) = \big| \{ (i, j) \in \text{supp}(img1) \mid (i, j) - \vec{v} \in \text{supp}(img2) \} \big|
$$
$$
\text{supp}(img) = \{ (r, c) \mid img[r][c] = 1 \}
$$

### 2. Hash Aggregation:
$$
cnt[\vec{\Delta}] = \sum_{p \in \text{supp}(img1)} \sum_{q \in \text{supp}(img2)} \mathbb{I}[p - q = \vec{\Delta}]
$$
$$
ans = \max_{\vec{\Delta}} cnt[\vec{\Delta}]
$$

> **Cross-Correlation Support Invariant.** The 2D cross-correlation $(img1 \star img2)[\Delta]$ has support bounded by $[-n+1, n-1]^2$. The value at $\Delta$ equals the cardinality of the fiber $\pi^{-1}(\Delta)$ under the difference projection $\pi(p, q) = p - q$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: 1-Pixel Coordinates
- $img1$: $(0, 0), (0, 1), (1, 1), (2, 1)$.
- $img2$: $(1, 1), (1, 2), (2, 2)$.

---

### Step 2: Compute Vectors
- $(0, 0) - (1, 1) = \mathbf{(-1, -1)}$.
- $(0, 1) - (1, 2) = \mathbf{(-1, -1)}$.
- $(1, 1) - (2, 2) = \mathbf{(-1, -1)}$.

---

### Step 3: Find Maximum Frequency
- Vector $(-1, -1)$ appears **3 times**.

---

### Step 4: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Point in $img1$ | Point in $img2$ | Displacement Vector $\vec{d} = p - q$ | Count of $\vec{d}$ |
|:---:|:---:|:---:|:---:|
| $(0, 0)$ | $(1, 1)$ | $(-1, -1)$ | $1$ |
| $(0, 1)$ | $(1, 2)$ | $(-1, -1)$ | $2$ |
| **$(1, 1)$** | **$(2, 2)$** | **$(-1, -1)$** | **`3`** |
| Other pairs | Various | Miscellaneous vectors | $1$ or $2$ |
| **Max Count** | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **No 1s in Either Image:** Counter is empty $\implies$ returns 0.
- **Single 1 in Both Images:** Counter has 1 entry with count 1 $\implies$ returns 1.
- **Dense All-1s Images ($30 \times 30$):** Max overlap is $30 \times 30 = 900$ at shift $(0, 0)$.
- **Disjoint 1s That Never Align:** Max count is 1.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Sliding and Matrix Comparison ($O(N^6)$):** Sliding $img1$ through all $(2N)^2$ offsets and comparing $N^2$ cells for each requires $O(N^4)$ matrix operations. Sparse vector hashing scales with the number of 1-pixels ($M_1 \cdot M_2 \le N^4$).
- **Sign Inversion Confusion:** Whether using $(i - h, j - k)$ or $(h - i, k - j)$, remain consistent across all pairs.
- **Handling Empty Counter:** Always guard `max(cnt.values()) if cnt else 0` to prevent `ValueError` on empty inputs.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $M_1, M_2$ be the number of 1s in $img1$ and $img2$ ($M_1, M_2 \le N^2 \le 900$).
  - Nested loops visit only pairs of 1-pixels: $\mathcal{O}(M_1 \cdot M_2)$.
  - Worst case (all 1s): $N^4 = 30^4 = 8.1 \times 10^5$ operations. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M_1 \cdot M_2)$ memory for the frequency map, bounded by $(2N - 1)^2 \approx 3600$ distinct offset keys.
