# Guided Example: Minimum Adjacent Swaps to Alternate Parity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 6, 5, 7]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` of **distinct** integers.

The objective is to compute `3` from `{"nums": [2, 4, 6, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Feasibility

An alternating length-`n` arrangement has parity counts differing by at most one.

If the input even/odd counts differ by more than one, no permutation can alternate, so the source returns `-1`.

If one parity has one extra element, it must occupy both ends and therefore must start at position zero. If counts are equal, either parity may start.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 6, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Position lists

`pos[0]` stores original indices of even values and `pos[1]` stores odd indices. Because the input is scanned left to right, each list is sorted.

`calc(k)` assumes parity `k` occupies even target indices:

`0,2,4,...`.

It pairs these targets with `pos[k]` in their existing order and sums absolute movements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pos[0]` stores original indices of even values and `pos[1]`... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why order-preserving matching is optimal

Elements of the same parity are interchangeable for validity. Under adjacent swaps, there is no benefit to making two same-parity elements cross: exchanging their assigned targets removes the crossing and cannot increase total distance.

Therefore the first current even should go to the first even target, the second to the second, and similarly for odds. This sorted matching minimizes total displacement.

The sum

$$
\sum_t |current_t-target_t|
$$

equals the minimum adjacent swaps. Each swap between opposite parities moves one tracked parity element one position toward its target. Same-parity swaps are unnecessary, and the order-preserving plan can realize all required movements.

Counting movement for only one parity does not miss a factor of two. One adjacent even-odd swap moves both elements, but it is one operation and advances exactly one tracked parity token by one position. Summing that class’s displacement counts each swap once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 6, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate adjacent swaps:** Moving misplaced el:** - **Simulate adjacent swaps:** Moving misplaced elements directly can also be linear with careful pointers, but position matching proves the count without mutating the array.
- **Try arbitrary permutations:** Values within a parity class are interchangeable; factorial enumeration is unnecessary.
- **Count mismatched positions only:** A misplaced element may need to travel several cells, so mismatch count alone does not equal adjacent-swap cost.
- **Count difference above one:** Alternation is impossible and returns `-1`.
- **Equal counts:** Both starting parities must be evaluated; costs can differ.
- **One extra even:** Even must occupy index zero and every even target.
- **One extra odd:** Odd must start.
- **Single element:** Count difference is one, its parity starts, and movement sum is zero.
- **Already alternating:** Current and target positions match, producing zero.
- **All same parity with n>1:** Count difference exceeds one and is impossible.
- **Negative integers:** Outside current positive constraints, `x&1` still classifies Python odd/even parity consistently.
- **Distinctness:** It is irrelevant to the parity-token proof but guaranteed by the statement.
- **No input mutation:** Position lists are derived while `nums` remains unchanged.
- **Why zip lengths match:** Feasibility and selected starting parity guarantee the tracked class count equals the number of even-index targets.
- **Manifest space mismatch:** Both position lists together always contain exactly `n` indices, so their storage cannot be called constant.
- **Crossing argument:** If two same-parity elements at positions `a<b` were assigned to targets `y<x`, swapping their assignments changes cost from `|a-x|+|b-y|` to `|a-y|+|b-x|` and never increases it. Repeating removes every crossing, proving sorted-to-sorted matching.
- **Why values are irrelevant:** Adjacent-swap validity observes only even versus odd. Distinct magnitudes do not change target slots or movement cost, so preserving numerical order within a parity class is unnecessary beyond the no-crossing position order.
- **Realizing the distance sum:** Move tracked parity elements toward their assigned slots from left to right. Each crossing with the opposite parity costs one adjacent swap and decreases remaining tracked displacement by one, constructing a sequence with exactly the calculated total.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Building position lists takes `O(n)` time. Each `calc` call scans one parity list, and at most two calls are made, so total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
