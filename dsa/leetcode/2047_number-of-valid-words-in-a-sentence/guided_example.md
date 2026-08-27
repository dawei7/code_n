# Guided Example: Number of Valid Words in a Sentence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence": "cat and  dog"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A sentence consists of lowercase letters (`'a'` to `'z'`), digits (`'0'` to `'9'`), hyphens (`'-'`), punctuation marks (`'!'`, `'.'`, and `','`), and spaces (`' '`) only. Each sentence can be broken down into **one or more tokens** separated by one or more spaces `' '`.

The objective is to compute `3` from `{"sentence": "cat and  dog"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Split on arbitrary runs of spaces

`sentence.split()` with no explicit separator removes leading and trailing whitespace and treats one or more spaces as a separator. It therefore returns exactly the nonempty tokens even when the sentence contains several spaces between them.

The outer expression applies helper `check` to every token and sums the Boolean results. In Python, true contributes one and false contributes zero, so the sum is the number of valid tokens.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence": "cat and  dog"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject any digit

Inside `check`, the loop scans every character with its index. If `c.isdigit()` is true, the token is immediately invalid.

The input alphabet contains ASCII digits only, so this implements the rule that a valid word may contain no number anywhere, including at the beginning or end.

Early return is safe because no later character can remove an already present digit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Inside `check`, the loop scans every character with its inde... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Allow punctuation only at the final position

The permitted punctuation characters are `!`, `.`, and `,`. The exact expression `c in "!.,"` identifies precisely those three marks.

The full check rejects punctuation when `i < len(s) - 1`. Therefore a punctuation mark is valid only at the token's last index.

This also enforces the “at most one” rule. If a token contained two punctuation marks, the earlier one could not be last and would be rejected. A one-character token such as `"!"` passes because its punctuation is at the end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence": "cat and  dog"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Regular expression:** A carefully anchored pat:** - **Regular expression:** A carefully anchored pattern can validate tokens, but boundary and count rules are easier to audit explicitly.
- **Manual sentence scan:** Validate tokens between spaces without materializing `split()` output, reducing auxiliary space.
- **Only punctuation token:** `!`, `.`, or `,` is valid because the mark is at the end and unique.
- **Punctuation before a letter:** Invalid immediately.
- **Two punctuation marks:** The first cannot be final, so the token is rejected.
- **One internal hyphen:** Valid only with letters directly on both sides.
- **Leading or trailing hyphen:** Invalid by the index checks.
- **Two hyphens:** The second fails the `st` flag.
- **Digit anywhere:** Invalid regardless of all other characters.
- **Several spaces:** `split()` ignores empty regions and returns only real tokens.
- **Letters only:** Always valid under the constrained alphabet.
- **Mixed unsupported character outside constraints:** The exact helper relies on the input alphabet and does not explicitly reject it.
- **Boolean summation:** Each valid token contributes exactly one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the sentence length. Splitting scans $O(L)$ characters. Across all tokens, `check` also examines at most $O(L)$ characters; early rejection can only reduce the work. Total time is $O(L)$.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
