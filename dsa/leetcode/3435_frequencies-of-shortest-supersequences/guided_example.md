# Guided Example: Frequencies of Shortest Supersequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["ab", "ba"]}`
- **Required output:** `[[2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `words`. Find all **shortest common supersequences (SCS)** of `words` that are not permutations of each other.

The objective is to compute `[[2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]` from `{"words": ["ab", "ba"]}` while avoiding redundant calculations and unnecessary overhead.

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

**Translate every two-letter word into an ordering edge.** If word `"uv"` must be a subsequence, some occurrence of `u` must appear before some occurrence of `v` in the common supersequence. The source collects the at most $16$ distinct letters, maps them to compact vertices, and records edge $u\to v$ in the bit mask `outgoing[u]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["ab", "ba"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Every used letter must appear at least once. Some letters may need a second occurrence to satisfy cyclic ordering requirements. A frequency vector is therefore determined by the subset of letters used twice: ordinary vertices have frequency one, doubled vertices frequency two, and unused alphabet letters frequency zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why cycles force doubled letters.** Suppose a set of letters each appears only once. Their positions in any string define a strict linear order. All graph edges between those single-occurrence letters must point forward in that order, so their induced directed graph must be acyclic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["ab", "ba"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate supersequence strings:** Even at small alphabet size, ordering and repeated-letter choices create enormous duplication. Frequency subsets avoid permutations entirely.
- **Topological sort without doubling:** It works only when the original graph is already acyclic. Cycles require repeated letters.
- **Double every cycle vertex:** That is sufficient but not shortest. The enumeration finds minimum feedback vertex sets.
- **Self-loop:** A word with two equal letters requires two copies, and its graph self-loop forces that vertex into every valid doubled subset.
- **Acyclic graph:** The empty doubled subset succeeds first, so every used letter receives frequency one.
- **Multiple edges:** Bitwise OR deduplicates identical ordering edges without changing feasibility.
- **Disconnected components:** Kahn's algorithm processes all zero-indegree components; doubled choices are needed only to hit cycles.
- **Several minimum subsets:** All are collected before returning, producing all non-permutation-equivalent shortest frequencies.
- **Alphabet letters absent from words:** Their frequency remains zero in every length-26 result.
- **Construction sufficiency:** Early and late copies of doubled letters satisfy edges crossing the removed set, while the remaining DAG's topological order satisfies every single-to-single edge.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W+2^C C^2)$. Let $C\le16$ be the number of distinct letters and $W$ the total input characters. Building letters and edges costs $O(W)$. Across all subset sizes, at most $2^C$ doubled subsets are tested. Rebuilding indegrees and performing topological processing costs $O(C^2)$ per subset in the dense worst case. Total time is $O(W+2^C C^2)$.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
