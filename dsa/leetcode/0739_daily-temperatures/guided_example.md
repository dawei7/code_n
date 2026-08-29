# Guided Example: Daily Temperatures

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]}`
- **Required output:** `[1, 1, 4, 2, 1, 1, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* $\text{answer}[i]$ *is the number of days you have to wait after the* $i^{\text{th}}$ *day to get a warmer temperature*. If there is no future day for which this is possible, keep $\text{answer}[i] = 0$ instead.

The objective is to compute `[1, 1, 4, 2, 1, 1, 0, 0]` from `{"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Scan backward so the future is already summarized

For each day, we need the nearest later day with a strictly higher temperature. A direct forward search from every day repeats comparisons and can become quadratic.

The exact solution scans indices from right to left. When processing day `i`, all future days have already been considered. A stack of future indices keeps only the days that could still be the nearest warmer answer for some earlier day.

The answer array begins with zeroes. Zero is already correct for any day that has no warmer future day, so the code writes a positive distance only when a candidate exists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the monotonic stack represents

The stack stores indices, not temperatures, because the answer needs a day difference. Their temperatures can be read through `temperatures[index]`.

Before answering day `i`, the solution removes stack tops whose temperatures are less than or equal to `temperatures[i]`:

`while stk and temperatures[stk[-1]] <= temperatures[i]:`

After these removals, any remaining top is strictly warmer than the current day.

The top is also the nearest surviving future candidate because indices were pushed during a right-to-left scan. More recently pushed indices lie closer to the current position and appear at the top.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why colder or equal future days can be discarded forever

Suppose future day `j` has temperature no greater than current day `i`. For the current day, `j` is not strictly warmer and cannot be the answer.

For any still-earlier day `h`, day `i` is closer than `j`. If `j` would be warm enough for `h`, then `i` is at least as warm as `j` and is also warm enough, while occurring sooner. Therefore `j` can never be the preferred answer for any earlier day.

This domination argument makes popping permanent and is the source of linear time.

Equal temperatures are popped as well because the problem requires a strictly warmer day. An equal day cannot answer the current index, and the closer equal-temperature current day dominates it for earlier indices.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 4, 2, 1, 1, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 4, 2, 1, 1, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Forward monotonic stack:** Scan left to right and keep unresolved days with decreasing temperatures. When a warmer day arrives, pop and fill their waits. This is equally optimal and may feel more event-driven.
- **Nested forward searches:** For every day, scan later days until finding a warmer one. Worst-case decreasing or constant temperatures cause `O(n^2)` comparisons.
- **Jump using already computed answers:** Scan backward and skip through future days by their known waits. This can achieve linear behavior with careful zero handling, but the monotonic stack has a clearer domination proof.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of days. Each index is pushed once. An index can also be popped at most once because popped indices never return. Thus all while-loop iterations across the entire scan total at most `n`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
