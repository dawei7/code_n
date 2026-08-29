# Guided Example: Binary Gap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000000000}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a positive integer `n`, find and return *the **longest distance** between any two **adjacent** *`1`*'s in the binary representation of *`n`*. If there are no two adjacent *`1`*'s, return *`0`*.*

The objective is to compute `3` from `{"n": 1000000000}` while avoiding redundant calculations and unnecessary overhead.

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

The binary gap concerns consecutive set bits, not every possible pair of set bits. A set bit is a binary digit equal to `1`. Two such bits are adjacent for this problem when no other `1` lies between them, even though any number of `0` digits may lie between them. Therefore, while scanning the binary representation, the only history needed for a newly encountered `1` is the position of the previous `1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000000000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution reads bits from right to left, beginning with the least significant bit. The variable `cur` is the position of the bit currently being examined: position zero for the rightmost bit, position one for the next bit, and so on. The test `n & 1` is nonzero exactly when the current least significant bit is `1`. After processing that bit, `n >>= 1` discards it and shifts the next bit into the least significant position. Incrementing `cur` keeps the position synchronized with that shift.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**The two pieces of state.** The variable `pre` stores the original position of the most recently encountered `1`. The variable `ans` stores the largest distance between consecutive `1` bits found so far. When the current bit is `1`, the distance from the preceding set bit is `cur - pre`. The update

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000000000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store all set-bit positions:** First collect every position containing `1`, then compare neighboring positions in the list. This is correct and still takes $O(\log n)$ time, but it uses $O(\log n)$ space that the one-pass state makes unnecessary.
- **Convert to a binary string:** Scanning `bin(n)` can be visually intuitive. It also takes $O(\log n)$ time, but creates an $O(\log n)$ string and requires careful treatment of indices or counts between ones.
- **Count zeros between ones:** One can reset a counter whenever a `1` appears and translate a run of zeros into a distance by adding one. This is equivalent, but tracking absolute bit positions makes the definition of distance more direct.
- **Compare every pair of ones:** This does extra work and, more importantly, includes pairs that are not adjacent because another `1` may separate them. Only consecutive set bits are valid candidates.
- **Exactly one set bit:** Powers of two such as `8 = 1000` contain no pair. The infinity sentinel ensures the answer remains zero.
- **Adjacent literal ones:** A suffix such as `11` gives a distance of one. No separating zero is required for two set bits to be adjacent under the definition.
- **Long zero run:** For `100001`, the two ones are still adjacent because there is no intervening one, and their positional difference is five.
- **Three or more ones:** Only neighboring ones in positional order are compared. For `10101`, the outer ones are not a valid pair because the middle one separates them.
- **Least significant bit set:** If the rightmost bit is `1`, it is simply recorded at position zero; no special indexing adjustment is needed.
- **Maximum allowed value:** The constraint $n \le 10^9$ means at most 30 relevant bits, but the loop is written generically and naturally stops after the actual most significant set bit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(b)$. Let $b = \lfloor\log_2 n\rfloor+1$ be the number of bits in the positive integer `n`. Each loop iteration examines one bit, performs constant-time arithmetic and bit operations, and shifts the number once.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
