# Guided Example: Remove Duplicates from Sorted Array II

We trace the step-by-step two-pointer compaction with lookback gating on a representative sorted array:

- **Input:** $\text{nums} = [1, 1, 1, 2, 2, 3]$
- **Required output:** Length $k = 5$, modified prefix $[1, 1, 2, 2, 3]$

This instance demonstrates in-place two-pointer filtering, the two-element lookback invariant ($\text{nums}[r] \ne \text{nums}[w - 2]$), skipping excess duplicates without extra memory, and generalizing the rule to arbitrary multiplicity limits.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ sorted in non-decreasing order:
$$
[1, 1, 1, 2, 2, 3]
$$
remove duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements must be kept the same, returning the number of retained elements $k$.

In $[1, 1, 1, 2, 2, 3]$:
- The number $1$ appears 3 times $\implies$ drop the 3rd occurrence.
- The number $2$ appears 2 times $\implies$ keep both.
- The number $3$ appears 1 time $\implies$ keep it.
The retained prefix is $[1, 1, 2, 2, 3]$ of length $k = 5$.

A naive algorithm using frequency dictionaries or array deletions shifts elements on each drop, causing $O(N^2)$ time.
By exploiting the sorted invariant, we can compare the incoming candidate against the element written two positions earlier ($\text{nums}[w - 2]$), filtering in a single $O(N)$ pass with $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### 2-Lookback Pointer Gating
Maintain a write pointer $w$ (initially $w = 0$).
Iterate a read pointer $r$ through all elements $x = \text{nums}[r]$:

1. **Acceptance Condition:**
   - If $w < 2$: The first two elements are always accepted.
   - If $w \ge 2$ and $x \ne \text{nums}[w - 2]$:
     Because the array is sorted, if $x == \text{nums}[w - 2]$, then $\text{nums}[w - 1]$ must also equal $\text{nums}[w - 2]$. Writing $x$ would create a 3rd duplicate.
     If $x > \text{nums}[w - 2]$, at most one duplicate of $x$ currently exists in the output. Thus, $x$ is valid!
2. **Write Action:**
   If accepted:
   $$
   \text{nums}[w] \leftarrow x, \quad w \leftarrow w + 1
   $$
   If rejected:
   - $w$ does not advance; candidate $x$ is skipped.

> **Invariant.** At every step, the slice $\text{nums}[0 \dots w-1]$ is non-decreasing and contains at most two occurrences of any unique integer.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, 1, 1, 2, 2, 3]$ ($N = 6$):

### Initialization
- Write pointer $w = 0$.

---

### Step 1 ($r = 0, \text{val} = 1$)
- Condition: $w = 0 < 2$. Accepted!
- Write: $\text{nums}[0] \leftarrow 1$.
- Advance: $w \leftarrow 1$.
- Prefix: `[1]`.

---

### Step 2 ($r = 1, \text{val} = 1$)
- Condition: $w = 1 < 2$. Accepted!
- Write: $\text{nums}[1] \leftarrow 1$.
- Advance: $w \leftarrow 2$.
- Prefix: `[1, 1]`.

---

### Step 3 ($r = 2, \text{val} = 1$)
- Condition: $w = 2 \ge 2$.
- Lookback check: Compare candidate $\text{val} = 1$ with $\text{nums}[w - 2] = \text{nums}[0] = 1$.
  $$
  1 == 1 \implies \textbf{Excess Duplicate! Reject.}
$$
- Action: Skip element. $w$ remains $2$.
- Prefix: `[1, 1]`.

---

### Step 4 ($r = 3, \text{val} = 2$)
- Condition: $w = 2 \ge 2$.
- Lookback check: Compare $\text{val} = 2$ with $\text{nums}[w - 2] = \text{nums}[0] = 1$.
  $$
  2 \ne 1 \implies \textbf{Valid! Accept.}
$$
- Write: $\text{nums}[2] \leftarrow 2$.
- Advance: $w \leftarrow 3$.
- Prefix: `[1, 1, 2]`.

