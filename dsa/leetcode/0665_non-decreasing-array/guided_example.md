# Guided Example: Non-decreasing Array

We trace the step-by-step inversion detection ($nums[i] > nums[i+1]$), dual repair hypothesis branch testing (lowering $nums[i] \leftarrow nums[i+1]$ vs raising $nums[i+1] \leftarrow nums[i]$), prefix and suffix boundary monotonicity validation, and single-modification admissibility verification on representative integer arrays:

- **Input:** $nums = [4, 2, 3]$
- **Required output:** `true`
  - Non-decreasing definition:
    $$
    nums[i] \le nums[i + 1] \quad \text{for all } 0 \le i \le n - 2
    $$
  - Objective: Determine if the array can be made non-decreasing by modifying **at most one single element**.
- **The Dual-Modification Invariant:**
  - **Inversion Detection:**
    - Scan adjacent pairs from left to right.
    - If no inversion exists ($nums[i] \le nums[i+1]$ everywhere), the array is already sorted $\implies \mathbf{True}$.
    - Suppose we encounter the **first adjacent violation**:
      $$
      nums[i] > nums[i + 1]
      $$
    - Because we are allowed at most **one** modification, this conflict must be resolved immediately by modifying either $nums[i]$ or $nums[i + 1]$.
  - **The Two Competing Hypotheses:**
    - **Hypothesis 1 (Lower the Left Element):**
      - Set $nums[i] \leftarrow nums[i + 1]$.
      - Makes $nums[i] == nums[i + 1]$.
      - Check if the entire resulting array is now non-decreasing.
      - If yes $\implies \mathbf{True}$!
    - **Hypothesis 2 (Raise the Right Element):**
      - Set $nums[i + 1] \leftarrow nums[i]$.
      - Makes $nums[i + 1] == nums[i]$.
      - Check if the entire resulting array is now non-decreasing.
      - If yes $\implies \mathbf{True}$!
    - If **neither** modification produces a sorted array (or if multiple disjoint inversions exist that cannot be rectified by a single edit), then it is impossible $\implies \mathbf{False}$.
- **Step-by-Step Worked Execution Trace on $[4, 2, 3]$:**
  - Initial array: $[4, 2, 3]$, length $n = 3$.
  - **Step 1: Scan for First Inversion:**
    - Compare index $0$ and $1$:
      $$
      nums[0] = 4, \quad nums[1] = 2 \implies 4 > 2 \quad \mathbf{(Inversion\ Detected\ at\ i = 0!)}
      $$
  - **Step 2: Test Hypothesis 1 (Lower Left Element $nums[0]$):**
    - Set $nums[0] \leftarrow nums[1] = 2$.
    - Modified array:
      $$
      nums^{(1)} = [\mathbf{2}, \; 2, \; 3]
      $$
    - Verify monotonicity:
      - Pair $(0, 1)$: $2 \le 2 \implies \mathbf{True}$.
      - Pair $(1, 2)$: $2 \le 3 \implies \mathbf{True}$.
    - Entire array is now non-decreasing!
    - Hypothesis 1 succeeds immediately!
  - **Step 3: Conclude:**
    - Valid single-element repair found: change $nums[0]$ from $4$ to $2$.
    - Return **`true`**.
- **Failure Trace on Double Inversion ($nums = [4, 2, 1]$):**
  - First inversion at $i = 0$ ($4 > 2$).
  - Hypothesis 1 (lower $nums[0]$):
    - Array becomes $[2, 2, 1]$.
    - Check: $2 > 1$ at the end $\implies$ Not sorted!
  - Hypothesis 2 (raise $nums[1]$):
    - Array becomes $[4, 4, 1]$.
    - Check: $4 > 1$ at the end $\implies$ Not sorted!
  - Both hypotheses fail $\implies$ Return **`false`**.
- **Internal Predecessor Constraint ($nums = [3, 4, 2, 3]$):**
  - Inversion at $i = 1$ ($4 > 2$).
  - Hypothesis 1: lower $nums[1]$ to 2 $\implies [3, 2, 2, 3]$.
    - Fails because $3 > 2$ at the start!
  - Hypothesis 2: raise $nums[2]$ to 4 $\implies [3, 4, 4, 3]$.
    - Fails because $4 > 3$ at the end!
  - Return **`false`**.
- **Already Sorted Array ($nums = [1, 2, 3]$):**
  - 0 inversions detected $\implies$ Returns **`true`**.

This instance demonstrates local anomaly detection and finite hypothesis branch verification, mathematically proves why exactly two mutually exclusive single-element modifications exhaust the local solution space, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Determine if it can become non-decreasing by modifying **at most 1 element**.

