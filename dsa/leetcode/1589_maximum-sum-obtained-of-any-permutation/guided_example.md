# Guided Example: Maximum Sum Obtained of Any Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5], "requests": [[1, 3], [0, 1]]}`
- **Required output:** `19`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We have an array of integers, `nums`, and an array of `requests` where $\text{requests}[i] = [\text{start}_{i}, \text{end}_{i}]$. The $i^{\text{th}}$ request asks for the sum of $nums[\text{start}_{i}] + nums[\text{start}_{i} + 1] + ... + nums[\text{end}_{i} - 1] + nums[\text{end}_{i}]$. Both $\text{start}_{i}$ and $\text{end}_{i}$ are *0-indexed*.

The objective is to compute `19` from `{"nums": [1, 2, 3, 4, 5], "requests": [[1, 3], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rewrite all requests as position frequencies

The value placed at index `i` contributes to the total once for every request interval that covers `i`. If index `i` is covered `d[i]` times and the chosen permutation places value `v` there, that position contributes `v * d[i]`.

Therefore, the total over all requests can be rewritten as one dot product:

$$
\sum_{i=0}^{N-1}\text{value-at-position-}i\cdot\text{coverage}[i].
$$

The original request boundaries matter only for calculating coverage counts. After those counts are known, maximizing the total is an assignment problem: decide which number should receive which frequency.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5], "requests": [[1, 3], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Difference-array range updates

Incrementing every covered index separately would cost proportional to each request’s length. With up to $10^5$ requests of length up to $N$, that can be quadratic.

The solution uses `d` as a difference array. For inclusive request `[l, r]`, it performs:

- `d[l] += 1` to mark that coverage rises by one starting at `l`;
- if `r + 1 < n`, `d[r + 1] -= 1` to mark that the added coverage stops after `r`.

No subtraction sentinel is written when `r` is the last index because `d` has length exactly $N$. There is no following in-range position whose coverage must be reduced.

After all requests have deposited their boundary changes, the loop

`d[i] += d[i - 1]`

turns differences into prefix totals. At index `i`, the running sum contains one active increment for every request that started at or before `i` and has not ended before it. Thus `d[i]` becomes exactly the number of request intervals containing index `i`.

For requests `[[1,3],[0,1]]` over five positions, the final frequencies are `[1,2,1,1,0]`. Index one appears in both requests, indices zero, two, and three appear once, and index four appears in none.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why large values belong at high-frequency positions

After coverage counts are available, only the multiset of counts matters because `nums` may be permuted arbitrarily. The code sorts `nums` and `d` in ascending order, then pairs equal indices through `zip(nums, d)`.

This places the smallest values at the smallest frequencies and largest values at the largest frequencies. The rearrangement inequality proves that this pairing maximizes the dot product.

A simple exchange argument makes the reason beginner-friendly. Suppose two values satisfy $a\le b$, while two assigned frequencies satisfy $x\le y$. Pairing in the same order produces $ax+by$. Crossing them produces $ay+bx$. Their difference is:

$$
(ax+by)-(ay+bx)=(b-a)(y-x)\ge 0.
$$

Therefore, assigning the larger value to the larger frequency is never worse. If any arrangement contains an inverted pair—a smaller value assigned to a higher frequency than a larger value—swapping them does not decrease the total. Repeating such swaps leads to the sorted-with-sorted pairing used by the solution, so that pairing is optimal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `19` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5], "requests": [[1, 3], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `19` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Apply every request directly:** Incrementing coverage throughout each interval can take $O(RN)$ time. Difference markers reduce each interval to constant work.
- **Sort requests or sweep endpoints as events:** This can also recover coverage frequencies, but a fixed-index difference array is simpler because the domain is exactly zero through $N-1$.
- **Assign values greedily without sorting frequencies:** Repeatedly selecting the current largest value and largest count can be correct with heaps, but sorting both arrays is simpler and has the same dominant asymptotic cost.
- **Keep original index identities:** One can sort pairs of `(frequency, index)` to construct an actual optimal permutation. The checked-in method needs only the maximum sum, so identities are unnecessary.
- **Index covered by no request:** Its frequency is zero, so pairing it with a small value preserves larger values for positive frequencies. Its product contributes zero.
- **All positions covered equally:** Every permutation has the same total because all frequency multipliers are equal. Sorting still returns that value.
- **Duplicate requests:** Each copy independently increments coverage, which is correct because every request contributes separately to the total.
- **Single-position request:** The start increment and following decrement make only that position’s frequency rise.
- **Request ending at `n - 1`:** The code omits the out-of-range decrement. Prefix coverage correctly remains active through the final position.
- **Zero values in `nums`:** They naturally pair with the smallest frequencies and contribute zero.
- **Duplicate numbers or counts:** Any order within ties is optimal; sorting need not preserve identity.
- **Modulo timing:** Python safely sums the full value before reducing. Fixed-width languages should reduce during accumulation or use a sufficiently wide type.
- **Input mutation:** `nums.sort()` changes the original list. Pass a copy if later code needs the source ordering.
- **Inclusive endpoints:** The decrement occurs at `r + 1`, not `r`, because position `r` is part of the request.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $N$ be the length of `nums` and $R$ be the number of requests.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
