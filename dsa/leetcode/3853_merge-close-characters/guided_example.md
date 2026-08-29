# Guided Example: Merge Close Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abca", "k": 3}`
- **Required output:** `"abc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters and an integer `k`.

The objective is to compute `"abc"` from `{"s": "abca", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Think in current-string positions, not original positions

The distance rule is evaluated after every deletion. If characters disappear, later characters move left, so two equal characters that were originally farther than `k` apart may eventually become close. An algorithm that stores only original indices would miss that change.

The source instead builds the final string in `ans`. At every moment, `ans` contains only characters that have survived processing so far. Therefore `len(ans)` is exactly the index at which the next input character would appear in the currently compacted string. This is why the line `cur = len(ans)` is the central detail: `cur` is a current-string position even though the outer loop reads the original string from left to right.

The dictionary `last` maps a character to the index of its most recent retained occurrence in `ans`. When the next character `c` arrives, the source checks whether

`cur - last[c] <= k`.

If so, the new right occurrence merges into the retained left occurrence, which means the new occurrence is deleted. The implementation performs that deletion simply by not appending `c`. If no retained equal occurrence is close enough, it appends `c` and records its new compacted index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abca", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the most recent equal occurrence is sufficient

Suppose `ans` is already stable: no two equal retained characters are within distance `k`. For any character `c`, consecutive retained occurrences of `c` must therefore be more than `k` positions apart.

The next input character would be placed at the right end, at index `cur`. If it is not close to the most recent retained `c`, it cannot be close to any earlier `c` because every earlier occurrence has an even smaller index and therefore a greater distance from `cur`. If it is close to the most recent retained `c`, no second retained `c` can also be close: two retained occurrences inside the last `k` positions would themselves be at distance at most `k`, contradicting the stability of `ans`.

Thus there is at most one eligible equal left partner for the new character, and `last[c]` identifies it. No scan over all earlier positions is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why prefix compaction agrees with the required merge order

The problem describes repeated operations on the whole current string and specifies smallest left index first, then smallest right index. The source appears to use a different schedule because it resolves a character as soon as that character is encountered. These schedules produce the same survivors.

First, every merge deletes only its right character. A character already retained in a processed prefix can never be deleted because of a character appended later: if they merge, the later character is the right endpoint and is the one removed. Operations wholly inside a prefix may delete prefix characters, but performing those internal deletions before examining a later suffix is safe. A deletion in the suffix cannot change which prefix character is the right endpoint of a pair wholly inside that prefix, while a prefix deletion merely compacts all later positions in exactly the way represented by `len(ans)`.

This permits an induction over input prefixes. Before reading a new character, assume `ans` is the stable result of the processed prefix. Appending the new character introduces no pair between two old survivors because the prefix was already stable. Any new eligible pair must use the appended character as its right endpoint. The preceding argument shows that there is at most one such pair and that its left endpoint is `last[c]`. If it is close, the specified process eventually deletes the new right character; skipping it produces the same stable prefix. If it is not close, no merge is possible and appending it preserves stability.

The priority rule cannot change this conclusion. If other deletions in the full string are scheduled before or after a merge involving the new suffix, they never cause a later character to delete an earlier survivor. They only remove right endpoints and compact the positions, which the prefix construction already incorporates. Therefore processing prefixes eagerly is a valid way to compute the deterministic final string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abca", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal repeated simulation:** Search the current string for the priority pair, delete its right endpoint, and restart. This follows the statement directly but repeatedly scans and shifts a mutable sequence; depending on the data structure and search strategy, it can take quadratic or even cubic time.
- **Original-index distance:** Comparing original loop indices is incorrect because earlier deletions shorten the current string. The source's `len(ans)` is the exact current index after all skipped characters have been removed.
- **Track every occurrence per character:** A list or deque of retained positions is unnecessary. Stability guarantees that if the newest retained equal character is too far away, every older one is farther; if it is close, no other retained equal occurrence can also be close.
- **Stack without per-character lookup:** Scanning backward through `ans` for an equal character can degrade to `O(N^2)`. The dictionary locates the only relevant retained occurrence directly.
- **Repeated equal characters:** A run such as `"aaaa"` with positive `k` keeps only its first character. Every later `a` would appear immediately after the retained one in the compacted string and is deleted.
- **Cascading closeness:** Deleting intervening characters can bring later equal characters within range. Because deleted characters are never appended, later `cur` values automatically reflect every cascade.
- **Exactly distance `k`:** The pair is eligible because the rule says at most `k`. The source correctly uses `<= k` rather than a strict comparison.
- **No equal characters:** Every character is appended, `ans` remains the original string, and the final join returns it unchanged.
- **`k` at least the string length:** Every later occurrence of a character is within range of its first surviving occurrence after compaction, so the result contains only the first occurrence of each distinct letter.
- **Dictionary indices after skips:** Skipping a new right character does not shift any character already in `ans`, so stored indices remain valid. The construction never physically deletes an element from the middle of `ans`.
- **Priority ties:** Once the processed prefix is stable, a new rightmost character has at most one close equal survivor. The smallest-left and smallest-right tie rules therefore do not require an explicit comparison in the one-pass representation.
- **Empty result:** The input is nonempty and merges always preserve the left endpoint, so at least the first input character survives. The returned string cannot be empty under this contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let `N` be the length of `s`. The outer loop visits every input character once. Dictionary membership, lookup, and update are expected `O(1)` operations, and list append is amortized `O(1)`. Joining the retained characters takes `O(N)` time in the worst case. The exact source therefore runs in expected `O(N)` time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
