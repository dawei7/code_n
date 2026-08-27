# Guided Example: Get the Maximum Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [2, 4, 5, 8, 10], "nums2": [4, 6, 8, 9]}`
- **Required output:** `30`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **sorted** arrays of distinct integers `nums1` and `nums2`.

The objective is to compute `30` from `{"nums1": [2, 4, 5, 8, 10], "nums2": [4, 6, 8, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Common values are the only switching points

Both arrays are strictly increasing, and traversal within the chosen array always moves left to right. A path may switch arrays only at a value appearing in both.

Between two common values, there is no legal place to switch. A path must take the entire intervening segment from one array or the entire segment from the other. At the next common value, it can choose whichever accumulated route has the larger score and then continue on either side.

This structure lets the solution avoid constructing paths. It maintains only the best score associated with each current array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [2, 4, 5, 8, 10], "nums2": [4, 6, 8, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Merge the sorted arrays with two pointers

Pointers `i` and `j` indicate the next unprocessed values in `nums1` and `nums2`. Accumulator `f` represents the running best score for a path currently following the first array, while `g` represents the corresponding score for the second array.

If `nums1[i] < nums2[j]`, the first value occurs before the second array's next possible matching value. Because the arrays are sorted, it cannot match anything at or after `nums2[j]`. The code adds it to `f` and advances only `i`.

The symmetric case adds a smaller `nums2[j]` to `g` and advances only `j`.

This is the same ordering logic used by merging sorted lists. Every value is processed once, and equal values are detected exactly when both pointers reach them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Pointers `i` and `j` indicate the next unprocessed values in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Synchronize scores at an intersection

When `nums1[i] == nums2[j]`, both pointers identify the same switching value. A best path arriving there may have followed either array up to that point.

The source computes:

`f = g = max(f, g) + nums1[i]`

Choosing `max(f, g)` keeps the better route into the intersection. Adding the common value once respects the rule that path score sums unique visited values; the same numeric intersection must not be counted twice.

Assigning the new total to both accumulators means that after visiting the intersection, the optimal path can legally continue in either array. Both pointers advance, so the common value is consumed once from each input representation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `30` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [2, 4, 5, 8, 10], "nums2": [4, 6, 8, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `30` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming table:** It could model po:** - **Dynamic programming table:** It could model positions explicitly but wastes $O(MN)$ work or storage when only intersections matter.
- **Hash common values:** A map can locate intersections but uses extra space and ignores the advantage of sorted arrays.
- **Segment-sum formulation:** Sum values between intersections separately, add the larger segment at each common value, and add the intersection once. It is equivalent to the two accumulators.
- **No common values:** The accumulators become the two complete array sums, and the larger is returned.
- **Common first value:** Both initial scores synchronize immediately at that value.
- **Common last value:** The better complete prefix is selected at the final intersection.
- **One array exhausted early:** Its score stops changing while the other route consumes its remaining suffix.
- **Strictly increasing arrays:** There are no duplicates within one array, so a common value is encountered only once per side.
- **Common-value counting:** The intersection value is added once, never once per array.
- **Switching repeatedly:** Synchronizing both accumulators at every intersection permits any legal sequence of switches.
- **Large totals:** Exact Python integers avoid overflow; modulo is applied only after optimization is complete.
- **Modulo during traversal:** It is unsafe because modular residues do not preserve which true sum is larger.
- **Positive values:** Every remaining suffix value helps its route; there is no decision to skip values within a traversal.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let $M$ and $N$ be the two array lengths. Every loop iteration advances `i`, `j`, or both. Neither pointer moves backward, so at most $M+N$ values are processed.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
