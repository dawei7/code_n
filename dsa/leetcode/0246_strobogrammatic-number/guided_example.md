# Guided Example: Strobogrammatic Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "69"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `num` which represents an integer, return `true` *if* `num` *is a **strobogrammatic number***.

The objective is to compute `true` from `{"num": "69"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: How the array encodes rotation

The exact solution stores



The array index is an original digit, and the stored number is its rotated digit. Thus `d[6] == 9` and `d[9] == 6`. Invalid digits map to `-1`. Since every actual character in `num` converts to an integer from `0` through `9`, `-1` can never equal a real mirrored digit. The same comparison detects both an invalid digit and a valid digit paired with the wrong mirror.

An array is a natural fit because there are exactly ten possible decimal digits. It avoids hash lookup and keeps the mapping constant-sized.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "69"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Two pointers compare the positions rotation swaps

Pointer `i` starts at `0`, and pointer `j` starts at `len(num) - 1`. During an iteration, the solution converts `num[i]` and `num[j]` to integers `a` and `b`. It then asks whether `d[a] == b`.

This direction matters. `d[a]` is what the left digit becomes after rotation, and rotation moves it to the mirrored right position. If that result does not equal the existing right digit, the rotated number cannot match the original, so the function returns `false` immediately.

After a successful pair, `i` moves one step right and `j` moves one step left. The outer pair never needs examination again. The loop uses `i <= j`, ensuring that an odd-length number's center digit is checked rather than skipped.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Pointer `i` starts at `0`, and pointer `j` starts at `len(nu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why checking one direction per pair is enough

The valid mapping is involutive: rotating twice restores the original digit. In particular, `0`, `1`, and `8` map to themselves, while `6` and `9` map to each other. If the left digit rotates to the right digit, then the right digit necessarily rotates back to the left digit. Therefore, checking `d[a] == b` already validates both destinations of that mirrored pair; a separate `d[b] == a` comparison would be redundant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "69"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build the full rotated copy:** Traverse the st:** - **Build the full rotated copy:** Traverse the string backward, map each digit, join the result, and compare it with the input. This is straightforward and $O(n)$ time, but it uses $O(n)$ additional space that the two-pointer check avoids.
- **Hash-map rotation table:** A dictionary such as `{'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}` can make the valid pairs self-documenting. It has the same asymptotic bounds; the exact solution uses a ten-entry integer array with `-1` sentinels.
- **Explicit valid-pair set:** Check whether `(num[i], num[j])` belongs to `{('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')}`. This is equivalent but represents pairs rather than the rotation function.
- **One digit:** The pointers meet immediately. `0`, `1`, and `8` return `true`; every other digit returns `false`.
- **Odd-length center `6` or `9`:** Both digits rotate validly in a pair but not into themselves, so either one in the center must be rejected.
- **Invalid digits `2`, `3`, `4`, `5`, or `7`:** Their table value is `-1`, which cannot match any right-side digit. The method rejects as soon as such a digit is examined from the left side of its mirrored pair.
- **A nominally invalid digit on the right:** It is still detected. If the left digit is valid, none of its mapped values equals that invalid right digit; if it is paired with another invalid digit, the left maps to `-1`, not the right's numeric value.
- **`6` paired with `6`:** This is invalid because rotating the left `6` produces `9`. Likewise, `9` paired with `9` is invalid.
- **Leading zeros:** The input contract excludes them except for the number `"0"`. The pair logic itself would still test a string such as `"00"` as visually strobogrammatic, but numeric-format validity is supplied by the caller's contract.
- **Long input:** Keeping the number as a string avoids overflow. The algorithm's behavior depends on digit positions, not on the numeric magnitude.
- **Empty input:** The documented minimum length is one. If given an empty string outside the contract, the loop would not run and the source would return `true`; callers requiring different semantics should validate input explicitly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters in `num`. Each iteration validates two positions, except that the final odd-length iteration validates one center position. The loop therefore runs $\lceil n/2\rceil$ times. Each iteration performs constant-time character access, single-digit conversion, array lookup, comparison, and pointer updates, giving $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
