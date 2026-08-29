# Guided Example: Longest Subarray With Maximum Bitwise AND

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 3, 2, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of size `n`.

The objective is to compute `2` from `{"nums": [1, 2, 3, 3, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First identify the largest possible AND value

The phrase “maximum possible bitwise AND of any non-empty subarray” initially suggests examining many subarrays. The key simplification comes from a basic property of bitwise AND. For non-negative integers, AND can only keep a bit that is present in every operand. It cannot introduce a new 1-bit. Consequently, the AND of a subarray is less than or equal to every element in that subarray.

Let

`mx = max(nums)`.

The one-element subarray containing any occurrence of `mx` has bitwise AND exactly `mx`, so the maximum achievable AND is at least `mx`. On the other hand, every subarray's AND is no greater than each of its elements and therefore no greater than the array maximum `mx`. Combining the lower and upper bounds proves that the maximum possible AND value is exactly `mx`.

This reasoning depends on subarrays being non-empty and the values being positive as specified. A singleton is a legal subarray, and the bitwise AND of a singleton is simply its sole value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 3, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Which longer subarrays can still have AND equal to the maximum

Knowing the target value is `mx` is only half of the problem; the algorithm must determine which multi-element subarrays have that AND. If a subarray contains a value `x < mx`, then its total AND is at most `x` and therefore strictly below `mx`. Such a subarray cannot qualify.

No array element can be larger than `mx` by definition. It follows that every element in a qualifying subarray must be exactly `mx`. Conversely, ANDing `mx` with itself any number of times leaves `mx` unchanged. Thus a subarray has the maximum possible AND if and only if it is a contiguous run consisting entirely of the array maximum.

The original bitwise problem has now become a simple sequence problem: find the longest consecutive run of `mx`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Measure one run at a time

The solution initializes `ans = cnt = 0`. The variable `cnt` is the length of the run of maximum values ending at the element currently being processed. The variable `ans` is the largest such run seen anywhere in the processed prefix.

For each `x` in `nums`:

- When `x == mx`, the current maximum-only run extends by one, so `cnt` increases. The code then updates `ans` with `max(ans, cnt)`.
- When `x != mx`, this position cannot belong to a qualifying subarray. It breaks any run that ended immediately before it, so `cnt` resets to zero.

The reset is essential because the required object is a subarray, which must be contiguous. Two groups of maximum values separated by a smaller value cannot be combined.

For `nums = [1, 2, 3, 3, 2, 2]`, `mx` is 3. The counters remain zero for 1 and 2. The first 3 makes `cnt` equal 1 and `ans` equal 1; the next 3 makes both equal 2. The following 2 resets `cnt`, while `ans` stays 2. The returned length is therefore 2.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 3, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subarrays:** Compute an AND for every start and end position. Even with a running AND per start, this takes $O(n^2)$ time and ignores the decisive fact that a singleton maximum establishes the target immediately.
- **Track distinct subarray AND values:** A common technique maintains the small set of AND results for subarrays ending at each position. It is useful when the target or number of distinct results matters, but it is unnecessary here because the maximum target collapses to the array maximum.
- **One-pass maximum and streak tracking:** When a larger value appears, replace the known maximum and reset the best and current streaks; handle equal and smaller values appropriately. This remains $O(n)$ and $O(1)$, but the exact two-pass solution is easier to verify.
- **Binary search on a length:** Testing whether a qualifying subarray of length $L$ exists would still reduce to finding a run of `mx` and would add needless logarithmic searches.
- **One element:** Its singleton subarray is legal and has the maximum AND, so the result is 1. The scan increments `cnt` once and returns 1.
- **All values equal:** Every element is `mx`, `cnt` grows to $n$, and the whole array is correctly selected.
- **Maximum appears only once:** The longest run has length 1 even if many smaller values share bits with the maximum. Any smaller operand makes the AND no greater than that smaller value.
- **Separated maximum values:** Runs on opposite sides of a smaller element cannot be joined because a subarray must be contiguous. Resetting `cnt` at the separator enforces this.
- **Bit patterns that seem compatible:** A smaller number may contain many of the maximum's 1-bits, but it is still numerically below `mx`, and the subarray AND is at most that operand. It therefore cannot keep the target value.
- **Positive-value constraint:** The proof uses the ordinary ordering property of bitwise AND for non-negative integers. The given values are positive, so signed negative-integer behavior never enters the problem.
- **Maximum constraint size:** With up to $10^5$ elements, the linear scan is suitable, while quadratic subarray enumeration would be far too slow.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Finding `mx` with `max` visits $n$ elements and takes $O(n)$ time. The following loop visits $n$ elements and performs constant-time comparisons, assignments, increments, and maximum updates. Total time is $O(n) + O(n) = O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
