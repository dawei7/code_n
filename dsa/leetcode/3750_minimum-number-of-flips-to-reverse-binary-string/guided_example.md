# Guided Example: Minimum Number of Flips to Reverse Binary String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 536870911}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `n`.

The objective is to compute `0` from `{"n": 536870911}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The target is fixed before any flips

Let `s` be the original binary representation and let `rev=s[::-1]`. The task is to change `s` into this fixed reversed original string. It is not asking merely to make the modified string a palindrome.

Each position can be handled independently: if `s[i]==rev[i]`, no flip is needed there; if they differ, that position must be flipped exactly once. The minimum is therefore the Hamming distance between `s` and its reverse.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 536870911}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Analyze mirrored positions as pairs

`rev[i]=s[m-1-i]`. Consider one mirrored pair `(i,m-1-i)`.

If the original bits are equal, reversing swaps equal values, so both target positions already match. The pair costs zero.

If the original bits differ, suppose they are zero and one. The reversed target requires one at the first position and zero at the second. Both original positions differ from their targets, so both must be flipped. The pair costs two.

This explains why the source examines only the first half and multiplies its mismatch count by two.

The middle position of an odd-length string mirrors itself. It always equals its reversed target and needs zero flips, so it is correctly excluded by `range(m//2)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact expression works

`bin(n)[2:]` creates the binary representation without Python's `"0b"` prefix. Positive `n` guarantees at least one bit and no leading zeros.

The generator

`s[i] != s[m-i-1]`

produces Boolean values for one representative of every mirrored pair. Python sums `true` as one and `false` as zero. Multiplying the number of mismatched pairs by two gives the number of mismatched positions.

For `n=10`, `s="1010"`. The outer pair one versus zero mismatches, and the inner pair zero versus one mismatches. Two pairs times two flips gives four.

For `n=7`, `s="111"`. The only examined pair matches, and the center needs no change, so the result is zero.

For `n=6`, `s="110"` and the fixed target is `"011"`. The outer pair one and zero differs, so positions zero and two both need flips; the middle one remains one. The answer is two. Merely flipping one outer bit could create a palindrome such as `"111"`, but that would not equal the required reversed original `"011"`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 536870911}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build the reversed string explicitly:** Comparing `s` with `s[::-1]` is correct and still $O(B)$, but it allocates another length-$B$ string. The exact source indexes mirrored positions directly.
- **Make `s` any palindrome:** That is a different goal. The required target is the reversal of the original string, even though equality with one's reverse characterizes palindromes only when no changes occur.
- **Count mismatched pairs without multiplying by two:** Each unequal mirrored pair requires two positional flips, not one.
- **Compare all `B` positions and also multiply:** That would double-count. The source compares half and doubles once.
- **Odd bit length:** The center maps to itself and costs zero.
- **Single-bit number:** There are no pairs, so the result is zero.
- **Already palindromic representation:** Every mirrored pair matches and no flips are required.
- **Alternating even-length bits:** Every mirrored pair may mismatch, causing all positions to flip.
- **Leading zeros:** The canonical representation has none, and reversal keeps the same fixed length even if its first target character is zero.
- **Positive-input guarantee:** It avoids the special representation of zero and ensures `bin(n)[2:]` is nonempty.
- **Independent flips:** No operation couples positions, which is why Hamming distance is exact.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let `B` be the bit length. Converting `n` to a binary string takes $O(B)$ time and space. The generator checks `floor(B/2)` pairs, taking $O(B)$ time. Total time is $O(B)$.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