---

### Step 5 ($r = 4, \text{val} = 2$)
- Condition: $w = 3 \ge 2$.
- Lookback check: Compare $\text{val} = 2$ with $\text{nums}[w - 2] = \text{nums}[1] = 1$.
  $$
  2 \ne 1 \implies \textbf{Valid! Accept.}
$$
- Write: $\text{nums}[3] \leftarrow 2$.
- Advance: $w \leftarrow 4$.
- Prefix: `[1, 1, 2, 2]`.

---

### Step 6 ($r = 5, \text{val} = 3$)
- Condition: $w = 4 \ge 2$.
- Lookback check: Compare $\text{val} = 3$ with $\text{nums}[w - 2] = \text{nums}[2] = 2$.
  $$
  3 \ne 2 \implies \textbf{Valid! Accept.}
$$
- Write: $\text{nums}[4] \leftarrow 3$.
- Advance: $w \leftarrow 5$.
- Prefix: `[1, 1, 2, 2, 3]`.

Termination. Return $k = w = 5$.

---

## 4. Complete Execution Trace

| Read Index $r$ | Value $\text{nums}[r]$ | Write Pointer $w$ | Gate Condition ($w < 2 \lor x \ne \text{nums}[w-2]$) | Decision | Action on Array | Active Prefix $\text{nums}[0 \dots w-1]$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 | 1 | 0 | $0 < 2$ (True) | Accept | $\text{nums}[0] = 1$ | `[1]` |
| 1 | 1 | 1 | $1 < 2$ (True) | Accept | $\text{nums}[1] = 1$ | `[1, 1]` |
| 2 | 1 | 2 | $1 \ne \text{nums}[0]$ ($1 \ne 1$ False) | **Reject** | Skip | `[1, 1]` |
| 3 | 2 | 2 | $2 \ne \text{nums}[0]$ ($2 \ne 1$ True) | Accept | $\text{nums}[2] = 2$ | `[1, 1, 2]` |
| 4 | 2 | 3 | $2 \ne \text{nums}[1]$ ($2 \ne 1$ True) | Accept | $\text{nums}[3] = 2$ | `[1, 1, 2, 2]` |
| 5 | 3 | 4 | $3 \ne \text{nums}[2]$ ($3 \ne 2$ True) | Accept | $\text{nums}[4] = 3$ | `[1, 1, 2, 2, 3]` |
| Final | - | **5** | - | - | **Return $k = 5$** | **`[1, 1, 2, 2, 3]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because the input is sorted in non-decreasing order, identical elements occur contiguously. If $\text{nums}[w - 2] == x$, then $\text{nums}[w - 1]$ must also equal $x$. Appending $x$ would create a third duplicate. If $\text{nums}[w - 2] < x$, at most one $x$ has been written so far, guaranteeing that $x$ can appear at most twice.

**Completeness.** Since $w \le r$ at all times, writes never overwrite unread input elements. The read pointer scans strictly from $0$ to $N - 1$, considering every original number.

---

## 6. Traps This Instance Exposes

- **Generalization to $K$ Duplicates:** This exact template generalizes to allowing at most $K$ duplicates by checking `w < K or x != nums[w - K]`. For $K = 1$ (LeetCode 26), compare against `w - 1`. For $K = 2$ (this problem), compare against `w - 2`.
- **Comparing Against $r - 2$ instead of $w - 2$:** Comparing $\text{nums}[r]$ against $\text{nums}[r - 2]$ fails when duplicates have already been skipped, because the input indices no longer match the compacted output layout. The lookback must check the **write** index $\text{nums}[w - 2]$.
- **Short Arrays ($N \le 2$):** If $N \le 2$, the condition $w < 2$ accepts all elements, immediately returning $N$ without any index out-of-bounds error.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. The loop executes $N$ times, doing $O(1)$ operations per element.
- **Auxiliary Space Complexity:** $O(1)$. Array elements are rearranged in place using scalar pointers $r$ and $w$.
