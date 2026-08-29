# Guided Example: Destroying Asteroids

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mass": 10, "asteroids": [3, 9, 19, 5, 21]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `mass`, which represents the original mass of a planet. You are further given an integer array `asteroids`, where $\text{asteroids}[i]$ is the mass of the $i^{\text{th}}$ asteroid.

The objective is to compute `true` from `{"mass": 10, "asteroids": [3, 9, 19, 5, 21]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose the easiest remaining asteroid first

The planet may collide with asteroids in any order. Destroying an asteroid never decreases planet mass; it adds that asteroid's mass.

This makes ascending order the safest greedy choice. The source sorts `asteroids` and processes them from smallest to largest.

At asteroid mass `x`:

- if `mass < x`, the planet cannot destroy it and returns false;
- otherwise, it destroys the asteroid and updates `mass += x`.

The comparison permits equality, matching the rule that greater than or equal mass succeeds.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mass": 10, "asteroids": [3, 9, 19, 5, 21]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why failure at the smallest remaining asteroid is final

Suppose the sorted scan reaches `x` with planet mass smaller than `x`. Every unprocessed asteroid has mass at least `x`.

The planet cannot destroy any of them, so it has no way to gain additional mass. No different ordering of the remaining asteroids can help. Returning false is therefore a proof of impossibility, not merely failure of this particular order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why successful small collisions never hurt

If the planet can destroy the smallest remaining asteroid, doing so increases its mass. Any asteroid that was already destroyable remains destroyable, and some larger asteroids may become newly possible.

There is no resource consumed by a collision and no penalty for gaining mass. Thus postponing a destroyable small asteroid offers no advantage over taking its gain immediately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mass": 10, "asteroids": [3, 9, 19, 5, 21]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly search for any destroyable asteroid:** It may work but can cost $O(n^2)$. Sorting establishes a definitive order once.
- **Max-heap:** Choosing the largest currently destroyable asteroid can also gain mass, but requires maintaining eligibility. The ascending proof is simpler.
- **Original input order:** It may fail even when another ordering succeeds, so reordering is essential.
- **Equal mass:** The planet succeeds because the rule is `>=`.
- **One asteroid:** Return whether the initial mass covers it.
- **Duplicate masses:** They are processed separately and each contributes its mass.
- **Failure at smallest remaining:** Immediately proves all larger remaining asteroids are impossible too.
- **Large accumulated mass:** Use a sufficiently wide type outside Python.
- **Already huge planet:** Every sorted test succeeds.
- **Positive masses:** Every successful collision strictly increases planet mass.
- **Input mutation:** `asteroids.sort()` changes the caller's list order.
- **Early return:** Avoids scanning asteroids after impossibility is established.
- **Mass invariant:** Before each asteroid, all smaller available gains have already been collected.
- **Failure in unsorted order:** Would not be conclusive, which is why sorting is essential.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of asteroids.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
