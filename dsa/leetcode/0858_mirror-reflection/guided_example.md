# Guided Example: Mirror Reflection

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"p": 2, "q": 1}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered `0`, `1`, and `2`.

The objective is to compute `2` from `{"p": 2, "q": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Unfold reflections into a straight ray

Tracking every mirror bounce inside one square is awkward. Instead, imagine reflecting the room itself across a wall whenever the laser would bounce.

In this unfolded tiling of square rooms, the laser travels in one straight line. A receptor is reached when the line arrives at a corner of one reflected square.

Each time the ray crosses one room width `p` horizontally, its unfolded vertical rise is `q`. After `m` room widths, its coordinates relative to the original scale are:

$$
(mp,mq).
$$

It reaches a corner when the vertical coordinate is also a multiple of `p`:

$$
mq=np
$$

for some integer `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"p": 2, "q": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the first common alignment

Let `g=\gcd(p,q)`. Dividing by `g` gives coprime values:

$$
p'=\frac p g,\qquad q'=\frac q g.
$$

The smallest positive solution to:

$$
mq=np
$$

is:

$$
m=p',\qquad n=q'.
$$

So the first receptor depends only on whether `p'` and `q'` are odd or even.

The code calculates exactly these reduced parities:

`p = (p // g) % 2` and `q = (q // g) % 2`.

After these assignments, local `p` and `q` no longer store wall length and rise; each is only a parity bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret horizontal parity

Each unfolded room-width crossing alternates between the original room's east and west walls when folded back:

- odd `m=p'` means the receptor is on the east wall;
- even `m` means it is on the west wall.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"p": 2, "q": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate reflections geometrically:** It can work but needs repeated position/direction updates and potentially many bounces before a corner is reached.
- **Use least common multiple explicitly:** The first common height is `lcm(p,q)`. Dividing it by `p` and `q` yields the same parity counts, but gcd reduction avoids constructing more values.
- **`q=p`:** Gcd is `p`, reduced values are both one, and the ray reaches east-top receptor 1 immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log \min(p,q))$. Euclid's algorithm computes `gcd(p,q)` in:
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
