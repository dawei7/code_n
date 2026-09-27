# Guided Example: Queue Reconstruction by Height

We trace the step-by-step greedy reconstruction, dual-key sorting invariant ($(-h, k)$ descending height, ascending relative rank), sequential list insertion at exact index $k$ (`ans.insert(p[1], p)`), and shorter-element invisibility preservation on representative height-rank queues:

- **Input:** $people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]$
- **Required output:** `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]`
  - Step 1 (Sort order $(-h, k)$):
    - $[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]$
  - Step 2 (Insertions into `ans`):
    - Insert $[7, 0]$ at index $0 \implies [[7, 0]]$
    - Insert $[7, 1]$ at index $1 \implies [[7, 0], [7, 1]]$
    - Insert $[6, 1]$ at index $1 \implies [[7, 0], [6, 1], [7, 1]]$
    - Insert $[5, 0]$ at index $0 \implies [[5, 0], [7, 0], [6, 1], [7, 1]]$
    - Insert $[5, 2]$ at index $2 \implies [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]$
    - Insert $[4, 4]$ at index $4 \implies [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]$
  - Result: `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]`
- **Identical Heights:** $people = [[7, 1], [7, 0]] \implies$ sorted to $[7, 0], [7, 1] \implies [[7, 0], [7, 1]]$
- **Pre-Sorted Monotonic:** $[[1, 0], [2, 0]] \implies$ sorted to $[2, 0], [1, 0] \implies [[1, 0], [2, 0]]$

This instance demonstrates greedy invariant decoupling, mathematically proves why placing taller elements first isolates constraint evaluation without interference from subsequent shorter elements, and derives $O(N^2)$ time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of people attributes $people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]$:
Each person is defined by $[h, k]$, where $h$ is height and $k$ is the exact number of people in front who have height $\ge h$.
Reconstruct the original queue:

```text
Input: [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

Sorted by (-h, k):
1. [7, 0]
2. [7, 1]
3. [6, 1]
4. [5, 0]
5. [5, 2]
6. [4, 4]

Key Insight:
  A person of height h only cares about people with height >= h.
  Shorter people (< h) are completely INVISIBLE to them!
  Therefore:
    1. Place taller people first.
    2. Inserting a shorter person later will NEVER disrupt the k-count of taller people!
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Dual-Key Sorting Rule:
Sort all people using the tuple key:
$$
\text{key}(p) = (-p[0], \; p[1])
$$
- **Primary key ($-h$):** Process taller people before shorter people.
- **Secondary key ($k$):** For identical heights, process smaller $k$ first so that earlier positions are occupied before later ones.

### 2. The Direct Insertion Invariant:
Let `ans` be the partial queue. When processing person $p = [h, k]$:
- Every person currently in `ans` has height $\ge h$.
- Therefore, inserting $p$ at index $k$ (`ans.insert(k, p)`):
  - Places exactly $k$ people of height $\ge h$ ahead of $p$.
  - Satisfies $p$'s constraint immediately!
- When subsequent people of height $h' \le h$ are inserted later:
  - If $h' < h$, the new person does not contribute to $p$'s count of people $\ge h$.
  - $p$'s count remains valid forever.

> **Invariant.** After inserting person $p = [h, k]$, every person currently in `ans` has exactly their required number of people $\ge h$ in front of them, and no future insertion will alter that count.

---

## 3. Step-by-Step Worked Execution

We trace $people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]$:

---

### Step 1: Sort People
Apply key $\lambda x: (-x[0], x[1])$:
$$
\text{Sorted: } [[7, 0], \; [7, 1], \; [6, 1], \; [5, 0], \; [5, 2], \; [4, 4]]
$$
Initialize `ans = []`.

---

### Step 2: Insert $[7, 0]$
- $k = 0 \implies ans.\text{insert}(0, [7, 0])$:
  $$
  ans = [[7, 0]]
  $$

---

### Step 3: Insert $[7, 1]$
- $k = 1 \implies ans.\text{insert}(1, [7, 1])$:
  $$
  ans = [[7, 0], \; [7, 1]]
  $$
- In front of $[7, 1]$ is $[7, 0]$ (height $\ge 7$, count = 1). Valid!

---

### Step 4: Insert $[6, 1]$
- $k = 1 \implies ans.\text{insert}(1, [6, 1])$:
  $$
  ans = [[7, 0], \; \mathbf{[6, 1]}, \; [7, 1]]
  $$
- In front of $[6, 1]$ is $[7, 0]$ (height $\ge 6$, count = 1).
- In front of $[7, 1]$ is $[7, 0]$ (count of $\ge 7$ is still 1, since $6 < 7$). Valid!

---

### Step 5: Insert $[5, 0]$
- $k = 0 \implies ans.\text{insert}(0, [5, 0])$:
  $$
  ans = [\mathbf{[5, 0]}, \; [7, 0], \; [6, 1], \; [7, 1]]
  $$
- In front of $[5, 0]$ is 0 people.
- Taller people $[7, 0], [6, 1], [7, 1]$ ignore the presence of $[5, 0]$ because $5 < 6, 7$. Valid!

---

### Step 6: Insert $[5, 2]$
- $k = 2 \implies ans.\text{insert}(2, [5, 2])$:
  $$
  ans = [[5, 0], \; [7, 0], \; \mathbf{[5, 2]}, \; [6, 1], \; [7, 1]]
  $$
- In front of $[5, 2]$ are $[5, 0]$ and $[7, 0]$ (both $\ge 5$, count = 2). Valid!

---

### Step 7: Insert $[4, 4]$
- $k = 4 \implies ans.\text{insert}(4, [4, 4])$:
  $$
  ans = [[5, 0], \; [7, 0], \; [5, 2], \; [6, 1], \; \mathbf{[4, 4]}, \; [7, 1]]
  $$
- In front of $[4, 4]$ are $[5, 0], [7, 0], [5, 2], [6, 1]$ (all $\ge 4$, count = 4). Valid!

---

### Step 8: Termination
All $N = 6$ people inserted. Return:
$$
[[5, 0], \; [7, 0], \; [5, 2], \; [6, 1], \; [4, 4], \; [7, 1]]
$$

---

## 4. Complete Execution Trace

```text
Sorted People: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

