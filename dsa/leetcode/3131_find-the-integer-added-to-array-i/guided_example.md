# Guided Example: Find the Integer Added to Array I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [2, 6, 4], "nums2": [9, 7, 5]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two arrays of equal length, `nums1` and `nums2`.

The objective is to compute `3` from `{"nums1": [2, 6, 4], "nums2": [9, 7, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A uniform shift preserves order and frequencies

Every element of `nums1` is changed by the same integer $x$. If a value $a$ occurs several times, all of those copies become $a+x$, so duplicates remain duplicates. If $a<b$, then

$$
a+x<b+x.
$$

Therefore, adding the same number preserves the complete sorted order of the multiset. The smallest original value must become the smallest resulting value, the second-smallest must become the second-smallest, and so on.

This observation means we do not have to determine which element in the unsorted `nums1` corresponds to which position in the unsorted `nums2`. The minimum elements are guaranteed to correspond:

$$
\min(\texttt{nums1}) + x = \min(\texttt{nums2}).
$$

Rearranging this equation gives

$$
x=\min(\texttt{nums2})-\min(\texttt{nums1}).
$$

That is exactly the one-line implementation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [2, 6, 4], "nums2": [9, 7, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why looking at just one extreme is sufficient

Normally, inferring a transformation from one pair of values could be unsafe. Here the problem guarantees that a valid uniform shift exists. Once $x$ is determined from any corresponding sorted position, every other position must have the same difference. The minimum is simply the easiest corresponding position to identify without sorting.

Suppose `nums1 = [2, 6, 4]` and `nums2 = [9, 7, 5]`. Their iteration orders do not match, but their sorted forms are `[2,4,6]` and `[5,7,9]`. The minima differ by $5-2=3$. Adding 3 to all of the first multiset gives `[5,9,7]`, which has exactly the same values and frequencies as the second.

The same reasoning works when the shift is negative. For `nums1 = [10]` and `nums2 = [5]`, the difference of minima is $5-10=-5$. “Adding” $-5$ is the required decrease.

Duplicates do not create ambiguity. If `nums1` contains four copies of 1 and `nums2` contains four copies of 1, both minima are 1 and the answer is zero. More generally, applying a uniform shift cannot split equal values into different results, so multiset frequencies line up automatically under the guaranteed transformation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the minimum maps to the minimum

Let $a$ be the minimum of `nums1`. For every other input element $b$, $a\le b$. Adding the same $x$ to both sides gives $a+x\le b+x$. Thus $a+x$ is no larger than any transformed element and is a minimum of the transformed multiset. Since that multiset equals `nums2`, $a+x=\min(\texttt{nums2})$.

This proof also handles tied minima. If several elements equal $a$, all become $a+x$ and supply the same number of copies of the minimum in `nums2`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [2, 6, 4], "nums2": [9, 7, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compare maximum values:** `max(nums2) - max(nums1)` gives the same $x$ because a uniform shift also maps maximum to maximum. It has identical complexity.
- **Sort both arrays:** After sorting, subtract any pair of equal ranks and optionally verify all differences. This takes $O(n\log n)$ time and unnecessary extra storage or mutations.
- **Frequency-map verification:** Compute the candidate from minima, shift every key frequency, and compare maps. This is useful if the validity guarantee is removed, but unnecessary here.
- **Sum difference:** Since both arrays have length $n$, $x=(\sum nums2-\sum nums1)/n$. This works under the guarantee, but requires divisibility reasoning and can overflow fixed-width sums in other constraints.
- **Single element:** The formula becomes the direct difference between the only two values.
- **Negative answer:** No special branch is required; the subtraction naturally returns a negative integer when `nums2` is shifted downward.
- **Zero answer:** Identical multisets have identical minima, so the result is zero.
- **Duplicate minima:** Every minimum copy moves together. The proof uses values and frequencies, not unique positions.
- **Different input order:** Array equality in this problem means multiset equality, so order is intentionally irrelevant.
- **Missing validity guarantee:** The one-line method would need a second pass or frequency comparison; equal minimum differences alone cannot prove arbitrary multisets match.
- **Nonempty arrays:** The contract guarantees length at least one, which is required because Python's `min` has no result for an empty sequence.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
