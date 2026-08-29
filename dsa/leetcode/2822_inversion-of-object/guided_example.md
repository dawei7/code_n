# Guided Example: Inversion of Object

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj": {"a": "1", "b": "2", "c": "3", "d": "4"}}`
- **Required output:** `{"1": "a", "2": "b", "3": "c", "4": "d"}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an object or an array `obj`, return an inverted object or array `invertedObj`.

The objective is to compute `{"1": "a", "2": "b", "3": "c", "4": "d"}` from `{"obj": {"a": "1", "b": "2", "c": "3", "d": "4"}}` while avoiding redundant calculations and unnecessary overhead.

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

**Invert from original values to original keys.** Each own entry of the input has an original key and a string value. In the output, that value becomes a property name. If only one original key had the value, the output value is that key string. If several original keys shared it, the output value is an array of all corresponding key strings.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj": {"a": "1", "b": "2", "c": "3", "d": "4"}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Arrays follow the same rule because `Object.entries(array)` exposes their present indices as string keys such as `"0"` and `"1"`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Use a Map while grouping.** The method creates `inverted = new Map()`. A Map is useful during construction because it supports direct string-key lookup, distinguishes absence through `has`, preserves insertion order, and safely accepts strings such as `"__proto__"` without interacting with object prototypes.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"1": "a", "2": "b", "3": "c", "4": "d"}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj": {"a": "1", "b": "2", "c": "3", "d": "4"}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"1": "a", "2": "b", "3": "c", "4": "d"}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Plain object accumulator:** It can group values directly, but naive assignment is vulnerable to special names such as `"__proto__"` and requires careful own-property checks.
- **Null-prototype accumulator:** `Object.create(null)` avoids inherited-name collisions and can replace the Map, though final conversion and duplicate shape logic are still needed.
- **Always store arrays first:** Group every value into an array and convert length-one arrays to strings afterward. This simplifies updates but requires a second normalization pass.
- **Exactly one occurrence:** The output value is the original key string, not a one-element array.
- **Two occurrences:** The second occurrence converts the stored string into an array in the correct order.
- **Three or more occurrences:** Later keys append to the existing array without nesting it.
- **Array input:** Present numeric indices become strings. Sparse holes, if any, do not appear in `Object.entries`.
- **String value `"__proto__"`:** Map grouping and `Object.fromEntries` create a safe own property rather than mutating the prototype.
- **Integer-like object keys:** JavaScript enumeration may order them numerically before other strings; the output duplicate array follows actual `Object.entries` order.
- **Inherited properties:** They are ignored, as appropriate for JSON data.
- **Input preservation:** No input property or array element is changed.
- **Non-string values outside the contract:** Object materialization would coerce keys and could merge values that were distinct in a Map, so the guarantee is essential.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of enumerable input entries. `Object.entries` materializes an array containing $n$ pairs, taking $O(n)$ time and $O(n)$ space under a unit-cost string-reference model. The loop performs an expected $O(1)$ Map lookup/update per entry, and each original key is appended at most once.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
