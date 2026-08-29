# Guided Example: Minimum Flips to Make a OR b Equal to c

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": 2, "b": 6, "c": 5}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make ( `a` OR `b` == `c` ). (bitwise OR operation).

The objective is to compute `3` from `{"a": 2, "b": 6, "c": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: When the target bit is zero

If `z == 0`, the OR result must be zero. OR is zero only when both input bits are zero.

Each current one must therefore be flipped independently:

- `x = 0, y = 0` needs zero flips;
- exactly one of `x` and `y` is one, so one flip is needed;
- both are one, so both must change and two flips are needed.

Because `x` and `y` are each zero or one, `x + y` is exactly that required count. This explains the expression `x + y if z == 0`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": 2, "b": 6, "c": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When the target bit is one

If `z == 1`, the OR result needs at least one input one.

If either `x` or `y` is already one, the condition is satisfied and no flip is needed. If both are zero, one of them must be flipped to one. Flipping both would be unnecessary.

`int(x == 0 and y == 0)` converts this Boolean condition to one when both are zero and zero otherwise.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Adding independent costs

`ans` accumulates the required contribution for all positions. A choice made at one bit cannot help or hurt another bit, so choosing the local minimum at every position produces a globally minimum total.

For `a = 2`, `b = 6`, and `c = 5`:

- at bit zero, input bits are zero and zero while the target is one, costing one;
- at bit one, input bits are one and one while the target is zero, costing two;
- at bit two, input bits are zero and one while the target is one, costing zero.

All higher relevant bits are zero. The total is three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": 2, "b": 6, "c": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Shift values in a while loop:** Repeatedly inspect `a & 1`, `b & 1`, and `c & 1` and right-shift until all become zero. It naturally adapts to bit length but mutates local copies.
- **Population-count formula:** Count set bits in `(a | b) ^ c`, then add another count for positions where both `a` and `b` are one but `c` is zero. It is concise but less transparent.
- **Target zero with two ones:** This is the only per-bit case requiring two flips; one remaining one would keep OR equal to one.
- **Target one with two zeros:** Exactly one flip is enough; the algorithm must not count two.
- **Already matching OR:** Every position contributes zero, so the answer is zero.
- **Higher zero bits:** They add nothing because `x = y = z = 0`.
- **32-bit assumption:** It is safe for values at most $10^9$ but not for unrestricted Python integers.
- **Operator precedence:** The exact expressions rely on shifts and bitwise AND producing the selected bit; parentheses can make `(a >> i) & 1` easier to read.
- **Flips apply only to `a` and `b`:** `c` is a fixed target, and the algorithm never changes it.
- **Independence:** There are no carries in bitwise OR, unlike addition, so per-position optimization is valid.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The exact code always performs 32 iterations with constant work, so under the stated bounded integer type its running time is $O(1)$ and auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
