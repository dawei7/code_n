# Guided Example: Rotate Non Negative Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -2, 3, -4], "k": 3}`
- **Required output:** `[3, -2, 1, -4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `[3, -2, 1, -4]` from `{"nums": [1, -2, 3, -4], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate movable values from fixed positions

Negative values are barriers only in the layout: they must remain at their exact indices, but they do not divide the non-negative values into independent rotation groups. Reading all non-negative values from left to right produces one logical sequence that rotates as a whole.

The source extracts that sequence with

`t = [x for x in nums if x >= 0]`.

Zero is included because “non-negative” means greater than or equal to zero. Every negative number is excluded from `t` but remains in `nums` for later preservation.

Let $M=\lvert\texttt{t}\rvert$. The relative positions available for reinsertion are exactly the $M$ indices that originally contained non-negative values. Rotating `t` and writing it back to those positions completely describes the requested transformation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -2, 3, -4], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map each source position to its left-rotated destination

A left rotation by one moves the element at logical index 0 to index $M-1$, index 1 to 0, index 2 to 1, and so on. More generally, the element originally at logical index `i` moves to

$$
(i-k)\bmod M.
$$

The source allocates `d = [0] * m` for the rotated sequence and performs

`d[((i - k) % m + m) % m] = x`

for every `(i, x)` in `t`. This writes each original non-negative value directly into its destination.

Modulo makes rotation cyclic. If `i - k` is negative, wrapping sends it to the end of `d`. If `k >= M`, only `k % M` affects the destination, so the code automatically normalizes arbitrarily large allowed rotations.

In Python, `(i - k) % m` is already nonnegative when `m > 0`, so the added `+ m` and second modulo are redundant. They express the common language-independent normalization

$$
((i-k)\bmod M+M)\bmod M,
$$

which is needed in languages whose remainder for a negative dividend may remain negative.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A left rotation by one moves the element at logical index 0 ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The destination mapping is a permutation

For fixed `k` and positive `M`, two different logical indices cannot map to the same destination modulo $M$. If

$$
(i_1-k)\bmod M=(i_2-k)\bmod M,
$$

then $i_1\equiv i_2\pmod M$. Both indices lie between 0 and $M-1$, so they must be equal. Every destination receives exactly one value.

This ensures the zero placeholders in `d` are all overwritten before reinsertion. They are only allocation placeholders; they are not confused with real zero values.

The mapping also preserves the cyclic order. The value from source index `k % M` lands at destination 0, the next source value lands at destination 1, and so on, which is precisely a left rotation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, -2, 1, -4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -2, 3, -4], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, -2, 1, -4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Slice-based rotation:** After extraction, comp:** - **Slice-based rotation:** After extraction, compute `r = k % M` and use `t[r:] + t[:r]`. This is shorter but must branch when $M=0$ before taking the modulo; it has the same $O(N)$ time and $O(M)$ space.
- **Queue of movable values:** A deque can rotate the extracted sequence and then feed values back into movable slots. It expresses the cyclic operation directly but still needs $O(M)$ storage.
- **In-place cycle decomposition:** Store the movable indices and permute their values by rotation cycles. This can avoid the second value array but requires careful visited or gcd-cycle handling and still stores indices unless they are repeatedly rediscovered.
- **All values negative:** No element is movable, both logical rotation loops do no effective work, and the input remains unchanged.
- **Zero values:** Zero belongs to the rotating sequence because the predicate is `x >= 0`, not `x > 0`.
- **Rotation by zero:** Every source index maps to itself, and reinsertion reconstructs the original array.
- **Rotation by a multiple of $M$:** Modulo maps every value back to its original logical slot, so the result is unchanged.
- **One non-negative value:** Any cyclic rotation of a length-one sequence is identical.
- **Negative barriers:** They retain both value and physical index, but non-negative values on opposite sides still participate in one shared cyclic sequence.
- **Large k:** The formula normalizes `k` implicitly at every destination; performing the rotation one step at a time would waste $O(kM)$ work.
- **Returned object identity:** The exact implementation mutates and returns `nums`. A non-mutating interface would first copy the array, increasing output allocation but not changing asymptotic complexity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+M)$. Let $N=\lvert\texttt{nums}\rvert$ and $M$ be the number of non-negative elements. Extraction scans $N$ values and stores $M$ of them. Building `d` performs $M$ constant-time modular assignments. Reinsertion scans all $N$ positions. Total time is $O(N+M)=O(N)$.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
