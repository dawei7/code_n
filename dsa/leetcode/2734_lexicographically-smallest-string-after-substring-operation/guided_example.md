# Guided Example: Lexicographically Smallest String After Substring Operation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cbabc"}`
- **Required output:** `"baabc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` consisting of lowercase English letters. Perform the following operation:

The objective is to compute `"baabc"` from `{"s": "cbabc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Lexicographic order is decided at the first changed position

One nonempty substring must be transformed. Every selected non-`'a'` letter decreases by one, which makes the string smaller at that position. A selected `'a'` wraps to `'z'`, which makes the string larger at that position.

When comparing candidate results, the earliest position where they differ from the original dominates every later change. This observation determines both where the chosen substring should begin and where it should end.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cbabc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Never begin inside the leading block of a characters

Suppose `s` begins with one or more `'a'` characters and later contains a non-`'a'`. Selecting any leading `'a'` changes it to `'z'`. At the first selected leading position, the candidate becomes larger than the original and larger than a candidate that leaves the prefix unchanged and decreases the later non-`'a'`.

Therefore the code advances `i` while `s[i] == "a"`. The optimal operation must skip this entire leading block when a reducible character exists later.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose `s` begins with one or more `'a'` characters and lat... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start at the first non-a character

At the first non-`'a'` index `i`, decrementing the letter makes it strictly smaller. Starting after `i` would leave this position unchanged, so a substring starting at `i` wins lexicographically at the earliest differing position.

Starting before `i` would include a leading `'a'` and change that earlier character to `'z'`, which is worse. Thus `i` is the uniquely optimal start position whenever the string is not all `'a'`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"baabc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cbabc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"baabc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every substring:** There are $O(n^2)$ choi:** - **Try every substring:** There are $O(n^2)$ choices and comparing or constructing each result is far slower than the greedy boundary proof.
- **Decrement the whole string:** Incorrect when an `'a'` appears after a useful block because wrapping it to `'z'` worsens the first such position.
- **Skip only one leading a:** Incorrect when the leading run contains several `'a'` characters; all must remain unchanged if a later non-`'a'` exists.
- **All a characters:** Change only the last one to `'z'` because an operation is mandatory.
- **No leading a:** Start at index zero for the earliest possible improvement.
- **No later a:** Decrement from the first non-`'a'` through the end.
- **Single non-a character:** It is decremented and forms a legal one-character substring.
- **Single-character `"a"`:** The all-a branch returns `"z"`.
- **Single-character non-a:** It is replaced by its predecessor.
- **Contiguity:** Stopping at the first interior `'a'` is required; the operation cannot skip it and resume later.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. The scan for `i` and the scan for `j` together visit at most $n$ characters. Building the decremented middle and concatenating the returned string also process $O(n)$ characters. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
