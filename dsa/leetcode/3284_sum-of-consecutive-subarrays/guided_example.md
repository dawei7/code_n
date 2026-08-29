# Guided Example: Sum of Consecutive Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We call an array `arr` of length `n` **consecutive** if one of the following holds:

The objective is to compute `20` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

Every valid subarray is either strictly increasing by one at each step, strictly decreasing by one, or a singleton. The source aggregates values of all valid subarrays ending at each index without enumerating their starts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`f` is the length of the current plus-one run. `s` is the sum of the values of all increasing-consecutive subarrays ending at the current element. Symmetrically, `g` and `t` describe the minus-one run.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Initially the first singleton is both an increasing and decreasing run of length one, but it must be counted only once. The state variables start at one and `nums[0]`, while `ans` begins with `nums[0]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subarrays:** Checking every candidate takes at least $O(n^2)$ time.
- **Store run arrays:** Prefix lengths for both directions work but use $O(n)$ space; rolling state is sufficient.
- **Count only run lengths:** The task sums subarray values, not counts, so ending-value aggregates `s,t` are needed.
- **Single element:** The loop is empty and the initialized value is returned.
- **Difference plus one:** Only increasing aggregation runs; the singleton is included there.
- **Difference minus one:** Only decreasing aggregation runs.
- **Difference zero:** Neither direction qualifies, and only the singleton is added.
- **Direction reversal:** Both run states reset appropriately on the branch they do not extend.
- **Overlapping valid subarrays:** Ending aggregates intentionally count each distinct start separately.
- **Modulo:** Reducing contributions during accumulation is algebraically safe; the source reduces the running answer.
- **Missing `pairwise` import:** A standalone module needs `from itertools import pairwise` if the harness does not provide it.
- **Positive values:** State initialization uses actual first value and needs no empty-array case because length is at least one.
- **Meaning of `s` after extension:** It includes the singleton ending at `y` and every longer plus-one suffix. Adding it to `ans` counts all valid increasing subarrays by their unique right endpoint.
- **Why `f*y` is added:** There are `f-1` old suffixes to extend plus one new singleton. Each receives one new copy of `y` in its value, totaling exactly `f` copies.
- **Reset does not lose future information:** Once an adjacent difference fails, no earlier increasing suffix can cross it. The only possible increasing suffix ending at `y` starts with `y` itself.
- **Singleton ownership:** Exactly one of three paths counts `[y]`: the increasing aggregate, the decreasing aggregate, or the explicit nonconsecutive branch. The plus-one and minus-one tests cannot both be true.
- **Modulo and ending totals:** `s` and `t` need not be reduced for correctness because only their residues affect `ans`. Reducing them too would also be valid and could ease fixed-width ports.
- **Maximum intermediate scale:** Long runs can make ending aggregates much larger than individual values. Python integer arithmetic avoids overflow before the answer's modulo reduction.
- **Several separate runs:** Reset states ensure subarrays never cross a break, while `ans` retains contributions from earlier completed runs.
- **Pairwise availability:** The exact file assumes Python 3.10's `itertools.pairwise` or an equivalent harness import; older runtimes require a manual adjacent-index loop.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `pairwise(nums)` visits each adjacent pair once, and each iteration performs constant arithmetic. Time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
