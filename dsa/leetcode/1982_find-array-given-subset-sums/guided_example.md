# Guided Example: Find Array Given Subset Sums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "sums": [-3, -2, -1, 0, 0, 1, 2, 3]}`
- **Required output:** `[1, 2, -3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the length of an unknown array that you are trying to recover. You are also given an array `sums` containing the values of all $2^n$ **subset sums** of the unknown array (in no particular order).

The objective is to compute `[1, 2, -3]` from `{"n": 3, "sums": [-3, -2, -1, 0, 0, 1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the signed problem into a nonnegative one

The smallest subset sum is obtained by including every negative original element and no positive element. Let that minimum be `min(sums)` and define

`m = -min(sums)`.

Thus $m$ is the sum of the absolute values of the original negative elements.

The source adds $m$ to every supplied subset sum and stores the shifted multiset in a `SortedList`. This shifted collection is exactly the subset-sum multiset of the unknown elements' absolute values.

To see why, consider an original negative value $-x$. In a supplied subset, including it contributes $-x$; after adding the total $m$, that contribution is canceled, while excluding it leaves the corresponding $+x$ inside the shift. This complements the inclusion choice for every negative element. Positive elements keep their ordinary inclusion choice. Across all subsets, the shifted sums therefore enumerate all subsets of the nonnegative magnitudes.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "sums": [-3, -2, -1, 0, 0, 1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a sorted multiset is required

Subset sums can repeat, especially when elements are equal or zero. A plain set would lose multiplicities and make later removals incorrect. `SortedList` retains duplicates, supports finding the smallest remaining value at index zero, and removes one occurrence at a time.

The shifted multiset contains zero for the empty magnitude subset. The source removes exactly one zero before recovery begins.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Subset sums can repeat, especially when elements are equal o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recover magnitudes from smallest remaining sums

After empty zero is removed, the smallest remaining subset sum must be the smallest element magnitude, so the source begins `ans = [sl[0]]`.

The recovery invariant is: before selecting the next element, remove all nonempty subset sums that can be formed entirely from magnitudes already recovered. Once those known sums are removed, the smallest remaining value must be the next smallest unrecovered magnitude. Its singleton subset exists, and every subset containing an unrecovered magnitude is at least as large because all magnitudes are nonnegative.

The loop implements removals by highest included index. At stage `i`, the newest known magnitude has index `i - 1`. It enumerates all masks over the first `i` known values but processes only masks whose bit `i - 1` is set. Those are exactly the known-element subsets containing the newest value. Subsets not containing it were removed in earlier stages.

For each such mask, it recomputes the subset sum and removes one matching occurrence from `sl`. After all these removals, `sl[0]` is appended as the next magnitude.

This scheme handles duplicates correctly because removal is by multiset occurrence, not unique numeric value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, -3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "sums": [-3, -2, -1, 0, 0, 1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, -3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive partition by a candidate magnitude:*:** - **Recursive partition by a candidate magnitude:** Split sorted sums into pairs differing by that magnitude and recurse on the half containing zero; this is another standard $O(N2^N)$ strategy.
- **Plain set:** Incorrect because repeated subset sums carry essential multiplicity.
- **Recover signs during magnitude extraction:** Possible, but the shift cleanly separates magnitude recovery from one final subset-sum sign choice.
- **All elements nonnegative:** The minimum sum is zero, $m=0$, and the empty sign subset succeeds without negating anything.
- **All elements negative:** Their magnitudes sum to $m$, so the sign search can negate the full recovered array.
- **Zero elements:** Repeated zero sums allow zero magnitudes to be recovered correctly.
- **Duplicate magnitudes:** `SortedList` removes one occurrence at a time, preserving multiplicity.
- **Several valid arrays:** Any recovered order and any sign subset totaling $m$ is accepted.
- **Guaranteed solvability:** Every requested removal and the final sign subset exist for valid generated input.
- **Exponential input size:** $O(2^N)$ space is unavoidable merely to receive all supplied sums.
- **Imported data structure:** The exact source assumes `SortedList` is provided by the execution environment.
- **Input preservation:** It creates shifted values rather than sorting or changing `sums` itself.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log Q)$. Let $N$ be the unknown array length and $Q=2^N$ the number of supplied sums. Sorting the initial values costs $O(Q\log Q)=O(N2^N)$. The recovery and sign-search loops enumerate $O(2^N)$ masks and compute each selected sum in up to $O(N)$ time. `SortedList.remove` also costs logarithmic time, $O(\log Q)=O(N)$.
- **Auxiliary Space Complexity:** $O(2^N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
