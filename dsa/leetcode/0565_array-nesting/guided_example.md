# Guided Example: Array Nesting

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 4, 0, 3, 1, 6, 2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` where `nums` is a permutation of the numbers in the range `[0, n - 1]`.

The objective is to compute `4` from `{"nums": [5, 4, 0, 3, 1, 6, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

Because `nums` is a permutation of indices zero through `n - 1`, treating each index `i` as pointing to `nums[i]` creates a directed graph where every node has exactly one outgoing edge and exactly one incoming edge. Such a graph is a collection of disjoint cycles.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 4, 0, 3, 1, 6, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The set `s[k]` described by the problem is exactly the cycle reached by repeatedly following those pointers from index `k`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution visits each cycle once and records its length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 4, 0, 3, 1, 6, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Start a fresh traversal from every index:** Without global visited state, the same cycle is walked once per member and can take $O(n^2)$ time.
- **Mark in place:** Add `n` or use another sentinel in `nums` to avoid a visited array, but this mutates the input.
- **Use a set per start:** It detects repetition but allocates and repeats work unnecessarily.
- **Identity permutation:** Every cycle has length one.
- **One large cycle:** The first start marks every index and returns `n`.
- **Several equal-length cycles:** The maximum is unchanged whichever is discovered first.
- **Starting in the middle of a cycle:** It still visits every cycle member before returning.
- **Permutation guarantee:** It ensures disjoint pure cycles with no tails.
- **Visited starting index:** It is skipped because its full cycle was already counted.
- **Input immutability:** Separate `vis` preserves the original permutation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the permutation length. Although there is a while loop inside a for loop, each index is marked during exactly one cycle traversal. Total pointer advances across all starts are $O(n)$, and the outer checks are $O(n)$, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
