# Guided Example: Longest Balanced Subarray I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 4, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `4` from `{"nums": [2, 5, 4, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count distinct values, not elements

A subarray is balanced when its number of distinct even values equals its number of distinct odd values. Repeated occurrences of the same number do not increase either side. For example, `[2, 2, 2, 3]` contains one distinct even value, two, and one distinct odd value, three, so it is balanced despite having three even elements and only one odd element.

This distinction determines the data the algorithm must maintain. For each candidate subarray, it needs to know whether a value has appeared before and how many first-time values belong to each parity group. It does not need the full occurrence frequency of every value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 4, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fix a left boundary and extend the right boundary

Every subarray is identified by a left endpoint `i` and a right endpoint `j`. The outer loop chooses each possible `i`. For that fixed left endpoint, the inner loop advances `j` from `i` through the end of the array, so the current candidate grows as

`nums[i:j + 1]`.

The solution creates two pieces of state for each new `i`:

- `vis` is the set of values already present in the current candidate.
- `cnt[0]` is the number of distinct even values, while `cnt[1]` is the number of distinct odd values.

Both start empty or zero because no value has been included before the first inner-loop iteration.

When `nums[j]` is appended, the code first checks `if nums[j] not in vis`. If the value is new to this particular subarray, it must increase exactly one of the two distinct counters. The expression `nums[j] & 1` evaluates to zero for an even integer and one for an odd integer, so

`cnt[nums[j] & 1] += 1`

updates the proper group. The value is then added to `vis` so later copies will not be counted again.

If the value is already in `vis`, neither distinct count changes. The candidate's length still increases because a new array position was included, but the set of distinct values is unchanged. This is why a later duplicate can make a longer balanced subarray even though it does not affect the balance equation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every subarray is identified by a left endpoint `i` and a ri... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Detect balance after each extension

After processing the newly included value, the condition

`cnt[0] == cnt[1]`

is exactly the problem's definition. The left side is the number of distinct even values in `nums[i:j + 1]`, and the right side is the number of distinct odd values in the same subarray. When they are equal, the candidate is balanced and its length is `j - i + 1`.

The code updates

`ans = max(ans, j - i + 1)`

so `ans` always holds the longest balanced candidate encountered so far. It does not stop after finding one balanced ending for a fixed `i`. Extending farther may introduce matched new even and odd values or only duplicates, creating an even longer balanced subarray.

Consider the fixed-left scan of `[3, 2, 2, 5, 4]`:

| Current candidate | New distinct value? | Distinct evens | Distinct odds | Balanced? |
| --- | --- | ---: | ---: | --- |
| `[3]` | 3, yes | 0 | 1 | No |
| `[3, 2]` | 2, yes | 1 | 1 | Yes |
| `[3, 2, 2]` | 2, no | 1 | 1 | Yes |
| `[3, 2, 2, 5]` | 5, yes | 1 | 2 | No |
| `[3, 2, 2, 5, 4]` | 4, yes | 2 | 2 | Yes |

The duplicate two leaves both counters unchanged, but the length grows from two to three while the candidate remains balanced. The final new even value restores equality and makes the whole length-five array balanced.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 4, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rebuild sets for every endpoint pair:** Constr:** - **Rebuild sets for every endpoint pair:** Constructing the distinct even and odd sets from scratch for each subarray adds up to $O(n)$ work per pair and $O(n^3)$ total time. Extending the right boundary reuses everything learned for the shorter candidate.
- **Store two sets instead of `vis` and `cnt`:** Separate even and odd sets also work, and their sizes directly express the balance condition. The exact source uses one set plus two integer counts, which avoids choosing a set twice and stores each value only once.
- **Maintain occurrence counts while sliding the left boundary:** A more advanced method can update distinct counts as both boundaries move, but finding the globally longest equality is not a standard monotonic sliding-window problem. The larger version requires a more sophisticated segment-tree treatment; simple shrinking decisions can miss answers.
- **Compare counts of even and odd elements:** This solves a different problem. Duplicates must contribute only once, so an array such as `[2, 2, 2, 3]` demonstrates why raw parity totals are wrong.
- **All values have the same parity:** Every nonempty subarray has at least one distinct value of that parity and zero of the other, so no balance occurs. `ans` correctly remains zero.
- **One even and one odd value with duplicates:** Any subarray containing both distinct values and no additional unmatched distinct value is balanced regardless of their occurrence counts.
- **A duplicate at the right endpoint:** The distinct counters do not change, but the new longer length must still be tested. The code performs the equality check on every iteration, not only when a new value appears.
- **The same numeric value cannot belong to both groups:** Integer parity is fixed. A single `vis` set is sufficient because every first appearance maps unambiguously to `cnt[0]` or `cnt[1]`.
- **Single-element array:** Its one distinct value is either even or odd, so the counts are one and zero. The method returns zero, matching the absence of a balanced nonempty subarray.
- **Negative or zero values:** The stated input contains positive integers. Python's low bit still classifies other integers, but the approach relies only on parity and would conceptually extend; no extra handling is needed for the actual contract.
- **Large numeric values:** Set operations depend on how many values are stored, not on the maximum value `10^5`. No value-indexed array of that size is required.
- **Overlapping optimal candidates:** Every left boundary receives an independent scan, so overlapping, nested, and duplicate-containing subarrays are all evaluated without conflict.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the number of elements. For left endpoint zero, the inner loop runs `n` times; for left endpoint one, it runs `n - 1` times; and so on. The total number of candidate extensions is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
