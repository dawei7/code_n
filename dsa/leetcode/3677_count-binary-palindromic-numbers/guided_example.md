# Guided Example: Count Binary Palindromic Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000000000000000}`
- **Required output:** `63356754`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **non-negative** integer `n`.

The objective is to compute `63356754` from `{"n": 1000000000000000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A binary palindrome is determined by its first half

For a binary string of length `L`, the second half must mirror the first.

If `L` is even, the first `L / 2` bits determine all remaining bits. If `L` is odd, the first `ceil(L / 2)` bits include the center and determine the rest.

Let

`h = ceil(L / 2) = (L + 1) // 2`.

Any positive `L`-bit integer must begin with one, so the first bit of this `h`-bit prefix is fixed. The other `h - 1` prefix bits are free.

Therefore the number of positive binary palindromes of length `L` is

`2^(h - 1)`.

The source writes the equivalent exponent

`(L - 1) // 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000000000000000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count zero separately

Positive binary representations have a leading one and are covered by the length formula. Number zero is special: its representation is `"0"` and it is declared palindromic.

For `n > 0`, the source initializes `answer = 1` to count zero.

For `n = 0`, it immediately returns one because there are no positive candidates to process.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Positive binary representations have a leading one and are c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Add every shorter binary length

Let `length = n.bit_length()`. Every positive integer with fewer than `length` bits is automatically at most `n`.

For each `shorter_length` from one through `length - 1`, the source adds

`1 << ((shorter_length - 1) // 2)`,

which is the count derived above.

After this loop, `answer` includes zero and every binary palindrome shorter than `n`’s representation. Only palindromes of exactly `length` bits remain to be bounded against `n`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `63356754` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000000000000000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `63356754` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every integer through `n`:** Convert:** - **Enumerate every integer through `n`:** Convert each to binary and test it, costing `O(n log n)` time.
- **Generate every palindrome explicitly:** It is much better than checking every integer but still unnecessary when prefix counts give a direct formula.
- **Mirror the center bit twice:** For odd lengths this creates one extra bit and the wrong number. Shift the prefix by one before mirroring.
- **Count prefixes from zero:** That introduces leading-zero strings representing shorter numbers and double-counts them.
- **Forget zero:** Positive-length formulas do not include it, but the statement explicitly declares it palindromic.
- **`n = 0`:** Return one immediately.
- **`n = 1`:** Count zero and binary `1`, returning two.
- **`n` itself palindromic:** The equal-prefix construction reproduces it and `<=` includes it.
- **Equal-prefix palindrome larger than `n`:** Do not add the final candidate.
- **Even length:** Mirror every prefix bit.
- **Odd length:** Exclude the center bit from the mirrored portion.
- **Power of two:** Its leading prefix may mirror to a number larger than it; the final comparison handles this boundary.
- **No leading zeros:** The prefix lower bound forces a leading one for every positive candidate.
- **Large constraint:** `10^15` needs at most 50 binary digits, so the logarithmic method is very small in practice.
- **Input preservation:** The integer is never modified outside local derived variables.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let `L = bit_length(n)`, which is `O(log n)` for positive `n`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
