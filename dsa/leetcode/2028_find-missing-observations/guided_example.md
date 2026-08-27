# Guided Example: Find Missing Observations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rolls": [3, 2, 4, 3], "mean": 4, "n": 2}`
- **Required output:** `[6, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have observations of $n + m$ **6-sided** dice rolls with each face numbered from `1` to `6`. `n` of the observations went missing, and you only have the observations of `m` rolls. Fortunately, you have also calculated the **average value** of the $n + m$ rolls.

The objective is to compute `[6, 6]` from `{"rolls": [3, 2, 4, 3], "mean": 4, "n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recover the sum that the missing rolls must have

There are `m = len(rolls)` known observations and `n` missing observations. If the average across all `m+n` rolls must be exactly `mean`, then their required total sum is

$$
(m+n)\cdot\textit{mean}.
$$

The known observations already contribute `sum(rolls)`. Therefore the missing observations must contribute

$$
s=(m+n)\cdot\textit{mean}-\sum\texttt{rolls}.
$$

This is the value calculated by the source. Once `s` is known, the original average requirement becomes a simpler construction problem: produce exactly `n` legal die values whose sum is `s`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rolls": [3, 2, 4, 3], "mean": 4, "n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Determine whether that sum is possible

Every six-sided die value is at least one. Consequently, `n` missing dice have minimum possible sum `n`. Every value is at most six, so their maximum possible sum is `6n`.

The necessary condition is therefore

$$
n\le s\le6n.
$$

It is also sufficient. Every integer sum in this inclusive range can be distributed among `n` values from one through six. The source checks both boundaries and immediately returns an empty list when `s<n` or `s>6n`.

This test handles both directions of impossibility. A very large known sum can make the required missing sum too small, while a small known sum combined with a high requested mean can make it too large.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every six-sided die value is at least one.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Distribute the sum as evenly as possible

On feasible input, divide `s` by `n`:

$$
q=\left\lfloor\frac{s}{n}\right\rfloor,\qquad r=s\bmod n.
$$

The source first creates `n` copies of `q`. Their current total is `nq`. By the division algorithm,

$$
s=nq+r
$$

with `0\le r<n`. The construction then increments the first `r` entries by one. That adds exactly the missing remainder, so the final sum is `s`.

The resulting list contains `r` copies of `q+1` and `n-r` copies of `q`. The order is irrelevant because the task accepts any valid set of missing observations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rolls": [3, 2, 4, 3], "mean": 4, "n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Start every die at one:** Distribute `s-n` ext:** - **Start every die at one:** Distribute `s-n` extra points, at most five per die; this is equivalent but requires a slightly more explicit capacity loop.
- **Backtracking over die faces:** It explores many unnecessary combinations even though only the total matters.
- **Random valid distribution:** It can work but complicates reproducibility and range enforcement without improving complexity.
- **Required sum exactly `n`:** Every missing roll must be one.
- **Required sum exactly `6n`:** Every missing roll must be six.
- **Required sum below `n`:** Return empty because even all ones are too large.
- **Required sum above `6n`:** Return empty because even all sixes are too small.
- **Remainder zero:** Every output value is the quotient.
- **Positive remainder:** Exactly that many entries receive one extra point.
- **One missing roll:** It must equal `s`, provided `1<=s<=6`.
- **Many valid answers:** The source returns a balanced one; output order has no semantic importance.
- **Exact average:** Total-sum arithmetic avoids floating-point comparison.
- **Input preservation:** `rolls` is never changed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M+N)$. Let $M$ be the number of known rolls and $N$ the number of missing rolls. Computing `sum(rolls)` takes $O(M)$ time. Allocating the answer takes $O(N)$ time, and incrementing the first remainder entries takes at most $N-1$ additional operations. Total time is $O(M+N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
