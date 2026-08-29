# Guided Example: Guess the Majority in a Hidden Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"reader": {"api": "majority", "array": [0, 0, 1, 0, 1, 1, 1, 1], "max_queries": 16}}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We have an integer array `nums`, where all the integers in `nums` are **0** or **1**. You will not be given direct access to the array, instead, you will have an **API** `ArrayReader` which have the following functions:

The objective is to compute `5` from `{"reader": {"api": "majority", "array": [0, 0, 1, 0, 1, 1, 1, 1], "max_queries": 16}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use query equality to compare hidden bits

The API reveals only whether a four-index sample contains four equal bits, a three-to-one split, or a two-to-two split. It does not reveal which bit is zero or one.

However, compare two queries that share three indices and differ only in the fourth. Their results are equal exactly when the two substituted hidden bits are equal. If the substituted bits match, the four-bit multisets are identical. If they differ, replacing a zero with a one or vice versa changes the balance category, so the returned value changes.

The solution uses this observation to classify every position relative to index three. It never needs to know whether `nums[3]` itself is zero or one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"reader": {"api": "majority", "array": [0, 0, 1, 0, 1, 1, 1, 1], "max_queries": 16}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Establish the reference query

`x = reader.query(0, 1, 2, 3)` records the distribution of the first four positions.

Counters `a` and `b` mean “same as index three” and “different from index three.” The initialization `a = 1` counts index three itself, while `b = 0` starts the opposite class empty.

Variable `k` stores an index known to be in the different class. It is updated whenever such an index is discovered. Its initial value does not matter if no different element exists, because it is returned only when the different class is larger.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Classify indices four and beyond

For every `i` from four through `n-1`, the source compares `query(0, 1, 2, i)` with `x`. These queries share indices zero, one, and two; they substitute `i` for index three.

Equal results mean `nums[i] == nums[3]`, so `a` increases. Different results mean the bits differ, so `b` increases and `k = i` records a representative.

This loop includes index four. Later, the code calls the same query `query(0, 1, 2, 4)` again and stores it as `y`. That duplicate call is part of the exact implementation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"reader": {"api": "majority", "array": [0, 0, 1, 0, 1, 1, 1, 1], "max_queries": 16}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cache the index-four query:** Reusing the loop result as `y` saves one call and gives $N$ total queries without changing the reasoning.
- **Try to decode actual bit values:** It is unnecessary; majority depends only on the sizes of the two equivalence classes.
- **Compare arbitrary queries:** Equality is informative for individual bits only when the queries share three indices and differ in exactly one.
- **Equal frequencies:** The code returns negative one before choosing either representative.
- **Reference class majority:** Index three is always a valid returned index when `a > b`.
- **Opposite class majority:** `k` has been assigned to a proven different position before it can be returned.
- **All bits equal:** Every classification joins `a`, and index three is returned.
- **Minimum length five:** All indices used by the fixed queries exist, and the query count is six, below the budget of ten.
- **Binary-domain requirement:** With more than two possible values, “different from index three” would not necessarily be one uniform class.
- **Valid query ordering:** Every call passes four distinct indices in strictly increasing order.
- **Symmetric query result:** The API does not distinguish zero-majority from one-majority, which is why relative comparison is the appropriate tool.
- **Interactive boundary:** The platform supplies `ArrayReader`; the solution must not implement or inspect it.
- **Follow-up minimum calls:** The exact source is budget-compliant but intentionally does not prove the theoretical minimum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the hidden array length. The loop performs $N-4$ iterations, and the remaining work uses a fixed number of API calls. With each query guaranteed $O(1)$, total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
