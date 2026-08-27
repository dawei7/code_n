# Guided Example: Find the Difference of Two Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 3], "nums2": [2, 4, 6]}`
- **Required output:** `[[1, 3], [4, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two **0-indexed** integer arrays `nums1` and `nums2`, return *a list* `answer` *of size* `2` *where:*

The objective is to compute `[[1, 3], [4, 6]]` from `{"nums1": [1, 2, 3], "nums2": [2, 4, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The requested results are mathematical set differences

The output cares about distinct values, not about how many times each value appears. The first result must contain every value that occurs in `nums1` and does not occur in `nums2`. In mathematical notation, that is

$$
S_1 \setminus S_2,
$$

where `S_1` and `S_2` are the sets of values appearing in the two arrays. The second result reverses the direction and is `S_2 \setminus S_1`. These two differences are not interchangeable: a value unique to the first array belongs only in the first output list, while a value unique to the second belongs only in the second.

Python's `set` type directly represents the two facts the problem needs: each value is stored only once, and membership can normally be tested in constant time. The exact solution first constructs both sets with

`s1, s2 = set(nums1), set(nums2)`.

During construction, duplicates disappear automatically. For instance, `set([1, 2, 3, 3])` contains only `1`, `2`, and `3`. This is not accidental data loss; it exactly implements the word “distinct” in the output contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 3], "nums2": [2, 4, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute each direction separately

The expression `s1 - s2` creates a new set containing values that belong to `s1` but not to `s2`. It does not mutate either original set. Similarly, `s2 - s1` creates values present only in the second input's set.

The return statement is

`[list(s1 - s2), list(s2 - s1)]`.

The outer list therefore always has exactly two entries. Position zero is the first directional difference, and position one is the second. Each difference set is converted to a list because the required return type is a list of lists rather than a pair of set objects.

The conversion does not sort the values. Set iteration order is not a promised numeric or input order, so the lists may appear in any order. That behavior is allowed explicitly by the problem. A caller or judge must compare each inner list as an unordered collection of distinct values rather than expect a particular arrangement such as ascending order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression `s1 - s2` creates a new set containing values... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every returned value belongs

Take any value `x` in the first returned list. It came from `s1 - s2`. By the definition of set subtraction, `x` is in `s1` and is not in `s2`. Being in `s1` means it appears at least once in `nums1`. Not being in `s2` means it never appears in `nums2`. Thus, `x` satisfies exactly the rule for `answer[0]`.

The same reasoning with the sets reversed proves that every value in the second returned list appears in `nums2` and not in `nums1`. Therefore, the method never includes a shared value on either side and never places a one-sided value in the wrong side.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 3], [4, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 3], "nums2": [2, 4, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 3], [4, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested scans with a result set:** For each val:** - **Nested scans with a result set:** For each value in one array, scan the other array to decide membership and insert qualifying values into a set, then repeat in reverse. This is logically correct but takes `O(nm)` time in the worst case.
- **Frequency arrays over the bounded value range:** Because values lie between `-1000` and `1000`, two boolean arrays with an offset could mark presence and then enumerate the domain. This is also efficient for these constraints, but it depends on the small numeric range and normally emits values in sorted domain order; hash sets express the actual set operation more directly.
- **Sort and use two pointers:** Sorting copies of both arrays would allow duplicate skipping and a linear merge afterward. Its total time is `O(n \log n + m \log m)`, and sorting the original lists in place would modify caller data unless copies were made.
- **Symmetric difference:** `s1 ^ s2` finds every value that appears in exactly one set, but it loses which input owned the value. The required answer has two directional lists, so two subtractions are necessary unless the symmetric difference is partitioned again.
- **Intersection removal by mutating sets:** One could calculate the intersection and remove it from both sets. That adds a separate structure or mutates the input-derived sets, whereas direct subtraction already returns the required two results clearly.
- **Duplicates within one input:** Set construction collapses them. A value exclusive to one side appears once in its output no matter how many times it occurs in that source array.
- **Different duplicate counts across inputs:** If a value appears at least once in both arrays, it appears in neither output. The method compares presence, not multiplicity.
- **Identical sets of values:** Both differences are empty, so the method returns `[[], []]` even if the arrays have different orders or repetition counts.
- **No overlap:** Every distinct value of `nums1` appears in the first list, and every distinct value of `nums2` appears in the second.
- **One side's values are a subset of the other's:** The subset side's directional difference is empty; the other side contains only its additional distinct values.
- **Negative numbers and zero:** Python integer sets handle them without an offset or separate branch.
- **Arbitrary output order:** Converting a set with `list(...)` does not promise sorted order. This is contract-compliant; sorting would add unnecessary `O(k \log k)` work for an output of size `k`.
- **Outer-list position:** Even though inner order is arbitrary, the two inner lists cannot be swapped. Index `0` always describes values exclusive to `nums1`, and index `1` always describes values exclusive to `nums2`.
- **Input preservation:** Neither `set(nums1)` nor subtraction changes the original arrays. The result can be computed safely even if the caller retains and later reuses them.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let `n = len(nums1)` and `m = len(nums2)`. Constructing `s1` performs `n` expected constant-time hash insertions, and constructing `s2` performs `m`. Their combined expected time is `O(n + m)`.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
