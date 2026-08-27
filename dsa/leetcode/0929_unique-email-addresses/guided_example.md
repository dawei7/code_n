# Guided Example: Unique Email Addresses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"emails": ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Every **valid email** consists of a **local name** and a **domain name**, separated by the `'@'` sign. Besides lowercase letters, the email may contain one or more `'.'` or `'+'`.

The objective is to compute `3` from `{"emails": ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Scan the local name from left to right.

- A period `.` is ignored with `continue`.
- The first plus `+` ends meaningful local input, so the loop `break`s.
- Any lowercase letter is appended to temporary list `t`.

After the first plus, all remaining local characters—including letters, dots, and later plus signs—are ignored. Breaking immediately implements that rule directly.

Joining `t` removes all periods that appeared before the plus while preserving letter order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"emails": ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Ensure every candidate decision satisfies the required const... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"emails": ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Regular expressions:** They can remove dots an:** - **Regular expressions:** They can remove dots and plus suffixes but add complexity and must still avoid altering domains.
- **Normalize the full email string:** Incorrect because dots and plus signs in the domain do not use local-name rules.
- **Split local on plus first, then remove dots:** This is an equivalent concise formulation.
- **No dots or plus:** Canonical form equals the original email.
- **Several local dots:** All are removed, including adjacent dots allowed by the simplified contract.
- **Several plus signs:** Only the first matters because everything after it is ignored.
- **Dot after plus:** It is ignored as part of the entire discarded suffix.
- **Same local, different domain:** These are distinct recipients.
- **Different written locals, same normalized letters:** They collapse when domains match.
- **Duplicate identical emails:** The set counts one recipient.
- **Domain periods:** They remain exactly where written.
- **Exactly one `@`:** Makes two-variable split safe.
- **Any input order:** Set cardinality is independent of message order.
- **Local plus near the end:** Even a one-character suffix after plus is fully discarded.
- **Periods only in the domain:** They are preserved, so domains remain distinguishable.
- **Canonical set strings:** Including `@` makes the local/domain boundary explicit.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $S$ be the total number of characters across all input emails. Splitting, scanning, joining, hashing, and set insertion together take expected time proportional to processed text.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