```text
nums = [ 4, 2, 3 ]

Conflict: 4 > 2 at indices 0 and 1.

Option 1 (lower 4 to 2):
  [ 2, 2, 3 ] -> Sorted! Valid! Return true.

Option 2 (raise 2 to 4):
  [ 4, 4, 3 ] -> 4 > 3 -> Not sorted.
```

### The Invariant of the Single Inversion
- In an array with at most 1 allowable change, the first encountered inversion $nums[i] > nums[i + 1]$ must be fixed by either:
  1. Decreasing $nums[i]$ to $nums[i + 1]$.
  2. Increasing $nums[i + 1]$ to $nums[i]$.
- If neither option yields a fully non-decreasing array, no valid solution exists.

---

## 2. Conceptual Foundation & Invariants

### 1. The Decision Branch:
At the first index $i$ where $nums[i] > nums[i+1]$:
$$
\text{Test 1: } nums[i] \leftarrow nums[i+1] \implies \text{check if sorted}
$$
$$
\text{Test 2: } nums[i] \leftarrow a, \; nums[i+1] \leftarrow a \implies \text{check if sorted}
$$
$$
\text{Result} = (\text{Test 1 is sorted}) \lor (\text{Test 2 is sorted})
$$

### 2. Predecessor Compatibility Invariant:
To lower $nums[i]$ to $nums[i+1]$ without breaking the previous element:
$$
i == 0 \quad \lor \quad nums[i - 1] \le nums[i + 1]
$$
Otherwise, you must raise $nums[i+1]$ to $nums[i]$.

> **Local Defect Resolution Invariant.** Any single-element repair of an order inversion $x_i > x_{i+1}$ is uniquely bounded by the adjacent order constraints $x_{i-1} \le x_i' \le x_{i+1}$ or $x_i \le x_{i+1}' \le x_{i+2}$, giving at most two admissible modification candidates.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 2, 3]$:

---

### Step 1: Scan
- $i = 0$: $4 > 2$. Inversion found!

---

### Step 2: Try Lowering $nums[0]$
- $nums[0] = 2$.
- Array is $[2, 2, 3]$.
- Check: $2 \le 2$ (yes), $2 \le 3$ (yes).
- All pairs satisfy $a \le b$.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Input Sequence | Inversion Position $(i, i+1)$ | Conflict Values | Hypothesis 1 (Lower Left) | Hypothesis 2 (Raise Right) | Feasibility Result |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[4, 2, 3]` | $(0, 1)$ | $4 > 2$ | `[2, 2, 3]` (Sorted) | — | **`true`** |
| `[4, 2, 1]` | $(0, 1)$ | $4 > 2$ | `[2, 2, 1]` (Not sorted) | `[4, 4, 1]` (Not sorted) | **`false`** |
| `[3, 4, 2, 3]` | $(1, 2)$ | $4 > 2$ | `[3, 2, 2, 3]` (Failed at 0) | `[3, 4, 4, 3]` (Failed at 2) | **`false`** |
| `[1, 2, 3]` | None | None | Already sorted | Already sorted | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **$N \le 2$:** Any array of length 1 or 2 can be made non-decreasing by modifying at most 1 element $\implies$ always `true`.
- **Inversion at Beginning ($i = 0$):** Lowering $nums[0]$ has no left predecessor constraint $\implies$ always valid prefix.
- **Inversion at End ($i = n - 2$):** Raising $nums[n - 1]$ has no right successor constraint $\implies$ always valid suffix.
- **Multiple Disjoint Inversions:** Fails naturally during the post-modification sorted check.

---

## 6. Traps & Common Anti-Patterns

- **Only Counting Inversions:** Counting $nums[i] > nums[i+1]$ can fail on inputs like `[3, 4, 2, 3]`: there is only 1 inversion ($4 > 2$), but it cannot be fixed with 1 modification! You must actually verify the resulting modified array.
- **Greedy Modification Without Checking Both Branches:** Assuming you should always lower $nums[i]$ fails when $nums[i-1] > nums[i+1]$ (e.g. $[3, 3, 2]$).
- **Mutating Input Permanently Without Restoring:** If Hypothesis 1 fails, remember to restore $nums[i]$ before testing Hypothesis 2.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding the first inversion: $\mathcal{O}(N)$ scan.
  - Verifying if the modified array is sorted: $\mathcal{O}(N)$ scan.
  - At most 2 verification passes occur.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (in-place modification and scalar variables).
