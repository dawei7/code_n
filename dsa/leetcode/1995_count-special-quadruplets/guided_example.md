# Guided Example: Count Special Quadruplets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 6]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums`, return *the number of **distinct** quadruplets* `(a, b, c, d)` *such that:*

The objective is to compute `1` from `{"nums": [1, 2, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate index quadruplets directly

The exact source uses four nested loops. Each loop starts after the index chosen by the previous loop:

- `a` ranges up to `n - 4`;
- `b` starts at `a + 1`;
- `c` starts at `b + 1`;
- `d` starts at `c + 1`.

This construction guarantees `a < b < c < d` without an extra ordering test. Every increasing four-index combination appears exactly once.

For each combination, the code evaluates

`nums[a] + nums[b] + nums[c] == nums[d]`.

If true, it increments `ans`. Since quadruplets are defined by indices, equal values at different positions still produce distinct valid quadruplets, and the loops naturally count them separately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop bounds are chosen carefully

The first index must leave room for three later positions, so its final possible value is $n-4$. Python's `range(n - 3)` stops just before $n-3$ and reaches exactly that endpoint.

Likewise, `b` must leave two later positions and `c` must leave one. The ranges become empty automatically when insufficient positions remain, though the outer bounds already prevent such states.

These bounds avoid invalid access and unnecessary iterations while retaining every legal tuple.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace repeated values

For `[1,1,1,3,5]`, the first three ones with index three form one valid quadruplet because $1+1+1=3$.

For right endpoint four, value five can be formed by choosing value three at index three and any two of the three earlier ones. There are three index pairs, so three additional quadruplets are counted.

The answer is four. A value-frequency set would risk collapsing these different index choices, while direct enumeration preserves them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Pair-sum frequency scan:** Rearrange to `nums[a] + nums[b] = nums[d] - nums[c]` and maintain only pairs satisfying the index boundary, achieving $O(N^2)$ time with frequency storage.
- **Triple loops plus value lookup:** Can reduce one index search, but multiplicity and the position-after-$c$ condition must be maintained carefully.
- **Sort the array:** Incorrect because quadruplets depend on original index order, not only multiset values.
- **Exactly four elements:** The loops test the sole possible quadruplet once.
- **Duplicate values:** Different index choices remain distinct and are correctly counted separately.
- **No satisfying equality:** `ans` remains zero.
- **Several right endpoints:** Each appears in its own `d` iterations.
- **Positive values:** Bound arithmetic but do not justify reordering indices.
- **Loop ordering:** Starting each index after its predecessor enforces strict inequalities automatically.
- **Maximum length 50:** Makes the exact $\binom{N}{4}$ enumeration practical despite its $O(N^4)$ asymptotic class.
- **Manifest mismatch:** The exact source is exhaustive, not the quadratic pair-count approach.
- **Input preservation:** The array is neither sorted nor modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^4)$. Let $N$ be the array length. The number of iterations is $\binom{N}{4}$, which is $\Theta(N^4)$ in the asymptotic worst case. Each equality check is constant-time under the bounded integer values, so exact time is $O(N^4)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
