# Guided Example: Number of Adjacent Elements With the Same Color

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "queries": [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]}`
- **Required output:** `[0, 1, 1, 0, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing an array `colors` of length `n` where all elements are set to 0's meaning **uncolored**. You are also given a 2D integer array `queries` where $\text{queries}[i] = [\text{index}_{i}, \text{color}_{i}]$. For the $$i^{\text{th}}$$ **query**:

The objective is to compute `[0, 1, 1, 0, 2]` from `{"n": 4, "queries": [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain the answer instead of recounting it

The array begins uncolored, represented by zeros. Each query assigns a positive color `c` to one index `i` and asks for the number of adjacent pairs whose two elements have the same nonzero color.

A direct implementation could apply a query and scan all $n-1$ neighboring pairs again. That would repeat almost the same work after every update.

Only one array position changes. Therefore only pairs touching that position can possibly change:

- the left pair between indices $i-1$ and $i$, when $i>0$;
- the right pair between indices $i$ and $i+1$, when $i<n-1$.

Every other pair has exactly the same two endpoint colors before and after the query. The solution keeps `x` as the current total and adjusts only these at most two local contributions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "queries": [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What counts as a contributing pair

A pair contributes one precisely when:

1. both positions are colored, and
2. their colors are equal.

Since all assigned colors are positive and zero means uncolored, checking that the current color is nonzero distinguishes a real equal-colored pair from two uncolored zeros.

The solution stores current colors in `nums`. Before a query, `nums[i]` is the old color at the updated position and may be zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A pair contributes one precisely when:

1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: First remove the old local contributions

Before installing color `c`, the algorithm asks whether the old position currently forms a counted pair with each neighbor.

For the left side it checks:

`i > 0 and nums[i] and nums[i - 1] == nums[i]`.

The boundary test ensures the neighbor exists. `nums[i]` ensures the updated position was colored. Equality then proves the old left pair contributed one, so `x` is decremented.

The right-side condition is symmetric. After these two checks, `x` represents the total number of valid pairs that do not rely on the old color at index `i`.

This removal step must happen while `nums[i]` still contains the old color.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 1, 0, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "queries": [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 1, 0, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rescan every adjacent pair after each query:**:** - **Rescan every adjacent pair after each query:** Simple but costs $O(nq)$ time.
- **Store a Boolean for every edge:** This can also update two edges per query, but the single total `x` is sufficient and needs less state.
- **Segment tree:** It can maintain richer interval information, but it is unnecessary because the requested statistic changes locally and constant-time updates are possible.
- **First color at an index:** No old pair is removed because `nums[i]` is zero.
- **Recolor to the same color:** Old contributions are removed and identically restored, giving no net change.
- **Change the middle of a run:** Up to two equal pairs may disappear and up to two different pairs may appear.
- **Left endpoint:** Only the right pair exists.
- **Right endpoint:** Only the left pair exists.
- **Array of length one:** No adjacent pair exists, so every answer is zero.
- **Two uncolored neighbors:** Equal zeros never count because a contributing pair must be colored.
- **Positive color guarantee:** It makes direct neighbor comparison with `c` sufficient when adding new pairs.
- **Repeated queries at one index:** The stored assignment ensures every later query removes contributions of the latest color, not an older one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+q)$. Creating the length-$n$ color array takes $O(n)$ time. For each of $q$ queries, the algorithm performs at most four neighbor comparisons, a constant number of additions or subtractions, one output write, and one color assignment. Total time is $O(n+q)$.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
