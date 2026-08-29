# Guided Example: To Be Or Not To Be

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"val": 5, "method": "toBe", "other": 5}`
- **Required output:** `{"value": true, "error": null}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function `expect` that helps developers test their code. It should take in any value `val` and return an object with the following two functions.

The objective is to compute `{"value": true, "error": null}` from `{"val": 5, "method": "toBe", "other": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Capture the actual value in a tiny expectation object

Calling `expect(val)` returns an object with two methods.

Both methods are closures: they retain access to the original `val` even after `expect` has returned.

The caller then supplies an `expected` value to either `toBe` or `notToBe`. The methods implement opposite assertions over the same captured actual value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"val": 5, "method": "toBe", "other": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: `toBe` requires strict equality

The condition is `val !== expected`.

If that inequality is true, the assertion failed and the method throws `new Error("Not Equal")`.

Otherwise strict equality holds and the method returns true.

There is no false return path: a failed assertion throws, while a successful assertion returns true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: `notToBe` requires strict inequality

The second method checks `val === expected`.

Equality means the negative assertion failed, so it throws `new Error("Equal")`. If the values differ strictly, it returns true.

Together, the two methods are logical complements with different required failure messages.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"value": true, "error": null}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"val": 5, "method": "toBe", "other": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"value": true, "error": null}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Loose equality:** Incorrect because it coerces types such as number 5 and string `"5"`.
- **Deep equality:** Answers a different question for objects and arrays.
- **Return false on failure:** Incorrect because the contract requires throwing.
- **Throw a string:** Produces a different thrown type from the exact `Error` source.
- **Different primitive types:** Strict comparison treats them as unequal.
- **Same object reference:** `toBe` succeeds.
- **Structurally equal different objects:** `toBe` throws because identity differs.
- **`NaN`:** Is not strictly equal to itself.
- **Positive and negative zero:** Are strictly equal.
- **Null and undefined:** Are strictly unequal.
- **Repeated method calls:** Use the same captured actual value and have no internal state changes.
- **Exact messages:** `toBe` uses `Not Equal` and `notToBe` uses `Equal`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Creating the expectation object and two closures takes $O(1)$ time and space. Each method performs one strict comparison and either returns or creates one Error, all $O(1)$ under the ordinary fixed-size value/reference model.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
