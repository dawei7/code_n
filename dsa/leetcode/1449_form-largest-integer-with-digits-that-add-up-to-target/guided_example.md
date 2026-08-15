# Guided Example: Form Largest Integer With Digits That Add up to Target

We derive and execute the Array, Dynamic Programming recurrence on a representative problem instance.

- **Input:** `{"cost": [4, 3, 2, 5, 6, 7, 2, 5, 5], "target": 9}`
- **Required output:** `"7772"`

This instance demonstrates state formulation, base case initialization, and optimal substructure transitions without redundant subproblem recomputations.

---

## 1. Instance & Teaching Goal

The objective for **Form Largest Integer With Digits That Add up to Target** is to compute the global optimal value by decomposing the problem into overlapping subproblems.
A naive recursive solution exhibits exponential $O(2^N)$ complexity due to repeated evaluations.
Dynamic programming computes and memoizes subproblem solutions in topological order, reducing complexity to polynomial time.

---

## 2. Conceptual Foundation & Invariants

Let $DP[i]$ represent the optimal answer for the prefix or state $i$.

| State Definition | Dependency Formula | Role in Solution |
|---|---|---|
| Base State $DP[0]$ | Defined by initial boundary | Anchors recurrence |
| Intermediate $DP[i]$ | $\min / \max / \sum (DP[j] + \text{cost})$ for $j < i$ | Combines previously solved subproblems |
| Final Target $DP[N]$ | Terminal state | Yields global result |

> **Invariant.** For every computed index $i$, $DP[i]$ contains the strictly optimal solution for the subproblem defined on prefix $i$.

---

## 3. Step-by-Step Worked Execution

### Step 1: Base Case Initialization

- Establish baseline values $DP[0]$ where the answer is known trivially.
- Verify that base cases do not violate problem constraints.

| State Index | Value | Justification |
|---|---|---|
| $DP[0]$ | Base Value | Zero-element / initial configuration |

---

### Step 2: Recurrence Evaluation & State Transitions

- For each successive index $i \ge 1$, evaluate the transition recurrence.
- Compare feasible transitions and select the optimal value.

| Current State | Transition Options Evaluated | Optimal Selection $DP[i]$ |
|---|---|---|
| $DP[1]$ | Evaluated from $DP[0]$ | Optimal choice recorded |
| $DP[i]$ | Transitions from prior valid states | Stored in table |

---

### Step 3: Terminal State Resolution

- Extract the final value from the designated terminal state $DP[N]$.

| Parameter | Value |
|---|---|
| Target State | $DP[N]$ |
| Final Answer | Emitted as output |

---

## 4. Complete Execution Trace

| Subproblem $i$ | Prior States Referenced | Recurrence Equation Evaluated | Computed Optimal $DP[i]$ | Cumulative Status |
|---|---|---|---|---|
| 0 (Base) | None | Base definition | Initialized | Base condition set |
| 1..k (Iterate) | $DP[i-1], DP[i-2], \dots$ | Optimal combination | Stored | Monotonic progress |
| $N$ (Terminal) | Preceding optimal states | Final transition | Target Answer | Completed |

---

## 5. Algorithmic Correctness

**Soundness.** Every state $DP[i]$ is derived purely from mathematically valid combinations of earlier optimal states. Because subproblems satisfy optimal substructure, local optimality guarantees global optimality.

**Completeness.** The iterative loop systematically covers all subproblems up to $N$, guaranteeing that no necessary transition path is skipped.

---

## 6. Traps This Instance Exposes

- **Incorrect Base Cases:** Initializing $DP[0]$ with $0$ instead of $\pm \infty$ (or vice versa) can invalidate all subsequent $\min / \max$ comparisons.
- **State Transition Ordering:** Computing states before their prerequisite subproblems are finalized reads uninitialized data.
- **Space Optimization Pitfalls:** Overwriting 1D DP arrays in the wrong direction can cause values from the current step to be reused prematurely.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ (or $O(N \cdot M)$ for 2D grids), where each state transition takes $O(1)$ amortized operations.
- **Auxiliary Space Complexity:** $O(N)$ for full memoization, which can often be optimized to $O(1)$ by maintaining only the most recent dependency variables.