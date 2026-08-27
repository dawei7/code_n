# Guided Example: Generate Binary Strings Without Adjacent Zeros

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3}`
- **Required output:** `["111", "110", "101", "011", "010"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`.

The objective is to compute `["111", "110", "101", "011", "010"]` from `{"n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

**Simplify the validity rule.** A length-two binary substring fails to contain at least one `"1"` only when it is `"00"`. Therefore a valid length-$n$ string is exactly a binary string with no adjacent zeros.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This is a prefix-local restriction. Whether zero may be appended depends only on the immediately preceding character, while one is always safe. Backtracking can build strings from left to right and reject an invalid branch before completing it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This is a prefix-local restriction.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Maintain one mutable prefix.** The list `t` contains the characters selected for positions $0$ through $i-1$ when `dfs(i)` begins. Lists support efficient append and pop operations, unlike repeatedly creating longer immutable strings at every internal node.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["111", "110", "101", "011", "010"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["111", "110", "101", "011", "010"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all $2^n$ bit strings:** Filter thos:** - **Enumerate all $2^n$ bit strings:** Filter those lacking `"00"`. It is simple but explores invalid branches that prefix pruning rejects immediately.
- **Iterative generation:** Start with `[""]` and append legal next bits to every current prefix. It avoids recursion but stores an entire frontier in addition to final outputs.
- **Dynamic programming for only the count:** Fibonacci DP returns $V_n$ in $O(n)$ time, but it does not satisfy the requirement to list the strings.
- **Start with zero:** The next position, if any, is forced to one.
- **Start with one:** Either bit may follow.
- **$n=1$:** Both `"0"` and `"1"` are valid because no length-two substring exists.
- **All ones:** Always appears because the one branch is never restricted.
- **Alternating starting with zero:** Always valid and appears through alternating forced/optional decisions.
- **No adjacent-zero post-check:** null is needed because invalid prefixes are never created.
- **Any-order contract:** Zero-first branching yields lexicographic order, but callers must not require that beyond this source's current loop order.
- **Mutable path snapshot:** Joining at the leaf is essential; appending `t` itself would store multiple references to one list that backtracking later changes.
- **Positive-$n$ guarantee:** The source would emit the empty string for $n=0$, but that case is outside the contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n V_n)$. Joining `t` costs $O(n)$ for each of the $V_n$ emitted strings, so output construction takes $O(nV_n)$ time. Internal valid-prefix nodes add $O(V_n)$-scale work and do not change the bound. This matches the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
