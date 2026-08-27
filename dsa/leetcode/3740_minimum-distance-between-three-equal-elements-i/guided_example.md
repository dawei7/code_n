# Guided Example: Minimum Distance Between Three Equal Elements I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 1, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `6` from `{"nums": [1, 2, 1, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simplify the three-index distance

Sort the three selected indices conceptually as `i<j<k`. Their distance becomes

$$
(j-i)+(k-j)+(k-i)=2(k-i).
$$

The middle index cancels. For three equal values, minimizing the stated distance is therefore equivalent to minimizing the span from the first selected occurrence to the third.

Tuple order does not matter because absolute pairwise distances are symmetric. Every set of three distinct indices can be analyzed in increasing order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group occurrence positions by value

The dictionary `g` maps each array value to its list of indices. Because indices are appended during a left-to-right enumeration, every list is already strictly increasing.

For example, if a value occurs at indices `[0,2,3,8]`, all good triples using it come from choosing three entries of this list. The distance depends only on the first and last chosen entries.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The dictionary `g` maps each array value to its list of indi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Only consecutive occurrence triples can be optimal

Consider a chosen triple at occurrence-list positions `p<q<r`. If these are not three consecutive occurrences, then either an occurrence exists between the first and middle or between the middle and last. Replacing an outer selected occurrence with a closer intervening occurrence can only shrink, never enlarge, the outer span.

More directly, for any fixed first occurrence position `h` in the list, the smallest possible third occurrence is `h+2`; choosing a later one makes `k-i` larger. Every globally minimum triple therefore appears as

`ls[h], ls[h+1], ls[h+2]`

for some `h`.

One can also start from an arbitrary nonconsecutive triple `p_a,p_b,p_c`. Because `b>=a+1` and `c>=b+1`, `p_{a+2}` exists and is at most `p_c`. Replacing the chosen middle and third occurrences by `p_{a+1}` and `p_{a+2}` keeps the value equal and distinct while shrinking or preserving the outer endpoint. This constructs the required consecutive witness explicitly.

The source does not need the middle index numerically. It loops `h` through `0` to `len(ls)-3`, reads `i=ls[h]` and `k=ls[h+2]`, and evaluates `2*(k-i)`.

Overlapping consecutive triples are all considered. In `[0,2,3,8]`, windows `[0,2,3]` and `[2,3,8]` are separate candidates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three nested loops:** The small constraints pe:** - **Three nested loops:** The small constraints permit $O(n^3)$ enumeration, but occurrence grouping is both clearer and asymptotically better.
- **Check all triples within each list:** A value appearing many times still creates cubic combinations. Consecutive windows are sufficient.
- **Track only frequencies:** A count tells whether a triple exists but not its index span, so positions are required.
- **Use the middle index in the formula:** Its two adjacent gaps telescope; only the outer span matters.
- **Exactly three occurrences:** The list contributes one window.
- **More than three occurrences:** Overlapping windows must all be checked because the tightest cluster can occur anywhere.
- **No value appears three times:** Infinity remains and maps to `-1`.
- **Adjacent equal occurrences:** Indices `i,i+1,i+2` produce the minimum possible distance four.
- **Several values qualify:** Their best windows compete in the same global minimum.
- **Tuple ordering:** Permuting the same three indices does not change pairwise absolute distances.
- **Input values bounded by `n`:** The dictionary works without relying on that bound and uses space proportional to actual occurrences.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. Building all lists takes expected $O(n)$ time. Across all values, the total list lengths are `n`, and the total number of consecutive triple windows is at most `n`. The scan therefore takes $O(n)$ time, for $O(n)$ expected total.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
