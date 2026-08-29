# Guided Example: Determine if Two Strings Are Close

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word1": "abc", "word2": "bca"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Two strings are considered **close** if you can attain one from the other using the following operations:

The objective is to compute `true` from `{"word1": "abc", "word2": "bca"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Understand what each operation can and cannot change

Trying to simulate arbitrary swaps is unnecessary because the operations have simple global invariants. Operation 1 swaps positions, so repeated applications can rearrange the string in any desired order. It changes neither which character labels occur nor how many copies of each label exist.

Operation 2 swaps the roles of two existing character labels everywhere. For example, if one label occurs twice and another occurs five times, after the operation the first label occurs five times and the second occurs twice. It can move frequency values among existing labels, but it cannot create a character that was absent, remove a character label from the support, or change the multiset of frequency values.

These observations produce two necessary conditions for closeness:

1. The two words must contain exactly the same set of distinct characters.
2. The unordered collection of their character frequencies must be identical.

The exact source tests precisely these two conditions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word1": "abc", "word2": "bca"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build frequency maps

`Counter(word1)` creates a mapping from every character present in `word1` to its occurrence count; `Counter(word2)` does the same for the other word. Missing characters do not appear as keys.

The expression `set(cnt1.keys()) == set(cnt2.keys())` checks the support condition. This is stronger than checking only the number of distinct characters. For example, `"aabb"` and `"ccdd"` have the same number of distinct labels and the same frequencies, but they are not close: operation 2 is allowed only between existing characters, so the first word can never introduce `c` or `d`.

The expression `sorted(cnt1.values()) == sorted(cnt2.values())` checks the frequency-multiset condition. Sorting deliberately discards the association between a count and its current label. That association is exactly what operation 2 may rearrange. For instance, counts `a: 3, b: 1` and `a: 1, b: 3` should compare equal after sorting because globally swapping `a` and `b` transforms one assignment into the other.

The return statement joins the conditions with `and`. Python evaluates the sorted-frequency comparison first because it appears first in the source, then evaluates the key-set comparison only if needed. Evaluation order does not affect the mathematical result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why both conditions are necessary

Position swaps merely permute occurrences, and global character exchanges act only on two labels already present. Therefore neither operation changes the set of labels that occur. If the key sets differ, transformation is impossible.

Every position swap leaves every frequency unchanged. A global exchange swaps two entries in the conceptual frequency table but leaves the unordered list of entry values unchanged. A sequence of such operations still preserves that multiset. If the sorted frequency lists differ, transformation is likewise impossible.

Notice that an explicit length comparison is not required. Equal sorted frequency lists have equal sums, and each sum is the corresponding word length. Therefore frequency equality already implies equal lengths. For `"a"` and `"aa"`, the lists `[1]` and `[2]` differ immediately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word1": "abc", "word2": "bca"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed arrays of length 26:** Count each letter by `ord(character) - ord("a")`, compare zero-versus-nonzero positions, and compare sorted count arrays. This has the same asymptotic bounds and makes constant alphabet storage explicit.
- **Bitmask for character support:** A 26-bit integer can record which letters occur, while arrays hold counts. It avoids allocating sets but does not change the algorithmic complexity.
- **Direct counter equality:** This checks whether the words are anagrams, which is sufficient but not necessary for closeness because global label swaps may reassign frequencies.
- **Sorted frequencies without key sets:** This is incorrect for words such as `"aabb"` and `"ccdd"`. Matching counts cannot introduce absent labels.
- **Equal key sets without frequency comparison:** This is also insufficient; `"aaab"` and `"aabb"` share labels but have frequency multisets `[1, 3]` and `[2, 2]`.
- **Different lengths:** Their frequency lists cannot have equal sums, so the source returns false without needing a separate length branch.
- **One-character words:** Equal letters produce the same key set and count; different letters fail the key-set condition even though both frequency lists are `[1]`.
- **Already equal or anagrams:** Both invariants hold, and positional swaps alone are enough. The method correctly returns true without simulating them.
- **Same frequencies attached to different shared letters:** This is the main case enabled by operation 2; sorted values match even when the counters themselves differ.
- **Repeated equal frequencies:** Pairing labels is still possible. If several labels share one count, their assignments are interchangeable, and sorting naturally retains the right multiplicity.
- **Operation restriction to existing characters:** The support-set equality is precisely what enforces this often-missed rule.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u\log u)$. Let `N` and `M` be the lengths of `word1` and `word2`, and let `u` be the number of distinct lowercase letters involved. Building both counters takes $O(N + M)$ time. Creating key sets takes $O(u)$ expected time, and sorting the two frequency lists takes $O(u\log u)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
