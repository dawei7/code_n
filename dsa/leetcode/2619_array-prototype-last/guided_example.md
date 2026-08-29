# Guided Example: Array Prototype Last

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [null, {}, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write code that enhances all arrays such that you can call the `array.last()` method on any array and it will return the last element. If there are no elements in the array, it should return `-1`.

The objective is to compute `3` from `{"nums": [null, {}, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Place one shared method where every array can find it

JavaScript arrays inherit from `Array.prototype`. When code evaluates `arr.last` and `arr` has no own property named `last`, JavaScript follows the array's prototype link and finds the method defined by the solution.

Assigning

`Array.prototype.last = function() { ... }`

therefore enhances every ordinary array without copying a separate function into every instance. Arrays that already exist and arrays created later both use the same prototype method.

This is the exact interface requested by the problem: the caller invokes `array.last()` rather than passing an array to a standalone helper.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [null, {}, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the method is a normal function

Inside a method call such as `arr.last()`, a normal function receives `arr` as its dynamic `this` value. The body can consequently inspect `this.length` and index `this`.

An arrow function would be wrong here because arrow functions do not create their own `this` binding. They capture `this` from the surrounding lexical scope, which would not reliably be the calling array.

The normal function syntax is therefore not cosmetic. It is what connects the shared prototype method to the particular array on which it is invoked.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Distinguish an empty array by length

The last valid zero-based index of a nonempty array of length $n$ is $n-1$. The method uses the conditional expression:

`this.length === 0 ? -1 : this[this.length - 1]`.

If length is zero, index negative one is not a normal last-element lookup in JavaScript. Array bracket access with `-1` asks for a property literally named `"-1"`, not an element counted from the end. Returning the required sentinel explicitly avoids that trap.

If the array is nonempty, `this.length - 1` is a valid final index, and direct bracket access returns that element.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [null, {}, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`Array.prototype.at(-1)`:** It provides end-relative indexing, but a separate length check is still needed to distinguish an empty array from a legitimate final undefined-like value.
- **`pop()`:** It returns the last element but removes it, violating the expected query behavior.
- **`slice(-1)[0]`:** Non-mutating but allocates a new one-element array and is needlessly indirect.
- **Arrow-function method:** It captures lexical `this` and will not reliably refer to the receiving array.
- **Empty array:** Return `-1` based on length.
- **Final `null`:** Return null, not the empty sentinel.
- **Final false or zero:** Falsy values are real elements and must be returned unchanged.
- **Nested final array or object:** Return the original reference without copying or serialization.
- **Repeated calls:** They do not mutate the array and therefore remain stable.
- **Prototype collision:** Relevant in production design, but extending `Array.prototype` is explicitly required by this challenge.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Reading `length`, subtracting one, and accessing one array index are constant-time operations. Each call to `last()` therefore takes $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
