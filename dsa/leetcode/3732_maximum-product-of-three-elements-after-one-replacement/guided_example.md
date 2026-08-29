# Guided Example: Maximum Product of Three Elements After One Replacement

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-5, 7, 0]}`
- **Required output:** `3500000`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `3500000` from `{"nums": [-5, 7, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An optimal product can use the replaced element

Let `B = 10^5`, the greatest allowed absolute replacement value. For any chosen pair of unchanged original elements with product `p`, the replaced third factor can be chosen as:

- `+B` when `p >= 0`.
- `-B` when `p < 0`.

The resulting product is

$$
B|p|,
$$

which is nonnegative and as large as possible for that pair.

There is no benefit in using a replacement magnitude below `B` because the sign can be chosen freely. An outcome that replaces an unselected index and takes three original values can be matched or improved by replacing one selected factor with magnitude `B` and the sign that makes the other two factors' product nonnegative. Original magnitudes are also bounded by `B`.

Thus the problem reduces to selecting two distinct original indices whose absolute product is maximum, then supplying the optimal signed boundary replacement as the third factor.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-5, 7, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only three types of extreme pair matter

After sorting, name:

- `a = nums[0]`, the smallest value.
- `b = nums[1]`, the second-smallest value.
- `c = nums[-2]`, the second-largest value.
- `d = nums[-1]`, the largest value.

The pair with greatest absolute product must be one of three structural types:

1. Two large-magnitude negative values: `a * b`.
2. Two large positive values: `c * d`.
3. One extreme negative and one extreme positive: `a * d`.

For a same-sign positive pair product, the replacement should be `+B`. For the cross-sign negative product, it should be `-B`. The exact source therefore returns

`max(a * b * B, c * d * B, a * d * -B)`.

These formulas remain safe when a category is not genuinely present. For example, in an all-positive array, `a*b*B` is merely a smaller positive candidate and `a*d*(-B)` is negative; `c*d*B` wins. In an all-negative array, `a*b*B` captures the two largest magnitudes. Zeros naturally produce zero candidates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no interior pair can be better

For two nonnegative values, product increases as either factor increases, so the best pair is the two largest, `c` and `d`. For two nonpositive values, their product equals the product of their absolute magnitudes, which are largest at the most negative end, `a` and `b`.

For opposite signs, the absolute product is maximized by the most negative value `a` and greatest nonnegative value `d`. Multiplying by `-B` turns that negative pair product into a positive final result.

Every pair belongs to one of these sign types. The source evaluates the best extreme representative of each, so its maximum equals

$$
B\max_{i<j}|\texttt{nums}[i]\texttt{nums}[j]|.
$$

The two chosen originals have distinct indices because `a,b` and `c,d` refer to separate sorted positions. The replacement occupies a third index. Since the original array has at least three elements, such an index exists; when `n=3`, choosing a pair implicitly determines the remaining replacement position.

For `[-5,7,0]`, the cross-extreme pair is `-5*7=-35`. Choosing replacement `-100000` makes the product `3,500,000`.

For `[-4,-2,-1,-3]`, the two smallest sorted values are `-4` and `-3`. Their product is 12, and replacement `+100000` gives `1,200,000`.

For `[0,10,0]`, every pair contains zero, so all possible three-factor products after one replacement remain zero. The maximum formula returns zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3500000` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-5, 7, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3500000` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track four extremes in one pass:** Maintaining the two smallest and two largest values yields $O(n)$ time and $O(1)$ space and would match the manifest. It is a valid optimization, but the exact source sorts and therefore has different actual bounds.
- **Try every pair:** Evaluating $O(n^2)$ original pairs and selecting the replacement sign is correct but unnecessary because monotonicity confines the best pair to sorted extremes.
- **Replace with zero or an interior magnitude:** A smaller absolute replacement cannot improve a fixed pair. The optimum always uses `+10^5` or `-10^5`.
- **Consider only the three largest numeric values:** Two large negative magnitudes can create the best positive pair, so the smallest sorted values are equally important.
- **Consider only same-sign pairs:** A large negative and large positive pair becomes a large positive triple when the replacement is negative. The `a*d*(-B)` candidate covers it.
- **All positive values:** The two largest values with positive replacement win.
- **All negative values:** The two most negative values have the largest positive pair product and use positive replacement.
- **Mixture with zeros:** Zero is optimal only when every available pair product is zero. The formulas handle this without branching.
- **Exactly three elements:** Each candidate selects two originals and replaces the remaining index, satisfying distinctness.
- **Duplicate extremes:** Sorted positions remain distinct even when their values are equal, so using `a` and `b` or `c` and `d` is legal.
- **Values already at replacement bounds:** The inclusive range still permits boundary replacements. Magnitude cannot exceed `B`.
- **Input mutation:** Callers needing the original order would have to sort a copy, adding another explicit $O(n)$ allocation; the current source modifies the list.
- **Manifest mismatch:** Complexity documentation must follow the executed sort, not the summary's aspirational one-pass bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The manifest claims $O(n)$ time and $O(1)$ space, but that does not match the exact Optimal source being explained. The source executes `nums.sort()`. For `n` elements, this makes the actual time complexity $O(n\log n)$, followed by only constant-time endpoint arithmetic.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
