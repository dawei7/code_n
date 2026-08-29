# Guided Example: Hand of Straights

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

The objective is to compute `true` from `{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A necessary divisibility check

Every group must contain exactly `groupSize` cards, and every card must belong to one group. If `len(hand)` is not divisible by `groupSize`, a complete partition is impossible.

The solution returns false immediately in that case.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count copies of every card value

`cnt = Counter(hand)` records how many unused copies of each value remain. Multiple identical cards may be needed in different consecutive groups, so a set alone would lose essential multiplicity.

The algorithm iterates through `sorted(hand)`, which includes duplicates in nondecreasing order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The smallest remaining card must start a group

When current value `x` has `cnt[x] > 0`, at least one copy remains unassigned. Because the traversal is sorted, there is no smaller remaining card that could start a group containing `x` later.

Could `x` appear in the middle of a group starting at `x-1` or lower? If such a group were still needed, its smaller starting card would also remain and would have been encountered earlier. All groups starting below `x` have already been formed.

Therefore, the smallest remaining `x` is forced to be the first value of a new group:

$$
x,x+1,\ldots,x+\texttt{groupSize}-1.
$$

This forced-choice property is the greedy proof.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Min-heap of distinct values:** Repeatedly take the smallest remaining key and consume a group. It avoids sorting all duplicate occurrences but requires heap cleanup and logarithmic operations.
- **Ordered map:** Process counts by ascending key and propagate required group starts. It can be efficient but is more involved than the direct greedy scan.
- **Backtracking over group assignments:** The smallest-card argument makes choices forced, so exponential search is unnecessary.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n = len(hand)`. Building the Counter takes `O(n)` time. Sorting the hand takes `O(n\log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
