# Guided Example: Binary Search Tree Iterator II

This guide walks through the stateful bidirectional traversal of a Binary Search Tree (BST) supporting forward step (`next`), backward step (`prev`), and their respective boundary verification queries (`hasNext`, `hasPrev`).

- **Input BST Root:** `[7, 3, 15, null, null, 9, 20]`
- **Operation Stream:** `["BSTIterator", "hasNext", "next", "hasPrev", "next", "hasPrev", "prev", "next", "next", "hasNext", "next", "next", "hasNext", "hasPrev", "prev", "prev"]`
- **Output Sequence:** `[null, true, 3, false, 7, true, 3, 7, 9, true, 15, 20, false, true, 15, 9]`

---

## 1. Instance & Teaching Goal

In a Binary Search Tree, an in-order depth-first traversal (visiting left subtree, root node, then right subtree) produces an ascending sorted order of values. Standard iterators only progress strictly forward. Supporting reversible, bidirectional iteration requires maintaining either a materialized history buffer or a dual-stack suspension mechanism.

```
          7
        /   \
       3     15
            /  \
           9    20
```

The underlying sorted in-order sequence across all nodes is:
$$\text{Sorted Sequence} = [3, 7, 9, 15, 20]$$

Our teaching goal is to trace how the iterator maintains an internal cursor position $p$ over the flattened sequence of size $M = 5$, enforcing exact boundary invariants across alternating forward and backward queries.

---

## 2. Conceptual Foundation & Invariants

```
+-------------------------------------------------------------------------+
|                  BIDIRECTIONAL ITERATOR STATE MACHINE                   |
|                                                                         |
|  Initial Cursor:  p = -1 (sentinel position before first node)          |
|  Sequence Array:  A = [ 3,   7,   9,  15,  20 ]                         |
|  Indices:               0    1    2    3    4                           |
|                                                                         |
|  hasNext() : Returns (p < M - 1)                                        |
|  next()    : Increments p <- p + 1; Emits A[p]                          |
|  hasPrev() : Returns (p > 0)                                            |
|  prev()    : Decrements p <- p - 1; Emits A[p]                          |
+-------------------------------------------------------------------------+
```

| Component | Mathematical Definition | Role in Iteration |
|---|---|---|
| In-order Buffer $A$ | $\text{InOrder}(\text{Tree})$ where $A[k] < A[k+1]$ | Static or lazily populated linear projection of BST keys |
| Active Index $p$ | Integer cursor with domain $\{-1, 0, \dots, M-1\}$ | Pointer to the most recently delivered element |
| Forward Feasibility | $p < M - 1$ | Predicate indicating whether a successor element exists |
| Backward Feasibility | $p > 0$ | Predicate indicating whether a predecessor element exists |

> **Pointer Invariant.** At any quiet state between operations, if $p \in [0, M-1]$, the current element returned by the last movement operation is strictly $A[p]$. The forward boundary check $\text{hasNext}()$ holds if and only if $p + 1 < M$. The backward boundary check $\text{hasPrev}()$ holds if and only if $p - 1 \ge 0$.

```mermaid
flowchart LR
    accTitle: Bidirectional Iterator Transition Diagram
    accDescr: State transitions between iterator positions driven by next and prev operations.
    S["Sentinel Position (p = -1)"] -->|"next() -> 3"| N0["p = 0 : Val 3"]
    N0 -->|"next() -> 7"| N1["p = 1 : Val 7"]
    N1 -->|"prev() -> 3"| N0
    N1 -->|"next() -> 9"| N2["p = 2 : Val 9"]
    N2 -->|"next() -> 15"| N3["p = 3 : Val 15"]
    N3 -->|"next() -> 20"| N4["p = 4 : Val 20"]
    N4 -->|"prev() -> 15"| N3
    N3 -->|"prev() -> 9"| N2
```

---

## 3. Step-by-Step Worked Execution

### Initialization Phase

- The BST with root $7$ is traversed via in-order depth-first traversal:
  1. Descend left to node $3$: leaf node, visit $3$.
  2. Visit root node $7$.
  3. Descend right to node $15$: left child is $9$, visit $9$; visit $15$; right child is $20$, visit $20$.
- Flattened sorted array: $A = [3, 7, 9, 15, 20]$ with length $M = 5$.
- Pointer initialized to sentinel: $p = -1$.

---

### Step 1: Forward Movement to First Node

- Operation: $\text{hasNext}()$
  - Evaluation: $p = -1 < 5 - 1 = 4 \implies \text{true}$.
- Operation: $\text{next}()$
  - Advance pointer: $p \leftarrow -1 + 1 = 0$.
  - Emitted value: $A[0] = 3$.

| State Field | Value Before | Value After |
|---|---|---|
| Pointer $p$ | $-1$ | $0$ |
| Target Element | Sentinel | $A[0] = 3$ |
| Boundary Check $\text{hasPrev}()$ | N/A | $0 > 0 \implies \text{false}$ |

---

### Step 2: Boundary Check & Progression to Second Node

- Operation: $\text{hasPrev}()$
  - Evaluation: $p = 0 > 0 \implies \text{false}$. (Cannot move left from the first element).
- Operation: $\text{next}()$
  - Advance pointer: $p \leftarrow 0 + 1 = 1$.
  - Emitted value: $A[1] = 7$.

| State Field | Value Before | Value After |
|---|---|---|
| Pointer $p$ | $0$ | $1$ |
| Target Element | $3$ | $A[1] = 7$ |
| Boundary Check $\text{hasPrev}()$ | $\text{false}$ | $1 > 0 \implies \text{true}$ |

---

### Step 3: Reversible Backward Step

