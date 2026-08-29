# Guided Example: Rabbits in Forest

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"answers": [1, 1, 2]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a forest with an unknown number of rabbits. We asked n rabbits **"How many other rabbits have the same color as you?"** and collected the answers in an integer array `answers` where $\text{answers}[i]$ is the answer of the $i^{\text{th}}$ rabbit.

The objective is to compute `5` from `{"answers": [1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret one answer as a complete color-group size

If a rabbit answers `x`, it claims that exactly `x` other rabbits share its color. Including the rabbit that spoke, that color must contain

$$
g = x + 1
$$

rabbits in total.

For example, an answer of two describes a color group of three rabbits. Some of those three may not be among the questioned rabbits, but they must still exist in the forest and must be counted in the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"answers": [1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rabbits with different answers cannot share a color

Every rabbit of one color sees the same number of other rabbits of that color. Therefore all members of a color group would give the same answer.

A rabbit answering one belongs to a two-rabbit color, while a rabbit answering two belongs to a three-rabbit color. They cannot be describing the same color. This lets the algorithm handle each distinct answer value independently and add the resulting minimum group sizes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rabbits with the same answer can share groups, but each group has a capacity

Suppose `v` questioned rabbits all answered `x`. A single color group for that answer has size `g = x + 1`, so at most `g` of those respondents can share one color.

Packing as many respondents as possible into each group minimizes the total number of implied rabbits. If `v <= g`, all `v` respondents can belong to one color, but the forest must still contain the full `g` rabbits of that color. If `v > g`, at least two colors with that same group size are needed, and so on.

The minimum number of groups is

$$
\left\lceil \frac{v}{g} \right\rceil.
$$

Each group contributes all `g` rabbits, whether or not every member answered the survey. Thus this answer class contributes

$$
\left\lceil \frac{v}{g} \right\rceil g.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"answers": [1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the answers:** Equal values become consecutive and can be grouped in $O(n \log n)$ time with little extra storage, but hashing reaches linear expected time.
- **Track remaining capacity online:** A map can remember open spots in the current color group for each answer. It is valid but more stateful than rounding a final frequency.
- **Count only respondents:** Incorrect whenever a color group is not filled by questioned rabbits, because unquestioned members still exist.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of responses and $u$ the number of distinct answer values. Building the counter takes $O(n)$ expected time. Iterating over its $u$ entries takes $O(u)$ time, and $u \le n$, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
