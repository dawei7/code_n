# Guided Example: Permutations

We trace the step-by-step recursive depth-first backtracking search on a representative distinct array instance:

- **Input:** $\text{nums} = [1, 2, 3]$
- **Required output:** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

This instance demonstrates generating all $N!$ distinct orderings, state vector tracking with a boolean `used` mask, in-order path appending, and state restoration during backtracking unwind.

---

## 1. Instance & Teaching Goal

Given an array $\text{nums}$ of $N = 3$ distinct integers, we must return all possible permutations.

For $\text{nums} = [1, 2, 3]$:
- Position 0 has 3 choices ($1, 2, 3$).
- Position 1 has 2 remaining choices.
- Position 2 has 1 remaining choice.
- Total valid orderings:
  $$
  N! = 3 \times 2 \times 1 = 6
  $$

The objective is to systematically explore all 6 paths of the permutation tree using depth-first search (DFS). By maintaining a boolean `used` table, each sub-branch selects only from currently unchosen elements, guaranteeing that each emitted array contains all original elements in a unique sequence.

---

## 2. Conceptual Foundation & Invariants

### Decision Tree Structure
```text
Root:                               []
                /                    |                    \
Pos 0:        [1]                   [2]                   [3]
             /   \                 /   \                 /   \
Pos 1:    [1,2]  [1,3]          [2,1]  [2,3]          [3,1]  [3,2]
            |      |              |      |              |      |
Pos 2:   [1,2,3] [1,3,2]       [2,1,3] [2,3,1]       [3,1,2] [3,2,1]
```

### Backtracking Transitions
We maintain:
- `path`: Current list of selected numbers ($0 \le |\text{path}| \le N$).
- `used`: Boolean array of length $N$ indicating whether $\text{nums}[j]$ is currently inside `path`.

Recursive Function `dfs()`:
1. **Base Case:** If $|\text{path}| == N$, append a clone of `path` to the output list and return.
2. **Expansion:** For each index $j \in [0, N - 1]$:
   - If $\text{used}[j]$ is False:
     - Mark $\text{used}[j] \leftarrow \text{True}$.
     - Append $\text{nums}[j]$ to `path`.
     - Recurse: `dfs()`.
     - Rollback: Pop $\text{nums}[j]$ from `path`, and reset $\text{used}[j] \leftarrow \text{False}$.

> **Invariant.** At recursion depth $d$, `path` contains exactly $d$ distinct elements from $\text{nums}$, and $\text{used}$ accurately reflects their indices.

---

## 3. Step-by-Step Worked Execution

We trace the DFS traversal for $\text{nums} = [1, 2, 3]$:

### Subtree 1: Anchor on $1$ ($\text{path} = [1]$)
- Index 0 marked used: $\text{used} = [\text{T}, \text{F}, \text{F}]$.
- **Branch 1A (Choose $2$):**
  - $\text{path} = [1, 2]$, $\text{used} = [\text{T}, \text{T}, \text{F}]$.
  - Only index 2 ($3$) is available.
  - $\text{path} = [1, 2, 3]$. Length is 3!
  - **Record Permutation 1: `[1, 2, 3]`**.
  - Rollback $3$, rollback $2$.
- **Branch 1B (Choose $3$):**
  - $\text{path} = [1, 3]$, $\text{used} = [\text{T}, \text{F}, \text{T}]$.
  - Only index 1 ($2$) is available.
  - $\text{path} = [1, 3, 2]$. Length is 3!
  - **Record Permutation 2: `[1, 3, 2]`**.
  - Rollback $2$, rollback $3$, rollback $1$.

---

### Subtree 2: Anchor on $2$ ($\text{path} = [2]$)
- Index 1 marked used: $\text{used} = [\text{F}, \text{T}, \text{F}]$.
- **Branch 2A (Choose $1$):**
  - $\text{path} = [2, 1]$, $\text{used} = [\text{T}, \text{T}, \text{F}]$.
  - Only index 2 ($3$) is available.
  - $\text{path} = [2, 1, 3]$.
  - **Record Permutation 3: `[2, 1, 3]`**.
  - Rollback $3$, rollback $1$.
- **Branch 2B (Choose $3$):**
  - $\text{path} = [2, 3]$, $\text{used} = [\text{F}, \text{T}, \text{T}]$.
  - Only index 0 ($1$) is available.
  - $\text{path} = [2, 3, 1]$.
  - **Record Permutation 4: `[2, 3, 1]`**.
  - Rollback $1$, rollback $3$, rollback $2$.

