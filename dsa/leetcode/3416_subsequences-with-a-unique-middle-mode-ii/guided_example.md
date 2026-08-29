# Guided Example: Subsequences with a Unique Middle Mode II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 1, 1, 1]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

The objective is to compute `6` from `{"nums": [1, 1, 1, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Fix the middle index and choose two positions on each side.** A length-$5$ subsequence whose middle element is `nums[index]` must choose exactly two earlier indices and two later indices. Let the middle value be $x$, let $L$ be the number of positions on the left, and let $R$ be the number on the right. There are

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

total ways to choose those four surrounding positions. The source counts all of them and subtracts precisely the choices in which $x$ is not the unique mode.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Let $l_v$ and $r_v$ be the frequencies of value $v$ on the left and right of the middle. In particular, write $a=l_x$ and $b=r_x$. The `left` and `right` counters maintain these frequencies while the middle index moves.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate five indices:** Directly checking every length-$5$ subsequence costs $O(n^5)$ and is impossible for $n=10^5$.
- **Loop over distinct values per middle:** The same formulas can be computed from counters by summing all values each time, but this degrades to $O(n^2)$ when values are mostly distinct.
- **Count valid patterns directly:** Valid cases can also be divided by the number of extra middle values, but the exactly-one case remains intricate. Total-minus-invalid produces compact disjoint formulas.
- **All values equal:** Every choice of five indices is valid. The subtraction terms become zero, yielding $\binom n5$ across all middle positions, as in the first example.
- **All values distinct:** The middle appears once and ties every other value, so every selection is included in the no-extra-$x$ invalid term and the result is zero.
- **Mode ties:** Appearing twice is insufficient if another value also appears twice. The duplicate-triple formulas exist specifically to remove those ties.
- **Negative and large values:** Counter keys can be any integers; the algorithm depends on equality and frequency, not numeric magnitude.
- **Too few positions on one side:** `choose_two(0)` and `choose_two(1)` are zero, so edge middle indices contribute nothing without separate branches.
- **Nonnegative subtraction:** The combinatorial derivation guarantees `total - invalid` counts real selections. Applying modulo also safely normalizes the accumulated answer.
- **Current occurrence placement:** The middle must be removed from `right` before counting and added to `left` afterward. Reversing either step would allow the same index to be selected as both middle and side element.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{nums}\rvert$. Building the initial counter and initial right-pair sum takes $O(n)$ expected time. Each middle index performs a constant number of expected-$O(1)$ counter accesses and integer arithmetic operations; it never loops over distinct values. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
