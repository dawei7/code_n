# Guided Example: Reward Top K Students

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"positive_feedback": ["smart", "brilliant", "studious"], "negative_feedback": ["not"], "report": ["this student is studious", "the student is smart"], "student_id": [1, 2], "k": 2}`
- **Required output:** `[1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two string arrays $\text{positive}_{feedback}$ and $\text{negative}_{feedback}$, containing the words denoting positive and negative feedback, respectively. Note that **no** word is both positive and negative.

The objective is to compute `[1, 2]` from `{"positive_feedback": ["smart", "brilliant", "studious"], "negative_feedback": ["not"], "report": ["this student is studious", "the student is smart"], "student_id": [1, 2], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn feedback vocabulary into constant-time score lookups

Positive words are worth $+3$, negative words are worth $-1$, and every other word is worth zero.

The method converts `positive_feedback` to set `ps` and `negative_feedback` to set `ns`. Hash-set membership is expected $O(1)$, so each report word can be classified without scanning either vocabulary list.

The contract guarantees that no word belongs to both sets. The `if` followed by `elif` therefore has an unambiguous result:

- if `w in ps`, add three;
- else if `w in ns`, subtract one;
- otherwise, leave the score unchanged.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"positive_feedback": ["smart", "brilliant", "studious"], "negative_feedback": ["not"], "report": ["this student is studious", "the student is smart"], "student_id": [1, 2], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process reports with their student IDs

`zip(student_id,report)` pairs corresponding entries. For each pair `(sid,r)`, local score `t` begins at zero.

`r.split()` separates the report at spaces. The input guarantees one space between consecutive lowercase words, so each resulting token is exactly one feedback word.

Every occurrence is scored. If a positive word appears twice, it contributes six total points; feedback is based on word occurrences, not merely the set of words used in the report.

After the complete report, `(t,sid)` is appended to `arr`.

Student IDs are unique, so every report corresponds to a distinct ranking entry.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `zip(student_id,report)` pairs corresponding entries.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why unknown words contribute zero

Reports may contain ordinary words absent from both feedback lists, such as `"this"` or `"student"`. The source has no final `else` update, so these words leave `t` unchanged, exactly matching the scoring rules.

No stemming, punctuation removal, or case conversion is needed because the input already consists of lowercase words separated cleanly by spaces.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"positive_feedback": ["smart", "brilliant", "studious"], "negative_feedback": ["not"], "report": ["this student is studious", "the student is smart"], "student_id": [1, 2], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One weight dictionary:** Map positive words to:** - **One weight dictionary:** Map positive words to 3 and negative words to $-1$, then use a default zero lookup.
- **Size-`k` heap:** It can avoid sorting all students when `k` is much smaller than `n`, but tie ordering must be encoded carefully.
- **Repeated feedback word:** Score every occurrence, not only the first.
- **Neutral word:** It contributes zero.
- **Equal scores:** Lower student ID ranks higher.
- **Negative total score:** It is valid and sorts below larger scores.
- **`k=n`:** Return every ID in full ranking order.
- **Unique IDs:** They eliminate a remaining sort tie.
- **Disjoint vocabularies:** The `if/elif` precedence never faces a contradictory word.
- **Report splitting:** The single-space guarantee makes tokens exact.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(F+R+n\log n)$. Let $F$ be the total size of the two feedback vocabularies, measured by their words or total characters, and let $R$ be the total number of words or characters across all reports.
- **Auxiliary Space Complexity:** $O(F + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
