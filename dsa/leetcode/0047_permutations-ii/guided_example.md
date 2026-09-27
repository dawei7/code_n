# Guided Example: Permutations II

We trace the step-by-step recursive backtracking search with duplicate sibling pruning on a representative array with repeated values:

- **Input:** $\text{nums} = [1, 1, 2]$
- **Required output:** `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

This instance demonstrates sorting to group duplicate values, the canonical precedence invariant ($\text{used}[j-1]$ prerequisite), distinguishing vertical multiplicity from horizontal branch duplication, and generating strictly unique permutations without post-processing sets.

---

## 1. Instance & Teaching Goal

Given a collection of numbers $\text{nums} = [1, 1, 2]$ that contains duplicate values, we must return all possible **unique** permutations.

If we treated the two $1$s as distinct ($1_a$ and $1_b$), standard permutation generation would produce $3! = 6$ arrangements:
1. $[1_a, 1_b, 2] \to [1, 1, 2]$
2. $[1_b, 1_a, 2] \to [1, 1, 2]$ (Duplicate!)
3. $[1_a, 2, 1_b] \to [1, 2, 1]$
4. $[1_b, 2, 1_a] \to [1, 2, 1]$ (Duplicate!)
5. $[2, 1_a, 1_b] \to [2, 1, 1]$
6. $[2, 1_b, 1_a] \to [2, 1, 1]$ (Duplicate!)

The objective is to enforce a canonical ordering rule during generation: an identical duplicate element $\text{nums}[j]$ may only be chosen if its preceding duplicate $\text{nums}[j-1]$ has already been committed to the active path. This prunes all 3 duplicate branches, emitting exactly the 3 unique permutations:
$$
\frac{3!}{2! \cdot 1!} = 3
$$

---

## 2. Conceptual Foundation & Invariants

### Sorting and Relative Precedence
We sort the array so all identical elements are contiguous:
$$
\text{nums} = [1, 1, 2]
$$

### The Sibling Pruning Condition
Inside the DFS loop over $j \in [0, N - 1]$:
```text
if used[j] or (j > 0 and nums[j] == nums[j - 1] and not used[j - 1]):
    continue
