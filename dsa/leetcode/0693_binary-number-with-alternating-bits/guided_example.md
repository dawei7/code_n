# Guided Example: Binary Number with Alternating Bits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1431655765}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

The objective is to compute `true` from `{"n": 1431655765}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reading one bit

The expression

`curr = n & 1`

uses bitwise AND with `1`. Since `1` has only its least significant bit set, every higher bit is cleared. The result is:

- `0` when the current least significant bit of `n` is zero;
- `1` when it is one.

No conversion to a binary string is necessary.

After the comparison, `n >>= 1` shifts all bits one place to the right. The bit just inspected is discarded, and its left neighbor in the original representation becomes the new least significant bit.

For example, starting from decimal `10`:

- binary `1010` yields current bit `0`;
- right shift produces binary `101`, whose current bit is `1`;
- later shifts expose `0` and then `1`.

The inspection order is right to left, but adjacency is symmetric. If every pair differs when read from the least significant side, every pair also differs in the usual left-to-right representation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1431655765}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The role of `prev`

`prev` stores the bit from the preceding loop iteration—that is, the original bit immediately to the right of `curr`.

The invariant at the beginning of each iteration is:

> Every adjacent pair among the bits already removed from `n` alternates, and `prev` is the most recently removed bit.

When `prev == curr`, two adjacent original bits are equal. The alternating requirement is violated, so the method returns `false` immediately. No later bits can repair an already invalid pair.

When they differ, the newly examined pair is valid. Assigning `prev = curr` extends the verified suffix by one bit, and the right shift prepares the next adjacent comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `prev` stores the bit from the preceding loop iteration—that... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `prev` starts at `-1`

Before the first bit is read, there is no previous bit to compare with. The code uses `-1` as a sentinel because a real binary digit can only be zero or one.

Therefore, the first comparison can never report equality. The first real bit is accepted and stored in `prev`. From the second iteration onward, both `prev` and `curr` are genuine adjacent bits.

An explicit “first iteration” branch would also work, but the sentinel keeps the loop uniform.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1431655765}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert to a binary string:** `bin(n)` followe:** - **Convert to a binary string:** `bin(n)` followed by adjacent-character comparisons is straightforward, but it uses `O(\log n)` extra string space.
- **- **XOR pattern observation:** If `n` alternates, :** - **XOR pattern observation:** If `n` alternates, then `x = n ^ (n >> 1)` consists entirely of ones. Such a number satisfies `x & (x + 1) == 0`. This gives a compact constant-number-of-operations test for fixed-width integers but is less immediately intuitive.
- **- **Single-bit numbers:** `1` has no adjacent pair:** - **Single-bit numbers:** `1` has no adjacent pair, so the property is vacuously true. The loop processes its only bit and returns `true`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(w)$. Let `w` be the number of significant bits in `n`:
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
