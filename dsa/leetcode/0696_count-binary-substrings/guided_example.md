# Guided Example: Count Binary Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "00110011"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s`, return the number of non-empty substrings that have the same number of `0`'s and `1`'s, and all the `0`'s and all the `1`'s in these substrings are grouped consecutively.

The objective is to compute `6` from `{"s": "00110011"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Finding one maximal run

The outer index `i` is the first position of the current run. The inner index starts at `j = i + 1` and advances while:

- `j < n`; and
- `s[j] == s[i]`.

When the inner loop stops, positions `i` through `j - 1` form one maximal run of identical bits. Its length is

`cur = j - i`.

The run is maximal because `j` is either the end of the string or a position holding the opposite bit.

At the bottom of the outer loop, `i = j` begins the next run. Every character is therefore part of exactly one discovered group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "00110011"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Counting substrings across one boundary

Consider two adjacent runs with lengths `a` and `b`. Any valid substring centered on their boundary must take some positive number `x` of characters from the end of the first run and exactly `x` characters from the beginning of the second.

The possible values are:

$$
x=1,2,\ldots,\min(a,b).
$$

For each `x`, there is exactly one such substring at this boundary because its end portions are forced. Thus these two runs contribute

$$
\min(a,b)
$$

valid substrings.

They cannot contribute more: taking over `a` characters from the left or over `b` from the right is impossible, and extending past either maximal run would introduce a third group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider two adjacent runs with lengths `a` and `b`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What `pre` means

`pre` stores the length of the immediately previous run. It begins at zero because no run precedes the first.

After discovering a current run of length `cur`, the code adds:

`ans += min(pre, cur)`.

For the first run, this adds `min(0, cur) = 0`, correctly reflecting that one group alone cannot form a valid substring.

Then `pre = cur` prepares the next boundary. Only the immediately preceding run matters; a valid substring cannot cross two group boundaries.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "00110011"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store every run length:** Build a list such as:** - **Store every run length:** Build a list such as `[2, 3, 4]` and sum minima of adjacent entries. It has the same time but uses `O(n)` worst-case space.
- **- **Character-by-character rolling counts:** Track:** - **Character-by-character rolling counts:** Track current and previous run lengths in one for-loop and add a boundary contribution when the character changes, plus one final contribution. This is equivalent to the exact run-skipping implementation.
- **- **Enumerate every substring:** Checking counts a:** - **Enumerate every substring:** Checking counts and grouping for all substrings is at least quadratic and ignores the key one-boundary structure.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
