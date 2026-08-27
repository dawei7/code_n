# Guided Example: Group By

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"array": [5, 2, 3, 8, 1, 4], "fnName": "parity", "fnArg": null, "arrayPlan": null}`
- **Required output:** `{"odd": [5, 3, 1], "even": [2, 8, 4]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write code that enhances all arrays such that you can call the `array.groupBy(fn)` method on any array and it will return a **grouped** version of the array.

The objective is to compute `{"odd": [5, 3, 1], "even": [2, 8, 4]}` from `{"array": [5, 2, 3, 8, 1, 4], "fnName": "parity", "fnArg": null, "arrayPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One callback result chooses one output bucket

For every source item $x$, callback `fn(x)` returns the string key of the group that should contain $x$.

The result is an object whose relationship is:

$$
\texttt{groups[key]}
=
\text{all source items whose callback result is }\texttt{key}.
$$

The solution constructs this relationship in one left-to-right pass. It does not need to know all possible keys in advance.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"array": [5, 2, 3, 8, 1, 4], "fnName": "parity", "fnArg": null, "arrayPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Attach one shared method to arrays

The implementation defines `Array.prototype.groupBy` as a normal function. Any ordinary array can find this method through its prototype chain.

When called as `array.groupBy(fn)`, the normal function receives the array as `this`. An arrow function would not work reliably because it would capture lexical `this` rather than the receiver.

The method reads source items and returns a separate grouping object. It never reorders or mutates the source array.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The implementation defines `Array.prototype.groupBy` as a no... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Create a bucket on first use

`groups` begins as an empty object. For each `item`:

1. evaluate `const key = fn(item)`;
2. determine whether `groups` already has its own property for that key;
3. create an empty array if this is the first occurrence;
4. append `item` to the bucket.

The callback is invoked exactly once per source item. Its result is reused for the membership check and lookup rather than recomputed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"odd": [5, 3, 1], "even": [2, 8, 4]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"array": [5, 2, 3, 8, 1, 4], "fnName": "parity", "fnArg": null, "arrayPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"odd": [5, 3, 1], "even": [2, 8, 4]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`reduce` construction:** Can build the same ob:** - **`reduce` construction:** Can build the same object but is no more efficient and adds accumulator callback syntax.
- **Use a `Map`:** Avoids prototype-name concerns naturally, but the contract requires an object result.
- **Plain assignment for new keys:** Usually works but mishandles special names such as `__proto__` on ordinary objects.
- **Empty array:** The loop performs no callback calls and returns an empty object.
- **All items share one key:** One bucket receives every item in source order.
- **Every item has a unique key:** The result has $n$ one-element buckets.
- **Key `"toString"`:** Own-property checking distinguishes the new group from the inherited method.
- **Key `"__proto__"`:** `Object.defineProperty` safely creates a data property instead of changing the result's prototype.
- **Object or array items:** Buckets store the original references without cloning.
- **Callback order:** `fn` is called once per item from left to right.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop visits every item once. Assuming `fn` and property lookup are $O(1)$, total time is expected $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
