# Guided Example: Zigzag Iterator

We trace the step-by-step round-robin vector turn alternation, circular index advancement, exhausted list skip rotation, and full-cycle termination on representative 1D integer vectors:

- **Input:** $v_1 = [1, 2], \quad v_2 = [3, 4, 5, 6]$
- **Required output:** $[1, 3, 2, 4, 5, 6]$ (Alternates between $v_1$ and $v_2$; once $v_1$ is exhausted, streams the remaining suffix of $v_2$)
- **Unequal Length Exhaustion:** $v_1$ runs out of elements after index 1; subsequent queries cleanly skip $v_1$ and draw exclusively from $v_2$
- **Empty Vector Boundary:** $v_1 = [1], \quad v_2 = [] \implies [1]$ ($v_2$ is skipped immediately on its turn)
- **Both Empty Base Case:** $v_1 = [], \quad v_2 = [] \implies \text{hasNext() returns False}$
- **$K$-Vector Generalization:** Extends seamlessly to $k$ streams using round-robin cyclic rotation $(cur + 1) \bmod k$ or a FIFO queue of active vectors

This instance demonstrates stateful streaming iterator design, explains why interleaving vectors requires independent index tracking rather than pre-materializing all elements in memory, details the circular turn normalization inside `hasNext()`, and guarantees $O(1)$ amortized time per `next()` and `hasNext()` call with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given two 1D vectors $v_1 = [1, 2]$ and $v_2 = [3, 4, 5, 6]$:
Implement an iterator that returns elements alternating between $v_1$ and $v_2$:
```text
Stream progression:
Turn 1: v1[0] = 1
Turn 2: v2[0] = 3
Turn 3: v1[1] = 2  (v1 is now exhausted!)
Turn 4: v2[1] = 4
Turn 5: v2[2] = 5
Turn 6: v2[3] = 6  (v2 is now exhausted!)
Result: [1, 3, 2, 4, 5, 6]
```

### Why Pre-Merging is Suboptimal
Merging all elements upfront into a flat list takes $O(N_1 + N_2)$ auxiliary memory and does all the work upfront even if the caller only reads the first few elements.
A true iterator should:
1. Store only pointers/indices into the original vectors ($O(1)$ auxiliary space).
2. Fetch the next alternating element on demand in strictly $O(1)$ time per call.
3. Automatically skip vectors that have already been fully consumed without breaking alternating order.

---

## 2. Conceptual Foundation & Invariants

### Iterator Internal State
The iterator maintains three scalar variables:
- `vectors = [v1, v2]`: References to the input vectors.
- `indexes = [0, 0]`: Next unread element index for each vector (`indexes[0]` for $v_1$, `indexes[1]` for $v_2$).
- `cur = 0`: The vector index whose turn it is to emit the next element ($0$ or $1$).
- `size = 2`: Total number of vectors.

### Operation Protocols

#### `hasNext() -> bool`
Ensures `cur` points to a vector that still has unread elements:
1. Save `start = cur`.
2. While `indexes[cur] == len(vectors[cur])` (current vector is exhausted):
   - Rotate turn: $\text{cur} \leftarrow (\text{cur} + 1) \bmod \text{size}$.
   - If $\text{cur} == \text{start}$: A complete loop over all vectors found no unread elements. Return `False`.
3. Return `True` (`cur` now points to a valid, non-exhausted vector).

#### `next() -> int`
Called only when `hasNext()` is True:
1. Retrieve element: $\text{res} = \text{vectors}[\text{cur}][\text{indexes}[\text{cur}]]$.
2. Advance index: $\text{indexes}[\text{cur}] \leftarrow \text{indexes}[\text{cur}] + 1$.
3. Rotate turn to the next vector: $\text{cur} \leftarrow (\text{cur} + 1) \bmod \text{size}$.
4. Return `res`.

> **Invariant.** Before any `next()` call, `hasNext()` guarantees that `indexes[cur] < len(vectors[cur])`. Every vector maintains its original relative internal order.

---

## 3. Step-by-Step Worked Execution

