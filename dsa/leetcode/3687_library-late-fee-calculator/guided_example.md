# Guided Example: Library Late Fee Calculator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"daysLate": [5, 1, 7]}`
- **Required output:** `32`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `daysLate` where $\text{daysLate}[i]$ indicates how many days late the $$i^{\text{th}}$$ book was returned.

The objective is to compute `32` from `{"daysLate": [5, 1, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Handling the exceptional one-day rule first

The helper begins with:

`if x == 1:`

`    return 1`

One day late is a special fixed fee of one. It must not fall through to the ordinary $2x$ rule, which would incorrectly charge two.

The equality check is exact. It does not say `x <= 1` because the constraints already guarantee every delay is at least one, and the stated exceptional case is specifically $x=1$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"daysLate": [5, 1, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handling delays above five days

The next branch is:

`if x > 5:`

`    return 3 * x`

The strict comparison places $6$ and all larger delays in the highest-rate bracket while leaving $5$ in the middle bracket. This boundary is a common source of off-by-one errors: the statement says $2 \le x \le 5$ for the doubled fee and $x>5$ for the tripled fee.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The next branch is:

`if x > 5:`

`    return 3 * x`

The st... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Using the remaining constraints for the middle bracket

If neither earlier branch returns, `x` is not one and is not greater than five. Since the contract guarantees $x\ge1$, the only remaining possibilities are $2,3,4,5$. The helper can therefore finish with:

`return 2 * x`

No additional comparison is needed. The order of the branches partitions every legal input into exactly one fee category.

For the boundary values, the helper returns:

- $f(1)=1$;
- $f(2)=4$;
- $f(5)=10$; and
- $f(6)=18$.

These four checks capture both transitions between fee brackets.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `32` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"daysLate": [5, 1, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `32` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit loop with an accumulator:** A loop th:** - **Explicit loop with an accumulator:** A loop that selects a branch and adds to `total` is equally $O(n)$ and may be more verbose. The generator-plus-helper source expresses the same scan compactly.
- **List comprehension before summing:** `sum([f(x) for x in daysLate])` returns the same result but allocates $O(n)$ temporary space. The generator keeps auxiliary space constant.
- **Sort by lateness:** Sorting does not help because fee calculation is independent for every book and addition ignores order. It would unnecessarily increase time to $O(n \log n)$.
- **Delay exactly one:** This must return a fixed fee of $1$, not $2x$. The first branch handles the exception.
- **Delay exactly five:** Five belongs to the inclusive middle interval, so its penalty is $10$, not $15$.
- **Delay exactly six:** Six satisfies `x > 5` and begins the tripled-rate interval, producing $18$.
- **Repeated delays:** Each array position represents a separate book, so equal delays contribute equal fees repeatedly; they must not be deduplicated.
- **One book:** The generator produces one fee, and `sum` returns it unchanged.
- **Positive-delay guarantee:** A zero or negative delay is outside the contract. The helper's final branch relies on legal remaining values being between two and five.
- **No cumulative bracket:** Ten books each one day late cost ten in total. Their delays are not combined into ten days before applying the fee rule.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(daysLate)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
