# Guided Example: Join Two Arrays by ID

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr1": [], "arr2": [{"id": 7, "value": "only"}]}`
- **Required output:** `[{"id": 7, "value": "only"}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two arrays `arr1` and `arr2`, return a new array `joinedArray`. All the objects in each of the two inputs arrays will contain an `id` field that has an integer value.

The objective is to compute `[{"id": 7, "value": "only"}]` from `{"arr1": [], "arr2": [{"id": 7, "value": "only"}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use each id as the identity of one output object

The result contains one object per distinct `id` across both arrays. That makes a map the natural central structure: the key is `id`, and the value is the currently merged object for that identity.

The input guarantee says IDs are unique within each individual array. Therefore at most one object from `arr1` and at most one object from `arr2` can contribute to a given map entry.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr1": [], "arr2": [{"id": 7, "value": "only"}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Load arr1 as the base layer

The first loop visits every object in `arr1` and executes:

`merged.set(object.id, { ...object })`.

The object spread creates a new top-level object containing the same enumerable properties. This avoids placing the original top-level object itself in the result. At this stage, each map entry is simply the corresponding `arr1` object copied under its ID.

An object that appears only in `arr1` remains this copy through the end of merging.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first loop visits every object in `arr1` and executes:

... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Overlay arr2 after arr1

The second loop handles each `arr2` object with:

`{ ...(merged.get(object.id) || {}), ...object }`.

If the ID already exists, the existing `arr1`-based properties are spread first. The `arr2` properties are spread afterward, so a duplicate key from `arr2` overwrites the earlier value. Keys found only in the base object survive because nothing replaces them.

If the ID does not exist, `merged.get(...)` is `undefined`, so `|| {}` supplies an empty base. Spreading the `arr2` object then copies it unchanged into a new top-level object.

The new merged object is stored back under the same ID.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"id": 7, "value": "only"}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr1": [], "arr2": [{"id": 7, "value": "only"}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"id": 7, "value": "only"}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested search for matching IDs:** Avoids a map:** - **Nested search for matching IDs:** Avoids a map but can take $O(\lvert arr1\rvert\lvert arr2\rvert)$ time.
- **Sort both inputs and use two pointers:** Works in $O(N\log N)$ time and then linear merging, but mutates or copies both arrays and is more elaborate.
- **Plain object keyed by ID:** Can work for integer IDs, though `Map` avoids property-name and prototype concerns and makes key intent explicit.
- **Deep merge:** Incorrect; when both objects contain a nested property, the entire `arr2` value must replace the `arr1` value.
- **ID only in arr1:** Its copied base object reaches the result without an overlay.
- **ID only in arr2:** The empty fallback creates a copy containing exactly that object's properties.
- **Conflicting property:** The later `...object` spread from `arr2` wins.
- **Nonconflicting property:** It survives from whichever source contains it.
- **Input mutation:** Top-level input objects are not mutated, although nested values remain shared references.
- **Large object bodies:** Property-copy cost may dominate sorting, which is why the detailed bound includes $P$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P+U\log U)$. Let $N=\lvert\texttt{arr1}\rvert+\lvert\texttt{arr2}\rvert$, let $U$ be the number of unique IDs, and let $P$ be the total number of top-level properties copied across all spread operations. Expected map lookup and insertion are $O(1)$ per object. Property spreading costs $O(P)$ in total, materializing values costs $O(U)$, and sorting costs $O(U\log U)$ comparisons.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
