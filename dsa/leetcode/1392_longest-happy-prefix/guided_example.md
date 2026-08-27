# Guided Example: Longest Happy Prefix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "level"}`
- **Required output:** `"l"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A string is called a **happy prefix** if it is a **non-empty** prefix which is also a suffix (excluding itself).

The objective is to compute `"l"` from `{"s": "level"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare candidate prefix and suffix lengths from longest to shortest

A happy prefix must be a proper prefix: it begins at index zero but cannot equal the entire string. It must also equal a suffix ending at the final character.

For an offset `i` between one and `len(s) - 1`:

- `s[:-i]` removes the last $i$ characters and is a prefix of length $n-i$.
- `s[i:]` removes the first $i$ characters and is a suffix of the same length $n-i$.

The equality test `s[:-i] == s[i:]` therefore asks whether the prefix and suffix of length $n-i$ are identical.

The loop tries `i = 1` first, which corresponds to the longest possible proper prefix length $n-1$. Increasing `i` shortens both candidates one character at a time. Consequently, the first equality found is automatically the longest happy prefix, and returning `s[i:]` is correct.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "level"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the slices have equal length

This detail prevents an off-by-one mistake. `s[:-i]` contains positions zero through $n-i-1$, a total of $n-i$ characters. `s[i:]` contains positions $i$ through $n-1$, also $n-i$ characters. They may overlap in the original string, which the problem explicitly allows.

For `"ababab"` with $n=6$:

- At `i=1`, `"ababa"` and `"babab"` differ.
- At `i=2`, `"abab"` and `"abab"` match.

The method immediately returns `"abab"`. It never reaches shorter matches such as `"ab"` because the first one is already longest.

For `"level"`, offsets one through three fail. At `i=4`, the one-character prefix and suffix are both `"l"`, so it returns `"l"`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This detail prevents an off-by-one mistake.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the entire string is excluded

The range begins at one rather than zero. An offset of zero would compare the whole string with itself, but the definition says the happy prefix must exclude the string itself. Every tested candidate has length at most $n-1$ and is therefore proper.

The range stops before `len(s)`. At offset $n$, both slices would be empty. A happy prefix must be nonempty, so that candidate must not be accepted. `range(1, len(s))` enforces both boundaries exactly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"l"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "level"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"l"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **KMP prefix function:** Compute the longest pro:** - **KMP prefix function:** Compute the longest proper border length in one pass and return the prefix of that length. This achieves the manifest's $O(n)$ time and $O(n)$ space.
- **Rolling hash:** Compare prefix and suffix hashes for each length, often in $O(n)$ preprocessing and constant expected comparison time, but hash collisions require care.
- **Z-function:** A linear string-matching table can identify suffixes that match the prefix and select the longest proper one.
- **Single character:** The loop is empty because no nonempty proper prefix exists, so it returns `""`.
- **All characters equal:** The first candidate of length $n-1$ matches and is returned.
- **No matching border:** Every candidate fails and the empty string is returned.
- **Overlapping occurrences:** They are valid and handled naturally by slicing.
- **Proper-prefix boundary:** Starting the offset at one prevents returning the entire string.
- **Nonempty boundary:** Stopping before offset $n$ prevents accepting two empty slices.
- **First match:** Candidate lengths decrease monotonically, so returning immediately cannot miss a longer result.
- **Unicode or lowercase:** The method works for arbitrary Python strings, though the contract supplies lowercase English letters.
- **Input immutability:** String slicing creates new strings and never changes `s`.
- **Performance constraint:** The direct method is pedagogically simple but can be too slow at the maximum length; prefix-function matching is the practical optimal replacement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. The exact implementation may test $n-1$ offsets. At offset $i$, Python constructs two slices of length $n-i$, and comparing them may also examine $O(n-i)$ characters. In a worst case with many long near-matches, total work is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
