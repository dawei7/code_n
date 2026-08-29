# Guided Example: Distinct Echo Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "abcabcabc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Return the number of **distinct** non-empty substrings of `text` that can be written as the concatenation of some string with itself (i.e. it can be written as $a + a$ where `a` is some string).

The objective is to compute `3` from `{"text": "abcabcabc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building powers and prefix hashes

Each lowercase character is converted to an integer from one through 26. With base 131, a string behaves like a number whose digits are those character values.

`h[i + 1]` is the polynomial hash of the prefix ending at original index `i`. `p[i + 1]` stores $131^{i+1}$ modulo `mod`.

The update

`h[i + 1] = (h[i] * base) % mod + t`

shifts the previous polynomial by one base position and adds the new character. The final addition is not reduced immediately, so `h` can temporarily be slightly larger than `mod`, but it remains congruent to the intended modular hash. The later arithmetic and next multiplication apply modulo, so hash comparisons still use the same residue class.

Arrays have `n + 10` slots, more than the needed `n + 1`. The extra constant padding is harmless.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "abcabcabc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extracting any substring hash

`get(l, r)` uses one-based inclusive positions. The prefix `h[r]` contains everything through `r`. Multiplying `h[l - 1]` by `p[r - l + 1]` aligns the earlier prefix with that same polynomial degree. Subtracting cancels all characters before `l`:

`(h[r] - h[l - 1] * p[r - l + 1]) % mod`.

Python's modulo returns a nonnegative residue, so equal substrings receive equal returned hashes even when the raw subtraction is negative.

After preprocessing, `get` performs constant-time array access and arithmetic instead of comparing every character in a candidate half.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerating only even lengths

`i` is the original zero-based start. The end `j` begins at `i + 1` and advances by two:

`range(i + 1, n, 2)`.

Therefore, `j - i` is odd, and the inclusive substring length `j - i + 1` is even. No odd-length substring is examined because it cannot be split into two equal-length halves.

The midpoint `k = (i + j) >> 1` is the last original index of the first half. The halves are:

- original indices `i` through `k`, hashed by `get(i + 1, k + 1)`; and
- original indices `k + 1` through `j`, hashed by `get(k + 2, j + 1)`.

Both one-based conversions add one to each original endpoint. The second half begins one original position after `k`, hence `k + 2` in the hash coordinate system.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "abcabcabc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct half comparison:** Compare slices or characters for every candidate. It is deterministic but can take $O(n^3)$ time because each of $O(n^2)$ candidates may compare $O(n)$ characters.
- **Double rolling hash:** Two independent moduli make collisions vastly less likely while retaining $O(n^2)$ expected time, but do not provide absolute collision freedom.
- **Suffix array or suffix LCP structure:** Deterministic longest-common-prefix queries can compare halves efficiently after heavier preprocessing.
- **Store actual echo substrings:** It avoids hash-based distinctness collisions but slicing and hashing full strings can increase total time and memory.
- **Length one text:** No even nonempty candidate exists, both loops add nothing, and the answer is zero.
- **Length two text:** The only candidate compares its two characters and counts one only when they match.
- **Overlapping occurrences:** Each interval is tested, and equal text across overlapping positions is deduplicated by the set.
- **Same half at different lengths is impossible:** A string's content determines its length, so identical half text also has identical length and defines the same echo.
- **One-based hash coordinates:** Every original endpoint must be shifted by one; the second half's start uses `k + 2`.
- **Modulo subtraction:** Applying `% mod` normalizes negative raw differences.
- **Hash collision:** The exact source has a probabilistic correctness caveat that should not be omitted from an expert explanation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the text length. Prefix preprocessing takes $O(n)$ time and space.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
