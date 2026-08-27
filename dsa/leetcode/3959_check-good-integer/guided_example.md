# Guided Example: Check Good Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`.

The objective is to compute `false` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the per-digit transformation is safe

The transformation does not approximate or change the condition. For every digit `d`, `d(d-1)` is exactly `d^2-d`. Adding these terms for all digits is exactly the requested square-sum minus digit-sum.

This form also reveals useful behavior:

- digit `0` contributes `0(0-1)=0`;
- digit `1` contributes `1(1-1)=0`;
- every digit from `2` through `9` contributes a positive amount;
- the largest single-digit contribution is `9 \cdot 8=72`.

Thus zeros and ones do not affect goodness, while sufficiently large digits can make the threshold reachable quickly. The source still processes all digits rather than returning early, which keeps the code simple and exactly matches the final comparison.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extracting decimal digits without building a string

The loop uses



For a nonnegative integer, division by ten separates the number into two parts. The quotient is the number with its last decimal digit removed, and the remainder is that last digit. Python's `divmod(n, 10)` returns both values together. The quotient is assigned back to the local variable `n`, and the remainder is assigned to `x`.

The next line,



adds `x^2-x` to the accumulated difference. Repeating this process removes one decimal digit per iteration. Eventually the quotient becomes zero and `while n` stops.

At the start of each iteration, `s` equals the sum of `d(d-1)` over every digit already removed from the original number. The still-unprocessed prefix is held in `n`. The iteration extracts exactly its final digit, adds exactly that digit's contribution, and replaces the prefix with the remaining quotient. When the loop terminates, no digits remain in the prefix, so `s` equals the complete square-sum minus digit-sum.

Finally,



uses `>=` because a difference equal to `50` is good; it does not have to be strictly greater.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop uses



For a nonnegative integer, division by ten ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A complete trace

Consider `n=529`. Initially `s=0`.

1. `divmod(529, 10)` gives quotient `52` and digit `9`. The contribution is `9 \cdot 8=72`, so `s=72`.
2. `divmod(52, 10)` gives quotient `5` and digit `2`. The contribution is `2 \cdot 1=2`, so `s=74`.
3. `divmod(5, 10)` gives quotient `0` and digit `5`. The contribution is `5 \cdot 4=20`, so `s=94`.

The loop ends, and `94 \ge 50` is true. Checking from the definition gives the same result: the square-sum is `25+4+81=110`, the digit sum is `5+2+9=16`, and their difference is `94`.

For contrast, `n=123` contributes `1\cdot0+2\cdot1+3\cdot2=8`, so it is not good.

Reassigning the parameter name `n` does not modify an integer owned by the caller. Python integers are immutable, and the assignment merely makes the local name refer to the next quotient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two separate accumulators:** Summing `x` into :** - **Two separate accumulators:** Summing `x` into one variable and `x^2` into another, then comparing their difference, is correct and has the same asymptotic bounds. The source's single accumulator more directly tracks the only quantity the answer needs.
- **- **String conversion:** Converting `n` to text an:** - **String conversion:** Converting `n` to text and iterating over characters is also `O(D)` time, but it allocates `O(D)` extra storage for the decimal representation. Arithmetic extraction preserves constant auxiliary space.
- **- **Precomputed digit contributions:** A ten-entry:** - **Precomputed digit contributions:** A ten-entry table for `d(d-1)` could replace the multiplication. Because there are only ten possible digits, this remains correct, but it adds a collection without changing the asymptotic or practical structure of the solution.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let `D` be the number of decimal digits in `n`. Every loop iteration removes exactly one digit, and each iteration performs a constant amount of arithmetic and assignment. The running time is therefore `O(D)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
