# Guided Example: Construct Smallest Number From DI String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"pattern": "IIIDIDDD"}`
- **Required output:** `"123549876"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

The objective is to compute `"123549876"` from `{"pattern": "IIIDIDDD"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search candidate numbers in lexicographic order

The exact solution uses backtracking rather than the linear greedy construction described by the manifest summary. It builds the answer from left to right, trying unused digits `1` through `9` in ascending order at every position. This traversal order is crucial: complete candidate strings are encountered in lexicographic order.

For equal-length strings made of digits, lexicographic order is determined by the first differing position. Trying the smallest possible first digit, then the smallest possible second digit under that prefix, and so on is precisely a depth-first enumeration from smallest to largest.

The first complete candidate satisfying the pattern is therefore the lexicographically smallest answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"pattern": "IIIDIDDD"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the current prefix and used digits

`t` is a list of digit characters forming the current prefix. A list supports efficient append and pop during recursion. When a complete answer is found, `''.join(t)` converts it to the required string.

`vis` is a Boolean array of length ten. Indices `1` through `9` represent whether each digit is already in `t`; index zero is unused. Before selecting digit `i`, the search checks `not vis[i]`. It marks the digit, appends it, explores, then unmarks and pops it. This restoration makes the same digit available in a different branch while still enforcing uniqueness within one candidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check only the newly created relation

The recursion parameter `u` is the number of digits already placed, so it is also the index where the next digit will go. When `u > 0`, choosing `i` creates exactly one new adjacent pair between `t[-1]` and `i`. Earlier adjacent relations were already checked when those digits were appended.

If `pattern[u - 1] == 'I'`, the previous digit must be smaller. The branch is rejected when:



If the symbol is `'D'`, the previous digit must be larger, so the branch is rejected when `int(t[-1]) <= i`.

Checking the constraint immediately prunes invalid prefixes. No extension can repair an already incorrect adjacent relation, so abandoning that branch is safe.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"123549876"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"pattern": "IIIDIDDD"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"123549876"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reverse consecutive `D` runs:** Start with digits `1` through `n+1` and reverse the positions covered by each maximal decreasing run. This constructs the smallest answer in $O(n)$ time.
- **Stack-based greedy:** Push successive digits and flush the stack at each `I` or at the end. Popping reverses precisely the required decreasing segments.
- **Try all permutations then filter:** It is correct but misses the safe prefix pruning used by the exact DFS and performs much more work.
- **All `I` symbols:** The first path chooses `1, 2, ..., n+1` and succeeds without backtracking.
- **All `D` symbols:** Smaller starting digits fail until the smallest digit large enough to support the full descending run is tried.
- **Alternating symbols:** Constraint checks apply locally as each digit is appended; no special pattern form is needed.
- **Digit uniqueness:** `vis` prevents outputs such as `123414321` even if their adjacent comparisons appear suitable.
- **Maximum pattern length eight:** Exactly nine distinct digits are required, consuming the full allowed set.
- **First position:** With `u = 0` there is no prior digit or pattern relation, so every unused digit is structurally eligible.
- **Successful early exit:** `ans` stops all lexicographically larger branches after the first valid complete string is found.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $L=\lvert\texttt{pattern}\rvert+1$, with $2\le L\le9$. At recursion depth $d$, an unconstrained search can have up to:
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
