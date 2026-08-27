# Guided Example: Filter Elements from Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [0, 10, 20, 30], "fnName": "greaterThan", "fnArg": 10, "arrPlan": null}`
- **Required output:** `[20, 30]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr` and a filtering function `fn`, return a filtered array `filteredArr`.

The objective is to compute `[20, 30]` from `{"arr": [0, 10, 20, 30], "fnName": "greaterThan", "fnArg": 10, "arrPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filtering decides inclusion without transforming the value

For every source position $i$, callback `fn(arr[i], i)` decides whether the original element belongs in the result.

The callback's return value is interpreted through JavaScript truthiness:

$$
\text{include }\texttt{arr[i]}
\quad\Longleftrightarrow\quad
\texttt{Boolean(fn(arr[i], i))}=\texttt{true}.
$$

If included, the output receives `arr[i]` itself—not the callback's result. This distinguishes filtering from mapping.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [0, 10, 20, 30], "fnName": "greaterThan", "fnArg": 10, "arrPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a new output array

`filtered` starts empty. The indexed loop visits every original position from zero through `arr.length - 1`.

At each position, the code evaluates the callback exactly once:

`if (fn(arr[index], index))`.

JavaScript's `if` condition automatically applies Boolean coercion. If the result is truthy, `filtered.push(arr[index])` appends the original source value. Otherwise, the loop advances without appending.

The source is never overwritten or shortened.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `filtered` starts empty.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why both value and index are passed

Some predicates depend only on the element, such as `n => n > 10`. Others depend on where the element appears, such as `(n, i) => i === 0`.

The exact call supplies both arguments in the required order:

- first: current value;
- second: current numeric index.

A JavaScript callback declaring only one parameter simply ignores the extra index. Supplying both therefore supports both allowed forms without inspecting `fn.length`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[20, 30]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [0, 10, 20, 30], "fnName": "greaterThan", "fnArg": 10, "arrPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[20, 30]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in `Array.filter`:** Provides the same c:** - **Built-in `Array.filter`:** Provides the same core behavior but is explicitly forbidden.
- **Preallocated output:** Store accepted values at a write pointer and truncate; same $O(n)$ bounds with more bookkeeping.
- **In-place compaction:** Can use $O(1)$ extra space but mutates the source, unlike the exact solution.
- **Empty array:** No callback calls occur and a new empty array is returned.
- **All predicates false:** The output stays empty.
- **All predicates true:** Every original value appears in source order.
- **Index-dependent callback:** Passing the numeric index is required for correct decisions.
- **Non-Boolean callback result:** Ordinary JavaScript truthiness determines inclusion.
- **Falsy source value:** It may still be kept when the callback result is truthy.
- **Callback side effects:** They occur exactly once per element from left to right.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\texttt{arr.length}$. The loop performs $n$ callback calls and constant additional work per element. Assuming `fn` is $O(1)$, time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
