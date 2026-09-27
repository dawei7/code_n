# Guided Example: Max Chunks To Make Sorted

We trace the step-by-step permutation subset invariant over the range $[0, n - 1]$, running prefix maximum tracking ($mx = \max(mx, arr[i])$), boundary partition equality condition ($i == mx$), greedy maximum chunk segmentation, and chunk count accumulation on representative permutations:

- **Input:** $arr = [1, 0, 2, 3, 4]$
- **Required output:** `4`
  - Permutation chunk sorting criteria:
    - $arr$ is a permutation of the integers in the range $[0, n - 1]$.
    - Split $arr$ into contiguous chunks such that sorting each chunk individually and concatenating them produces the sorted sequence $[0, 1, 2, \dots, n - 1]$.
    - Objective: Find the **maximum possible number of chunks**.
    - For $[1, 0, 2, 3, 4]$ (length $n = 5$):
      - Chunk 1: $[1, 0] \implies \text{sorted: } [0, 1]$.
      - Chunk 2: $[2] \implies \text{sorted: } [2]$.
      - Chunk 3: $[3] \implies \text{sorted: } [3]$.
      - Chunk 4: $[4] \implies \text{sorted: } [4]$.
      - Concatenation: $[0, 1, 2, 3, 4]$ (perfectly sorted).
      - Maximum chunks: **4**.
- **Permutation Prefix Identity & $mx == i$ Invariant:**
  - **The Canonical Range Property:**
    - In the final sorted array, the elements occupying the first $i + 1$ positions (indices $0 \dots i$) must be the exact numbers $\{0, 1, \dots, i\}$.
    - A partition cut is valid at index $i$ if and only if the prefix $arr[0 \dots i]$ contains **all integers from $0$ to $i$**.
  - **The Maximum-Index Equivalence Theorem:**
    - Because $arr$ is a permutation of non-negative distinct integers $[0, n - 1]$:
      - The prefix $arr[0 \dots i]$ contains $i + 1$ distinct integers.
      - If the maximum value in this prefix equals $i$:
        $$
        \max_{0 \le j \le i} arr[j] = i
        $$
      - Then all $i + 1$ distinct non-negative integers in the prefix must be $\le i$.
      - By the Pigeonhole Principle, the set of elements in $arr[0 \dots i]$ must be **identically equal to $\{0, 1, \dots, i\}$**!
  - **Greedy Cut Invariant:**
    - Whenever the running prefix maximum $mx$ equals the current index $i$:
      $$
      mx == i \implies \text{Valid chunk boundary!}
      $$
    - We immediately increment the chunk counter:
      $$
      ans \leftarrow ans + 1
      $$
    - Because each cut is made at the earliest possible index, this greedy strategy provably maximizes the total number of chunks!
- **Step-by-Step Worked Execution Trace on $arr = [1, 0, 2, 3, 4]$:**
  - Initialize running maximum: $mx = 0$.
  - Initialize chunk counter: $ans = 0$.
  - **Index $i = 0$ ($v = 1$):**
    - Update running maximum:
      $$
      mx \leftarrow \max(0, 1) = \mathbf{1}
      $$
    - Check boundary equality:
      $$
      i == mx \iff 0 == 1 \quad \mathbf{(False)}
      $$
      *(Element 1 requires element 0 to appear before it can form a valid sorted block)*.
    - No cut.
  - **Index $i = 1$ ($v = 0$):**
    - Update running maximum:
      $$
      mx \leftarrow \max(1, 0) = \mathbf{1}
      $$
    - Check boundary equality:
      $$
      i == mx \iff 1 == 1 \quad \mathbf{(Cut\ Point\ 1!)}
      $$
    - Prefix contains $\{0, 1\}$, spanning indices $0 \dots 1$.
    - Chunk 1 completed: $[1, 0]$.
    - Increment:
      $$
      ans \leftarrow 0 + 1 = \mathbf{1}
      $$
  - **Index $i = 2$ ($v = 2$):**
    - Update running maximum:
      $$
      mx \leftarrow \max(1, 2) = \mathbf{2}
      $$
    - Check boundary equality:
      $$
      i == mx \iff 2 == 2 \quad \mathbf{(Cut\ Point\ 2!)}
      $$
    - Chunk 2 completed: $[2]$.
    - Increment:
      $$
      ans \leftarrow 1 + 1 = \mathbf{2}
      $$
  - **Index $i = 3$ ($v = 3$):**
    - Update running maximum:
      $$
      mx \leftarrow \max(2, 3) = \mathbf{3}
      $$
    - Check boundary equality:
      $$
      i == mx \iff 3 == 3 \quad \mathbf{(Cut\ Point\ 3!)}
      $$
    - Chunk 3 completed: $[3]$.
    - Increment:
      $$
      ans \leftarrow 2 + 1 = \mathbf{3}
      $$
  - **Index $i = 4$ ($v = 4$):**
    - Update running maximum:
      $$
      mx \leftarrow \max(3, 4) = \mathbf{4}
      $$
    - Check boundary equality:
      $$
      i == mx \iff 4 == 4 \quad \mathbf{(Cut\ Point\ 4!)}
      $$
    - Chunk 4 completed: $[4]$.
    - Increment:
      $$
      ans \leftarrow 3 + 1 = \mathbf{4}
      $$
  - **Final Output:**
    $$
    ans = \mathbf{4}
    $$