- Operation: $\text{hasPrev}()$
  - Evaluation: $p = 1 > 0 \implies \text{true}$.
- Operation: $\text{prev}()$
  - Retract pointer: $p \leftarrow 1 - 1 = 0$.
  - Emitted value: $A[0] = 3$.

The cursor safely returns to index $0$, reproducing value $3$ without mutating or re-traversing the tree structure.

---

### Step 4: Advancing Forward Across the Spectrum

- Sequence of operations:
  - $\text{next}() \implies p = 1, \text{emit } A[1] = 7$.
  - $\text{next}() \implies p = 2, \text{emit } A[2] = 9$.
  - $\text{hasNext}() \implies p = 2 < 4 \implies \text{true}$.
  - $\text{next}() \implies p = 3, \text{emit } A[3] = 15$.
  - $\text{next}() \implies p = 4, \text{emit } A[4] = 20$.
  - $\text{hasNext}() \implies p = 4 < 4 \implies \text{false}$ (Reached upper bound).

---

### Step 5: Retracting from Upper Boundary

- Operation: $\text{hasPrev}() \implies p = 4 > 0 \implies \text{true}$.
- Operation: $\text{prev}() \implies p \leftarrow 3, \text{emit } A[3] = 15$.
- Operation: $\text{prev}() \implies p \leftarrow 2, \text{emit } A[2] = 9$.

Both operations step leftwards along the materialized sequence, yielding $15$ and $9$ respectively.

---

## 4. Complete Execution Trace

| Call Index | Operation | Prior $p$ | Condition Evaluated | Updated $p$ | Return Value |
|---|---|---|---|---|---|
| 0 | `BSTIterator(root)` | Unset | In-order DFS produces $A=[3, 7, 9, 15, 20]$ | $-1$ | `null` |
| 1 | `hasNext()` | $-1$ | $-1 < 4$ | $-1$ | `true` |
| 2 | `next()` | $-1$ | $p \leftarrow p + 1$ | $0$ | $3$ |
| 3 | `hasPrev()` | $0$ | $0 > 0$ | $0$ | `false` |
| 4 | `next()` | $0$ | $p \leftarrow p + 1$ | $1$ | $7$ |
| 5 | `hasPrev()` | $1$ | $1 > 0$ | $1$ | `true` |
| 6 | `prev()` | $1$ | $p \leftarrow p - 1$ | $0$ | $3$ |
| 7 | `next()` | $0$ | $p \leftarrow p + 1$ | $1$ | $7$ |
| 8 | `next()` | $1$ | $p \leftarrow p + 1$ | $2$ | $9$ |
| 9 | `hasNext()` | $2$ | $2 < 4$ | $2$ | `true` |
| 10 | `next()` | $2$ | $p \leftarrow p + 1$ | $3$ | $15$ |
| 11 | `next()` | $3$ | $p \leftarrow p + 1$ | $4$ | $20$ |
| 12 | `hasNext()` | $4$ | $4 < 4$ | $4$ | `false` |
| 13 | `hasPrev()` | $4$ | $4 > 0$ | $4$ | `true` |
| 14 | `prev()` | $4$ | $p \leftarrow p - 1$ | $3$ | $15$ |
| 15 | `prev()` | $3$ | $p \leftarrow p - 1$ | $2$ | $9$ |

---

## 5. Algorithmic Correctness

**Soundness.** The BST property dictates that for any node $u$, all nodes in its left subtree satisfy $\text{val} < u.\text{val}$ and all nodes in its right subtree satisfy $\text{val} > u.\text{val}$. An in-order depth-first traversal recursively visits the left subtree, then the node itself, then the right subtree. By structural induction on BST height, the generated array $A$ represents a strictly monotonic increasing sequence containing all $N$ node values. Since $A[p]$ is accessed only within legal bounds $0 \le p \le M-1$, each emitted value is mathematically identical to the corresponding in-order tree rank.

**Completeness.** Forward movement $\text{next}()$ increments the index $p$ monotonically, and backward movement $\text{prev}()$ decrements $p$ symmetrically. Because index steps are unit increments ($\Delta p = \pm 1$), no element in the sequence can be skipped. The boundary guard $p < M - 1$ prevents moving past the maximum key, while $p > 0$ prevents moving before the minimum key, guaranteeing that all valid operations terminate with valid results.

---

## 6. Traps This Instance Exposes

- **Zero-Index Boundary Condition:** Calling `hasPrev()` when $p = 0$ must evaluate to `false`. While index $0$ contains a valid value ($A[0] = 3$), no *previous* element exists. Checking $p \ge 0$ instead of $p > 0$ causes out-of-bounds attempts on subsequent `prev()` calls.
- **Sentinel Offset Pitfall:** At initialization, the cursor rests at $p = -1$. A query to `hasNext()` must test $p < M - 1$ rather than $p \ge 0$, ensuring the iterator correctly signals readiness to deliver the first item.
- **Lazy Stack Traversal Complexity:** If implementing lazy traversal without full pre-flattening, moving backward requires caching previously popped stack nodes. A purely naive generator cannot rewind without maintaining a history deque.

---

## 7. Complexity Derivation

- **Initialization Time:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the binary search tree, corresponding to a single full in-order traversal.
- **Query Time per Operation:** $\mathcal{O}(1)$ worst-case for each call to `hasNext()`, `next()`, `hasPrev()`, and `prev()`, as each performs a single comparison or array index offset.
- **Auxiliary Space:** $\mathcal{O}(N)$ space to store the flattened in-order sequence array $A$, alongside $\mathcal{O}(H)$ call stack space during initial recursive traversal where $H$ is the tree height.