Insert [7, 0] at idx 0 -> [[7, 0]]
Insert [7, 1] at idx 1 -> [[7, 0], [7, 1]]
Insert [6, 1] at idx 1 -> [[7, 0], [6, 1], [7, 1]]
Insert [5, 0] at idx 0 -> [[5, 0], [7, 0], [6, 1], [7, 1]]
Insert [5, 2] at idx 2 -> [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
Insert [4, 4] at idx 4 -> [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

Final Queue: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
```

| Step | Person $p = [h, k]$ | Target Insertion Index $k$ | Pre-existing Elements with Height $\ge h$ | Queue State After Insertion |
|:---:|:---:|:---:|:---:|:---|
| 1 | `[7, 0]` | 0 | 0 | `[[7, 0]]` |
| 2 | `[7, 1]` | 1 | 1 (`[7, 0]`) | `[[7, 0], [7, 1]]` |
| 3 | `[6, 1]` | 1 | 1 (`[7, 0]`) | `[[7, 0], [6, 1], [7, 1]]` |
| 4 | `[5, 0]` | 0 | 0 | `[[5, 0], [7, 0], [6, 1], [7, 1]]` |
| 5 | `[5, 2]` | 2 | 2 (`[5, 0], [7, 0]`) | `[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]` |
| **6** | **`[4, 4]`** | **4** | **4 (`[5, 0], [7, 0], [5, 2], [6, 1]`)** | **`[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Suppose person $p = [h, k]$ is inserted at position $k$ among previously inserted elements. Every previously placed element has height $\ge h$, so exactly $k$ elements $\ge h$ precede $p$. Any element placed afterwards has height $h' \le h$. If $h' < h$, its presence ahead of $p$ does not increment $p$'s count. If $h' == h$, the secondary sort order guarantees $k' > k$, meaning the identical-height person is placed strictly after $p$, also preserving $p$'s count. Thus all conditions are simultaneously satisfied.

**Completeness.** By sorting people, every person is inserted into the queue exactly once. Because the problem guarantees a valid configuration exists, the list insertion at index $k \le \text{len}(ans)$ is always within bounds.

---

## 6. Traps This Instance Exposes

- **Wrong Secondary Tie-Breaking:** If people of the same height are sorted with descending $k$ (e.g. $[7, 1]$ before $[7, 0]$), inserting $[7, 0]$ at index 0 pushes $[7, 1]$ to index 1, which works here, but in general corrupts relative positioning. Smaller $k$ must be processed first so the base elements exist before later ranks reference them.
- **Short-First Insertion Fallacy:** Sorting shortest people first requires tracking empty slots via Fenwick Trees or Segment Trees, which is significantly more complex. Placing tallest first allows direct native array insertion.
- **List Insertion Overhead:** In Python, `ans.insert(k, p)` runs in $O(N)$ time per insertion, yielding $O(N^2)$ total runtime, which easily passes for $N \le 2000$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N = \text{len}(people)$.
  - Sorting $N$ elements takes $O(N \log N)$ time.
  - Inserting $N$ elements into a dynamic array takes $\sum_{i=1}^N i = O(N^2)$ time.
  - Total time is $O(N^2)$, executing in $< 10$ ms for $N = 2000$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the output array `ans`.
