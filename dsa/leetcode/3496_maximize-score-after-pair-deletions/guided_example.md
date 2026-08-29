# Guided Example: Maximize Score After Pair Deletions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 1]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums`. You **must** repeatedly perform one of the following operations while the array has more than two elements:

The objective is to compute `6` from `{"nums": [2, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**The score is everything removed, so focus on what remains.** Every operation adds the values of the two removed elements. No element is removed twice, and operations stop when the array has at most two elements. Therefore,

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\text{score}
=
\sum\texttt{nums}
-
\text{sum of the final remaining elements}.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The total array sum is fixed. Maximizing the score is equivalent to minimizing the sum of a remainder that can actually be left by the allowed end deletions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Interval dynamic programming:** It can model all operations but costs at least quadratic time when final-remainder reachability gives a linear formula.
- **Greedily remove the largest current pair:** A locally large removal may force an unfavorable final remainder; optimizing the remainder globally is simpler.
- **Leave any two elements for even \(n\):** Only adjacent original elements can form the final contiguous interval.
- **Odd length:** Exactly one element remains because removing two preserves odd parity.
- **Even length:** Exactly two remain, including the initial $n=2$ case.
- **One element:** No operation runs; total minus that same minimum returns zero.
- **Two elements:** The only adjacent-pair sum equals the total, so the score is zero.
- **Negative minimum singleton:** Leaving it can increase the score above the whole-array sum, which is mathematically valid.
- **Negative adjacent pair:** The best score may similarly exceed the original sum by leaving that negative pair.
- **All equal values:** Every reachable remainder has the same sum, so every complete sequence ties.
- **Lazy `pairwise`:** It enumerates consecutive values only and keeps constant memory.
- **Reachability parity:** Side counts around a target singleton or pair have the same parity, enabling either same-side removals or one initial cross-end removal.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `sum(nums)` scans all $n$ elements. For odd length, `min(nums)` performs another linear scan. For even length, `pairwise` yields $n-1$ adjacent pairs and the generator computes each sum once before `min` chooses the smallest. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
