# Guided Example: Find All Numbers Disappeared in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}`
- **Required output:** `[5, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of `n` integers where $\text{nums}[i]$ is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

The objective is to compute `[5, 6]` from `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the known range matters

If the possible values were unrestricted, observing the input would not tell us which unobserved integers were supposed to be reported. Here the domain `[1, n]` defines the complete checklist. Once the set of observed values is available, scanning that checklist is sufficient: a candidate is missing exactly when the set does not contain it.

The code uses `range(1, len(nums) + 1)`. Python's upper endpoint is excluded, so this produces `1, 2, ..., n` and includes `n` itself. Starting from `1` also matches the problem's one-based value domain; zero is not a candidate and is never returned.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the comprehension forms the answer

The expression

`[x for x in range(1, len(nums) + 1) if x not in s]`

visits candidates in increasing order. For each candidate, the condition keeps it only when the set has no matching value. Consequently, the result is automatically sorted in ascending order even though the input may be in any order. The problem does not require a special ordering operation, and no final sort is needed.

For `nums = [4,3,2,7,8,2,3,1]`, the set becomes `{1,2,3,4,7,8}`. The candidate scan makes the following decisions:

- `1`, `2`, `3`, and `4` are in the set, so they are skipped.
- `5` and `6` are absent, so they are appended.
- `7` and `8` are present, so they are skipped.

The returned list is `[5,6]`.

In `nums = [1,1]`, the array length is two, so the candidate domain is `{1,2}`. The duplicate `1` creates only one set entry. Candidate `1` is present, while candidate `2` is absent, yielding `[2]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why duplicates imply missing values but require no special case

There are exactly `n` array positions and exactly `n` possible values. When one value appears more than once, at least one other value must be absent. The algorithm does not need to match a particular duplicate to a particular missing number. Set construction removes the repeated copies, and the complete domain scan independently identifies every gap.

The same reasoning handles several duplicates or several missing values. If the set has `u` distinct members, exactly `n - u` candidates from `[1, n]` are absent, and the returned list has that length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **In-place sign marking:** For each value `v`, use index `abs(v) - 1` as its presence slot and make that slot negative. A final scan reports positive slots. This satisfies the follow-up in $O(n)$ time and $O(1)$ auxiliary space, but it mutates `nums` and requires `abs` because earlier visits may have changed signs.
- **Cyclic placement:** Repeatedly swap each value `v` toward index `v - 1`; positions that do not contain their canonical values reveal missing numbers. It also uses $O(1)$ auxiliary space and $O(n)$ total swaps, but its duplicate stopping condition is easier to get wrong.
- **Boolean presence array:** A length-`n` Boolean list makes indexing explicit and has deterministic $O(n)$ time, but still consumes $O(n)$ auxiliary space.
- **Sort first:** Sorting allows gaps to be detected, but comparison sorting costs $O(n\log n)$ time and may mutate the input. It provides no advantage over a set for the exact implementation's goals.
- **Every value appears:** The set contains the full domain, every membership test succeeds, and the result is the empty list.
- **One-element input:** The only permitted value is `1`, so `[1]` produces no missing numbers.
- **Many copies of one value:** Duplicates collapse into one set entry; every other candidate is returned once, in increasing order.
- **Output order:** The set itself is unordered, but the solution never iterates over it. Iterating over `range(1, n + 1)` guarantees ascending output.
- **Out-of-range input:** The exact code would ignore an extra out-of-range value when scanning candidates, but the contract guarantees such values never occur; correctness relies on that domain guarantee.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Constructing `set(nums)` processes all $n$ elements. Under the standard expected-cost model for Python hash tables, each insertion takes expected $O(1)$ time, so set construction takes expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
