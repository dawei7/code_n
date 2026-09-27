# Guided Example: Subsets II

We trace the step-by-step backtracking search with horizontal duplicate sibling pruning on a representative multiset:

- **Input:** $\text{nums} = [1, 2, 2]$
- **Required output:** $[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]$

This instance demonstrates sorting to group duplicate elements together, differentiating vertical depth multiplicity ($j = \text{start}$) from duplicate horizontal sibling branching ($j > \text{start} \land \text{nums}[j] == \text{nums}[j - 1]$), state rollback, and contrasting cascading vs backtracking deduplication.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 2]$ that contains duplicate elements, return all possible subsets (the power set). The solution set must **not** contain duplicate subsets.

If treated as distinct elements, a 3-element set generates $2^3 = 8$ subsets.
However, because $2$ appears twice:
- $\{2_A\}$ and $\{2_B\}$ are identical subsets ($[2]$).
- $\{1, 2_A\}$ and $\{1, 2_B\}$ are identical subsets ($[1, 2]$).
The unique power set contains strictly $6$ distinct subsets:
$$
[[], \, [1], \, [1, 2], \, [1, 2, 2], \, [2], \, [2, 2]]
$$

Sorting the array upfront ($[1, 2, 2]$) ensures that identical values sit next to each other.
The backtracking condition:
$$
\text{if } j > \text{start} \text{ and } \text{nums}[j] == \text{nums}[j - 1]: \text{continue}
$$
prunes redundant sibling branches while still allowing vertical depth recursion to form multisets like $[2, 2]$.

---

## 2. Conceptual Foundation & Invariants

### Horizontal Sibling Pruning Rule
We define $\text{backtrack}(\text{start}, \text{path})$:
1. **Emit Current Subset:**
   At every recursive node, the current prefix $\text{path}$ is a valid unique subset:
   $$
   \text{results.append}(\text{list}(\text{path}))
   $$
2. **Loop Over Candidates ($j \in [\text{start}, N - 1]$):**
   - **Vertical Progression ($j == \text{start}$):**
     This is the first candidate considered at this recursion level, or the immediate continuation of an identical number from above (e.g. adding the second $2$ to $[1, 2]$ to form $[1, 2, 2]$). This branch is **permitted**.
   - **Horizontal Sibling Duplication ($j > \text{start} \land \text{nums}[j] == \text{nums}[j-1]$):**
     At this same tree level, another branch starting with an identical value was already fully explored by sibling $j - 1$. Exploring $j$ would generate exact duplicate subsets. This branch is **pruned** (`continue`).
3. **Explore and Backtrack:**
   - $\text{path.append}(\text{nums}[j])$
   - $\text{backtrack}(j + 1, \text{path})$
   - $\text{path.pop()}$

> **Invariant.** For any unique integer $v$, only the first available occurrence at index $\text{start}$ may head a new subtree branch at the current recursion depth.

---

## 3. Step-by-Step Worked Execution

We trace sorted $\text{nums} = [1, 2, 2]$:

### Root Level ($\text{path} = []$)
- Record empty set: `[]`.
- Loop candidates $j \in [0, 2]$:

---

### Branch $j = 0$ ($\text{val} = 1$):
- $j = 0 == \text{start} \implies$ Accepted.
- $\text{path} = [1]$. Record **$[1]$**.
- Recurse with $\text{start} = 1$:
  - **Child $j = 1$ ($\text{val} = 2$):**
    - $j = 1 == \text{start} \implies$ Accepted.
    - $\text{path} = [1, 2]$. Record **$[1, 2]$**.
    - Recurse with $\text{start} = 2$:
      - **Grandchild $j = 2$ ($\text{val} = 2$):**
        - $j = 2 == \text{start} \implies$ Accepted (Vertical reuse!).
        - $\text{path} = [1, 2, 2]$. Record **$[1, 2, 2]$**.
        - Recurse $\text{start} = 3 > 2 \implies$ returns.
        - Backtrack $\to [1, 2]$.
    - Backtrack $\to [1]$.
  - **Child $j = 2$ ($\text{val} = 2$):**
    - Check condition: $j = 2 > \text{start} = 1$, and $\text{nums}[2] == \text{nums}[1]$ ($2 == 2$).
    - **Duplicate Sibling Detected!** Pruned (`continue`).
