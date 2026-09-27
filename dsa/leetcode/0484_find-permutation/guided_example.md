# Guided Example: Find Permutation

We trace the step-by-step lexicographical greedy baseline initialization ($[1, 2, \dots, n+1]$), contiguous `'D'` run detection ($s[i \dots j-1] == \text{'D'}$), subarray segment reversal ($ans[i \dots j]$), and boundary continuity preservation on representative sign patterns:

- **Input:** $s = \text{"DI"}$
- **Required output:** `[2, 1, 3]`
  - Pattern length: $n = 2$
  - Permutation length: $n + 1 = 3$ (using numbers $\{1, 2, 3\}$)
  - Objective: Lexicographically smallest permutation satisfying $perm[0] > perm[1] < perm[2]$
- **Greedy execution trace:**
  - **Step 1: Initialize baseline in sorted ascending order:**
    $$
    ans = [1, \; 2, \; 3]
    $$
    *Insight:* Ascending order $[1, 2, 3]$ is the lexicographically smallest possible permutation of $\{1, 2, 3\}$. Any `'I'` relationship is already satisfied.
  - **Step 2: Process sign constraints:**
    - Start at $i = 0$: $s[0] = \text{'D'}$
    - Scan the contiguous block of `'D'` characters:
      - $s[0] = \text{'D'}$
      - $s[1] = \text{'I'} \ne \text{'D'}$ (Block ends at index $j = 1$)
    - Block span in permutation: indices $i = 0$ to $j = 1$ (elements $[ans[0], ans[1]] = [1, 2]$)
    - To satisfy the `'D'` condition ($perm[0] > perm[1]$) while keeping values as small as possible, **reverse the subarray** $ans[0 \dots 1]$:
      $$
      [1, 2] \xrightarrow{\text{reverse}} [2, 1]
      $$
    - Permutation after reversal:
      $$
      ans = [\mathbf{2}, \; \mathbf{1}, \; 3]
      $$
    - Advance pointer: $i \leftarrow \max(0 + 1, 1) = 1$
  - **Step 3: Process remaining indices:**
    - At index $i = 1$: $s[1] = \text{'I'}$
    - No `'D'` run starting at $i = 1 \implies$ Subarray remains unchanged.
    - Advance pointer: $i \leftarrow 2 \ge n$. Loop halts.
  - Final permutation: **`[2, 1, 3]`**
  - Verification:
    - $perm[0] = 2 > perm[1] = 1$ (Satisfies `'D'`)
    - $perm[1] = 1 < perm[2] = 3$ (Satisfies `'I'`)
- **Pure Increase Instance:** $s = \text{"I"} \implies [1, 2]$ (no reversals needed)
- **Multi-Decrease Instance ($s = \text{"DDI"}, n = 3$):**
  - Baseline: $[1, 2, 3, 4]$
  - Run of two `'D'`s spanning indices $0 \dots 2$: reverse $[1, 2, 3] \implies [\mathbf{3, 2, 1}, 4]$
- **Pure Decrease Instance ($s = \text{"DDD"}, n = 3$):**
  - Baseline: $[1, 2, 3, 4] \implies$ reverse all $\implies [\mathbf{4, 3, 2, 1}]$

This instance demonstrates lexicographical greedy baseline inversion, mathematically proves why reversing contiguous descending blocks yields the unique minimal permutation, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$ of length $n$ containing only characters `'I'` (Increase) and `'D'` (Decrease):
Reconstruct the **lexicographically smallest** permutation of numbers $[1, n + 1]$ such that:
- $perm[i] < perm[i + 1]$ whenever $s[i] == \text{'I'}$
- $perm[i] > perm[i + 1]$ whenever $s[i] == \text{'D'}$

```text
Target Pattern: "D I" (n = 2)

Step 1: Minimal Baseline:
        [ 1,  2,  3 ]

Step 2: Identify 'D' Run at index 0:
        s[0] = 'D' spans perm[0] and perm[1]
        Reverse subarray [1, 2] -> [2, 1]

Result: [ 2,  1,  3 ]
Check:   2 > 1  <  3
         (D)   (I)      -> Valid & Lexicographically Smallest!
```

### The Inherent Optimality of Reversal
- The globally smallest permutation of $n + 1$ distinct numbers is the identity permutation $[1, 2, \dots, n + 1]$.
- If $s[i] == \text{'I'}$, the identity permutation already satisfies $perm[i] < perm[i + 1]$.
- If a sequence of $k$ consecutive `'D'`s occurs from index $i$ to $i + k - 1$:
  $$
  perm[i] > perm[i + 1] > \dots > perm[i + k]
  $$
  The smallest $k + 1$ numbers available at that stage are $\{x, x + 1, \dots, x + k\}$.
  To satisfy the descending requirement with the smallest possible starting number, we assign them in strictly reversed order:
  $$
  x + k, \; x + k - 1, \; \dots, \; x
  $$
- This greedy choice guarantees that the prefix remains lexicographically minimal.

---

## 2. Conceptual Foundation & Invariants

