# Guided Example: Match Substring After Replacement

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "fool3e7bar", "sub": "leet", "mappings": [["e", "3"], ["t", "7"], ["t", "8"]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `sub`. You are also given a 2D character array `mappings` where $\text{mappings}[i] = [\text{old}_{i}, \text{new}_{i}]$ indicates that you may perform the following operation **any** number of times:

The objective is to compute `true` from `{"s": "fool3e7bar", "sub": "leet", "mappings": [["e", "3"], ["t", "7"], ["t", "8"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store replacement permission in the forward direction

Each mapping `[old,new]` permits one character of `sub` equal to `old` to become `new`. The dictionary of sets stores `new` inside `d[old]`.

Sets remove duplicate mapping pairs and provide expected constant-time membership checks. Direction is essential: permission from `o` to `0` does not imply permission from `0` to `o`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "fool3e7bar", "sub": "leet", "mappings": [["e", "3"], ["t", "7"], ["t", "8"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test every possible alignment

A matching result must occupy a contiguous substring of `s` with length `len(sub)`. If `S=len(s)` and `P=len(sub)`, its start can be zero through `S-P`.

`range(len(s)-len(sub)+1)` enumerates exactly these alignments, including the final one ending at the last character.

For each start `i`, the slice `s[i:i+len(sub)]` extracts the candidate text.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compare aligned characters

`zip(candidate, sub)` yields `a` from `s` and `b` from `sub` at the same relative position.

That position is compatible when either `a==b`, requiring no replacement, or `a in d[b]`, meaning the original sub character `b` may be replaced directly by target character `a`.

The orientation `a in d[b]` matches old-to-new semantics. Reversing the lookup would incorrectly permit mappings backward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "fool3e7bar", "sub": "leet", "mappings": [["e", "3"], ["t", "7"], ["t", "8"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Avoid window slicing:** Compare `s[i+j]` directly to reduce temporary space while keeping the same time bound.
- **Boolean character matrix:** The fixed alphanumeric alphabet permits constant-size direct lookup instead of sets.
- **Transitive closure:** It would incorrectly allow more than one replacement per character.
- **Regular expressions:** Per-character directed mappings are possible to encode but less transparent.
- **No mappings:** Only exact substring matches pass.
- **Exact character:** Equality succeeds without consulting mappings.
- **Repeated use of one mapping:** Different positions may each apply the same allowed replacement.
- **Reverse-only mapping:** It does not authorize the forward comparison.
- **Equal string lengths:** There is exactly one alignment.
- **Final alignment:** The `+1` in the range includes it.
- **Case sensitivity:** Uppercase and lowercase are distinct.
- **Early mismatch:** `all` short-circuits safely.
- **Input preservation:** No input string or mapping row is modified.
- **Bare direct replacement:** A mapping may be used even when the same old character appears several times; the “once” restriction is per character occurrence, not per mapping rule.
- **Unused mappings:** Rules unrelated to characters in `sub` simply remain in the dictionary and never affect a comparison.
- **Duplicate mapping rows:** Set insertion collapses them without changing permission.
- **Digit characters:** They are ordinary mapping keys and values, not converted to numbers.
- **Substring contiguity:** Testing fixed-length slices prevents a subsequence-style match with gaps.
- **Short-circuit success:** The first passing alignment proves existence, so later starts need not be tested.
- **Mismatching lengths:** Every candidate slice has exactly `len(sub)` characters, making `zip` cover all required positions.
- **Default dictionary access:** Looking up an unmapped old character creates an empty set in this `defaultdict`, which makes the membership test false.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `S=len(s)`, `P=len(sub)`, and `R` be the number of mappings. Building sets takes expected `O(R)` time and `O(R)` space.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
