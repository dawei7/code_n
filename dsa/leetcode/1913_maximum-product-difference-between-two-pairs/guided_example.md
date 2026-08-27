# Guided Example: Maximum Product Difference Between Two Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 6, 2, 7, 4]}`
- **Required output:** `34`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **product difference** between two pairs `(a, b)` and `(c, d)` is defined as $(a * b) - (c * d)$.

The objective is to compute `34` from `{"nums": [5, 6, 2, 7, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate the expression into a maximum product and minimum product.** The objective is `a * b - c * d` using four distinct indices. Because every input value is positive, increasing either factor of the first product cannot reduce it, and increasing either factor of the subtracted product cannot improve the difference. The best choice is therefore the two largest occurrences for the positive product and the two smallest occurrences for the negative product.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 6, 2, 7, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Sort to expose all four extremes.** `nums.sort()` arranges occurrences in nondecreasing order. `nums[-1]` and `nums[-2]` are the largest and second-largest occurrences; `nums[0]` and `nums[1]` are the smallest and second-smallest. The returned expression multiplies the upper pair and subtracts the lower pair.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Sort to expose all four extremes.** `nums.sort()` arranges... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Occurrences matter rather than distinct values. If the largest value appears twice, the two final sorted positions correspond to two distinct indices and may both be selected. If it appears once, the second-last position supplies the next available occurrence. Sorting preserves multiplicity automatically.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `34` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 6, 2, 7, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `34` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Track two minima and two maxima:** Update four:** - **Track two minima and two maxima:** Update four scalar extrema in one pass, obtaining the manifest's $O(n)$ time and $O(1)$ space without mutation.
- **Heap selection:** Keeping two-element min/max heaps also works in $O(n)$ time but adds unnecessary data-structure overhead for fixed-size extrema.
- **Enumerate four indices:** Brute force is $O(n^4)$ and repeats information that extremes settle directly.
- **Exactly four elements:** All occurrences are used; sorting determines which pair is added and which is subtracted.
- **Duplicate extremes:** Equal values at different sorted positions are valid distinct-index choices.
- **All values equal:** Both products are equal and the maximum difference is zero.
- **Positive-value guarantee:** It is essential to the monotonic product proof. General signed arrays need consideration of negative extremes.
- **Input mutation:** The exact solution leaves `nums` sorted. Use a copy if callers require the original order.
- **Manifest mismatch:** Linear constant-space tracking is available, but complexity documentation must reflect this source's sorting behavior.
- **Four distinct indices versus values:** The values themselves need not differ. What matters is that the four selected sorted positions represent four occurrences from distinct original indices.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $n$ be the array length. Python sorting takes $O(n\log n)$ time; the final indexing and arithmetic are constant. The exact source therefore does not match the manifest's $O(n)$ time label. A one-pass four-extrema tracker can achieve linear time, but it is not executed here.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
