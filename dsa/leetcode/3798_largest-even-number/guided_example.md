# Guided Example: Largest Even Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1112"}`
- **Required output:** `"1112"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting only of the characters `'1'` and `'2'`.

The objective is to compute `"1112"` from `{"s": "1112"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An attainable even number must end in `2`

The input contains only digits `1` and `2`. A decimal integer is even exactly when its last digit is even, so every nonempty valid subsequence must end at an occurrence of `2`.

If no `2` occurs, no deletion pattern can create an even final digit and the answer is the empty string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1112"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the last `2` as the final digit

Suppose the final retained digit is the `2` at index `p`. Every retained character must come from positions at most `p` because subsequence order cannot change.

Keeping all characters `s[0:p+1]` produces the longest possible subsequence ending at that occurrence. Deleting any character from this prefix would shorten the result without helping evenness.

Among all possible final `2` occurrences, choosing the last one permits the greatest prefix length. Every character after the last `2` is necessarily `1` and must be deleted because retaining it would make the number odd.

Thus the unique optimal form is the entire prefix ending at the last `2`.

This separates forced deletions from harmful ones. Every character after the last two is forced out by parity. Every character at or before it can remain without changing the final digit, and deleting any of them only reduces magnitude.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the final retained digit is the `2` at index `p`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why maximum length determines maximum numeric value

All digits are nonzero. Any $L$-digit positive decimal number is at least $10^{L-1}$, while any number with fewer than $L$ digits is smaller than $10^{L-1}$.

Therefore a longer attainable subsequence always represents a larger integer than every shorter one, regardless of its arrangement of ones and twos. The last-`2` prefix has maximum length, so no lexicographic comparison among shorter candidates is needed.

Within that maximum length, there is only one subsequence: retaining every position through the last `2`. It is consequently the largest numeric result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1112"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1112"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1112"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Search explicitly for the last `2`:** `s.rfind:** - **Search explicitly for the last `2`:** `s.rfind("2")` followed by a prefix slice expresses the same logic, but `rstrip` is shorter.
- **Keep only all twos:** Internal ones can remain without hurting parity and increase digit count, so deleting them is suboptimal.
- **Choose the first `2`:** A later `2` permits a longer and therefore larger result.
- **Delete arbitrary trailing digits:** Only trailing ones are forced; deleting a trailing two would lose the best final digit.
- **All ones:** No even subsequence exists, so return `""`.
- **Single `2`:** It is already the largest even result.
- **Single `1`:** Stripping returns the empty string.
- **String already ends in `2`:** Keep every character.
- **Multiple trailing ones:** All are removed in one operation.
- **Internal ones:** They remain because they increase the number's length.
- **No leading-zero concern:** The input alphabet excludes zero.
- **Input preservation:** Strings are immutable; trimming returns a string result without modifying `s`.
- **`rstrip` semantics:** It removes only the maximal trailing run of ones.
- **Maximum-length uniqueness:** Keeping the whole last-two prefix is the sole candidate of that length.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=len(s)$. In the worst case, `rstrip` scans the entire string from right to left, so time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
