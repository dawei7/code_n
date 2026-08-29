# Guided Example: Eat Pizzas!

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"pizzas": [1, 2, 3, 4, 5, 6, 7, 8]}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `pizzas` of size `n`, where $\text{pizzas}[i]$ represents the weight of the $i^{\text{th}}$ pizza. Every day, you eat **exactly** 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights `W`, `X`, `Y`, and `Z`, where $W \le X \le Y \le Z$, you gain the weight of only 1 pizza!

The objective is to compute `14` from `{"pizzas": [1, 2, 3, 4, 5, 6, 7, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate score-producing pizzas from fillers.** Every day consumes four pizzas. On an odd day, only the largest selected weight $Z$ contributes. The other three can be smaller fillers. On an even day, the second-largest $Y$ contributes, so that day also needs one pizza at least as large as $Y$ to serve as the non-scoring $Z$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"pizzas": [1, 2, 3, 4, 5, 6, 7, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

Among 1-indexed days, the number of odd days is `odd = (days + 1) // 2`, and even days number `even = days - odd`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"pizzas": [1, 2, 3, 4, 5, 6, 7, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate all daily groupings:** The number of partitions into groups of four is enormous. Only sorted role ranks affect the score.
- **Use the four largest pizzas every day:** This wastes valuable weights in non-scoring roles and can reduce later scores.
- **Score the largest remaining pizza on an even day:** It cannot be $Y$ without an even larger $Z$ in the same group.
- **One day:** It is odd, so the largest pizza is the answer and the other three are fillers.
- **No even days:** The loop is empty and only the largest odd-count weights score.
- **Duplicate weights:** Any equal copies can exchange roles without changing feasibility or score.
- **All weights equal:** Every day scores that common weight, and the formula selects exactly one score per day.
- **In-place sorting:** Callers needing original order must pass a copy.
- **Odd-day count:** Ceiling division reflects days $1,3,5,\ldots$.
- **All pizzas consumed:** The role-and-filler count accounts for exactly four pizzas per day.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n=\lvert\texttt{pizzas}\rvert$. Sorting dominates with $O(n\log n)$ time. Summing odd winners and iterating over at most $n/8$ even days take $O(n)$ additional time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
