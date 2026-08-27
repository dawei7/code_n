# Guided Example: Count Bowl Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 3, 1, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` with **distinct** elements.

The objective is to compute `2` from `{"nums": [2, 5, 3, 1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rephrase the bowl condition around the smaller endpoint

For endpoints `l < r`, the bowl condition is

`min(nums[l], nums[r]) > every interior value`.

Because all values are distinct, one endpoint is strictly smaller. The condition says that this smaller endpoint must still be larger than every element between the endpoints.

There are two cases:

- If `nums[l] < nums[r]`, then `r` is the first position to the right of `l` with a value greater than `nums[l]`; otherwise an earlier greater interior value would violate the bowl.
- If `nums[l] > nums[r]`, then `l` is the nearest position to the left of `r` with a value greater than `nums[r]`.

A monotonic decreasing stack identifies both kinds of endpoint pair in one left-to-right scan.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 3, 1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain a decreasing stack

The stack stores pairs `(value, index)` with values strictly decreasing from bottom to top.

When new `value = nums[right]` arrives, every top value smaller than it is popped. After all smaller values are removed, the remaining top, if any, is greater than the current value.

Each stored index represents a candidate endpoint that has not yet encountered a greater value to its right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The stack stores pairs `(value, index)` with values strictly... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count bowls when a smaller left endpoint is popped

Suppose stack entry `(v, left)` is popped because `v < value`.

The current `right` is the first index after `left` with a value greater than `v`. If any earlier interior value had exceeded `v`, it would have popped this entry sooner.

Therefore every value strictly between `left` and `right` is less than `v`. Since `v` is the smaller endpoint,

`min(v, value) = v`

is greater than every interior element. The pair forms a bowl whenever it has at least one interior position.

The source checks

`right - left >= 2`,

which is exactly the length-at-least-three requirement.

One new large value can pop several entries. Each popped entry defines a different left endpoint and therefore a different bowl subarray ending at `right`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 3, 1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subarrays:** Checking interior m:** - **Enumerate all subarrays:** Checking interior maxima directly costs at least `O(n^2)` and often `O(n^3)` without preprocessing.
- **Range-maximum queries for every endpoint pair:** A sparse table makes each test fast but still leaves `O(n^2)` pairs.
- **Nearest-greater arrays:** Precompute first greater to the right and nearest greater to the left, then count qualifying distances. This is equivalent monotonic-stack reasoning with extra arrays.
- **Use an increasing stack:** It tracks the wrong dominance relationship for endpoints that must exceed interiors.
- **Pop on `<=`:** Distinctness makes no difference here, but with duplicates it would not automatically preserve the strict bowl condition.
- **Adjacent endpoints:** They are not bowls because length must be at least three; `right - left >= 2` enforces this.
- **Strictly decreasing array:** No right endpoint has a qualifying interior-lower pair of length at least three, so the answer is zero.
- **Strictly increasing array:** Symmetrically, popped pairs are adjacent and no greater-left bowls form, giving zero.
- **Large outer endpoints:** One right endpoint may complete several bowls by popping multiple smaller candidates.
- **Nearest greater on the left:** Only the nearest can pair with a smaller right endpoint; any farther candidate contains that nearer greater value inside.
- **Distinct-value guarantee:** It ensures every endpoint pair has one uniquely smaller value and avoids equality cases.
- **Input preservation:** The source stores value-index pairs without modifying `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each array element is pushed onto the stack once. It can be popped at most once. The total number of while-loop iterations across the whole scan is therefore `O(n)`, even though one iteration may pop many entries.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
