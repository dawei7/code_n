# Guided Example: Sum of Unique Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. The unique elements of an array are the elements that appear **exactly once** in the array.

The objective is to compute `4` from `{"nums": [1, 2, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: “Unique” means frequency one, not merely distinct

The central distinction is between a value that appears in the array and a value that appears exactly once. A set can identify distinct values, but it discards how many times each value occurred. This problem needs the complete frequency of each number before deciding whether that number contributes to the sum.

The exact solution uses `Counter(nums)`. A Python `Counter` is a dictionary-like mapping from each distinct value to its occurrence count. If a number occurs once, its stored count is one. If it occurs two or more times, it must contribute nothing, regardless of how large or small it is.

For `nums = [1,2,3,2]`, the counter conceptually contains one mapped to one, two mapped to two, and three mapped to one. Values one and three satisfy the exact-frequency test, so their sum is four.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count first because future elements can change eligibility

It is tempting to add a value the first time it appears. That is not enough by itself because a later duplicate can make the earlier contribution invalid. For instance, after reading the first two in `[2,3,2]`, two appears unique so far, but it is not unique in the complete array.

Building all counts first separates two concerns cleanly:

- The counting pass discovers the final frequency of every distinct value.
- The aggregation pass includes only keys whose final frequency equals one.

This makes the correctness condition visible in the code rather than requiring compensating updates when second or later occurrences arrive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Read the generator expression from left to right

The return statement is:

`sum(x for x, v in cnt.items() if v == 1)`.

`cnt.items()` produces each distinct number and its count as a pair `(x, v)`. The filter `if v == 1` retains exactly those pairs whose number occurred once. The generator yields only `x`, not its count. Finally, `sum` adds the yielded values.

The generator is lazy. It does not allocate a separate list of unique values before summing. At any moment, it only needs the current mapping entry and the running total maintained by `sum`.

The order in which the counter entries are visited does not matter because integer addition is independent of order. The task asks for one total, not for the unique values in their original positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed frequency array:** Use 101 counters indexed by value. It provides deterministic constant-time updates and makes the bounded-domain space explicit, but is less flexible than `Counter`.
- **Set only:** A plain set loses occurrence counts and would incorrectly include values that repeat.
- **Nested counting:** Calling `nums.count(x)` for every element is simple but can take $O(n^2)$ time.
- **One-pass adjusted sum:** Add a value on its first occurrence and subtract it on its second. This can work with frequency tracking, but later occurrences add state-transition complexity.
- **All values unique:** Every counter entry passes, so the answer is the ordinary array sum.
- **No unique values:** The generator is empty and `sum` returns zero.
- **One-element array:** Its only frequency is one, so that element is returned.
- **A value appearing twice:** It is fully excluded, not counted once.
- **A value appearing many times:** Count magnitude beyond one does not matter to the filter.
- **Same numeric total from different sets:** Only the sum is returned; the solution need not preserve which unique values formed it.
- **Positive-value constraint:** There is no cancellation between positive and negative unique values, although the counter method would still work if negatives were allowed.
- **Bounded domain:** At most 100 counter entries justify the stated $O(1)$ space.
- **Input preservation:** `Counter` reads `nums` and does not reorder or modify it.
- **Hash behavior:** The $O(n)$ time is the standard expected bound for Python dictionary-based counting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums` and $U$ the number of distinct values. Constructing `Counter(nums)` processes all $n$ elements and takes expected $O(n)$ time using hash-table operations. Iterating through `cnt.items()` takes $O(U)$ time. Since $U \le n$, total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
