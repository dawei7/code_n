# Guided Example: Split Array With Same Average

We trace the step-by-step mean centering transformation ($v' = n \cdot v - \sum nums$), zero-sum proper subset isomorphism ($\sum_{x \in A} v' = 0$), meet-in-the-middle subset generation ($2^{n/2}$ partition search), left-half hash set accumulation ($vis$), right-half complement lookup ($-t \in vis$), and whole-array boundary exclusion on representative numerical sequences:

- **Input:**
  $$
  nums = [1, 2, 3, 4, 5, 6, 7, 8]
  $$
- **Required output:** `true`
  - Problem requirements & average equality:
    - You must split $nums$ of length $n$ into two non-empty, disjoint sub-arrays $A$ and $B$ such that:
      $$
      \text{average}(A) = \text{average}(B)
      $$
    - Because the total sum is partitioned ($sum(A) + sum(B) = sum(nums)$), the sub-arrays share the exact same average if and only if their average equals the global mean of the entire array:
      $$
      \text{average}(A) = \text{average}(B) = \mu = \frac{\sum nums}{n}
      $$
    - For $nums = [1, 2, 3, 4, 5, 6, 7, 8]$ ($n = 8$):
      - Total sum: $s = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36$.
      - Global average: $\mu = 36 / 8 = \mathbf{4.5}$.
      - Consider sub-array $A = [1, 8]$ (size 2):
        $$
        \text{average}(A) = \frac{1 + 8}{2} = \frac{9}{2} = \mathbf{4.5}
        $$
      - The remaining 6 elements $B = [2, 3, 4, 5, 6, 7]$ have sum $27$, average $27 / 6 = \mathbf{4.5}$.
      - Both averages match $\implies$ return **`true`**.
