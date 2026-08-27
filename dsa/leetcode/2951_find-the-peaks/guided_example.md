# Guided Example: Find the Peaks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mountain": [2, 4, 4]}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `mountain`. Your task is to find all the **peaks** in the `mountain` array.

The objective is to compute `[]` from `{"mountain": [2, 4, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: List-comprehension structure

For every interior index `i`, the condition

`mountain[i - 1] < mountain[i] > mountain[i + 1]`

is Python's chained comparison. It is equivalent to:

`mountain[i - 1] < mountain[i] and mountain[i] > mountain[i + 1]`.

The middle value is evaluated as the shared peak candidate. Both comparisons are strict.

If the condition succeeds, `i` is placed in the returned list. Otherwise it contributes nothing.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mountain": [2, 4, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why local checks are enough

The definition depends only on immediate neighbors, not on whether the value is a global maximum or whether the entire array rises and falls like one mountain. Therefore each interior position can be decided independently with two comparisons.

Take any returned index. Both strict relations passed, so it is a peak by definition.

Conversely, any genuine peak lies between indices $1$ and $n-2$ and satisfies those exact relations. The range visits it, and the condition includes it. Hence the result contains all and only peaks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The definition depends only on immediate neighbors, not on w... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Plateaus are not peaks

If the candidate equals either neighbor, one strict comparison fails. For `[2,4,4]`, index one is not a peak because $4$ is not greater than the right neighbor $4$.

This differs from a non-strict local maximum definition. Replacing either comparison with `<=` in the wrong direction would incorrectly accept flat areas.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mountain": [2, 4, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare with the global maximum:** Incorrect; :** - **Compare with the global maximum:** Incorrect; a local peak need not be globally greatest.
- **Track rising and falling trends:** It can find peaks, but direct neighbor comparisons are simpler and equally linear.
- **Sort values:** Sorting destroys index adjacency and cannot answer the question.
- **First index:** Never a peak because it lacks a left neighbor, even if greater than index one.
- **Last index:** Never a peak because it lacks a right neighbor.
- **Minimum length three:** Exactly one interior candidate is tested.
- **All equal values:** Strict comparisons fail everywhere, returning an empty list.
- **Strictly increasing array:** Every interior element has a larger right neighbor, so none is a peak.
- **Strictly decreasing array:** Every interior element has a larger left neighbor, so none is a peak.
- **Plateau beside a high value:** Equality on either side disqualifies the candidate.
- **Negative values would also work:** The proof uses only ordering, though the contract supplies positive integers.
- **Output order:** Increasing order is a deterministic bonus, not a requirement.
- **Chained-comparison evaluation:** Python evaluates the shared middle expression once conceptually and short-circuits if the left comparison fails, while preserving the exact two-inequality meaning.
- **Neighbor equality on one side:** Even if the candidate exceeds the other neighbor by a large amount, one equality is enough to disqualify it.
- **Valley detection is different:** Reversing both comparisons would find local minima. The source's directions point upward toward the middle from both sides.
- **No need to remember a previous trend:** Direct indexed access supplies both neighbors at once, so the list comprehension uses no rolling state.
- **Peak count bound:** Strict peaks cannot be adjacent, so output contains at most roughly half the interior indices, although $O(n)$ remains the appropriate bound.
- **Changing one endpoint value:** It may affect whether index one or $n-2$ is a peak, but endpoints themselves remain excluded; the scan still checks the affected interior candidate.
- **Any-order contract:** Returning sorted indices makes testing and reading deterministic without paying a sorting cost because traversal already has that order.
- **No mutation:** Comparisons leave the mountain array intact.
- **Why one pass is optimal:** An unexamined interior position could be changed to exceed both neighbors without affecting distant checks, so worst-case correctness requires considering every candidate index.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For an array of length $n$, the method checks $n-2$ interior positions. Each performs two constant-time comparisons, so time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
