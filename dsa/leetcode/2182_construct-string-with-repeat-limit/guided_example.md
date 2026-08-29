# Guided Example: Construct String With Repeat Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cczazcc", "repeatLimit": 3}`
- **Required output:** `"zzcccac"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears **more than** `repeatLimit` times **in a row**. You do **not** have to use all characters from `s`.

The objective is to compute `"zzcccac"` from `{"s": "cczazcc", "repeatLimit": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count the fixed alphabet

Array `cnt` has 26 entries. Index zero represents `a` and index 25 represents `z`. Scanning `s` increments the matching count through `ord(c) - ord("a")`.

The algorithm does not sort all $n$ characters. The constant-size alphabet already provides their priority order through indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cczazcc", "repeatLimit": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the largest main letter

The outer loop visits `i` from 25 down to zero. At a given `i`, all letters larger than it have already been used as much as possible or have become impossible to continue.

Inside the loop, `x = min(repeatLimit, cnt[i])` selects the largest legal initial run of that character. The code subtracts those copies and appends `ascii_lowercase[i] * x`.

Using fewer than `repeatLimit` copies while more remain would place a smaller breaker earlier than necessary. The resulting string would be lexicographically smaller at that first breaker position. Thus taking the maximum legal run is optimal.

When `cnt[i]` was already zero, `x` is zero and the code appends an empty string before breaking. This is harmless; joining empty chunks does not change the result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the best separator

If copies of letter `i` remain after a full run, another `i` would violate the repeat limit. The construction needs one different letter.

Pointer `j` searches downward for the largest smaller letter with a positive count. Appending exactly one copy is optimal:

- choosing the largest available breaker maximizes the current differing position;
- using more than one breaker would delay the return to the larger letter and make the string lexicographically smaller.

After one breaker, the consecutive run of `i` has ended. The inner loop can append another block of up to `repeatLimit` copies of `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"zzcccac"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cczazcc", "repeatLimit": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"zzcccac"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Max heap:** Repeatedly pop the largest letter and a breaker. This generalizes to large alphabets but adds $O(\log A)$ heap operations for alphabet size $A$.
- **Sort all characters:** Sorting descending costs $O(n\log n)$ and still needs repair logic for repeat-limit violations.
- **Use a smaller breaker than necessary:** The result remains valid but becomes lexicographically smaller at that breaker position.
- **Use several breakers together:** One is enough to reset the run, and extra smaller characters unnecessarily delay a larger letter.
- **All characters identical:** The result contains at most `repeatLimit` copies because no breaker exists.
- **Repeat limit one:** Equal adjacent letters are forbidden, so the algorithm alternates through one-character main runs and breakers.
- **Limit at least every frequency:** No letter needs a breaker for itself, and characters are emitted in descending order.
- **Unused characters allowed:** Leftover copies are correctly abandoned when no separator can make them legal.
- **Empty appended chunks:** A zero count produces `""` in `ans`, which does not affect the joined output.
- **Breaker later becomes main:** The `min(i - 1, j)` update prevents the same letter from being used as its own breaker.
- **Fixed lowercase alphabet:** Array indexing and `ascii_lowercase` are valid because every input character is `a` through `z`.
- **Output length tie:** If one valid string is a prefix of another, the longer is larger; the greedy only stops when no legal extension exists.
- **Input preservation:** Counts are stored separately, and the immutable source string is unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the input length. Counting characters takes $O(n)$. The algorithm appends at most $n$ characters, possibly grouped into chunks. The breaker pointer decreases across a constant alphabet of 26 letters, and the outer loop has 26 iterations. Total construction and final joining time are $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