- **Descending Permutation Trace ($arr = [4, 3, 2, 1, 0]$):**
  - Index 0: $v = 4 \implies mx = 4$.
  - For all $i \in [0, 3]$, $i < mx = 4$.
  - Only at the final index $i = 4$ does $i == mx$ ($4 == 4$).
  - Entire array is a single monolithic chunk $\implies ans = \mathbf{1}$.
- **Already Sorted Permutation ($arr = [0, 1, 2, 3, 4]$):**
  - At every index $i$, $arr[i] = i \implies mx == i$.
  - Every single element is its own chunk $\implies ans = \mathbf{5}$.

This instance demonstrates permutation ideal-cone projection and linear prefix extremum tracking, mathematically proves why $i = \max_{j \le i} \pi(j)$ is necessary and sufficient for permutation prefix invariance, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $arr$ which is a permutation of $[0, n - 1]$:
Find the **maximum number of chunks** to sort independently such that their concatenation is sorted.

```text
arr = [ 1, 0, 2, 3, 4 ]

i = 0 (v = 1): max = 1 != 0 (cannot cut)
i = 1 (v = 0): max = 1 == 1 -> CUT! (Chunk 1: [1, 0])
i = 2 (v = 2): max = 2 == 2 -> CUT! (Chunk 2: [2])
i = 3 (v = 3): max = 3 == 3 -> CUT! (Chunk 3: [3])
i = 4 (v = 4): max = 4 == 4 -> CUT! (Chunk 4: [4])

Total chunks = 4
Result: 4
```

### The Invariant of the Index Equality $mx == i$
- In a permutation of $[0, n-1]$, the prefix $[0 \dots i]$ contains all numbers from $0$ to $i$ if and only if the **maximum value in the prefix equals $i$**.
- Every time $mx == i$, we have a self-contained chunk that can be cut immediately.

---

## 2. Conceptual Foundation & Invariants

### 1. Running Maximum Update:
$$
mx \leftarrow \max(mx, \; arr[i])
$$

### 2. Permutation Prefix Invariant:
$$
\text{cut condition} \iff \max_{0 \le j \le i} arr[j] == i
$$
$$
ans = \sum_{i=0}^{n-1} [mx == i]
$$

> **Permutation Fixed Ideal Invariant.** In the symmetric group $S_n$, an initial segment $[0, i]$ is an invariant set under permutation $\pi$ if and only if $\pi([0, i]) = [0, i]$, which for order ideals in the natural numbers is equivalent to the scalar identity $\max_{j \le i} \pi(j) = i$.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [1, 0, 2, 3, 4]$:

---

### Step 1: Elements 1 and 0
- $i = 0, v = 1 \implies mx = 1 \ne 0$.
- $i = 1, v = 0 \implies mx = 1 == 1 \implies$ Cut 1.

---

### Step 2: Elements 2, 3, 4
- $i = 2, v = 2 \implies mx = 2 == 2 \implies$ Cut 2.
- $i = 3, v = 3 \implies mx = 3 == 3 \implies$ Cut 3.
- $i = 4, v = 4 \implies mx = 4 == 4 \implies$ Cut 4.

---

### Step 3: Output
- Total cuts: **`4`**.

---

## 4. Complete Execution Trace

| Index $i$ | Element $v = arr[i]$ | Running Maximum $mx$ | Condition $mx == i$? | Action Taken | Total Chunks $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $1$ | No ($1 \ne 0$) | Continue | $0$ |
| $1$ | $0$ | $1$ | Yes ($1 == 1$) | Cut Chunk `[1, 0]` | **$1$** |
| $2$ | $2$ | $2$ | Yes ($2 == 2$) | Cut Chunk `[2]` | **$2$** |
| $3$ | $3$ | $3$ | Yes ($3 == 3$) | Cut Chunk `[3]` | **$3$** |
| **$4$** | **$4$** | **$4$** | **Yes ($4 == 4$)** | **Cut Chunk `[4]`** | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Descending ($[4, 3, 2, 1, 0]$):** $mx$ jumps to 4 at $i = 0$; only equals $i$ at $i = 4 \implies ans = 1$.
- **Strictly Ascending ($[0, 1, 2, 3, 4]$):** $mx == i$ at every index $\implies ans = n$.
- **Length 1 ($[0]$):** $0 == 0 \implies ans = 1$.
- **Arbitrary Shuffled Permutation:** Distinct values in $[0, n-1]$ guarantee $mx \ge i$ always holds.

---

## 6. Traps & Common Anti-Patterns

- **Applying This Formula to Arrays with Duplicates / Arbitrary Ranges:** The $mx == i$ identity relies strictly on $arr$ being a permutation of $[0, n - 1]$. For arbitrary numbers or duplicates, use the monotonic stack or prefix max vs suffix min approach from Part II (Problem 0768).
- **Summing Elements instead of Checking Maximum:** While checking $\sum_{j=0}^i arr[j] == \frac{i(i+1)}{2}$ works, integer sum calculations risk overflow and require more arithmetic operations than a simple `max(mx, v) == i`.
- **Modifying the Array:** No array mutations or sorting are needed; a single read-only pass suffices.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass of $N$ elements tracking running maximum: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar accumulators $mx, ans$).
