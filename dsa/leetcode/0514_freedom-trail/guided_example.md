# Guided Example: Freedom Trail

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ring": "godding", "key": "gd"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In the video game Fallout 4, the quest **"Road to Freedom"** requires players to reach a metal dial called the **"Freedom Trail Ring"** and use the dial to spell a specific keyword to open the door.

The objective is to compute `4` from `{"ring": "godding", "key": "gd"}` while avoiding redundant calculations and unnecessary overhead.

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

The same key character may appear at several positions on the ring. Choosing the nearest occurrence now is not always globally optimal because the chosen position becomes the starting alignment for the next character. Dynamic programming preserves every relevant ending position instead of making a premature greedy choice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ring": "godding", "key": "gd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Let `n = len(ring)` and `m = len(key)`. The dictionary `pos` maps each character to all ring indices where it appears. This avoids scanning every ring cell when processing one key character; only matching alignments can be valid states.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Circular rotation distance.** Between ring indices `j` and `k`, direct movement along one direction has length `abs(j - k)`. Going the other way around the circular ring has length `n - abs(j - k)`. The minimum rotation steps are therefore

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ring": "godding", "key": "gd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy nearest occurrence:** It can choose a locally short rotation that leaves the ring poorly aligned for later key characters. DP is needed for global optimality.
- **Top-down memoization:** Cache states `(key_index, ring_index)` and recursively try matching occurrences. It expresses the same recurrence.
- **Space-compressed DP:** Retain only the preceding row because each transition depends only on `i - 1`. This achieves $O(R)$ table space.
- **Shortest-path formulation:** Treat `(key progress, ring position)` as graph states and use a priority queue. It can avoid some dense transitions but adds graph machinery.
- **Repeated current character:** Staying at the same ring occurrence costs zero rotation but still costs one button press.
- **Wraparound:** Always compare direct distance with `R - direct_distance`.
- **First ring character already matches:** Initialization charges zero rotation plus exactly one press.
- **Several final occurrences:** The answer must minimize across all of them rather than assume the first position list entry.
- **Guaranteed spellability:** Every key character has at least one ring occurrence, so no unreachable-key branch is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(KR^2)$. Let $R = len(ring)$ and $K = len(key)$. For each adjacent key-character pair, the exact source tries every occurrence of the current character against every occurrence of the previous character. In the worst case, both characters occur at all $R$ positions, so one row costs $O(R^2)$ and total time is $O(KR^2)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
