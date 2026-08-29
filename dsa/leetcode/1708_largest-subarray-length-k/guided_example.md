# Guided Example: Largest Subarray Length K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 5, 2, 3], "k": 3}`
- **Required output:** `[5, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An array `A` is larger than some array `B` if for the first index `i` where $A[i] \neq B[i]$, $A[i] > B[i]$.

The objective is to compute `[5, 2, 3]` from `{"nums": [1, 4, 5, 2, 3], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only certain indices can start a length-$k$ subarray

If `nums` has length $n$, a subarray of length $k$ beginning at index `i` ends at `i+k-1`. It stays inside the array exactly when

$$
0\le i\le n-k.
$$

Therefore the valid starting values are contained in

`nums[: len(nums) - k + 1]`.

The slice stop is exclusive, so adding one includes index `n-k`, the final legal start. Values after that index cannot begin a complete length-$k$ subarray and must not influence the choice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 5, 2, 3], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Distinct values reduce lexicographic comparison to the first element

Every candidate has the same length $k$. Lexicographic comparison examines position zero first and looks farther only if the first elements are equal.

The contract guarantees that all values in `nums` are distinct. In particular, the first elements of any two candidates with different start indices are different. Their comparison is therefore decided immediately by those first elements; no second or later position can overturn it.

Consequently the lexicographically largest candidate is exactly the one whose starting value is largest among all valid starts. The source computes that value with

`max(nums[: len(nums) - k + 1])`.

This is the central reason the solution can avoid comparing entire subarrays.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recover the chosen start index

`nums.index(...)` returns the first index at which the maximum starting value occurs. Because every number is unique, there is exactly one occurrence in the whole array. Its location is the valid start that supplied the maximum.

Calling `index` on the whole list rather than only the prefix is still safe: the searched value came from the prefix, and uniqueness means no earlier or later duplicate can cause a different result.

The chosen position is stored in `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 5, 2, 3], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan valid start indices:** Track the index with the greatest `nums[i]` for `i <= n-k`. This keeps $O(n)$ time and reduces non-output auxiliary space to $O(1)$.
- **Compare every candidate list:** Materializing and comparing all length-$k$ slices can cost $O(nk)$ time and unnecessary allocation.
- **Non-distinct follow-up:** Equal starting values require comparing later positions; the exact max-start rule is insufficient.
- **`k = 1`:** Every element can start, so the maximum element alone is returned. The exact source still allocates the full prefix slice.
- **`k = n`:** Only index zero is legal, and the returned slice is the entire array.
- **Maximum near the end:** It is eligible only if its index is at most `n-k`; later large values cannot start a full candidate.
- **Negative values in a generalized input:** Distinctness, not positivity, powers the proof, so the method would still compare starts correctly.
- **Unique maximum:** Guaranteed by all values being distinct, making `index` unambiguous.
- **Output copying:** Python slicing returns a new list rather than a view.
- **Off-by-one boundary:** The `+1` in the prefix stop is required to include the last valid start.
- **Input preservation:** Neither `max`, `index`, nor slicing changes `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n-k+1)$. Let $n$ be the list length. Creating the valid-start slice copies $n-k+1$ elements. `max` scans that slice, `nums.index` may scan up to $n$ elements, and the returned slice copies $k$ elements. Total time is
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
