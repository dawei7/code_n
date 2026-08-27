# Guided Example: Apply Transform Over Each Element in Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3], "fnName": "plusOne", "fnArg": null, "arrPlan": null}`
- **Required output:** `[2, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The objective is to compute `[2, 3, 4]` from `{"arr": [1, 2, 3], "fnName": "plusOne", "fnArg": null, "arrPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Mapping produces one output for every input position

The required relationship is:

$$
\texttt{transformed[i]}
=
\texttt{fn(arr[i], i)}.
$$

Unlike filtering, mapping never decides whether to keep an element. Every source position contributes exactly one result, so output length always equals input length.

The callback result replaces the source value in the new array; the source itself remains unchanged.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3], "fnName": "plusOne", "fnArg": null, "arrPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a separate result

`transformed` begins as a new empty array. The loop runs `index` from zero while `index < arr.length`.

For each index, it evaluates:

`fn(arr[index], index)`

and immediately pushes that returned integer onto `transformed`.

Because one push occurs on every iteration, the $i$-th callback result becomes the $i$-th output element.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `transformed` begins as a new empty array.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the index is supplied

Callbacks may depend only on value:

`n => n + 1`.

They may instead use both value and position:

`(n, i) => n + i`.

Passing both values supports either form. JavaScript ignores extra arguments when a function declares fewer parameters, so no branching based on callback arity is needed.

The order is important: `arr[index]` is the first argument, and `index` is the second.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3], "fnName": "plusOne", "fnArg": null, "arrPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in `Array.map`:** Directly expresses the:** - **Built-in `Array.map`:** Directly expresses the operation but is explicitly forbidden.
- **Preallocate result length:** Assign `transformed[index]` instead of pushing; same $O(n)$ bounds.
- **In-place transformation:** Saves output allocation but mutates the source and violates the new-array requirement.
- **Empty array:** Returns a new empty array without invoking `fn`.
- **Value-only callback:** The extra index argument is harmlessly ignored.
- **Index-aware callback:** Receives the correct zero-based source position.
- **Constant callback:** It still runs once per input and fills every result position.
- **Negative source values:** They are passed unchanged to `fn`; the mapping helper imposes no arithmetic assumption.
- **Repeated output values:** They remain separate positions, preserving output length.
- **Callback side effects:** They occur exactly once per source element in left-to-right order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\texttt{arr.length}$. The loop executes once per element and invokes `fn` once each time. Assuming constant-time callback work, total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
