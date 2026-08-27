# Guided Example: Unique Substrings With Equal Digit Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1212"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a digit string `s`, return *the number of **unique substrings **of *`s`* where every digit appears the same number of times.*

The objective is to compute `5` from `{"s": "1212"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build counts for every prefix

Let `presum[p][d]` mean the number of occurrences of digit `d` among the first `p` characters, which are the characters at indices zero through `p - 1`. The table has `n + 1` rows and ten columns. Row zero represents the empty prefix, so all ten counts start at zero.

When the outer construction loop reads `s[i]`, it first increments the matching digit in row `i + 1`. It then adds every value from row `i` into that new row. Consequently, row `i + 1` contains all counts from the previous prefix plus the newly encountered digit.

For example, after processing the first three characters of `"1212"`, the row for prefix length three records two occurrences of digit one, one occurrence of digit two, and zero for every other digit. The table retains such a snapshot for every possible prefix boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1212"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recover a substring's frequencies by subtraction

The helper `check(i, j)` examines the inclusive substring from index `i` through `j`. For a digit `k`, its count in that substring is

$$
\texttt{presum[j + 1][k]}-\texttt{presum[i][k]}.
$$

The first term counts digit `k` before the boundary just after `j`. The second counts occurrences before `i`, which do not belong to the substring. Subtracting removes exactly that earlier portion.

The helper puts every positive count into a small set `v`. A zero is deliberately ignored because the rule compares only digits that appear in the substring. As soon as `v` contains more than one value, two present digits have different frequencies, so the helper immediately returns false. If the scan over all ten digits finishes with at most one positive frequency value, all present digits occur equally often and the helper returns true.

Every tested substring is nonempty because `j` starts at `i`. Therefore, at least one digit has a positive count. The “at most one value” test is effectively “exactly one distinct positive frequency,” but writing the helper this way also keeps the logic simple.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper `check(i, j)` examines the inclusive substring fr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate every possible interval

The nested comprehension chooses every start index `i` from zero through `n - 1` and every end index `j` from `i` through `n - 1`. These are precisely all nonempty contiguous substrings: each substring has one unique pair of inclusive endpoints, and every generated pair satisfies `i <= j`.

For each pair, the filter calls `check(i, j)`. Only when that helper succeeds does the expression create `s[i : j + 1]`. Python slicing excludes its right endpoint, so `j + 1` is necessary to include the character at `j`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1212"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rolling hash:** Maintain a hash while extendin:** - **Rolling hash:** Maintain a hash while extending each start position and store only hashes for valid intervals, as the editorial and manifest describe. This can reach expected $O(n^2)$ time and $O(n^2)$ space, but a single modular hash has a collision risk unless collision handling is added.
- **Trie of substrings:** Insert digit paths into a prefix tree and mark valid terminal nodes. This avoids probabilistic hash collisions but can allocate many nodes and has a larger constant factor.
- **Incremental ten-count array:** For each fixed start, extend the end and update one digit count. This removes the prefix table and still checks each interval in constant alphabet time, although storing real slices retains the cubic worst-case copying cost.
- **Naively recount every slice:** Scanning all characters again for every endpoint pair takes cubic time even before accounting for set insertion, so prefix counts are a meaningful local improvement.
- **Single-character input:** Its only substring contains one present digit with frequency one, so the result is one.
- **Only one distinct digit:** Every substring is frequency-valid, but equal runs of the same length have equal contents and are deduplicated by the set.
- **Digit zero:** Zero is a normal input character. The helper ignores a frequency of zero, meaning “digit absent,” but does not ignore the character `'0'` when its computed count is positive.
- **Equal frequencies do not imply equal strings:** `"12"` and `"21"` must both be counted because order is part of substring identity.
- **Repeated occurrences:** Identical text at different endpoints contributes once because `vis` stores values rather than positions.
- **Early helper exit:** Once two different positive counts are found, later digits cannot make those existing counts equal, so returning false immediately is safe.
- **Input preservation:** The prefix table and slices are new objects; the original string is never modified.
- **Manifest discrepancy:** The branch metadata describes paired rolling hashes, but the protected source uses prefix counts and full strings. Complexity and mechanics must be judged from that source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(10n)$. Let $n$ be the length of `s`. Building `presum` processes ten columns for each character. Because the digit alphabet has fixed size ten, this is $O(10n)=O(n)$ time and $O(10n)=O(n)$ space.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
