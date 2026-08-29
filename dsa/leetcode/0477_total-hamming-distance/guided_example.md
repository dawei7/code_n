# Guided Example: Total Hamming Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 14, 2]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

The objective is to compute `6` from `{"nums": [4, 14, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count differing pairs at one bit

Suppose the array has `n` positions. At bit `i`, let `a` be the number of values whose bit is one. Then `b = n - a` values have zero there.

To form an unordered pair that differs at this bit, choose one position from the one-group and one from the zero-group. There are

$$
a\cdot b
$$

such pairs. No division by two is needed: choosing from two distinct groups gives each unordered pair exactly once. There is no alternate selection order inside this product that creates the same pair again.

Pairs whose two bits are both zero or both one contribute nothing at this position and are not included.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 14, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract a bit

For value `x`, the expression

`x >> i & 1`

shifts bit `i` into the least significant position and masks away every other bit. The result is integer zero or one. Summing this expression across `nums` produces `a` directly.

Python operator precedence interprets it as `(x >> i) & 1`. Parentheses could improve readability but do not change the exact behavior.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why adding across bits gives total Hamming distance

The Hamming distance of one pair is the sum of one-unit indicators over all bit positions where it differs. Summing over pairs and then bits gives the same result as summing over bits and then pairs:

$$
\sum_{\{u,v\}}\sum_i [u_i\ne v_i]
=
\sum_i\sum_{\{u,v\}}[u_i\ne v_i].
$$

The inner sum on the right is exactly `a * b`. Therefore adding that product for every bit counts every pair's every differing position once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 14, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every pair:** XOR and population count is simple but costs $O(n^2B)$ time.
- **Store a 32-entry count array:** Count one-bits while scanning each number, then sum products. It has the same time and constant bounded space; the exact source instead computes each bit immediately.
- **Binary-string conversion:** Formatting every number into 32 characters adds allocation and parsing overhead without changing the counting idea.
- **Single element:** Every bit has either `a = 0` or `b = 0`, so the total is zero because no pair exists.
- **All values equal:** Each bit group is all zero or all one, so every product is zero.
- **Duplicate positions:** They remain separate choices in `a` and `b`, as required, even when their mutual distance is zero.
- **Zeros:** All their bits belong to the zero group and pair correctly with set bits of other values.
- **Leading zero positions:** They contribute zero and need no special handling.
- **Answer size:** Python accumulation cannot overflow; the source also guarantees the final result fits a signed 32-bit integer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nB)$. Let $B=32$ be the checked width and $n$ the array length. The outer loop has $B$ iterations, and each generator scans all `n` values. Time complexity is $O(nB)$, matching the manifest. With fixed $B=32$, this simplifies to $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
