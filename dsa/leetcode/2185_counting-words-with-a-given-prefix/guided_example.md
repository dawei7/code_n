# Guided Example: Counting Words With a Given Prefix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["pay", "attention", "practice", "attend"], "pref": "at"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `words` and a string `pref`.

The objective is to compute `2` from `{"words": ["pay", "attention", "practice", "attend"], "pref": "at"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What “prefix” requires

For `pref` of length $p$ to be a prefix of word `w`, two conditions must hold:

- `w` must contain at least $p$ characters;
- for every index $q$ from zero through $p-1$, `w[q] == pref[q]`.

The matching characters must begin at index zero. Finding `pref` later inside the word does not qualify.

For example, `"attention"` starts with `"at"`, while `"practice"` does not. A word such as `"format"` contains `"at"` near its end but still fails the prefix test.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["pay", "attention", "practice", "attend"], "pref": "at"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Delegate the character comparison to `startswith`

`w.startswith(pref)` returns true exactly when `pref` matches the leading characters of `w`. If `w` is shorter, it safely returns false rather than indexing beyond the word.

The built-in operation compares only as far as necessary. It can stop at the first mismatching character. In the worst case—when the whole prefix matches or the mismatch is at the end—it examines all $p$ prefix characters.

Using the built-in avoids manual boundary checks and makes the code's intent explicit. It does not change the fundamental work: prefix characters still have to be compared.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `w.startswith(pref)` returns true exactly when `pref` matche... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate one result per input word

The expression `(w.startswith(pref) for w in words)` is a generator. It obtains words one at a time and yields a boolean for each.

It does not build a list of all booleans. This keeps the extra memory constant while `sum` consumes the results.

Every word occurrence is evaluated separately. If the same matching string appears twice in `words`, both occurrences contribute because the task counts strings in the array, not distinct string values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["pay", "attention", "practice", "attend"], "pref": "at"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Manual two-pointer comparison:** Check length :** - **Manual two-pointer comparison:** Check length and compare characters from index zero. It has the same complexity but requires more code and boundary handling.
- **Slice then compare:** `w[:len(pref)] == pref` is concise, but slicing may allocate a temporary substring for every word.
- **Trie:** Build prefix counts when many queries reuse the same words. For one query, its construction and memory are unnecessary.
- **Hash prefixes:** Hashing can help repeated queries but introduces collision considerations and preprocessing.
- **Word shorter than prefix:** `startswith` returns false safely.
- **Word equal to prefix:** The entire word is a valid leading substring, so it counts.
- **Prefix appears only later:** The word does not count because matching must begin at index zero.
- **Duplicate words:** Every array occurrence is counted independently.
- **No matches:** Every boolean is false and `sum` returns zero.
- **All words match:** Each contributes one, so the answer equals `len(words)`.
- **One-character prefix:** Only the first character of each nonempty word needs comparison.
- **Nonempty guarantee:** Both words and `pref` have positive length, so empty-prefix semantics do not arise.
- **Lowercase alphabet:** Comparison is direct and case-sensitive; no normalization is needed.
- **Generator memory:** Results are consumed lazily instead of stored in a boolean list.
- **Input preservation:** Strings are immutable and the word array is read only.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. With $C$ defined above, total time is $O(C)$. Equivalently, it is $O(np)$ when $n$ is the number of words and $p$ is the prefix length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
