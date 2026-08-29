# Guided Example: Count Prefix and Suffix Pairs I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["a", "aba", "ababa", "aa"]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string array `words`.

The objective is to compute `4` from `{"words": ["a", "aba", "ababa", "aa"]}` while avoiding redundant calculations and unnecessary overhead.

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

**Test exactly the index pairs the statement permits.** A pair $(i,j)$ is eligible only when $i<j$. The outer loop selects `words[i]` as the candidate smaller word `s`. The inner loop visits `words[i + 1:]`, so every later index $j$ is tested once and no reversed or self-pair is included.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["a", "aba", "ababa", "aa"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For each later word `t`, the condition is written directly:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Both sides must be true. A prefix match alone is insufficient, and a suffix match alone is insufficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["a", "aba", "ababa", "aa"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index-based nested loops:** It implements the same comparisons without suffix-list allocation and would meet $O(1)$ auxiliary space.
- **Paired-character trie:** The larger version uses one to process total input length efficiently, but it is unnecessary for these small limits.
- **Compare string slices manually:** Built-in prefix and suffix predicates are clearer and avoid creating substring objects.
- **Candidate longer than target:** The built-ins return false without special handling.
- **Equal words at different indices:** The candidate is both full prefix and full suffix, so the pair counts.
- **One-character candidate:** It counts when the target's first and last characters both match it.
- **Overlapping prefix and suffix:** Overlap is allowed and handled naturally.
- **Repeated words:** Indices define pairs, so identical content at several positions can produce multiple counts.
- **One-word array:** There are no later words and the answer is zero.
- **Order constraint:** A matching later word can pair with an earlier candidate, but the reverse index order is never counted.
- **Manifest mismatch:** The exact slicing implementation has $O(N)$ peak auxiliary space despite the constant-space high-level idea.
- **Suffix checked before prefix:** Short-circuit order affects only performance, not correctness. A target that fails its suffix test contributes false immediately; a target that passes still undergoes the required independent prefix test.
- **Character-comparison worst case:** Long repeated strings can make both built-ins inspect nearly all candidate characters for many pairs. That is why the length factor remains in the worst-case bound even though mismatches often terminate early.
- **Indices rather than distinct contents:** If the same candidate text occurs at two earlier positions and both qualify against one later word, they form two different $(i,j)$ pairs. Pair enumeration naturally counts both.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2L)$. Let $N$ be the number of words and $L$ the maximum word length. There are $N(N-1)/2=O(N^2)$ index pairs. `startswith` and `endswith` can each compare up to $O(L)$ characters, so worst-case time is $O(N^2L)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
