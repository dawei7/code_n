# Guided Example: Partition Labels

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ababcbacadefegdehijhklij"}`
- **Required output:** `[9, 7, 8]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

The objective is to compute `[9, 7, 8]` from `{"s": "ababcbacadefegdehijhklij"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A partition cannot end before the last occurrence of any letter it contains

If the current part contains character `c`, every occurrence of `c` must remain in that same part. Therefore its right boundary must reach at least `last[c]`, the character’s final position in the whole string.

The solution first builds a dictionary of final positions. The comprehension overwrites earlier indices, leaving the last index for each lowercase letter.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ababcbacadefegdehijhklij"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grow the smallest valid current boundary

Variable `j` is the current part’s start. Variable `mx` is the farthest last occurrence required by every character seen since `j`.

While scanning index `i` and character `c`, the update

`mx = max(mx, last[c])`

extends the required boundary if this character appears farther right.

Characters encountered inside that extension may themselves have later occurrences, so the scan continues and keeps expanding `mx` until all dependencies are contained.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Variable `j` is the current part’s start.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Close exactly when the scan reaches the boundary

When `i == mx`, every character seen in the current part has its last occurrence at or before `i`. No such character appears later, so cutting after `i` is valid.

The length is `i - j + 1`. The next part begins at `i + 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[9, 7, 8]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ababcbacadefegdehijhklij"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[9, 7, 8]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Expand each partition with repeated searches:*:** - **Expand each partition with repeated searches:** Repeatedly finding last positions can become quadratic. Precompute them once.
- **- **Cut after a character’s first occurrence:** La:** - **Cut after a character’s first occurrence:** Later copies would cross the boundary and invalidate the partition.
- **- **Delay a valid cut:** This remains valid but re:** - **Delay a valid cut:** This remains valid but reduces or preserves, never increases, the number of parts.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. Building last occurrences takes `O(n)` time, and the greedy scan takes another `O(n)`. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
