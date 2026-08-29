# Guided Example: People Whose List of Favorite Companies Is Not a Subset of Another List

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"favoriteCompanies": [["leetcode"], ["google"], ["facebook"], ["amazon"]]}`
- **Required output:** `[0, 1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `favoriteCompanies` where $\text{favoriteCompanies}[i]$ is the list of favorites companies for the `ith` person (**indexed from 0**).

The objective is to compute `[0, 1, 2, 3]` from `{"favoriteCompanies": [["leetcode"], ["google"], ["facebook"], ["amazon"]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Convert company names into compact set elements.** The problem is fundamentally about set containment, not list order. The source first assigns every distinct company string a unique integer identifier. Dictionary `d` maps a company name to its identifier, and `idx` supplies the next unused identifier.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"favoriteCompanies": [["leetcode"], ["google"], ["facebook"], ["amazon"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For each person's list, the corresponding set `nums[i]` receives those identifiers. If a company has appeared before, the existing identifier is reused, so equal names across people become equal set elements. If it is new, it receives a fresh number. The exact numeric value has no meaning beyond identity; uniqueness and consistency are what matter.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The input already guarantees that a person's company strings are distinct, but using a set still gives the representation needed for intersection and subset testing. It also makes the code robust to an accidental duplicate within one list because a repeated identifier would not change membership.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"favoriteCompanies": [["leetcode"], ["google"], ["facebook"], ["amazon"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use string sets directly:** Convert each list with `set(ss)` and test `nums[i] <= nums[j]`. This is shorter and avoids the identifier dictionary, while retaining the same asymptotic bounds.
- **Use issubset:** `nums[i].issubset(nums[j])` states the intention more directly and avoids explicitly materializing an intersection. It can reduce temporary allocation while performing the same membership logic.
- **Length precheck:** If `len(nums[i]) > len(nums[j])`, containment is impossible. Skipping the set test in that case can improve constants but not the worst-case bound.
- **Sort every company list:** A two-pointer subset test on sorted lists is possible, but sorting adds preprocessing and string comparisons. Hash sets provide direct membership.
- **Bit masks:** After integer encoding, each list could become a bitset and containment could use bit operations. This can be fast when the total company universe fits a practical bitset, but its storage model depends on universe size.
- **Compare only list lengths:** This is insufficient. A shorter set is not automatically a subset of a longer set.
- **One person:** There is no other list that can contain it, so `any` is false and index zero is returned.
- **All singleton lists with different companies:** No singleton intersects another as itself, so every index is returned.
- **A chain of nested lists:** Every set except the largest is excluded. The largest has no containing witness and remains.
- **Multiple containing witnesses:** The first one makes `any` stop. Exclusion does not depend on how many witnesses exist.
- **Shared companies without full containment:** A nonempty intersection is not enough. It must equal all of `nums[i]`.
- **Self-comparison:** `i != j` prevents the universal fact that every set contains itself from eliminating all indices.
- **Distinct-list guarantee:** Different people cannot have identical company sets. If identical sets were allowed, the implemented non-strict subset test would cause each to disqualify the other.
- **Input order inside a list:** Set conversion intentionally ignores it because subset membership has no ordering component.
- **Output order:** Scanning `i` upward already satisfies the required increasing indices.
- **Hash behavior:** Complexity assumes expected constant-time dictionary and set operations. Pathological collision behavior is outside the standard expected analysis.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(PC)$. Let `P` be the number of people and `C` the maximum number of companies in one person's list. Encoding visits at most `PC` list entries. Expected dictionary and set insertion take constant time per entry, so preprocessing is `O(PC)` expected time.
- **Auxiliary Space Complexity:** $O(PC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
