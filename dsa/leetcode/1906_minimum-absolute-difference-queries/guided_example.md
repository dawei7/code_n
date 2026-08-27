# Guided Example: Minimum Absolute Difference Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 4, 8], "queries": [[0, 1], [1, 2], [2, 3], [0, 3]]}`
- **Required output:** `[2, 1, 4, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **minimum absolute difference** of an array `a` is defined as the **minimum value** of $|a[i] - a[j]|$, where $0 \le i < j < \text{a.length}$ and $a[i] \neq a[j]$. If all elements of `a` are the **same**, the minimum absolute difference is `-1`.

The objective is to compute `[2, 1, 4, 1]` from `{"nums": [1, 3, 4, 8], "queries": [[0, 1], [1, 2], [2, 3], [0, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Exploit the tiny value domain.** Array positions can reach $10^5$, but every value lies from 1 through 100. Instead of extracting and sorting each queried subarray, the algorithm asks which of these 100 possible values occurs inside the query. A fixed-size scan then computes the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 4, 8], "queries": [[0, 1], [1, 2], [2, 3], [0, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Build one prefix count per value.** `pre_sum[i][j]` is the number of occurrences of value `j` among the first `i` elements of `nums`, covering original indices zero through `i - 1`. Row zero is all zeros. For each later row and each value one through 100, the source copies the previous count and adds one exactly when `nums[i - 1] == j`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Build one prefix count per value.** `pre_sum[i][j]` is the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This table costs more memory than a single prefix sum, but it turns an arbitrary range-frequency question into one subtraction. Value zero receives an unused all-zero column because valid values begin at one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 4, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 4, 8], "queries": [[0, 1], [1, 2], [2, 3], [0, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 4, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort each queried subarray:** This repeats ext:** - **Sort each queried subarray:** This repeats extraction and sorting, potentially costing far more than the fixed 100-value scan across many queries.
- **Store positions for each value:** Binary-search whether each value has an occurrence in `[l,r]`. This uses $O(n)$ storage but adds logarithmic checks for each of 100 values.
- **Bitsets:** Presence in ranges can be accelerated with specialized bit operations, but prefix counts are straightforward and exact.
- **Duplicate-only range:** One present value leaves no unequal pair, so `-1` is returned.
- **Adjacent numerical values:** A gap of one is the smallest possible positive difference; later scanning cannot improve it, though the exact source continues through 100.
- **Query endpoints:** Adding one to `r` is essential for inclusive input. Omitting it would lose the final array element.
- **Value 100:** The table has 101 value columns, so index 100 is valid.
- **Unused value zero:** It remains zero and is intentionally skipped by loops starting at one.
- **Output order:** Queries are handled sequentially and answers are appended in the same order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+q)$. Let $n$ be the number of elements, $q$ the number of queries, and $V=100$ the value-domain size. Building the table processes every element-value pair in $O(nV)$ time. Each query scans all $V$ values, costing $O(qV)$. Total time is $O((n+q)V)$.
- **Auxiliary Space Complexity:** $O(nV)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
