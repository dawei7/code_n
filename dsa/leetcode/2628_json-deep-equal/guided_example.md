# Guided Example: JSON Deep Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"o1": {"x": 1, "y": 2}, "o2": {"x": 1, "y": 2}}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two values `o1` and `o2`, return a boolean value indicating whether two values, `o1` and `o2`, are **deeply equal**.

The objective is to compute `true` from `{"o1": {"x": 1, "y": 2}, "o2": {"x": 1, "y": 2}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare values according to their structural category

Deep equality is recursive. Two outer containers are equal only when their corresponding contents are deeply equal.

The solution distinguishes four relevant JSON situations in a careful order:

1. values already equal by `===`;
2. null or non-object values that failed strict equality;
3. arrays;
4. ordinary objects.

This order matters because JavaScript reports `typeof null` as `"object"`, and arrays also have object type even though their comparison rules require order and length.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"o1": {"x": 1, "y": 2}, "o2": {"x": 1, "y": 2}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Accept strict equality immediately

The first line is:

`if (o1 === o2) return true`.

This handles equal primitives directly:

- the same number;
- the same string;
- the same Boolean;
- null with null.

It also accepts two references to the exact same array or object. A value is necessarily deeply equal to itself, so traversing it would be wasted work.

The inputs come from valid JSON, so problematic primitive cases such as `NaN` do not occur.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject incompatible leaves

If strict equality failed, the code checks whether either value is null or either type is not `"object"`.

At this point, any primitive pair is unequal by definition because it already failed `===`. A primitive cannot be deeply equal to a container. Null must be handled explicitly because its type string misleadingly says object.

Returning false here ensures recursion proceeds only when both values are non-null containers.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"o1": {"x": 1, "y": 2}, "o2": {"x": 1, "y": 2}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Serialize both values:** Plain `JSON.stringify` is sensitive to object key order, so logically equal objects can produce different strings.
- **Iterative stack:** Avoid recursive call-stack limits while applying the same category checks.
- **Lodash `isEqual`:** General-purpose but explicitly forbidden and broader than JSON semantics.
- **Both values null:** The initial strict-equality branch returns true.
- **One null:** The explicit null guard returns false before object traversal.
- **Array versus object:** `Array.isArray` distinguishes their structural categories.
- **Different object key order:** Lookup by key still returns true when values match.
- **Same key count but different keys:** The own-property check detects the mismatch.
- **Number versus numeric string:** Strict equality rejects them.
- **Maximum nesting:** Recursive depth follows the JSON tree and may motivate an iterative implementation in runtimes with small stacks.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the total number of primitive values, array elements, and object keys across the compared structures. In the worst case, each corresponding node and key is examined once, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