We trace the iterator on $v_1 = [1, 2]$ and $v_2 = [3, 4, 5, 6]$:
Initial state: $\text{indexes} = [0, 0], \quad \text{cur} = 0$.

---

### Step 1: Emit First Element
- `hasNext()`:
  - At $\text{cur} = 0$: $\text{indexes}[0] = 0 < \text{len}(v_1) = 2$.
  - Returns `True`.
- `next()`:
  - $\text{res} = v_1[0] = \mathbf{1}$.
  - Update: $\text{indexes}[0] \leftarrow 0 + 1 = 1$.
  - Advance turn: $\text{cur} \leftarrow (0 + 1) \bmod 2 = \mathbf{1}$.
  - Emitted: $1$.

---

### Step 2: Emit Second Element
- `hasNext()`:
  - At $\text{cur} = 1$: $\text{indexes}[1] = 0 < \text{len}(v_2) = 4$.
  - Returns `True`.
- `next()`:
  - $\text{res} = v_2[0] = \mathbf{3}$.
  - Update: $\text{indexes}[1] \leftarrow 0 + 1 = 1$.
  - Advance turn: $\text{cur} \leftarrow (1 + 1) \bmod 2 = \mathbf{0}$.
  - Emitted: $3$.

---

### Step 3: Emit Third Element
- `hasNext()`:
  - At $\text{cur} = 0$: $\text{indexes}[0] = 1 < 2$.
  - Returns `True`.
- `next()`:
  - $\text{res} = v_1[1] = \mathbf{2}$.
  - Update: $\text{indexes}[0] \leftarrow 1 + 1 = \mathbf{2}$ ($v_1$ **exhausted!**).
  - Advance turn: $\text{cur} \leftarrow (0 + 1) \bmod 2 = \mathbf{1}$.
  - Emitted: $2$.

---

### Step 4: Emit Fourth Element
- `hasNext()`:
  - At $\text{cur} = 1$: $\text{indexes}[1] = 1 < 4$.
  - Returns `True`.
- `next()`:
  - $\text{res} = v_2[1] = \mathbf{4}$.
  - Update: $\text{indexes}[1] \leftarrow 1 + 1 = 2$.
  - Advance turn: $\text{cur} \leftarrow (1 + 1) \bmod 2 = \mathbf{0}$.
  - Emitted: $4$.

---

### Step 5: Emit Fifth Element (Exhausted Vector Skipped)
- `hasNext()`:
  - At $\text{cur} = 0$: $\text{indexes}[0] = 2 == \text{len}(v_1) = 2$ ($v_1$ is empty!).
  - Rotate turn: $\text{cur} \leftarrow (0 + 1) \bmod 2 = \mathbf{1}$.
  - At $\text{cur} = 1$: $\text{indexes}[1] = 2 < 4$. Not exhausted!
  - Loop terminates with $\text{cur} = 1$. Returns `True`.
- `next()`:
  - $\text{res} = v_2[2] = \mathbf{5}$.
  - Update: $\text{indexes}[1] \leftarrow 2 + 1 = 3$.
  - Advance turn: $\text{cur} \leftarrow (1 + 1) \bmod 2 = \mathbf{0}$.
  - Emitted: $5$.

---

### Step 6: Emit Sixth Element (Exhausted Vector Skipped)
- `hasNext()`:
  - At $\text{cur} = 0$: $\text{indexes}[0] == 2$. Rotates $\text{cur} \leftarrow 1$.
  - At $\text{cur} = 1$: $\text{indexes}[1] = 3 < 4$. Returns `True`.
- `next()`:
  - $\text{res} = v_2[3] = \mathbf{6}$.
  - Update: $\text{indexes}[1] \leftarrow 3 + 1 = \mathbf{4}$ ($v_2$ **exhausted!**).
  - Advance turn: $\text{cur} \leftarrow 0$.
  - Emitted: $6$.

---

