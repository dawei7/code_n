# Guided Example: Maximum Length of a Concatenated String with Unique Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": ["un", "iq", "ue"]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

The objective is to compute `4` from `{"arr": ["un", "iq", "ue"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a set of lowercase letters with 26 bits

Each lowercase letter maps to one bit: `a` to bit zero, `b` to bit one, through `z` to bit 25. A mask stores one at a letter’s bit exactly when that letter is present.

For a string `t`, the code maps each character to `b = ord(c) - 97`. It tests `x >> b & 1` to see whether bit `b` is already set. If so, `t` itself contains a duplicate character and can never participate in a valid concatenation, so `x` is reset to zero and processing that string stops.

Otherwise, `x |= 1 << b` adds the character. Because input strings are nonempty, a valid string produces a positive mask; zero is reserved for invalid strings and the empty concatenation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": ["un", "iq", "ue"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain every valid combination mask

The list `s` begins as `[0]`, representing the choice to select no strings. After processing some prefix of `arr`, `s` contains a mask for every valid concatenation obtainable as a subsequence of that prefix.

For a valid current string mask `x`, it can be appended to an existing combination `y` exactly when they share no letter. Bitwise AND detects overlap:

`(x & y) == 0`.

When disjoint, `x | y` is the union mask for the extended concatenation. The source adds all such unions with:

`s.extend((x | y) for y in s if (x & y) == 0)`.

Existing masks remain in `s`, representing the choice to skip the current string. Newly appended masks represent taking it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why extending while iterating the same list is safe here

Python’s list iterator can observe elements appended during iteration. That deserves attention because the generator loops over `s` while `extend` adds to `s`.

Every newly added mask has the form `x | y` and therefore contains every bit of the nonzero `x`. When the iterator later reaches that new mask, `x & (x | y)` is nonzero, so the condition fails and no second copy of the same input string is appended.

Thus the operation terminates and has the intended effect. Taking a snapshot of the old list would be clearer, but the overlap condition makes the exact source correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": ["un", "iq", "ue"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Snapshot before extending:** Iterate over `s[:]` or its original length. This makes “use the current string at most once” explicit, at the cost of a temporary list.
- **Set of masks:** Deduplicate equivalent character sets and often reduce work. Hashing adds overhead but preserves the same worst-case exponential bound.
- **Backtracking with one mask:** Explore take/skip choices recursively using only \(O(n)\) stack space, though time remains exponential.
- **String with internal duplicates:** It is discarded because no valid concatenation can include it.
- **Overlap between two valid strings:** Bitwise AND rejects their combination immediately.
- **All strings mutually disjoint:** Every subset is valid, so the state list reaches \(2^n\) entries and the answer is the sum of all lengths, at most 26.
- **All choices invalid:** The initial zero state remains and `max` returns zero.
- **Different subsequences with the same mask:** The list may store duplicates, which affects constants but not the result.
- **Alphabet bound:** Only 26 bits are needed because every character is lowercase English.
- **Required Python version:** `int.bit_count` must be available; older versions can count set bits with another method.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+2^n)$. Let \(n=\lvert\texttt{arr}\rvert\) and let \(S\) be the sum of all string lengths. Building individual masks costs \(O(S)\). Across processing, at most one state exists per selected subsequence occurrence, so the total state-generation and scanning work is \(O(2^n)\) in the worst case. Final bit counting is also \(O(2^n)\). Total time is \(O(S+2^n)\).
- **Auxiliary Space Complexity:** $O(2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
