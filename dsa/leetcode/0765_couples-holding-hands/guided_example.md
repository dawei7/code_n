# Guided Example: Couples Holding Hands

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"row": [0, 2, 1, 3]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` couples sitting in `2n` seats arranged in a row and want to hold hands.

The objective is to compute `1` from `{"row": [0, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace people with their couple identifiers

People are numbered so partners are consecutive: `0` with `1`, `2` with `3`, and so on. Integer division by two converts a person ID to a couple ID. The exact source uses the equivalent bit shift:

`person >> 1`.

Thus both members of couple zero map to zero, both members of couple one map to one, and so forth.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"row": [0, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Treat every adjacent seat pair as a connection

Seats `0` and `1` must ultimately hold one couple, as must seats `2` and `3`, continuing in pairs. For each seat pair, the solution reads the couple IDs `a` and `b` of its two current occupants.

If `a == b`, that seat pair is already correct. If they differ, it connects two couples whose members are mixed within the same rearrangement problem.

The solution unions `a` and `b` in a disjoint-set structure. After all seat pairs are processed, each union-find component represents a group of couples whose members are interwoven among the same collection of seat pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why connected components describe independent work

Every couple contributes two people, and every seat pair contains two people. Inside one connected component of `c` couple IDs, exactly `2c` people occupy exactly `c` adjacent seat pairs.

No person from that component sits in a seat pair connected to a different component; such a seat pair would have created a union edge. Therefore components can be corrected independently.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"row": [0, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy physical swapping with a position map:** For every seat pair, locate the first person’s partner and swap it into place. This gives a direct `O(n)` solution when positions are updated.
- **Search for partners linearly:** It is easy to implement but can cost `O(n^2)`.
- **Union by size or rank:** Adding it supplies the strongest standard near-constant union-find guarantee.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of couples. The algorithm processes `n` seat pairs and performs a constant number of union-find operations per pair.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
