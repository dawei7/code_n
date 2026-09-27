# Guided Example: Range Addition

We trace the step-by-step difference array marking ($d[l] \mathrel{+}= c$, $d[r + 1] \mathrel{-}= c$), $O(1)$ range interval boundary updates, and single-pass cumulative prefix reconstruction (`accumulate(d)`) on representative batch modification instances:

- **Input:** $\text{length} = 5, \quad \text{updates} = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]$
- **Required output:** `[-2, 0, 3, 5, 3]`
  - Initial difference array: $d = [0, 0, 0, 0, 0]$
  - Update 1: $[1, 3, 2] \implies d[1] \mathrel{+}= 2, \; d[4] \mathrel{-}= 2 \implies d = [0, 2, 0, 0, -2]$
  - Update 2: $[2, 4, 3] \implies d[2] \mathrel{+}= 3, \; r + 1 = 5 \ge 5 \text{ (no-op)} \implies d = [0, 2, 3, 0, -2]$
  - Update 3: $[0, 2, -2] \implies d[0] \mathrel{-}= 2, \; d[3] \mathrel{+}= 2 \implies d = [-2, 2, 3, 2, -2]$
  - Prefix sum accumulation:
    - Index 0: $-2$
    - Index 1: $-2 + 2 = 0$
    - Index 2: $0 + 3 = 3$
    - Index 3: $3 + 2 = 5$
    - Index 4: $5 + (-2) = 3$
  - Final reconstructed array: `[-2, 0, 3, 5, 3]`
- **Full Array Increment:** $\text{updates} = [[0, 4, 5]] \implies d = [5, 0, 0, 0, 0] \implies [5, 5, 5, 5, 5]$
- **Zero Updates:** $\text{updates} = [] \implies [0, 0, 0, 0, 0]$

This instance demonstrates the difference array / prefix sum duality for offline range mutations, mathematically proves why recording discrete derivatives reduces range updates from $O(K \cdot N)$ to strictly $O(K + N)$ linear time, and analyzes memory bounds.

---

## 1. Instance & Teaching Goal

Given an integer $\text{length} = 5$ (initially all zeros: $[0, 0, 0, 0, 0]$) and a sequence of 3 range update operations:
$$
\text{updates} = \big[ [1, 3, 2], \; [2, 4, 3], \; [0, 2, -2] \big]
$$
where each update $[l, r, c]$ adds value $c$ to every index from $l$ to $r$ inclusive.
Return the final modified array after applying all operations:

```text
Initial Array: [  0,  0,  0,  0,  0 ]

Update 1: [1, 3, 2]   -> add 2 to indices 1..3:
          [  0, +2, +2, +2,  0 ]

Update 2: [2, 4, 3]   -> add 3 to indices 2..4:
          [  0, +2, +5, +5, +3 ]

Update 3: [0, 2, -2]  -> add -2 to indices 0..2:
          [ -2,  0, +3, +5, +3 ]

Final Output: [-2, 0, 3, 5, 3]
```

### The Difference Array Duality
- Naively iterating from $l$ to $r$ for each of the $K$ updates takes $O(K \cdot N)$ time. For $N, K \le 100,000$, this results in $10^{10}$ operations, causing Time Limit Exceeded.
- **The Difference Array Principle:**
  Define $d[i] = A[i] - A[i-1]$ (with $A[-1] = 0$).
  Adding $c$ to the entire contiguous subsegment $A[l \dots r]$ changes only **two** boundary values in the difference array:
  1. $d[l] \leftarrow d[l] + c$ (The step increase entering index $l$)
  2. $d[r + 1] \leftarrow d[r + 1] - c$ (The step cancellation exiting index $r$)
- Each range update runs in strictly $O(1)$ time.
- A single final prefix sum pass ($A[i] = A[i-1] + d[i]$) recovers all elements in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Difference Array Structure:
Initialize $d = [0] \times \text{length}$.

### 2. $O(1)$ Boundary Modification for each $[l, r, c]$:
1. Increment at start index:
   $$
   d[l] \leftarrow d[l] + c
   $$
2. Decrement at end index successor (if within bounds):
   $$
   \text{if } r + 1 < \text{length}: \quad d[r + 1] \leftarrow d[r + 1] - c
   $$

### 3. Prefix Sum Reconstruction:
$$
A[i] = \sum_{p=0}^i d[p] = \text{accumulate}(d)[i]
$$

> **Invariant.** For every position $i$, the prefix sum $\sum_{p=0}^i d[p]$ exactly equals the algebraic sum of all increments $c$ whose intervals $[l, r]$ satisfy $l \le i \le r$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{length} = 5$ with updates $[[1, 3, 2], [2, 4, 3], [0, 2, -2]]$:
Initial difference array: $d = [0, 0, 0, 0, 0]$.

---

### Step 1: Apply Update 1 (`[1, 3, 2]`)
- $l = 1, r = 3, c = 2$.
- Add at start:
  $$
  d[1] \leftarrow d[1] + 2 = 0 + 2 = \mathbf{2}
  $$
- Subtract at right boundary: $r + 1 = 4 < 5$.
  $$
  d[4] \leftarrow d[4] - 2 = 0 - 2 = \mathbf{-2}
  $$
