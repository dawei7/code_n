# Guided Example: Permutations III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4}`
- **Required output:** `[[1, 2, 3, 4], [1, 4, 3, 2], [2, 1, 4, 3], [2, 3, 4, 1], [3, 2, 1, 4], [3, 4, 1, 2], [4, 1, 2, 3], [4, 3, 2, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are **both** odd or **both** even.

The objective is to compute `[[1, 2, 3, 4], [1, 4, 3, 2], [2, 1, 4, 3], [2, 3, 4, 1], [3, 2, 1, 4], [3, 4, 1, 2], [4, 1, 2, 3], [4, 3, 2, 1]]` from `{"n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

**Build only parity-valid prefixes.** A permutation is alternating when adjacent numbers have different parity. The source constructs permutations left to right and refuses any choice that would put two odd values or two even values together.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`t` is the current prefix. `vis[j]` records whether number `j` from $1$ through $n$ is already used. The recursive parameter `i` is the next position, which also equals `len(t)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

At each position, the loop considers `j` in increasing numeric order. A choice is legal when:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2, 3, 4], [1, 4, 3, 2], [2, 1, 4, 3], [2, 3, 4, 1], [3, 2, 1, 4], [3, 4, 1, 2], [4, 1, 2, 3], [4, 3, 2, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2, 3, 4], [1, 4, 3, 2], [2, 1, 4, 3], [2, 3, 4, 1], [3, 2, 1, 4], [3, 4, 1, 2], [4, 1, 2, 3], [4, 3, 2, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all permutations then filter:** It explores every one of $n!$ leaves even when parity fails near the front. Immediate pruning avoids most invalid branches.
- **Choose from separate odd/even lists:** Alternating between parity pools can reduce candidate scans, but numeric merge order must be handled carefully to preserve lexicographic output.
- **Sort results afterward:** It is unnecessary because ascending candidate order already emits lexicographically.
- **Odd \(n\):** There is one extra odd number, so complete solutions start with odd. Even-start branches die naturally.
- **Even \(n\):** Odd and even counts match, so valid permutations may start with either parity.
- **\(n=1\):** The singleton permutation is valid because it has no adjacent elements.
- **Copy at completion:** Appending `t` without slicing would store a mutable shared object and corrupt all answers.
- **Visited restoration:** Failing to clear `vis[j]` after recursion would incorrectly ban that number from sibling branches.
- **Parity restoration:** Popping `t` restores the previous last value, so sibling legality checks use the correct prefix.
- **Complexity terminology:** Output size is substantial, but the exact nested candidate scans also visit prefixes that never become outputs; they should be included in a literal runtime analysis.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A n)$. Let $A$ be the number of alternating permutations returned, and let $P$ be the number of valid prefixes visited, including dead-end prefixes. Copying the $A$ outputs costs $O(An)$. At each non-leaf prefix, the source scans all $n$ candidate numbers, so exact search overhead is $O(nP)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
