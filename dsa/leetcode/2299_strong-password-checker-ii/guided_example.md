# Guided Example: Strong Password Checker II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"password": "IloveLe3tcode!"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A password is said to be **strong** if it satisfies all the following criteria:

The objective is to compute `true` from `{"password": "IloveLe3tcode!"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reject insufficient length before scanning categories

A strong password needs at least eight characters. The method checks `len(password) < 8` first and immediately returns false.

No combination of character categories can repair a short password, so early rejection is both correct and avoids unnecessary work.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"password": "IloveLe3tcode!"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode four required categories as bits

`mask` begins at zero. Four bits represent whether the scan has seen:

- bit one, value `1`: a lowercase letter;
- bit two, value `2`: an uppercase letter;
- bit three, value `4`: a digit;
- bit four, value `8`: a special character.

Bitwise OR sets a category bit without clearing bits already found. Repeated characters from the same category leave the mask unchanged.

All four bits set produce `1+2+4+8=15`, so the final comparison `mask == 15` requires every category.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `mask` begins at zero.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject adjacent duplicates during the same pass

At index `i>0`, the code compares the current character with `password[i-1]`. Equality causes immediate false.

Only adjacent equality is forbidden. A character may reappear after another character, so `"aba"` passes this condition while `"aab"` fails.

Checking adjacency before category classification is safe: once a violation exists, no remaining suffix can remove it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"password": "IloveLe3tcode!"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Four Boolean variables:** They express the sam:** - **Four Boolean variables:** They express the same state and complexity; the bit mask packages them compactly.
- **Regular expressions:** Separate searches can verify categories and adjacency but may scan the string multiple times and obscure the one-pass invariant.
- **Set of categories:** It works but allocates a dynamic object for four fixed facts.
- **Explicit special-character membership:** It is safer if arbitrary input characters are allowed; the source guarantee makes the `else` branch exact.
- **Exactly eight characters:** Length passes because the test rejects only values below eight.
- **All categories but too short:** The early length condition still returns false.
- **Long enough but one category missing:** The final mask differs from 15.
- **Adjacent repeated special character:** It fails just like repeated letters or digits.
- **Nonadjacent repeated character:** It is allowed.
- **First character:** The `if i` guard prevents an invalid negative-index adjacency comparison.
- **Repeated category:** OR is idempotent and retains the bit once set.
- **Allowed character domain:** It is what makes every classification exhaustive.
- **Input preservation:** The method performs read-only checks.
- **Special-character list:** Every punctuation character permitted by the contract reaches the same `else` branch and sets bit eight.
- **Adjacent equality is case-sensitive:** `'a'` and `'A'` are different characters, so they do not violate adjacency.
- **Unicode method concern:** `islower` and related methods recognize more than ASCII in general, but the input contract restricts characters to the specified ASCII domain.
- **Mask cannot exceed 15:** Only the four designated bits are ORed, so equality with 15 is a complete all-flags test.
- **Failure order:** Length and adjacency may return early; the method is not required to report which or how many rules failed.
- **Digit classification:** Each allowed decimal digit sets bit four regardless of its numeric value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be password length. After the constant-time length test, the loop processes at most `n` characters once. Character classification and bit operations are constant time for the allowed single characters, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
