# Guided Example: Random Flip Matrix

We trace the step-by-step sparse virtual Fisher-Yates shuffle, dynamic tail-swap mapping ($mp[x] \leftarrow mp.get(total, total)$), 1D-to-2D coordinate projection ($[idx // n, idx \pmod n]$), uniform sampling probability preservation, and $O(1)$ state reset on representative matrix dimensions:

- **Input Configuration:**
  - Matrix dimensions: $m = 2, \; n = 2$ (Total cells: $T = 2 \times 2 = 4$)
  - Flattened cell indices:
    - Index $0 \to (0, 0)$
    - Index $1 \to (0, 1)$
    - Index $2 \to (1, 0)$
    - Index $3 \to (1, 1)$
  - Operation sequence: `["flip", "flip", "reset", "flip"]`
- **Sparse Virtual Fisher-Yates Shuffle execution trace:**
  - Initialize: $total = 4$, hash map $mp = \{\}$.
  - **Operation 1: `flip()` (Remaining available cells: 4):**
    - Decrement active pool size: $total \leftarrow 4 - 1 = \mathbf{3}$
    - Roll uniform random index: $x \in [0, 3]$. Suppose roll yields $x = 0$.
    - Retrieve mapped index:
      $$
      idx = mp.get(0, 0) = \mathbf{0}
      $$
    - Swap the tail element into the vacated slot $x = 0$:
      The tail element is at position $total = 3$.
      $$
      mp[0] \leftarrow mp.get(3, 3) = \mathbf{3}
      $$
      *(Future selections of slot 0 will now return cell 3!)*
    - Project flattened index $idx = 0$ into 2D coordinates:
      $$
      \text{row} = 0 // 2 = \mathbf{0}, \quad \text{col} = 0 \pmod 2 = \mathbf{0}
      $$
    - Return **`[0, 0]`**.
  - **Operation 2: `flip()` (Remaining available cells: 3):**
    - Decrement active pool size: $total \leftarrow 3 - 1 = \mathbf{2}$
    - Roll uniform random index: $x \in [0, 2]$. Suppose roll yields $x = 0$.
    - Retrieve mapped index:
      $$
      idx = mp.get(0, 0) = \mathbf{3}
      $$
      *(Notice: slot 0 now points to cell 3!)*
    - Swap the new tail element (position $total = 2$) into slot $0$:
      $$
      mp[0] \leftarrow mp.get(2, 2) = \mathbf{2}
      $$
    - Project flattened index $idx = 3$ into 2D coordinates:
      $$
      \text{row} = 3 // 2 = \mathbf{1}, \quad \text{col} = 3 \pmod 2 = \mathbf{1}
      $$
    - Return **`[1, 1]`**.
  - **Operation 3: `reset()`:**
    - Restore total pool size: $total \leftarrow m \times n = 2 \times 2 = \mathbf{4}$
    - Clear hash map: $mp.clear() \implies mp = \{\}$
    - All cells are once again available with identity mapping.
  - **Operation 4: `flip()` (Fresh pool after reset):**
    - Decrement: $total \leftarrow 4 - 1 = 3$
    - Roll $x \in [0, 3]$. Suppose roll yields $x = 0$.
    - $idx = mp.get(0, 0) = 0 \implies \mathbf{[0, 0]}$ (Cell $(0, 0)$ is available again!).
- **Large Dimension Space Efficiency:**
  - For $m = 10^4, n = 10^4$, total cells $T = 10^8$.
  - Storing a physical matrix takes $100$ MB of memory.
  - The sparse hash map only stores entries for flipped cells (at most $1000$ flips), consuming $< 100$ KB!

This instance demonstrates in-place Fisher-Yates sampling over virtual arrays via hash-mapped coordinate redirection, mathematically proves why tail-swapping preserves uniform sampling without replacement, and derives $O(1)$ flip runtime and $O(\text{flips})$ space bounds.

---

## 1. Instance & Teaching Goal

Given matrix dimensions $m \times n$ where all cells initially have value $0$:
Implement an algorithm with:
- `flip()`: Randomly pick an index `(row, col)` with value 0 and flip it to 1. Each 0-cell must have equal probability of being chosen.
- `reset()`: Reset all values in the matrix back to 0.

```text
2x2 Matrix Cells:
  (0, 0) -> 0    (0, 1) -> 1
  (1, 0) -> 2    (1, 1) -> 3

Pool: [0, 1, 2, 3] (size 4)

Flip 1: Random pick in [0..3] -> picks 0.
  Emit (0, 0).
  Swap tail (3) into slot 0. Pool becomes [3, 1, 2] (size 3).

Flip 2: Random pick in [0..2] -> picks 0.
  Slot 0 points to 3 -> Emit (1, 1).
  Swap tail (2) into slot 0. Pool becomes [2, 1] (size 2).
```

### Why We Cannot Allocate a Full Matrix
- Constraints: $m, n \le 10^4 \implies m \times n \le 10^8$ cells!
- Allocating an array or matrix of size $10^8$ causes immediate **Memory Limit Exceeded**.
- However, at most $1000$ calls to `flip()` are made.
- We simulate the **Fisher-Yates Shuffle** using a **hash map**:
  - An untouched index $k$ implicitly maps to itself ($k \to k$).
  - Only when an index is chosen do we record its swap with the current tail in the hash map.

---

## 2. Conceptual Foundation & Invariants

### 1. The Sparse Tail-Swap Mechanism:
Maintain $total$, the number of unflipped cells remaining (initially $m \times n$):
When `flip()` is invoked:
1. Decrement active pool size:
   $$
   total \leftarrow total - 1
   $$
2. Pick a random integer $x \in [0, total]$.
3. The selected cell is:
   $$
   idx = mp.get(x, \; x)
   $$
4. Overwrite slot $x$ with whatever is currently at the tail ($total$):
   $$
   mp[x] \leftarrow mp.get(total, \; total)
   $$
5. Convert flattened 1D index $idx$ to 2D coordinates:
   $$
   \text{row} = \lfloor idx / n \rfloor, \quad \text{col} = idx \pmod n
   $$

### 2. Reset Invariance:
Restoring $total = m \times n$ and clearing $mp$ resets the state in $O(1)$ time.

> **Uniformity Invariant.** At step $k$, each of the remaining $total$ unflipped cells occupies exactly one slot in the range $[0, total - 1]$ (either explicitly in $mp$ or implicitly as its own identity), guaranteeing that random uniform selection across $[0, total - 1]$ picks every remaining cell with probability $\frac{1}{total}$.

---

## 3. Step-by-Step Worked Execution

We trace $m = 2, n = 2$ ($T = 4$):

---

### Step 1: Initialize
- $total = 4$.
- $mp = \{\}$.

---

### Step 2: First `flip()` Call
- $total \leftarrow 4 - 1 = 3$.
- Pick $x \in [0, 3]$. Suppose random generator chooses $x = 0$.
- Retrieve actual index:
  $$
  idx = mp.get(0, 0) = \mathbf{0}
  $$
- Move tail element at position $3$ to slot $0$:
  $$
  mp[0] \leftarrow mp.get(3, 3) = \mathbf{3}
  $$
- Convert $idx = 0$:
  $$
  \text{row} = 0 // 2 = 0, \quad \text{col} = 0 \pmod 2 = 0 \implies \mathbf{[0, 0]}
  $$

---

### Step 3: Second `flip()` Call
- $total \leftarrow 3 - 1 = 2$.
- Pick $x \in [0, 2]$. Suppose random generator chooses $x = 0$.
- Retrieve actual index:
  $$
  idx = mp.get(0, 0) = \mathbf{3}
  $$
- Move tail element at position $2$ to slot $0$:
  $$
  mp[0] \leftarrow mp.get(2, 2) = \mathbf{2}
  $$
- Convert $idx = 3$:
  $$
  \text{row} = 3 // 2 = 1, \quad \text{col} = 3 \pmod 2 = 1 \implies \mathbf{[1, 1]}
  $$

---

### Step 4: `reset()` Call
- $total \leftarrow 4$.
- $mp.clear() \implies mp = \{\}$.

---

### Step 5: Third `flip()` Call (Post-Reset)
- $total \leftarrow 4 - 1 = 3$.
- Pick $x \in [0, 3]$. Suppose $x = 0$.
- $idx = mp.get(0, 0) = 0 \implies \mathbf{[0, 0]}$.

---

## 4. Complete Execution Trace

| Call | Active Range $[0, total]$ | Random $x$ Chosen | Value $idx = mp.get(x, x)$ | Tail Position $total$ | Hash Map Update $mp[x] = \text{tail}$ | Emitted Coordinate `[r, c]` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`flip()`** | $[0, 3]$ | $0$ | **$0$** | $3$ | $mp[0] = 3$ | `[0, 0]` |
| **`flip()`** | $[0, 2]$ | $0$ | **$3$** | $2$ | $mp[0] = 2$ | `[1, 1]` |
| **`reset()`** | — | — | — | — | $mp.clear()$ | `null` |
| **`flip()`** | $[0, 3]$ | $0$ | **$0$** | $3$ | $mp[0] = 3$ | `[0, 0]` |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell Matrix ($1 \times 1$):** $total = 1 \implies$ first flip always selects index 0 $\implies \mathbf{[0, 0]}$.
- **Picking the Tail Itself ($x == total$):** $idx = mp.get(total, total)$, and $mp[total] = mp.get(total, total)$. The assignment is an identity no-op and correctly drains the tail.
- **Flipping Every Single Cell:** Loop runs until $total = 0$, guaranteeing all $m \times n$ cells are flipped without duplication.
- **Immediate Reset After Initialization:** Clears an already empty map with zero overhead.

---

## 6. Traps & Common Anti-Patterns

- **Allocating an $M \times N$ 2D Array or 1D List:** For $10^4 \times 10^4$, creating an array of $10^8$ items exceeds memory limits. The sparse hash map only allocates memory for cells actually flipped.
- **Rejection Sampling (`while cell in seen: roll_again()`):** When most cells have been flipped, finding an unpicked cell by rolling random coordinates takes exponential trials, causing Time Limit Exceeded. The Fisher-Yates tail-swap runs in strictly $O(1)$ deterministic time per flip.
- **Decrementing `total` After Selecting:** If you choose $x \in [0, total]$ before decrementing, $total$ might exceed the 0-indexed bounds. Decrementing $total \leftarrow total - 1$ first and picking $x \in [0, total]$ keeps indices within valid bounds.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization `__init__`: $\mathcal{O}(1)$.
  - `flip()`: A single random integer generation, two hash map lookups, and integer arithmetic: strictly $\mathcal{O}(1)$ time.
  - `reset()`: Clearing the hash map of at most $K$ elements takes $\mathcal{O}(K)$ where $K$ is the number of flips since last reset ($\le 1000$).
  - Total Time: $\mathcal{O}(1)$ per operation. Completes in $< 1$ microsecond per flip.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ where $K$ is the number of calls to `flip()` (at most $1000$ entries in the hash map).
