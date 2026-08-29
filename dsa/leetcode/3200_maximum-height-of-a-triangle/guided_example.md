# Guided Example: Maximum Height of a Triangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"red": 2, "blue": 4}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `red` and `blue` representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1^st row will have 1 ball, the 2^nd row will have 2 balls, the 3^rd row will have 3 balls, and so on.

The objective is to compute `3` from `{"red": 2, "blue": 4}` while avoiding redundant calculations and unnecessary overhead.

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

**For a fixed first color, there are no choices.** Row $1$ needs one ball, row $2$ needs two, and in general row $i$ needs exactly $i$ balls. Every row is monochromatic, and neighboring rows have different colors. Once the color of row $1$ is chosen, all later row colors are forced to alternate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"red": 2, "blue": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

There are exactly two possible color patterns:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- red, blue, red, blue, and so on;
- blue, red, blue, red, and so on.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"red": 2, "blue": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Closed-form feasibility test:** Use $p^2$ and $q(q+1)$ to test a proposed height for both starting colors. This matches the mathematical resource formulas but still needs a way to find the largest feasible $h$.
- **Binary search on height:** Feasibility is monotone: if height $h$ is possible for a fixed start, every smaller height is possible. Binary search with the closed-form tests runs in $O(\log(red+blue))$ time and $O(1)$ space, which is not better than a direct inverse formula but avoids row simulation.
- **Direct inverse-square formulas:** Candidate bounds can be derived with integer square roots for odd- and even-row totals, yielding true $O(1)$ arithmetic under fixed-width integers. Care is needed with floors and with reconciling the two colors.
- **Try only the more numerous color first:** This is unsafe. Row sizes differ by parity, and the scarcer color may be better suited to the smaller odd or even total for the eventual height. Both starts must be evaluated.
- **Use leftover balls to recolor a row:** Not allowed. A row's color is fixed by alternation, and balls of the other color cannot substitute.
- **Skip an unaffordable row:** Not allowed. Height counts consecutive rows starting at one; row $i+1$ cannot exist without row $i$.
- **Equal color counts:** Both starting patterns are symmetric and reach the same height, though the source still tests each.
- **One color nearly absent:** At least row one can be built because both inputs are at least one. A second row requires two balls of the opposite color.
- **Surplus of one color:** The result may be limited entirely by the other color. Unused surplus does not increase height.
- **Answer update timing:** `ans` is updated only after successfully paying for row `i`. The failed row is never counted.
- **Fresh counts per start:** Reusing the mutated `c` from the first simulation would undercount the second. Creating a new list inside the loop prevents that error.
- **Integer arithmetic:** Every subtraction and comparison is exact. No floating-point square-root rounding enters the simulated source.
- **Manifest mismatch:** The exact implementation is iterative simulation, not a closed-form solution. Its $O(1)$ time claim is defensible only because the input values are capped at $100$, not as a parameterized asymptotic bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{red+blue})$. Let $S=red+blue$. Building height $h$ consumes
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
