# Guided Example: Maximize Number of Subsequences in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "abdcdbc", "pattern": "ac"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `text` and another **0-indexed** string `pattern` of length `2`, both of which consist of only lowercase English letters.

The objective is to compute `4` from `{"text": "abdcdbc", "pattern": "ac"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track first-character occurrences

Variable `x` counts how many copies of `pattern[0]` have appeared in the processed prefix.

Whenever the scan reaches a later `pattern[1]`, each of those `x` earlier copies forms one distinct subsequence ending at the current position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "abdcdbc", "pattern": "ac"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count existing subsequences as their second character arrives

When `c == pattern[1]`, the code increments `y`, the total number of second-pattern characters seen, and adds `x` to `ans`.

Each ordered pair is counted exactly once: at the iteration of its second position. Characters not equal to either pattern member affect no counter.

For distinct pattern characters, incrementing `y` before adding `x` has no interaction with `x`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `c == pattern[1]`, the code increments `y`, the total n... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle equal pattern characters correctly

If `pattern[0] == pattern[1]`, both `if` statements execute for each matching character.

The second-character block runs first and adds the old `x`, which is the number of earlier equal characters. Only afterward does the first-character block increment `x` for future pairs.

Thus $q$ equal characters produce

$$
0+1+\cdots+(q-1)=\binom q2
$$

existing subsequences, exactly the number of ways to choose two positions in increasing order. Both `x` and `y` end at $q$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "abdcdbc", "pattern": "ac"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix and suffix arrays:** Precompute first-c:** - **Prefix and suffix arrays:** Precompute first-character prefixes and second-character suffixes for every insertion point. This verifies all positions but uses $O(n)$ space unnecessarily.
- **Try both endpoint strings explicitly:** Construct and recount two modified strings. It stays linear but duplicates scans and allocates strings.
- **Pattern characters equal:** The ordered pair of independent `if` statements counts earlier equal occurrences before incrementing the current one.
- **No first-pattern characters:** Existing count is zero; inserting the first character gains all `y` second characters.
- **No second-pattern characters:** Inserting the second at the end gains all `x` first characters.
- **Neither character appears:** Exactly one insertion cannot form a length-two subsequence, so the result is zero.
- **One-character text:** Existing count is zero; the insertion may create one pair if that character matches the complementary pattern member.
- **Beginning insertion:** It is optimal only for the first pattern character.
- **End insertion:** It is optimal only for the second pattern character.
- **Other letters:** They preserve relative ordering but contribute no counters.
- **Subsequence, not substring:** Matching positions need not be adjacent.
- **Exactly one insertion:** The formula always accounts for one new character, even when it creates zero pairs.
- **Input preservation:** No character is actually inserted into `text`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The method scans `text` once and performs constant work per character, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
