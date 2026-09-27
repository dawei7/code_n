# Guided Example: Combination Sum III

We trace the step-by-step lexicographic backtracking search, remaining-sum pruning, and size-constrained path collection on representative digit combination queries:

- **Input:** $k = 3, \quad n = 7$
- **Required output:** `[[1, 2, 4]]` (Only $1 + 2 + 4 = 7$ uses exactly 3 distinct digits from $\{1 \dots 9\}$)
- **Multiple Solutions Instance:** $k = 3, \quad n = 9 \implies [[1, 2, 6], [1, 3, 5], [2, 3, 4]]$
- **Impossible Underflow Instance:** $k = 4, \quad n = 1 \implies []$ (Minimum possible sum for 4 distinct digits is $1 + 2 + 3 + 4 = 10 > 1$)
- **Maximum Complete Set Instance:** $k = 9, \quad n = 45 \implies [[1, 2, 3, 4, 5, 6, 7, 8, 9]]$

This instance demonstrates constrained subset enumeration with fixed size $k$ and fixed sum $n$, enforces strictly increasing digit order ($d_{i} < d_{i+1}$) to eliminate duplicate permutations, applies early branch pruning ($d > \text{remaining\_sum}$), and searches a bounded combinatorial space of $\binom{9}{k} \le 126$ states.

---

## 1. Instance & Teaching Goal

Given two integers $k = 3$ (number of digits) and $n = 7$ (target sum):
Find all valid combinations of $k$ distinct numbers chosen from $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$ such that:
1. Each number is used at most once.
2. The numbers sum to exactly $n$.
3. The combination contains exactly $k$ numbers.

Evaluating possible 3-digit candidate sets:
- $\{1, 2, 3\}$: sum $= 6 < 7$.
- $\{1, 2, 4\}$: sum $= 1 + 2 + 4 = 7$. **Valid combination.**
- $\{1, 2, 5\}$: sum $= 8 > 7$.
- Any larger digits (e.g. $\{1, 3, 4\} \implies 8$, $\{2, 3, 4\} \implies 9$) exceed the target sum $7$.
Output: `[[1, 2, 4]]`.

### Why Enforce Strictly Increasing Order?
If digits were chosen in arbitrary order, the set $\{1, 2, 4\}$ would be generated $3! = 6$ times (e.g. $[1, 2, 4], [2, 1, 4], [4, 2, 1], \dots$).
By enforcing that each chosen digit is strictly greater than the previous digit ($d_{\text{next}} \ge \text{start}$ where $\text{start} = d_{\text{prev}} + 1$):
- Duplicate permutations are prevented by construction.
- Digits cannot be reused.
- The output contains only unique combinations in lexicographical order.

---

## 2. Conceptual Foundation & Invariants

### Backtracking Search State
Define $\text{backtrack}(\text{start}, \text{path}, \text{rem\_sum})$:
- `start`: the smallest candidate digit available for selection ($\in [1, 9]$).
- `path`: the current list of chosen digits (length $\le k$).
- `rem\_sum`: the remaining sum needed ($n - \sum \text{path}$).

### Transition and Pruning Rules:
1. **Base Termination:**
   If $\text{len}(\text{path}) == k$:
   - If $\text{rem\_sum} == 0$: append a copy of `path` to `result`.
   - Return (do not explore further, since adding positive digits will exceed $k$).
