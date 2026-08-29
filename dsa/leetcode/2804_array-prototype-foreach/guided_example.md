# Guided Example: Array Prototype ForEach

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3], "callback": "double", "context": {"context": true}}`
- **Required output:** `[2, 4, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write your version of method `forEach` that enhances all arrays such that you can call the `array.forEach(callback, context)` method on any array and it will execute `callback` on each element of the array. Method `forEach` should not return anything.

The objective is to compute `[2, 4, 6]` from `{"arr": [1, 2, 3], "callback": "double", "context": {"context": true}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Recreate the core callback contract.** The method is installed as `Array.prototype.forEach`, so an array can call it through ordinary method syntax. For each index from zero upward, it invokes `callback` with three positional arguments: the value at that index, the index itself, and the array being traversed. It also uses the optional `context` as the callback's `this` value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3], "callback": "double", "context": {"context": true}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The implementation is a direct index loop:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`for (let index = 0; index < this.length; index++)`

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3], "callback": "double", "context": {"context": true}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Snapshot length first:** Store `const length = this.length` before looping. This matches native behavior for appended elements more closely because later growth does not expand the traversal.
- **Skip holes with `index in this`:** Adding a property-existence check avoids invoking the callback for missing sparse indices and better matches native `forEach`.
- **Use a `for...of` loop:** It easily supplies values but not the exact index and mutation semantics without maintaining additional state, and it also visits sparse-array holes as undefined through the array iterator.
- **Ordinary callback with context:** `call` makes the provided object the callback's `this`, subject to strict-mode and primitive-boxing language rules.
- **Arrow callback:** Its lexical `this` cannot be changed. It still receives value, index, and array as positional arguments.
- **Callback returns a value:** The method discards it and eventually returns undefined; use `map` when transformed results must be collected.
- **Empty array:** The condition is false immediately, so the callback is never invoked.
- **Sparse array:** The exact source invokes the callback for a hole with an undefined value, unlike the native method.
- **Deleting an upcoming element:** The loop still reaches that numeric index and supplies undefined unless the length was shortened enough to end traversal.
- **Appending elements:** Because length is reread, appended elements may be visited. Continuous appending can make the loop nonterminating.
- **Shrinking length:** The next condition observes the shorter value and can stop before indices that existed initially.
- **Thrown callback exception:** Nothing catches it, so traversal stops immediately and the exception propagates to the caller.
- **Overwriting the native method:** Other code in the same realm now receives these simplified semantics. This is acceptable in the isolated judge but unsafe as a general polyfill strategy.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the stable array length. The loop runs $n$ times and performs constant traversal overhead per iteration, so its own time is $O(n)$. The callback can perform arbitrary work; if invocation $i$ costs $C_i$, a fuller bound is $O(n + \sum C_i)$. Standard analysis excludes callback internals and reports $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
