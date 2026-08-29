# Guided Example: Number of Distinct Substrings in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabbaba"}`
- **Required output:** `21`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the number of **distinct** substrings of* `s`.

The objective is to compute `21` from `{"s": "aabbaba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “substring” into two boundaries

A nonempty substring is completely determined by a start index `i` and an exclusive end index `j` satisfying

$$
0 \le i < j \le n.
$$

In Python, `s[i:j]` contains the characters from `i` through `j - 1`. For a fixed `i`, allowing `j` to range from `i + 1` through `n` therefore generates every nonempty substring that starts at `i`: first the one-character substring, then the two-character substring, and so on through the suffix ending at the last character.

The exact source expresses these two ranges in one set comprehension:

`{s[i:j] for i in range(n) for j in range(i + 1, n + 1)}`.

The outer range chooses every possible start. The inner range chooses every valid nonempty end for that start. Because the end is exclusive, `n + 1` is passed to `range` so that `j = n` is included. Starting the inner range at `i + 1` deliberately excludes `s[i:i]`, the empty string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabbaba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Let a set perform the deduplication

Different boundary pairs can spell the same text. In `"aaa"`, for example, `s[0:1]`, `s[1:2]`, and `s[2:3]` are three occurrences but all produce the value `"a"`. A Python set stores only one entry for equal string values, so the comprehension automatically converts the collection of occurrences into the collection of distinct substring texts.

This distinction is the heart of the problem. The number of boundary pairs is always $n(n+1)/2$, but the answer can be smaller when repeated content causes several pairs to generate the same value. The source does not count pairs and then attempt to subtract duplicates. It materializes all values, lets hash-based set membership merge equal strings, and returns the final cardinality with `len(...)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every valid substring appears

Take any nonempty substring of `s`. By definition, it occupies some consecutive interval beginning at index `i` and ending at an inclusive index `r`. Choose `j = r + 1`. Then `i` occurs in `range(n)`, `j` lies between `i + 1` and `n`, and the comprehension generates exactly `s[i:j]`. Therefore no valid nonempty substring is absent.

Conversely, every value the comprehension generates uses a start in `[0, n - 1]` and an exclusive end in `[i + 1, n]`. Its characters are consecutive, it contains at least one character, and it stays inside the string. Thus the comprehension cannot introduce a value that is not a valid nonempty substring.

Finally, set equality is based on the characters and their order, not on the originating indices. Each distinct text remains exactly once. The length of the set is consequently exactly the requested count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `21` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabbaba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `21` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Suffix automaton:** Build automaton states for all substring end-position classes. The sum of `len[state] - len[link[state]]` over noninitial states counts distinct substrings in $O(n)$ time and $O(n)$ space, matching the follow-up and manifest, but it is substantially harder to derive and implement.
- **Suffix array with longest common prefixes:** The total possible substrings minus the sum of adjacent suffix LCP values gives the distinct count. Typical implementations take $O(n\log n)$ time and $O(n)$ space.
- **Trie of all suffixes:** Insert every suffix and count newly created nodes. It makes shared prefixes explicit but takes $O(n^2)$ time and space in the worst case.
- **Rolling hashes:** Store hashes rather than full substring strings, potentially reducing copied content, but collision handling is necessary for exact correctness and there are still $\Theta(n^2)$ candidates.
- **One character:** The only generated pair is `i = 0, j = 1`, so the answer is one.
- **All characters equal:** The distinct values are one substring for each possible length, so the answer is $n$ even though there are $n(n+1)/2$ occurrences.
- **Many distinct substrings:** The set approaches quadratic entry count and cubic total stored character volume, exposing the source's worst-case resource use.
- **Empty substring:** It is correctly excluded because `j` always starts at `i + 1`.
- **Whole string:** It is included by `i = 0` and `j = n`.
- **Equal text at different positions:** Set semantics merge it regardless of where each occurrence begins.
- **Lowercase alphabet:** The algorithm does not rely on the alphabet size; it would behave identically for any hashable Python string characters.
- **Off-by-one at the end:** The inner upper bound must be `n + 1` because Python's `range` omits its stop and slicing omits the end index.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. There are $\Theta(n^2)$ nonempty substring occurrences. Creating and hashing `s[i:j]` costs $\Theta(j-i)$ for that slice. Summed across every pair of boundaries, the total number of copied characters is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
