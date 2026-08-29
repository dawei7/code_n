# Guided Example: Shortest Distance to Target String in a Circular Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["hello", "i", "am", "leetcode", "hello"], "target": "hello", "startIndex": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** **circular** string array `words` and a string `target`. A **circular array** means that the array's end connects to the array's beginning.

The objective is to compute `1` from `{"words": ["hello", "i", "am", "leetcode", "hello"], "target": "hello", "startIndex": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every target occurrence is a possible destination

The target may appear multiple times. The closest occurrence is not necessarily the first one in ordinary array order, so the method scans all indices and evaluates every word equal to `target`.

For an occurrence at index `i`, there are two directions around the circular array:

- move directly along the index gap;
- wrap around the other side of the circle.

The shorter of these is the distance to that occurrence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["hello", "i", "am", "leetcode", "hello"], "target": "hello", "startIndex": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute the two circular distances

Let

`t = abs(i-startIndex)`.

This is the number of steps between the indices without crossing the array boundary. The circular route in the opposite direction uses the remaining edges of the `n`-node cycle, so its length is

`n-t`.

The shortest distance to occurrence `i` is therefore

$$
\min(t,n-t).
$$

The update

`ans = min(ans,t,n-t)`

compares both routes with the best target occurrence found earlier.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the two choices are exhaustive

Between two vertices on a simple cycle, there are exactly two simple paths: clockwise and counterclockwise. Any route that reverses direction or loops around more than once repeats edges and is no shorter than one of those two simple paths.

The direct index difference measures one path, and `n-t` measures the complement. Their minimum is exactly the shortest possible movement distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["hello", "i", "am", "leetcode", "hello"], "target": "hello", "startIndex": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bidirectional step simulation:** Move left and right from the start until finding the target. It can return early but requires modular indexing.
- **Preindexed positions:** Store occurrence indices per word for many repeated queries, but one query does not justify the extra structure.
- **Target at start:** Return distance zero.
- **Multiple occurrences:** Evaluate all or stop only when the theoretical minimum zero is found.
- **No occurrence:** The sentinel remains `n` and becomes `-1`.
- **One-element array:** The result is zero on a match and `-1` otherwise.
- **Wraparound shorter:** `n-t` captures movement across the end-to-start boundary.
- **Direct route shorter:** `t` captures movement without wrapping.
- **Exact match:** Substrings do not count.
- **Sentinel safety:** No valid shortest circular distance can equal `n`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $n$ be the number of words. The loop examines every word once, so there are $O(n)$ comparisons and constant-time index calculations.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
