# Guided Example: Lexicographically Smallest Negated Permutation that Sums to Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "target": 0}`
- **Required output:** `[-3, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` and an integer `target`.

The objective is to compute `[-3, 1, 2]` from `{"n": 3, "target": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce sign choices to a subset-sum target

If every magnitude `1..n` were positive, their total would be

$$
T=\frac{n(n+1)}2.
$$

Negating magnitude `v` changes its contribution from `+v` to `-v`, reducing the total by `2v`. If the negative magnitudes sum to `N`, the signed array sum is

$$
T-2N.
$$

To reach `target`, the required negative subset sum is

$$
N=\frac{T-\texttt{target}}2.
$$

A solution is impossible when `|target|>T` or `T-target` is odd. The first condition places the target outside the maximum possible signed range; the second makes `N` non-integral.

When both pass, `0<=N<=T`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "target": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Greedily choose negative magnitudes from largest to smallest

The source scans `value=n,n-1,...,1`. If the remaining `negative_sum` is at least `value`, it marks that magnitude negative and subtracts it.

For consecutive magnitudes, this greedy choice always completes the subset. Before considering `v`, the remaining sum is within what `1..v` can represent. If it is at least `v`, choosing `v` leaves at most

$$
\frac{v(v+1)}2-v=\frac{v(v-1)}2,
$$

which smaller magnitudes can represent. If it is below `v`, including `v` would overshoot, so skipping is mandatory. By induction, the remainder reaches zero.

More precisely, before processing `v` the invariant is that the current remainder lies between zero and `v(v+1)/2`. The include case leaves it within the representable range of `1..v-1`. In the skip case the remainder is below `v`, so the smaller complete sequence can represent it. This maintains feasibility at every step.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the greedy subset gives lexicographic minimum

For a fixed sign assignment, the smallest permutation is its values sorted numerically:

- Negative values appear first from most negative upward, meaning descending magnitude.
- Positive values follow in ascending magnitude.

Across different feasible sign subsets, making a larger magnitude negative introduces a smaller numeric element `-v` at the earliest place where the sorted arrays can differ. Therefore, whenever magnitude `v` can be included while still completing the required subset sum, including it is lexicographically preferable.

The feasibility calculation above proves the descending greedy includes `v` exactly when it can do so. It thus chooses the lexicographically smallest feasible negative set.

The output construction mirrors numeric sorting:

`[-value for value in range(n,0,-1) if is_negative[value]]`

emits selected negatives from `-n` upward, then positive magnitudes are appended from one through `n`.

For `n=3` and target zero, `T=6` and `N=3`. Greedy selects magnitude three as negative. The sorted signed values are `[-3,1,2]`, matching the required minimum.

For `n=4` and target zero, `T=10` and `N=5`. Greedy selects four, skips three and two while the remainder is one, and finally selects one. The signed values sort to `[-4,-1,2,3]`. Any feasible solution without `-4` begins with a larger integer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-3, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "target": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-3, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **General subset-sum DP:** It would be far too expensive for totals near $n^2$. Consecutive magnitudes make descending greedy exact.
- **Choose small negatives first:** It may reach the sum but produces lexicographically larger arrays because large negative values are smaller numeric prefixes.
- **Emit values in magnitude order:** Lexicographic minimum requires ordinary signed numeric order, with large-magnitude negatives first.
- **Target above `T` or below `-T`:** No sign assignment can reach it.
- **Parity mismatch:** Every sign flip changes the all-positive total by an even amount, so reachable sums share `T`'s parity.
- **Target equals `T`:** `N=0`, no values are negative, and the answer is `[1,2,...,n]`.
- **Target equals `-T`:** Every magnitude is negative, emitted as `[-n,...,-1]`.
- **`n=1`:** Only targets one and negative one are reachable.
- **Duplicate values:** Absolute values are a permutation, so magnitudes are unique; the Boolean array maps one-to-one.
- **Remainder after greedy:** The complete-sequence invariant guarantees it is zero once feasibility passes.
- **Lexicographic comparison:** A more negative first unequal element is smaller, which is why the algorithm prioritizes large negative magnitudes.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Computing feasibility is constant time. The descending sign scan visits `n` magnitudes, and the two output passes together visit another $O(n)$ positions. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