```

Why `not used[j - 1]` is the critical test:
1. **Vertical Multiplicity (Allowed):** If $\text{used}[j - 1]$ is $\text{True}$, the first $1$ is already placed in an earlier position of the current permutation. Choosing the second $1$ is legitimate and necessary to construct permutations like $[1, 1, 2]$.
2. **Horizontal Sibling Pruning (Forbidden):** If $\text{used}[j - 1]$ is $\text{False}$, the first $1$ was already evaluated at the current position, and its entire subtree has finished and backtracked. Choosing the second $1$ at this same position would explore an identical subtree of suffixes, producing duplicate permutations. Hence, we skip $j$.

> **Invariant.** Identical values are always consumed in strictly increasing index order along any valid branch. No duplicate value is ever chosen to begin a sibling branch if its preceding twin is available.

---

## 3. Step-by-Step Worked Execution

We trace the DFS traversal on sorted $\text{nums} = [1, 1, 2]$ ($N = 3$):

### Level 0: Choose Position 0

#### Choice 1: $j = 0$ (Value $1_a$)
- Mark $\text{used}[0] = \text{True}$. Path: $[1]$. Recurse to Level 1:
  - **Level 1 Choice: $j = 1$ (Value $1_b$)**
    - $\text{used}[1]$ is False. Check duplicate: $j=1, \text{nums}[1] == \text{nums}[0]$, but $\text{used}[0]$ is $\text{True}$! (Valid vertical use).
    - Mark $\text{used}[1] = \text{True}$. Path: $[1, 1]$. Recurse to Level 2:
      - Only $j = 2$ (Value $2$) is available.
      - Path: $[1, 1, 2]$. Length is 3!
      - **Record Permutation 1: `[1, 1, 2]`**.
      - Rollback $2$, rollback $1_b$.
  - **Level 1 Choice: $j = 2$ (Value $2$)**
    - Mark $\text{used}[2] = \text{True}$. Path: $[1, 2]$. Recurse to Level 2:
      - Remaining available: $j = 1$ ($1_b$).
      - Path: $[1, 2, 1]$. Length is 3!
      - **Record Permutation 2: `[1, 2, 1]`**.
      - Rollback $1_b$, rollback $2$, rollback $1_a$.

---

#### Choice 2: $j = 1$ (Value $1_b$) at Level 0
- Check duplicate condition:
  - $j = 1 > 0$.
  - $\text{nums}[1] == \text{nums}[0] == 1$.
  - $\text{used}[0]$ is $\text{False}$! (Earlier twin already explored and backtracked).
- **Pruning Triggered!** Skip $j = 1$ via `continue`.
- *(Prevents duplicating `[1, 1, 2]` and `[1, 2, 1]`)*.

---

#### Choice 3: $j = 2$ (Value $2$) at Level 0
- Mark $\text{used}[2] = \text{True}$. Path: $[2]$. Recurse to Level 1:
  - **Level 1 Choice: $j = 0$ (Value $1_a$)**
    - Mark $\text{used}[0] = \text{True}$. Path: $[2, 1]$. Recurse to Level 2:
      - Available: $j = 1$ ($1_b$). Since $\text{used}[0]$ is True, $1_b$ is accepted.
      - Path: $[2, 1, 1]$. Length is 3!
      - **Record Permutation 3: `[2, 1, 1]`**.
      - Rollback $1_b$, rollback $1_a$.
  - **Level 1 Choice: $j = 1$ (Value $1_b$)**
    - $\text{nums}[1] == \text{nums}[0]$ and $\text{used}[0]$ is $\text{False}$!
    - Skip $j = 1$!
  - Rollback $2$.

All choices complete. Output contains exactly 3 unique permutations.

---

## 4. Complete Execution Trace

| DFS Path | Position Examined | Candidate Index $j$ | Candidate Value | $\text{used}$ Array | Decision / Pruning Rule | Emitted Output |
|:---|:---:|:---:|:---:|:---:|:---|:---:|
| `[]` | Pos 0 | 0 | 1 | `[F, F, F]` | First choice; explore | - |
| `[1]` | Pos 1 | 1 | 1 | `[T, F, F]` | $\text{used}[0] == \text{T} \implies$ Valid vertical reuse | - |
| `[1, 1]` | Pos 2 | 2 | 2 | `[T, T, F]` | Last remaining element | **`[1, 1, 2]`** |
| `[1]` | Pos 1 | 2 | 2 | `[T, F, F]` | Valid choice | - |
| `[1, 2]` | Pos 2 | 1 | 1 | `[T, F, T]` | Last remaining element | **`[1, 2, 1]`** |
| `[]` | Pos 0 | 1 | 1 | `[F, F, F]` | $\text{nums}[1]==\text{nums}[0] \land \neg\text{used}[0]$ | **Pruned (Skip $1_b$)** |
| `[]` | Pos 0 | 2 | 2 | `[F, F, F]` | Valid choice; explore | - |
| `[2]` | Pos 1 | 0 | 1 | `[F, F, T]` | Valid choice | - |
| `[2, 1]` | Pos 2 | 1 | 1 | `[T, F, T]` | $\text{used}[0] == \text{T} \implies$ Valid vertical reuse | **`[2, 1, 1]`** |
| `[2]` | Pos 1 | 1 | 1 | `[F, F, T]` | $\text{nums}[1]==\text{nums}[0] \land \neg\text{used}[0]$ | **Pruned (Skip $1_b$)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted array is a valid permutation of length $N$ using every input element exactly once. Sibling pruning guarantees that identical values never head identical subtrees at the same recursion depth, ensuring zero duplicate permutations in the output.

**Completeness.** By requiring identical elements to be selected in left-to-right order ($1_a$ before $1_b$), we establish a unique canonical representative for each multiset permutation. Since the canonical representation is never skipped, all valid unique permutations are generated.

---

## 6. Traps This Instance Exposes

- **Using `used[j-1]` vs `not used[j-1]`:** Checking `if nums[j] == nums[j-1] and used[j-1]` would incorrectly prune the vertical branch, making it impossible to form $[1, 1, 2]$. Testing `not used[j-1]` targets horizontal sibling branches exclusively.
- **Forgetting to Sort:** The duplicate condition `nums[j] == nums[j-1]` assumes identical elements are adjacent. Without sorting, identical values scattered across the array will not trigger the check.
- **Cloning Mutated Paths:** As in all backtracking routines, appending `path[:]` rather than `path` prevents subsequent element pop operations from altering stored results.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot \frac{N!}{\prod n_i!})$, where $n_i$ is the count of each duplicate value. For $[1, 1, 2]$, $\frac{3!}{2! \cdot 1!} = 3$ unique permutations. Sorting takes $O(N \log N)$. Generating and copying each permutation takes $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$ for the recursion call stack, boolean `used` array, and candidate path list.
