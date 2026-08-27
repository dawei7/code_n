# Guided Example: Longest Consecutive Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [100, 4, 200, 1, 3, 2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

The objective is to compute `4` from `{"nums": [100, 4, 200, 1, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why duplicates disappear from the set

`s = set(nums)` keeps one copy of each integer. Consecutive-sequence length counts distinct consecutive values, so duplicate input occurrences must not increase a sequence.

The outer loop still visits the original `nums`, including duplicates, but a value can be removed from `s` only once. Later occurrences find it absent and perform no removal loop.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [100, 4, 200, 1, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the removal loop discovers

For current `x`, `y` starts at `x`. While `y in s`, the source removes it and increments `y`.

When the loop stops, all still-unprocessed values in the half-open integer interval `[x, y)` have been consumed. Their count is `y - x`.

The stopping value `y` has one of two meanings:

- `y` is not present in the input, so it is a genuine gap and contributes no suffix; or
- `y` was removed earlier as the start of an already summarized consecutive suffix.

`defaultdict(int)` returns zero for the first case. In the second case, `d[y]` supplies the known suffix length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For current `x`, `y` starts at `x`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the stopping point can safely use `d[y]`

Suppose `y` was removed earlier and is consecutive with the new block. The earlier processing that removed `y` scanned continuously to the right and stored its combined length under the starting value of that scan.

A future block approaching from smaller values meets that earlier scan at its left boundary. It cannot first meet an unrecorded interior value while the earlier boundary lies farther left, because those lower overlapping values would already have been removed and could not form the new block.

Therefore, when a newly removed block reaches a previously processed consecutive component, the meeting value has the suffix summary needed in `d[y]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [100, 4, 200, 1, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Start-only hash-set scan:** Begin a run only w:** - **Start-only hash-set scan:** Begin a run only when `x - 1` is absent, then count upward. It is the standard and easier-to-prove expected $O(n)$ solution.
- **Boundary-length interval merging:** Store interval lengths at their endpoints and merge neighboring components as values arrive.
- **Sorting:** Sort distinct or original values and scan, handling duplicates. It takes $O(n\log n)$ time and may mutate the input.
- **Union-find:** Connect present neighboring integers. It works but adds more structure than the interval nature requires.
- **Empty input:** Returns zero.
- **Only duplicates:** The set contains one value, so longest length is one.
- **Negative through positive sequence:** Arithmetic adjacency works across zero.
- **Unsorted order:** The set makes array position irrelevant.
- **Previously processed suffix:** `d[y]` joins it to a newly removed lower block.
- **true gap:** Default zero terminates the sequence.
- **Duplicate outer iteration:** Performs no removals and cannot lower `ans`.
- **Hash complexity:** Linear time is expected, based on expected constant-time set and dictionary access.
- **Missing imports:** `List` and `defaultdict` must be supplied.
- **Input preservation:** Only the copied set is destructively reduced.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be input length and $u$ the number of distinct values. Set construction is expected $O(n)$ time. The outer loop has $n$ iterations, but every successful `while` iteration removes one distinct value permanently, so all removal loops together run only $u$ times.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
