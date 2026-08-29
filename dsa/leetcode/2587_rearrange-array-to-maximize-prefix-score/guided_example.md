# Guided Example: Rearrange Array to Maximize Prefix Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, -1, 0, 1, -3, 3, -3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. You can rearrange the elements of `nums` to **any order** (including the given order).

The objective is to compute `6` from `{"nums": [2, -1, 0, 1, -3, 3, -3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Larger values should appear earlier

A value placed early contributes to many prefix sums. A value placed late contributes to only a few. To maximize how many prefixes stay positive, the most helpful values should be used first.

The solution sorts `nums` in descending order, then accumulates its running sum. It returns the number of positive prefixes before the first nonpositive one.

The critical reasoning is not merely that “positives come first.” Among all values, descending order never gives a smaller prefix sum at any length than another permutation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, -1, 0, 1, -3, 3, -3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Exchange proof for descending order

Suppose a permutation contains adjacent values $a<b$ in that order. Swap them to place $b$ first.

Every prefix ending before the pair is unchanged. The prefix ending after the first position of the pair increases by $b-a>0$. Every prefix containing both values is unchanged because their sum is the same.

Therefore swapping an ascending inversion cannot turn any positive prefix nonpositive and may turn one nonpositive prefix positive. Repeatedly removing all such inversions produces descending order without decreasing the score.

Hence some optimal arrangement is the descending sort used by the code.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Pointwise maximum-prefix interpretation

For any length $t$, the first $t$ elements of descending order are the $t$ largest values in the array. Their sum is the greatest total any $t$ chosen elements can have. Thus the sorted prefix sum is an upper bound on the prefix sum at position $t-1$ in every other permutation.

This gives another view of optimality: descending order makes every prefix as large as possible simultaneously.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, -1, 0, 1, -3, 3, -3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every permutation:** There are $n!$ orders; the adjacent-swap proof collapses the search to one sorted arrangement.
- **Put only positive values first:** This is directionally correct, but full descending order also optimally orders positives, zeros, and negatives.
- **Priority queue:** Repeatedly extracting the maximum reproduces descending order in $O(n\log n)$ time with explicit $O(n)$ heap space.
- **All negative:** The largest value still makes a nonpositive first prefix, so the answer is zero.
- **All zero:** Every prefix equals zero, and “positive” is strict, so the answer is zero.
- **Zeros after positive sum:** Each preserves positivity and increases the score by one.
- **Total sum positive:** Descending order keeps every prefix positive, so the score is $n$.
- **Duplicate values:** Their relative order is irrelevant and sorting handles them naturally.
- **Strict positivity:** The stopping test is `s <= 0`; a zero prefix does not count.
- **Input mutation:** Sort a copy when original ordering must be retained.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Sorting takes $O(n\log n)$ time, and the single running-sum scan takes $O(n)$ in the worst case. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
