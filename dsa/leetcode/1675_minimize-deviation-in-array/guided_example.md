# Guided Example: Minimize Deviation in Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` of `n` positive integers.

The objective is to compute `1` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize every value to its largest reachable form

The allowed moves are asymmetric. An even value can be divided by two, while an odd value can be doubled. For one original odd value `v`, its only larger reachable value is `2v`; after doubling, it is even and may be divided back. For an original even value, the largest reachable value is the value itself. It can only move downward until becoming odd, after which doubling merely returns to the preceding even value.

The source therefore converts every odd input to `2v` and leaves every even input unchanged. After this normalization, every element starts at the top of its reachable descending chain. All remaining useful transitions are repeated divisions of an even current value by two.

This common direction is crucial. Instead of mixing increases and decreases, the algorithm starts from one valid array and explores candidates by decreasing current maxima.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use negative numbers as a max-heap

Python’s `heapq` is a min-heap. The source stores `-v`, so the smallest negative number represents the largest actual value. Thus `-h[0]` is the current array maximum.

While normalizing, `mi` records the smallest actual value placed in the heap. After `heapify(h)`, the heap contains exactly one current representative for each input element, and `mi` is their minimum. The initial deviation is

`-h[0] - mi`.

The heap gives fast access to the only element that can immediately reduce the current maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the current maximum is changed

Deviation is `maximum - minimum`. Starting from every value’s largest reachable representative means no element has an unexplored larger choice. To obtain a smaller range from the current selection, the meaningful next action is to lower a current maximum if it is even.

Lowering a nonmaximum cannot reduce the maximum and can only keep or decrease the minimum, so it cannot improve the current deviation at that moment. The heap simulation therefore divides only the largest current value.

This does not lose configurations. Whenever an element is reduced, the algorithm records the deviation before reducing it. Its old larger value has already participated in the current candidate range. The heap process systematically walks downward through reachable values at the moments they can constrain the maximum, just like the standard smallest-range search across ordered candidate lists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit max-heap implementation:** Languages with a native max-heap can store positive values. Python’s negation technique changes representation, not the algorithm.
- **Generate every reachable list and solve smallest range:** This makes the candidate-list interpretation explicit but can store $O(n\log M)$ values instead of the exact heap’s $O(n)$ representatives.
- **Normalize downward and raise minima:** One can start from minimum reachable values and advance upward with a min-heap, but candidate generation and stopping conditions are less direct.
- **All values equal:** The initial deviation is zero, which remains the minimum even if the loop performs later halvings.
- **All values odd:** Normalization doubles all of them, making every heap value even. This creates the option to return each to its original odd value as maxima are processed.
- **Power of two:** It has the longest halving chain down to one and determines the logarithmic transition bound.
- **Odd current maximum:** The loop stops immediately because it cannot be reduced under the allowed rule.
- **New minimum after halving:** Updating `mi` is mandatory; retaining the old minimum would understate the deviation.
- **Duplicate maxima:** Reducing one copy leaves another copy at the old maximum. The next heap iteration can reduce that copy, and both frontier states are evaluated.
- **Negative heap parity:** Python’s modulo operation still reports zero for negative even values, so the loop condition is sound.
- **Integer division:** The popped heap value is divided only when even, so `// 2` has no rounding ambiguity despite being negative.
- **Input preservation:** Odd values are doubled only in the local loop variable `v`. The original `nums` list is not modified.
- **Upper numeric bound:** Doubling an odd value up to $10^9$ produces at most $2\cdot10^9$, which remains safe in Python and within typical 32-bit signed range except near its endpoint; Python integers avoid overflow entirely.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log M\log n)$. Let `n` be the number of elements and `M` the largest normalized value. Each element can be halved at most $O(\log M)$ times before becoming odd. Across all elements, there are at most $O(n\log M)$ heap transitions.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
