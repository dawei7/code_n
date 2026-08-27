# Guided Example: K-Similar Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "ab", "s2": "ba"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Strings `s1` and `s2` are `k`**-similar** (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

The objective is to compute `1` from `{"s1": "ab", "s2": "ba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search strings by number of swaps

Each state is a string obtainable from `s1`. An edge represents one swap of two positions. The task asks for the fewest swaps reaching `s2`, so breadth-first search over this unweighted state graph is appropriate.

The queue starts with `s1` at distance zero. Each BFS level adds one swap. The first time `s2` is dequeued, the current level `ans` is the minimum possible number of swaps.

The challenge is generating only useful neighbors rather than all $\binom{n}{2}$ swaps from every state.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "ab", "s2": "ba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Always focus on the first mismatch

Helper `next(s)` finds the smallest index `i` for which `s[i] != s2[i]`.

Every earlier position already matches the target. The neighbor generation never touches those positions, so the correct prefix grows monotonically and is never damaged.

If `s != s2`, an anagram must contain the needed character `s2[i]` somewhere after `i`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Helper `next(s)` finds the smallest index `i` for which `s[i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose a swap partner that fixes index `i`

For each `j > i`, the source requires:

- `s[j] == s2[i]`, so moving `s[j]` to `i` fixes the first mismatch;
- `s[j] != s2[j]`, so position `j` is currently wrong and the swap does not destroy a correct target character there.

Only such positions generate neighbors.

This pruning makes every produced swap increase the length of the matching prefix by at least one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "ab", "s2": "ba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate every possible swap:** BFS remains co:** - **Generate every possible swap:** BFS remains correct but branches into many swaps that do not improve the first mismatch.
- **- **Depth-first search with branch-and-bound:** It:** - **Depth-first search with branch-and-bound:** It can find good solutions but needs careful lower bounds to prove minimality. BFS gives shortest swap count directly.
- **- **A* search:** A mismatch-based heuristic can re:** - **A* search:** A mismatch-based heuristic can reduce explored states, but adds priority-queue and admissibility reasoning.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2P)$. Let `n` be string length and `P` be the number of distinct states reached by the pruned BFS.
- **Auxiliary Space Complexity:** $O(nP)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
