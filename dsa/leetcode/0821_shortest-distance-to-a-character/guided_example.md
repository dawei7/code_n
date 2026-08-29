# Guided Example: Shortest Distance to a Character

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "loveleetcode", "c": "e"}`
- **Required output:** `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` and a character `c` that occurs in `s`, return *an array of integers *`answer`* where *$\text{answer.length} = \text{s.length}$* and *$\text{answer}[i]$* is the **distance** from index *`i`* to the **closest** occurrence of character *`c`* in *`s`.

The objective is to compute `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]` from `{"s": "loveleetcode", "c": "e"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The nearest occurrence must be on one of two sides

For any index `i`, the closest occurrence of `c` is either the nearest occurrence at or before `i`, or the nearest occurrence at or after `i`. No other occurrence can be better: an earlier occurrence farther left is more distant than the nearest left one, and a later occurrence farther right is more distant than the nearest right one.

The solution computes these two directional distances with two linear scans and stores their minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "loveleetcode", "c": "e"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prepare a safe initial upper bound

Let `n = len(s)`. The answer list begins as `ans = [n] * n`.

The largest possible distance between two valid indices is `n - 1`, so `n` is larger than every real answer. It works as a finite placeholder until a scan discovers an occurrence of `c`. Using a finite placeholder also ensures the final list contains ordinary integers after both passes.

The Reference guarantees that `c` occurs at least once, so every placeholder will eventually be replaced by a genuine distance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Left-to-right pass

Variable `pre` stores the index of the most recent occurrence of `c` at or before the current position. It begins at negative infinity because no left occurrence has been seen.

At index `i`:

- if `s[i] == c`, set `pre = i`;
- update `ans[i]` with `min(ans[i], i - pre)`.

When the current character is `c`, the distance becomes `i - i = 0`. Otherwise, `pre` remains the closest occurrence on the left. It is the closest because the scan replaces it every time a newer, larger occurrence index is found.

Before the first `c`, `i - (-inf)` is positive infinity. Taking the minimum with the placeholder `n` leaves `ans[i] = n`. Those positions do not yet have a left-side candidate and will be corrected by the right-to-left pass.

After this pass, every position at or after the first occurrence holds its exact nearest-left distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "loveleetcode", "c": "e"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Collect occurrence indices and binary-search each position:** This works in `O(n\log m)` time for `m` occurrences. Two directional scans are simpler and linear.
- **Expand outward from every index:** Searching left and right independently for each position can take `O(n^2)` on long gaps.
- **Multi-source BFS on indices:** Starting from every `c` and spreading distances left and right also gives `O(n)` time, but the two-pass method needs no queue.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`. Initializing `ans` takes `O(n)` time. Each of the two scans visits every character once and performs constant work, so total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
