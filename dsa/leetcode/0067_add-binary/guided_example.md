# Guided Example: Add Binary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": "11", "b": "1"}`
- **Required output:** `"100"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two binary strings `a` and `b`, return *their sum as a binary string*.

The objective is to compute `"100"` from `{"a": "11", "b": "1"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Binary addition follows the same rule as decimal addition

Addition starts with the least significant characters at the right ends of `a` and `b`. At each position, add the available input bits and the incoming carry. The output bit is the total modulo 2, and the next carry is the total divided by 2.

Because each input bit is 0 or 1 and the incoming carry is at most 1, the position total is 0, 1, 2, or 3. Its quotient by 2 is always a valid carry bit, and its remainder is always a valid output bit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": "11", "b": "1"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use independent pointers for unequal lengths

`i` starts at the last character of `a`, and `j` starts at the last character of `b`. The strings may have different lengths, so each contribution is conditional. If a pointer is negative, that input contributes zero at the current higher position.

This is equivalent to conceptually padding the shorter string with leading zeros, but it avoids constructing a padded copy.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One variable temporarily holds the column total

At loop entry, `carry` is the incoming carry from the previously processed lower bit. The assignment adds the current bits into that variable. Then `carry, v = divmod(carry, 2)` replaces it with the outgoing quotient and stores the remainder in `v`.

For example, adding bit 1, bit 1, and carry 1 gives total 3. `divmod(3,2)` returns `(1,1)`: write output bit 1 and carry 1 leftward. Adding two ones with no carry gives total 2, which produces output 0 and carry 1.

Reusing the variable is safe because the old carry has already been included in the total before it is overwritten.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"100"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": "11", "b": "1"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"100"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Preallocate an output array:** Reserve $L+1$ positions and fill from right to left, then omit an unused leading slot. It avoids a reverse slice but needs careful start indexing.
- **Repeated string concatenation:** It is syntactically shorter but can copy the growing prefix repeatedly and become quadratic under a conservative analysis.
- **Pad the shorter input:** It simplifies paired indexing but allocates an unnecessary leading-zero string.
- **Convert complete strings to integers:** Python permits it, but this bypasses the intended arbitrary-length bit addition and may be unavailable in fixed-width environments.
- **Different lengths:** A negative pointer contributes zero, so the longer prefix is processed correctly.
- **Final carry:** The loop condition emits it as a new leading 1.
- **Both inputs zero:** One iteration appends zero and returns `"0"`.
- **No leading zeros:** The source adds no leading zero; any final extra bit is a real carry.
- **Maximum length:** Work scales with characters, not numeric magnitude.
- **Input preservation:** Strings are immutable and never sliced or altered.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L=\max(m,n)$. The loop performs at most $L+1$ iterations. Reversing the list and joining the result are also $O(L)$, so total time is $O(L)$.
- **Auxiliary Space Complexity:** $O(\max(m,n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
