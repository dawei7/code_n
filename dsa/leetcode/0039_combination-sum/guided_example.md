# Guided Example: Combination Sum

We trace the step-by-step recursive backtracking decision tree on a representative multiset combination instance:

- **Input:** $\text{candidates} = [2, 3, 6, 7]$, $\text{target} = 7$
- **Required output:** `[[2, 2, 3], [7]]`

This instance demonstrates sorting to enable early branch pruning, recursive re-use of candidates via start-index forwarding, state rollback upon exceeding remaining capacity, and structural duplicate elimination.

---

## 1. Instance & Teaching Goal

Given an array of distinct integers $\text{candidates} = [2, 3, 6, 7]$ and a target integer $\text{target} = 7$, we must find all unique combinations of candidates where the chosen numbers sum to $7$. The same candidate number may be chosen an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers differs. For example, $[2, 2, 3]$ and $[3, 2, 2]$ represent the exact same multiset combination and must not both appear in the output.

A naive approach generates all unrestricted permutations of candidates summing to 7 and filters them with a hash set. The optimal backtracking approach enforces non-decreasing candidate indices: by only allowing candidates at index $j \ge i$ in subsequent recursive steps, every valid multiset combination is generated in canonical sorted order exactly once without hash-set filtering.

---

## 2. Conceptual Foundation & Invariants

### Canonical Search Order
We sort $\text{candidates}$ in ascending order:
$$
\text{candidates} = [2, 3, 6, 7]
$$

We define recursive state `backtrack(start_idx, remain, current_combo)`:
1. **Base Case 1 (Success):** If $\text{remain} == 0$, append a copy of $\text{current\_combo}$ to the results list.
2. **Loop & Early Prune:** For $j \in [\text{start\_idx}, N - 1]$:
   - If $\text{candidates}[j] > \text{remain}$: Because candidates are sorted, all subsequent candidates $k > j$ will also exceed $\text{remain}$. We `break` immediately (early pruning).
   - **Forward Transition:** Append $\text{candidates}[j]$ to $\text{current\_combo}$, and recurse with:
     $$
     \text{backtrack}(j, \text{remain} - \text{candidates}[j], \text{current\_combo})
     $$
     *(Passing index $j$ rather than $j + 1$ allows $\text{candidates}[j]$ to be reused).*
   - **Rollback:** Pop $\text{candidates}[j]$ from $\text{current\_combo}$ before trying the next candidate.

> **Invariant.** At any state, $\text{sum}(\text{current\_combo}) + \text{remain} = \text{target}$, and $\text{current\_combo}$ contains elements with non-decreasing indices. This guarantees zero duplicate combinations.

---

## 3. Step-by-Step Worked Execution

We trace the decision tree from root `backtrack(0, 7, [])`:

### Subtree 1: Starting with Candidate `2` (Index 0)
- **Path `[2]` ($\text{remain} = 5$):**
  - Next candidate `2` (idx 0):
    - **Path `[2, 2]` ($\text{remain} = 3$):**
      - Next candidate `2` (idx 0):
        - **Path `[2, 2, 2]` ($\text{remain} = 1$):**
          - Try `2`: $2 > 1 \implies$ prune branch.
          - Try `3, 6, 7`: all $> 1 \implies$ prune.
          - Backtrack to `[2, 2]`.
      - Next candidate `3` (idx 1):
        - **Path `[2, 2, 3]` ($\text{remain} = 3 - 3 = 0$):**
          - $\text{remain} == 0$! **Match found: `[2, 2, 3]`**.
          - Record copy in results.
      - Next candidate `6` (idx 2): $6 > 3 \implies$ prune.
      - Backtrack to `[2]`.
  - Next candidate `3` (idx 1):
    - **Path `[2, 3]` ($\text{remain} = 5 - 3 = 2$):**
      - Next candidate $\ge 3$: smallest is $3 > 2 \implies$ prune.
      - Backtrack to `[2]`.
  - Next candidate `6` (idx 2): $6 > 5 \implies$ prune.
  - Backtrack to `[]`.

---

### Subtree 2: Starting with Candidate `3` (Index 1)
- **Path `[3]` ($\text{remain} = 7 - 3 = 4$):**
  - Next candidate $\ge 3$:
    - Choose `3` (idx 1):
      - **Path `[3, 3]` ($\text{remain} = 4 - 3 = 1$):**
        - Next candidate $\ge 3$: smallest is $3 > 1 \implies$ prune.
        - Backtrack to `[3]`.
    - Try `6` (idx 2): $6 > 4 \implies$ prune.
  - Backtrack to `[]`.

