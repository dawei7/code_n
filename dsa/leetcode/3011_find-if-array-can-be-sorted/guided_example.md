# Guided Example: Find if Array Can Be Sorted

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [8, 4, 2, 30, 15]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of **positive** integers `nums`.

The objective is to compute `true` from `{"nums": [8, 4, 2, 30, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The sequence of set-bit counts cannot change

Assign each element a label equal to `element.bit_count()`. A legal adjacent swap exchanges two elements only when their labels are equal. Swapping equal labels leaves the label sequence unchanged.

Therefore, an element can move only inside its original maximal contiguous block of one label. It can never cross a neighboring block with a different set-bit count. The block boundaries are permanent.

Within one block, however, any permutation is possible: arbitrary permutations can be produced through adjacent swaps, and every adjacent pair in the block has the same label. Thus each block may be sorted internally.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [8, 4, 2, 30, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reduce global sorting to block ranges

After sorting every block internally, the smallest value of a block appears first and its largest appears last. The concatenation is globally nondecreasing exactly when every block’s minimum is at least the maximum value of all earlier blocks.

Because earlier blocks have already passed this condition, the immediately previous block’s maximum is also the largest value seen in the sortable prefix. The code stores it as `pre_mx`.

For the current block, it computes `mi` and `mx`. If `pre_mx > mi`, some earlier value is larger than the smallest current value. Those two values lie in different immutable label blocks and cannot cross, so global sorting is impossible.

If `pre_mx <= mi`, every value in the earlier sorted prefix is at most every value at the beginning of this block. Sorting the current block internally preserves global order across the boundary. `pre_mx` becomes this block’s maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact scan identifies blocks

Pointer `i` begins a block. `cnt = nums[i].bit_count()` stores its label. Pointer `j` advances while later values have the same bit count.

During that inner scan, `mi` and `mx` track the block’s extremes. The algorithm does not actually sort or swap values because only these two boundary facts are needed to decide feasibility.

After checking the block, `i = j` jumps directly to the next label block.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [8, 4, 2, 30, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bubble-sort with legality checks:** It can simulate valid swaps but takes $O(N^2)$ time and may mutate or copy the input.
- **Sort each block explicitly:** This is constructive but costs $O(N\log N)$ total; minima and maxima suffice for feasibility.
- **Group all equal-popcount values globally:** Noncontiguous blocks cannot cross intervening labels, so they must not be merged.
- **Already sorted array:** Every boundary range is compatible, and the method returns true without swaps.
- **One element:** It forms one block and is trivially sortable.
- **All labels equal:** The whole array is one block and any permutation, including sorted order, is reachable.
- **Equal values across a boundary:** Nondecreasing order permits equality; failure uses strict `pre_mx > mi`.
- **Positive input guarantee:** It makes zero a valid initial previous maximum.
- **Input preservation:** Only range summaries are computed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length. Every element is visited once by the advancing block pointers. `bit_count` is constant time for the bounded integers, so running time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
