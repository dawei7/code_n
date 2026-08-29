# Guided Example: Longest Common Suffix Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"wordsContainer": ["abcd", "bcd", "xbcd"], "wordsQuery": ["cd", "bcd", "xyz"]}`
- **Required output:** `[1, 1, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two arrays of strings `wordsContainer` and `wordsQuery`.

The objective is to compute `[1, 1, 1]` from `{"wordsContainer": ["abcd", "bcd", "xbcd"], "wordsQuery": ["cd", "bcd", "xyz"]}` while avoiding redundant calculations and unnecessary overhead.

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

**A suffix becomes a prefix after reversal.** Comparing a query with every container word would repeat the same character checks many times. A trie shares common prefixes, but this problem asks about common suffixes. The exact source gets the same benefit by reading every word from right to left. Words ending in `"bcd"` then all follow the trie path `d -> c -> b`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"wordsContainer": ["abcd", "bcd", "xbcd"], "wordsQuery": ["cd", "bcd", "xyz"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The implementation uses `w[::-1]` in each insertion and query loop. Conceptually, each trie depth represents one more character of a suffix:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- the root represents the empty suffix;
- a child at depth one represents a one-character suffix;
- a node at depth $d$ represents the exact suffix spelled by its root-to-node path in reverse-reading order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"wordsContainer": ["abcd", "bcd", "xbcd"], "wordsQuery": ["cd", "bcd", "xyz"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compare every query with every container word:** It is direct but can require $O(CQ)$-scale repeated suffix checks in unfavorable inputs.
- **Dictionary children:** Storing only existing edges can use much less memory for sparse tries, at the cost of hash lookups and dictionary overhead.
- **Sort reversed words:** Binary-searching prefix ranges is possible, but maintaining the shortest-and-earliest candidate for every query prefix is less direct.
- **No nonempty common suffix:** Traversal remains at the root and returns the globally shortest, earliest container word.
- **Query fully matched:** The deepest node reached after all query characters stores the best container word ending with the entire query.
- **Container word shorter than query:** It can still win if its whole text is the longest suffix any container supplies.
- **Equal container lengths:** Strict-length replacement preserves the first inserted, hence smallest index.
- **Duplicate container words:** They traverse identical paths; the earlier duplicate remains stored because lengths tie.
- **One-letter words:** They update both the root and one child, correctly serving empty- and one-character suffix queries.
- **All lowercase letters:** The `ord` offset and 26-child array depend on this contract.
- **Root initialization:** At least one container word is guaranteed, so the root's infinite placeholders are replaced before any query.
- **Match priority:** A deeper trie node always wins over a shallower one, even if the shallower node stores a shorter word.
- **Length priority within one node:** Only words sharing the same represented suffix compete by total word length.
- **Index priority within equal length:** Front-to-back insertion provides the tie-break implicitly.
- **Input mutation:** Container and query arrays are read only; reversed slices are temporary strings.
- **Large constant memory:** $O(C)$ hides 26 references per node. A map-based node may be preferable when memory limits are tight.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+Q)$. Let:
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
