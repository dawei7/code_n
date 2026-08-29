# Guided Example: Number of Perfect Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [0, 1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Remove the distracting signs

The original conditions contain both `|a - b|` and `|a + b|`, so checking them directly for every pair would be cumbersome and quadratic. The first simplification is to describe both quantities using only

`x = |a|` and `y = |b|`.

Assume without loss of generality that `x <= y`. If `a` and `b` have the same sign, then the smaller of `|a - b|` and `|a + b|` is `y - x`, while the larger is `y + x`. If the signs are opposite, subtraction and addition exchange those roles, but the unordered pair of results is still

`{y - x, y + x}`.

Therefore, regardless of signs,

`min(|a - b|, |a + b|) = y - x`

and

`max(|a - b|, |a + b|) = y + x`.

This identity proves that whether a pair is perfect depends only on the two magnitudes. Replacing every input value by its absolute value cannot change the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reduce both inequalities to one ratio condition

Under `x <= y`, the smaller input magnitude is `x` and the larger is `y`. Substitute the identities into the two required inequalities.

The first becomes

`y - x <= x`,

which rearranges to

`y <= 2x`.

The second becomes

`y + x >= y`.

Because `x` is non-negative, that second inequality is always true. It imposes no additional restriction.

Thus two values form a perfect pair exactly when their larger magnitude is at most twice their smaller magnitude:

`max(|a|, |b|) <= 2 * min(|a|, |b|)`.

This is the entire mathematical core of the solution. Once the magnitudes are sorted, the condition describes a contiguous range rather than an arbitrary collection of partners.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort magnitudes to make every valid partner adjacent in a range

The source builds

`magnitudes = sorted(abs(value) for value in nums)`.

Suppose `magnitude = magnitudes[right]` is the current, larger endpoint. Every earlier position has magnitude no greater than it. An earlier value at position `p` forms a perfect pair with `right` precisely when

`magnitude <= 2 * magnitudes[p]`.

Because the array is sorted, if this condition holds at some position `p`, it also holds for every later position up to `right - 1`: later magnitudes are at least as large, so their doubled values are also large enough. Conversely, if it fails for `p`, it fails for every earlier, no-larger magnitude.

The valid earlier partners therefore form one suffix

`left, left + 1, ..., right - 1`.

The two-pointer loop maintains `left` as the first position in this suffix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every pair directly:** Evaluating both original inequalities for all `i < j` is straightforward but costs `O(n^2)`, which is too slow for `n = 10^5`.
- **Binary search per right endpoint:** After sorting, binary-search the first magnitude at least half of the current one. This gives `O(n log n)` counting after the sort; the monotone two-pointer scan improves that phase to `O(n)`.
- **Frequency map over magnitudes:** One could count repeated magnitudes and process sorted distinct keys with multiplicities. It may reduce scanning when duplicates are common but requires careful combination counting and does not improve the worst-case sorting bound.
- **Keep the original signs:** Signs do not affect the minimum and maximum of `|a-b|` and `|a+b|`. Retaining them obscures the one ratio condition without adding information.
- **Forget the second inequality:** It is safe to omit only after proving `x + y >= max(x, y)` for non-negative magnitudes. Dropping it without that derivation would leave the reduction unjustified.
- **Boundary ratio exactly two:** A pair with larger magnitude exactly twice the smaller is valid because the condition uses `<=`. The source’s `while` loop removes only strict violations.
- **Two zero values:** They form a perfect pair because all four relevant quantities are zero. The loop counts earlier zeros with a current zero.
- **One zero and one nonzero value:** The ratio condition becomes positive `<= 0`, which is false. The left pointer discards zeros before pairing a positive magnitude.
- **Equal nonzero magnitudes:** They always form a perfect pair because `x <= 2x`. Duplicate occurrences are counted as distinct index pairs.
- **All magnitudes far apart:** For values such as `[1, 10, 100, 1000]`, each new magnitude discards all earlier ones and the answer remains zero.
- **Negative values:** Applying `abs` is mathematically exact, not an approximation. A positive and negative value with the same magnitude behaves like any equal-magnitude pair.
- **Original index order:** The requirement `i < j` chooses one representation of each unordered index pair. Since the relation is symmetric, sorting occurrences and counting each pair once preserves the requested count.
- **Input preservation:** The generator computes new magnitudes and `sorted` returns a new list; `nums` itself is not modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`. Computing absolute values and creating the list takes `O(n)` time. Sorting dominates at `O(n log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
