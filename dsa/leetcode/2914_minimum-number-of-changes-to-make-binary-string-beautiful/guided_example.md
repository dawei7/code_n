# Guided Example: Minimum Number of Changes to Make Binary String Beautiful

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1001"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** binary string `s` having an even length.

The objective is to compute `2` from `{"s": "1001"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why every beautiful string must have equal fixed pairs

Assume the string already has a valid beautiful partition. Each part has even length. Starting from index $0$, the first part therefore ends after an even number of characters, so its boundary lies between two fixed pairs rather than through the middle of one. The same is true for every later part because a sum of even lengths is even.

Consequently, no fixed pair $(0,1),(2,3),\ldots$ is split between two parts. Both of its characters lie inside the same homogeneous part, and all characters in that part are identical. The two characters in every fixed pair must therefore be equal.

This proves necessity. If even one pair is `01` or `10` after all changes, no choice of valid even-length boundaries can hide that mismatch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1001"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why equal fixed pairs are sufficient

Now assume every fixed pair contains equal characters. We can use each pair itself as one substring in the partition. Every such substring:

- has length $2$, which is even;
- is either `00` or `11`, so it contains only one character.

Thus the list of pairs is already a valid beautiful partition. Adjacent equal pairs could optionally be merged into a longer homogeneous even part, but merging is not needed to prove validity.

This direction is what removes all boundary-search complexity. We do not need to discover the original statement's larger substrings. Length-two pieces always supply a valid partition whenever the pair condition holds.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimize each pair independently

Consider one fixed pair.

- If its bits are equal, it already meets the condition and costs zero changes.
- If its bits differ, any beautiful final string must make them equal, so at least one of those two positions must change.
- Flipping either bit makes a differing binary pair equal, so one change is also sufficient.

Therefore the exact minimum cost of a pair is $0$ when equal and $1$ when different. The pairs are disjoint, so changing a bit in one pair cannot repair or damage another pair. Their independent minimum costs can simply be added.

This is both a lower-bound and construction argument. Every mismatching pair forces at least one change, so no solution can use fewer changes than the mismatch count. Changing one bit in every mismatching pair makes all pairs equal, which creates a valid partition and achieves exactly that count. Hence the count is globally minimal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1001"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over partition boundaries:** One could test even-length homogeneous suffixes and compute a minimum over prefixes, but the fixed-pair equivalence makes all boundary choices irrelevant. That approach adds time and state without changing the answer.
- **Greedily build maximal runs:** Counting odd-length runs can be made to work with careful reasoning, but run boundaries shift after changes and are easier to mishandle. Disjoint fixed pairs give independent, exact costs.
- **Try all possible beautiful strings:** Enumerating repairs is exponential. Each pair has an immediate local lower bound and construction, so enumeration has no value.
- **Already beautiful with several parts:** A string such as `001100` returns zero even though it is not all one character. Each pair is homogeneous, which is sufficient for a valid partition.
- **A long homogeneous run:** Any even-length run divides into equal pairs and needs no change. The method does not need to identify the run explicitly.
- **A mismatch at the beginning or end:** The odd-index range compares both endpoint pairs normally; no special boundary branch is needed.
- **Even length guarantee:** Because $n$ is even, the final character always has a partner. Without that guarantee, an unpaired final character could not itself form an even-length part and would require separate impossibility handling.
- **Changing both bits of a mismatching pair:** This is never better than changing one. One change already makes the two characters equal, so a second change only wastes an operation.
- **Merging repaired pairs:** It is unnecessary for correctness. Once every pair is homogeneous, treating pairs as separate length-two substrings already satisfies the definition.
- **Boolean arithmetic:** The source relies on Python's `bool` being a subclass of `int`. In a language without numeric Booleans, the comparison should be converted explicitly to $0$ or $1$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