- **Affine Mean-Centering & Zero-Sum Invariant:**
  - **The Zero-Sum Linear Transformation:**
    - To eliminate floating-point division and variable subset sizes, multiply each element by $n$ and subtract total sum $s$:
      $$
      nums'[i] = n \cdot nums[i] - s
      $$
    - For any subset $A$ of size $k$:
      $$
      \sum_{x \in A} nums'[x] = \sum_{x \in A} (n \cdot x - s) = n \sum_{x \in A} x - k \cdot s = n \cdot k \left( \frac{\sum_{x \in A} x}{k} - \frac{s}{n} \right)
      $$
    - Thus:
      $$
      \sum_{x \in A} nums'[x] = 0 \iff \text{average}(A) = \mu
      $$
    - The problem transforms completely into finding a **non-empty proper subset of $nums'$ that sums to 0**!
  - **Meet-in-the-Middle Partition ($N \le 30$):**
    - Directly exploring all $2^{30} \approx 10^9$ subsets causes Time Limit Exceeded.
    - Instead, divide $nums'$ into two halves of size $m = \lfloor n / 2 \rfloor \le 15$ and $n - m \le 15$:
      1. **Left Half ($nums'[:m]$):**
         - Enumerate all $2^m - 1 \le 32767$ non-empty subsets.
         - If any subset sum $t == 0$, return `true` immediately.
         - Store all non-zero subset sums in hash set $vis$.
      2. **Right Half ($nums'[m:]$):**
         - Enumerate all $2^{n - m} - 1 \le 32767$ non-empty subsets.
         - If any subset sum $t == 0$, return `true` immediately.
         - If $-t \in vis$, and we have not selected the *full* right half combined with the *full* left half (which would represent the entire array, not a proper split), return `true`!
- **Step-by-Step Worked Execution Trace on $nums = [1, 2, 3, 4, 5, 6, 7, 8]$:**
  - Parameters: $n = 8$, sum $s = 36$.
  - Compute centered array $nums'[i] = 8 \cdot nums[i] - 36$:
    - $nums'[0] = 8(1) - 36 = \mathbf{-28}$
    - $nums'[1] = 8(2) - 36 = \mathbf{-20}$
    - $nums'[2] = 8(3) - 36 = \mathbf{-12}$
    - $nums'[3] = 8(4) - 36 = \mathbf{-4}$
    - $nums'[4] = 8(5) - 36 = \mathbf{+4}$
    - $nums'[5] = 8(6) - 36 = \mathbf{+12}$
    - $nums'[6] = 8(7) - 36 = \mathbf{+20}$
    - $nums'[7] = 8(8) - 36 = \mathbf{+28}$
  - Half division ($m = 8 / 2 = 4$):
    - Left Half: $[-28, -20, -12, -4]$
    - Right Half: $[+4, +12, +20, +28]$
  - **Phase 1: Generate Left Half Subsets ($2^4 - 1 = 15$ subsets):**
    - Singletons: $-28, -20, -12, -4$.
    - Pairs: $(-28-20=-48), (-28-12=-40), \dots, (-12-4=-16)$.
    - Triples: $-60, -52, \dots$
    - Full left: $-64$.
    - Insert all into set $vis$:
      $$
      vis = \{ -4, -12, -16, -20, -24, -28, -32, -36, -40, -44, -48, -52, -56, -60, -64 \}
      $$
    - No single subset in Left Half sums to 0 (all are negative).
  - **Phase 2: Generate Right Half Subsets ($2^4 - 1 = 15$ subsets):**
    - Right Half: $[+4, +12, +20, +28]$.
    - **Subset 1: $\{ +4 \}$:**
      - Sum $t = +4$.
      - Test complement: $-t = -4$.
      - Check membership:
        $$
        -4 \in vis \implies \mathbf{Match\ Found!}
        $$
      - In left half, subset $\{-4\}$ produced sum $-4$.
      - In right half, subset $\{+4\}$ produced sum $+4$.
      - Combined subset: $\{-4, +4\}$.
      - Total sum: $-4 + 4 = \mathbf{0}$.
    - Map back to original numbers:
      - Left element $-4 \implies nums[3] = 4$.
      - Right element $+4 \implies nums[4] = 5$.
      - Sub-array $A = [4, 5]$ has average $(4 + 5) / 2 = 4.5 == \mu$!
    - Return:
      $$
      ans = \mathbf{true}
      $$
- **Two Elements Unequal Trace ($nums = [3, 1]$):**
  - $n = 2, s = 4$.
  - Centered: $nums' = [2(3) - 4, 2(1) - 4] = [+2, -2]$.
  - $m = 1$. Left half: $[+2]$. Right half: $[-2]$.
  - Left half set: $vis = \{ +2 \}$.
  - Right half subset: $\{-2\}$ has sum $t = -2$. Complement $-t = +2 \in vis$.
  - But taking left half $\{+2\}$ and right half $\{-2\}$ uses the **entire array** ($i == (1 \ll 1) - 1$), which leaves the second partition $B$ empty!
  - Blocked by proper subset check $\implies$ returns **`false`**.
- **Single Element Array ($n = 1$):**
  - Cannot split into two non-empty sub-arrays $\implies$ returns **`false`**.

This instance demonstrates affine barycentric coordinate transformation and meet-in-the-middle subset sum bifurcation, mathematically proves why the equal average partition problem is polynomial-time isomorphic to knapsack balance over zero hyperplanes, and derives $O(2^{N/2})$ runtime and $O(2^{N/2})$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Can we split $nums$ into two non-empty arrays $A$ and $B$ with the **same average**?

```text
nums = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

Total sum = 36, n = 8.
Global average = 36 / 8 = 4.5.

Consider sub-array A = [ 4, 5 ]:
  Average = (4 + 5) / 2 = 4.5.
Remaining elements B = [ 1, 2, 3, 6, 7, 8 ]:
  Sum = 27, count = 6 -> Average = 27 / 6 = 4.5.

Result: true
```

### The Invariant of Mean-Centering to Zero-Sum
- Sub-array average equals global average $\mu \iff \sum_{x \in A} (n \cdot x - s) = 0$.
- By transforming $nums'[i] = n \cdot nums[i] - s$, the problem becomes: find a **non-empty proper subset summing to 0**.
- Meet-in-the-middle splits $N \le 30$ into two halves of size $\le 15$, checking $2^{15}$ subsets in each half.

---

## 2. Conceptual Foundation & Invariants

### 1. Affine Centering Transform:
$$
nums'[i] = n \cdot nums[i] - \sum_{j = 0}^{n - 1} nums[j]
$$
$$
\sum_{i = 0}^{n - 1} nums'[i] \equiv 0
$$

### 2. Zero-Sum Subset Equivalence:
$$
\text{Valid Split} \iff \exists \emptyset \subsetneq A \subsetneq nums': \quad \sum_{x \in A} x = 0
$$

> **Barycentric Hyperplane Invariant.** The average equivalence condition $\frac{1}{|A|}\sum_{i \in A} v_i = \frac{1}{|B|}\sum_{j \in B} v_j$ defines an affine hyperplane passing through the center of mass $\mu$. The transformation $v \mapsto n v - s$ projects this hyperplane to a central linear subspace with integer coefficients.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3, 4, 5, 6, 7, 8]$:

---

### Step 1: Center Elements
- $nums' = [-28, -20, -12, -4, +4, +12, +20, +28]$.

---

### Step 2: Left Half ($m = 4$)
- Subsets of $[-28, -20, -12, -4]$ recorded in $vis$.
- $vis$ contains $-4$.

---

### Step 3: Right Half
- Subset $\{+4\}$ has sum $t = +4$.
- Check $-t = -4 \in vis \implies$ Match!
- Formed subset $\{-4, +4\} \implies 0$.

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Half Evaluated | Subset Selected | Transformed Sum $t$ | Complement Looked Up | Exists in $vis$? | Proper Subset Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Left ($m=4$) | $\{-4\}$ | $-4$ | — | Added to $vis$ | — |
| Left ($m=4$) | $\dots$ | $\dots$ | — | Added to $vis$ | — |
| Right ($n-m=4$) | $\{+4\}$ | $+4$ | $-t = -4$ | **Yes (Found!)** | **Yes (Size $2 < 8$)** |
| **Final** | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($n = 1$):** Cannot split into two non-empty arrays $\implies$ returns `false`.
- **Two Elements ($[3, 1]$):** Both subsets must be non-empty; only proper split is two singletons $\implies$ returns `false`.
- **All Elements Equal ($[2, 2, 2]$):** Any split has same average $\implies$ returns `true`.
- **Excluding Full Array Match:** A match combining all elements of both halves is the entire array, which is invalid because partition $B$ cannot be empty.

---

## 6. Traps & Common Anti-Patterns

- **Direct DP on Target Sum with Floating Points:** Floating point averages suffer from precision issues and requires 3D DP $(index, count, sum)$. Affine centering $n \cdot x - s$ uses strictly integers and eliminates count tracking!
- **Full $2^N$ Subset Enumeration:** For $N = 30$, $2^{30} \approx 10^9$ operations TLEs. Meet-in-the-middle cuts this to $2 \times 2^{15} \approx 6.5 \times 10^4$ operations.
- **Off-By-One on Full Array Inclusion:** In the second half, if $i = 2^{n - m} - 1$ (all elements chosen) and $-t = \sum nums'[:m]$, this selects all elements of the original array; ensure $i \ne 2^{n - m} - 1$ when checking against full left half.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Left half generates $2^{N / 2}$ subset sums: $\mathcal{O}(2^{N / 2})$.
  - Right half generates $2^{N / 2}$ subset sums and performs $O(1)$ set lookups: $\mathcal{O}(2^{N / 2})$.
  - Total Time: strictly $\mathcal{O}(2^{N / 2})$ where $N \le 30 \implies \le 2 \times 32768 \approx 6.5 \times 10^4$ operations. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(2^{N / 2}) \le 32768$ space for the hash set $vis$.