### 1. The Block-Reversal Algorithm:
1. Initialize array $ans = [1, 2, 3, \dots, n + 1]$.
2. Maintain index $i = 0$.
3. While $i < n$:
   - If $s[i] == \text{'D'}$:
     - Find the end of the contiguous block of `'D'` characters:
       $$
       j = i, \quad \text{while } j < n \text{ and } s[j] == \text{'D'}: j \leftarrow j + 1
       $$
     - Reverse the subarray $ans[i \dots j]$:
       $$
       ans[i \dots j] \leftarrow \text{reverse}(ans[i \dots j])
       $$
     - Advance $i \leftarrow j$.
   - If $s[i] == \text{'I'}$:
     - Advance $i \leftarrow i + 1$.
4. Return $ans$.

> **Lexicographical Invariant.** Reversing each maximal run of `'D'` independently changes the minimal number of inversions required to satisfy the constraints, leaving all `'I'` transitions strictly increasing.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"DI"}$ ($n = 2$):

---

### Step 1: Initialize Identity Array
$$
ans = [1, \; 2, \; 3]
$$

---

### Step 2: Identify Contiguous 'D' Run
- Set $i = 0$.
- Inspect $s[0]$: character is `'D'`.
- Expand $j$:
  - $s[0] == \text{'D'} \implies j = 1$.
  - $s[1] == \text{'I'} \ne \text{'D'} \implies$ stop expansion.
- The maximal run of `'D'` is $s[0 \dots 0]$ ($k = 1$ decrease).
- Affected permutation slice: indices $0$ through $1$ ($ans[0 \dots 1]$).

---

### Step 3: Reverse Subarray
- Elements before: $ans[0 \dots 1] = [1, 2]$.
- Reverse:
  $$
  ans[0 \dots 1] \leftarrow [2, 1]
  $$
- Array state:
  $$
  ans = [\mathbf{2}, \; \mathbf{1}, \; 3]
  $$
- Advance cursor: $i \leftarrow j = 1$.

---

### Step 4: Process Character at $i = 1$
- Inspect $s[1]$: character is `'I'`.
- No `'D'` block $\implies$ Advance $i \leftarrow 2$.
- Since $i = 2 \ge n$, loop halts.

---

### Final Permutation:
$$
ans = \mathbf{[2, 1, 3]}
$$

---

## 4. Complete Execution Trace

| Pattern String $s$ | Initial Identity Baseline | Contiguous `'D'` Runs Found | Subarrays Reversed | Resulting Permutation | Relation Check |
|:---:|:---:|:---|:---|:---:|:---:|
| `"I"` | `[1, 2]` | None | None | **`[1, 2]`** | $1 < 2$ |
| `"D"` | `[1, 2]` | $s[0] = \text{'D'}$ | `ans[0..1]` | **`[2, 1]`** | $2 > 1$ |
| `"DI"` | `[1, 2, 3]` | $s[0] = \text{'D'}$ | `ans[0..1]` | **`[2, 1, 3]`** | $2 > 1 < 3$ |
| `"ID"` | `[1, 2, 3]` | $s[1] = \text{'D'}$ | `ans[1..2]` | **`[1, 3, 2]`** | $1 < 3 > 2$ |
| `"DDI"` | `[1, 2, 3, 4]` | $s[0..1] = \text{"DD"}$ | `ans[0..2]` | **`[3, 2, 1, 4]`** | $3 > 2 > 1 < 4$ |
| `"DID"` | `[1, 2, 3, 4]` | $s[0]=\text{'D'}, s[2]=\text{'D'}$ | `ans[0..1]`, `ans[2..3]` | **`[2, 1, 4, 3]`** | $2 > 1 < 4 > 3$ |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Length ($n = 1$, $s = \text{"I"}$):** Returns $[1, 2]$.
- **Minimum Length ($n = 1$, $s = \text{"D"}$):** Returns $[2, 1]$.
- **All Increasing ($s = \text{"IIII"}$):** Returns identity array $[1, 2, 3, 4, 5]$ with zero modifications.
- **All Decreasing ($s = \text{"DDDD"}$):** Reverses entire array $\implies [5, 4, 3, 2, 1]$.

---

## 6. Traps & Common Anti-Patterns

- **Stack-Based Off-by-One:** Stacking numbers and popping on `'I'` is another valid technique, but handling the trailing number after the loop ends requires an extra flush step. The in-place array reversal method eliminates off-by-one errors.
- **Overlapping Block Inversions:** Reversing beyond $j$ corrupts the adjacent increasing relationship. Reversing strictly from $i$ to $j$ guarantees that $ans[j] < ans[j+1]$ when followed by `'I'`.
- **Quadratic Slicing in Python:** Slicing and re-assigning repeatedly with `ans[i:j+1] = ...` can be $O(N^2)$ if entire copies are made. Using two pointers to swap elements in place guarantees $O(N)$ runtime.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding `'D'` blocks traverses $s$ linearly.
  - Each element of $ans$ is swapped during reversal at most once.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, finishes in $< 12$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ to store the output permutation array.
