# Guided Example: Alien Dictionary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["wrt", "wrf", "er", "ett", "rftt"]}`
- **Required output:** `"wertf"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

The objective is to compute `"wertf"` from `{"words": ["wrt", "wrf", "er", "ett", "rftt"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat letter order as a directed dependency graph

The input does not directly reveal one alphabet string. It reveals comparisons between words that are claimed to be sorted under an unknown alphabet. Each trustworthy comparison can impose a rule of the form “letter `x` must come before letter `y`.” These rules are naturally represented as a directed graph: every distinct letter appearing in the dictionary is a vertex, and an edge `x -> y` means that `x` must precede `y` in any valid alien alphabet.

Once the graph has been built, the requested alphabet is a topological ordering of its vertices—an ordering in which every edge points from an earlier letter to a later letter. If the graph has a directed cycle, no such ordering exists, because following the cycle would require a letter to come before itself. The solution then returns the empty string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["wrt", "wrf", "er", "ett", "rftt"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A word's internal letters do not create rules

Seeing a word such as `"wrt"` does not imply `w < r < t`. Lexicographic sorting compares different words, not consecutive characters inside one word. The only reliable rules come from comparing words that occupy ordered positions in the given list.

It is enough to compare adjacent words. If the entire list is sorted, every adjacent pair must be in the correct order. Conversely, if every adjacent comparison is compatible with one letter order, transitivity makes all nonadjacent pairs compatible as well. Comparing every pair would add work without providing a fundamentally different source of constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Seeing a word such as `"wrt"` does not imply `w < r < t`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Only the first differing position matters

Consider adjacent words `first` and `second`. Scan their characters from left to right. Equal characters provide no new information: both words share that prefix, so the comparison has not yet been decided. At the first index where the characters differ, suppose `first` contains `x` and `second` contains `y`. Since `first` appears earlier in the sorted dictionary, the alien alphabet must place `x` before `y`, so the graph needs edge `x -> y`.

After that first difference, later characters must be ignored. Lexicographic order has already been decided at the earliest unequal position. Adding edges from later differences would invent constraints that the dictionary does not imply and could falsely make a valid input appear inconsistent.

For example, comparing `"wrt"` with `"wrf"` gives no rule from the shared `w` and `r`; the first difference is `t` versus `f`, so it gives only `t -> f`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"wertf"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["wrt", "wrf", "er", "ett", "rftt"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"wertf"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sparse adjacency sets:** Store only actual out:** - **Sparse adjacency sets:** Store only actual outgoing neighbors and increment indegree when a set gains a new edge. This gives the manifest's $O(c+e)$ time and $O(a+e)$ space for arbitrary alphabets, but the 26-by-26 matrix is straightforward and safely deduplicates edges under the fixed contract.
- **DFS topological sort:** Three-state graph coloring can detect a back edge and append vertices after exploring their dependencies. It has the same sparse asymptotic bounds, but its cycle reasoning and reversed finishing order differ from the exact queue-based source.
- **Compare every pair of words:** Nonadjacent comparisons are unnecessary because adjacent sortedness is sufficient and graph transitivity captures implied relations. Comparing every pair increases work and complicates extraction.
- **Infer rules from characters within one word:** This is invalid. A word's spelling does not say that each character precedes the next in the alphabet; only the first mismatch between ordered words carries comparison information.
- **Longer word before its prefix:** Inputs such as `["abc", "ab"]` are impossible regardless of the letter order. They must be rejected even though no mismatching character exists.
- **Shorter prefix first:** Inputs such as `["ab", "abc"]` are valid and add no edge. Prefix order alone already explains why the shorter word comes first.
- **Repeated identical words:** They add no edge and cause no prefix failure. Their letters still become graph vertices and must appear in the result.
- **Duplicate inferred edges:** Several pairs may imply the same rule. The Boolean matrix stores it once, so indegree is incremented once and later decremented once.
- **Direct contradiction:** If both `x -> y` and `y -> x` are inferred, the source rejects immediately. This optimization is sound because no linear alphabet can satisfy both inequalities.
- **Longer directed cycle:** A cycle involving three or more letters may evade the reverse-edge shortcut. Kahn's processed-count check is the definitive cycle test and rejects it.
- **Isolated letters:** A letter with no incident edge starts with indegree zero and is still appended. Its exact location may vary, which is allowed because the evidence does not constrain it.
- **Multiple valid orders:** When several letters have indegree zero, queue order selects one valid answer. The problem does not require the lexicographically smallest ordinary-English representation.
- **Single word:** There are no adjacent comparisons, so every distinct letter in that word is isolated. The source returns them in its zero-indegree initialization order, with each distinct letter appearing once.
- **Single distinct letter:** Repeated occurrences create only one graph vertex, no self-edge, and the result is that one letter.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a+e)$. Let $c$ be the total number of characters across all words, let $a$ be the number of distinct appearing letters, and let $e$ be the number of distinct precedence edges.
- **Auxiliary Space Complexity:** $O(26^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
