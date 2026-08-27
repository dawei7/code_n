# Guided Example: Maximum Subarray XOR with Bounded Range

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 4, 5, 6], "k": 2}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a non-negative integer array `nums` and an integer `k`.

The objective is to compute `7` from `{"nums": [5, 4, 5, 6], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert every subarray XOR into two prefix XORs

Define:

$$
P[0]=0,
\qquad
P[t+1]=P[t]\mathbin{\mathrm{xor}}\texttt{nums}[t].
$$

Then the XOR of subarray `nums[l..r]` is:

$$
P[l]\mathbin{\mathrm{xor}}P[r+1].
$$

Every value before `l` appears in both prefixes and cancels under XOR.

For a fixed right endpoint `r`, `P[r + 1]` is fixed. Maximizing the subarray XOR means choosing the best eligible start-prefix `P[l]`.

The source builds all prefix XORs once in `prefix_xor`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 4, 5, 6], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Valid starts form a suffix for each right endpoint

The range condition is:

$$
\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r])\le k.
$$

If a window is valid, removing elements from its left cannot increase its maximum-minus-minimum range. Therefore every later start is also valid.

For each `r`, there is a smallest valid start `left`. All starts from `left` through `r` are eligible, and starts before `left` are not.

As `r` increases, extending a window cannot reduce its range. A previously invalid start cannot become valid again, so `left` only moves right. This gives a sliding window.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The range condition is:

$$
\max(\texttt{nums}[l..r])-\min(\... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the window maximum and minimum

`maximum_indices` is a deque of indices whose values decrease from front to back. Before appending `right`, the source removes back indices with value `<= value`. The new value is at least as large and remains in the window longer, so those older values can never again be needed as maxima.

Its front is the current maximum.

`minimum_indices` is symmetric: values increase from front to back, and back indices with value `>= value` are removed. Its front is the current minimum.

After appending the new index, the source can test current range in $O(1)$:

`nums[maximum_indices[0]] - nums[minimum_indices[0]]`.

While that exceeds `k`, it removes the current `left` from all maintained structures and increments `left`.

When an extreme deque's front equals the outgoing index, that front is popped. Other stored indices remain inside the new window.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 4, 5, 6], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all valid subarrays:** Maintaining r:** - **Enumerate all valid subarrays:** Maintaining range and XOR incrementally still requires $O(N^2)$ endpoint pairs.
- **Balanced range structure plus XOR scan:** Fast min/max alone is insufficient; scanning all eligible prefix XORs per endpoint remains quadratic.
- **Linear XOR basis:** A basis maximizes XOR over arbitrary combinations of values, not XOR with one selected prefix, so it solves a different problem.
- **k equals zero:** The valid window contains only subarrays whose values are all equal; the sliding range logic enforces this.
- **Singleton subarray:** It is always valid, ensuring at least one active trie prefix before each query.
- **Repeated prefix XOR values:** Node counts allow multiple active copies and prevent one deletion from removing all copies.
- **Zero-count trie nodes:** They remain allocated but are ignored by `maximum_xor`.
- **Duplicate extrema:** The monotonic deques keep the newest equal value, which expires later and preserves the correct range.
- **Value zero:** Its all-zero bit path is handled normally.
- **Inclusive range bound:** Shrinking occurs only when range is `> k`, so equality remains valid.
- **Fixed bit width:** Bits 14 through 0 cover both inputs and every prefix XOR because XOR cannot introduce a bit absent from all operands.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log V)$. Let $N=\lvert\texttt{nums}\rvert$ and $V=2^{15}$. Each prefix is inserted once and removed at most once. A trie update or query visits $\log_2V=15$ bits, costing $O(\log V)$.
- **Auxiliary Space Complexity:** $O(N log V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
