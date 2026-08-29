# Guided Example: Longest Common Prefix Between Adjacent Strings After Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["jump", "run", "run", "jump", "run"]}`
- **Required output:** `[3, 0, 0, 3, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `words`. For each index `i` in the range `[0, words.length - 1]`, perform the following steps:

The objective is to compute `[3, 0, 0, 3, 3]` from `{"words": ["jump", "run", "run", "jump", "run"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Computing one LCP

`calc(s,t)` compares characters in order with `zip` and stops at the first mismatch or shorter-string end. The number of equal leading positions is their longest common prefix length.

`@cache` remembers results by the two string values. Original adjacent pairs and temporary bridge pairs are reused during remove/add restoration, so caching avoids rescanning their characters.

Because argument order is consistent for all calls, no symmetric reversed cache entry is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["jump", "run", "run", "jump", "run"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initial multiset

`pairwise(words)` produces all original adjacent pairs. Their LCP lengths initialize `SortedList sl`.

A sorted multiset, rather than a set, is necessary because several different adjacent pairs may have the same LCP length. Removing one affected pair must remove only one copy while leaving other equal scores available.

The current maximum is `sl[-1]` when the multiset is nonempty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Temporary removal update

For index `i`:

1. remove pair `(i,i+1)` if it exists;
2. remove pair `(i-1,i)` if it exists;
3. add bridge `(i-1,i+1)` if both neighbors exist.

The helper boundary checks make first, last, and single-element removals use the same code.

After these operations, `sl` contains exactly the adjacent-pair LCP values of the array with word `i` removed.

The answer is its largest value, except an empty multiset or a nonpositive maximum produces zero. LCP lengths are never negative, so the explicit positive test mainly states the output rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 0, 0, 3, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["jump", "run", "run", "jump", "run"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 0, 0, 3, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix/suffix maxima:** Precompute original pair LCPs, prefix maxima, and suffix maxima. Each removal combines unaffected maxima with one bridge in constant time, realizing `O(S+n)`.
- **Rebuild after every removal:** It costs `O(n^2)` pair work and repeats most comparisons.
- **Use a set:** Duplicate LCP scores would be collapsed, so removing one pair could incorrectly erase another pair’s maximum.
- **First word removed:** Only pair `(0,1)` disappears; no bridge exists.
- **Last word removed:** Only its left pair disappears.
- **Single word input:** No adjacent pair remains and the answer is zero.
- **Two words:** Removing either leaves one word and no pair.
- **Bridge has the maximum:** The temporary insertion lets a newly adjacent pair dominate.
- **Unchanged remote maximum:** It remains in the multiset automatically.
- **All LCPs zero:** Largest value is zero.
- **Identical strings:** LCP equals their full length.
- **Different lengths:** Zip stops at the shorter string after all shared characters.
- **Repeated word contents:** Cache keys by string values may reuse work across different positions, while multiset multiplicity still counts separate pairs.
- **Third-party dependency:** The source assumes `SortedList` is available; prefix/suffix arrays avoid that requirement.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `S` be the sum of word lengths and `n` the number of words. Original adjacent and distance-two bridge pairs make only `O(n)` distinct cached calls, and each word participates in a constant number of those pairs. Total character comparison work is `O(S)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
