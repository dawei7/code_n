# Guided Example: Number of Burgers with No Waste of Ingredients

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tomatoSlices": 16, "cheeseSlices": 7}`
- **Required output:** `[1, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `tomatoSlices` and `cheeseSlices`. The ingredients of different burgers are as follows:

The objective is to compute `[1, 6]` from `{"tomatoSlices": 16, "cheeseSlices": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the ingredient rules into two equations

Let $x$ be the number of jumbo burgers and $y$ be the number of small burgers. Every burger uses exactly one cheese slice, so using all cheese gives

$$
x+y=\texttt{cheeseSlices}.
$$

A jumbo burger uses four tomato slices and a small burger uses two, so using all tomatoes gives

$$
4x+2y=\texttt{tomatoSlices}.
$$

The task is not searching among many possible answers. These two independent equations determine at most one pair $(x,y)$. The only remaining question is whether that pair consists of nonnegative whole numbers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tomatoSlices": 16, "cheeseSlices": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive the exact variables used by the code

Write $C=\texttt{cheeseSlices}$ and $T=\texttt{tomatoSlices}$. Multiplying the cheese equation by four gives

$$
4x+4y=4C.
$$

Subtracting the tomato equation removes $x$:

$$
(4x+4y)-(4x+2y)=4C-T,
$$

so

$$
2y=4C-T.
$$

The source stores the right-hand side in `k = 4 * cheeseSlices - tomatoSlices`. Therefore the number of small burgers must be `y = k // 2`, and the cheese equation then gives `x = cheeseSlices - y` for the number of jumbo burgers.

This derivation also explains why the output order is `[x, y]`: the problem asks for jumbo burgers first and small burgers second.

For `tomatoSlices = 16` and `cheeseSlices = 7`, `k` is `28 - 16 = 12`. Thus `y = 6` and `x = 7 - 6 = 1`. Those burgers consume `4 * 1 + 2 * 6 = 16` tomato slices and `1 + 6 = 7` cheese slices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Write $C=\texttt{cheeseSlices}$ and $T=\texttt{tomatoSlices}... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Validate that the algebraic answer is physically possible

The expression $4C-T$ must be even because it equals $2y$. The condition `k % 2` detects an odd value. When it is odd, there is no integer number of small burgers, so the answer must be empty.

Both burger counts must also be nonnegative. The checks `y < 0` and `x < 0` reject algebraic solutions that would require a negative number of one burger type.

These nonnegativity checks have an intuitive ingredient interpretation. If $T>4C$, even making every cheese slice into a jumbo burger cannot consume all tomatoes; then $k<0$ and $y<0$. If $T<2C$, even making every burger small uses too many tomatoes; the derived $x$ becomes negative. Therefore a solution requires

$$
2C\le T\le4C,
$$

as well as compatible parity.

The return expression checks `k % 2 or y < 0 or x < 0`. If any invalid condition is true, it returns `[]`. Otherwise it returns `[x, y]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tomatoSlices": 16, "cheeseSlices": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every possible jumbo count:** Testing valu:** - **Try every possible jumbo count:** Testing values from zero through `cheeseSlices` eventually finds the same pair but takes $O(C)$ time despite the system having a direct algebraic solution.
- **Solve for jumbo burgers first:** Substituting `y = C - x` gives `x = (T - 2C) / 2`. This is equivalent; the exact source instead derives the small count through `4C - T`.
- **Odd tomato total:** Both burger types use an even number of tomato slices, so an odd `tomatoSlices` can never be consumed exactly; this appears as odd `k`.
- **Too many tomatoes:** If $T>4C$, even all jumbo burgers are insufficient and `y` becomes negative.
- **Too few tomatoes:** If $T<2C$, even all small burgers require more tomatoes and `x` becomes negative.
- **All jumbo burgers:** When $T=4C$, `k = 0`, so `y = 0` and `x = C`.
- **All small burgers:** When $T=2C$, `y = C` and `x = 0`.
- **No ingredients:** `[0, 0]` is valid because it leaves no unused slice.
- **One ingredient type absent:** A positive amount of only tomatoes or only cheese cannot form burgers and is rejected by nonnegativity.
- **Uniqueness:** Two linear equations with different tomato coefficients leave at most one candidate pair, so the method never needs to choose among several valid answers.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of integer multiplications, subtractions, divisions, remainder checks, comparisons, and list construction operations. Under the conventional fixed-width model for the bounded inputs, its time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
