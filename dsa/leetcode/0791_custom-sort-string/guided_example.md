# Guided Example: Custom Sort String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"order": "cba", "s": "abcd"}`
- **Required output:** `"cbad"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.

The objective is to compute `"cbad"` from `{"order": "cba", "s": "abcd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the custom order into numeric ranks

String `order` already lists its characters from earliest to latest. The dictionary comprehension:

`d = {c: i for i, c in enumerate(order)}`

assigns rank zero to the first character, rank one to the second, and so on. Characters in `order` are unique, so no later dictionary entry overwrites an earlier rank.

Once these ranks exist, arranging the constrained characters is an ordinary key-based sort: smaller rank means earlier in the result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"order": "cba", "s": "abcd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand exactly what the output condition requires

If character `x` occurs before character `y` in `order`, every sorted occurrence of `x` must be placed before every occurrence of `y`.

Characters that do not occur in `order` have no constraint relative to any other character. They may appear at the beginning, end, or between constrained groups. The method is therefore free to assign all such characters any convenient rank.

The exact key function is:

`lambda x: d.get(x, 0)`.

For a character in `order`, it returns the recorded index. For an absent character, `get` returns zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why default rank zero is valid

Rank zero is also the rank of `order[0]`. Consequently, unconstrained characters are tied with the first custom-ordered character.

This does not violate the problem:

- Every first-ranked character and every absent character still has a key smaller than ranks one, two, and so on.
- The relative placement of absent characters versus the first-ranked character is unrestricted.
- All later custom-ranked groups remain in their required order.

Some implementations put absent characters after all ordered characters by using default rank `len(order)`. That is also valid, but it produces a different permitted answer. The problem accepts any satisfying permutation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"cbad"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"order": "cba", "s": "abcd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"cbad"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency counting:** Count characters in `s`, emit ordered groups following `order`, then emit leftovers. This achieves $O(m+n)$ time and is the method matching the manifest.
- **Default leftovers after the order:** Use key `d.get(x, len(order))` to place absent characters at the end. It remains valid but differs from the exact source's output placement.
- **Custom comparator:** Compare characters by rank directly, but repeated map lookups and comparator calls are more cumbersome than a key function.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m$ be the length of `order` and $n$ the length of `s`. Building the rank dictionary costs $O(m)$ expected time and $O(m)$ space.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