2. **Candidate Iteration with Pruning:**
   For digit $d$ from $\text{start}$ to $9$:
   - **Pruning 1 (Sum Overflow):** If $d > \text{rem\_sum}$, break immediately (since candidates are increasing, all subsequent $d' > d$ will also exceed $\text{rem\_sum}$).
   - **Pruning 2 (Count Insufficiency):** If the count of remaining digits $(9 - d + 1)$ is strictly less than $(k - \text{len}(\text{path}))$, break (impossible to fill $k$ slots).
   - **Recurse:**
     $$
     \text{path.append}(d)
     $$
     $$
     \text{backtrack}(d + 1, \, \text{path}, \, \text{rem\_sum} - d)
     $$
     $$
     \text{path.pop()}
     $$

> **Invariant.** Along any recursion branch, `path` contains strictly increasing digits from $\{1 \dots 9\}$, ensuring no number is selected twice and no duplicate permutation is evaluated.

---

## 3. Step-by-Step Worked Execution

We trace the search for $k = 3, \, n = 7$:
Initial call: $\text{backtrack}(\text{start}=1, \, \text{path}=[], \, \text{rem\_sum}=7)$.

### Level 1 (First Digit Choices):
- **Choose $d = 1$:**
  - $\text{path} = [1], \quad \text{rem\_sum} = 7 - 1 = 6$.
  - Call $\text{backtrack}(2, [1], 6)$.

---

### Level 2 (Under $d = 1$):
- **Choose $d = 2$:**
  - $\text{path} = [1, 2], \quad \text{rem\_sum} = 6 - 2 = 4$.
  - Call $\text{backtrack}(3, [1, 2], 4)$.

---

### Level 3 (Under $[1, 2]$):
- **Candidate $d = 3$:**
  - $\text{path} = [1, 2, 3], \quad \text{rem\_sum} = 4 - 3 = 1$.
  - $\text{len}(\text{path}) = 3 == k$, but $\text{rem\_sum} = 1 \ne 0 \implies$ Discard. Backtrack.
- **Candidate $d = 4$:**
  - $\text{path} = [1, 2, 4], \quad \text{rem\_sum} = 4 - 4 = 0$.
  - $\text{len}(\text{path}) = 3 == k$ and $\text{rem\_sum} = 0$!
  - **Match Found! Add `[1, 2, 4]` to results.** Backtrack.
- **Candidate $d = 5$:**
  - $d = 5 > \text{rem\_sum} = 4 \implies$ **Pruning 1 triggers!** Break loop.

Backtrack to Level 2.

---

### Level 2 (Under $d = 1$, Next Candidates):
- **Choose $d = 3$:**
  - $\text{path} = [1, 3], \quad \text{rem\_sum} = 6 - 3 = 3$.
  - Next candidate must be $\ge 4$.
  - But $d = 4 > \text{rem\_sum} = 3 \implies$ Break loop immediately.
- **Choose $d \ge 4$:**
  - $d = 4 \implies \text{rem\_sum} = 2 < 4$. All prune.

Backtrack to Level 1.

---

### Level 1 (Next First Digit Candidates):
- **Candidate $d = 2$:**
  - $\text{path} = [2], \quad \text{rem\_sum} = 5$.
  - Level 2 must pick $d \ge 3$:
    - If $d = 3 \implies \text{rem\_sum} = 2$. Next digit $\ge 4 > 2 \implies$ Pruned!
- **Candidate $d \ge 3$:**
  - Minimum sum for 3 digits starting at 3 is $3 + 4 + 5 = 12 > 7 \implies$ Pruned!

Recursion finishes. Output: `[[1, 2, 4]]`.

---

## 4. Complete Execution Trace

```text
k = 3, n = 7

DFS Tree:
[]
 |-- [1] (rem=6)
 |    |-- [1, 2] (rem=4)
 |    |    |-- [1, 2, 3] (rem=1, len=3) -> sum!=0, discard
 |    |    |-- [1, 2, 4] (rem=0, len=3) -> MATCH! -> record [1, 2, 4]
 |    |    \-- [1, 2, 5] (5 > 4) -> PRUNED
 |    |-- [1, 3] (rem=3)
 |    |    \-- [1, 3, 4] (4 > 3) -> PRUNED
 |    \-- [1, 4] (rem=2) -> PRUNED
 |-- [2] (rem=5)
 |    \-- [2, 3] (rem=2)
 |         \-- [2, 3, 4] (4 > 2) -> PRUNED
 \-- [3] (min sum 3+4+5=12 > 7) -> PRUNED

Final Result: [[1, 2, 4]]
```

| Recursion Path | Selected Digit | Remaining Sum | Path Length | Decision / Branch Evaluation |
|:---|:---:|:---:|:---:|:---|
| `[]` | - | 7 | 0 | Root of search tree |
| `[1]` | 1 | 6 | 1 | Recurse with $\text{start}=2$ |
| `[1, 2]` | 2 | 4 | 2 | Recurse with $\text{start}=3$ |
| `[1, 2, 3]` | 3 | 1 | 3 | $\text{len} == 3, \, \text{rem} \ne 0 \implies$ Discard |
| **`[1, 2, 4]`** | **4** | **0** | **3** | **$\text{len} == 3, \, \text{rem} == 0 \implies$ Emit `[1, 2, 4]`** |
| `[1, 2, 5]` | 5 | - | - | $5 > 4 \implies$ Pruned |
| `[1, 3]` | 3 | 3 | 2 | Next digit $4 > 3 \implies$ Pruned |
| `[2]` | 2 | 5 | 1 | Smallest suffix $3 + 4 = 7 > 5 \implies$ Pruned |
| `[3]` | 3 | - | - | $3 + 4 + 5 = 12 > 7 \implies$ Pruned |

---

## 5. Algorithmic Correctness

**Soundness.** A path is emitted if and only if $\text{len}(\text{path}) == k$ and $\sum \text{path} == n$. Because candidates are drawn strictly from $\{1 \dots 9\}$ with $d_{\text{next}} > d_{\text{curr}}$, all digits are distinct and each combination is strictly ordered, guaranteeing 0 duplicate permutations in the output.

**Completeness.** Every combination of $k$ distinct digits from $\{1 \dots 9\}$ can be sorted into a unique strictly increasing sequence. The backtracking search explores the entire tree of strictly increasing sequences; pruning occurs only when the sum or remaining digit count mathematically guarantees no completion exists.

---

## 6. Traps This Instance Exposes

- **Deep Copying Paths:** Appending `path` directly to `result` (`result.append(path)`) stores references to the mutable list, which becomes empty when backtracking completes. Appending a copy (`result.append(list(path))` or `result.append(path[:])`) is mandatory.
- **Missing Break Pruning:** Continuing the loop after $d > \text{rem\_sum}$ wastes time evaluating $d+1, \dots, 9$, all of which also exceed the sum. Using `break` instead of `continue` prunes entire subtrees.
- **Extreme Target Bounds:** If $n < \frac{k(k+1)}{2}$ (e.g. $k = 4, n = 9 < 10$) or $n > \sum_{i=10-k}^{9} i$, no solution is possible and the search terminates immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(\binom{9}{k} \cdot k\right)$. The total number of subsets of size $k$ from 9 digits is $\binom{9}{k} \le \binom{9}{4} = 126$. Each valid combination takes $O(k)$ time to copy into the results array. The search space is bounded by at most $512$ total nodes.
- **Auxiliary Space Complexity:** $O(k)$ auxiliary space for the recursion call stack and the active `path` buffer, where $k \le 9$.
