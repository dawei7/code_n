# Guided Example: Find the Shortest Superstring II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "aba", "s2": "bab"}`
- **Required output:** `"abab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given **two** strings, `s1` and `s2`. Return the **shortest** *possible* string that contains both `s1` and `s2` as substrings. If there are multiple valid answers, return *any *one of them.

The objective is to compute `"abab"` from `{"s1": "aba", "s2": "bab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize so s1 is not longer

The source first compares lengths. If `len(s1) > len(s2)`, it recursively calls the same method with arguments swapped.

After at most one swap, `m = len(s1) <= n = len(s2)`. This simplifies containment: only the shorter string `s1` can fit entirely inside the longer `s2`. If lengths are equal and one contains the other, they must be identical.

The recursive swap cannot continue indefinitely because the swapped pair satisfies the length order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "aba", "s2": "bab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Containment is always the best case

If `s1 in s2`, returning `s2` is optimal. Any result containing `s2` must have length at least `n`, and `s2` itself already contains both strings.

This check also handles identical strings and appearances of `s1` in the middle of `s2`. Boundary-overlap checks alone would miss middle containment.

After containment fails, a shortest result must include characters unique to both strings and therefore combines them at a boundary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scanning overlap sizes from largest to smallest

The loop index `i` ranges from zero through `m-1`. The candidate overlap length is `m-i`. As `i` increases, overlap length decreases:

`m, m-1, ..., 1`.

Full overlap length `m` at `i=0` cannot succeed after containment unless the strings have a special equal-boundary relation that would itself imply containment, but checking it is harmless.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "aba", "s2": "bab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **KMP prefix functions:** Combining strings with a delimiter and computing prefix functions can find each maximum boundary overlap in linear time. This would realize the manifest summary, but it is not the current source.
- **Z algorithm:** Z-values on appropriate concatenations also find containment and maximum overlaps in `O(m+n)` time.
- **Try every merged string:** Brute-force alignment across both directions is similar in spirit to the source but can be expressed more explicitly; boundary overlap checks are the compact version.
- **One string contained in the other:** Return the containing string immediately, including middle containment.
- **Equal strings:** The containment test returns either identical string.
- **Original s1 longer:** One recursive swap normalizes the order without changing the symmetric problem.
- **Overlap in both directions:** The loop compares equal overlap lengths at the same `i`. Either result is allowed when lengths tie.
- **No overlap:** Direct concatenation is shortest and the chosen order is permitted.
- **One-character strings:** Equality is handled by containment; different characters have no overlap and concatenate.
- **Repeated-character patterns:** They can make naive substring/overlap comparisons approach their worst case, which is why the source cannot claim KMP’s linear guarantee.
- **Lexicographic order:** The problem asks only for minimum length, not the lexicographically smallest among ties, so returning the first equal-length candidate is correct.
- **Lowercase alphabet:** No delimiter concerns arise in the current scanning method. A KMP concatenation would need a separator outside the lowercase alphabet.
- **Substring versus subsequence:** Containment and overlaps require contiguous equality; the Python operations used enforce exactly that.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m + n)$. Let `m \le n` after normalization.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
