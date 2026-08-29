# Guided Example: Find Maximum Removals From Source String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"source": "abbaa", "pattern": "aba", "targetIndices": [0, 1, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `source` of size `n`, a string `pattern` that is a subsequence of `source`, and a **sorted** integer array `targetIndices` that contains **distinct** numbers in the range `[0, n - 1]`.

The objective is to compute `1` from `{"source": "abbaa", "pattern": "aba", "targetIndices": [0, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**Choose a subsequence embedding and remove every eligible unused position.** The pattern must remain a subsequence after removals. Any source position used to realize that subsequence must be kept. Any target position not used by the chosen embedding can be removed, while non-target positions may remain unused without counting as operations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"source": "abbaa", "pattern": "aba", "targetIndices": [0, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Thus the task is to choose a pattern embedding that maximizes how many `targetIndices` positions are skipped. The exact source models this directly rather than first minimizing kept target positions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Let $S=\lvert\texttt{source}\rvert$ and $P=\lvert\texttt{pattern}\rvert$. State `f[i][j]` is the maximum number of removable target positions among the first $i$ source characters while embedding the first $j$ pattern characters. Impossible states carry negative infinity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"source": "abbaa", "pattern": "aba", "targetIndices": [0, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-row compression:** Every transition reads only row `i-1`, so retaining previous and current arrays reduces DP space to $O(P)$ without changing $O(SP)$ time.
- **One-row dynamic programming:** Update pattern positions in descending order while carefully incorporating skip rewards. It can reduce storage further but is easier to implement incorrectly.
- **Minimize kept target positions:** Compute the minimum number of eligible indices used by an embedding, then subtract from `len(targetIndices)`. This is algebraically equivalent to the source's direct maximization.
- **Greedy earliest subsequence:** It may consume removable indices unnecessarily; a later embedding can allow more operations, so DP is required.
- **Pattern equals source:** Every source position is required in the only full-length embedding, so no target position can be removed.
- **Target index not used by pattern:** The skip transition gains one, even if the character remains conceptually irrelevant after other removals.
- **Non-target index not used:** It earns zero but may stay in the source without harming subsequence validity.
- **Repeated characters:** Multiple embedding choices are exactly why states compare skip and take rather than greedily choosing the first match.
- **All target indices removable:** If the pattern can be embedded entirely in non-target positions, the answer is `len(targetIndices)`.
- **Stable original indices:** Set membership is checked against the original scan index, consistent with the contract that operations do not renumber later characters.
- **Impossible states:** Negative infinity prevents a path that has not embedded enough pattern characters from competing with a legal plan.
- **Pattern guarantee:** Because an embedding exists initially, the final state is finite even if zero removals are possible.
- **Manifest discrepancy:** The exact two-dimensional allocation is $O(SP)$ space; only a compressed variant would meet the listed linear-space claim.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(SP+T)$. The nested loops visit every one of the $(S+1)(P+1)$ states, performing expected constant-time set membership and a constant number of arithmetic/comparison operations. Building the target set costs $O(T)$ for $T=\lvert\texttt{targetIndices}\rvert$. Total expected time is $O(SP+T)=O(SP)$.
- **Auxiliary Space Complexity:** $O(SP+S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
