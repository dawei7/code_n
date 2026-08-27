# Guided Example: Recover the Original Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 10, 6, 4, 8, 12]}`
- **Required output:** `[3, 7, 11]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice had a **0-indexed** array `arr` consisting of `n` **positive** integers. She chose an arbitrary **positive integer** `k` and created two new **0-indexed** integer arrays `lower` and `higher` in the following manner:

The objective is to compute `[3, 7, 11]` from `{"nums": [2, 10, 6, 4, 8, 12]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The global minimum must be a lower value

Each original value $a$ creates $a-k$ and $a+k$, separated by $2k$. Since $k>0$, the smaller member of every pair is its lower value.

After sorting `nums`, `nums[0]` cannot be a higher value: its corresponding lower value would be even smaller and would also appear. Therefore, it must pair with some later `nums[i]` as

$$
\texttt{nums[i]}-\texttt{nums[0]}=2k.
$$

The source tries every possible partner index `i`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 10, 6, 4, 8, 12]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject impossible candidate gaps

The gap `d` must be positive because $k$ is positive, and it must be even because `d = 2k`.

Candidates with `d == 0` or odd `d` are skipped.

For a valid gap, the recovered original value for a pair $(low,high)$ is their midpoint:

$$
\frac{low+high}{2}.
$$

The source uses a right shift by one, `>> 1`, which is exact because the gap and hence the sum parity are compatible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The gap `d` must be positive because $k$ is positive, and it... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Greedily pair the smallest unused value

For one candidate `d`, `vis` marks elements already used as higher partners. `nums[i]` is initially marked because it pairs with `nums[0]`, and their midpoint begins `ans`.

`l` identifies the smallest remaining value not already consumed as a higher element. This value must be the lower member of its pair. Pairing it with anything other than `nums[l] + d` cannot fit the fixed candidate $k$.

`r` advances until the difference from `nums[l]` is at least `d`:

- if the difference is smaller, that position cannot be the required higher partner, so move right;
- if the first adequate difference is greater than `d` or no position remains, this candidate gap is impossible;
- if it equals `d`, mark `r` used, append the midpoint, and continue.

Always taking the smallest unused lower value makes the validation deterministic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 7, 11]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 10, 6, 4, 8, 12]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 7, 11]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Multiset counter validation:** Repeatedly remo:** - **Multiset counter validation:** Repeatedly remove the smallest value and its value-plus-gap partner from a frequency map. It expresses the same greedy proof.
- **Try arbitrary pairings:** Exponential backtracking is unnecessary because the smallest unused lower partner is forced for a fixed gap.
- **Zero gap:** It implies `k = 0` and must be rejected.
- **Odd gap:** It cannot equal `2k` for integer `k`.
- **Duplicate values:** Position-based `vis` preserves multiplicity.
- **Multiple valid answers:** The first successful candidate may be returned.
- **Two input numbers:** Their positive even difference yields their midpoint.
- **Large numeric values:** Midpoint arithmetic remains within Python integer capacity.
- **First element role:** Sorted global minimum must be lower, which reduces possible `k` values to its partner choices.
- **Candidate failure:** A missing exact-gap partner invalidates that `d` immediately.
- **Input mutation:** `nums.sort()` changes the input order.
- **Existence guarantee:** The final empty return is a fallback outside the promised valid cases.
- **Monotonic partner pointer:** Sorted required partner values mean `r` never needs to retreat.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $M$ be the length of `nums`, equal to twice the recovered array length.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
