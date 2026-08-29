# Guided Example: Minimum Swaps to Move Zeros to End

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 0, 3, 12]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [0, 1, 0, 3, 12]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the next misplaced zero from the left

Pointer `i` starts at index zero. The loop

`while i < n and nums[i] != 0`

skips values that are already suitable for the nonzero prefix. It stops at the first zero not previously handled, or moves beyond the array if no zero remains.

That zero is not automatically wrong merely because it occurs somewhere in the array. It is wrong only if some nonzero still occurs to its right. If every later entry is zero, the array already has the required suffix from that point onward.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 0, 3, 12]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the next misplaced nonzero from the right

Pointer `j` starts at the final index. The loop

`while j and nums[j] == 0`

skips zeroes that are already suitable for the final suffix. It stops at a nonzero value or at index zero.

The condition `while j` means “while `j != 0`.” It deliberately avoids decrementing `j` below zero. This slightly unusual spelling is safe because the outer logic only forms a pair when `i < j`. If both pointers have met at index zero, no swap is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One crossing pair needs one swap

After the scans, if `i < j`, then:

- `nums[i]` is zero;
- `nums[j]` is nonzero;
- the zero is to the left of the nonzero.

They are a mismatched pair relative to the desired nonzero-prefix/zero-suffix order. Swapping them would put a nonzero at `i` and a zero at `j`, correcting both positions in one operation.

The source increments `ans` and then advances `i` and decreases `j`. It does not physically exchange the array values. That omission is safe because the conceptual swap would make both boundary positions correct, and neither position will be inspected again. Everything between the new pointers is unchanged.

The next outer iteration skips any additional already-correct values and locates the next crossing pair.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 0, 3, 12]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count nonzeroes in the reserved suffix:** First count $Z$, then count nonzero entries among the last $Z$ positions. This yields the same minimum in two linear passes and makes the mismatch lower bound explicit.
- **Actually perform each swap:** This returns the same count and constructs a valid arrangement, but mutation is unnecessary because only the minimum number is requested.
- **Stable two-pointer compaction:** Moving nonzeroes forward while preserving their relative order solves a stronger arrangement problem. Counting writes or adjacent movements would not equal the arbitrary-swap minimum.
- **Count zero-before-nonzero inversions:** That measures adjacent swaps. One arbitrary swap can eliminate many such inversions, so the inversion total overestimates the answer.
- **All zeroes:** The right pointer skips the zero suffix until the pointers meet, and no swap is counted.
- **No zeroes:** The left pointer reaches `n`, the pointers cross, and the result is zero.
- **Already partitioned array:** Every nonzero is skipped from the left and every trailing zero from the right; no crossing pair is formed.
- **All zeroes before all nonzeroes:** The algorithm pairs the outermost mismatches and returns the smaller of the zero and nonzero counts, which is exactly the number of wrong suffix positions.
- **One-element array:** The pointers start equal, so the loop exits with zero whether the value is zero or nonzero.
- **Zero at the left and nonzero at the right:** They can be exchanged directly in one operation even when far apart.
- **Repeated nonzero values:** Their identities do not matter; only whether each value is zero affects its target region.
- **The condition `while j` at index zero:** It does not inspect past the beginning. The later `i >= j` check prevents treating an unclassified index-zero value as a swappable right endpoint.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `nums`. Pointer `i` only increases and pointer `j` only decreases. Across all nested loops, each index is passed at most once from each direction. The total time complexity is $O(N)$ rather than $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
