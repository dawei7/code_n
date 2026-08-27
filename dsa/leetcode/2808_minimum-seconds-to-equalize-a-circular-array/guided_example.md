# Guided Example: Minimum Seconds to Equalize a Circular Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` containing `n` integers.

The objective is to compute `1` from `{"nums": [1, 2, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Choose the final value, then ask how fast it can spread.** In one second, every position may copy a value from either circular neighbor. No operation invents a new value: every copied value already existed at a neighboring position in the previous second. Therefore, if the whole array eventually becomes one value, that final value must be one that appears in the original array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The algorithm considers each distinct original value as a candidate target. It groups all indices of equal values in a dictionary. Because `enumerate(nums)` visits indices in increasing order, every stored index list is already sorted.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The algorithm considers each distinct original value as a ca... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Propagation happens simultaneously in both directions.** Fix one target value. Its original occurrences are sources. After one second, positions at circular distance one from a source can hold the target. After two seconds, positions at distance two can hold it, and so on. Since all positions update simultaneously, the time for the target to cover the array is the maximum, over all positions, of the distance to the nearest original source.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Multi-source BFS for each value:** Treat all o:** - **Multi-source BFS for each value:** Treat all occurrences of one value as sources and compute the farthest circular distance. This is correct but can take $O(n)$ per distinct value, or $O(n^2)$ overall.
- **Binary search on time:** Check whether some value can cover the circle within a proposed number of seconds. The gap formula already yields each exact time directly, so search is unnecessary.
- **Simulate every second:** Repeatedly copy values until the array is equal. This can be complicated by simultaneous-state handling and does more work than measuring propagation distances.
- **Array already equal:** Every cyclic gap for the sole value is one, so `1 // 2` is zero and no operation is needed.
- **One occurrence of a target:** Its only cyclic gap is $n$, giving $\lfloor n/2 \rfloor$ seconds.
- **Two sources opposite each other:** The largest gap determines how far the two wavefront pairs must travel; equal gaps are handled naturally.
- **Odd largest gap:** Integer division correctly gives the distance of the central positions, such as $5 // 2 = 2$.
- **Even largest gap:** The unique middle position or central boundary is reached in exactly half the source distance.
- **Wraparound largest gap:** The explicit last-to-first distance ensures positions near indices zero and $n-1$ are analyzed as adjacent on the circle.
- **Duplicate values:** More occurrences create more, usually smaller gaps; every position index is retained because source multiplicity and spacing matter.
- **Final value not initially present:** This is impossible because operations only copy existing neighbor values; the dictionary therefore covers every feasible target.
- **Simultaneous copying:** The distance model assumes at most one-edge propagation per second, exactly as required by using the previous second's values.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Building the dictionary visits every element once, taking expected $O(n)$ time and $O(n)$ space. Across all target groups, the total number of stored indices is exactly $n$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