---

### Subtree 3: Starting with Candidate `6` (Index 2)
- **Path `[6]` ($\text{remain} = 7 - 6 = 1$):**
  - Next candidate $\ge 6$: smallest is $6 > 1 \implies$ prune.
  - Backtrack to `[]`.

---

### Subtree 4: Starting with Candidate `7` (Index 3)
- **Path `[7]` ($\text{remain} = 7 - 7 = 0$):**
  - $\text{remain} == 0$! **Match found: `[7]`**.
  - Record copy in results.
  - Backtrack to `[]`.

All branches exhausted. Emitted combinations: `[[2, 2, 3], [7]]`.

---

## 4. Complete Execution Trace

### Backtracking Decision Tree Table

| DFS Path Explored | Chosen Element | Remaining Needed | Decision / Condition Met | Action Taken |
|:---|:---:|:---:|:---|:---|
| `[]` $\to$ `[2]` | 2 | 5 | $2 \le 5$; recurse | Recurse with start index 0 |
| `[2]` $\to$ `[2, 2]` | 2 | 3 | $2 \le 3$; recurse | Recurse with start index 0 |
| `[2, 2]` $\to$ `[2, 2, 2]` | 2 | 1 | $2 \le 1$ is False | Prune branch; backtrack |
| `[2, 2]` $\to$ `[2, 2, 3]` | 3 | 0 | $3 == 3 \implies \text{remain} = 0$ | **Record `[2, 2, 3]`**; backtrack |
| `[2, 2]` $\to$ try 6 | 6 | - | $6 > 3$ | Prune branch |
| `[2]` $\to$ `[2, 3]` | 3 | 2 | $3 \le 5$; recurse | Recurse with start index 1 |
| `[2, 3]` $\to$ try 3 | 3 | - | $3 > 2$ | Prune branch; backtrack |
| `[]` $\to$ `[3]` | 3 | 4 | $3 \le 7$; recurse | Recurse with start index 1 |
| `[3]` $\to$ `[3, 3]` | 3 | 1 | $3 \le 4$; recurse | Recurse with start index 1 |
| `[3, 3]` $\to$ try 3 | 3 | - | $3 > 1$ | Prune branch; backtrack |
| `[]` $\to$ `[6]` | 6 | 1 | $6 \le 7$; recurse | Recurse with start index 2 |
| `[6]` $\to$ try 6 | 6 | - | $6 > 1$ | Prune branch; backtrack |
| `[]` $\to$ `[7]` | 7 | 0 | $7 == 7 \implies \text{remain} = 0$ | **Record `[7]`**; backtrack |

---

## 5. Algorithmic Correctness

**Soundness.** A combination is added to the result list if and only if $\text{remain} == 0$, which means the sum of its elements equals $\text{target}$. Since all candidates are strictly positive ($> 0$), each candidate addition strictly reduces $\text{remain}$, making infinite cycles impossible.

**Completeness.** Every combination can be written uniquely in non-decreasing order. Because the algorithm systematically explores every choice with index $j \ge \text{start\_idx}$, the unique ordered representation of every valid combination is guaranteed to be generated.

---

## 6. Traps This Instance Exposes

- **Storing List References Instead of Copies:** Appending `current_combo` directly into `results` stores a reference to the mutable working list. When subsequent backtracking calls modify the list, earlier entries in `results` become corrupted or empty. Appending a clone `current_combo[:]` is essential.
- **Missing Early Break Optimization:** Without sorting, one must continue checking all remaining candidates even after one exceeds $\text{remain}$. Sorting allows an immediate `break`, pruning entire subtrees.
- **Forgetting Element Reuse ($j$ vs $j+1$):** Passing $j + 1$ prevents candidate reuse (which is required for $0040\text{ Combination Sum II}$, but incorrect for $0039$). Passing $j$ allows arbitrary reuse while preventing smaller-index elements from creating permutations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^{T/M})$, where $N = |\text{candidates}|$, $T = \text{target}$, and $M = \min(\text{candidates})$. The maximum recursion depth is $T / M$ (e.g. $7 / 2 = 3$). Loose upper bound is bounded by the number of nodes in the $N$-ary decision tree of depth $T/M$, with early pruning reducing actual visited states to a small fraction.
- **Auxiliary Space Complexity:** $O(T / M)$ recursion stack depth and working list storage.
