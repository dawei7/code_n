# Guided Example: Happy Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write an algorithm to determine if a number `n` is happy.

The objective is to compute `true` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow a deterministic sequence of numbers

Each positive integer has exactly one successor: the sum of the squares of its
decimal digits. Repeatedly applying that rule creates one deterministic chain.
The chain either reaches 1, after which the number is happy, or revisits an
earlier value, after which the same cycle repeats forever.

The exact optimal source detects repetition with set `vis`. It does not use
Floyd's two-pointer cycle detector, despite the manifest summary saying that it
does.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remember states before transforming them

The outer loop continues while `n != 1` and `n not in vis`. At the beginning of
an iteration, current `n` has not previously been processed, so the method adds
it to `vis` before calculating its successor.

Recording before transition is important. If a later transition returns to
this value, membership is already present and the loop stops without following
the same cycle again.

If current `n` is 1, the first condition stops immediately and the final
comparison returns true. If current `n` is a repeated non-1 value, the second
condition stops and the final comparison returns false.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extract decimal digits numerically

The inner loop initializes successor accumulator `x` to zero. `divmod(n, 10)`
returns the quotient and remainder from division by ten. The remainder `v` is
the current least significant decimal digit, and the quotient replaces `n`,
discarding that digit.

The update `x += v * v` adds its square. Repetition continues until the working
`n` becomes zero. Every original digit has then been extracted exactly once,
and `x` is the required digit-square sum. Assignment `n = x` advances the outer
chain.

Destroying the old numeric value during digit extraction is safe because it was
already stored in `vis`, and only its computed successor is needed afterward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Floyd cycle detection:** Advance one value by one transition and another by two; true constant auxiliary state and matches the manifest summary.
- **Known-cycle sentinel:** Stop when reaching 1 or 4, relying on the proven unique non-happy cycle for decimal digit squares.
- **Dictionary history:** Equivalent to the set but stores unnecessary values, as the competitive variant does.
- **String digit conversion:** Easier to read but allocates text for each transition.
- **Input 1:** Returns true without entering either loop.
- **Single-digit unhappy number:** Transitions normally and eventually repeats in the non-happy cycle.
- **Zeros inside a number:** Their square contributes zero and `divmod` handles them naturally.
- **Positive guarantee:** Avoids defining digit extraction and happiness for zero or negatives.
- **Fixed 32-bit domain:** Makes the reachable post-transition region a bounded constant.
- **Set growth:** Exact code remembers history even though a two-pointer alternative need not.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Processing the initial number's decimal digits costs $O(\log n)$. Its successor
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
