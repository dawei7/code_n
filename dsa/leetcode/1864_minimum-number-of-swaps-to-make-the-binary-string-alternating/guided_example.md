# Guided Example: Minimum Number of Swaps to Make the Binary String Alternating

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "111000"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s`, return *the **minimum** number of character swaps to make it **alternating**, or *`-1`* if it is impossible.*

The objective is to compute `1` from `{"s": "111000"}` while avoiding redundant calculations and unnecessary overhead.

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

**There are only two possible alternating patterns.** A binary alternating string must be either `010101...` or `101010...`. The helper `calc(c)` measures swaps needed for the pattern whose first bit is `c`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "111000"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

At index `i`, that pattern’s expected bit is `c XOR (i mod 2)`. Even indices keep `c` and odd indices flip it. The expression `c ^ i & 1` follows Python’s bitwise precedence as `c ^ (i & 1)` and produces exactly that expected bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Count mismatched positions.** `map(int, s)` lazily converts the characters to zero or one, and `enumerate` provides their indices. The Boolean

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "111000"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct both target strings:** It simplifies visual comparison but allocates `O(n)` extra space.
- **Track the two mismatch types separately:** Counting misplaced zeros alone gives the swap count, but total mismatches divided by two is more symmetric.
- **Count difference above one:** No alternating arrangement exists because one symbol lacks enough separating copies.
- **Equal counts:** Both zero-starting and one-starting patterns must be tested.
- **One extra zero:** Only the zero-starting odd-length pattern is feasible.
- **One extra one:** Only the one-starting odd-length pattern is feasible.
- **Single character:** Its majority bit determines the pattern and zero swaps are needed.
- **Already alternating:** Its matching pattern has no mismatches.
- **Arbitrary-position swaps:** Division by two relies on being allowed to swap nonadjacent mismatches directly.
- **Mismatch parity:** For a feasible pattern, mismatch count is always even because misplaced zeros and ones balance.
- **Bitwise precedence:** The expression computes `c ^ (i & 1)`; explicit parentheses could make this easier to read without changing behavior.
- **Input preservation:** The immutable source string is scanned but never changed.
- **Even-length position counts:** Each pattern has exactly `n / 2` zero positions and `n / 2` one positions. That is why equal source counts make both patterns feasible rather than merely one of them.
- **Odd-length position counts:** The starting bit owns one extra position because indices zero, two, and so on include both ends. The majority character must therefore be the starting bit.
- **Pairing construction:** Collect mismatched zero positions and mismatched one positions in corresponding pairs. Swapping each pair independently reaches the target in exactly the mismatch-count-halved total, demonstrating achievability rather than only a lower bound.
- **Why adjacent order is irrelevant:** Since a permitted swap can connect any two positions, the physical distance between complementary mismatches never changes its cost; every paired correction costs one swap.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Counting zeros scans `s` once. `calc` scans it once per feasible pattern, at most twice. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
