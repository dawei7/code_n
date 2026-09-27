# Guided Example: Longest Consecutive Sequence

We trace the step-by-step sequence-head identification and hash set streak expansion on a representative unsorted integer array:

- **Input:** $\text{nums} = [100, 4, 200, 1, 3, 2]$
- **Required output:** $4$ (Consecutive sequence: $[1, 2, 3, 4]$)
- **Base Instances:** $\text{nums} = [] \implies 0, \quad \text{nums} = [0, 0] \implies 1$

This instance demonstrates why sorting ($O(N \log N)$) is suboptimal, establishes the sequence-head filtering condition ($x - 1 \notin \text{set}$), proves why each number is visited at most twice across the entire execution to guarantee strictly $O(N)$ linear time, and analyzes hash collisions and duplicate handling.

---

## 1. Instance & Teaching Goal

Given an unsorted array of integers:
$$
\text{nums} = [100, 4, 200, 1, 3, 2]
$$
return the length of the longest consecutive elements sequence. The algorithm must run in $O(N)$ time.

In this instance, the elements form three disjoint contiguous chains:
1. $[100]$ (length $1$)
2. $[200]$ (length $1$)
3. $[1, 2, 3, 4]$ (length $4$)
The longest sequence has length $4$.

Sorting the array achieves $O(N \log N)$ time, violating the linear time constraint.
A naive search that counts upwards from *every* element takes $O(N^2)$ time (e.g. counting $1 \to 2 \to 3 \to 4$, then $2 \to 3 \to 4$, then $3 \to 4$).
The optimal method converts `nums` into a hash set `num_set` and **only** initiates counting if $x$ is the true **head** of a streak (i.e. $x - 1 \notin \text{num\_set}$). Interior elements are skipped in $O(1)$ time, guaranteeing each element is traversed at most once.

---

## 2. Conceptual Foundation & Invariants

### Sequence Head Identification Protocol
1. **Deduplication & Lookup Set:**
   $$
   \text{num\_set} = \text{set}(\text{nums})
   $$
2. **Streak Initiation Condition:**
   An integer $x$ is the start of a consecutive streak if and only if its predecessor does not exist in the set:
   $$
   x - 1 \notin \text{num\_set}
   $$
   - If $x - 1 \in \text{num\_set}$, $x$ is an interior or terminal element of an already existing streak. **Skip $x$ immediately in $O(1)$ time.**
   - If $x - 1 \notin \text{num\_set}$, $x$ is the unique starting anchor.
3. **Streak Expansion:**
   From anchor $x$, count upward:
   - Let $\text{curr} = x, \, \text{streak} = 1$.
   - While $\text{curr} + 1 \in \text{num\_set}$:
     $$
     \text{curr} \leftarrow \text{curr} + 1, \quad \text{streak} \leftarrow \text{streak} + 1
     $$
   - $\text{max\_streak} \leftarrow \max(\text{max\_streak}, \, \text{streak})$.

> **Invariant.** The inner expansion loop executes if and only if $x$ is the minimum element of a maximal connected component in the integer line. Every integer is expanded at most once across all iterations.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [100, 4, 200, 1, 3, 2]$:
Initialize `num_set = {100, 4, 200, 1, 3, 2}`.
`max_streak = 0`.

---

### Step 1: Inspect $x = 100$
- Predecessor check: $100 - 1 = 99 \notin \text{num\_set}$.
- **$100$ is a streak head!**
- Count upward:
  - $100 + 1 = 101 \notin \text{num\_set}$.
  - Streak length $= 1$.
- Update: $\text{max\_streak} = \max(0, 1) = 1$.

---

### Step 2: Inspect $x = 4$
- Predecessor check: $4 - 1 = 3 \in \text{num\_set}$.
- $4$ is an interior element!
- **Prune immediately** in $O(1)$ time without counting.

---

### Step 3: Inspect $x = 200$
- Predecessor check: $200 - 1 = 199 \notin \text{num\_set}$.
- **$200$ is a streak head!**
- Count upward:
  - $200 + 1 = 201 \notin \text{num\_set}$.
  - Streak length $= 1$.
