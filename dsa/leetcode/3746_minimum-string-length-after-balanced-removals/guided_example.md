# Guided Example: Minimum String Length After Balanced Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabbab"}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting only of the characters `'a'` and `'b'`.

The objective is to compute `0` from `{"s": "aabbab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid removal preserves the count difference

Let `A` and `B` be the current counts of `'a'` and `'b'`. A removable substring contains the same number `x` of each character. After removing it, the new counts are

$$
A'=A-x,\qquad B'=B-x.
$$

Their difference is unchanged:

$$
A'-B'=(A-x)-(B-x)=A-B.
$$

Therefore every sequence of legal operations preserves `A-B`.

Any remaining string with counts `A_r` and `B_r` has length `A_r+B_r`, which is at least

$$
|A_r-B_r|=|A-B|.
$$

This proves that no strategy can leave fewer than the absolute original count difference.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabbab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The lower bound can always be reached

If both character types remain, the current string must contain some adjacent boundary where the character changes: `"ab"` or `"ba"`. That two-character substring contains one of each and is balanced, so it may be removed.

Removing such a pair decreases both counts by one. Concatenation may create a new mixed boundary, and the same argument can be repeated while both counts are positive.

Eventually the less frequent character count becomes zero. The remaining string contains only the more frequent character and has length

$$
|A-B|.
$$

No further balanced nonempty substring can exist because every remaining substring contains only one character type.

This is also an induction on `min(A,B)`. If that minimum is zero, the desired terminal form already exists. Otherwise both symbols occur, so an adjacent unlike pair can be removed, reducing the minimum by one while preserving the difference. The induction hypothesis then reaches a string of length `|A-B|`.

Thus the invariant lower bound is attainable, and the minimum is exactly `|A-B|`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why substring placement does not create an obstacle

It may initially seem that equal counts are not enough because removals must be contiguous. The adjacent-boundary argument resolves this. Whenever at least one `a` and one `b` exist, scanning from one occurrence type toward another must cross an adjacent unlike pair. That pair is always a legal contiguous removal.

For example, a string shaped as one large run `"aaaaabbbbb"` has only one mixed boundary, but removing its central `"ab"` joins shorter runs of the same shape. A highly alternating string has many choices. Both structures support exactly the same one-for-one cancellation.

There is no need to find a large balanced substring. Repeated length-two removals simulate cancellation of one `a` against one `b` regardless of their original separation.

For `"aaabb"`, remove an adjacent `"ab"` to leave `"aab"`, then remove its adjacent `"ab"` to leave `"a"`. The original difference is three minus two, or one.

For `"aabbab"`, the counts are equal, so the invariant predicts zero. The whole string can be removed directly, although pairwise removals would also reach empty.

For `"aaaa"`, the difference is four. No `b` exists, so no valid substring can be removed and the original length remains.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabbab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate removal choices recursively:** Many balanced substrings can overlap, creating exponential branching. Count difference makes all choices unnecessary.
- **Use a stack to cancel unlike adjacent characters:** It can reach the same remaining magnitude but uses $O(n)$ space. Counts alone suffice because order does not affect the optimum.
- **Remove only the largest balanced substring:** This may work in some cases but locating it is extra work and is not needed for optimality.
- **Assume equal total counts imply only pairwise removals:** The entire string is directly removable, but either route reaches zero.
- **All one character:** The absolute difference equals the full length, and no operation is possible.
- **Equal counts:** The answer is zero.
- **Difference one:** Repeated cancellations leave exactly one majority character.
- **Alternating string:** Many adjacent balanced pairs exist; any sequence preserves the same result.
- **Long homogeneous runs:** A boundary pair exists whenever both types occur, even if they are grouped into two large runs.
- **Concatenation after removal:** It cannot change the invariant and may only expose another removable boundary.
- **Binary-alphabet guarantee:** Computing `b=len(s)-a` relies on every character being one of the two allowed letters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. Counting `a` characters scans the string once in $O(n)$ time. Length, subtraction, and absolute value are constant-time under the bounded model. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
