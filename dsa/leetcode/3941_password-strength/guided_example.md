# Guided Example: Password Strength

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"password": "aA1!"}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `password`.

The objective is to compute `11` from `{"password": "aA1!"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why deduplication is the central operation

Suppose the password contains `"bbB11#"`. Iterating the original string and adding a score per position would count `b` twice and `1` twice, producing too large a result. The set contains only `{"b", "B", "1", "#"}`, so each identity contributes once.

Uppercase and lowercase versions remain distinct because Python strings are case-sensitive: `"b" != "B"`. This matches the rule that they are different characters and also assigns them different weights.

The order in which a set yields its characters is unspecified, but addition is commutative. The final sum is independent of iteration order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"password": "aA1!"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Classify one distinct character

The `if`/`elif` chain assigns exactly one category:

- `ch.islower()` adds one;
- otherwise, `ch.isupper()` adds two;
- otherwise, `ch.isdigit()` adds three;
- otherwise, the source adds five.

Under the contract, the only possible characters are English letters, decimal digits, and `!@#$`. Therefore every character that reaches the final `else` is one of the four allowed special characters.

Using an exclusive chain matters. A character must contribute one category weight, not several independent weights. For the restricted ASCII alphabet, the lowercase, uppercase, digit, and special categories are disjoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why each contribution is exact

Take any character appearing in `password`. Set construction places one copy of it in `st` regardless of its frequency. The loop visits that copy once. The category tests select its prescribed weight, so the character contributes exactly once.

Conversely, every member of `st` came from the password. The loop never invents or scores an absent character. Summing the selected weights therefore equals the definition over all and only distinct present characters.

The result begins at zero and increases by a positive category weight for every set member. There are no interactions between characters, so no dynamic programming or position tracking is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"password": "aA1!"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Score every input position:** This overcounts repeated characters because the rule is based on distinct identities.
- **Use four bitmasks:** One bit per lowercase letter, uppercase letter, digit, and special character can deduplicate using fixed integer state and gives a more literal $O(1)$ representation.
- **Use one 66-entry Boolean table:** Map every allowed character to an index, mark presence, and total marked category weights. This avoids hashing but requires explicit mapping logic.
- **Count category diversity rather than character diversity:** Two different lowercase letters each earn one point. The score is not merely one point for the lowercase category being present.
- **Case-fold the password:** Lowercase and uppercase forms are distinct and have different weights, so normalization would corrupt the result.
- **Repeated character:** Any number of repetitions produces the same one set member and one contribution.
- **Same letter in both cases:** `a` and `A` are distinct; together they contribute $1+2=3$.
- **Repeated special character:** A symbol such as `!` contributes five once, not five per occurrence.
- **All 66 allowed characters:** The score is the maximum 128.
- **One-character password:** The answer is simply that character's category weight.
- **Set iteration order:** It may vary between executions, but integer addition yields the same total.
- **Invalid punctuation:** The source's `else` would score it as special. Correctness relies on the documented restriction to `!@#$`.
- **Non-ASCII characters:** Python classification may accept some, but they are outside the input contract and need no special handling here.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the password length and $D$ the number of distinct characters.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