### Step 7: Stream Exhaustion
- `hasNext()`:
  - At $\text{cur} = 0$: $\text{indexes}[0] == 2$ (empty). Rotates to $\text{cur} = 1$.
  - At $\text{cur} = 1$: $\text{indexes}[1] == 4$ (empty). Rotates to $\text{cur} = 0$.
  - $\text{cur} == \text{start}$ ($0 == 0$) $\implies$ Full cycle without unread elements.
  - Returns **`False`**.

Iteration complete. Emitted list:
$$
\mathbf{[1, 3, 2, 4, 5, 6]}
$$

---

## 4. Complete Execution Trace

```text
v1 = [1, 2], v2 = [3, 4, 5, 6]

Call 1: hasNext() -> cur=0 -> next() -> v1[0]=1 -> indexes=[1, 0], cur=1
Call 2: hasNext() -> cur=1 -> next() -> v2[0]=3 -> indexes=[1, 1], cur=0
Call 3: hasNext() -> cur=0 -> next() -> v1[1]=2 -> indexes=[2, 1], cur=1  (v1 done)
Call 4: hasNext() -> cur=1 -> next() -> v2[1]=4 -> indexes=[2, 2], cur=0
Call 5: hasNext() -> cur=0 exhausted -> skip to 1 -> next() -> v2[2]=5 -> indexes=[2, 3], cur=0
Call 6: hasNext() -> cur=0 exhausted -> skip to 1 -> next() -> v2[3]=6 -> indexes=[2, 4], cur=0  (v2 done)
Call 7: hasNext() -> all exhausted -> False

Result: [1, 3, 2, 4, 5, 6]
```

| Step | Method Called | `cur` Before Call | Vector Evaluated | Element Emitted | Updated `indexes` | `cur` After Call |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `next()` | 0 | $v_1$ (Index 0) | **1** | `[1, 0]` | 1 |
| 2 | `next()` | 1 | $v_2$ (Index 0) | **3** | `[1, 1]` | 0 |
| 3 | `next()` | 0 | $v_1$ (Index 1) | **2** | `[2, 1]` | 1 |
| 4 | `next()` | 1 | $v_2$ (Index 1) | **4** | `[2, 2]` | 0 |
| 5 | `next()` | 1 (skipped 0) | $v_2$ (Index 2) | **5** | `[2, 3]` | 0 |
| 6 | `next()` | 1 (skipped 0) | $v_2$ (Index 3) | **6** | `[2, 4]` | 0 |
| **7** | `hasNext()` | 0 | All empty | - | `[2, 4]` | **`False`** |

---

## 5. Algorithmic Correctness

**Soundness.** `hasNext()` actively rotates `cur` past exhausted vectors until finding an unread position or cycling back to `start`. This guarantees that `next()` never accesses an out-of-bounds index and always draws from the next valid alternating vector.

**Completeness.** Every element in $v_1$ and $v_2$ is visited exactly once in non-decreasing index order. The cycle condition in `hasNext()` terminates only when every vector has its index equal to its length, ensuring no element is missed.

---

## 6. Traps This Instance Exposes

- **Calling `next()` Without `hasNext()`:** If a caller invokes `next()` when `cur` points to an exhausted vector, it causes an `IndexError`. The official iterator contract expects callers to loop using `while i.hasNext(): v.append(i.next())`.
- **Unequal Vector Lengths:** If $v_1$ has 2 elements and $v_2$ has 100 elements, alternating blindly would fail after 2 steps. The rotation loop in `hasNext()` handles unequal lengths and finishes streaming the remainder of $v_2$.
- **$k$-Vector Scalability:** For $k$ vectors, repeated linear scanning of exhausted vectors in `hasNext()` can take $O(k)$ time. A `collections.deque` storing `(vector, index)` pairs achieves strictly $O(1)$ time for $k$ vectors by removing exhausted vectors from the queue entirely.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `next()`: $O(1)$ constant time.
  - `hasNext()`: $O(1)$ amortized time. For 2 vectors, `hasNext()` checks at most 2 entries. Across the entire iteration, each vector is found exhausted at most once.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory. Only scalar pointers and an index list of size 2 are maintained.
