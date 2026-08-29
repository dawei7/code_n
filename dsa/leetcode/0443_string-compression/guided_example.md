# Guided Example: String Compression

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"chars": ["a"]}`
- **Required output:** `{"length": 1, "prefix": ["a"]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of characters `chars`, compress it using the following algorithm:

The objective is to compute `{"length": 1, "prefix": ["a"]}` from `{"chars": ["a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate reading from writing

The input is already arranged into consecutive character groups. The solution uses:

- `i` as the first unread index of the current group;
- `j` to scan for that group's exclusive end; and
- `k` as the next output position in the same array.

At all times, `chars[0:k]` is the completed compressed prefix, while `chars[i:n]` contains groups not yet processed.

The algorithm does not need a second output array. It overwrites positions at or before the read frontier because a group's compressed representation is never longer than that group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"chars": ["a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find one maximal run

For current `i`, set `j = i + 1` and advance while `j < n` and `chars[j] == chars[i]`. When the loop stops, the group occupies indices `i` through `j-1`, and its length is `j - i`.

Stopping on the first different character makes each group maximal. The next outer iteration begins with `i = j`, so no character is skipped or included in two groups.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Write the character and optional count

Every group contributes its character once:

`chars[k] = chars[i]`, followed by `k += 1`.

If the group length is one, nothing else is written. This follows the required format: a singleton `a` stays `a`, not `a1`.

For length greater than one, `cnt = str(j - i)` creates the decimal count. The loop writes each digit separately. This matters for lengths at least ten: a run of 12 `b` characters contributes `'b'`, `'1'`, and `'2'`, not one multi-character array element.

Finally `i = j` advances to the next group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"length": 1, "prefix": ["a"]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"chars": ["a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"length": 1, "prefix": ["a"]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build a separate compressed list:** It simplifies writing but violates the constant-extra-space requirement.
- **Use repeated string concatenation:** Besides not updating `chars` directly, immutable concatenation can copy growing results repeatedly.
- **Write `1` for singletons:** This violates the required format and increases the result unnecessarily.
- **Write a multi-digit count as one list item:** Each position must contain one character, so count digits must be emitted separately.
- **One input character:** The character is written to position zero and length one is returned.
- **All characters distinct:** Every group is a singleton, `k == n`, and the visible array remains unchanged.
- **One long group:** Output is the character followed by every decimal digit of `n`.
- **Group length ten or more:** `str(...)` naturally preserves digit order, such as `12` becoming `'1','2'`.
- **Symbols and digit characters:** Grouping compares character equality only; an input digit used as data is distinct from count digits by position/context, as allowed by the compression format.
- **Trailing stale cells:** They are intentionally ignored beyond returned `k` and need not be erased.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the original array length. `j` moves forward over each input character exactly once across groups. The number of output writes is at most $n$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
