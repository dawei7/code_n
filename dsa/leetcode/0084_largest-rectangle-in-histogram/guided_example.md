# Guided Example: Largest Rectangle in Histogram

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [2, 1, 5, 6, 2, 3]}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

The objective is to compute `10` from `{"heights": [2, 1, 5, 6, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View every bar as a possible rectangle height

Any rectangle covering consecutive histogram bars is limited by the shortest bar in its interval. Turn that statement around: choose a bar at index `i` with height `h`, and ask how far a rectangle of height `h` can extend left and right before meeting a blocking bar.

If the nearest blocking positions are known, the width is the number of indices strictly between them. The source stores one boundary in `left[i]` and one in `right[i]`, then evaluates

`h * (right[i] - left[i] - 1)`.

The outside sentinel positions `-1` and `n` allow a bar to extend to the physical beginning or end without separate width formulas.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [2, 1, 5, 6, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain indices of increasing heights

`stk` stores indices whose heights are strictly increasing from bottom to top after each iteration. When a new height `h` arrives, every stack-top height greater than or equal to `h` is popped. Once those bars see this new shorter-or-equal bar, they cannot extend through index `i` under the source's tie convention, so `right[popped] = i` is recorded.

After all such pops, any remaining top has height strictly smaller than `h`. It is the nearest surviving smaller bar to the left, so `left[i] = stk[-1]`. If the stack is empty, no smaller bar exists to the left and the initialized `-1` remains.

Finally, index `i` is pushed. Because all greater-or-equal heights were removed, strict height increase is restored.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `stk` stores indices whose heights are strictly increasing f... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why popping reveals the nearest right blocker

Consider a bar index `p` that is popped when processing `i`. It stayed on the stack through every index between `p` and `i`, so none of those earlier positions caused its removal. Therefore no intervening height was less than or equal to `heights[p]` under this pop rule. The current index is the first such blocker to its right.

Bars that never get popped have no blocking height at or below them on the right. Their `right` entries keep the initialized sentinel `n`, allowing their rectangles to reach the histogram end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [2, 1, 5, 6, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compute areas during pops:** A sentinel index :** - **Compute areas during pops:** A sentinel index or appended zero can finalize width immediately, avoiding the two boundary arrays while retaining $O(n)$ stack space.
- **Quadratic expansion:** For each bar, scan left and right until a shorter bar. It is easy to derive but can take $O(n^2)$ time on monotone histograms.
- **Divide and conquer:** Split at a minimum-height bar. Without fast range-minimum queries, sorted inputs cause quadratic time.
- **Segment tree:** It accelerates range-minimum queries but adds substantial structure and usually $O(n\log n)$ total time.
- **Single bar:** Both sentinel boundaries give width one and return its height.
- **Zero-height bar:** Its area is zero and it pops all positive stack heights, correctly finalizing their right boundaries.
- **Strictly increasing heights:** Nothing pops during the scan; right sentinels let each bar extend to the end.
- **Strictly decreasing heights:** Each new bar pops prior bars immediately; total work remains linear.
- **Equal-height plateau:** Earlier equals are popped, while a later representative inherits the full left reach.
- **Maximum length:** Amortized push/pop analysis avoids the quadratic behavior of repeated outward scans.
- **Nonempty guarantee:** The final `max` depends on at least one candidate.
- **Input preservation:** Only boundary and stack arrays are mutated.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each index is pushed once and popped at most once. Although the pop loop is nested inside the scan, its total iterations across the whole algorithm are $O(n)$. Computing all final areas also takes $O(n)$, so total time is $O(n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
