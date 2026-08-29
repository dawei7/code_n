# Guided Example: Count the Number of Special Characters II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "aaAbcBC"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `word`. A letter `c` is called **special** if it appears **both** in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

The objective is to compute `3` from `{"word": "aaAbcBC"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Version II adds an ordering condition.** A letter is special only if both cases occur and every lowercase occurrence lies before the first uppercase occurrence. It is not enough to know that lowercase and uppercase are present. The decisive positions are:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "aaAbcBC"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the last occurrence of the lowercase form;
- the first occurrence of the uppercase form.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

All lowercase copies precede all uppercase copies exactly when:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "aaAbcBC"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four-state automaton:** Track unseen, lowercase-only, valid uppercase-after-lowercase, and invalid ordering per letter. This matches the manifest.
- **Two 26-element position arrays:** Store last lowercase and first uppercase indices, avoiding hash maps.
- **Set-only solution from version I:** Incorrect because it forgets occurrence order.
- **Only lowercase form:** Fails uppercase membership.
- **Only uppercase form:** Fails lowercase membership.
- **Uppercase before lowercase:** The position inequality fails.
- **Lowercase after an uppercase:** Latest lowercase exposes the violation even if an earlier lowercase was validly placed.
- **Several lowercase then several uppercase:** Qualifies.
- **Interleaved cases:** Fails whenever any lowercase occurs after the first uppercase.
- **One occurrence of each:** Their index order alone decides.
- **Strict case sensitivity:** Lowercase and uppercase are different keys.
- **First uppercase:** It is the earliest boundary every lowercase must precede.
- **Last lowercase:** It is the strongest lowercase boundary to test.
- **No input mutation:** The method only records indices.
- **Source/manifest mismatch:** Exact source uses two occurrence dictionaries, not an automaton.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+26)$. The occurrence scan takes $O(n)$ expected time using dictionary operations. The final generator performs exactly 26 constant-time checks. Total expected time is $O(n+26)=O(n)$.
- **Auxiliary Space Complexity:** $O(52)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
