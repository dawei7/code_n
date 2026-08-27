# Guided Example: Least Number of Unique Integers after K Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [5, 5, 4], "k": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr` and an integer `k`. Find the *least number of unique integers* after removing **exactly** `k` elements**.**

The objective is to compute `1` from `{"arr": [5, 5, 4], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

**Eliminate complete value groups as cheaply as possible.** A distinct integer disappears only after every occurrence of it is removed. Spending removals on part of a frequency does not reduce the unique count. To eliminate the greatest number of distinct values, fully remove the smallest frequencies first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [5, 5, 4], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`Counter(arr)` maps each value to its occurrence count. The actual integer identities no longer matter because the objective counts how many identities remain, not which ones.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Counter(arr)` maps each value to its occurrence count.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The source sorts `cnt.values()` ascending. For each frequency `v`, it subtracts `v` from remaining budget `k`, conceptually trying to erase that whole value group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [5, 5, 4], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Min-heap frequencies:** Pop cheapest groups un:** - **Min-heap frequencies:** Pop cheapest groups until budget is insufficient. It has similar logarithmic processing.
- **Frequency-of-frequencies array:** Counts are at most `N`, enabling linear-time bucket processing with `O(N)` space.
- **Remove largest frequencies first:** This wastes budget and can leave more unique values.
- **k equals zero:** The first attempted subtraction becomes negative, returning all unique values.
- **k equals N:** Every group is removed and zero is returned.
- **One unique value:** It remains unless all its occurrences are removed.
- **All values unique:** Every frequency is one, so exactly `k` distinct values disappear.
- **Budget exactly matches a group:** `k` becomes zero and that group is correctly removed.
- **Partial current group:** It remains unique and is included in `len(cnt)-i`.
- **Tied frequencies:** Their order is irrelevant because their removal cost is equal.
- **Large integer values:** Hashing handles them without a bounded value array.
- **Input preservation:** Counter construction and sorting frequencies do not mutate `arr`.
- **Budget smaller than every frequency:** No value can disappear, so the original unique count is returned.
- **Partial removals are still required:** They can be spent after the greedy stopping point without decreasing the unique count.
- **Counter expected complexity:** The analysis assumes standard expected constant-time hashing.
- **Return zero:** It occurs only after every complete frequency group fits within the original removal budget.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let `N` be array length and `U` the number of unique values. Building the counter takes expected `O(N)` time and `O(U)` space.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
