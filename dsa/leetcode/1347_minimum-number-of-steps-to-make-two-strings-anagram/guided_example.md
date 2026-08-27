# Guided Example: Minimum Number of Steps to Make Two Strings Anagram

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "bab", "t": "aba"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings of the same length `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

The objective is to compute `1` from `{"s": "bab", "t": "aba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the frequencies of `s` as available quotas

`cnt = Counter(s)` records how many copies of each character the target anagram needs. Before processing `t`, `cnt[c]` is the full quota for character `c`.

For each character `c` in `t`, the solution executes `cnt[c] -= 1`:

- If the new count is zero or positive, this occurrence of `c` can be matched to one required occurrence in `s`.
- If the new count is negative, `t` has supplied more copies of `c` than `s` needs. This occurrence is surplus and must eventually be replaced.

`ans += cnt[c] < 0` uses the fact that Python Booleans behave as integers in addition: `true` contributes one and `false` contributes zero. Once a character’s quota has been exhausted, every additional occurrence makes its count more negative and adds one more required replacement.

For `s = "bab"`, the quotas are two `b` characters and one `a`. Processing `t = "aba"` consumes the `a` quota and one `b` quota. The final `a` drives its count below zero, so exactly one surplus occurrence is counted. Replacing that surplus `a` with the missing `b` makes the strings anagrams.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "bab", "t": "aba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why counting surplus occurrences gives the minimum

Every surplus occurrence in `t` has a character whose final frequency is greater than its frequency in `s`. Leaving that occurrence unchanged would keep the frequency too high, so at least one replacement is necessary for each surplus. This gives a lower bound of `ans` operations.

The strings have the same length. Therefore, the total amount by which some character frequencies in `t` exceed those in `s` is exactly equal to the total amount by which other frequencies fall short. Each replacement can take one surplus occurrence and change it into one missing character, reducing both totals by one. Repeating this pairing performs exactly `ans` replacements and reaches the target frequency multiset.

The lower bound is achievable, so it is the minimum.

Preloading all of `s` before scanning `t` is important. It means the algorithm knows the complete quota even if a matching occurrence conceptually appears at a later position. Because anagram matching ignores positions, no ordering decision is necessary.

The method does not need to construct the final anagram or decide which specific missing character replaces each surplus while counting. Equal lengths guarantee that a one-to-one pairing with deficits exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every surplus occurrence in `t` has a character whose final ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "bab", "t": "aba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed array of twenty-six counts:** Increment :** - **Fixed array of twenty-six counts:** Increment positions for `s`, decrement for `t`, and sum the surplus or deficit side. It has the same $O(n)$ time and $O(1)$ space with lower hashing overhead.
- **Two counters:** Build frequencies for both strings and sum positive differences. This is straightforward but stores duplicate map structure and performs a separate comparison pass.
- **Sorting both strings:** Equal sorted strings reveal whether no work is needed, but deriving the replacement count through sorting takes $O(n\log n)$ time.
- **Counting deficits instead of surpluses:** Because lengths are equal, the total missing occurrences in `t` equals the total excess occurrences. Either side gives the same answer.
- **Already anagrams:** No quota becomes negative, so `ans` remains zero even when character orders differ.
- **All characters different:** Every occurrence in `t` outside the quotas becomes surplus, and each must be replaced.
- **Repeated characters:** The counter distinguishes occurrences through the quota; only copies beyond the required count contribute.
- **One-character strings:** Equal characters return zero, while different characters produce one replacement.
- **Equal-length guarantee:** The proof that every surplus can pair with a deficit depends on equal total lengths. A generalized unequal-length problem would also require insertions or deletions.
- **Position independence:** A character at one position may satisfy a quota originating anywhere in `s` because anagrams depend only on frequencies.
- **Input preservation:** Neither string is modified; the algorithm changes only counter values.
- **Boolean arithmetic:** `cnt[c] < 0` is a Boolean expression, and Python adds it as zero or one. In a language without this conversion, use an explicit conditional increment to preserve the same counting logic.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length.
- **Auxiliary Space Complexity:** $O(26)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
