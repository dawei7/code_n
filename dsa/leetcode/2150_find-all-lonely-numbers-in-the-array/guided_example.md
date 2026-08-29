# Guided Example: Find All Lonely Numbers in the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 6, 5, 8]}`
- **Required output:** `[10, 8]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. A number `x` is **lonely** when it appears only **once**, and no **adjacent** numbers (i.e. $x + 1$ and $x - 1)$ appear in the array.

The objective is to compute `[10, 8]` from `{"nums": [10, 6, 5, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count every distinct value once

The source constructs `cnt = Counter(nums)`. For every value `x`, `cnt[x]` is its number of occurrences.

This first pass is necessary because seeing a value once during a left-to-right scan does not prove it will not appear again later. It also gives constant-time expected checks for neighboring values without searching the array repeatedly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 6, 5, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Iterate over distinct value-frequency pairs

The comprehension loops through `cnt.items()`, so each distinct value `x` is considered exactly once with its frequency `v`. Its filter is

`v == 1 and cnt[x - 1] == 0 and cnt[x + 1] == 0`.

The first comparison enforces uniqueness. A frequency of two or more immediately makes the value non-lonely, even if neither adjacent numeric value occurs.

The second and third comparisons require both adjacent values to be absent. Logical `and` short-circuits from left to right. If `v != 1`, Python does not need to evaluate the neighbor checks, though this affects only constant factors.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand missing Counter keys

For a normal dictionary, reading a missing key with square brackets raises `KeyError`. A `Counter` is different: a missing key reads as count zero.

Therefore `cnt[x - 1] == 0` means precisely that `x - 1` does not occur, and `cnt[x + 1] == 0` means `x + 1` does not occur. These missing-key reads do not insert new entries into the counter, so iterating through `cnt.items()` remains safe.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 8]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 6, 5, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 8]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the array:** After sorting, a value is lonely if it occurs once and differs by more than one from its immediate sorted neighbors. This costs $O(n\log n)$ time and needs careful boundary and duplicate handling.
- **Use a set plus a separate count:** A set handles neighbor membership, but uniqueness still requires counts. `Counter` supplies both in one structure.
- **Search the list for every value:** Repeated calls to count or membership can make the algorithm $O(n^2)$.
- **One element:** Its frequency is one and neither numeric neighbor occurs, so it is lonely.
- **Duplicate with absent neighbors:** It is not lonely because `v == 1` fails.
- **Unique value with one adjacent neighbor:** Either neighbor check failing is enough to reject it.
- **Both neighbors present:** The value is non-lonely regardless of all three frequencies.
- **Zero value:** The check for `-1` safely returns zero because negative numbers need not be legal input values to be queried as absent keys.
- **Maximum value one million:** Querying one million plus one is equally safe.
- **Consecutive chain:** In values such as `[4,5,6]`, none is lonely: endpoints each have one neighbor and the middle has two.
- **Gaps of two:** Values `x` and `x+2` do not disqualify one another because only differences of exactly one matter.
- **Any output order:** The comprehension’s order is acceptable; no sorting step is required.
- **Missing-key behavior:** Counter lookup returns zero and does not grow the mapping, avoiding mutation during `items()` iteration.
- **Input preservation:** All frequency and output storage is separate from `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length and $d$ the number of distinct values. Building the counter takes $O(n)$ expected time. The comprehension examines $d \le n$ entries and performs expected $O(1)$ counter lookups for each, taking $O(d)$ expected time. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
