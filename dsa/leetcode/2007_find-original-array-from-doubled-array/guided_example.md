# Guided Example: Find Original Array From Doubled Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"changed": [1, 3, 4, 2, 6, 8]}`
- **Required output:** `[1, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer array `original` is transformed into a **doubled** array `changed` by appending **twice the value** of every element in `original`, and then randomly **shuffling** the resulting array.

The objective is to compute `[1, 3, 4]` from `{"changed": [1, 3, 4, 2, 6, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process the smallest remaining value first

The changed array contains only nonnegative values. After sorting, the smallest unused value `x` cannot be the double of a smaller positive unused original value, because no smaller unused value exists. It must serve as an original value and be paired with `2x`.

This removes the ambiguity between treating a number as an original or as someone else's double.

The source sorts `changed` in place and builds `Counter(changed)` to track how many unused occurrences of each value remain.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"changed": [1, 3, 4, 2, 6, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Skip occurrences already consumed as doubles

The loop still iterates through every entry of the sorted list, including entries whose counter was reduced earlier when they served as a double.

If `cnt[x] == 0`, that occurrence is already fully accounted for, so the loop continues. Otherwise, one occurrence of `x` is selected as an original and its count is decremented.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Require and consume its double

The double is computed as `x << 1`, a left shift by one bit that equals `2 * x` for nonnegative integers.

If `cnt[2x] <= 0` after consuming the original occurrence, no unused double exists. The array cannot be partitioned into original-double pairs, so the method returns an empty list.

If it exists, the source decrements that count and appends `x` to `ans`.

The order of decrementing matters for zero. When `x=0`, its double is also zero. Consuming the original first means the second count check correctly requires another zero. An odd number of zeroes eventually fails.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"changed": [1, 3, 4, 2, 6, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Counting-array scan:** Values are bounded by $10^5$, so frequencies can be processed from zero upward in $O(N+V)$ time and $O(V)$ space.
- **Unsorted counter iteration:** Unsafe because deciding whether a value is original or a double requires magnitude order.
- **Backtracking pair choices:** Exponential ambiguity is unnecessary once the smallest remaining value is chosen.
- **Odd changed length:** Cannot be split into pairs and eventually returns empty.
- **Zero values:** Must occur an even number of times; consuming the original before checking its identical double enforces this.
- **Missing double:** Causes immediate failure because the smallest remaining value has no alternative role.
- **Duplicate originals:** Each occurrence consumes a distinct doubled occurrence through counter multiplicity.
- **Large values:** Their doubles may exceed the input value bound but absent counter entries safely read as zero.
- **Already valid sorted input:** Works identically; sorting preserves its order.
- **Answer order:** The exact method returns sorted originals, which is allowed.
- **Bit shift:** `x << 1` is exactly twice `x` for these nonnegative integers.
- **Input side effect:** The exact source sorts `changed` in place.
- **Environment import:** The solution assumes `Counter` is available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the changed-array length. Sorting takes $O(N\log N)$ time. Counter construction and the greedy scan take expected $O(N)$ time, so total is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
