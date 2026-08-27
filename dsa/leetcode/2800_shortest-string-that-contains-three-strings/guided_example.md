# Guided Example: Shortest String That Contains Three Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": "abc", "b": "bca", "c": "aaa"}`
- **Required output:** `"aaabca"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given three strings `a`, `b`, and `c`, your task is to find a string that has the** minimum** length and contains all three strings as **substrings**.
If there are multiple such strings, return the* ***lexicographically* *smallest **one.

The objective is to compute `"aaabca"` from `{"a": "abc", "b": "bca", "c": "aaa"}` while avoiding redundant calculations and unnecessary overhead.

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

**The goal has two levels.** The returned string must contain `a`, `b`, and `c` as substrings. Among all such strings, it must first have minimum length. If several minimum-length answers exist, it must be lexicographically smallest. The algorithm handles this by trying every order in which the three source strings might appear and selecting candidates with the pair `(length, text)` in that priority order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": "abc", "b": "bca", "c": "aaa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Merge two strings as tightly as their order permits.** The helper `f(s, t)` constructs a shortest string that contains both values while treating `s` as coming before `t` unless one is already contained in the other.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Merge two strings as tightly as their order permits.** The... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Its first two checks are containment checks. If `s in t`, returning `t` already contains both and cannot be improved because any answer containing `t` needs at least `len(t)` characters. Conversely, if `t in s`, returning `s` is optimal. These checks are essential when one input occurs in the middle of another; suffix-prefix overlap alone would not notice every such containment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aaabca"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": "abc", "b": "bca", "c": "aaa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aaabca"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bitmask shortest-superstring dynamic programmi:** - **Bitmask shortest-superstring dynamic programming:** This is the standard generalization for many strings. It tracks the best result for each subset and last string, but for exactly three inputs it adds machinery without improving the practical bound.
- **Precompute pair overlaps:** Computing all directed overlaps first can make the six-order evaluation concise. It must still account for containment and lexicographic ties carefully.
- **KMP or Z-algorithm overlaps:** These can find each maximum suffix-prefix overlap in linear time. They are useful for long strings, but the simple descending checks are clearer under the length-$100$ constraint.
- **One string contains another:** The helper returns the containing string immediately, preventing duplicated characters and allowing containment in the middle rather than only at an edge.
- **All three strings identical:** Every merge returns that same string, and the final answer is the common input.
- **No overlaps at all:** Every order has total length $L$. The candidate comparison selects the lexicographically smallest concatenation among the six orders.
- **Directional overlap:** A match from the suffix of `s` to the prefix of `t` says nothing about the reverse direction. Enumerating permutations is what handles both possibilities.
- **Equal-length candidates:** Only then is lexicographic order consulted. This preserves the primary minimum-length objective.
- **Duplicate permutations:** Repeated input strings may make several generated tuples identical. The work remains constant and the same best candidate is considered more than once harmlessly.
- **Empty strings outside the constraints:** Containment would make an empty string disappear naturally, but the problem guarantees each input has at least one character.
- **Lowercase ordering:** Python's ordinary string comparison agrees with lexicographic order for the constrained lowercase English letters.
- **Greedy choice without permutations:** Merging whichever pair has the largest immediate overlap can miss the global best arrangement. Exhausting all six orders avoids that local-choice trap at negligible cost.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the total length of the three input strings. There are only six permutations. In each helper call, containment testing can take $O(L^2)$ time in a conservative substring-search analysis. The descending overlap loop performs at most $O(L)$ iterations, and Python slicing plus string equality can inspect $O(L)$ characters per iteration, giving $O(L^2)$ time per helper call in the worst case. A constant number of calls therefore yields $O(L^2)$ total time.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
