# Guided Example: Remove All Occurrences of a Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "daabcbaabcbc", "part": "abc"}`
- **Required output:** `"dab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `part`, perform the following operation on `s` until **all** occurrences of the substring `part` are removed:

The objective is to compute `"dab"` from `{"s": "daabcbaabcbc", "part": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

**Follow the operation exactly.** The statement repeatedly removes the leftmost occurrence of `part` from the current string. The loop condition `while part in s` asks whether at least one occurrence remains. `s.replace(part, '', 1)` then replaces only the first occurrence with the empty string, which is precisely deletion of the current leftmost match.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "daabcbaabcbc", "part": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The third argument `1` is essential. Without it, `replace` would remove every nonoverlapping occurrence simultaneously, which can differ from the required sequence when one deletion creates a new occurrence across the joined boundary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Recheck the entire new string after every deletion.** Removing a middle block brings the prefix before that block next to the suffix after it. Characters from opposite sides can now combine into a fresh `part` occurrence that did not exist previously. Assigning the rebuilt string back to `s` and repeating the membership test ensures these newly formed matches are discovered.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "daabcbaabcbc", "part": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Stack with suffix comparison:** Append characters and remove the last $M$ when the stack suffix equals `part`. It handles newly formed boundaries naturally but can still spend $O(M)$ per character without optimized matching.
- **KMP state plus stack:** Track prefix-function match lengths alongside output characters. This achieves the manifest's $O(N+M)$ time and $O(N+M)$ space.
- **Remove all matches at once:** `replace(part, '')` without count one does not necessarily follow the mandated leftmost step sequence when deletions create new matches.
- **`part` equals `s`:** One iteration removes the whole string and returns empty.
- **No occurrence:** The loop never runs and the original string value is returned.
- **Overlapping appearances:** Only the current leftmost full occurrence is removed; the next membership test evaluates overlap effects in the shortened string.
- **Pattern longer than source:** Membership is false immediately.
- **Single-character pattern:** Every matching character is removed one iteration at a time, exposing the quadratic rebuilding behavior.
- **Nonempty pattern guarantee:** Termination relies on every iteration shortening the string. An empty pattern would invalidate that reasoning but is excluded.
- **Exact leftmost semantics:** Python's `replace(part, '', 1)` removes only the first occurrence in reading order, matching one mandated deletion before the loop searches the newly shortened string again.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + M)$. Let $N$ be the initial length of `s` and $M$ the length of `part`. There can be $O(N/M)$ successful iterations. Each membership test and one-occurrence replacement may scan a string of length $O(N)$, and replacement copies the surviving characters. A safe high-level bound for this exact repeated-string implementation is $O(N^2)$ time in the worst case, such as removing a one-character pattern many times.
- **Auxiliary Space Complexity:** $O(N + M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
