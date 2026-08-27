# Guided Example: Minimum Subsequence in Non-Increasing Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 3, 10, 9, 8]}`
- **Required output:** `[10, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `nums`, obtain a subsequence of the array whose sum of elements is **strictly greater** than the sum of the non included elements in such subsequence.

The objective is to compute `[10, 9]` from `{"nums": [4, 3, 10, 9, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rephrase the sum condition

Let $S$ be the sum of all array values and $T$ the sum of the chosen subsequence. The unchosen sum is $S-T$. The requirement is

$$
T>S-T,
$$

or equivalently $2T>S$.

We need the fewest selected elements that make this strict inequality true. Among solutions with that size, we need the greatest selected sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 3, 10, 9, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: For any fixed size, choose the largest values

Suppose a size-$r$ selection contains value $a$ while an unselected value $b>a$ exists. Replacing $a$ with $b$ increases the chosen sum without changing the size. Repeating this exchange shows that the maximum sum attainable with exactly $r$ elements is the sum of the $r$ largest array values.

Therefore it is enough to sort values in descending order and examine prefixes. No other size-$r$ subsequence can beat the descending prefix's sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose a size-$r$ selection contains value $a$ while an uns... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Grow the prefix until it crosses half

The code computes `s = sum(nums)` and initializes chosen sum `t = 0`. It iterates through `sorted(nums, reverse=true)`, adding each next-largest value to `t` and appending it to `ans`.

After every addition, `t > s - t` tests the original condition directly. The first time it succeeds, the loop stops.

For `[4,3,10,9,8]`, descending order is `[10,9,8,4,3]`. Choosing 10 alone gives selected sum 10 and remaining sum 24, so it fails. Adding 9 gives 19 against remaining 15, so `[10,9]` succeeds and is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 3, 10, 9, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort ascending and pop from the end:** It make:** - **Sort ascending and pop from the end:** It makes the same greedy choices but mutates a working list and is slightly less direct.
- **Max-heap:** Repeatedly extract the largest value until the sum condition holds. It also costs $O(n\log n)$ and needs heap construction.
- **Counting frequencies:** Values lie between one and 100, so scan a frequency array from 100 downward for $O(n+100)$ time.
- **Choose arbitrary large-enough subset:** It may satisfy the inequality but fail minimum size or maximum-sum tie breaking.
- **Equality of sums:** The algorithm must continue because the requirement is strictly greater.
- **Single element:** Selecting it leaves sum zero and succeeds immediately.
- **All equal values:** The method selects the smallest count whose total exceeds the remaining total; duplicates are preserved.
- **Duplicate maximum values:** Each occurrence can be chosen, and descending sorting keeps all needed copies.
- **All positive values:** This guarantees eventual success and monotonic chosen sum.
- **Already descending input:** `sorted` still creates a copy, but the greedy order is unchanged.
- **Input immutability:** Using `sorted` rather than `sort` leaves `nums` untouched.
- **Output ordering:** Appending from the descending scan directly satisfies non-increasing order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Computing the total takes $O(n)$ time. Sorting a copy takes $O(n\log n)$, and the prefix scan takes at most $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