- Backtrack from $[1] \to []$.

---

### Branch $j = 1$ ($\text{val} = 2$):
- $j = 1 > \text{start} = 0$, but $\text{nums}[1] = 2 \ne \text{nums}[0] = 1 \implies$ Accepted.
- $\text{path} = [2]$. Record **$[2]$**.
- Recurse with $\text{start} = 2$:
  - **Child $j = 2$ ($\text{val} = 2$):**
    - $j = 2 == \text{start} \implies$ Accepted (Vertical reuse!).
    - $\text{path} = [2, 2]$. Record **$[2, 2]$**.
    - Recurse $\text{start} = 3 \implies$ returns.
    - Backtrack $\to [2]$.
- Backtrack from $[2] \to []$.

---

### Branch $j = 2$ ($\text{val} = 2$):
- Check condition: $j = 2 > \text{start} = 0$, and $\text{nums}[2] == \text{nums}[1]$ ($2 == 2$).
- **Duplicate Sibling Detected!** Pruned (`continue`).

Search terminates. Exactly 6 subsets generated.

---

## 4. Complete Execution Trace

```text
                        []
             /          |          \
           [1]         [2]         [2] (PRUNED: j=2 > start=0, 2==2)
          /   \         |
      [1,2]   [1,2]   [2,2]
       /     (PRUNED)
    [1,2,2]
```

| Step | Current Path | Candidate Index $j$ | Candidate Value | $j > \text{start}$? | $\text{nums}[j] == \text{nums}[j-1]$? | Action | Subset Recorded |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `[]` | - | - | - | - | Base root | **`[]`** |
| 2 | `[1]` | 0 | 1 | No ($0 = 0$) | - | Recurse | **`[1]`** |
| 3 | `[1, 2]` | 1 | 2 | No ($1 = 1$) | - | Recurse | **`[1, 2]`** |
| 4 | `[1, 2, 2]` | 2 | 2 | No ($2 = 2$) | - | Recurse | **`[1, 2, 2]`** |
| 5 | `[1]` | 2 | 2 | **Yes ($2 > 1$)** | **Yes ($2 == 2$)** | **Prune duplicate** | - |
| 6 | `[2]` | 1 | 2 | Yes ($1 > 0$) | No ($2 \ne 1$) | Recurse | **`[2]`** |
| 7 | `[2, 2]` | 2 | 2 | No ($2 = 2$) | - | Recurse | **`[2, 2]`** |
| 8 | `[]` | 2 | 2 | **Yes ($2 > 0$)** | **Yes ($2 == 2$)** | **Prune duplicate** | - |

---

## 5. Algorithmic Correctness

**Soundness.** Sorting guarantees that all identical values are contiguous. The condition $j > \text{start} \land \text{nums}[j] == \text{nums}[j-1]$ ensures that among identical elements at any recursion depth, only the first occurrence is expanded horizontally. Hence, no duplicate subset combinations can ever be generated.

**Completeness.** Whenever multiple copies of an element exist, vertical recursion ($j = \text{start}$) allows picking the first, then the second, up to all available copies (e.g. $[2, 2]$). Every unique multiset frequency combination is faithfully explored.

---

## 6. Traps This Instance Exposes

- **Forgetting to Sort First:** The condition $\text{nums}[j] == \text{nums}[j-1]$ relies entirely on identical elements being adjacent. If $\text{nums} = [2, 1, 2]$ is not sorted, the two $2$s will be separated, generating duplicate $[2]$ subsets. Sorting is strictly mandatory.
- **Checking $j > 0$ Instead of $j > \text{start}$:** Writing $j > 0$ mistakenly prunes vertical depth recursion, preventing valid multisets like $[2, 2]$ from ever being generated. It must strictly be $j > \text{start}$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$. In the worst case (all elements distinct), $2^N$ subsets are generated, each requiring $O(N)$ copy operations. Pruning reduces the work proportionally when duplicates exist. Sorting takes $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ recursion depth and path buffer.
