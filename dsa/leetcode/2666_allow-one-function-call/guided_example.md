# Guided Example: Allow One Function Call

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operation": "sum", "calls": [[1, 2, 3], [2, 3, 6]]}`
- **Required output:** `[{"calls": 1, "value": 6}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called at most once.

The objective is to compute `[{"calls": 1, "value": 6}]` from `{"operation": "sum", "calls": [[1, 2, 3], [2, 3, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A closure remembers whether the opportunity was used

`once(fn)` returns a wrapper that may forward at most one invocation to `fn`.

Local Boolean `called` begins false and is captured by the returned function. Because it belongs to the wrapper's lexical environment, it persists across every later call.

The entire policy is:

- when `called` is false, mark it true and invoke `fn`;
- when it is true, do nothing.

Falling off a JavaScript function without a return statement produces `undefined`, exactly the required later-call result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operation": "sum", "calls": [[1, 2, 3], [2, 3, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Forward the first call's arguments

The wrapper accepts `...args`. Rest syntax gathers every supplied positional argument into an array in order.

On the first call:

`fn(...args)`

spreads that array back into positional arguments for the original function.

Thus, a call `onceFn(1,2,3)` behaves like `fn(1,2,3)` on its one permitted execution. The wrapper does not know or need to know the original function's arity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The wrapper accepts `...args`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark before invoking

Inside the first-call branch, the exact order is:

1. `called = true`;
2. `return fn(...args)`.

Setting the flag before running `fn` matters for two subtle cases.

First, `fn` might synchronously call the wrapper again. The recursive call sees `called === true` and is suppressed rather than invoking `fn` recursively without limit.

Second, `fn` might throw. The first call was still an attempted and actual call to `fn`. Because the flag was already set, a later wrapper call does not retry it.

This matches “called at most once” more robustly than setting the flag only after successful return.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"calls": 1, "value": 6}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operation": "sum", "calls": [[1, 2, 3], [2, 3, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"calls": 1, "value": 6}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Cache and return the first result:** Implement:** - **Cache and return the first result:** Implements a different contract because later calls should return undefined.
- **Set flag after `fn` returns:** Allows reentrant calls or retries after an exception, violating strict at-most-once semantics.
- **Numeric call counter:** Works but stores more state than a Boolean needs.
- **First call returns undefined:** It still consumes the one allowed invocation.
- **First call throws:** The error propagates and later calls remain suppressed.
- **Reentrant first call:** Pre-setting the flag prevents a second underlying invocation.
- **Several arguments:** Rest and spread preserve their order.
- **No arguments:** Empty argument list forwards correctly.
- **Independent wrappers:** Each factory call owns a separate flag.
- **Method receiver:** The exact source forwards arguments but not dynamic `this`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Persistent wrapper state is one Boolean and one reference to `fn`, so retained space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