- Update: $\text{max\_streak} = \max(1, 1) = 1$.

---

### Step 4: Inspect $x = 1$
- Predecessor check: $1 - 1 = 0 \notin \text{num\_set}$.
- **$1$ is a streak head!**
- Count upward:
  - $1 + 1 = 2 \in \text{num\_set} \implies \text{streak} = 2$.
  - $2 + 1 = 3 \in \text{num\_set} \implies \text{streak} = 3$.
  - $3 + 1 = 4 \in \text{num\_set} \implies \text{streak} = 4$.
  - $4 + 1 = 5 \notin \text{num\_set} \implies$ halt expansion.
- Component discovered: $[1, 2, 3, 4]$ of length $4$.
- Update: $\text{max\_streak} = \max(1, 4) = \mathbf{4}$.

---

### Step 5: Inspect $x = 3$
- Predecessor check: $3 - 1 = 2 \in \text{num\_set}$.
- Interior element $\implies$ **Prune in $O(1)$**.

---

### Step 6: Inspect $x = 2$
- Predecessor check: $2 - 1 = 1 \in \text{num\_set}$.
- Interior element $\implies$ **Prune in $O(1)$**.

Traversal complete. Maximum streak length: $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
Numbers:      [ 100,   4,   200,   1,   3,   2 ]
num - 1?       99:No  3:Yes 199:No 0:No 2:Yes 1:Yes
Role:          HEAD   SKIP   HEAD  HEAD SKIP SKIP
Chain Built:   [100]    -    [200] [1,2,3,4] -  -
Length:          1      -      1      4      -  -  => MAX = 4
```

| Evaluated Number $x$ | Predecessor $x - 1$ | In `num_set`? | Role Identified | Expansion Sequence | Discovered Length | Updated $\text{max\_streak}$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 100 | 99 | No | **Sequence Head** | $100$ | 1 | 1 |
| 4 | 3 | **Yes** | Interior Node | Skipped ($O(1)$) | - | 1 |
| 200 | 199 | No | **Sequence Head** | $200$ | 1 | 1 |
| **1** | **0** | **No** | **Sequence Head** | **$1 \to 2 \to 3 \to 4$** | **4** | **4 (Global Max)** |
| 3 | 2 | **Yes** | Interior Node | Skipped ($O(1)$) | - | 4 |
| 2 | 1 | **Yes** | Interior Node | Skipped ($O(1)$) | - | 4 |

---

## 5. Algorithmic Correctness

**Soundness.** Consecutive integer sequences are equivalence classes (connected components) on the integer line. Each component has a unique minimum element $x_{\min}$ characterized by $x_{\min} - 1 \notin \text{num\_set}$. By starting upward counting strictly at $x_{\min}$, every element of the component is counted exactly once, and no spurious sub-chains are generated.

**Completeness.** Every consecutive sequence that exists in the input has an initial element. Because all elements are tested against the predecessor condition, every sequence head will be identified and fully expanded to its true terminal boundary.

---

## 6. Traps This Instance Exposes

- **Expanding Non-Head Elements ($O(N^2)$ Trap):** Omitting the `if x - 1 not in num_set:` guard causes the inner loop to run for every element (e.g. $[1, 2, \dots, N]$ takes $N + (N-1) + \dots + 1 = O(N^2)$ operations). The guard is what guarantees $O(N)$ runtime.
- **Duplicate Elements:** If the input contains repeated numbers (e.g. `[1, 2, 0, 1]`), constructing `set(nums)` handles duplicates naturally so they do not artificially increment lengths.
- **Empty Array:** If `nums = []`, `num_set` is empty and the loop never executes, correctly returning `0`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ average time. Building `num_set` takes $O(N)$. The outer loop iterates $N$ times. Each interior element is rejected in $O(1)$ time. The inner while loop visits each element in a consecutive chain exactly once across the entire run. Total set lookups are bounded by $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ to store the hash set `num_set` containing up to $N$ unique integers.
