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

### Subtree Sizes and the Factorial Count

Reading the trace one line at a time hides why the total work is $\Theta(N \cdot N!)$ rather than merely $N!$. The table below lists every node of the decision tree for $\text{nums} = [1, 2, 3]$ together with the number of leaves hanging beneath it. A prefix of length $d$ fixes $d$ of the $N$ positions, so it has exactly $(N - d)!$ completions, and the emitted leaves must sum back to $N!$.

| Prefix (path so far) | Unchosen elements | Completions below this node $(N - \lvert \text{prefix} \rvert)!$ | Leaves emitted from this subtree |
|:---|:---|:---:|:---|
| `[]` | $\{1, 2, 3\}$ | $3! = 6$ | `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]` |
| `[1]` | $\{2, 3\}$ | $2! = 2$ | `[1,2,3]`, `[1,3,2]` |
| `[1, 2]` | $\{3\}$ | $1! = 1$ | `[1,2,3]` |
| `[1, 3]` | $\{2\}$ | $1! = 1$ | `[1,3,2]` |
| `[2]` | $\{1, 3\}$ | $2! = 2$ | `[2,1,3]`, `[2,3,1]` |
| `[2, 1]` | $\{3\}$ | $1! = 1$ | `[2,1,3]` |
| `[2, 3]` | $\{1\}$ | $1! = 1$ | `[2,3,1]` |
| `[3]` | $\{1, 2\}$ | $2! = 2$ | `[3,1,2]`, `[3,2,1]` |
| `[3, 1]` | $\{2\}$ | $1! = 1$ | `[3,1,2]` |
| `[3, 2]` | $\{1\}$ | $1! = 1$ | `[3,2,1]` |

Summing the leaf column *below* the root gives $2 + 1 + 1 + 2 + 1 + 1 + 2 + 1 + 1 = 12$, and adding the root's own $6$ gives $18 = 6 \times 3$: each of the six permutations appears once at each of the three prefixes that extend it. The tree itself is only a constant factor larger than its leaves, since depth $d$ holds $\frac{N!}{(N-d)!}$ nodes and $\sum_{d=0}^{N} \frac{N!}{(N-d)!} \approx e \cdot N!$. The extra factor of $N$ in the running time therefore comes from recording rather than from searching: every one of the $N!$ completed paths must be copied out at cost $O(N)$.

---

## 5. Algorithmic Correctness

**Soundness.** Because each level checks `not used[j]` before picking $\text{nums}[j]$, no element is picked more than once per path. When depth reaches $N$, `path` contains all $N$ distinct elements, forming a valid permutation.

**Completeness.** At each step, the loop visits every unchosen element. Because the DFS visits all branches of the $N!$ factorial tree, all unique permutations are generated.

---

## 6. Traps This Instance Exposes

- **Failing to Clone Path:** Storing `ans.append(path)` appends a reference to the mutable list `path`. When subsequent backtrack calls pop elements, all previously stored answers become corrupted. Cloning via `path[:]` is mandatory.
- **Incomplete State Rollback:** Both the path list (`path.pop()`) and the boolean mask (`used[j] = False`) must be reverted on backtracking. Forgetting either causes subsequent branches to miss elements.
- **In-Place Swap Alternative:** Permutations can also be generated by swapping elements in-place (`swap(nums[i], nums[j])`). While it saves the `used` array, maintaining an explicit boolean array is often easier to reason about and keeps lexicographical ordering intact.

### Boundary Cases and Value Versus Index Identity

| Scenario | Input | Required output | What this instance proves |
|:---|:---|:---|:---|
| Shortest legal input | `[1]` | `[[1]]` | The answer is a single leaf at depth $1$; $1! = 1$ and no branching decision is ever genuinely open. |
| Two distinct values | `[0, 1]` | `[[0, 1], [1, 0]]` | The value $0$ is an ordinary element, not an empty slot or a sentinel, and it occupies each position in turn. |
| Negative values | `[-1, 2]` | `[[-1, 2], [2, -1]]` | Ordering is by index, not by value: the array is never sorted, and a negative element behaves exactly like a positive one. |
| Extreme legal values | `[-10, 10]` | `[[-10, 10], [10, -10]]` | The smallest and largest permitted values permute like any other pair, so no magnitude comparison enters the search. |
| Maximum-length distinct input | `[1, 2, 3, 4]` | the $4! = 24$ orderings listed in the package cases | The output size grows factorially while the constraint ceiling, $N = 6$, still corresponds to only $720$ recorded paths. |

The distinction these rows turn on is that `used` tracks *positions* in `nums`, never *values*. Duplicate values never arise under this problem's contract, but if they did, an index-based mask would happily emit the same ordering twice — the precise defect that the duplicate-pruning rule of the next problem repairs.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot N!)$. There are $N!$ leaf nodes (permutations). Constructing and copying each permutation of length $N$ takes $O(N)$ time. Total operations across all tree nodes is $\sum_{k=1}^N P(N, k) \cdot O(1) \approx O(N \cdot N!)$.
- **Auxiliary Space Complexity:** $O(N)$ for the recursion stack and `used` boolean array.

### Alternative Formulations

| Approach | Mechanism | Time | Auxiliary space | Emission order for $\text{nums} = [1, 2, 3]$ |
|:---|:---|:---|:---|:---|
| Used-mask DFS (this lesson) | Explicit growing path plus a boolean mask over indices | $O(N \cdot N!)$ | $O(N)$ | `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]` |
| In-place swap DFS | At depth $d$, swap position $d$ with every index $i \ge d$, recurse, then swap back | $O(N \cdot N!)$ | $O(N)$ recursion only, no mask | Same six permutations, but the last two swap places: `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,2,1]`, `[3,1,2]` |
| Lexicographic successor iteration | Repeatedly transform a sorted array into its next permutation in lexicographic order | $O(N \cdot N!)$ | $O(N)$ | The lexicographic sequence `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]` |
| Insertion build | Insert each new element into every gap of every partial ordering already built | $O(N \cdot N!)$ total | $O(N \cdot N!)$ for the intermediate orderings | Order depends on where the new element is inserted, so it is not the DFS order |

Because the contract accepts any order, all four are correct; they differ only in the ordering they expose and in whether the intermediate state is mutable positions or immutable partial lists.
