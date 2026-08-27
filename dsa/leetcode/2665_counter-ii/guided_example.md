# Guided Example: Counter II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"init": 5, "calls": ["increment", "reset", "decrement"]}`
- **Required output:** `[6, 5, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function `createCounter`. It should accept an initial integer `init`. It should return an object with three functions.

The objective is to compute `[6, 5, 4]` from `{"init": 5, "calls": ["increment", "reset", "decrement"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One object exposes three operations on shared private state

`createCounter(init)` must return an object with methods that all observe and change the same current value.

The solution declares:

`let current = init`

inside the factory and returns three functions that close over both `current` and `init`.

Even after `createCounter` returns, those lexical bindings remain alive because the methods reference them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"init": 5, "calls": ["increment", "reset", "decrement"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep initial and current values conceptually separate

`init` is the permanent reset target. `current` is the mutable state after operations.

Increment and decrement change only `current`. Reset assigns `init` back into `current` but never changes `init` itself.

If the implementation mutated the sole initial binding without retaining its original value, reset would no longer know where to return.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `init` is the permanent reset target.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Increment before returning

The increment method executes:

`current += 1`

then returns `current`.

This matches “increases the current value by one and then returns it.” With initial five, the first increment returns six, not five.

Using postfix `return current++` would return the old value and violate this version of the counter contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 5, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"init": 5, "calls": ["increment", "reset", "decrement"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 5, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Class with a field:** Models the same state bu:** - **Class with a field:** Models the same state but exposes or requires receiver-based access unless private fields are used.
- **Object with public `current`:** Simpler but allows external mutation and weaker encapsulation.
- **Postfix increment:** Returns the old value and is wrong for this contract unless rewritten.
- **Repeated reset:** Always returns the original `init`.
- **Increment after reset:** Starts from `init` again.
- **Negative initial value:** Arithmetic behavior remains unchanged.
- **No calls:** The object is created with hidden state but produces no outputs.
- **Detached method:** Still works because it closes over state rather than relying on `this`.
- **Multiple counters:** Each factory call has independent bindings.
- **Shared methods:** Within one object, all three closures reference the same mutable `current`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Creating a counter allocates one result object, three function closures, and two captured numeric bindings, all $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
