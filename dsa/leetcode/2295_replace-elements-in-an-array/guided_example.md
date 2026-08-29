# Guided Example: Replace Elements in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 4, 6], "operations": [[1, 3], [4, 7], [6, 1]]}`
- **Required output:** `[3, 2, 7, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` that consists of `n` **distinct** positive integers. Apply `m` operations to this array, where in the $i^{\text{th}}$ operation you replace the number $\text{operations}[i][0]$ with $\text{operations}[i][1]$.

The objective is to compute `[3, 2, 7, 1]` from `{"nums": [1, 2, 4, 6], "operations": [[1, 3], [4, 7], [6, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Avoid searching the array for every operation

A direct implementation could scan `nums` to locate the old value for each replacement. With up to `10^5` values and operations, that could take quadratic time.

Because all current values are distinct, each value identifies exactly one array index. The dictionary comprehension

`d = {x: i for i, x in enumerate(nums)}`

records that index for every initial value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 4, 6], "operations": [[1, 3], [4, 7], [6, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply one replacement in constant expected time

For operation `[x,y]`, the contract guarantees `x` currently exists and `y` currently does not.

`d[x]` retrieves the unique index holding `x`. The code writes `y` into that position:

`nums[d[x]] = y`.

It then records the new lookup:

`d[y] = d[x]`.

After these statements, future operations can find `y` at the same index without scanning the list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why operation order is preserved

Operations must be applied sequentially because a value introduced by one may be replaced later. The loop processes `operations` in input order and updates the dictionary immediately.

For `[1,3]` followed later by `[3,2]`, the first operation creates `d[3]` at the old position of one. The later operation retrieves that updated position and replaces it correctly.

The method never attempts to batch independent-looking replacements, so chains and reintroduced values follow their exact temporal semantics.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 2, 7, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 4, 6], "operations": [[1, 3], [4, 7], [6, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 2, 7, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Delete the old key:** Saving `idx=d[x]`, deleting `x`, and inserting `y` preserves correctness while keeping map size `O(n)`.
- **Scan for each old value:** It avoids a dictionary but can take `O(nm)` time.
- **Value-to-value chain map:** Deferred replacements are harder because output positions and temporal reintroductions must still be resolved.
- **Direct-address array:** Values are bounded by `10^6`, but it allocates for the whole domain rather than current and historical keys.
- **Replacement chain:** Immediate mapping updates let a newly introduced value be replaced later.
- **Reintroducing an old value:** Assigning it as `y` overwrites its stale mapping with the new current index.
- **New value has a stale key:** Current absence is sufficient; the dictionary assignment corrects that key.
- **Distinctness:** It guarantees one current index per value and removes ambiguity.
- **One element:** Every operation simply changes index zero and updates its mapping.
- **No position movement:** Only values change, so unaffected elements retain their order.
- **Expected dictionary time:** The linear time bound uses ordinary expected hash-table behavior.
- **Input mutation:** The returned object is the modified original `nums` list.
- **Operations preservation:** `operations` is read sequentially and never changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let `n` be the array length and `m` the number of operations. Building the initial dictionary takes `O(n)` expected time. Each operation performs expected-constant-time dictionary accesses and one list assignment, so total expected time is `O(n+m)`.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
