# Guided Example: Reverse Bits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 43261596}`
- **Required output:** `964176192`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Reverse bits of a given 32 bits signed integer.

The objective is to compute `964176192` from `{"n": 43261596}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the integer as exactly 32 positions

The operation reverses a fixed-width bit pattern, not merely the visible binary
digits of the integer. Leading zero positions are part of the 32-bit input and
become trailing zero positions in the answer. This is why the loop always runs
32 times, even if `n` becomes zero much earlier.

Number bit positions from 0 at the least significant end through 31 at the most
significant end. Reversal maps original position $i$ to destination position
$31-i$. The implementation processes original positions in increasing order
and builds that mapping explicitly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 43261596}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract the current least significant bit

`n & 1` isolates bit zero. Bitwise AND with binary `...0001` clears every other
position, leaving integer zero when the current bit is 0 and integer one when
it is 1.

After processing that bit, `n >>= 1` shifts the remaining input right. The bit
that was originally at position 1 becomes the new position 0, then original
position 2 does so on the next iteration. Thus loop index `i` corresponds to
the original bit position being examined.

The Reference restricts `n` to a nonnegative value, so Python's right shift
inserts zeros on the left. Negative Python integers use an unbounded two's
complement model and arithmetic right shift, which would require an explicit
32-bit mask; those values are outside this local contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Move the extracted bit to its mirrored destination

On iteration `i`, the expression `(n & 1) << (31 - i)` places the isolated bit
at output position $31-i$. If the input bit is zero, shifting zero changes
nothing. If it is one, the expression creates exactly one set bit at the
mirrored position.

The solution combines that bit with `ans` using bitwise OR. Each iteration
targets a different destination position, so no two contributions overlap and
OR is equivalent to adding the powers of two. OR states the bit-setting intent
more clearly and cannot carry into adjacent positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `964176192` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 43261596}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `964176192` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Mask-and-shift network:** Swap 16-bit halves, then bytes, nibbles, pairs, and adjacent bits; five fixed stages give $O(1)$ time.
- **Byte lookup table:** Reverse four bytes using a 256-entry cache and reorder them, useful when the function is called repeatedly.
- **Binary string:** Pad to exactly 32 characters before reversing; readable but allocates extra representation storage.
- **Input zero:** Every extracted bit is zero, so the answer remains zero.
- **Leading zeros:** They must be included conceptually even though integer formatting normally hides them.
- **Even input:** Maps a zero low bit to a zero high bit but requires no special branch.
- **Maximum permitted input:** Still uses the same 32 iterations and bounded shifts.
- **Negative integers:** Outside the Reference; mask with `0xffffffff` first if supporting signed Python inputs as raw 32-bit patterns.
- **Repeated calls:** A byte or nibble reversal table can trade a small fixed cache for fewer operations.
- **Variable width:** Replace constants 32 and 31 with the chosen explicit bit width.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop executes exactly 32 iterations. Under the problem's fixed 32-bit word
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
