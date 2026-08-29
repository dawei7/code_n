# Guided Example: Curry

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"fnName": "sum", "arity": 3, "inputs": [[1], [2], [3]], "inputPlan": null}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn`, return a **curried** version of that function.

The objective is to compute `6` from `{"fnName": "sum", "arity": 3, "inputs": [[1], [2], [3]], "inputPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Collect arguments across an unknown number of calls

A curried wrapper may receive the original function's parameters in any grouping:

- one at a time;
- several at once;
- empty batches between nonempty batches;
- all at once.

The original function should execute only when the total number of collected arguments reaches its declared arity `fn.length`.

The exact solution represents the history as immutable linked chunks rather than repeatedly copying one growing argument array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"fnName": "sum", "arity": 3, "inputs": [[1], [2], [3]], "inputPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `fn.length` means

For a function with explicitly declared parameters, `fn.length` is its declared arity. A function `function sum(a, b, c)` has length three; `function life()` has length zero.

The problem guarantees explicitly defined parameters and a total supplied argument count matching this arity. Therefore, counting received positional arguments tells the wrapper when it has enough information to call `fn`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: `extend` creates the next curried stage

Helper `extend(previous, count)` returns a function named `curried`.

- `previous` points to the most recent stored argument chunk, or null at the beginning.
- `count` is the total number of arguments collected across that linked history.

Calling `extend(null, 0)` creates the initial wrapper with no history.

Every returned stage closes over its own `previous` and `count`. This makes its history persistent and private.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"fnName": "sum", "arity": 3, "inputs": [[1], [2], [3]], "inputPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated array concatenation:** Simpler but can take $O(n^2)$ total copying when arguments arrive one at a time.
- **One mutable collection:** Linear for a single chain but makes branching from a partial curried function unsafe.
- **`Function.bind` accumulation:** Can implement partial application but may obscure arity and batching behavior.
- **Empty argument batch:** It advances the call chain without increasing the collected count.
- **All arguments at once:** Completion occurs on the first invocation.
- **One argument per call:** Nodes form a length-$n$ chain and are flattened once.
- **Zero-arity function:** The first empty invocation calls `fn()`.
- **Branched partial application:** Immutable linked nodes let branches share history safely.
- **Argument order:** Backward node traversal must be reversed before invoking `fn`.
- **Receiver context:** The exact `fn(...args)` call does not forward the curried wrapper's `this` because the contract is argument-based.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+p)$. Let $n$ be the total number of supplied arguments and $p$ the number of curried invocations, including empty calls.
- **Auxiliary Space Complexity:** $O(n + p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
