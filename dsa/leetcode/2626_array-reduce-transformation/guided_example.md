# Guided Example: Array Reduce Transformation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4], "fnName": "sum", "init": 0}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, a reducer function `fn`, and an initial value `init`, return the final result obtained by executing the `fn` function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

The objective is to compute `10` from `{"nums": [1, 2, 3, 4], "fnName": "sum", "init": 0}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Carry one accumulated value from left to right

A reduction converts an array into one final value. The value after processing one element becomes the input state for processing the next element.

The exact recurrence is:

$$
\begin{aligned}
A_0&=\texttt{init},\\
A_{i+1}&=\texttt{fn}(A_i,\texttt{nums[i]}).
\end{aligned}
$$

After all $n$ elements, the required answer is $A_n$.

The implementation mirrors this definition directly. Variable `result` stores the current accumulator and starts as `init`. For every source `value` in order, the assignment

`result = fn(result, value)`

replaces the accumulator with the next recurrence value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4], "fnName": "sum", "init": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the initial value is not an array element

`init` is supplied separately and is the accumulator before any element is processed. It is not automatically added, multiplied, or otherwise combined except through the callback.

For a sum callback with zero initialization, it acts like an additive identity. For a sum-of-squares callback with initialization 100, the first call is `fn(100, nums[0])`, so 100 remains part of the computation.

The reduction helper must not guess what `init` means. Only `fn` defines how accumulator and current element combine.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Evaluation order is part of the contract

The array is processed from index zero upward. In general:

$$
\texttt{fn}(\texttt{fn}(\texttt{init},a),b)
$$

need not equal:

$$
\texttt{fn}(\texttt{fn}(\texttt{init},b),a).
$$

A reducer can subtract, concatenate digits, build a string, or make any order-sensitive calculation. Therefore, reversing the array, grouping calls, or processing elements concurrently could change the result.

`for (const value of nums)` follows array iteration order and gives exactly the sequential left fold required by the statement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4], "fnName": "sum", "init": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Built-in `Array.reduce`:** It expresses the operation directly but is explicitly forbidden.
- **Indexed `for` loop:** Equivalent and makes the index available, though this callback contract needs only accumulator and value.
- **Recursion:** Can express the recurrence but adds $O(n)$ call-stack space and risks stack overflow.
- **Empty array:** The loop makes no callback calls and returns `init`.
- **Nonzero initial value:** It is the first callback's accumulator, not an extra array element.
- **Non-associative reducer:** Left-to-right order must be preserved.
- **Callback returning zero:** Zero must replace the accumulator normally; truthiness is irrelevant.
- **Single element:** The answer is exactly `fn(init, nums[0])`.
- **Input preservation:** The source array is never modified.
- **Side-effecting callback:** It is invoked exactly once per element in source order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\texttt{nums.length}$. The loop visits every element once and performs one callback invocation per element. Assuming each callback call is $O(1)$, total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