- Array state:
  $$
  d = [0, \; \mathbf{2}, \; 0, \; 0, \; \mathbf{-2}]
  $$

---

### Step 2: Apply Update 2 (`[2, 4, 3]`)
- $l = 2, r = 4, c = 3$.
- Add at start:
  $$
  d[2] \leftarrow d[2] + 3 = 0 + 3 = \mathbf{3}
  $$
- Subtract at boundary: $r + 1 = 5 \not< 5$.
  - The interval extends through the end of the array; no subtraction is performed.
- Array state:
  $$
  d = [0, \; 2, \; \mathbf{3}, \; 0, \; -2]
  $$

---

### Step 3: Apply Update 3 (`[0, 2, -2]`)
- $l = 0, r = 2, c = -2$.
- Add at start:
  $$
  d[0] \leftarrow d[0] + (-2) = 0 - 2 = \mathbf{-2}
  $$
- Subtract at boundary: $r + 1 = 3 < 5$.
  $$
  d[3] \leftarrow d[3] - (-2) = 0 + 2 = \mathbf{2}
  $$
- Final difference array:
  $$
  d = [\mathbf{-2}, \; 2, \; 3, \; \mathbf{2}, \; -2]
  $$

---

### Step 4: Prefix Sum Reconstruction (`accumulate(d)`)
Accumulate running sum $S$ from index 0 to 4:
- $i = 0$: $S = -2 \implies A[0] = \mathbf{-2}$
- $i = 1$: $S = -2 + 2 = 0 \implies A[1] = \mathbf{0}$
- $i = 2$: $S = 0 + 3 = 3 \implies A[2] = \mathbf{3}$
- $i = 3$: $S = 3 + 2 = 5 \implies A[3] = \mathbf{5}$
- $i = 4$: $S = 5 + (-2) = 3 \implies A[4] = \mathbf{3}$

Final output array:
$$
\mathbf{[-2, 0, 3, 5, 3]}
$$

---

## 4. Complete Execution Trace

```text
length = 5, updates = [[1,3,2], [2,4,3], [0,2,-2]]

Boundary Markers:
Init  : d = [ 0,  0,  0,  0,  0]
[1,3,2]: d[1]+=2, d[4]-=2 -> d = [ 0,  2,  0,  0, -2]
[2,4,3]: d[2]+=3          -> d = [ 0,  2,  3,  0, -2]
[0,2,-2]:d[0]-=2, d[3]+=2 -> d = [-2,  2,  3,  2, -2]

Reconstruction (Prefix Sum):
i=0: -2             = -2
i=1: -2 + 2         =  0
i=2:  0 + 3         =  3
i=3:  3 + 2         =  5
i=4:  5 + (-2)      =  3

Final Result: [-2, 0, 3, 5, 3]
```

| Index $i$ | Difference Value $d[i]$ | Incoming Running Sum | Cumulative Sum $A[i]$ | Active Overlapping Updates Contributing |
|:---:|:---:|:---:|:---:|:---|
| 0 | $-2$ | 0 | **$-2$** | Update 3 ($-2$) |
| 1 | $+2$ | $-2$ | **$0$** | Update 1 ($+2$), Update 3 ($-2$) |
| 2 | $+3$ | $0$ | **$3$** | Update 1 ($+2$), Update 2 ($+3$), Update 3 ($-2$) |
| 3 | $+2$ | $3$ | **$5$** | Update 1 ($+2$), Update 2 ($+3$) |
| 4 | $-2$ | $5$ | **$3$** | Update 2 ($+3$) |

---

## 5. Algorithmic Correctness

**Soundness.** Consider a single update $[l, r, c]$. The prefix sum $\sum_{p=0}^i d[p]$ evaluates to:
- $0$ for $i < l$ (neither boundary encountered)
- $c$ for $l \le i \le r$ (only $+c$ encountered)
- $c - c = 0$ for $i > r$ (both $+c$ and $-c$ encountered, cancelling out)
By the superposition principle (linearity of summation), the prefix sum of the combined difference array equals the sum of the individual updates at every position.

**Completeness.** Every update $[l, r, c]$ is processed without loss. The boundary check $r + 1 < length$ correctly guards against out-of-bounds indexing when an update extends through the end of the array, ensuring structural safety.

---

## 6. Traps This Instance Exposes

- **Subtracting at $r$ instead of $r + 1$:** The interval $[l, r]$ is inclusive, meaning index $r$ must still receive the increment $c$. Subtracting at $r$ would prematurely terminate the effect at $r - 1$.
- **Missing Right Boundary Check:** If an update has $r = length - 1$, $r + 1 = length$ is out of bounds. The subtraction must be conditionally skipped (`if r + 1 < length:`).
- **Negative Increments:** Increments $c$ can be negative. Difference arithmetic handles negative numbers cleanly via $+(-c)$ and $-(-c) = +c$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K + N)$, where $K$ is the number of updates and $N$ is `length`.
  - Processing each update takes $O(1)$ time $\implies O(K)$.
  - Computing the prefix sum with `accumulate(d)` takes $O(N)$ time.
  - Overall time is strictly linear $O(K + N)$, compared to $O(K \cdot N)$ for naive simulation.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the difference array `d`.
