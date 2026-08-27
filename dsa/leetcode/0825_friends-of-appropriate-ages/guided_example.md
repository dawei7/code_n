# Guided Example: Friends Of Appropriate Ages

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ages": [16, 16]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` persons on a social media website. You are given an integer array `ages` where $\text{ages}[i]$ is the age of the $$i^{\text{th}}$$ person.

The objective is to compute `2` from `{"ages": [16, 16]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count ages instead of people

The decision to send a request depends only on the sender's age and the recipient's age. Individual identities matter only for excluding a person from sending to themself.

Ages are bounded from 1 through 120, so the solution builds `cnt` of length 121, where `cnt[a]` is the number of people aged `a`. This compresses as many as 20,000 people into at most 121 age categories.

The two nested loops then examine every ordered pair of ages `(ax, ay)`. Variable `x` is the number of possible senders aged `ax`, and `y` is the number of possible recipients aged `ay`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ages": [16, 16]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the rejection rules exactly

A sender aged `ax` does not request a recipient aged `ay` when at least one condition holds:

$$
ay\le 0.5ax+7,
$$

$$
ay>ax,
$$

or

$$
ay>100\ \text{and}\ ax<100.
$$

The code places these three conditions inside `not (...)`. It enters the counting branch only when none is true, exactly matching the statement's “otherwise.”

Age zero entries exist in the count array only for convenient indexing and have count zero, so they add nothing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A sender aged `ax` does not request a recipient aged `ay` wh... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count ordered requests

If `ax != ay` and the age pair is permitted, any of the `x` senders may request any of the `y` recipients. That gives `x * y` directed requests.

Direction matters. A request from person A to person B is distinct from a request from B to A, and the reverse age pair is evaluated separately by the loops. The rules are not generally symmetric.

When `ax == ay`, the raw product `x * y = x^2` includes each person choosing themself. For every one of the `x` senders, exactly one of the `y` same-aged recipients is that sender. Therefore, each sender has only `y - 1` valid same-age recipients, giving `x(y-1)`.

The expression

`x * (y - int(ax == ay))`

handles both cases. The equality converts to 1 for the same age and 0 otherwise.

For two people aged 16, the pair 16 to 16 passes because `16 > 15` and is not older than the sender. The contribution is `2 * (2 - 1) = 2`, representing the two opposite directed requests.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ages": [16, 16]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every pair of people:** It follows the d:** - **Check every pair of people:** It follows the definition directly but takes quadratic time. Age frequencies aggregate people with identical behavior.
- **- **Sort and use two pointers:** Sorting can count:** - **Sort and use two pointers:** Sorting can count eligible recipient ranges per sender age, but the fixed 1–120 domain makes a frequency table simpler.
- **- **Prefix sums by age:** They can sum allowed rec:** - **Prefix sums by age:** They can sum allowed recipient counts for each sender age. This reduces a generalized `A^2` scan to `O(A)`, though `A = 121` already makes the direct pair scan tiny.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + A^2)$. Let `n` be the number of people and `A = 121` be the size of the age domain.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
