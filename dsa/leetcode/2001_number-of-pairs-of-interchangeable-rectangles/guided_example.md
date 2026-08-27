# Guided Example: Number of Pairs of Interchangeable Rectangles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rectangles": [[4, 8], [3, 6], [10, 20], [15, 30]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given `n` rectangles represented by a **0-indexed** 2D integer array `rectangles`, where $\text{rectangles}[i] = [\text{width}_{i}, \text{height}_{i}]$ denotes the width and height of the $$i^{\text{th}}$$ rectangle.

The objective is to compute `6` from `{"rectangles": [[4, 8], [3, 6], [10, 20], [15, 30]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a ratio exactly

Two rectangles are interchangeable when their fractions $w/h$ are equal. Using floating-point division as a dictionary key risks rounding concerns and is unnecessary.

The source reduces each fraction to lowest terms. It computes `g = gcd(w, h)` and replaces the dimensions with

`(w // g, h // g)`.

This pair is a canonical exact representation of the ratio.

For example, `(4,8)`, `(3,6)`, and `(10,20)` all reduce to `(1,2)`. Rectangles with unequal ratios reduce to different coprime pairs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rectangles": [[4, 8], [3, 6], [10, 20], [15, 30]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why gcd reduction is canonical

Let $g=\gcd(w,h)$. Dividing both values by $g$ removes every common factor, so the resulting numerator and denominator are coprime.

If two positive fractions are equal, cross multiplication gives $w_1h_2=w_2h_1$. Their reduced coprime representations must have the same numerator and denominator. Conversely, identical reduced pairs clearly represent equal fractions.

Thus tuple equality is necessary and sufficient for ratio equality.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let $g=\gcd(w,h)$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count pairs as each rectangle arrives

`cnt[ratio]` stores how many earlier rectangles have the same reduced ratio. When the current rectangle belongs to a class with count $c$, it forms one new pair with each of those $c$ earlier occurrences.

The source adds `cnt[(w,h)]` to `ans` and then increments the count. Updating after the addition prevents pairing a rectangle with itself.

This online counting automatically enforces index order: every pair is counted when its later index is processed, so the earlier member is already in the counter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rectangles": [[4, 8], [3, 6], [10, 20], [15, 30]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Floating-point ratio key:** Often works under :** - **Floating-point ratio key:** Often works under small values but relies on representation details and is less exact than reduced integers.
- **Cross-multiply every rectangle pair:** Avoids floating point but takes $O(N^2)$ time.
- **Group then use combinations:** First count every reduced ratio, then sum $c(c-1)/2$; equivalent to the online method.
- **Identical rectangles:** Counted as interchangeable distinct occurrences.
- **Proportional but different sizes:** Gcd reduction maps them to one key.
- **Only one rectangle:** Its prior count is zero and the answer is zero.
- **All ratios distinct:** Every counter lookup contributes zero.
- **All ratios equal:** The result is $N(N-1)/2$.
- **Positive dimensions:** Guarantee a nonzero denominator and positive gcd.
- **Large pair count:** Python integers hold values beyond 32-bit range.
- **Update order:** Add the prior count before incrementing the current rectangle.
- **Input preservation:** Local `w` and `h` are reassigned, but rectangle rows are not modified.
- **Environment imports:** The exact source assumes `Counter` and `gcd` are available.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log M)$. Let $N$ be the number of rectangles and $M$ the largest dimension. Euclid's algorithm computes each gcd in $O(\log M)$ time. Counter access is expected $O(1)$, so total expected time is $O(N\log M)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
