# Guided Example: Solve the Equation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"equation": "x+5-3+x=6+x-2"}`
- **Required output:** `"x=2"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Solve a given equation and return the value of `'x'` in the form of a string `"x=#value"`. The equation contains only `'+'`, `'-'` operation, the variable `'x'` and its coefficient. You should return `"No solution"` if there is no solution for the equation, or `"Infinite solutions"` if there are infinite solutions for the equation.

The objective is to compute `"x=2"` from `{"equation": "x+5-3+x=6+x-2"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce each side to one coefficient and one constant

Every allowed term is either a constant integer or a multiple of `x`. Addition and subtraction are the only operations joining terms. Therefore, regardless of how many terms a side contains, that side can always be simplified to:

`coefficient * x + constant`.

The helper `f(s)` performs exactly that simplification. It returns a pair `(x, y)`, where `x` is the accumulated coefficient of the variable and `y` is the accumulated constant. The local variable named `x` is a number here; it is not the unknown itself.

For example, the side `x+5-3+x` simplifies as follows:

- `x` contributes one to the coefficient;
- `+5` contributes five to the constant;
- `-3` contributes negative three to the constant;
- `+x` contributes one more to the coefficient.

The returned pair is therefore `(2, 2)`, representing `2x + 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"equation": "x+5-3+x=6+x-2"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize the first term so every term has an explicit sign

Terms after the first naturally begin after a plus or minus sign, but the first term may have no leading sign. The parser makes the treatment uniform: if the side does not start with minus, it prepends plus.

After this normalization, the character at the current index is always a sign. The parser records `+1` for plus or `-1` for minus, advances past the sign, and scans forward until the next plus, the next minus, or the end of the side. The substring between those boundaries is exactly one unsigned term.

This design avoids special cases such as “if this is the first term.” A leading negative term already has its sign and is left unchanged; a leading positive term gains the explicit plus that later logic expects.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Terms after the first naturally begin after a plus or minus ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Classify a term by its last character

The permitted syntax makes term classification simple. If a term ends in `x`, it is a variable term. Otherwise, it is a constant.

For a variable term:

- `x` has an omitted coefficient, which means one;
- `2x` has coefficient two;
- the separately parsed sign makes `-x` contribute negative one and `-12x` contribute negative twelve.

The parser checks the term length. If the term consists only of `x`, it uses coefficient one. Otherwise, it converts the portion before the final `x` to an integer. It multiplies the coefficient by the saved sign and adds it to the coefficient total.

For a constant term, it converts the entire term to an integer, multiplies by the sign, and adds it to the constant total.

Because signs are handled outside the term text, integer conversion never has to interpret an embedded plus or minus.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"x=2"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"equation": "x+5-3+x=6+x-2"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"x=2"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Evaluate the entire equation in one pass:** Ma:** - **Evaluate the entire equation in one pass:** Maintain a side multiplier of plus one before `=` and negative one after it, then accumulate all variable coefficients and constants into one reduced equation. This avoids parsing the two sides separately and can avoid side-string copies, but requires careful sign composition.
- **- **Regular-expression tokenization:** A pattern c:** - **Regular-expression tokenization:** A pattern can extract signed terms concisely. It still takes linear time, but it hides some of the parsing logic, allocates match objects, and is easier to get wrong around omitted coefficients such as `x` and `-x`.
- **- **Symbolic algebra library:** A general solver i:** - **Symbolic algebra library:** A general solver is far more powerful than needed and introduces substantial overhead. The restricted one-variable linear grammar reduces to two integer totals directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the total number of characters in the equation. The equation is split once, and each character in each side is scanned a constant number of times. Parsing terms and accumulating their contributions therefore takes `O(N)` time overall. Python's integer conversions process the term digits; summed across all terms, those digits are still bounded by `N` under the standard fixed-width-value model used for this problem.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
