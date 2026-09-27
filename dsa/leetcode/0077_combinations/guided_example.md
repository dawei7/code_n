# Guided Example: Combinations

We trace the step-by-step recursive backtracking tree with upper-bound pruning on a representative combination instance:

- **Input:** $n = 4, k = 2$
- **Required output:** $[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]$

This instance demonstrates recursive decision-tree exploration, enforcing strictly increasing element order to eliminate permutation duplicates, the upper-bound pruning condition ($i \le n - (k - |\text{path}|) + 1$), and state rollback.

---

## 1. Instance & Teaching Goal

Given two integers $n = 4$ and $k = 2$, return all possible combinations of $k$ numbers chosen from the range $[1, n] = [1, 2, 3, 4]$.

The total number of combinations is given by the binomial coefficient:
$$
\binom{n}{k} = \binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6
$$

A naive search that considers all permutations generates $4 \times 3 = 12$ candidates, producing duplicates like $[1, 2]$ and $[2, 1]$.
By forcing elements within each combination to be strictly increasing ($\text{start} \le \text{num} \le n$), every subset is generated in a unique canonical order. Furthermore, mathematical pruning terminates exploration when the number of remaining candidates is strictly less than the number of vacancies needed.

---

## 2. Conceptual Foundation & Invariants

### Strictly Increasing Backtracking Recurrence
We define a recursive procedure $\text{backtrack}(\text{start}, \text{path})$:
1. **Base Case:**
   If $|\text{path}| == k$:
   - Append a snapshot copy of $\text{path}$ to results.
   - Return.
2. **Loop with Pruning:**
   How many more numbers do we need? $\text{needed} = k - |\text{path}|$.
   To have at least $\text{needed}$ numbers available in the range $[i, n]$, the upper bound for choice $i$ is:
   $$
   i \le n - \text{needed} + 1 = n - (k - |\text{path}|) + 1
   $$
   For each candidate $i$ from $\text{start}$ up to $n - (k - |\text{path}|) + 1$:
   - Append $i$ to $\text{path}$.
   - Recurse: $\text{backtrack}(i + 1, \text{path})$.
   - Backtrack: remove $i$ from $\text{path}$ ($\text{path.pop()}$).

> **Invariant.** At any recursive depth, `path` contains a strictly increasing prefix of integers, ensuring zero redundant permutations and zero duplicate combinations.

---

## 3. Step-by-Step Worked Execution

We trace $n = 4, k = 2$:

### Depth 0: Root State ($\text{path} = []$)
- Vacancies needed: $2 - 0 = 2$.
- Pruned upper bound: $n - 2 + 1 = 4 - 2 + 1 = 3$.
- Candidate initial picks: $i \in [1, 3]$ *(Candidate $4$ is pruned because $[4]$ can never reach length 2)*.

---

### Branch 1: Pick $1$ ($\text{path} = [1]$)
- Recurse with $\text{start} = 2$.
- Vacancies needed: $2 - 1 = 1$.
- Upper bound: $4 - 1 + 1 = 4$. Candidates: $i \in [2, 4]$.
  - **Pick $2$:** $\text{path} = [1, 2]$. Length $= 2$. Emit **$[1, 2]$**. Backtrack $\to [1]$.
  - **Pick $3$:** $\text{path} = [1, 3]$. Length $= 2$. Emit **$[1, 3]$**. Backtrack $\to [1]$.
  - **Pick $4$:** $\text{path} = [1, 4]$. Length $= 2$. Emit **$[1, 4]$**. Backtrack $\to [1]$.
- Backtrack from $1 \to []$.

---

### Branch 2: Pick $2$ ($\text{path} = [2]$)
- Recurse with $\text{start} = 3$.
- Vacancies needed: $1$. Upper bound: $4$. Candidates: $i \in [3, 4]$.
  - **Pick $3$:** $\text{path} = [2, 3]$. Length $= 2$. Emit **$[2, 3]$**. Backtrack $\to [2]$.
  - **Pick $4$:** $\text{path} = [2, 4]$. Length $= 2$. Emit **$[2, 4]$**. Backtrack $\to [2]$.
- Backtrack from $2 \to []$.

---

### Branch 3: Pick $3$ ($\text{path} = [3]$)
- Recurse with $\text{start} = 4$.
- Vacancies needed: $1$. Upper bound: $4$. Candidates: $i \in [4, 4]$.
  - **Pick $4$:** $\text{path} = [3, 4]$. Length $= 2$. Emit **$[3, 4]$**. Backtrack $\to [3]$.
- Backtrack from $3 \to []$.

---

### Branch 4: Pick $4$
- Evaluated bound: $4 > 3$. Pruned without recursive call.

Search complete. Emitted combinations: $[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]$.

---

## 4. Complete Execution Trace

| DFS Step | Action Taken | Candidate $i$ | Resulting Path | Condition Check ($\lvert \text{path} \rvert == 2$) | Emitted Output |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Push | 1 | `[1]` | False | - |
| 2 | Push | 2 | `[1, 2]` | **True (Base Case)** | **`[1, 2]`** |
| 3 | Pop / Push | 3 | `[1, 3]` | **True (Base Case)** | **`[1, 3]`** |
| 4 | Pop / Push | 4 | `[1, 4]` | **True (Base Case)** | **`[1, 4]`** |
| 5 | Pop to root | - | `[]` | - | - |
| 6 | Push | 2 | `[2]` | False | - |
| 7 | Push | 3 | `[2, 3]` | **True (Base Case)** | **`[2, 3]`** |
| 8 | Pop / Push | 4 | `[2, 4]` | **True (Base Case)** | **`[2, 4]`** |
| 9 | Pop to root | - | `[]` | - | - |
| 10 | Push | 3 | `[3]` | False | - |
| 11 | Push | 4 | `[3, 4]` | **True (Base Case)** | **`[3, 4]`** |
| 12 | Pop to root | - | `[]` | - | - |
| 13 | Prune 4 | 4 | - | $4 > 3$ (Pruned) | Search Complete |

---

## 5. Algorithmic Correctness

**Soundness.** Since every recursive branch advances the lower bound $i + 1$, elements in $\text{path}$ are strictly monotonically increasing ($p_1 < p_2 < \dots < p_k$). Consequently, any two generated paths that contain the same set of elements must be identical, preventing duplicate set generation.

**Completeness.** Pruning only discards candidate $i$ when $(n - i + 1) < (k - |\text{path}|)$. Because there are fewer remaining numbers than vacancies, no valid $k$-combination could ever be formed along the discarded path. All legitimate combinations are visited.

---

## 6. Traps This Instance Exposes

- **Missing Mathematical Pruning:** Looping all the way up to $n$ instead of $n - (k - |\text{path}|) + 1$ visits dead-end recursive branches that fail down the line, slowing performance significantly when $n$ is large.
- **Passing Mutable Lists by Reference:** Appending `path` directly to results (`results.append(path)`) causes all entries to reference the same mutable list object, which ends empty `[]` after backtracking. Adding a shallow copy (`results.append(path[:])` or `list(path)`) is required.
- **$k > n$ Edge Case:** If $k > n$, 0 combinations are possible; the pruning formula immediately halts at depth 0, returning `[]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left( k \cdot \binom{n}{k} \right)$. There are $\binom{n}{k}$ combinations, and copying each valid combination of size $k$ takes $O(k)$ time. Pruning ensures the search tree visits only viable states.
- **Auxiliary Space Complexity:** $O(k)$ recursion call stack depth and path buffer storage (excluding the returned result array).
