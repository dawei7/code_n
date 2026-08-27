# Guided Example: Bulls and Cows

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"secret": "1807", "guess": "7810"}`
- **Required output:** `"1A3B"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing the **<a href="https://en.wikipedia.org/wiki/Bulls_and_Cows" target="_blank">Bulls and Cows</a>** game with your friend.

The objective is to compute `"1A3B"` from `{"secret": "1807", "guess": "7810"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separating bulls before counting cows

The loop processes corresponding characters `a` from `secret` and `b` from `guess`.

If `a == b`, the position is unquestionably a bull. The source increments `x` and does not add either occurrence to a counter. This permanently pairs the two equal-position occurrences in the strongest category.

If `a != b`, the two occurrences cannot be bulls at this index. The secret occurrence may still match the same digit somewhere else in the guess, and the guess occurrence may still match the same digit somewhere else in the secret. The source records them independently:

- `cnt1[a] += 1` counts an unmatched occurrence available from the secret;
- `cnt2[b] += 1` counts an unmatched occurrence requested by the guess.

The counters do not attempt to pair digits immediately. Deferring the pairing avoids dependence on scan order. A matching guess occurrence may appear before or after the corresponding secret occurrence, and the final frequencies summarize both cases uniformly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"secret": "1807", "guess": "7810"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a minimum gives the cow count for one digit

Fix one digit $d$. Suppose that after all bulls are excluded, `cnt1[d] = s_d` and `cnt2[d] = g_d`.

Every cow of digit $d$ consumes one unmatched $d$ from the secret and one unmatched $d$ from the guess. Therefore, the number of such cows cannot exceed either available count. It is at most

$$
\min(s_d,g_d).
$$

That upper bound is also achievable. Pair any $\min(s_d,g_d)$ secret occurrences with the same number of guess occurrences. All these occurrences came from mismatching positions, so none was already used as a bull. The definition allows the non-bull digits to be rearranged, so their original mismatching positions do not prevent these equal-digit pairs from becoming cows.

Thus, digit $d$ contributes exactly `min(cnt1[d], cnt2[d])` cows.

Different digits cannot compete for the same occurrence: a secret `3` can match only a guessed `3`, never a `7`. The contributions are independent, so summing the per-digit minima gives the total cow count:

$$
y=\sum_d\min(\texttt{cnt1}[d],\texttt{cnt2}[d]).
$$

The source iterates only through keys in `cnt1`. That is sufficient. If a digit occurs only in `cnt2`, the secret has zero available copies, so its contribution would be `min(0, count) = 0`. Omitting explicit zero-contribution keys cannot change the sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Fix one digit $d$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Tracing the duplicate-heavy example

Consider `secret = "1123"` and `guess = "0111"`.

| Index | Secret | Guess | Classification | Remaining counters after the index |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | mismatch | secret: `{1: 1}`, guess: `{0: 1}` |
| 1 | 1 | 1 | bull | unchanged |
| 2 | 2 | 1 | mismatch | secret: `{1: 1, 2: 1}`, guess: `{0: 1, 1: 1}` |
| 3 | 3 | 1 | mismatch | secret: `{1: 1, 2: 1, 3: 1}`, guess: `{0: 1, 1: 2}` |

There is one bull at index 1. Among the remaining occurrences, digit 1 contributes

$$
\min(1,2)=1
$$

cow. Digits 0, 2, and 3 have no counterpart in the other unmatched collection, so they contribute zero. The result is `"1A1B"`.

This example demonstrates why a membership-only test is insufficient. The guess contains two unmatched copies of digit 1, but the secret has only one unmatched copy after its bull is removed. Only one cow can be formed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1A3B"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"secret": "1807", "guess": "7810"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1A3B"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two fixed arrays of length ten:** Convert each:** - **Two fixed arrays of length ten:** Convert each unmatched digit to an index and increment two arrays, then sum their minima. This matches the manifest wording and avoids hash-table machinery, while preserving $O(n)$ time and $O(1)$ space. It is not the exact source representation.
- **One signed frequency array in one pass:** For each mismatch, a negative existing count for the secret digit reveals an earlier unmatched guess, and a positive count for the guess digit reveals an earlier unmatched secret. This can count cows online but is less immediately transparent than intersecting two final multisets.
- **Remove matched characters from mutable lists:** Repeated searching and deletion can become $O(n^2)$ and makes duplicate accounting more error-prone.
- **Set intersection:** Sets discard multiplicity. They would undercount when several copies can be cows and overinterpret presence when only one counterpart exists.
- **Counting all common digits before bulls:** The total multiset intersection includes bull occurrences. One may subtract bulls afterward if done carefully, but separating exact matches first makes disjointness explicit and avoids double counting.
- **All digits match in position:** Every index is a bull, both counters remain empty, and the result is `nA0B` with the numeric value of `n` formatted normally.
- **No digit appears in both strings:** Bulls and cows are both zero, yielding `"0A0B"`.
- **Same multiset in different order:** If no positions match but both strings contain the same digit multiplicities, there are zero bulls and $n$ cows.
- **Repeated secret digit:** The number of cows for that digit cannot exceed its unmatched secret frequency, regardless of how many copies the guess contains.
- **Repeated guess digit:** Symmetrically, cows cannot exceed the unmatched guess frequency even when the secret has more copies.
- **Leading zeros:** Inputs are strings rather than numeric values, so a leading `0` remains a real digit and is counted at its position.
- **Equal-length guarantee:** `zip` stops at the shorter input, but the contract guarantees equal lengths, so every position is processed. The source deliberately does not add a separate length check.
- **Length one:** The only pair is either a bull or a mismatch. A mismatching one-character guess cannot produce a cow because no equal digit exists elsewhere.
- **Maximum length:** The method performs one linear scan and stores only ten possible frequency entries, so length 1000 requires no special handling.
- **Output format:** The literal letters are always uppercase and appear in the exact order `A` then `B`, including when either count is zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common length of `secret` and `guess`. The `zip` loop processes each aligned pair once, performing constant-time comparisons and counter updates. This costs $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
