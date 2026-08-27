# Guided Example: Number of Divisible Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "asdf"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Each character of the English alphabet has been mapped to a digit as shown below.

The objective is to compute `6` from `{"word": "asdf"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Construct the phone-style mapping

List

`["ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"]`

groups letters assigned to digits $1$ through $9$. The nested initialization loop uses `enumerate(d, 1)`, so every character in the first group maps to one, every character in the second to two, and so forth.

Dictionary `mp` ends with one entry for each of the 26 lowercase letters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "asdf"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fix a substring start

For each left endpoint `i`, running mapped sum `s` starts at zero. The inner loop moves right endpoint `j` from `i` through the end:

1. Add `mp[word[j]]` to `s`.
2. Current length is `j - i + 1`.
3. Test `s % length == 0`.
4. Add the Boolean result to `ans`.

Because Python treats `true` as one and `false` as zero, the last statement increments the answer exactly for divisible substrings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each left endpoint `i`, running mapped sum `s` starts at... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the running sum stays correct

At the first inner iteration, `s` equals the mapped value of `word[i]`. Each later iteration adds exactly the newly included rightmost character. By induction, after processing $j$,

$$
\texttt{s}
=
\sum_{p=i}^{j}\texttt{mp}[\texttt{word}[p]].
$$

The divisor `j - i + 1` is exactly the number of characters in the same interval, so the modulus test implements the definition directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "asdf"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nine transformed prefix scans:** For each poss:** - **Nine transformed prefix scans:** For each possible average $q=1..9$, count equal prefix sums after subtracting $q$ from every mapped value. This achieves $O(9n)=O(n)$ time.
- **Prefix sums plus all endpoints:** Prefix sums make each range sum constant time but still leave $O(n^2)$ endpoint pairs; the source's running sum is simpler.
- **Recompute each substring sum:** Summing from scratch for every pair would take $O(n^3)$ time.
- **Single character:** Always divisible because any integer is divisible by length one.
- **All characters share a mapped value:** Every substring has that integer average and qualifies.
- **Average need not be a mapped character present:** Only integrality matters; the integer average may differ from each individual value.
- **Lowercase guarantee:** Every input character exists in `mp`, so dictionary lookup cannot fail.
- **Boolean arithmetic:** `ans += condition` relies on Python converting the comparison result to zero or one.
- **Input length 2000:** Quadratic work is about two million substrings, which explains why direct enumeration can still run for this contract.
- **Manifest mismatch:** The approach and complexity must be documented as $O(n^2)$/$O(1)$ for the checked-in implementation.
- **Mapping covers all letters once:** The nine group strings are disjoint and together contain `a` through `z`, so later assignments never overwrite a character with a different value.
- **Integer-average range:** Because mapped values lie from one to nine, any substring average also lies in that interval. This is why the faster alternative needs only nine transformations.
- **Running sum reset:** Each new left endpoint sets `s=0` so characters before `i` do not contaminate the new family of substrings.
- **Modulo divisor is never zero:** Every visited substring is nonempty, making `j-i+1 >= 1`.
- **Endpoint uniqueness:** Equal substring text occurring at two locations counts twice because the problem counts substrings by positions; the nested endpoint loops represent this correctly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The number of endpoint pairs is $n(n+1)/2$. Each extension does constant dictionary lookup and integer arithmetic, so actual time complexity is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
