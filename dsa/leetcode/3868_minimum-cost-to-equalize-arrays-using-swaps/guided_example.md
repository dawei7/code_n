# Guided Example: Minimum Cost to Equalize Arrays Using Swaps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [10, 20], "nums2": [20, 10]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2` of size `n`.

The objective is to compute `0` from `{"nums1": [10, 20], "nums2": [20, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Free reordering removes all positional constraints

Within either array, any two positions can be swapped for free. Repeating free swaps can realize any permutation of that array. Therefore original indices do not matter for the final feasibility or paid cost; only the frequency of each value in each array matters.

Let `A_x` be the count of value `x` in `nums1` and `B_x` its count in `nums2`. If the final arrays are identical, they must contain the same count `T_x` of every value. Paid cross-array swaps preserve the combined number of copies, so

$$
2T_x=A_x+B_x.
$$

Thus the only possible target frequency is

$$
T_x=\frac{A_x+B_x}{2}.
$$

This immediately gives the feasibility condition: `A_x+B_x` must be even for every value. If any combined frequency is odd, it cannot be divided equally between two identical arrays.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [10, 20], "nums2": [20, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cancel copies already balanced between the arrays

The source begins with `cnt2 = Counter(nums2)` and an empty `cnt1`. It then scans `nums1`.

For a value `x`:

- if `cnt2[x]` is positive, one copy from `nums1` is matched with one copy from `nums2`, and the source decrements `cnt2[x]`;
- otherwise, `nums2` has no unmatched copy of `x` left, so this copy is an excess on the `nums1` side and `cnt1[x]` is incremented.

After every element of `nums1` is processed,

$$
\texttt{cnt1}[x]=\max(A_x-B_x,0)
$$

and

$$
\texttt{cnt2}[x]=\max(B_x-A_x,0).
$$

The counters no longer represent complete frequencies. They represent directional imbalance after all common copies have been canceled.

For example, if `nums1` contains five copies of `x` and `nums2` contains one, one pair is canceled, `cnt1[x]=4`, and `cnt2[x]=0`. The final equal split needs three copies on each side, so two of the four residual copies must move from the first array to the second.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source begins with `cnt2 = Counter(nums2)` and an empty ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every residual count must be even

For any value,

$$
A_x+B_x\equiv A_x-B_x\pmod2.
$$

Therefore the combined frequency is even exactly when the nonzero directional difference is even. The source checks every residual in both counters. If any `v` is odd, it returns minus one.

Zero entries that remain in `cnt2` are harmless because zero is even. Values absent from one counter have their positive residual in the other counter, where they are checked.

This parity test is sufficient as well as necessary. When every total can be halved, assigning `T_x` copies to each array gives a valid equal-frequency target for every value. The arrays have equal length, so those per-value target counts sum to the correct size.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [10, 20], "nums2": [20, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare sorted arrays only:** If sorting makes:** - **Compare sorted arrays only:** If sorting makes the arrays equal, cost zero. Otherwise sorting alone cannot determine how many cross-array transfers are needed unless frequency differences are then analyzed.
- **Build full frequency counters for both arrays:** Compute `A_x-B_x` directly for every key. This is equally correct and perhaps more algebraic; cancellation during the scan stores only unmatched copies.
- **Simulate indices and swaps:** Free permutations make particular indices irrelevant. Searching positional swap sequences adds unnecessary state and can become exponential.
- **Check only total multiset size:** Both arrays already have equal length, but each individual value's combined count must be even. A globally even number of elements is not enough.
- **Odd residual:** It makes equality impossible because half of the combined frequency would not be an integer.
- **Sum both surplus counters:** This doubles the paid cost. One exchange handles one outgoing surplus on each side simultaneously.
- **Already equal multisets:** All residuals are zero and the result is zero even if element orders differ.
- **Identical arrays:** They are a special zero-cost case handled by the same cancellation logic.
- **One value dominates one side:** A large even residual contributes half its size to the answer; each paid swap reduces the inter-array difference for that value by two.
- **Free operations before and after paid swaps:** They allow arbitrary surplus values to be aligned at a shared index and allow final equal multisets to be arranged identically.
- **Counter zero entries:** Decrementing matched counts may leave stored zeros. They neither affect parity nor the answer.
- **Hash-table complexity:** Counter operations are expected constant time. A fixed array indexed by values could give deterministic linear behavior under the bounded value domain.
- **Source mutation:** The method changes only its counters. Both input arrays remain untouched.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be each array length and `U` the number of distinct values across both arrays. Constructing `cnt2` and scanning `nums1` take expected `O(N)` time. Iterating through the two counters takes `O(U)` time, and `U\le2N`, so total expected time is `O(N)`.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