---

### Subtree 3: Anchor on $3$ ($\text{path} = [3]$)
- Index 2 marked used: $\text{used} = [\text{F}, \text{F}, \text{T}]$.
- **Branch 3A (Choose $1$):**
  - $\text{path} = [3, 1]$, $\text{used} = [\text{T}, \text{F}, \text{T}]$.
  - Only index 1 ($2$) is available.
  - $\text{path} = [3, 1, 2]$.
  - **Record Permutation 5: `[3, 1, 2]`**.
  - Rollback $2$, rollback $1$.
- **Branch 3B (Choose $2$):**
  - $\text{path} = [3, 2]$, $\text{used} = [\text{F}, \text{T}, \text{T}]$.
  - Only index 0 ($1$) is available.
  - $\text{path} = [3, 2, 1]$.
  - **Record Permutation 6: `[3, 2, 1]`**.
  - Rollback $1$, rollback $2$, rollback $3$.

DFS completes. Output contains all 6 permutations.

---

## 4. Complete Execution Trace

| DFS Call Sequence | Active `path` | Element Added | Active `used` Flags $[0, 1, 2]$ | Target Depth Met? | Output Emitted |
|:---|:---|:---:|:---:|:---:|:---|
| Root | `[]` | - | `[F, F, F]` | No | - |
| Depth 1 | `[1]` | 1 | `[T, F, F]` | No | - |
| Depth 2 | `[1, 2]` | 2 | `[T, T, F]` | No | - |
| Depth 3 | `[1, 2, 3]` | 3 | `[T, T, T]` | **Yes ($d=3$)** | **`[1, 2, 3]`** |
| Depth 2 (Alternate) | `[1, 3]` | 3 | `[T, F, T]` | No | - |
| Depth 3 | `[1, 3, 2]` | 2 | `[T, T, T]` | **Yes ($d=3$)** | **`[1, 3, 2]`** |
| Depth 1 (Anchor 2) | `[2]` | 2 | `[F, T, F]` | No | - |
| Depth 2 | `[2, 1]` | 1 | `[T, T, F]` | No | - |
| Depth 3 | `[2, 1, 3]` | 3 | `[T, T, T]` | **Yes ($d=3$)** | **`[2, 1, 3]`** |
| Depth 2 (Alternate) | `[2, 3]` | 3 | `[F, T, T]` | No | - |
| Depth 3 | `[2, 3, 1]` | 1 | `[T, T, T]` | **Yes ($d=3$)** | **`[2, 3, 1]`** |
| Depth 1 (Anchor 3) | `[3]` | 3 | `[F, F, T]` | No | - |
| Depth 2 | `[3, 1]` | 1 | `[T, F, T]` | No | - |
| Depth 3 | `[3, 1, 2]` | 2 | `[T, T, T]` | **Yes ($d=3$)** | **`[3, 1, 2]`** |
| Depth 2 (Alternate) | `[3, 2]` | 2 | `[F, T, T]` | No | - |
| Depth 3 | `[3, 2, 1]` | 1 | `[T, T, T]` | **Yes ($d=3$)** | **`[3, 2, 1]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because each level checks `not used[j]` before picking $\text{nums}[j]$, no element is picked more than once per path. When depth reaches $N$, `path` contains all $N$ distinct elements, forming a valid permutation.

**Completeness.** At each step, the loop visits every unchosen element. Because the DFS visits all branches of the $N!$ factorial tree, all unique permutations are generated.

---

## 6. Traps This Instance Exposes

- **Failing to Clone Path:** Storing `ans.append(path)` appends a reference to the mutable list `path`. When subsequent backtrack calls pop elements, all previously stored answers become corrupted. Cloning via `path[:]` is mandatory.
- **Incomplete State Rollback:** Both the path list (`path.pop()`) and the boolean mask (`used[j] = False`) must be reverted on backtracking. Forgetting either causes subsequent branches to miss elements.
- **In-Place Swap Alternative:** Permutations can also be generated by swapping elements in-place (`swap(nums[i], nums[j])`). While it saves the `used` array, maintaining an explicit boolean array is often easier to reason about and keeps lexicographical ordering intact.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot N!)$. There are $N!$ leaf nodes (permutations). Constructing and copying each permutation of length $N$ takes $O(N)$ time. Total operations across all tree nodes is $\sum_{k=1}^N P(N, k) \cdot O(1) \approx O(N \cdot N!)$.
- **Auxiliary Space Complexity:** $O(N)$ for the recursion stack and `used` boolean array.
