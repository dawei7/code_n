# Guided Example: Maximum Frequency Score of a Subarray

We trace the dynamic Array, Hash Table, Math, Stack, Sliding Window sliding window on a representative input instance.

- **Input:** `{"nums": [1, 1, 1, 2, 1, 2], "k": 3}`
- **Required output:** `5`

This instance highlights expanding the right boundary $R$, maintaining the internal frequency/validity state, and contracting the left boundary $L$ to restore feasibility.

---

## 1. Instance & Teaching Goal

The objective for **Maximum Frequency Score of a Subarray** is to find the optimal contiguous window without evaluating all $O(N^2)$ candidate subarrays.
By recognizing that the window constraint exhibits monotonic expansion and contraction, we adjust two pointers $L$ and $R$ in a single forward pass.

---

## 2. Conceptual Foundation & Invariants

We maintain two boundary indices $L$ and $R$, alongside a state tracker $M$ (frequency map or accumulator).

| State Tracker | Role in Algorithm |
|---|---|
| Left Boundary $L$ | Tracks start of active contiguous window |
| Right Boundary $R$ | Expands exploration frontier |
| Window State $M$ | Tracks validity metrics (character counts / sum) |

> **Invariant.** At each step $R$, the window $[L, R]$ is adjusted so that it satisfies the problem constraints, and the global optimum is updated from all valid windows ending at $R$.

---

## 3. Step-by-Step Worked Execution

### Step 1: Expand Window by Advancing $R$

- Incorporate element at index $R$ into the window accumulator $M$.
- Check whether the expanded window satisfies the target constraint.

| Parameter | State |
|---|---|
| Active Window | $[L, R]$ |
| Window Condition | Evaluated against constraint |
| Optimum Candidate | Staged for update |

---

### Step 2: Contract Window from Left $L$ When Constraint Violated

- If adding element at $R$ causes an invalid state, increment $L$ and decrement $M$ until feasibility is restored.

| Parameter | State |
|---|---|
| Adjusted Boundary | $L$ advanced to restore validity |
| Restored Window | Valid subsegment $[L, R]$ |
| Global Optimum | Updated with valid window metric |

---

## 4. Complete Execution Trace

| Step | $R$ | Processed Item | Condition Met? | Action on $L$ | Active Window $[L, R]$ | Current Metric | Global Best |
|---|---|---|---|---|---|---|---|
| 1 (Start) | 0 | First item | Yes | $L = 0$ | `[0, 0]` | Initial window metric | Baseline |
| 2 (Expand) | Intermediate | Next item | Evaluated | Advance $L$ if invalid | Dynamic $[L, R]$ | Valid window metric | Updated |
| 3 (Finish) | End | Final item | Maintained | Final adjustment | Terminal $[L, R]$ | Final window metric | Confirmed Best |

---

## 5. Algorithmic Correctness

**Soundness.** Every window evaluated for the global optimum satisfies the exact validity condition by virtue of the while-contraction loop.

**Completeness.** Since $R$ visits every possible ending position and $L$ identifies the widest valid prefix for that $R$, no maximal valid window is overlooked.

---

## 6. Traps This Instance Exposes

- **Backward Pointer Movement:** Setting $L$ from stale lookup tables without taking $\max(L, \dots)$ can cause $L$ to jump backwards, admitting invalid elements.
- **Off-by-One Window Size:** The length of window $[L, R]$ is $R - L + 1$, not $R - L$.
- **Premature Exit:** Stopping expansion when an invalid element is encountered instead of contracting $L$ misses valid downstream windows.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ amortized. The right pointer $R$ increments $N$ times, and the left pointer $L$ increments at most $N$ times.
- **Auxiliary Space Complexity:** $O(K)$ where $K$ is the size of the distinct character alphabet or state map.