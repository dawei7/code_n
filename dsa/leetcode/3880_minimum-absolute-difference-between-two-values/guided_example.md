# Guided Example: Minimum Absolute Difference Between Two Values

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 0, 2, 0, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` consisting only of 0, 1, and 2.

The objective is to compute `2` from `{"nums": [1, 0, 0, 2, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every valid pair has a later endpoint

A valid pair uses one index containing one and one index containing two. Its absolute distance is the later index minus the earlier index.

During a left-to-right scan, when the later endpoint is reached, the algorithm only needs the closest earlier occurrence of the opposite value. Among all earlier opposite indices, the largest index is closest to the current position.

This turns an apparent all-pairs problem into maintaining two latest positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 0, 2, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use value arithmetic to select the opposite

The only relevant nonzero values are one and two. For either one,

`3 - x`

is the other:

- when `x=1`, `3-x=2`;
- when `x=2`, `3-x=1`.

The list `last` has three entries so it can be indexed directly by value. `last[1]` stores the most recent index containing one, and `last[2]` stores the most recent index containing two. Entry zero is unused.

The loop skips `x=0` because zero cannot be part of a valid pair and should update neither latest position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The only relevant nonzero values are one and two.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Candidate distance at one index

At current index `i` containing `x`, the closest earlier valid partner is `last[3-x]`. If it exists, the distance is

`i - last[3 - x]`.

The source takes the minimum of this candidate and the best answer seen so far, then records `last[x]=i` for future positions.

Keeping only the latest opposite occurrence is sufficient. If earlier opposite indices are `j_1<j_2<\cdots<j_t<i`, then

$$
i-j_t<i-j_{t-1}<\cdots<i-j_1.
$$

No older index can improve the candidate for this fixed `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 0, 2, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every one-two index pair:** If both :** - **Enumerate every one-two index pair:** If both values occur many times, this takes `O(N^2)`. The latest-opposite observation reduces it to one pass.
- **Store all positions of one and two:** Two sorted position lists can be merged with two pointers in `O(N)` time but require `O(N)` space.
- **Two explicit variables:** `last_one` and `last_two` are equivalent and may be clearer than the `3-x` trick in a generalized language.
- **Check only one ordering:** A one may appear before a two or after it. Processing whichever endpoint is later handles both.
- **Zeros:** They are neither target value and must not reset a latest position.
- **Missing one:** No valid pair exists and the sentinel produces minus one.
- **Missing two:** Symmetrically, the result is minus one.
- **Adjacent one and two:** Distance one is globally minimal.
- **Repeated same value:** Each new occurrence updates its latest position, improving potential proximity to a future opposite value.
- **Singleton array:** It cannot contain both required values and returns minus one.
- **Sentinel comparison:** Testing `ans>n` is safe because real distances are at most `n-1`.
- **Negative infinity arithmetic:** Python produces positive infinity for `i-(-inf)`. A language without infinities can use minus one latest indices plus an explicit presence check.
- **Return distance, not indices:** The algorithm discards endpoint identities after updating the minimum because only the numeric distance is requested.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. The loop visits every one of `N` elements once and performs constant-time arithmetic, indexing, and comparisons. Total time is `O(N)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
