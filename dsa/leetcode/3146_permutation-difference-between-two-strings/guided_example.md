# Guided Example: Permutation Difference between Two Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc", "t": "bac"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t` such that every character occurs at most once in `s` and `t` is a permutation of `s`.

The objective is to compute `2` from `{"s": "abc", "t": "bac"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert repeated position searches into one lookup table

The permutation difference asks for one term per character:

$$
\left|\operatorname{pos}_s(c)-\operatorname{pos}_t(c)\right|.
$$

The strings contain the same distinct characters, only in different orders. Therefore, every character has exactly one position in each string.

The dictionary comprehension

`d = {c: i for i, c in enumerate(s)}`

records the unique index of every character in `s`. After this pass, `d[c]` answers “where was character `c` in `s`?” in expected constant time.

The generator then enumerates `t`. For each pair `(i, c)`, index `i` is the position of `c` in `t`, while `d[c]` is its position in `s`. The absolute value `abs(d[c] - i)` is exactly that character's contribution. `sum` combines all contributions.

The manifest summary describes indexing the second string and scanning the first. The exact code does the symmetric version: it indexes `s` and scans `t`. Because absolute difference is symmetric and both strings contain the same character set, either direction produces the same result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc", "t": "bac"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why characters can be handled independently

The definition does not ask how many swaps transform one permutation into the other. It simply sums each character's displacement. Moving one character conceptually does not change the index term assigned to any other character because both positions come from the original strings.

This means no simulation is required. Once the two original positions of a character are known, its contribution is fixed and can be added independently.

For `s = "abc"` and `t = "bac"`:

- `a` is at indices 0 and 1, contributing 1;
- `b` is at indices 1 and 0, contributing 1;
- `c` is at indices 2 and 2, contributing 0.

The sum is 2.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the dictionary has exactly the needed information

Since every character occurs at most once in `s`, assigning `d[c] = i` cannot overwrite an earlier position for the same character. Since `t` is a permutation of `s`, every scanned character is guaranteed to be a key in `d`. There is no missing-key case and no need to store lists of positions.

Likewise, each key is encountered exactly once while scanning `t`, so every character contributes once. No character is omitted or counted twice.


After the dictionary comprehension, for every character $c$ in the strings, `d[c]` equals $\operatorname{pos}_s(c)$ by construction.

During enumeration of `t`, the loop index $i$ equals $\operatorname{pos}_t(c)$. Thus each generated term is

$$
\left|\operatorname{pos}_s(c)-\operatorname{pos}_t(c)\right|,
$$

the term specified by the problem. Because `t` contains every character exactly once, the generator produces the complete set of required terms exactly once. Summing them returns the permutation difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc", "t": "bac"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index t and scan s:** This is the manifest's orientation and is mathematically identical because absolute differences are symmetric.
- **Call `str.index` for every character:** It avoids a dictionary but scans a string repeatedly, producing $O(n^2)$ time.
- **Fixed 26-entry array:** Store positions by `ord(c) - ord('a')`. It uses constant alphabet-bounded storage and deterministic lookup.
- **Sort position pairs:** Unnecessary because characters themselves give the correspondence between the two permutations.
- **Single character:** Both positions are zero, so the answer is zero.
- **Identical strings:** Every displacement is zero.
- **Reverse order:** Characters near the ends have large displacements; the same direct sum still applies.
- **No duplicate characters:** This guarantee is essential for a single position per dictionary key. With duplicates, occurrences would require matching rules or position lists.
- **Permutation guarantee:** It ensures every `t` character exists in `d` and both strings have equal length.
- **Signed displacement:** The problem uses absolute distance, so left and right movement are not allowed to cancel.
- **Input preservation:** Neither string is modified.
- **Dictionary ordering:** The algorithm never relies on dictionary iteration order; it performs key lookups while scanning `t`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
