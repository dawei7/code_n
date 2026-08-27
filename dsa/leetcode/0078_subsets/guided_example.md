# Guided Example: Subsets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0]}`
- **Required output:** `[[], [0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The objective is to compute `[[], [0]]` from `{"nums": [0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every element creates one binary decision

A subset either contains `nums[i]` or it does not. There is no third possibility, and because the input elements are unique, choosing the same membership decisions always identifies the same subset. The recursion explores these two choices for indices from zero through `len(nums) - 1`.

`dfs(i)` means that decisions for indices before `i` have already been made, and the mutable list `t` contains exactly the elements included by those decisions. The source first explores exclusion by calling `dfs(i + 1)` without changing `t`. It then appends `nums[i]`, explores inclusion with another `dfs(i + 1)`, and pops the element to restore the parent state.

Exploring exclusion first affects only output order. The contract accepts any order, so the algorithm could reverse these branches without changing the set of answers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The recursion tree is the power set

At depth zero there is one undecided path. After the first element there are two paths: absent or present. After two elements there are four membership patterns, and after `n` elements there are $2^n$ leaves. Each root-to-leaf path is a length-`n` binary pattern whose zero/one choices specify a subset.

For `nums = [1, 2, 3]`, the all-exclude path reaches `[]`. A path excluding 1, including 2, and including 3 reaches `[2, 3]`. The all-include path reaches `[1, 2, 3]`. Every possible membership pattern occurs exactly once.

This tree explains why exponential work cannot be avoided: the required output itself contains $2^n$ different lists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At depth zero there is one undecided path.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record only at a complete decision path

When `i == len(nums)`, every input position has a decided membership state. The current `t` is therefore one complete subset, including possibly the empty subset. The source appends `t[:]`, a copy, and returns.

The copy is essential. All calls share and mutate the same working list. If the algorithm appended `t` directly, stored entries would refer to that one object and later appends or pops would change earlier answers. Slicing creates an independent list whose contents remain fixed.

Unlike combinations of a fixed size, there is no success condition based on `len(t)`. Every length from zero to `n` is valid, so the only leaf condition is that all elements have been considered.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[], [0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[], [0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Cascading iteration:** Start with `[[]]`; for :** - **Cascading iteration:** Start with `[[]]`; for each value, copy every existing subset and append that value. It produces the same doubling pattern without recursion.
- **Bitmask enumeration:** Treat integers from zero through $2^n-1$ as membership patterns. It is compact and directly exposes the one-bit-per-element correspondence.
- **Backtrack and append at every node:** Record `t` immediately, then loop over possible next indices. This visits one node per subset and avoids explicit exclude calls.
- **Input of length one:** The two leaves are the empty subset and the singleton.
- **Empty subset:** The all-exclude path records it automatically.
- **Full subset:** The all-include path records every input element.
- **Negative values:** Membership decisions depend on positions, not numeric magnitude or sign.
- **Original order:** Selected elements retain input order because indices only increase.
- **Unique-element guarantee:** It ensures distinct decision patterns yield distinct value subsets.
- **Copying:** `t[:]` is mandatory because `t` is later mutated by backtracking.
- **Any output order:** Exclusion-first DFS order is acceptable and needs no sorting.
- **Maximum length ten:** At most 1024 subsets are generated, but the general complexity remains exponential.
- **Input preservation:** The source never sorts or modifies `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\cdot2^n)$. There are $2^n$ output subsets. Copying a leaf list can cost up to $O(n)$, and across the complete power set each input value appears in exactly half the subsets, for $n2^{n-1}$ stored elements. Total time is $\Theta(n2^n)$, matching the manifest's $O(n\cdot2^n)$ bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
